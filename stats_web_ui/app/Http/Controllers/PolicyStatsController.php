<?php

namespace App\Http\Controllers;

use App\Services\PolicyStatsService;

class PolicyStatsController extends Controller
{
    public function totalPolicies()
    {
        $stats_service = app(PolicyStatsService::class);
        return $stats_service->getTotalPolicies();
    }

    public function cancelledPolicies()
    {
        $stats_service = app(PolicyStatsService::class);
        return $stats_service->getCancelledPolicies();
    }

    public function reinstatedPolicies()
    {
        $stats_service = app(PolicyStatsService::class);
        return $stats_service->getReinstatedPolicies();
    }

    public function policiesByType()
    {
        $stats_service = app(PolicyStatsService::class);
        return $stats_service->getPoliciesByType();
    }

    public function policiesTimePeriod($timePeriod)
    {
        $stats_service = app(PolicyStatsService::class);
        return $stats_service->getTotalPoliciesForTimeRange($timePeriod);
    }

    public function policiesByPremium()
    {
        $stats_service = app(PolicyStatsService::class);
        return $stats_service->getPoliciesByPremium();
    }

    public function policiesCreatedDaily()
    {
        $stats_service = app(PolicyStatsService::class);
        return $stats_service->getDailyPolicies();
    }

    public function policiesCreatedWeekly()
    {
        $stats_service = app(PolicyStatsService::class);
        return $stats_service->getWeeklyPolicies();
    }

    public function policiesCreatedMonthly()
    {
        $stats_service = app(PolicyStatsService::class);
        return $stats_service->getMonthlyPolicies();
    }

    public function policiesByBranch()
    {
        $stats_service = app(PolicyStatsService::class);
        return $stats_service->getPoliciesByBranch();
    }

    public function policiesForBranch($branch)
    {
        $stats_service = app(PolicyStatsService::class);
        return $stats_service->getPoliciesBySpecificBranch($branch);
    }
}
