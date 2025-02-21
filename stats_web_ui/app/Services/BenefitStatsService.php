<?php


namespace App\Services;

use Illuminate\Http\Client\Response;

class BenefitStatsService extends BaseHttpService {

    function http_get(string $path, array | null $data): Response
    {
        $api_base_url = env('API_BASE_URL', 'http://localhost:5050/api/stats/');
        return parent::http_get($api_base_url . $path, $data);
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
    public function getTotalBenefitsForTimeRange($timePeriod): array
    {
       return $this->http_get('benefits/time-period', ['range' => $timePeriod])->json();
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

