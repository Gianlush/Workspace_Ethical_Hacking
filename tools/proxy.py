import http.server
import socketserver
import threading
import requests
import sys
import argparse
from termcolor import colored

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Handle requests in a separate thread."""
    daemon_threads = True

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    # List of domains to intercept
    do_intercept_list = ["localhost"]
    # List of file extensions to blacklist
    blacklisted_extensions = [".png", ".jpg", ".css", ".js"]
    # Logging verbosity
    log_all = False

    def modify_request(self, path, method, body=None):
        """Modify the request based on intercept list and log decisions."""
        # Check for blacklisted extensions
        for ext in self.blacklisted_extensions:
            if path.endswith(ext):
                break
            # Check if the domain is in the intercept list
            for domain in self.do_intercept_list:
                if domain in path:
                    print(colored(f"Intercepted request for domain: {domain}", "green"))
                    if method == "GET":
                        if self.headers
                    elif method == "POST":
                        # Example modification for POST (e.g., altering body)
                        body = body.replace(b"original", b"modified") if body else body
                    return path, body

        # If not intercepted or blacklisted, return original values
        if self.log_all:
            print(f"Forwarding request: {path}")
            
        return path, body

    def do_GET(self):
        # Intercept and modify request
        modified_path, _ = self.modify_request(self.path, "GET")
        if modified_path is None:
            return

        # Forward the request to the target server
        try:
            response = requests.get(modified_path, headers=self.headers)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error forwarding request: {e}".encode("utf-8"))
            return

        # Send the response back to the client
        self.send_response(response.status_code)
        for key, value in response.headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(response.content)

    def do_POST(self):
        # Intercept and modify request
        content_length = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_length)
        modified_path, modified_body = self.modify_request(self.path, "POST", post_body)
        if modified_path is None:
            return

        # Forward the request to the target server
        try:
            response = requests.post(modified_path, headers=self.headers, data=modified_body)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error forwarding request: {e}".encode("utf-8"))
            return

        # Send the response back to the client
        self.send_response(response.status_code)
        for key, value in response.headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(response.content)

    def log_message(self, format, *args):
        """Override default logging behavior to respect the -a flag."""
        if self.log_all:
            super().log_message(format, *args)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Simple Python HTTP Proxy with request modification capabilities.")
    parser.add_argument("-p", "--port", type=int, default=8081, help="Port on which the proxy will listen (default: 8081).")
    parser.add_argument("-a", "--all-logs", action="store_true", help="Log all requests, not just in-scope ones.")
    args = parser.parse_args()

    # Start the server with threading and logging settings
    PORT = args.port
    ProxyHandler.log_all = args.all_logs

    with ThreadingTCPServer(("", PORT), ProxyHandler) as httpd:
        print(f"Serving on port {PORT} with threading...")
        if ProxyHandler.log_all:
            print("Logging all requests.")
        else:
            print("Logging only in-scope requests.")
        httpd.serve_forever()