<?php

use PHPUnit\Framework\TestCase;

// Include the class we're testing
require_once __DIR__ . '/../src/IncludeValidator.php';

class IncludeValidatorTest extends TestCase
{
    public function testCheckIncludesValidation()
    {
        $testCases = [
            // Valid cases
            ['foo,bar', ['foo', 'bar'], null],
            ['foo:limit(5),bar', ['foo', 'bar'], null],
            ['', ['foo', 'bar'], null],
            [null, ['foo', 'bar'], null],
            [false, ['foo', 'bar'], null],

            // Invalid cases
            [
                'baz,qux', 
                ['foo', 'bar'], 
                "The following includes are not allowed: 'baz,qux', enabled: 'foo,bar'"
            ],
            [
                'foo,baz', 
                ['foo', 'bar'], 
                "The following includes are not allowed: 'baz', enabled: 'foo,bar'"
            ],
            [
                'foo:limit(5),baz', 
                ['foo', 'bar'], 
                "The following includes are not allowed: 'baz', enabled: 'foo,bar'"
            ],
        ];

        foreach ($testCases as $case) {
            [$input, $allowedIncludes, $expectedError] = $case;
            
            $validator = new IncludeValidator($allowedIncludes, $input);

            try {
                $result = $validator->checkIncludes();
                $this->assertTrue($result, "Case with input '{$input}' should pass validation");
                $this->assertNull($expectedError, "Case with input '{$input}' should fail but passed");
            } catch (\Exception $e) {
                $this->assertNotNull($expectedError, "Case with input '{$input}' failed unexpectedly: ".$e->getMessage());
                $this->assertEquals($expectedError, $e->getMessage());
            }
        }
    }
}