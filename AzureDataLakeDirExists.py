from azure.storage.filedatalake import DataLakeServiceClient
import os

# Define Azure Storage account and filesystem details
account_name = 'geraldaccount'  # Replace with your Storage Account Name
account_key = 'T6iWDFUukzJK1JchuBn7Y/BNm9U1SX2Juw7BL4L2Q7XWWGjXTPj3uMqWnAgAHBpws3XyhsrgfOYj+AStxJXnMQ=='  # Replace with your Access Key
filesystem_name = 'geraldblob'  # The filesystem (container) in Data Lake
# local_file_path = '/path/to/your/local/file.csv'  # Path to the CSV file on your Mac
remote_file_path = 'giraffe/Electrical_Vehicle_Population_Data_1000.csv'  # Desired path in Azure Data Lake Storage Gen2

# Create a DataLakeServiceClient object using the account name and account key
def create_datalake_service_client(account_name, account_key):
    service_url = f"https://{account_name}.dfs.core.windows.net"
    credential = account_key
    service_client = DataLakeServiceClient(account_url=service_url, credential=credential)
    return service_client

# Ensure that the directory exists
def ensure_directory_exists(file_system_client, remote_file_path):
    directory_path = '/'.join(remote_file_path.split('/')[:-1])  # Get the directory path
    print(directory_path)
    
    if directory_path:
        try:
            # Try to get the directory client; if it does not exist, this will raise an error
            file_system_client.get_directory_client(directory_path)
            print('directory exists')
        except Exception:
            # If the directory doesn't exist, create it
            file_system_client.create_directory(directory_path)
            print(f"Directory '{directory_path}' created.")


# Create a service client and get the filesystem client
service_client = create_datalake_service_client(account_name, account_key)
file_system_client = service_client.get_file_system_client(filesystem_name)
    
# Ensure the directory exists before uploading
ensure_directory_exists(file_system_client, remote_file_path)

