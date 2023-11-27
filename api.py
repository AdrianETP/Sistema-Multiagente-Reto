from flask import Flask, request, jsonify
import ciudad
from ciudad import get_model_state
import random
import json

app = Flask(__name__)

# Inicialización de la ciudad
cm = ciudad.Ciudad([1, 5, 8], 100, [10, 20, 30])

@app.route('/model_state', methods=['GET'])
def get_simulation_state():
    cm.step()
    state = get_model_state(cm)
    return jsonify(state)

if __name__ == '__main__':
    app.run(debug=True, port=5000)