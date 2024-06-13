import chess
import chess.svg

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def make_move(self, move):
        try:
            self.board.push_san(move)
            return True
        
        #value error will occur if it is an invalid, illegal, or ambiguous move
        except ValueError:
            return False
    
    def make_move_against_ai(self, move, difficulty):
        try:
            self.board.push_san(move)
            #by default we will set depth equal to 3 (difficulty 1)
            depth = 3
            if difficulty == '2':
                depth = 5
            elif difficulty == '3':
                depth = 10
            eval, bestMove = self.minimax(self.board, depth, float('-inf'), float('inf'), True)
            if bestMove:
                self.board.push(bestMove)
            return True
        except ValueError:
            return False

    # counter = 0

    def minimax(self, position, depth, alpha, beta, maximizingPlayer):
        # ChessGame.counter += 1
        # print('enter' + str(ChessGame.counter))
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
        


    
if __name__ == "__main__":
    game = ChessGame()
