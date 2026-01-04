import pytest
from unittest.mock import MagicMock
from sentinel.engine import run_governance_gate
from sentinel.adapters.business_central import BusinessCentralAdapter

def test_end_to_end_validation_flow(monkeypatch):
    """
    Simulates a successful Business Central load and verifies 
    that Sentinel returns a 'Success' exit code.
    """
    # 1. Mock the BC Adapter to return valid sample data
    mock_adapter = MagicMock()
    mock_adapter.fetch_entity.return_value = [
        {"entry_no": 1, "posting_date": "2024-01-01", "amount": 150.0}
    ]
    
    # 2. Patch the adapter in the engine
    monkeypatch.setattr("sentinel.engine.BusinessCentralAdapter", lambda **kwargs: mock_adapter)
    
    # 3. Act & Assert: The engine should exit with 0 (Success)
    with pytest.raises(SystemExit) as e:
        run_governance_gate()
    
    assert e.value.code == 0
