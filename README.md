<h1> NotSoDeepBlue </h1>
Inspired by Deep Blue, the IBM supercomputer that revolutionized the chess industry by beating Garry Kasparov







<h3> Frontend  </h3>
- React, Tailwind CSS

<h3> Backend </h3>
- Flask RESTFUL API

<h3> Algorithm </h3>
Implemented minimax algorithm with the general idea of
- The bot will create a decision tree of a specified depth and search for the most optimal move
- Optimal move is found based on a heuristic of current board position and piece values
- Alpha beta pruning is implemented to cut down move checking for efficiency assuming that the player will play most optimal next move ("greedy")

Reference video


[![Alt text](https://img.youtube.com/vi/l-hh51ncgDI/0.jpg)](https://www.youtube.com/watch?v=l-hh51ncgDI)


# Features
- Difficulty Level of 1, 2, or 3 to specify the depth of tree to branch into
- Play against a friend or against a bot

# Instructions


# Instructions to enter moves
- For pawn moves, you only need to specify the destination square (e.g., "e4").
- For capturing moves, use "x" to denote capture (e.g., "exd5").
- For castling, use "O-O" for kingside castling and "O-O-O" for queenside castling.
- For pawn promotion, append the promotion piece at the end of the move (e.g., "e8=Q" for promoting to a queen).
- If a move is invalid, you'll receive an error message and be prompted to enter a valid move.

# Lessons
- Flask applications can post, and get, also have render templates and GINGA which can simplify.
- Had trouble redirecting urls for ai different difficulty and calling the logic from frontend back to the algorithm
- Initially had the game run in terminal, then used redirect urls on flask api, then finally deployed a frontend to link to backend

# Improvements
- Can deploy GUI drag and drop instead of manual typing
