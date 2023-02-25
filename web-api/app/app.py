from flask import Flask, jsonify, request
from app.solver import sudoku, validate_game


app = Flask(__name__)

app.debug = True


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())


@app.route("/")
def index():
    return jsonify({"message": "Hello, World!"})


@app.route("/solve", methods=['POST'])
def ok():
    game = request.get_json().get("game")

    if not game:
        return jsonify({"error": "name is needed"})

    if not validate_game(game):
        return jsonify({"error": "invalid game"})

    app.logger.log(1, "Solving game: %s", game)
    sudoku(game, 0, 0)

    return jsonify({"solvedGame": game})
