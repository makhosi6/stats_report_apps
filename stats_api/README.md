### **API Routes**

#### **1. Policies Analytics**

| Route                                        | HTTP Method | Description                                     |
|----------------------------------------------|-------------|-------------------------------------------------|
| `/api/stats/policies/total`                  | `GET`       | Total number of policies.                       |
| `/api/stats/policies/cancelled`              | `GET`       | Total number of cancelled policies.             |
| `/api/stats/policies/reinstated`             | `GET`       | Total number of reinstated policies.            |
| `/api/stats/policies/by-type`                | `GET`       | Policies grouped by type (e.g., legal, funeral).|
| `/api/stats/policies/time-period`            | `GET`     | policies data over specific time periods.          |
| `/api/stats/policies/by-premium`             | `GET`       | Policies grouped by premium ranges.             |
| `/api/stats/policies/created-daily`          | `GET`       | Number of policies created daily.               |
| `/api/stats/policies/created-weekly`         | `GET`       | Number of policies created weekly.              |
| `/api/stats/policies/created-monthly`        | `GET`       | Number of policies created monthly.             |
| `/api/stats/policies/by-branch`              | `GET`       | Policies grouped by branch.                     |
| `/api/stats/policies/branch/<branch>`        | `GET`       | Policies for a specific branch.                 |

#### **2. Benefits Analytics**

| Route                                        | HTTP Method | Description                                         |
|----------------------------------------------|-------------|-----------------------------------------------------|
| `/api/stats/benefits/total`                  | `GET`       | Total number of benefits across all policies.       |
| `/api/stats/benefits/time-period`            | `GET`       | benefits data over specific time periods.          |
| `/api/stats/benefits/average-per-policy`     | `GET`       | Average number of benefits per policy.              |
| `/api/stats/benefits/by-policy-type`         | `GET`       | Benefits grouped by policy type.                    |
| `/api/stats/benefits/most-common`            | `GET`       | Most common benefits across policies.               |
| `/api/stats/benefits/created-daily`          | `GET`       | Number of policies created daily.                   |
| `/api/stats/benefits/created-weekly`         | `GET`       | Number of policies created weekly.                  |
| `/api/stats/benefits/created-monthly`        | `GET`       | Number of policies created monthly.                 |

#### **3. Claims Analytics**

| Route                                        | HTTP Method | Description                                      |
|----------------------------------------------|-------------|--------------------------------------------------|
| `/api/stats/claims/total`                    | `GET`       | Total number of claims.                          |
| `/api/stats/claims/approved`                 | `GET`       | Total number of approved claims.                 |
| `/api/stats/claims/rejected`                 | `GET`       | Total number of rejected claims.                 |
| `/api/stats/claims/by-policy`                | `GET`       | Claims grouped by policy type.                   |
| `/api/stats/claims/by-benefit`               | `GET`       | Claims grouped by benefit type.                  |
| `/api/stats/claims/time-period`              | `GET`       | Claims data over specific time periods.          |
| `/api/stats/claims/daily`                    | `GET`       | Number of claims filed daily.                    |
| `/api/stats/claims/weekly`                   | `GET`       | Number of claims filed weekly.                   |
| `/api/stats/claims/monthly`                  | `GET`       | Number of claims filed monthly.                  |


---

### **JSON Responses**

#### **1. `/api/stats/policies/by-type`**
```json
{
  "data": [
    {
      "type": "Popcru 25",
      "total": 200
    },
    {
      "type": "Legal Prestige",
      "total": 600
    },
    {
      "type": "Legal Gold",
      "total": 40
    }
  ]
}
```

#### **2. `/api/stats/benefits/average-per-policy`**
```json
{
  "data": {
    "average_benefits_per_policy": 3.2
  }
}
```

#### **3. `/api/stats/claims/time-period?start_date=2024-01-01&end_date=2024-12-31`**
```json
{
  "data": [
    {
      "date": "2024-01-01",
      "claims": 120
    },
    {
      "date": "2024-01-02",
      "claims": 95
    },
    {
      "date": "2024-01-03",
      "claims": 80
    }
  ]
}
```

#### **4. `/api/stats/policies/by-branch`**
```json
{
  "data": [
    {
      "branch": "Johannesburg",
      "total_policies": 500
    },
    {
      "branch": "Cape Town",
      "total_policies": 300
    },
    {
      "branch": "Durban",
      "total_policies": 200
    }
  ]
}
```

#### **2. `/api/stats/policies/branch/<branch>`**
```json
{
  "data": {
    "branch": "Johannesburg",
    "policies": [
      {
        "policy_code": "PC_25",
        "product_name": "Popcru 25",
        "created_at": "2024-01-01"
      },
      {
        "policy_code": "LP",
        "product_name": "Legal Prestige",
        "created_at": "2024-01-02"
      }
    ]
  }
}
```