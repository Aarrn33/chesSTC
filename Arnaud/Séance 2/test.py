import chess


def eval(board):
    pieces_values = {"K": 900, "Q": 90, "R": 50, "N": 30, "B": 30, "P": 10}
    if board.turn:
        player = chess.WHITE  # lettres majuscules
    else:
        player = chess.BLACK  # lettres minuscules

    white_pieces = []
    black_pieces = []
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            if piece.symbol().isupper():
                white_pieces.append(piece)
            else:
                black_pieces.append(piece)


board = chess.Board()
eval(board)

legal_moves = list(board.legal_moves)
