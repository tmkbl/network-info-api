from flask import Flask, jsonify
import os
import platform
import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "service": "Network Info API",
        "status": "running",
        "description": "Simple cloud-based web service",
        "version": "1.0.0",
        "server": platform.system(),
        "timestamp": datetime.datetime.now().isoformat()
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
