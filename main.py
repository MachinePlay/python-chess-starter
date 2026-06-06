"""A minimal UCI chess engine.

This is the starter template for machineplay. It speaks just enough of the
UCI (Universal Chess Interface) protocol to play a full game, and its
"thinking" is as simple as it gets: it always plays the first legal move.

Your job is to make it play *better*. Everything that matters lives in the
`choose_move` function below — the next tutorials build a random mover and then
a minimax search on top of this same skeleton.

Try it locally with:

    uv run python main.py

then type `uci`, `position startpos`, `go` and watch it reply with a move.
"""

import sys

import chess


def choose_move(board: chess.Board) -> chess.Move:
    """Pick a move to play in the given position.

    This is the only function you need to change. Right now it returns the
    first legal move python-chess offers. Some ideas, easiest first:

      * pick a random move with ``random.choice(list(board.legal_moves))``
      * prefer captures, or the move that wins the most material
      * search a few moves ahead with minimax and a simple evaluation
    """
    return next(iter(board.legal_moves))


def parse_position(command: str) -> chess.Board:
    """Build a board from a UCI ``position`` command.

    Handles the three forms the protocol allows:

        position startpos
        position startpos moves e2e4 e7e5
        position fen <fen> moves ...
    """
    tokens = command.split()

    if tokens[1] == "startpos":
        board = chess.Board()
        moves_index = 2
    else:  # tokens[1] == "fen"
        fen = " ".join(tokens[2:8])
        board = chess.Board(fen)
        moves_index = 8

    if len(tokens) > moves_index and tokens[moves_index] == "moves":
        for uci in tokens[moves_index + 1 :]:
            board.push_uci(uci)

    return board


def main() -> None:
    board = chess.Board()

    while True:
        line = sys.stdin.readline()
        if not line:  # stdin closed
            break
        command = line.strip()

        if command == "uci":
            print("id name first-legal-move")
            print("id author your-name-here")
            print("uciok")
        elif command == "isready":
            print("readyok")
        elif command == "ucinewgame":
            board.reset()
        elif command.startswith("position"):
            board = parse_position(command)
        elif command.startswith("go"):
            move = choose_move(board)
            print(f"bestmove {move.uci()}")
        elif command == "quit":
            break

        sys.stdout.flush()


if __name__ == "__main__":
    main()
