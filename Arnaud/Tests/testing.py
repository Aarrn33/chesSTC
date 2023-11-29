import chess
import chess.pgn


def eval(board: chess.Board):
    pieces_values = {"K": 900, "Q": 90, "R": 50, "N": 30, "B": 30}
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            print(piece)


pgn = open("Arnaud/PGN/Firouzja.pgn")
game = chess.pgn.read_game(pgn)

board = game.board()
eval(board)
lm = board.legal_moves
