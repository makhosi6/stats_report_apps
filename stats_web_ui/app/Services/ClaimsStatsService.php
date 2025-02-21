<?php


namespace App\Services;
use Illuminate\Support\Facades\Http;
use Illuminate\Http\Client\Response;

class ClaimsStatsService {
    function http_get(string $path, array | null $data): Response
    {
        $api_base_url = env('API_BASE_URL', 'http://localhost:5050/api/stats/');
        return Http::get($api_base_url . $path, $data);
    }
  /**
     * Get the total number of claims.
     */
    public function getTotalClaims(): array
    {
       return $this->http_get('claims/total', [])->json();
    }

    /**
     * Get the total number of approved claims.
     */
    public function getApprovedClaims(): array
    {
       return $this->http_get('claims/approved', [])->json();
    }

    /**
     * Get the total number of rejected claims.
     */
    public function getRejectedClaims(): array
    {
       return $this->http_get('claims/rejected', [])->json();
    }

    /**
     * Get claims grouped by policy type.
     */
    public function getClaimsByPolicyType(): array
    {
       return $this->http_get('policies/by-type', [])->json();
    }

    /**
     * Get claims grouped by benefit type.
     */
    public function getClaimsByBenefitType(): array
    {
       return $this->http_get('claims/by-benefit', [])->json();
    }

    /**
     * Get claims data over specific time periods.
     */
    public function getClaimsOverTimePeriod(string $timePeriod): array
    {
       return $this->http_get('claims/time-period', ["range"=> $timePeriod])->json();
    }

    /**
     * Get the number of claims filed daily.
     */
    public function getDailyClaims(): array
    {
       return $this->http_get('claims/daily', [])->json();
    }

    /**
     * Get the number of claims filed weekly.
     */
    public function getWeeklyClaims(): array
    {
       return $this->http_get('claims/weekly', [])->json();
    }

    /**
     * Get the number of claims filed monthly.
     */
    public function getMonthlyClaims(): array
    {
        return $this->http_get('claims/weekly', [])->json();
    }
}
