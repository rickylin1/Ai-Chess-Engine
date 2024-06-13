from flask import Flask, jsonify, render_template, request, redirect, url_for, Response
import chess
import chess.svg
from GameSetup import ChessGame 

app = Flask(__name__)
game = ChessGame()  # Initialize ChessGame using GameSetup
gameBoard = game.board

@app.route('/board')
def board():
    svg = chess.svg.board(gameBoard)
    return Response(svg, mimetype='image/svg+xml')
    return svg, 200, {'Content-Type': 'image/svg+xml'}

@app.route('/play_2_players', methods=['GET','POST'])
def play_2_player():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            print(data['move'])
            if(data['move']):
                game.make_move(data['move'])
                if gameBoard.outcome == chess.Outcome:
                    print('game HAS ENDED')
                #     return str(gameBoard.outcome)
                print('move was made')
            else:
                return jsonify('Invalid move')
            
    return jsonify('Entered play_2_player')
       
@app.route('/play_ai', methods=['GET', 'POST'])
def play_ai_redirect():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            print(data['move'])
            print(data['difficulty'])
            if(data['move']):
                game.make_move_against_ai(data['move'], data['difficulty'])
                print('move was made')
                
            else:
                return jsonify('Invalid move')
            
    return jsonify('Entered play_ai')

@app.route('/gameOver', methods = ['GET'])
def gameOver():
    #reset to board position using FEN
    winning_color = ""
    if game.board.is_checkmate():
        winning_color = "White" if game.board.turn == chess.BLACK else "Black"
    elif game.board.is_stalemate() or game.board.is_insufficient_material() or game.board.is_seventyfive_moves() or game.board.is_fivefold_repetition():
        winning_color = "Draw"
    else:
        return "nobody won"
    
    return f'Game over! The winner is {winning_color}'


@app.route('/reset_game')
def reset_game():
    print('BOARD HAS BEEN RESET')
    game.board.set_fen(chess.STARTING_FEN)
    return "success reset"


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8080, debug=True)
