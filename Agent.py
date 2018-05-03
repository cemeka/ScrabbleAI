from Bag import Bag
from Utils import Utils
import Utils
from Board import Board
from Tile import Tile 
import copy



class Agent:
    """
       This is the baseline agent.
       It simply picks the move that maximizes its score, without looking for other features of the game.
       
    """


    def __init__(self, agent_name, myboard, game_bag):
        """
           Args: game_bag(Bag): should be shared by all players in a game. 
        """
        
        self.agent_name = agent_name #can be NN agent, Baseline agent etc.
        self.agent_goes_first = False #set to true if agent goes first.
        self.played = False #keep track of whether agent has played. 
        self.rack = [] #these are the tiles that the agent currently has in hand
        self.myboard  = myboard #this is the game board. should be shared between players. 
        self.game_bag = game_bag #this is the game bag (containing tiles). should be shared between players.
        self.cur_score = 0 #this is the current score tally for an agent.

    
    def choose_move(self):
        """
           Move should be a tuple in the form of (word, starting location to place, vertical/horizontal)
           E.g. ("boy", (1,1), "horizontal")
        """
         
        return None


    def compute_score(self, new_word, previous_score = 0):
        """
           Compute scores according to a given distribution in the bag
           Args: new_word(string): a word to compute a score for.
        """
    
            
        score = previous_score
        new_word = new_word.replace("<-", "").replace("->", "")
        for cur_char in new_word:
            score = score + self.game_bag.letter_freq_and_val[cur_char][1] #the points assigned for the current character. 
        return score

    
    def all_valid_moves(self, cur_board, all_english_words):
         """Return a list of all valid moves given his rack of tiles, the current board state and a list of all possible words in the language"""
         rack_to_str = self.convert_rack_to_str()
         if len(rack_to_str) == 0:
             return [] 
          
         moves_made = cur_board.find_words_on_board()
         actual_words = []

         if cur_board.board_empty: #no one has played yet.
             return Utils.get_all_legal_combos([""], rack_to_str, all_english_words)



             
         for move in moves_made:
             actual_words.append(move[0]) #the first element is a string, representing the actual move made.
             
        
         return Utils.get_all_legal_combos(actual_words, rack_to_str, all_english_words)
         
         
    def get_tiles(self, numTiles, gameBag):
        """Pick a specified number of tiles from a tile bag"""
        tiles_picked = gameBag.pick_tiles(numTiles)
        for givenTile in tiles_picked:
            self.rack.append(givenTile)
            
    def print_rack(self):
          hand = ""
          for tileT in self.rack:
              if tileT is not None:
                  hand = hand + tileT.letter

          print("My rack is " + hand)

    def convert_rack_to_str(self):
        myrack = ""
        for val in self.rack:
            myrack += val.letter;
        return myrack

    def detect_word_overlap(self, direction, old_word, new_word):
        """Unless the board is empty, the agent plays to overlap current tiles, per scrabble rules. """
        #get the location of the old_word
        old_move_data = self.myboard.find_specific_word(old_word) #all the instances of the old word.
        print("This is the data collected {}".format(old_move_data))
        print("New word to place is {}".format(new_word))

        for move_data in old_move_data:
            
            x = move_data[1]
            y = move_data[2]
            limit = len(old_word)
            old_word_duplicate = ""

            if self.myboard.board_empty:
                return True #Special case: board is empty, so we can use all squares.
            
            results = []
            if direction == "horizontal":
                    row = x
                    for col in range(y, y + limit):
                        cur_letter = self.myboard[row][col].curTile.letter
                        if cur_letter is None:
                            if len(old_word_duplicate) > 0:
                                results.append(old_word_duplicate)
                                old_word_duplicate = ""
                             
                        else:
                              old_word_duplicate += cur_letter

                    results.append(old_word_duplicate) # save last value
                    for prev_word in results:
                        if (len(prev_word) > 0 and new_word.startswith(prev_word) or new_word.endwith(prev_word)):
                                return True

            old_word_duplicate = ""
            full_results = []
            if direction == "vertical":
                 col = y 
                 for row in range(x, x + limit):
                      cur_letter = self.myboard[row][col].curTile.letter
                      if cur_letter is None:
                            if len(old_word_duplicate) > 0:
                                results.append(old_word_duplicate)
                                old_word_duplicate = ""
                      else:
                          old_word_duplicate += cur_letter

                          
                 results.append(old_word_duplicate) # save last value
                 for prev_word in results:
                        if (len(prev_word) > 0 and new_word.startswith(prev_word) or new_word.endwith(prev_word)):
                                return True
                
            return False
                
    
        
    def put_in_move_slots(self, good_word, all_eng_words):
         new_word = good_word.replace("->", "").replace("<-", "")
         old_word = ""

         board_words = self.myboard.find_words_on_board()
         
         if "->" in good_word:
             old_word = good_word.split("->")[1]
         elif "<-" in good_word:
             old_word = good_word.split("<-")[0]
             
         done = False
         #determine where to place a move that has been found. 
         for x in range(self.myboard.board_dimension):
             for y in range(self.myboard.board_dimension):
                 for direction in ["vertical", "horizontal"]:
                       try:
                           noOverLap = self.detect_word_overlap(direction, old_word, new_word)
                           if noOverLap == False:
                               print("Not a valid position to place tile. Skip")
                               continue
                           
                           done = self.play_move((new_word, x, y, direction), all_eng_words)
                        
                           if done:
                               self.deduct_from_rack(old_word, new_word)
                               self.played = True
                               print("Played 1 turn of game.")
                               return done
                       except:
                            continue
        
         return done
                
         
    def play_turn(self, cur_board, all_english_words):

        #Replenish tiles when exhausted.
        
        all_comp_choices = self.all_valid_moves(cur_board, all_english_words)
        scores = []
        
       
        for choice in all_comp_choices:
            choice_score = self.compute_score(choice)
            scores.append(choice_score)


        scores, all_comp_choices = zip(*sorted(zip(scores, all_comp_choices)))

        scores, all_comp_choices = (list(t) for t in zip(*sorted(zip(scores, all_comp_choices))))


      
        while (len(scores) > 0 and self.played == False): #try to play best move
            scores.pop()
            best_word = all_comp_choices.pop()
            print("Best word is ")
            self.put_in_move_slots(best_word, all_english_words)
            
        self.played = False #reset in anticipation of next move.

        #replace tiles. need new tiles in preparation for next turn.
        tiles_needed = max(7 - len(self.rack), 0)
        self.get_tiles(tiles_needed, self.game_bag)
            
            
            
        
            

        #
    def deduct_from_rack(self, old_word, new_word):
        """After you've played, remove those tiles from the rack"""
        chrs_used  = new_word.replace(old_word, "")
        print("Rack previous size = {}".format(len(self.rack)))
        for chr_val in chrs_used:
            used_tile = Tile(chr_val, self.game_bag.letter_freq_and_val[chr_val][1])
            self.rack.remove(used_tile)

        if len(new_word) - len(old_word) >= 7: #used all 7 tiles
            self.cur_score += 50
            
        print("Rack new size = {}".format(len(self.rack)))

    def play_move(self, move_data, all_english_words):
        """
            This method should not be called directly. Use play_turn instead. Handles all aspects of playing. 
            Play a move if it's legal.
            To be legal, move must be a valid word; also, no invalid word can be formed on board after move
            A move comes in the form [new word, starting row location, starting column location, orientation (i.e. horizontal or vertical) ]
        """
        
        #first, make copy of board and try to apply move there.
        board_cpy  = copy.deepcopy(self.myboard)
        
        rack_cpy  = copy.deepcopy(self.rack) #***need to remove appropriate words from rack after we've made a move. 

        i = 0 
        for cur_char in move_data[0]:
            new_tile = Tile(cur_char, self.game_bag.letter_freq_and_val[cur_char][1]) #create a new tile.
            if move_data[3] == "horizontal":
                print("adding cur_char {} at {} {}".format(cur_char, move_data[1], move_data[2]+i))
                board_cpy.place_tile(move_data[1], move_data[2]+ i, new_tile)
            elif move_data[3] == "vertical":
                board_cpy.place_tile(move_data[1] + i, move_data[2], new_tile)

            i = i + 1
            #print("New i value is {}".format(i))
        board_cpy.print_board()
        

        #once we're done placing the tiles, check for validity of entire board.
        cur_board_words =  board_cpy.find_words_on_board()
        move_valid = True #assume move is valid, until proven otherwise.

        for word_data in cur_board_words:
            word = word_data[0]
            print(word)
            if word not in all_english_words:
                return False #do nothing else
            
        #print("Getting here; all words valid")
             
        #getting here means that the move is actually valid, with no conflicts.
        main_board = self.myboard
        #In this case, add to the real board. 
        i = 0 
        for cur_char in move_data[0]:
            new_tile = Tile(cur_char, self.game_bag.letter_freq_and_val[cur_char][1]) #create a new tile.
            if move_data[3] == "horizontal":
                main_board.place_tile(move_data[1], move_data[2]+ i, new_tile)
            elif move_data[3] == "vertical":
                main_board.place_tile(move_data[1] + i, move_data[2], new_tile)

            i = i + 1
        return True
        

    
    
    
        
        


        
        
