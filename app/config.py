# config.py
import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


class Config:
    # Load environment variables for local development
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # Fallback to SQLite for local testing
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)
    BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING", "")

    # Azure Key Vault configuration
    KEY_VAULT_NAME = os.getenv("KEY_VAULT_NAME", "your-key-vault-name")
    AZURE_CREDENTIAL = DefaultAzureCredential()

    @classmethod
    def get_secret(cls, secret_name):
        """Fetch a secret from Azure Key Vault."""
        key_vault_url = f"https://{cls.KEY_VAULT_NAME}.vault.azure.net"
        secret_client = SecretClient(vault_url=key_vault_url, credential=cls.AZURE_CREDENTIAL)
        secret = secret_client.get_secret(secret_name)
        return secret.value


# Example usage of Config to get secrets from Azure Key Vault
try:
    # Fetch database URL from Azure Key Vault
    Config.DATABASE_URL = Config.get_secret("DATABASE_URL_SECRET_NAME")
    # Fetch Blob Storage connection string from Azure Key Vault
    Config.BLOB_CONNECTION_STRING = Config.get_secret("BLOB_CONNECTION_STRING_SECRET_NAME")
except Exception as e:
    print(f"Error fetching secrets from Azure Key Vault: {str(e)}")
