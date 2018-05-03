from enum import Enum
from Tile import Tile


class SquareType(Enum):
    """
      Enum to represent the multiplier for a square. Normal squares have a multiplier of 1 (no change). 
    """
    NORMAL = 1
    DOUBLE_LETTER = 2
    TRIPLE_LETTER = 3
    DOUBLE_WORD = 2
    TRIPLE_WORD = 3
    

class Square:
    """
      Class to represent a board square.
      Each square has a multiplier value dictated by its square type. 
      Args:
      occupied(bool): True if square is occupied, false otherwise. 
    """
    def __init__(self, square_type = SquareType.NORMAL, cur_tile = None):
        self.square_type = square_type
        self.cur_tile = cur_tile
        if self.cur_tile == None:
            self.occupied = False
        else:
            self.occupied = True


    def add_tile(self, supplied_tile):
        self.cur_tile = supplied_tile
        if supplied_tile != None:
            self.occupied = True
            
            
            
        
