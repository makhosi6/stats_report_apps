<?php

namespace App\Providers;

use App\Services\PolicyStatsService;
use Illuminate\Contracts\Foundation\Application;
use Illuminate\Support\ServiceProvider;

class PolicyStatsServiceProvider extends ServiceProvider
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
        $this->app->singleton(PolicyStatsService::class, function (Application $app) {
            return new PolicyStatsService();
        });
    }
}
