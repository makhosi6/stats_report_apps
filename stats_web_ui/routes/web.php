<?php

use App\DTO\PolicyDTO;
use App\Http\Controllers;
use App\Http\Controllers\BenefitStatsController;
use App\Providers\ClaimsStatsServiceProvider;
use App\Services\BenefitStatsService;
use App\Services\ClaimsStatsService;
use App\Services\PolicyStatsService;
use Illuminate\Foundation\Application;
use Illuminate\Support\Facades\Route;
use Inertia\Inertia;

Route::get('/', function () {
    return Inertia::render('Welcome', [
        'canLogin' => Route::has('login'),
        'canRegister' => Route::has('register'),
        'laravelVersion' => Application::VERSION,
        'phpVersion' => PHP_VERSION,
    ]);
});

Route::middleware([
    'auth:sanctum',
    config('jetstream.auth_session'),
    'verified',
])->group(function () {
    Route::get('/dashboard', function () {
        return Inertia::render('Dashboard', [
            "stats" => [
                /// benefits
                "totalBenefits" => app(BenefitStatsService::class)->getTotalBenefits(),
                "totalBenefitsForTimeRange" => app(BenefitStatsService::class)->getTotalBenefitsForTimeRange([]),
                "averageBenefitsPerPolicy" => app(BenefitStatsService::class)->getAverageBenefitsPerPolicy(),
                "benefitsByPolicyType" => app(BenefitStatsService::class)->getBenefitsByPolicyType(),
                "mostCommonBenefits" => app(BenefitStatsService::class)->getMostCommonBenefits(),
                "dailyBenefits" => app(BenefitStatsService::class)->getDailyBenefits(),
                "weeklyBenefits" => app(BenefitStatsService::class)->getWeeklyBenefits(),
                "monthlyBenefits" => app(BenefitStatsService::class)->getMonthlyBenefits(),

                /// claims
                "totalClaims" => app(ClaimsStatsService::class)->getTotalClaims(),
                "approvedClaims" => app(ClaimsStatsService::class)->getApprovedClaims(),
                "rejectedClaims" => app(ClaimsStatsService::class)->getRejectedClaims(),
                "claimsByPolicyType" => app(ClaimsStatsService::class)->getClaimsByPolicyType(),
                "claimsByBenefitType" => app(ClaimsStatsService::class)->getClaimsByBenefitType(),
                "claimsOverTimePeriod" => app(ClaimsStatsService::class)->getClaimsOverTimePeriod([]),
                "weeklyClaims" => app(ClaimsStatsService::class)->getWeeklyClaims(),
                "dailyClaims" => app(ClaimsStatsService::class)->getDailyClaims(),
                "monthlyClaims" => app(ClaimsStatsService::class)->getMonthlyClaims(),

                /// policies
                "policiesBySpecificBranch" => app(PolicyStatsService::class)->getPoliciesBySpecificBranch('Johannesburg'),
                "policiesForTimeRange" => app(PolicyStatsService::class)->getTotalPoliciesForTimeRange([]),
                "totalPolicies" => app(PolicyStatsService::class)->getTotalPolicies(),
                "averageBenefitsPerPolicy" => app(PolicyStatsService::class)->getAverageBenefitsPerPolicy(),
                "policiesByBranch" => app(PolicyStatsService::class)->getPoliciesByBranch(),
                "claimsByPolicyType" => app(PolicyStatsService::class)->getClaimsByPolicyType([]),
                "monthlyPolicies" => app(PolicyStatsService::class)->getMonthlyPolicies(),
                "weeklyPolicies" => app(PolicyStatsService::class)->getWeeklyPolicies(),
                "dailyPolicies" => app(PolicyStatsService::class)->getDailyPolicies(),
                "policiesByPremium" => app(PolicyStatsService::class)->getPoliciesByPremium(),
                "totalPoliciesForTimeRange" => app(PolicyStatsService::class)->getTotalPoliciesForTimeRange([]),
                "policiesByType" => app(PolicyStatsService::class)->getPoliciesByType(),
                "cancelledPolicies" => app(PolicyStatsService::class)->getCancelledPolicies(),
                "reinstatedPolicies" => app(PolicyStatsService::class)->getReinstatedPolicies(),
            ]
        ]);
    })->name('dashboard');
});
