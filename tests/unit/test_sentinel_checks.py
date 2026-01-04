import pytest
import pandas as pd
from sentinel.checks.smart_refresh import SmartRefresh
from sentinel.checks.schema_drift import SchemaDriftDetector

def test_smart_refresh_skips_when_balanced():
    # Arrange: Source and Sink have the same total
    source_df = pd.DataFrame({'amount': [100.0, 200.0, 300.0]})
    sink_metadata = {'total': 600.0}
    
    # Act
    should_skip = SmartRefresh.should_skip_load(source_df, sink_metadata, 'amount')
    
    # Assert
    assert should_skip is True

def test_schema_drift_detects_missing_column():
    # Arrange: Contract expects 'posting_date', but BC API sent 'date'
    current_schema = {'entry_no': 'int', 'date': 'string'}
    contract_schema = [
        {'column': 'entry_no', 'type': 'int'},
        {'column': 'posting_date', 'type': 'date'}
    ]
    
    # Act
    errors = SchemaDriftDetector.detect_changes(current_schema, contract_schema)
    
    # Assert
    assert "posting_date" in errors["missing"]
