from flask import Flask, request, jsonify
import joblib
from pyngrok import ngrok

app = Flask(__name__)

model_path = "/mnt/data/classifier.joblib"
model = joblib.load(model_path)

def process_data(data):
    processed_data = data 
    return processed_data

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'input' not in data:
        return jsonify({'error': 'No input data provided'}), 400

    input_data = data['input']
    processed_data = process_data(input_data)
    prediction = model.predict([processed_data])

    return jsonify({'prediction': prediction.tolist()})

public_url = ngrok.connect(5000)
print(f"Public URL: {public_url}")

if __name__ == '__main__':
    app.run(port=5000)
