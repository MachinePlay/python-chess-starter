# python-chess-starter

A minimal [UCI](https://en.wikipedia.org/wiki/Universal_Chess_Interface) chess
engine you can fork to build your own [machineplay](https://machineplay.org)
bot. Out of the box it plays the first legal move — your job is to make it play
better.

## What's here

- `main.py` — the whole engine: a small UCI loop plus a `choose_move` function.
- `pyproject.toml` — dependencies (just [python-chess](https://python-chess.readthedocs.io)),
  managed with [uv](https://docs.astral.sh/uv/).

## Quick start

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then:

```sh
uv sync
uv run python main.py
```

The engine now waits for UCI commands on stdin. Try a quick conversation
(type the lines without the `>`):

```
> uci
id name first-legal-move
id author your-name-here
uciok
> position startpos
> go
bestmove g1h3
```

`g1h3` is the first legal move from the starting position. Type `quit` to exit.

## Make it your own

All of the chess "thinking" lives in one function in `main.py`:

```python
def choose_move(board: chess.Board) -> chess.Move:
    return next(iter(board.legal_moves))
```

`board` is a [`chess.Board`](https://python-chess.readthedocs.io/en/latest/core.html#board).
Return any legal `chess.Move` and the engine plays it. Some ideas, roughly in
order of difficulty:

1. **Random mover** — `random.choice(list(board.legal_moves))`.
2. **Greedy** — prefer captures, or the move that wins the most material.
3. **Minimax** — search a few moves ahead with a simple evaluation function.

(The random-mover and minimax tutorials build directly on this template.)

## Uploading to machineplay

Coming soon — you'll package this engine as a Docker image and upload it from
your machineplay profile.
