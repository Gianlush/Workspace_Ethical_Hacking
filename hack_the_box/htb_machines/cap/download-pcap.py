import os
import requests
from concurrent.futures import ThreadPoolExecutor

# Create export directory if it doesn't exist
export_dir = 'export'
if not os.path.exists(export_dir):
    os.makedirs(export_dir)

# Function to handle the download process
def download_file(file_number):
    # Build URLs
    data_url = f'http://cap.htb/data/{file_number}'
    download_url = f'http://cap.htb/download/{file_number}'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Priority': 'u=0, i',
    }

    # Step 1: Send GET request to /data/{file_number}
    try:
        response = requests.get(data_url, headers=headers)
        if response.status_code == 200:
            print(f"[INFO] Data fetched for {file_number}, Response length: {len(response.text)}")

            # Step 2: If response length is greater than 500, download the file
            if len(response.text) > 200:
                print(f"[INFO] Response length > 500, proceeding to download for {file_number}")
                
                # Send GET request to /download/{file_number}
                download_response = requests.get(download_url, headers=headers)
                if download_response.status_code == 200:
                    # Save the downloaded file
                    file_path = os.path.join(export_dir, f"{file_number}.file")
                    with open(file_path, 'wb') as file:
                        file.write(download_response.content)
                    print(f"[INFO] File {file_number} downloaded successfully.")
                else:
                    print(f"[ERROR] Failed to download file {file_number}, Status code: {download_response.status_code}")
            else:
                print(f"[INFO] File {file_number} skipped, Response length <= 500")
        else:
            print(f"[ERROR] Failed to fetch data for {file_number}, Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Exception occurred for {file_number}: {e}")

# Create a thread pool to send requests concurrently
def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_file, range(0, 2))

if __name__ == "__main__":
    main()
