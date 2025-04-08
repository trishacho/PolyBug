<?php

use PHPUnit\Framework\TestCase;

class VenueTest extends TestCase
{
    // Dummy implementation of the curlWrap method, simulating external request
    private function curlWrap($method)
    {
        // Simulate a null response to mimic the bug scenario
        return null;
    }

    // The function being tested (with a bug fixed)
    public function getVenue($venueId): array
    {
        $method = "/v3/venues/" . $venueId . "/";

        $venue = $this->curlWrap($method);

        // Ensure it always returns an array, even if the curlWrap returns null
        return $venue ?? [];
    }

    // Unit test to check that getVenue always returns an array
    public function testGetVenueReturnsArray()
    {
        $venueId = 123;
        
        // Call the method
        $venue = $this->getVenue($venueId);
        
        // Check that the result is always an array
        $this->assertIsArray($venue, "getVenue should always return an array.");
    }

    // Optional: Test for empty response
    public function testGetVenueReturnsEmptyArrayWhenNull()
    {
        $venueId = 999;
        
        // Call the method
        $venue = $this->getVenue($venueId);
        
        // Check if the result is an empty array when curlWrap returns null
        $this->assertEmpty($venue, "getVenue should return an empty array if no data is fetched.");
    }
}

?>
