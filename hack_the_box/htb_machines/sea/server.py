from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    # Add CORS headers to the response
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

@app.route("/", methods=["POST", "OPTIONS"])
def receive_data():
    if request.method == "OPTIONS":
        # Handle preflight requests
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response, 200

    # Handle POST requests
    data = request.json
    print("Received data:", data)
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001)
