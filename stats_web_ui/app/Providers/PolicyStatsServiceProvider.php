<?php

namespace App\Providers;

use App\Services\PolicyStatsService;
use Illuminate\Auth\AuthManager;
use Illuminate\Contracts\Foundation\Application;
use Illuminate\Support\Facades;
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
        $this->app->singleton('auth2', fn ($app) => new AuthManager($app));
        $policy_service =  new PolicyStatsService();
        view()->share('count1', [1, 2, 3]);
        view()->share('key1', 'value');
        Facades\View::share('dashboard', PolicyStatsComposer::class);
        Facades\View::composer(['welcome', 'dashboard','view1'], PolicyStatsComposer::class);
        $this->app-> singleton(PolicyStatsService::class, function (Application $app) use($policy_service) {
            return $policy_service;
        });
    }
}


class PolicyStatsComposer
{

    /**
     * Bind data to the view.
     */
    public function compose($view): void
    {
        $view->with('count', [0,1,2,3]);
    }
}
