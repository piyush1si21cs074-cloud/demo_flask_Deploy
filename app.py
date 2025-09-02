from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # allow cross-origin 

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("text", "")
    return jsonify({"response": f"Hello from Flask! You said: {message}"})

@app.route("/", methods=["GET"])
def home():
    return jsonify({"response": "Connected successfully!"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5001))  
    app.run(host="0.0.0.0", port=port, debug=True)
