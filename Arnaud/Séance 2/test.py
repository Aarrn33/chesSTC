import chess


def eval(board):
    PIECES_VALUES = {"K": 900, "Q": 90, "R": 50, "N": 30, "B": 30, "P": 10}
    if board.turn:
        player = chess.WHITE  # lettres majuscules
    else:
        player = chess.BLACK  # lettres minuscules

    white_pieces = []
    black_pieces = []
    white_score = 0
    black_score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            if piece.symbol().isupper():
                white_pieces.append(piece)
                sym = piece.symbol()
                white_score += PIECES_VALUES[sym]
            else:
                black_pieces.append(piece)
                sym = piece.symbol().upper()
                black_score += PIECES_VALUES[sym]

    if player == chess.WHITE:
        score = white_score-black_score
    elif player == chess.BLACK:
        score = black_score-white_score

    # print([piece.symbol() for piece in white_pieces], white_score)
    # print([piece.symbol() for piece in black_pieces], black_score)

    return score


board = chess.Board()
iteration = 0
while not board.is_game_over():
    score = eval(board)
    print(score)
    if iteration % 5 == 0:
        print(board)
    legal_moves = list(board.legal_moves)
    board.push(legal_moves[0])
    iteration += 1
