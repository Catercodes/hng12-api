from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

@app.route("/", methods=["GET"])
def get_info():
    response_data = {
        "email": "chrisadamsadewuni@gmail.com",  # Your HNG email
        "current_datetime": datetime.utcnow().isoformat() + "Z",  # ISO 8601 format
        "github_url": "https://github.com/Catercodes/hng12-api"  # Your GitHub repo
    }
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)

