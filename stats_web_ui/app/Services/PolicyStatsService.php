<?php


namespace App\Services;

use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;

class PolicyStatsService
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
            Log::error("Error at policy stats http_get", ["Error" => $th->getTraceAsString()]);
            throw new \Exception($th->getMessage());
        }
    }
    /**
     * Get the total number of policies.
     */
    public function getTotalPolicies(): array
    {
        return $this->http_get('policies/total', [])->json();
    }
    /**
     * Get the total number of cancelled policies.
     */
    public function getCancelledPolicies(): array
    {
        return $this->http_get('policies/cancelled', [])->json();
    }

    /**
     * Get the total number of reinstated policies.
     */
    public function getReinstatedPolicies(): array
    {
        return $this->http_get('policies/reinstated', [])->json();
    }

    /**
     * Get policies grouped by type.
     */
    public function getPoliciesByType(): array
    {
        // return $this->http_get('policies/bytype', [])->json();
        return [];
    }

    /**
     * Get policies grouped by premium ranges.
     */
    public function getPoliciesByPremium(): array
    {
        // return $this->http_get('policies/by-premium', [])->json();
        return [];
    }

    /**
     * Get policies created daily. For the last 30days
     */
    public function getDailyPolicies(): array
    {
        return $this->http_get('policies/created-daily', [])->json();
    }
    /**
     * Get the total number of policies across all policies for a give period.
     */
    public function getTotalPoliciesForTimeRange($reqParams): array
    {
        return $this->http_get('policies/time-period', $reqParams)->json();
    }
    /**
     * Get policies created weekly. for the last 4weeks
     */
    public function getWeeklyPolicies(): array
    {
        return $this->http_get('policies/created-weekly', [])->json();
    }

    /**
     * Get policies created monthly. For the last 12 months
     */
    public function getMonthlyPolicies(): array
    {
        return $this->http_get('policies/total', [])->json();
    }

    /**
     * Get policies grouped by branch. Get array of objects for all branches
     */
    public function getPoliciesByBranch(): array
    {
        return $this->http_get('policies/by-branch', [])->json();
    }

    /**
     * Get policies for a specific branch.
     */
    public function getPoliciesBySpecificBranch(string $branchName): array
    {
        return $this->http_get("policies/branch/" . $branchName, [])->json();
    }

    /**
     * Get the total number of benefits across all policies.
     */
    public function getTotalBenefits(): array
    {
        return $this->http_get('policies/total', [])->json();
    }

    /**
     * Get the average number of benefits per policy.
     */
    public function getAverageBenefitsPerPolicy()
    {
        return $this->http_get('policies/average-benefits', [])->json();
    }
    /**
     * Get claims grouped by policy type.
     */
    public function getClaimsByPolicyType($reqParams): array
    {
        // return $this->http_get('policies/bytype', $reqParams)->json();
        return ['type1' => '78'];
    }
}
