from flask import Flask, request, jsonify

app = Flask(__name__)

# GET API Endpoint: Welcome Message
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the AI/ML Internship API", 
        "status": "success"
    }), 200

# POST API Endpoint: Square a number
@app.route('/square', methods=['POST'])
def square_number():
    try:
        data = request.get_json()
        
        # Error Handling: Check if input exists
        if not data or 'number' not in data:
            return jsonify({"error": "Missing 'number' field"}), 400
            
        number = data['number']
        
        # Error Handling: Validate data type
        if not isinstance(number, (int, float)):
            return jsonify({"error": "Input must be a number"}), 400

        result = number ** 2
        return jsonify({
            "input": number, 
            "result": result, 
            "status": "success"
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
