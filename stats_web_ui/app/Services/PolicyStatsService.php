<?php


namespace App\Services;

class PolicyStatsService  extends BaseHttpService
{
    /**
     * Get the total number of policies.
     */
    public function getTotalPolicies(): int
    {
        return 0;
    }
    /**
     * Get the total number of cancelled policies.
     */
    public function getCancelledPolicies(): array
    {
      return [];
    }

    /**
     * Get the total number of reinstated policies.
     */
    public function getReinstatedPolicies(): array
    {
      return [];
    }

    /**
     * Get policies grouped by type.
     */
    public function getPoliciesByType(): array
    {
      return [];
    }

    /**
     * Get policies grouped by premium ranges.
     */
    public function getPoliciesByPremium(): array
    {
      return [];
    }

    /**
     * Get policies created daily. For the last 30days
     */
    public function getDailyPolicies(): array
    {
      return [];
    }

    /**
     * Get policies created weekly. for the last 4weeks
     */
    public function getWeeklyPolicies(): array
    {
      return [];
    }

    /**
     * Get policies created monthly. For the last 12 months
     */
    public function getMonthlyPolicies(): array
    {
      return [];
    }

    /**
     * Get policies grouped by branch. Get array of objects for all branches
     */
    public function getPoliciesByBranch(): array
    {
      return [];
    }

    /**
     * Get policies for a specific branch.
     */
    public function getPoliciesBySpecificBranch(string $branch): array
    {
      return [];
    }

    /**
     * Get the total number of benefits across all policies.
     */
    public function getTotalBenefits(): int
    {
        return 0;
    }

    /**
     * Get the average number of benefits per policy.
     */
    public function getAverageBenefitsPerPolicy(): float
    {
        return 0.0;
    }

    /**
     * Get benefits grouped by policy type.
     */
    public function getBenefitsByPolicyType(): array
    {
      return [];
    }

    /**
     * Get the most common benefits.
     */
    public function getMostCommonBenefits(): array
    {
      return [];
    }

    /**
     * Get the total number of claims.
     */
    public function getTotalClaims(): int
    {
        return 0;
    }

    /**
     * Get claims grouped by policy type.
     */
    public function getClaimsByPolicyType(): array
    {
        return [];
    }
}
