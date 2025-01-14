<?php


namespace App\Services;

class ClaimsStatsService  extends BaseHttpService {
  /**
     * Get the total number of claims.
     */
    public function getTotalClaims(): array
    {
       return [];
    }

    /**
     * Get the total number of approved claims.
     */
    public function getApprovedClaims(): array
    {
       return [];
    }

    /**
     * Get the total number of rejected claims.
     */
    public function getRejectedClaims(): array
    {
       return [];
    }

    /**
     * Get claims grouped by policy type.
     */
    public function getClaimsByPolicyType(): array
    {
       return [];
    }

    /**
     * Get claims grouped by benefit type.
     */
    public function getClaimsByBenefitType(): array
    {
       return [];
    }

    /**
     * Get claims data over specific time periods.
     */
    public function getClaimsOverTimePeriod(string $timePeriod): array
    {
       return [];
    }

    /**
     * Get the number of claims filed daily.
     */
    public function getDailyClaims(): array
    {
       return [];
    }

    /**
     * Get the number of claims filed weekly.
     */
    public function getWeeklyClaims(): array
    {
       return [];
    }

    /**
     * Get the number of claims filed monthly.
     */
    public function getMonthlyClaims(): array
    {
       return [];
    }
}
