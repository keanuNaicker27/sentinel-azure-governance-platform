```mermaid
graph TD
    subgraph "External ERP"
        BC[D365 Business Central API]
    end

    subgraph "Azure Data Platform"
        KV[Azure Key Vault]
        MI[Managed Identity]
        
        subgraph "Sentinel Layer"
            SG{Sentinel Gate}
            CF[Contract Files]
        end

        subgraph "Data Storage"
            S10[(S10/S20: Raw)]
            S30[(S30: ODS)]
            S50[(S40/S50: Datamarts)]
        end
    end

    BC -->|OData/OAuth| S10
    S10 --> SG
    CF --> SG
    SG -->|Validation Passed| S30
    S30 --> S50
    S50 -->|Webhook Trigger| CA[Continuous Auditor API]

    style SG fill:#f96,stroke:#333,stroke-width:4px
    style BC fill:#0078d4,color:#fff
    
