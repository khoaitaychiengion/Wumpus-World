import world, graphics
import sys
import os.path

if __name__ == "__main__":
    wumpus_world = world.WumpusWorld()
    map_name = "original.txt"
    wumpus_world.read_Map('../map/' + map_name)
    board = graphics.Board(wumpus_world)
    board.createWorld()
    board.mainloop()

