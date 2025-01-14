<?php

namespace App\Services;

use Illuminate\Support\Facades\Http;
use Illuminate\Http\Client\Response;

abstract class BaseHttpService
{

    function connect(string $path, array | null $data): Response
    {
        $api_base_url = env('API_BASE_URL', 'http://localhost:5050/api/stats/');
        return Http::get($api_base_url . $path, $data);
    }
}
