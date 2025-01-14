<?php

namespace App\DTO;

class BenefitDTO
{
    public int $id;
    public int $policyId;
    public string $name;
    public float $amount;
    public bool $active;
    public ?string $createdAt;

    public function __construct(
        int $id,
        int $policyId,
        string $name,
        float $amount,
        bool $active,
        ?string $createdAt = null
    ) {
        $this->id = $id;
        $this->policyId = $policyId;
        $this->name = $name;
        $this->amount = $amount;
        $this->active = $active;
        $this->createdAt = $createdAt;
    }

    public function toArray(): array
    {
        return [
            'id' => $this->id,
            'policy_id' => $this->policyId,
            'name' => $this->name,
            'amount' => $this->amount,
            'active' => $this->active,
            'created_at' => $this->createdAt,
        ];
    }
}
