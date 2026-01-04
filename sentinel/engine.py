import sys
from adapters.business_central import BusinessCentralAdapter
from checks.smart_refresh import SmartRefresh
from checks.anomaly_detection import AnomalyDetector

def run_governance_gate():
    # 1. Initialize Adapters (Using env vars from GitHub Secrets)
    adapter = BusinessCentralAdapter(tenant_id="...", client_id="...", client_secret="...")
    
    # 2. Fetch Sample for Validation
    data = adapter.fetch_entity("CRONUS", "GeneralLedgerEntries")
    df = pd.DataFrame(data)

    # 3. Execute 'Smart Refresh' (FinOps)
    # Assume 1000.0 is the current value in our Azure SQL Sink
    is_balanced, new_total = SmartRefresh.verify_column_balance(df, 1000.0, "amount")
    
    if is_balanced:
        print("FinOps: Source matches Sink. Skipping expensive refresh.")
        sys.exit(0) # Success, but nothing to do

    # 4. Execute Anomaly Detection (Reliability)
    detector = AnomalyDetector()
    if detector.detect_volume_anomaly(len(df), [950, 1020, 980]):
        print("ALERT: Volume anomaly detected! Blocking Pipeline.")
        sys.exit(1) # CRITICAL FAILURE - Blocks Deployment

    print("Sentinel Gate: Passed. Proceeding to S30 Processing.")
    sys.exit(0)

if __name__ == "__main__":
    run_governance_gate()
