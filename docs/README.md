# Sentinel: Enterprise Azure Governance Platform

[![Code Quality](https://github.com/youruser/sentinel/actions/workflows/static-analysis.yml/badge.svg)](...)

[![Data Contract](https://img.shields.io/badge/Data%20Contract-Strict-green)](...)

Sentinel is not a data pipeline; it is a **Governance Engine**. Built to solve the volatility of **Dynamics 365 Business Central** integrations, it implements a **"Shift-Left" Reliability** strategy.

### Key Innovations
- **FinOps 'Smart Refresh':** Using hash-balance canaries to bypass Azure compute when data hasn't changed.
- **Circuit Breaker Pattern:** Automated blocking of production loads if OData schema drift is detected.
- **Audit-Ready Modeling:** Automated RGS mapping for the **Continuous Auditor API**.


## 🛠 Tech Stack
- **Languages:** Python (Sentinel Engine), SQL (Medallion S10-S50).
- **Orchestration:** Azure Data Factory + Event-Driven Webhooks.
- **Security:** Zero-Trust Managed Identities & Azure Key Vault.
- **Infrastructure:** Terraform (Private Endpoints & VNet Isolation).

## 📂 Quick Start
```bash
make setup
make test
make chaos  # Run a reliability simulation
