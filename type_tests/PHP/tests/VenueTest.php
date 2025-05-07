<?php

use PHPUnit\Framework\TestCase;

// Include the class we're testing
require_once __DIR__ . '/../src/Venue.php';

class VenueTest extends TestCase
{
    public function testGetVenueReturnsArray()
    {
        $venue = new Venue();
        $venueId = 123;
        
        $result = $venue->getVenue($venueId);
        $this->assertIsArray($result);
    }

    public function testGetVenueReturnsEmptyArrayWhenNull()
    {
        $venue = new Venue();
        $venueId = 999;
        
        $result = $venue->getVenue($venueId);
        $this->assertEmpty($result);
    }
}