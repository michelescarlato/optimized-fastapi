# storage.py
from azure.storage.blob import BlobServiceClient
import os

# Initialize Blob Service Client using the connection string from Key Vault
blob_service_client = BlobServiceClient.from_connection_string("your_blob_connection_string")

def upload_file_to_blob(container_name, file_path, blob_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
    return f"File {blob_name} uploaded successfully."
