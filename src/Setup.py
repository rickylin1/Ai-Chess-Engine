import ChessPiece

#NOTE POTENTENTIALLY USE FEN TO LOAD IN POSITIONS LATER, BUT FOR NOW WE WILL JUST MANUALLY DO IT
class Board:
      def __init__(self):
            self.board = self.createBoard()
     
      def createBoard(self):
      # Declare a 2D array with 8 rows and 8 columns as board
      #board has white on the bottom and black on the top
            rows, cols = 8, 8
            board = [[0 for _ in range(cols)] for _ in range(rows)]
            lightsquare = 0

            for i in range(len(board)):
                  #light square first in row, for now we will represent a light square with 1
                  if i % 2 == 0:
                        for j in range(0, len(board[i]), 2):
                              board[i][j] = 1
                              
                  #dark square first in row
                  else:
                        for j in range(1, len(board[i]), 2):
                              board[i][j] = 1
                  
                  print(board[i])
            return board
                  
      
      def setup_chess_pieces(self):
        # Place chess pieces on the board
        # Example: Placing pawns on the board
            for col in range(8):
                  self.board[6][col] = ChessPiece.Pawn("white",[6,col])  # Place white pawns on row 7
                  self.board[1][col] = ChessPiece.Pawn("black", [6,col])  # Place black pawns on row 2

            #kings 
            self.board[7][4] = ChessPiece.King("white", [7,4])
            self.board[0][4] = ChessPiece.King("black", [6,4])

            #queens
            self.board[7][3] = ChessPiece.King("white", [7,3])
            self.board[0][3] = ChessPiece.King("black", [0,3])

            #rooks
            self.board[0][0], self.board[0][7] = ChessPiece.Rook("black", [0,0]), ChessPiece.Rook("black", [0,7])
            self.board[7][0], self.board[7][7] = ChessPiece.Rook("white", [7,0]), ChessPiece.Rook("white", [7,7])

            #knights
            self.board[0][1], self.board[0][6] = ChessPiece.Rook("black", [0,1]), ChessPiece.Rook("black", [0,6])
            self.board[7][1], self.board[7][6] = ChessPiece.Rook("white", [7,1]), ChessPiece.Rook("white", [7,6])

            #bishops
            self.board[0][2], self.board[0][5] = ChessPiece.Rook("black", [0,2]), ChessPiece.Rook("black", [0,5])
            self.board[7][2], self.board[7][5] = ChessPiece.Rook("white", [7,2]), ChessPiece.Rook("white", [7,5])


      # def __repr__(self):
      #   # Return a string representation of the chessboard
      #   repr_str = ""
      #   for row in self.board:
      #       repr_str += " ".join(str(cell) for cell in row) + "\n"
      #   return repr_str
            


