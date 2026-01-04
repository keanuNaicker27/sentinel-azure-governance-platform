```mermaid
graph TD
    subgraph "External Cloud Tier"
        BC[D365 Business Central]
    end

    subgraph "Sentinel Governance Layer (The Brain)"
        direction TB
        AD[Anomaly Detector]
        SR[Smart Refresh Logic]
        SD[Schema Drift Check]
        VAL{Sentinel Gate}
    end

    subgraph "Azure Data Platform (Medallion)"
        direction TB
        S10[(S10/S20: Raw Parquet)]
        S30[(S30: Relational ODS)]
        S50[(S50: Auditor Datamart)]
    end

    subgraph "Consumer Tier"
        CA[Continuous Auditor API]
        PBI[Power BI Dashboards]
    end

    %% Flow logic
    BC -->|OData/OAuth2| S10
    S10 --> SD
    SD -->|Validated| SR
    SR -->|Delta Found| AD
    AD -->|Safe| VAL

    VAL -->|APPROVED| S30
    S30 --> S50
    S50 -->|Webhook Trigger| CA
    S50 --> PBI

    %% Circuit Breaker Path
    VAL -->|REJECTED| FAIL[HALT & ALERT]
    SD -.->|Drift Detected| FAIL
    AD -.->|Outlier Detected| FAIL
    SR -.->|No Delta| EXIT[Graceful Exit / Save Cost]

    %% Styling
    style VAL fill:#00c853,stroke:#333,stroke-width:4px,color:#fff
    style BC fill:#0078d4,color:#fff
    style FAIL fill:#d50000,color:#fff
    style SR fill:#2962ff,color:#fff
    style EXIT fill:#757575,color:#fff
