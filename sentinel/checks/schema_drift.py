from typing import Dict, List, Any

class SchemaDriftDetector:
    @staticmethod
    def detect_changes(current_schema: Dict[str, str], contract_schema: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """
        Compares BC API Metadata against the Contract YAML.
        Returns a dict of missing_columns and type_mismatches.
        """
        errors = {"missing": [], "mismatches": []}
        
        # Convert contract list to dict for faster lookup
        contract_dict = {col['column']: col['type'] for col in contract_schema}

        for col_name, col_type in contract_dict.items():
            if col_name not in current_schema:
                errors["missing"].append(col_name)
            elif current_schema[col_name] != col_type:
                errors["mismatches"].append(f"{col_name}: expected {col_type}, got {current_schema[col_name]}")
        
        return errors
