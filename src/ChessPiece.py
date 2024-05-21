class ChessPiece:
    def __init__(self, color, position):
        self.color = color
        #color == 'white'or 'black'
        self.position = position
        #position is a list 
        #position[0] = row, position[0] = column

    def move(self, new_position):
        self.position = new_position

    def get_legal_moves(self):
        # This method should be overridden in subclasses
        raise NotImplementedError("This method should be overridden in a subclass")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color}, {self.position})"

class Pawn(ChessPiece):
    def __init__(self, color):
        self.color = color
        self.has_moved = False  # Add a flag to track if the pawn has moved

    def get_legal_moves(self):
        # Implement legal moves for a pawn
        legal_moves = []

        # Define movement direction based on the pawn's color
        direction = -1 if self.color == 'white' else 1

        # Check one square forward
        new_row = position[0] + direction
        new_col = position[1]
        if 0 <= new_row < 8 and board[new_row][new_col] is None:
            legal_moves.append((new_row, new_col))
        
        #two square move
        if not self.has_moved:
            new_row += direction
            if 0 <= new_row < 8 and board[new_row][col] is None:
                moves.append((new_row, col))

        # Check diagonal squares for capturing opponent pieces
        for delta_col in (-1, 1):
            new_row = position[0] + direction
            new_col = position[1] + delta_col
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                    legal_moves.append((new_row, new_col))

        # Check for pawn promotion, NEED TO DO
        if (self.color == 'white' and row == 0) or (self.color == 'black' and row == 0):
            # Add promotion moves
            promotion_pieces = ['queen', 'rook', 'bishop', 'knight']
            for new_piece in promotion_pieces:
                moves.append((new_row, col, new_piece))

        return legal_moves

      def move(self):
        self.has_moved = True

class Knight(ChessPiece):
    def get_legal_moves(self):
        # Implement legal moves for a knight
        moves = []
        row, col = self.position
        move_offsets = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        for deltarow, deltacolumn in move_offsets:
            new_row, new_col = row + deltarow, col + deltacolumn
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                moves.append((new_row, new_col))
        return moves

class Bishop(ChessPiece):
    def get_legal_moves(self):
        # Implement legal moves for a bishop
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for deltarow, deltacolumn in directions:
            for i in range(1, 8):
                new_row, new_col = self.position[0] + deltarow * i, self.position[1] + deltacolumn * i
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))
        return moves

class Rook(ChessPiece):
    def get_legal_moves(self):
        # Implement legal moves for a rook
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for deltarow, deltacolumn in directions:
            for i in range(1, 8):
                new_row, new_col = self.position[0] + deltarow * i, self.position[1] + deltacolumn * i
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))
        return moves

class Queen(ChessPiece):
    def get_legal_moves(self):
        # Implement legal moves for a queen (combination of rook and bishop)
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        for deltarow, deltacolumn in directions:
            for i in range(1, 8):
                new_row, new_col = self.position[0] + deltarow * i, self.position[1] + deltacolumn * i
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))
        return moves

class King(ChessPiece):
    def get_legal_moves(self):
        # Implement legal moves for a king, as well as castling``
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        for deltarow, deltacolumn in directions:
            new_row, new_col = self.position[0] + deltarow, self.position[1] + deltacolumn
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                #HAVE TO ADD CONDITIONS FOR KING THAT CANNOT GO INTO CHECK
                if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                moves.append((new_row, new_col))
        return moves

def test():
    print('juju')
