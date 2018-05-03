from Bag import Bag
from Square import Square
from Square import SquareType



class Board:
    """
       Data structure to represent an actual board configuration.
    """

    def __init__(self, board_dimension):
        """
           Args:

           board_dimension(int): Board size is board_dimension * board_dimension
           
           Note that special squares may be used if the board is actually a standard scrabble board (i.e. 15 * 15)
        """
        self.board_dimension = board_dimension
        self.game_board = [] #this is a 2D board which stores squares. Squares may or may not contain tiles.
        

        for column in range(board_dimension):
            new_row = []
            for row in range(board_dimension):
                new_square = Square(square_type = SquareType.NORMAL)
                new_row.append(new_square)
            self.game_board.append(new_row)

    #add logic here for making certain squares special for board.


    def place_tile(self, x, y, tile_to_place):
        """
           Helper method to allow placement of tile quickly at position board[x][y]
        """
       
        self.game_board[x][y].cur_tile = tile_to_place
        


    def print_board(self):
        txt = ""
        for row in self.game_board:
            line_txt = ""
            
            for given_slot in row:
                
                if given_slot.cur_tile is None: #no letter is in that slot. 
                    line_txt = line_txt + " Empty "
                else:
                    cur_string = "   " + given_slot.cur_tile.letter + "   " #adding space manually so output aligned with empty slots
                    line_txt = line_txt + cur_string 
                    
            line_txt = line_txt + "\n"
            txt  = txt + line_txt
        print(txt)
    
         
        
            

    def board_full(self):
        for row in self.game_board:  
           for cur_square  in row:
             if cur_square.cur_tile == None:
                #then we have at least one square to place a tile on.
                return False
        return True

    def board_empty(self):
        for row in self.game_board:  
           for cur_square  in row:
             if cur_square.cur_tile is not None:
                #then we have at least one tile on the board
                return False
        return True

    
    def find_specific_word(self, word):
        instances = []
        all_found = self.find_words_on_board()
        for cur_word_data in all_found:
            if cur_word_data[0] == word:
                instances.append(cur_word_data)
        return instances
        

        
    def find_words_on_board(self):
            """
              Return a list of the words that are currently on the board.
              Because single letter words are invalid in Scrabble, we exclude them from our list of words. 
            """
            words = []
            word_txt = ""

            #horizontal search.
            rowNum = 0
            columnNum = 0
           
            data_pair = []
            
            for row in self.game_board:
                word_txt = "" #reset word text for each horizontal search

                columnNum = 0
                for cur_square in row:
                    tile_present = cur_square.cur_tile is not None
                    
                    if tile_present: #then we have a tile present
                         word_txt += cur_square.cur_tile.letter

                         if len(data_pair) == 0: #don't want to override old info for a given word. 
                             data_pair = [rowNum, columnNum]
                    else:
                        #we're not at a word. save previous word if it actually has text
                        if len(word_txt) > 1:
                            words.append((word_txt, data_pair[0], data_pair[1], "horizontal"))

                        data_pair = []    
                        word_txt = "" #reset word text once we've hit an empty square.
                        
                    columnNum += 1 

                    
                        
                            
                #if we're done with a row, it's possible that there's still text left to be saved.
                if (len(word_txt) > 1):
                    words.append((word_txt, data_pair[0], data_pair[1], "horizontal"))
                rowNum += 1
                   
                    


           
            rowNum = 0
    
            #vertical search   
            for row in range(self.board_dimension):
                word_txt = "" #reset word text for each vertical search
                
                
                for column in range(self.board_dimension):
                   cur_square = self.game_board[column][row] #going vertically (i.e. down the board)
                   
                   tile_present = cur_square.cur_tile is not None
                   
                   if tile_present:
                       word_txt += cur_square.cur_tile.letter
                       data_pair = [column, rowNum]
                   else:
                        #we're not at a word. save previous word if it actually has text
                        if len(word_txt) > 1:
                              words.append((word_txt, data_pair[0], data_pair[1], "vertical"))
                        data_pair = []
                        word_txt = ""
                        

                  #if we're done with a column, it's possible that there's still text left to be saved.
                if (len(word_txt) > 1):
                     words.append((word_txt, data_pair[0], data_pair[1], "vertical"))
                rowNum += 1
                    
            return words
                        
                       
               
             
