<?php

class IncludeValidator
{
    protected $allowedIncludes;
    protected $requestIncludes;

    public function __construct(array $allowedIncludes, $requestIncludes = null)
    {
        $this->allowedIncludes = $allowedIncludes;
        $this->requestIncludes = $requestIncludes;
    }

    public function checkIncludes()
    {
        $include = $this->requestIncludes ?? '';
        $includeParts = explode(',', $include);
        
        $cleanIncludes = array_map(function($item) {
            return explode(':', $item)[0]; // Remove modifiers like :limit(5)
        }, $includeParts);

        $diff = array_diff($cleanIncludes, $this->allowedIncludes);
        
        if (!empty($diff)) {
            $this->forbiddenResponse(
                "The following includes are not allowed: '".implode(',', $diff).
                "', enabled: '".implode(',', $this->allowedIncludes)."'"
            );
            return false;
        }
        return true;
    }

    protected function forbiddenResponse($message)
    {
        throw new \Exception($message);
    }
}