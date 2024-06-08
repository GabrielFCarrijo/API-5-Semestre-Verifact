# Instalar pyngrok
#!pip install pyngrok Flask

from flask import Flask, request, jsonify
import joblib
import json
import nbformat
from nbconvert import PythonExporter
import subprocess
from pyngrok import ngrok

app = Flask(__name__)


model_path = "/mnt/data/classifier.joblib"
model = joblib.load(model_path)


def run_notebook(notebook_path, parameters):
    with open(notebook_path) as f:
        notebook = nbformat.read(f, as_version=4)


    notebook.cells[0] = nbformat.v4.new_code_cell(f"parameters = {json.dumps(parameters)}")

    exporter = PythonExporter()
    source_code, _ = exporter.from_notebook_node(notebook)


    with open("temp_notebook.py", "w") as f:
        f.write(source_code)


    result = subprocess.run(["python3", "temp_notebook.py"], capture_output=True, text=True)
    return result.stdout

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if 'input' not in data:
        return jsonify({'error': 'No input data provided'}), 400

    input_data = data['input']


    notebook_output = run_notebook("/mnt/data/Pre_processamento_PI_FakeNews (1).ipynb", {"input_data": input_data})


    processed_data = json.loads(notebook_output)


    prediction = model.predict([processed_data])

    return jsonify({'prediction': prediction.tolist()})

# Iniciar o servidor Flask
#!python app.py &

public_url = ngrok.connect(5000)
print(f"Public URL: {public_url}")


