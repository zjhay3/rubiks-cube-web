from flask import Flask, request, jsonify
from flask_cors import CORS
import kociemba
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "Rubik Cube Solver API"}

@app.route("/solve", methods=["POST"])
def solve_cube():
    data = request.json
    cube_state = data.get("state")

    try:
        solution = kociemba.solve(cube_state)
        return jsonify({"solution": solution})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
