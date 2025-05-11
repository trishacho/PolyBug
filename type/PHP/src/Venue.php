<?php

class Venue
{
    // Dummy implementation of the curlWrap method
    private function curlWrap($method)
    {
        // Simulate a null response
        return null;
    }

    // The actual method to test
    public function getVenue($venueId): array
    {
        $method = "/v3/venues/" . $venueId . "/";
        $venue = $this->curlWrap($method);

        // Ensure it always returns an array (fixes the bug)
        return $venue;
    }
}