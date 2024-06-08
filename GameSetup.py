import chess
import chess.svg
import os

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def display_board(self):
        svg_board = chess.svg.board(board=self.board)
        with open("chess_board.svg", "w") as f:
            f.write(svg_board)
        print("SVG file has been updated: chess_board.svg")
        #manually open this file in VS Code or any other SVG viewer
        return svg_board

    def make_move(self, move):
        try:
            self.board.push_san(move)
            return True
        except ValueError:
            return False
    
    def make_move_against_ai(self, move, difficulty):
        try:
            self.board.push_san(move)
            eval, bestMove = self.minimax(self.board, difficulty, float('-inf'), float('inf'), True)
            if bestMove:
                self.board.push(bestMove)
                print("AI moves:", bestMove)
                self.display_board()  
            return True
        except ValueError:
            return False
        
    def select_mode(self):
        while True:
            mode = input("Select mode:\n1. Play against another player\n2. Play against AI\nEnter your choice: ")
            if mode == '1':
                self.play_two_players()
                break
            elif mode == '2':
                self.play_ai()
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def play_two_players(self):
        self.display_board()
        while not self.board.is_game_over():
            if self.board.turn == chess.WHITE:
                move = input("White's turn. Enter your move: ")
            else:
                move = input("Black's turn. Enter your move: ")
                
            if self.make_move(move):
                self.display_board()
            else:
                print("Invalid move. Please try again.")
        print("Game over:", self.board.result())


    def play_ai(self):
        self.display_board()
        # Get difficulty mode from the user
        while True:
            difficulty = input("Select difficulty mode:\n1. Easy\n2. Medium\n3. Hard\nEnter your choice: ")
            if difficulty == '1':
                depth = 3
                break
            elif difficulty == '2':
                depth = 5
                break
            elif difficulty == '3':
                depth = 10
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        while not self.board.is_game_over():
            if self.board.turn == chess.WHITE:
                move = input("Enter your move: ")
                if self.make_move(move):
                    self.display_board()
                else:
                    print("Invalid move. Please try again.")
            else:
                print("Computer is thinking...")
                # Call minimax with the selected depth to find the best move for the AI
                eval, bestMove = self.minimax(self.board, depth, float('-inf'), float('inf'), True)
                if bestMove:
                    self.board.push(bestMove)
                    print("AI moves:", bestMove)
                    self.display_board()
                else:
                    print("AI cannot make a move.")
        print("Game over:", self.board.result())

    counter = 0
    def minimax(self, position, depth, alpha, beta, maximizingPlayer):
        ChessGame.counter += 1
        print('enter' + str(ChessGame.counter))
        # Base case: if the depth is 0 or the game is over
        if depth == 0 or position.is_game_over():
            return self.evaluate_heuristic(position), None

        if maximizingPlayer:
            maxEval = float('-inf')
            bestMove = None
            for move in position.legal_moves:
                position.push(move)
                eval, _ = self.minimax(position, depth - 1, alpha, beta, False)
                position.pop()
                if eval > maxEval:
                    maxEval = eval
                    bestMove = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
            return maxEval, bestMove
        else:
            minEval = float('inf')
            bestMove = None
            for move in position.legal_moves:
                position.push(move)
                eval, _ = self.minimax(position, depth - 1, alpha, beta, True)
                position.pop()
                if eval < minEval:
                    minEval = eval
                    bestMove = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
            return minEval, bestMove
        
    def evaluate_heuristic(self, position):
        material_value = {
            chess.QUEEN: 9,
            chess.ROOK: 5,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.PAWN: 1,
            chess.KING: 1000
        }
        score = 0
        for square in chess.SQUARES:
            piece = position.piece_at(square)
            if piece is not None:
                score += material_value[piece.piece_type]

        return score
        


    

# To play the game, create an instance of the ChessGame class and call the play method
if __name__ == "__main__":
    game = ChessGame()
    game.select_mode()
