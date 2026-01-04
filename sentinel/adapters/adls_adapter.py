import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient
from io import BytesIO

class ADLSAdapter:
    def __init__(self, account_name: str, credential: str):
        self.service_client = DataLakeServiceClient(
            account_url=f"https://{account_name}.dfs.core.windows.net", 
            credential=credential
        )

    def write_parquet(self, df: pd.DataFrame, container: str, path: str):
        """Writes data to S10/S20 Staging as Parquet for cost-effective storage."""
        file_client = self.service_client.get_file_client(container, path)
        buffer = BytesIO()
        df.to_parquet(buffer, index=False)
        file_client.upload_data(buffer.getvalue(), overwrite=True)

    def read_parquet(self, container: str, path: str) -> pd.DataFrame:
        file_client = self.service_client.get_file_client(container, path)
        download = file_client.download_file()
        return pd.read_parquet(BytesIO(download.readall()))
