<?php

namespace App\Http\Controllers;

use App\Models\User;
use App\Services\BenefitStatsService;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;

class BenefitStatsController extends Controller
{
    //

    public function show(string $id)
    {
        $http_service = app(BenefitStatsService::class);
        $data = $http_service->getMostCommonBenefits();
        return view('dashboard');
    }

    public function index()
    {
        view('dashboard');
    }
}
