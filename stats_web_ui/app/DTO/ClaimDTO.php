<?php

namespace App\DTO;

class ClaimDTO
{
    public int $id;
    public int $policyId;
    public float $amount;
    public string $status;
    public ?string $benefitType;
    public ?string $filedAt;

    public function __construct(
        int $id,
        int $policyId,
        float $amount,
        string $status,
        ?string $benefitType = null,
        ?string $filedAt = null
    ) {
        $this->id = $id;
        $this->policyId = $policyId;
        $this->amount = $amount;
        $this->status = $status;
        $this->benefitType = $benefitType;
        $this->filedAt = $filedAt;
    }

    public function toArray(): array
    {
        return [
            'id' => $this->id,
            'policy_id' => $this->policyId,
            'amount' => $this->amount,
            'status' => $this->status,
            'benefit_type' => $this->benefitType,
            'filed_at' => $this->filedAt,
        ];
    }
}
