<?php

use PHPUnit\Framework\TestCase;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpKernel\Event\ResponseEvent;
use Symfony\Component\Cache\Adapter\FilesystemAdapter;
use Psr\Cache\CacheItemInterface;

class KernelResponseListenerTest extends TestCase
{
    private $listener;
    private $licenceChecker;
    private $parameterBag;

    protected function setUp(): void
    {
        $this->licenceChecker = $this->createMock(stdClass::class);
        $this->parameterBag = $this->createMock(stdClass::class);
        $this->listener = new class($this->licenceChecker, $this->parameterBag) {
            private $licenceChecker;
            private $parameterBag;

            public function __construct($licenceChecker, $parameterBag)
            {
                $this->licenceChecker = $licenceChecker;
                $this->parameterBag = $parameterBag;
            }

            public function onKernelResponse($event): void
            {
                $response = $event->getResponse();
                $route = $event->getRequest()->attributes->get('_route');

                if (!$response instanceof Response
                    || !str_contains($response->headers->get('Content-Type'), 'text/html')
                    || ($route && str_contains($event->getRequest()->attributes->get('_route'), 'installation'))
                ) {
                    return;
                }

                $cache = new FilesystemAdapter();
                $checkCount = $cache->getItem('licence.check_count');
                if (!$checkCount->isHit()) {
                    $checkCount->set(0);
                    $checkCount->expiresAfter(60);
                    $cache->save($checkCount);
                }

                $counter = $checkCount->get();
                $checkCount->set(++$counter);
                $cache->save($checkCount);

                $licenceKey = $this->parameterBag->get('fastfony_licence.key');

                if ($counter > 20 && (empty($licenceKey) || !$this->licenceChecker->isValid($licenceKey))) {
                    $content = $response->getContent();
                    $script = "<script>document.addEventListener('DOMContentLoaded', function(){let o=document.createElement('div');o.style.position='fixed';o.style.top='0';o.style.left='0';o.style.width='100%';o.style.height='100%';o.style.backgroundColor='darkred';o.style.color='yellow';o.style.fontSize='3rem';o.style.display='flex';o.style.flexDirection='column';o.style.justifyContent='center';o.style.alignItems='center';o.style.zIndex='99999';o.innerHTML='<h2>Invalid Fastfony licence key.</h2><p class=\"fs-sm\">Edit <a href=\"/admin/parameters\" class=\"underline\">here</a>.</p>';document.body.appendChild(o);});</script>";
                    $content = str_replace('</body>', $script . '</body>', $content);
                    $response->setContent($content);
                }
            }
        };
    }

    public function testNonHtmlResponse(): void
    {
        $request = new Request([], [], ['_route' => 'homepage']);
        $response = new Response('', 200, ['Content-Type' => 'application/json']);
        $event = new ResponseEvent(
            $this->createMock(Symfony\Component\HttpKernel\HttpKernelInterface::class),
            $request,
            Symfony\Component\HttpKernel\KernelEvents::RESPONSE,
            $response
        );

        $this->listener->onKernelResponse($event);
        $this->assertStringNotContainsString('Invalid Fastfony licence key.', $response->getContent());
    }
}