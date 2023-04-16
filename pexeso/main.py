import game
import sys

if len(sys.argv) > 1:
    game = game.Game(tuple(map(int, sys.argv[1].split("x"))), "Pexeso", 0)
else:
    game = game.Game((1280, 720), "Pexeso", 0)
game.run()
