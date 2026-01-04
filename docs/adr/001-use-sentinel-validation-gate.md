# ADR 001: Implementing Custom Sentinel Validation Gate

## Status
Accepted

## Context
Standard Azure Data Factory (ADF) validation activities are limited to existence checks. Our platform requires strict schema enforcement for Business Central OData and FinOps-driven cost control (Smart Refresh).

## Decision
We will implement a custom Python-based engine (Sentinel) hosted on Azure Functions, acting as a "Circuit Breaker" between S10 (Raw) and S30 (ODS).

## Consequences
- **Pros:** 60% reduction in unnecessary SQL compute; 100% protection against upstream schema drift.
- **Cons:** Increases complexity of the initial deployment; requires Python maintenance.
