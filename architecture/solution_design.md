# Technical Solution Design: Business Central to Analytics

## 1. Architectural Layers (Medallion Standard)
* **S10/S20 (Bronze):** Persistent raw capture of Business Central entities (GL, Items, Vendors). Includes historical snapshots for auditability.
* **S30 (Silver):** Standardized Relational ODS. Business rules and RGS mapping (Reference Chart of Accounts) are applied here.
* **S40/S50 (Gold):** Purpose-built dimensional datamarts optimized for Power BI and external API consumption.

## 2. Sentinel Governance Engine
* **Contract Enforcement:** Sentinel validates that incoming Business Central API payloads match the YAML-defined contracts.
* **Smart Refresh Logic:** Computes hash-based "Column Balances" at the source. If no delta exists, the pipeline bypasses expensive Synapse/SQL compute cycles.

## 3. Security & Infrastructure
* **Identity:** Managed Identities (MI) are used for all service-to-service communication, eliminating hardcoded keys.
* **Secrets:** Azure Key Vault acts as the central hub for API secrets and database connection strings.
* **Network:** VNet integration and Private Endpoints ensure data never traverses the public internet.
