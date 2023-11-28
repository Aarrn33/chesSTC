import time
import chess

board=chess.Board()

legal_moves=board.legal_moves

while True :
    board.puss(legal_moves[0])
    print(board)
    time.sleep(1)