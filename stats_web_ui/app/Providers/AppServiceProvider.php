<?php

namespace App\Providers;

use App\Models\User;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\ServiceProvider;
use Illuminate\Support\Facades\View;

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
        $user_acquisition = User::select(DB::raw("COUNT(*) as count"))
            ->whereYear('created_at', date('Y'))
            ->groupBy(DB::raw("Month(created_at)"))
            ->pluck('count');

        $users_activity = User::select(DB::raw("COUNT(*) as count"))
            ->whereYear('updated_at', date('Y'))
            ->groupBy(DB::raw("Month(updated_at)"))
            ->pluck('count');
        //
        View::share('users_activity', $users_activity);
        View::share('user_acquisition', $user_acquisition);
    }
}
