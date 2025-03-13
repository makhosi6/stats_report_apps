<?php


namespace App\Services;

use App\Stats\Services\BaseHttpService;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;

class ClaimsStatsService
{

    function http_get(string $path, array | null $data)
    {
        try {
            $api_base_url = env('API_BASE_URL', 'http://localhost:5050/api/stats/');
            $default_get_params = [
                'start_date' => date('Y-m-d', strtotime('-12 months')),
                'end_date' => date('Y-m-d'),
                'offset' => 15
            ];
            return Http::withHeaders([
                'Authorization' => 'Bearer ' . md5(Auth::user()->email)
            ])->get(
                $api_base_url . $path,
                array_merge($default_get_params, $data),
            );
        } catch (\Throwable $th) {
            Log::error("Error at claims stats http_get", ["Error" => $th->getTraceAsString()]);
            throw new \Exception($th->getMessage());
        }
    }
    /**
     * Get the total number of claims.
     */
    public function getTotalClaims(): array
    {
        return $this->http_get('claims/total', [
            "offset" => 100
        ])->json();
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
        return $this->http_get('claims/bytype', [])->json();
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
    public function getClaimsOverTimePeriod($reqParams): array
    {
        return $this->http_get('claims/time-period', $reqParams)->json();
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
        return $this->http_get('claims/monthly', [])->json();
    }
}
