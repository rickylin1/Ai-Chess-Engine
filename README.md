Implemented minimax algorithm with the general idea of
- The bot will create a decision tree of a specified depth and search for the most optimal move
- Optimal move is found based on a heuristic of current board position and piece values
- Alpha beta pruning is implemented to cut down move checking for efficiency assuming that the player will play most optimal next move ("greedy")

Reference video


[![Alt text](https://img.youtube.com/vi/l-hh51ncgDI/0.jpg)](https://www.youtube.com/watch?v=l-hh51ncgDI)


# Features
- Difficulty Level of 1, 2, or 3 to specify the depth the bot will look forward into
- Play against a friend or against a bot

# Instructions
- For pawn moves, you only need to specify the destination square (e.g., "e4").
- For capturing moves, use "x" to denote capture (e.g., "exd5").
- For castling, use "O-O" for kingside castling and "O-O-O" for queenside castling.
- For pawn promotion, append the promotion piece at the end of the move (e.g., "e8=Q" for promoting to a queen).
- If a move is invalid, you'll receive an error message and be prompted to enter a valid move.
