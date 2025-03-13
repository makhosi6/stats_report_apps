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
    Route::get('/stats/policies/total', [PolicyStatsController::class, 'totalPolicies'])->name('policies.total');
    Route::get('/stats/policies/cancelled', [PolicyStatsController::class, 'cancelledPolicies'])->name('policies.cancelled');
    Route::get('/stats/policies/reinstated', [PolicyStatsController::class, 'reinstatedPolicies'])->name('policies.by-type');
    Route::get('/stats/policies/by-type', [PolicyStatsController::class, 'policiesByType'])->name('policies.by-type');
    Route::get('/stats/policies/time-period', [PolicyStatsController::class, 'policiesTimePeriod'])->name('policies.time-period');
    Route::get('/stats/policies/by-premium', [PolicyStatsController::class, 'policiesByPremium'])->name('policies.by-premium');
    Route::get('/stats/policies/created-daily', [PolicyStatsController::class, 'policiesCreatedDaily'])->name('policies.created-daily');
    Route::get('/stats/policies/created-weekly', [PolicyStatsController::class, 'policiesCreatedWeekly'])->name('policies.created-weekly');
    Route::get('/stats/policies/created-monthly', [PolicyStatsController::class, 'policiesCreatedMonthly'])->name('policies.created-monthly');
    Route::get('/stats/policies/by-branch', [PolicyStatsController::class, 'policiesByBranch'])->name('policies.by-branch');
    Route::get('/stats/policies/branch/{branch}', [PolicyStatsController::class, 'policiesForBranch'])->name('policies.branch.');

    // // Benefits
    Route::get('/stats/benefits/total', [BenefitStatsController::class, 'totalBenefits'])->name('benefits.total');
    Route::get('/stats/benefits/time-period', [BenefitStatsController::class, 'benefitsTimePeriod'])->name('benefits.time-period');
    Route::get('/stats/benefits/average-per-policy', [BenefitStatsController::class, 'averageBenefitsPerPolicy'])->name('benefits.average-per-policy');
    Route::get('/stats/benefits/by-policy-type', [BenefitStatsController::class, 'benefitsByPolicyType'])->name('benefits.by-policy-type');
    Route::get('/stats/benefits/most-common', [BenefitStatsController::class, 'mostCommonBenefits'])->name('benefits.most-common');
    Route::get('/stats/benefits/created-daily', [BenefitStatsController::class, 'benefitsCreatedDaily'])->name('benefits.created-daily');
    Route::get('/stats/benefits/created-weekly', [BenefitStatsController::class, 'benefitsCreatedWeekly'])->name('benefits.created-weekly');
    Route::get('/stats/benefits/created-monthly', [BenefitStatsController::class, 'benefitsCreatedMonthly'])->name('benefits.created-monthly');

    // Claims
    Route::get('/stats/claims/total', [ClaimStatsController::class, 'totalClaims'])->name('total.claims');
    Route::get('/stats/claims/approved', [ClaimStatsController::class, 'approvedClaims'])->name('claims.approved');
    Route::get('/stats/claims/rejected', [ClaimStatsController::class, 'rejectedClaims'])->name('claims.rejected');
    Route::get('/stats/claims/by-policy', [ClaimStatsController::class, 'claimsByPolicy'])->name('claims.by-policy');
    Route::get('/stats/claims/by-benefit', [ClaimStatsController::class, 'claimsByBenefit'])->name('claims.by-benefit');
    Route::get('/stats/claims/time-period', [ClaimStatsController::class, 'claimsTimePeriod'])->name('claims.time-period');
    Route::get('/stats/claims/daily', [ClaimStatsController::class, 'claimsDaily'])->name('claims.daily');
    Route::get('/stats/claims/weekly', [ClaimStatsController::class, 'claimsWeekly'])->name('claims.weekly');
    Route::get('/stats/claims/monthly', [ClaimStatsController::class, 'claimsMonthly'])->name('claims.monthly');
});
