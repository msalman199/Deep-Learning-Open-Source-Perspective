from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    return jsonify({"model_version": "v2", "prediction": "class-B"})

if __name__ == '__main__':
    app.run(port=5002)
