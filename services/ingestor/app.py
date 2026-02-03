from flask import Flask, request, jsonify

app = Flask(__name__)
events = []

@app.route("/event", methods=["POST"])
def ingest_event():
    event = request.json
    events.append(event)
    return jsonify({"status": "event received"}), 201

@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
