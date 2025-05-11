<?php
use PHPUnit\Framework\TestCase;

class PasswordFormTest extends TestCase
{
    protected function setUp(): void
    {
        $_SESSION = [];
        $_GET = [];
    }

    public function testShortPasswordLength()
    {
        $_GET['long'] = 3;
        include __DIR__ . '/../password_form.php';

        $this->assertEquals('la password deve essere almeno di 5 caratteri', $_error);
        $this->assertEquals(3, $_SESSION['short']);
    }

    public function testNoConditionsSelected()
    {
        $_GET['long'] = 8;
        $_GET['upper'] = 'off';
        $_GET['lower'] = 'off';
        $_GET['number'] = 'off';
        $_GET['symbol'] = 'off';

        include __DIR__ . '/../password_form.php';

        $this->assertEquals('Seleziona almeno una condizione', $errorConditions);
    }

    public function testValidSubmissionRedirect()
    {
        $_GET['long'] = 8;
        $_GET['upper'] = 'on';
        $_GET['lower'] = 'off';
        $_GET['number'] = 'off';
        $_GET['symbol'] = 'off';

        $this->expectOutputString(''); // Suppress output from include
        @include __DIR__ . '/../password_form.php';

        // Since header() does not execute in CLI mode, we assume it was reached if no error message was set
        $this->assertFalse($errorConditions);
    }
}
?>
