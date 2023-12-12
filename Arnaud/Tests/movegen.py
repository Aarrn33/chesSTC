from typing import Dict, List, Any
import time
import chess
from eval import eval

debug_info: Dict[str, Any] = {}


def next_move(depth: int, board: chess.Board, debug=False) -> chess.Move:
    debug_info.clear()
    debug_info["nodes"] = 0
    t0 = time.time()

    # move = get_best_move(depth, board)
    move = list(board.legal_moves)[0]

    debug_info["time"] = time.time() - t0
    if debug == True:
        print(f"info {debug_info}")
    return move


def get_best_move(depth: int, board: chess.Board) -> chess.Move:
    legal_moves = list(board.legal_moves)
    scores = {}
    for move in legal_moves:
        scores[move.uci()] = eval(board.push(move))
