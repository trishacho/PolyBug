public function testCheckIncludesValidation()
{
    // Test cases: [input, allowedIncludes, expectedError (null if valid)]
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
        
        // Mock the request
        $request = Request::create('/', 'GET', ['include' => $input]);
        $this->app->instance('request', $request);
        
        // Create test double of the class
        $testClass = new class($allowedIncludes) {
            public $allowedIncludes;
            
            public function __construct($allowedIncludes) {
                $this->allowedIncludes = $allowedIncludes;
            }
            
            public function checkIncludes() {
                // This is the method we're testing - will be replaced by patched versions
                $include = collect(explode(',', request()->get('include', false)))
                    ->map(function($item) {
                        [$item] = explode(':', $item);
                        return $item;
                    })
                    ->implode(',');
                
                if ($include && $diff = array_diff(explode(',', $include), $this->allowedIncludes)) {
                    $this->forbiddenResponse(
                        "The following includes are not allowed: '".implode(',', $diff).
                        "', enabled: '".implode(',', $this->allowedIncludes)."'"
                    );
                    return false;
                }
                return true;
            }
            
            public function forbiddenResponse($message) {
                throw new \Exception($message);
            }
        };

        try {
            $result = $testClass->checkIncludes();
            $this->assertTrue($result, "Case with input '{$input}' should pass validation");
            $this->assertNull($expectedError, "Case with input '{$input}' should fail but passed");
        } catch (\Exception $e) {
            $this->assertNotNull($expectedError, "Case with input '{$input}' failed unexpectedly: ".$e->getMessage());
            $this->assertEquals($expectedError, $e->getMessage());
        }
    }
}