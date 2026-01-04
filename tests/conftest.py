import pytest
import pandas as pd

@pytest.fixture
def sample_bc_data():
    return pd.DataFrame([
        {"entry_no": 101, "amount": 500.50, "posting_date": "2023-12-31"},
        {"entry_no": 102, "amount": -100.00, "posting_date": "2024-01-01"}
    ])
