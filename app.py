app.py 
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

messages = []

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/send', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        username = data.get('username', 'Anonymous')
        message = data.get('message', '')
        
        if not message:
            return jsonify({"error": "Message cannot be empty"}), 400
        
        msg_obj = {
            "username": username,
            "message": message,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        
        messages.append(msg_obj)
        print(f"Message received: {msg_obj}")
        
        return jsonify({"status": "success", "message": msg_obj}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages), 200

@app.route('/clear', methods=['POST'])
def clear_messages():
    global messages
    messages = []
    return jsonify({"status": "cleared"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
