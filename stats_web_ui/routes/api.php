<?php

use App\Http\Controllers\BenefitStatsController;
use App\Http\Controllers\ClaimStatsController;
use App\Http\Controllers\PolicyStatsController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');


Route::middleware([
    'auth:sanctum',
])->group(function () {

    // Policies
    Route::get('/api/stats/policies/total', [PolicyStatsController::class, 'totalPolicies'])->name('policies.total');
    Route::get('/api/stats/policies/cancelled', [PolicyStatsController::class, 'cancelledPolicies'])->name('policies.cancelled');
    Route::get('/api/stats/policies/reinstated', [PolicyStatsController::class, 'reinstatedPolicies'])->name('policies.by-type');
    Route::get('/api/stats/policies/by-type', [PolicyStatsController::class, 'policiesByType'])->name('policies.by-type');
    Route::get('/api/stats/policies/time-period', [PolicyStatsController::class, 'policiesTimePeriod'])->name('policies.time-period');
    Route::get('/api/stats/policies/by-premium', [PolicyStatsController::class, 'policiesByPremium'])->name('policies.by-premium');
    Route::get('/api/stats/policies/created-daily', [PolicyStatsController::class, 'policiesCreatedDaily'])->name('policies.created-daily');
    Route::get('/api/stats/policies/created-weekly', [PolicyStatsController::class, 'policiesCreatedWeekly'])->name('policies.created-weekly');
    Route::get('/api/stats/policies/created-monthly', [PolicyStatsController::class, 'policiesCreatedMonthly'])->name('policies.created-monthly');
    Route::get('/api/stats/policies/by-branch', [PolicyStatsController::class, 'policiesByBranch'])->name('policies.by-branch');
    Route::get('/api/stats/policies/branch/{branch}', [PolicyStatsController::class, 'policiesForBranch'])->name('policies.branch.');

    // // Benefits
    Route::get('/api/stats/benefits/total', [BenefitStatsController::class, 'totalBenefits'])->name('benefits.total');
    Route::get('/api/stats/benefits/time-period', [BenefitStatsController::class, 'benefitsTimePeriod'])->name('benefits.time-period');
    Route::get('/api/stats/benefits/average-per-policy', [BenefitStatsController::class, 'averageBenefitsPerPolicy'])->name('benefits.average-per-policy');
    Route::get('/api/stats/benefits/by-policy-type', [BenefitStatsController::class, 'benefitsByPolicyType'])->name('benefits.by-policy-type');
    Route::get('/api/stats/benefits/most-common', [BenefitStatsController::class, 'mostCommonBenefits'])->name('benefits.most-common');
    Route::get('/api/stats/benefits/created-daily', [BenefitStatsController::class, 'benefitsCreatedDaily'])->name('benefits.created-daily');
    Route::get('/api/stats/benefits/created-weekly', [BenefitStatsController::class, 'benefitsCreatedWeekly'])->name('benefits.created-weekly');
    Route::get('/api/stats/benefits/created-monthly', [BenefitStatsController::class, 'benefitsCreatedMonthly'])->name('benefits.created-monthly');

    // Claims
    Route::get('/api/stats/claims/total', [ClaimStatsController::class, 'totalClaims'])->name('total.claims');
    Route::get('/api/stats/claims/approved', [ClaimStatsController::class, 'approvedClaims'])->name('claims.approved');
    Route::get('/api/stats/claims/rejected', [ClaimStatsController::class, 'rejectedClaims'])->name('claims.rejected');
    Route::get('/api/stats/claims/by-policy', [ClaimStatsController::class, 'claimsByPolicy'])->name('claims.by-policy');
    Route::get('/api/stats/claims/by-benefit', [ClaimStatsController::class, 'claimsByBenefit'])->name('claims.by-benefit');
    Route::get('/api/stats/claims/time-period', [ClaimStatsController::class, 'claimsTimePeriod'])->name('claims.time-period');
    Route::get('/api/stats/claims/daily', [ClaimStatsController::class, 'claimsDaily'])->name('claims.daily');
    Route::get('/api/stats/claims/weekly', [ClaimStatsController::class, 'claimsWeekly'])->name('claims.weekly');
    Route::get('/api/stats/claims/monthly', [ClaimStatsController::class, 'claimsMonthly'])->name('claims.monthly');
});
