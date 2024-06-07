from flask import Flask, render_template, request
import chess
import chess.svg
from GameSetup import ChessGame  # Import ChessGame directly

app = Flask(__name__)
game = ChessGame()  # Initialize your ChessGame instance

@app.route('/')
def index():
    return render_template('index.html')  # Render your HTML template

@app.route('/board')
def display_board():
    svg_board = chess.svg.board(board=game.board)
    return svg_board, 200, {'Content-Type': 'image/svg+xml'}

@app.route('/move', methods=['POST'])
def make_move():
    move = request.form['move']
    if game.make_move(move):
        return "Move successful"
    else:
        return "Invalid move"

if __name__ == '__main__':
    app.run(debug=True)
