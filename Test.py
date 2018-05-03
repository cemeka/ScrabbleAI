
from Bag import Bag
from Board import Board

b = Board(5)
b.print_board()
myBag = Bag()
b.game_board[1][2].add_tile(myBag.all_tiles[9])
print("----------------")
b.print_board()
