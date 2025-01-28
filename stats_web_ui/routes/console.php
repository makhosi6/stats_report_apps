<?php

use Carbon\Carbon;
use Illuminate\Support\Facades\DB;
use Illuminate\Foundation\Inspiring;
use Illuminate\Support\Facades\Artisan;

Artisan::command('inspire', function () {
    $this->comment(Inspiring::quote());
})->purpose('Display an inspiring quote')->hourly();


Artisan::command('update_users', function () {
    $users = DB::table('users')->get();
    $bar = $this->output->createProgressBar(count($users));
    $bar->start();
    foreach ($users as $user) {
        $created_at = Carbon::now()->subDays(rand(0, Carbon::now()->diffInDays(Carbon::parse('2024-02-29'))));
        $updated_at = Carbon::now()->subDays(rand(0, Carbon::now()->diffInDays(Carbon::parse('2024-04-30'))));
        DB::table('users')->where('id', $user->id)->update(['created_at' => $created_at, 'updated_at' => $updated_at]);
        $bar->advance();
    }
    $bar->finish();
})->purpose('Bulk update users (sanitize the data)');
