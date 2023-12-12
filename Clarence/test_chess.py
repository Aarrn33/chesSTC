import time
import chess
from random import*

board=chess.Board()

legal_moves=board.legal_moves
legal_moves=list(legal_moves)

while True :
    board.push(legal_moves[randint(0,len(legal_moves))])
    print(board)
    time.sleep(1)