from Bag import Bag
from Tile import Tile
from Board import Board
from Utils import Utils
from Agent import Agent
import os


game_bag = Bag()
game_bag.print_tiles(game_bag.all_tiles)


u = Utils()
myBoard = Board(7)


myBoard.print_board()





agentA = Agent("Baseline", myBoard, game_bag)
agentA.get_tiles(7, game_bag)
agentA.print_rack()
agentA.all_valid_moves(myBoard, u.valid_words)


val = agentA.play_move(["BEST", 6,1, "horizontal"], u.valid_words)
agentA.play_move(["CAB", 4,1, "vertical"], u.valid_words)
print("---------------")

print(val)
myBoard.print_board()
print(myBoard.find_specific_word("CAB"))

agentA.get_tiles(7, game_bag)


print(len(agentA.rack))

print("before playing, had {} tiles".format(len(agentA.rack)))


done = agentA.play_turn(myBoard, u.valid_words)

agentA.print_rack()





"""


print("after playing, now has {} tiles".format(len(agentA.rack)))

#print("Found:")
#print(agentA.myboard.find_specific_word("CAB"))
#agentA.detect_word_overlap("vertical", "CAB", "CABLE")


myBoard.print_board()


done = agentA.play_turn(myBoard, u.valid_words)
myBoard.print_board()

