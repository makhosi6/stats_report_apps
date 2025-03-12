<?php


namespace App\Services;

use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;

class BenefitStatsService {

    function http_get(string $path, array | null $data)
    {
        try {
            $api_base_url = env('API_BASE_URL', 'http://localhost:5050/api/stats/');
            return Http::get($api_base_url . $path, $data);
        } catch (\Throwable $th) {
            Log::error("Error at policy stats http_get", ["Error" => $th->getTraceAsString()]);
            throw new \Exception($th->getMessage());
            // return (object) [
            //     "error" => $th->getTraceAsString()
            // ];
        }
    }
    /**
     * Get the total number of benefits across all policies.
     */
    public function getTotalBenefits(): array
    {
       return $this->http_get('benefits/total', [])->json();
    }
    /**
     * Get the total number of benefits across all policies for a give period.
     */
    public function getTotalBenefitsForTimeRange($reqParams): array
    {
       return $this->http_get('benefits/time-period', $reqParams)->json();
    }

    /**
     * Get the average number of benefits per policy.
     */
    public function getAverageBenefitsPerPolicy(): array
    {
       return $this->http_get('benefits/average-per-policy', [])->json();
    }

    /**
     * Get benefits grouped by policy type.
     */
    public function getBenefitsByPolicyType(): array
    {
       return $this->http_get('benefits/by-policy-type', [])->json();
    }

    /**
     * Get the most common benefits across policies.
     */
    public function getMostCommonBenefits(): array
    {
        return $this->http_get('benefits/most-common', [])->json();
    }
    /**
     * Get benefits created daily.
     */
    public function getDailyBenefits(): array
    {
       return $this->http_get('benefits/created-daily', [])->json();
    }

    /**
     * Get benefits created weekly.
     */
    public function getWeeklyBenefits(): array
    {
       return $this->http_get('benefits/created-weekly', [])->json();
    }

    /**
     * Get benefits created monthly.
     */
    public function getMonthlyBenefits(): array
    {
       return $this->http_get('benefits/created-monthly', [])->json();
    }
}

