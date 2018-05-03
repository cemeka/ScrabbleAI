from Board import Board
from Bag import Bag
from Agent import Agent
import copy




class GameManager:

    def __init__(player1=Agent("baseline"), player2=Agent("baseline"), gameboard = None, tilebag = None):
        self.player1 = player1
        self.player2 = player2

        self.game_board = gameboard
        if gameboard == None:
            self.game_board = Board(15) #initialize to a standard game board if none provided.
        
            
        
        self.tile_bag = tilebag
        if tilebag == None:
            self.tile_bag = Bag() #initialize a full tile bag if none is provided.
            
        self.who_goes_first()
            
    
            
    def who_goes_first(self):
        """
           Determine who goes first by simulating both players picking a tile from the bag and seeing which is closer to "A"
           i.e. player with smaller letter goes first (where A is the smallest and Z is the largest).
           If same letter is picked by both players, redraw
           Then initialize players' racks. 
        """

        
        dummybag = copy.deep_copy(self.tile_bag)
        playerA_tile = dummybag.pick_tiles(1)
        playerB_tile = dummybag.pick_tiles(1)

        if playerA_tile.letter == playerB_tile.letter:
            self.who_goes_first() #call method recursively until we have a difference. 
            
        if playerA_tile.letter < playerB_tile.letter:
            playerA.agent_goes_first = True
        else:
            playerB.agent_goes_first = True

        #add those tiles to the rack of the respective players.
        playerA.rack.append(playerA_tile)
        playerB.rack.append(playerB_tile)

        #remove those tiles from the original bag
        self.tile_bag.remove(playerA_tile)
        self.tile_bag.available_tiles.remove(playerA_tile)
        self.tile_bag.available_tiles.remove(playerB_tile)
        print("After removing first two tiles, {} tiles left in bag".format(len(self.tile_bag.available_tiles)))


        self.player1.get_tiles(6) #get 6 tiles for agent 1 and store in their rack. 
        self.player2.get_tiles(6) #get 6 tiles for agent  2 and store in their rack.

        

        
        
        
        
            
            
    def play_round():
        """Play one round of the game. If playerB were to play first, according to board initialization, this should happen before method is called."""
        
        
    def game_over(self):
        game_done = False
        
        if len(self.player1.rack) == 0 and self.tile_bag.tiles_finished() : #game is over. tally score for the two players
            game_done = True
            opp_rack_total = 0
            for curTile in self.player2.rack:
                opp_rack_total += curTile.value
                
            
    
            self.player1.cur_score += opp_rack_total
            self.player2.cur_score -= opp_rack_total #the opponent loses points equivalent to the total value of his (i.e. the opponent's) rack



         #check the equivalent case for the second player. 

         if len(self.player2.rack) == 0 and self.tile_bag.tiles_finished() :
            game_done = True
            opp_rack_total = 0
            for curTile in self.player1.rack:
                opp_rack_total += curTile.value
                
            
    
            self.player2.cur_score += opp_rack_total
            self.player1.cur_score -= opp_rack_total


         if (game_done == True):
             print("Game is over.")
         else:
             print("Game continuing.")
            
            
            
