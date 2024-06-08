from flask import Flask, jsonify, render_template, request, redirect, url_for
import chess
import chess.svg
from GameSetup import ChessGame  # Import ChessGame directly

app = Flask(__name__)
game = ChessGame()  # Initialize your ChessGame instance

@app.route('/')
def setup():
    return render_template('setup.html')

@app.route('/play_2_players', methods=['GET','POST'])
def play_2_player():
    if request.method == 'POST':
        print("Data received in POST request to /play_2_players:")
        print(request.form['difficulty'])
        return 'play_2_players',200
    else:
        print('GET REQUEST')
        difficulty = request.args.get('difficulty')  # Retrieve difficulty for GET request
        
    return render_template('index.html', mode='2_player', difficulty=difficulty)

#GET IS THE URL WEBPAGE YOU SEE WHICH RETURNS THE RENDER TEMPLATE
#POST WILL PARSE INFO AND JUST RETURN GET
@app.route('/play_ai', methods=['POST', 'GET'])
def play_ai():
    if request.method == 'POST':
        print("Data received in POST request to /play_ai:")
        difficulty = request.form['difficulty']
        print(request.form['difficulty'])
        return jsonify({'mode': 'play_ai', 'difficulty': difficulty}), 200
    else:
        print('GET REQUEST')
        difficulty = request.args.get('difficulty')  # Retrieve difficulty for GET request
        print(difficulty)
    
    return render_template('index.html', mode='ai', difficulty=difficulty)


@app.route('/board')
def display_board():
    svg_board = game.display_board()
    return svg_board, 200, {'Content-Type': 'image/svg+xml'}

@app.route('/move', methods=['POST'])
def make_move():
    move = request.form['move']
    mode = request.form['mode']
    if game.make_move(move):
        return "Move successful"
    else:
        return "Invalid move"

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8080, debug=True)
