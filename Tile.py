class Tile:

    """
      class to represent one tile to be used in Scrabble game
    """
    def __init__(self, letter, value = 0):
        if letter is None:
            print("WARNING. INPUTTING NULL")
        self.letter = letter
        self.value = value
        
    def __str__(self):
         return "({ltr} {val})".format(ltr = self.letter, val = self.value)


    def __eq__(self, other):
        if (self.letter == other.letter and self.value == other.value):
            return True
        else:
            return False
