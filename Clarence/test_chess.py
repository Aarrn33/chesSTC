import time
import chess

board=chess.Board()

legal_moves=board.legal_moves

while True :
    board.push(list(legal_moves)[0])
    print(board)
    time.sleep(1)