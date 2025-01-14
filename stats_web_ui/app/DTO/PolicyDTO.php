<?php

namespace App\DTO;

class PolicyDTO
{
    public int $id;
    public string $type;
    public float $premium;
    public string $status;
    public string $branch;
    public ?string $createdAt;

    public function __construct(
        int $id,
        string $type,
        float $premium,
        string $status,
        string $branch,
        ?string $createdAt = null
    ) {
        $this->id = $id;
        $this->type = $type;
        $this->premium = $premium;
        $this->status = $status;
        $this->branch = $branch;
        $this->createdAt = $createdAt;
    }

    public function toArray(): array
    {
        return [
            'id' => $this->id,
            'type' => $this->type,
            'premium' => $this->premium,
            'status' => $this->status,
            'branch' => $this->branch,
            'created_at' => $this->createdAt,
        ];
    }
}
