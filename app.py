from flask import Flask, request, jsonify
from agent import run_task
import os

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run():
    task_description = request.args.get('task')
    if not task_description:
        return jsonify({"status": "error", "message": "Missing task description"}), 400
    
    result = run_task(task_description)
    
    if result["status"] == "success":
        return jsonify(result), 200
    else:
        return jsonify(result), 500

@app.route('/read', methods=['GET'])
def read():
    file_path = request.args.get('path')
    
    if not file_path or not file_path.startswith("/data/"):
        return jsonify({"status": "error", "message": "Invalid file path"}), 400
    
    if not os.path.exists(file_path):
        return jsonify({"status": "error", "message": "File not found"}), 404
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    return content, 200

if __name__ == '__main__':
    app.run(debug=True)
