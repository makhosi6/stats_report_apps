<?php
namespace App\Providers;
use App\Services\BenefitStatsService;
use Illuminate\Contracts\Foundation\Application;
use Illuminate\Support\ServiceProvider;

class BenefitStatsServiceProvider extends ServiceProvider
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
        $this->app->singleton(BenefitStatsService::class, function (Application $app) {
            return new BenefitStatsService();
        });
    }
}
