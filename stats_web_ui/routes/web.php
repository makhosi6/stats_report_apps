<?php

use App\Http\Controllers;
use App\Http\Controllers\BenefitStatsController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::middleware([
    'auth:sanctum',
    config('jetstream.auth_session'),
    'verified',
])->group(function () {
    ///
    Route::get('/dashboard', function () {
        return view('dashboard');
    })->name('dashboard');
    ///
    Route::get('/benefits/{id}', [BenefitStatsController::class, 'show']);
    Route::get('/benefits', [BenefitStatsController::class, 'index']);
});
