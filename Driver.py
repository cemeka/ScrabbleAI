from Bag import Bag
from Tile import Tile
from Board import Board
from Utils import Utils
from Agent import Agent
import os


game_bag = Bag()
game_bag.print_tiles(game_bag.all_tiles)
game_bag.available_tiles[0] = Tile("C", 24)
game_bag.available_tiles[1] = Tile("O", 22)
game_bag.available_tiles[2] = Tile("W", 24)
game_bag.available_tiles[3] = Tile("D", 24)
game_bag.available_tiles[4] = Tile("G", 24)
game_bag.available_tiles[5] = Tile("S", 24)
game_bag.available_tiles[6] = Tile("A", 24)
game_bag.available_tiles[7] = Tile("D", 24)


print("----")
game_bag.print_tiles(game_bag.available_tiles)
print("----")
print(game_bag.all_tiles[0])

u = Utils()
myBoard = Board(7)
#place vertically. first val changes, second val remains constant
myBoard.place_tile(4,4, game_bag.available_tiles[1])
myBoard.place_tile(3, 4, game_bag.available_tiles[0])
myBoard.place_tile(5, 4, game_bag.available_tiles[2])

#place horizontally. first val remains constant, second val changes
myBoard.place_tile(4, 3, game_bag.available_tiles[3])
myBoard.place_tile(4, 5, game_bag.available_tiles[4])
myBoard.place_tile(6, 4, game_bag.available_tiles[5])
#myBoard.place_tile(6, 5, game_bag.available_tiles[6])
#myBoard.place_tile(6, 6, game_bag.available_tiles[7])

myBoard.print_board()

print("------------")

words_found = myBoard.find_words_on_board()
for word in words_found:
    print(word)

agentA = Agent("Baseline", myBoard, game_bag)
val = agentA.play_move(["BEAST", 6,1, "horizontal"], u.valid_words)
agentA.play_move(["CAB", 4,1, "vertical"], u.valid_words)
print("---------------")
print(val)
myBoard.print_board()
print(myBoard.find_specific_word("CAB"))

agentA.get_tiles(7, game_bag)

#agentA.deduct_from_rack("HO", "HOWDY")
#print(len(agentA.rack))

#print("before playing, had {} tiles".format(len(agentA.rack)))


done = agentA.play_turn(myBoard, u.valid_words)

agentA.print_rack()


print("Status = {}".format(done))
print("after playing, now has {} tiles".format(len(agentA.rack)))

#print("Found:")
#print(agentA.myboard.find_specific_word("CAB"))
#agentA.detect_word_overlap("vertical", "CAB", "CABLE")


myBoard.print_board()


done = agentA.play_turn(myBoard, u.valid_words)
myBoard.print_board()
