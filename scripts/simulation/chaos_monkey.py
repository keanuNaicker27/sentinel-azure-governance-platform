import pandas as pd
import numpy as np
import argparse

def simulate_schema_drift(df: pd.DataFrame) -> pd.DataFrame:
    """Purposely renames a mandatory column to trigger a contract failure."""
    return df.rename(columns={"entry_no": "unknown_id_field"})

def simulate_data_poisoning(df: pd.DataFrame) -> pd.DataFrame:
    """Injects impossible values into the 'amount' column to test Anomaly Detection."""
    df.loc[0, 'amount'] = 999999999.99 
    return df

def simulate_null_violation(df: pd.DataFrame) -> pd.DataFrame:
    """Injects nulls into a non-nullable field defined in the YAML contract."""
    df.loc[0, 'posting_date'] = None
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sentinel Chaos Engineering Suite")
    parser.add_argument("--type", choices=["drift", "poison", "null"], required=True)
    args = parser.parse_args()

    # Load sample Business Central data
    df = pd.read_parquet("tests/data/sample_bc_gl.parquet")

    if args.type == "drift":
        df = simulate_schema_drift(df)
    elif args.type == "poison":
        df = simulate_data_poisoning(df)
    
    df.to_parquet("tests/data/chaos_payload.parquet")
    print(f"Chaos Engineering: {args.type} injected into payload.")
