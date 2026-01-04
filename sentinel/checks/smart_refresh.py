import pandas as pd
from typing import Tuple

class SmartRefresh:
    @staticmethod
    def verify_column_balance(source_df: pd.DataFrame, sink_total: float, column: str) -> Tuple[bool, float]:
        """
        FinOps Logic: Compares the sum of a critical column (e.g., 'Amount') 
        to determine if a delta exists.
        """
        source_total = source_df[column].sum()
        is_balanced = round(source_total, 2) == round(sink_total, 2)
        
        # If Balanced, we return True to 'Skip' the expensive full load
        return is_balanced, source_total
