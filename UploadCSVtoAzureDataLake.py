from azure.storage.filedatalake import DataLakeServiceClient
import os

# Define Azure Storage account and filesystem details
account_name = 'geraldaccount'
account_key = 'T6iWDFUukzJK1JchuBn7Y/BNm9U1SX2Juw7BL4L2Q7XWWGjXTPj3uMqWnAgAHBpws3XyhsrgfOYj+AStxJXnMQ=='
filesystem_name = 'geraldblob'
# local_file_path = '/path/to/your/local/file.csv'  # Path to the CSV file on your Mac
local_file_path = '/Users/geraldhopkins/Documents/PythonFiles/Data/Electrical_Vehicle_Population_Data_1000.csv'
# remote_file_path = 'path/in/adls/file.csv'  # Desired path in Azure Data Lake Storage Gen2
remote_file_path = 'vehicle_data/Electrical_Vehicle_Population_Data_1000.csv'

# Create a DataLakeServiceClient object using the account name and account key
def create_datalake_service_client(account_name, account_key):
    service_url = f"https://{account_name}.dfs.core.windows.net"
    credential = account_key
    service_client = DataLakeServiceClient(account_url=service_url, credential=credential)
    return service_client

print('here')

# Upload the CSV file
def upload_file_to_datalake(local_file_path, remote_file_path):
    # Create a service client and get the filesystem client
    service_client = create_datalake_service_client(account_name, account_key)
    file_system_client = service_client.get_file_system_client(filesystem_name)
    
    # Check if file already exists and delete if necessary
    try:
        file_client = file_system_client.get_file_client(remote_file_path)
        file_client.delete_file()  # Delete if file exists
    except Exception as e:
        print(f"File doesn't exist or can't be deleted: {e}")

    # Create a file client for the remote file
    file_client = file_system_client.get_file_client(remote_file_path)
    
    # Upload the file
    with open(local_file_path, "rb") as file_data:
        file_client.append_data(file_data, offset=0, length=os.path.getsize(local_file_path))
        file_client.flush_data(os.path.getsize(local_file_path))
    
    print(f"File {local_file_path} uploaded to Azure Data Lake Storage as {remote_file_path}")

# Run the function to upload the file
upload_file_to_datalake(local_file_path, remote_file_path)
