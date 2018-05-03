import copy
import random
from Tile import Tile

class Bag:
    """
       Class to represent a bag of tiles used in a game of Scrabble.
    """
    

    def __init__(self, letter_freq_and_val1 = None):
        
        self.all_tiles = []
        self.letter_freq_and_val = letter_freq_and_val1
        if letter_freq_and_val1 is None:
             #use the default dist if not provided with one. 
             self.letter_freq_and_val = {"E":(12,1), "A":(9, 1), "I":(9, 1), "O":(8, 1), "N":(6, 1), "R":(6,1),
                                "T":(6,1), "L":(4, 1), "S":(4,1), "U":(4, 1), "D":(4,2), "G":(3,2),
                                "B":(2,3), "C":(2,3), "M":(2,3), "P":(2,3), "F":(2,4), "H":(2,4),
                                "V":(2,4), "W":(2,4), "Y":(2,4), "K":(1,5), "J":(1,8), "X":(1,8),
                                "Q":(1,10), "Z":(1,10), "BLANK":(2,0)}
             print("Using default")

             
        self.all_tiles = self.get_full_bag()
        self.initial_tile_num = len(self.all_tiles)

       


        self.available_tiles = self.deep_copy_tiles(self.all_tiles) #initially, all the tiles are available. tiles removed as game progresses.
        self.shake_bag(self.available_tiles)

        
        

    
    def get_full_bag(self):
        """Return a full bag of letters, according to the specific distribution of a given bag."""
        
            
        bag_of_tiles = []
        
        for letter in self.letter_freq_and_val.keys():
            #for each letter, make appropriate number of tiles
            
            letter_freq = self.letter_freq_and_val[letter][0] #the number of times letter occurs. 
            letter_val = self.letter_freq_and_val[letter][1]   #the value of the letter
             
            for i in range(1, letter_freq + 1): #want to make N tiles with the current letter, where N is letter_freq. +1 is because range() doesn't include last element
                new_tile = Tile(letter, letter_val)
                bag_of_tiles.append(new_tile)
        return bag_of_tiles
    

    def shake_bag(self, tile_bag):
        """Ordinarily, tiles appear in a specific order. Randomly arrange them"""
        random.seed(5) #5 chosen arbitrarily; however, want numbers to be arranged randomly in the same fashion whenever method is called. 
        random.shuffle(tile_bag)
        

    def deep_copy_tiles(self, list_of_tiles):
        new_tile_list = copy.deepcopy(list_of_tiles)
        return new_tile_list


    def print_tiles(self, tiles_to_print):
        """Print a supplied list of tiles"""
        for cur_tile in tiles_to_print:
            print(cur_tile)


    def pick_tiles(self, num_tiles_to_pick):
        picked = 0
        new_tiles = []
        while(picked < num_tiles_to_pick and len(self.available_tiles)>0):
            #pick specified amount of tiles insofar as they are available
            #once tile is picked, remove from bag (i.e. list of available tiles)

            new_tile = random.choice(self.available_tiles) #get a random tile. now need to remove the said random tile from list of available tiles
            self.available_tiles.remove(new_tile) #only removing an identical tile; however, equivalent to removing actual tile in scrabble game

            new_tiles.append(new_tile)
            picked = picked + 1 # increase count of num of tiles picked.

            
        return new_tiles


   

    

    def tiles_finished(self):
        """
           Check if there are still tiles to be drawn from the bag.
           Returns:
           True if all tiles have been picked, False otherwise.
        """
        some_tiles_left =  len(self.available_tiles) > 0
        return not some_tiles_left 
        
            
            
    
        

        
