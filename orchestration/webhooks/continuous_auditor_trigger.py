import requests
import logging

class AuditorWebhook:
    def __init__(self, api_key: str, endpoint: str):
        self.headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
        self.endpoint = endpoint

    def notify_auditor(self, administration_id: str, load_status: str):
        """
        Triggers the Continuous Auditor once Sentinel confirms data integrity.
        """
        if load_status != "SUCCESS_VALIDATED":
            logging.warning(f"Aborting webhook for {administration_id}: Sentinel Validation Failed.")
            return

        payload = {
            "administration_id": administration_id,
            "event_type": "DATA_REFRESH_COMPLETE",
            "source": "Sentinel_Azure_Platform"
        }

        response = requests.post(self.endpoint, json=payload, headers=self.headers)
        response.raise_for_status()
        logging.info(f"Successfully triggered Auditor for {administration_id}")
