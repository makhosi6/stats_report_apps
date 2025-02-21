<?php

namespace App\Http\Controllers;

use App\Services\BenefitStatsService;

class BenefitStatsController extends Controller
{
    //
    public function totalBenefits()
    {
        $stats_service = app(BenefitStatsService::class);
        return $stats_service->getTotalBenefits();
    }

    public function benefitsTimePeriod(string $timePeriod)
    {
        $stats_service = app(BenefitStatsService::class);
        return $stats_service->getTotalBenefitsForTimeRange($timePeriod);
    }

    public function averageBenefitsPerPolicy()
    {
        $stats_service = app(BenefitStatsService::class);
        return $stats_service->getAverageBenefitsPerPolicy();
    }

    public function benefitsByPolicyType()
    {
        $stats_service = app(BenefitStatsService::class);
        return $stats_service->getBenefitsByPolicyType();
    }

    public function mostCommonBenefits()
    {
        $stats_service = app(BenefitStatsService::class);
        return $stats_service->getMostCommonBenefits();
    }

    public function benefitsCreatedDaily()
    {
        $stats_service = app(BenefitStatsService::class);
        return $stats_service->getDailyBenefits();
    }

    public function benefitsCreatedWeekly()
    {
        $stats_service = app(BenefitStatsService::class);
        return $stats_service->getWeeklyBenefits();
    }

    public function benefitsCreatedMonthly()
    {
        $stats_service = app(BenefitStatsService::class);
        return $stats_service->getMonthlyBenefits();
    }
}
