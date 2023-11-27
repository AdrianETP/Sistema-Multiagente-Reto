from flask import Flask, request, jsonify
import ciudad
import InicializadorModelo
from ciudad import get_model_state
import random
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_simulation_state():
    InicializadorModelo.cm.step()
    state = get_model_state(InicializadorModelo.cm)
    return jsonify(state)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
