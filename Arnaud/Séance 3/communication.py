# Stolen from https://github.com/healeycodes/andoma/blob/main/communication.py
import chess
import sys
from movegen import next_move


def play():
    board = chess.Board()

    while not board.outcome():
        board.push(next_move(1, board))
        player_move = 0
        print(board)
        print([str(move) for move in list(board.legal_moves)])
        while player_move not in list(board.legal_moves):
            player_move = chess.Move.from_uci(input(
                "Choisissez un coup valide parmi ceux ci-dessus :\n"))
        board.push(player_move)
