<?php

namespace App\Providers;

use App\Services\ClaimsStatsService;
use Illuminate\Foundation\Application;
use Illuminate\Support\ServiceProvider;

class ClaimsStatsServiceProvider extends ServiceProvider
{
    /**
     * Register services.
     */
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap services.
     */
    public function boot(): void
    {
        $this->app->singleton(ClaimsStatsService::class, function (Application $app) {
            return new ClaimsStatsService();
        });
    }
}
