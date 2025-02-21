<?php

namespace App\Http\Controllers;

use App\Services\ClaimsStatsService;

class ClaimStatsController extends Controller
{
    public function getTotalClaims(): array
    {
        $stats_service = app(ClaimsStatsService::class);
        return $stats_service->getTotalClaims();
    }


    public function getApprovedClaims(): array
    {
        $stats_service = app(ClaimsStatsService::class);
        return $stats_service->getApprovedClaims();
    }


    public function getRejectedClaims(): array
    {
        $stats_service = app(ClaimsStatsService::class);
        return $stats_service->getRejectedClaims();
    }


    public function getClaimsByPolicyType(): array
    {
        $stats_service = app(ClaimsStatsService::class);
        return $stats_service->getClaimsByPolicyType();
    }

    public function getClaimsByBenefitType(): array
    {
        $stats_service = app(ClaimsStatsService::class);
        return $stats_service->getClaimsByBenefitType();
    }


    public function getClaimsOverTimePeriod(string $timePeriod): array
    {
        $stats_service = app(ClaimsStatsService::class);
        return $stats_service->getClaimsOverTimePeriod($timePeriod);
    }


    public function getDailyClaims(): array
    {
        $stats_service = app(ClaimsStatsService::class);
        return $stats_service->getDailyClaims();
    }


    public function getWeeklyClaims(): array
    {
        $stats_service = app(ClaimsStatsService::class);
        return $stats_service->getWeeklyClaims();
    }


    public function getMonthlyClaims(): array
    {
        $stats_service = app(ClaimsStatsService::class);
        return $stats_service->getMonthlyClaims();
    }
}

