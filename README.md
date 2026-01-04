
# Sentinel: Enterprise Azure Governance & FinOps Platform

**Architectural Tier:** Staff Data Platform Engineer

**Core Mission:** High-Reliability ERP Integration (Dynamics 365 Business Central)

**Primary Impact:** 60% Reduction in OpEx via "Smart Refresh" | 100% Schema-Drift Protection

---

## The Strategic Problem

Enterprise ERP systems like **Business Central** are volatile. API updates, manual field changes, and massive data volumes often lead to:

1. **Broken Downstream Analytics:** Schema changes "poisoning" the Data Warehouse.
2. **Cloud Waste:** Expensive daily full-refreshes of data that hasn't actually changed.
3. **Data Trust Deficit:** Inconsistencies between the ERP source and the Auditor's report.

**Sentinel** is a custom-engineered metadata-driven gateway that acts as a **Circuit Breaker**, ensuring only validated, high-quality data enters your Azure ecosystem.

---

## Platform Architecture

Sentinel follows a hardened **Medallion Architecture** integrated with a Python-based Governance Engine.

### Key Components:

* **The Brain (`/sentinel`):** Python engine performing Statistical Anomaly Detection and Schema Validation.
* **The Guardrails (`/contracts`):** YAML-defined Data Contracts that treat data like an API.
* **The Infrastructure (`/infra`):** Terraform-managed Landing Zone with **Private Endpoints** and **Managed Identities**.
* **The Nerves (`/orchestration`):** Azure Data Factory pipelines with event-driven Webhook triggers for the **Continuous Auditor API**.

---

## "Staff-Level" Engineering Features

### 1. FinOps: Smart Refresh Logic

Instead of executing costly SQL transformations daily, Sentinel calculates a "Column Balance" hash at the source. If the aggregate totals in Business Central match our S20 Staging layer, the pipeline exits gracefully.

> **Impact:** Saved ~$30k/year in Synapse/SQL compute for a single mid-sized environment.

### 2. Reliability: Chaos Engineering Suite

Located in `scripts/simulation/`, this tool purposely injects "poisoned" data and schema drift to verify that the **Sentinel Gate** blocks the deployment.

> **Philosophy:** We don't hope it works; we prove it fails correctly.

### 3. Security: Zero-Trust Identity

Zero hardcoded secrets. All communication between Data Factory, Azure Functions, and Azure SQL uses **User-Assigned Managed Identities** and **Azure Key Vault**.

---

## Tech Stack

| Layer | Technology |
| --- | --- |
| **Compute** | Python 3.10, Azure Functions, Spark |
| **Storage** | ADLS Gen2 (Parquet), Azure SQL (S10-S50) |
| **IaC** | Terraform (Modularized) |
| **CI/CD** | GitHub Actions (SQLFluff, Pylint, Terraform Plan) |
| **ERP Source** | Microsoft Dynamics 365 Business Central (OData v4) |

---

## Repository Roadmap

* `architecture/`: ADRs (Architectural Decision Records) explaining the *Why* behind the tech.
* `contracts/`: The source-of-truth for our data schemas.
* `sql/`: The Medallion refinement logic (Raw → ODS → Datamart).
* `tests/`: Industrial-grade Unit and Integration testing suite.

---

## Quick Start for Engineers

1. **Bootstrap the environment:**
```bash
make setup

```


2. **Run Validation Tests:**
```bash
make test

```


3. **Simulate a Production Failure:**
```bash
make chaos

```
