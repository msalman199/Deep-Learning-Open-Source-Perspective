from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    return jsonify({"model": "replica1", "prediction": "class-A"})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(port=5001)
