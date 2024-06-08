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


@app.route('/play_ai_redirect', methods=['POST', 'GET'])
def play_ai_redirect():
    if request.method == 'POST':
        print("Data received in POST request to /play_ai:")
        diff = request.form['difficulty']
        print('the diff in play_ai is' + request.form['difficulty'])
        return redirect(url_for("play_ai", difficulty = diff))
    else:
        print('GET REQUEST')
        difficulty = request.args.get('difficulty')  # Retrieve difficulty for GET request

    
    # return render_template('index.html', mode='ai', difficulty=difficulty)


@app.route('/play_ai/<difficulty>')
def play_ai(difficulty):
    print('got to redirect url endpoint')
    return render_template("index.html", mode = 'ai', difficulty = difficulty)


@app.route('/board')
def display_board():
    svg_board = game.display_board()
    return svg_board, 200, {'Content-Type': 'image/svg+xml'}

@app.route('/move', methods=['POST'])
def make_move():
    move = request.form['move']
    mode = request.form['mode']
    if game.make_move(move):
            if game.board.is_game_over():
                print('game is over')
                return redirect(url_for('gameOver'))
        
            return "Move successful"
    else:
            return "Invalid move"

@app.route('/ai_move', methods=['POST'])
def ai_move():
    move = request.form['move']
    mode = request.form['mode']
    difficulty = request.form['difficulty']

    if game.make_move_against_ai(move, difficulty):
        if game.board.is_game_over():
            print('game is over')
            return redirect(url_for('gameOver'))
        
        return "Move successful"

    else:
        return "Invalid move"






@app.route('/gameOver', methods = ['GET'])
def gameOver():
    #reset to board position using FEN
    winning_color = ""
    if game.board.is_checkmate():
        winning_color = "White" if game.board.turn == chess.BLACK else "Black"
    elif game.board.is_stalemate() or game.board.is_insufficient_material() or game.board.is_seventyfive_moves() or game.board.is_fivefold_repetition():
        winning_color = "Draw"
    
    return f'Game over! The winner is {winning_color}'


@app.route('/reset_game')
def reset_game():
    print('BOARD HAS BEEN RESET')
    game.board.set_fen(chess.STARTING_FEN)
    return "success reset"






if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8080, debug=True)
