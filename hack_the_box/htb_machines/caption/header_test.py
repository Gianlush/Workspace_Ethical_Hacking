import requests
import os

# Target URL
url = "http://caption.htb/firewalls"

# Session cookie
cookies = {
    "session": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1hcmdvIiwiZXhwIjoxNzM3NzEzNjI1fQ.59xBdEgmL7Laj1lWKxBlzxOMOvj2Fsl76Pw5Vhrq2sk"
}

# List of headers to test
headers_list = [
    "Accept",
    "X-Forwarded-For",
    "X-Forwarded-Proto",
    "X-Real-IP",
    "User-Agent",
    "Referer",
    "Origin",
    "X-Forwarded-Host",
    "Accept-Language",
    "Accept-Encoding",
    "X-Custom-Header",
    "X-Rewrite-URL",
    "X-Original-URL",
    "X-HTTP-Method-Override",
    "X-Forwarded-Path",
    "X-Forwarded-Port",
    "X-Forwarded-Scheme",
    "X-Forwarded-Server",
    "X-Forwarded-By",
    "X-Forwarded-Prefix",
    "X-Forwarded-Protocol",
    "X-Forwarded-SSL",
    "X-Url-Scheme",
    "Via",
    "Authorization",
    "Content-Type",
    "Content-Length",
    "Cache-Control",
]

# Arbitrary value to test
test_value = "TestValue123"

# Function to clear the cache
def clear_cache():
    os.system("curl caption.htb -X XCGFULLBAN > /dev/null 2>&1")

# Test each header
for header in headers_list:
    print(f"Testing header: {header}")

    # Clear the cache before each request
    clear_cache()

    # Send the request with the header
    response = requests.get(url, cookies=cookies, headers={header: test_value}, proxies={"http":"http://localhost:8080"})

    # Check if the test value is reflected in the response
    if test_value in response.text:
        print(f"\n[+] Vulnerable Header Found: {header}\n")
    else:
        print(f"[-] Not Vulnerable: {header}")
