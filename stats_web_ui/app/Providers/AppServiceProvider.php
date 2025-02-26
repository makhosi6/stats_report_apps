<?php

namespace App\Providers;

use App\Models\User;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\ServiceProvider;
use Illuminate\Support\Facades\View;
use App\Models\PersonalAccessToken;
use Laravel\Sanctum\Sanctum;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {


        Sanctum::usePersonalAccessTokenModel(PersonalAccessToken::class);

        $user_acquisition = [];

        $users_activity = [];
        //
        View::share('users_activity', $users_activity);
        View::share('user_acquisition', $user_acquisition);
    }
}
