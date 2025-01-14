<?php

namespace App\Http\Controllers;

use App\Services\BenefitStatsService;
use Illuminate\Http\Request;

class BenefitStatsController extends Controller
{
    //

    public function show(string $id)
    {
        $http_service = app(BenefitStatsService::class);
        $data = $http_service->getAllData();
        return view('index', $data);
    }

}


