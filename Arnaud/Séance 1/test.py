import chess

board = chess.Board()
print(board)

legal_moves = board.legal_moves
# for move in legal_moves:
# print(move)

board.push(list(legal_moves)[0])
print(board)
