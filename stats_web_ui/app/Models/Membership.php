<?php

namespace App\Models;

use Laravel\Jetstream\Membership as JetstreamMembership;
use Illuminate\Support\Str;
use Illuminate\Database\Eloquent\Factories\HasFactory;
class Membership extends JetstreamMembership
{
    use HasFactory;

    public $incrementing = false;
    /**
     * Indicates if the IDs are auto-incrementing.
     *
     * @var bool
     */

    public $keyType = 'string';

    /**
     *
     */
    public static function boot()
    {
        parent::boot();

        static::creating(function ($model) {
            $model->id = (string) Str::uuid();
        });
    }
}
