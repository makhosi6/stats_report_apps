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
                "mostCommonBenefits" => app(BenefitStatsService::class)->getMostCommonBenefits(),
                "monthlyBenefits" => app(BenefitStatsService::class)->getMonthlyBenefits(),
                "totalBenefitsForTimeRange" => app(BenefitStatsService::class)->getTotalBenefitsForTimeRange([
                    'start_date' => '2024-01-01',
                    'end_date'   => '2025-03-03'
                ]),

                /// claims
                "claimsOverTimePeriod" => app(ClaimsStatsService::class)->getClaimsOverTimePeriod([
                    'start_date' => '2024-01-01',
                    'end_date'   => '2025-03-03'
                ]),
                "monthlyClaims" => app(ClaimsStatsService::class)->getMonthlyClaims(),
                "totalClaims" => app(ClaimsStatsService::class)->getTotalClaims(),
                "monthlyClaims" => app(ClaimsStatsService::class)->getMonthlyClaims(),

                /// policies
                "policiesBySpecificBranch" => app(PolicyStatsService::class)->getPoliciesBySpecificBranch('Johannesburg'),
                "policiesForTimeRange" => app(PolicyStatsService::class)->getTotalPoliciesForTimeRange([
                    'start_date' => '2024-01-01',
                    'end_date'   => '2025-03-03'
                ]),
                "totalPolicies" => app(PolicyStatsService::class)->getTotalPolicies(),
                "averageBenefitsPerPolicy" => app(PolicyStatsService::class)->getAverageBenefitsPerPolicy(),
                "policiesByBranch" => app(PolicyStatsService::class)->getPoliciesByBranch(),
                "claimsByPolicyType" => app(PolicyStatsService::class)->getClaimsByPolicyType([
                    'start_date' => '2024-01-01',
                    'end_date'   => '2025-03-03'
                ]),
                "monthlyPolicies" => app(PolicyStatsService::class)->getMonthlyPolicies(),
            ]
        ]);
    })->name('dashboard');
});
