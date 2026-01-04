import requests
from typing import Dict, Any, List

class BusinessCentralAdapter:
    def __init__(self, tenant_id: str, client_id: str, client_secret: str):
        self.base_url = f"https://api.businesscentral.dynamics.com/v2.0/{tenant_id}/production/ODataV4"
        self.token = self._get_token(tenant_id, client_id, client_secret)

    def _get_token(self, tenant_id: str, client_id: str, client_secret: str) -> str:
        url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": "https://api.businesscentral.dynamics.com/.default"
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def fetch_entity(self, company_name: str, entity_name: str) -> List[Dict[str, Any]]:
        """Fetches data with OData pagination support."""
        url = f"{self.base_url}/Company('{company_name}')/{entity_name}"
        headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
        
        results = []
        while url:
            resp = requests.get(url, headers=headers)
            resp.raise_for_status()
            data = resp.json()
            results.extend(data.get("value", []))
            url = data.get("@odata.nextLink") # Handle large datasets
        return results
