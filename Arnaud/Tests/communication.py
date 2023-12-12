# Stolen from https://github.com/healeycodes/andoma/blob/main/communication.py
import chess
import sys
from movegen import next_move


def talk():
    board = chess.Board()
    depth = 4
    while True:
        msg = input()
        print(msg)
        command(depth, board, msg)


def command(depth: int, board: chess.Board, msg: str):
    msg = msg.strip()
    tokens = msg.split(" ")
    while "" in tokens:
        tokens.remove("")

    if msg == "quit":
        sys.exit()

    if msg == "uci":
        print("id name ChesSTC_bot")
        print("id author Arnaud le Masne de Chermont")
        print("uciok")
        return

    if msg == "isready":
        print("readyok")
        return

    if msg == "ucinewgame":
        return

    if msg.startswith("position"):
        if len(tokens) < 2:
            return

        # Sets starting position
        if tokens[1] == "startpos":
            board.reset()
            moves_start = 2
        elif tokens[1] == "fen":
            fen = " ".join(tokens[2:8])
            board.set_fen(fen)
            moves_start = 8
        else:
            return

        # Apply moves
        if len(tokens) <= moves_start or tokens[moves_start] != "moves":
            return

        for move in tokens[(moves_start+1):]:
            board.push_uci(move)

    if msg == "d":
        # Non-standard command, but supported by Stockfish and helps debugging
        print(board)
        print(board.fen())

    if msg[0:2] == "go":
        _move = next_move(depth, board)
        print(f"bestmove {_move}")
        return
