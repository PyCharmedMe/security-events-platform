import requests
from flask import Flask, jsonify

INGESTOR_URL = "http://ingestor:5000/events"

app = Flask(__name__)

def classify(event):
    if event.get("type") == "login_failure":
        return "MEDIUM"
    if event.get("type") == "port_scan":
        return "HIGH"
    return "LOW"

@app.route("/analyze")
def analyze():
    events = requests.get(INGESTOR_URL).json()
    analyzed = [
        {**e, "severity": classify(e)}
        for e in events
    ]
    return jsonify(analyzed)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
