from Board import Board
from Tile import Tile
from Bag import Bag
from Square import Square
from itertools import permutations



class Utils:
    """
       class containing  helper methods that can be accessed by game/agents.
    """

    def __init__(self, wordlist = "valid_words.txt"):
        """
             Load the list of valid words into memory for manipulation.
             Also, we have a default letter freq table used to compute scores. 
        """
        self.valid_words = set(line.strip() for line in open('valid_words.txt'))  #using set for optimal performance.
       
        
        
    def word_valid(self, word):
        """
           Check to see if a given word is valid.
           Returns: True if word valid, False otherwise
        """
        pass

    
    

    def likely_tiles_to_draw(self):
        #these are the tiles that are likely to be drawn. estimate using monte carlo
        pass


    

def get_rack_powerset(s):
    """
         Return a list of characters that can be added to the board given the rack (a string) s.
         ***Currently, should be wrapped in a list object before use. 
    """
    for i in range(1, len(s)+1):
        perms = (p for p in permutations(s, i))
        for p in perms:
            yield ''.join(p)
    

def remove_duplicates(lst):
    lst.sort()
    i = len(lst) - 1
    while i > 0:  
        if lst[i] == lst[i - 1]:
            lst.pop(i)
        i -= 1
    return lst


def get_possible_words(word_on_board, rack):
    """
        Make all possible combinations of characters given a word on the board and rack.
        E.g. given word on board = odd, and rack = dly, can have oddly, dodd etc.
        Can only make new words by adding to beginning or end of existing word. 
    """

    rack_powerset = get_rack_powerset(rack) #***MAY NEED TO PUT LIST AROUND THIS. i.e. list(....)
    possible_words = []
    for string_seq in rack_powerset:
        if string_seq == "":
            continue  #don't do anything for empty string
        
        append_front = string_seq + "->" + word_on_board
        append_back =  word_on_board + "<-" +string_seq 
        possible_words.append(append_front)
        possible_words.append(append_back)
    return possible_words

def  get_legal_words(word_on_board, rack, all_valid_words):
    """
      Get all legal combinations of characters given a word on the board and your rack.
      A word is legal iff it appears in our list of valid words.
      Note: At least one character from the rack must be used before we return a word (e.g. "APPLE" is a valid word,
      but if no character can be added to it from rack, we will not return it as a valid word that a person can create.
    """
    
    if len(rack) == 0:
        return [] #don't continue looking if we have an empty rack.

    possible_words = get_possible_words(word_on_board, rack)
    legal_words_found = [] 
    for word in possible_words:
        plain_word = word.replace("->", "")
        plain_word = plain_word.replace("<-", "")
        
        if plain_word in all_valid_words:
            legal_words_found.append(word)
    return legal_words_found


def get_all_legal_combos(list_of_board_words, rack, all_valid_words):
    """
       Similar to get_legal_words but for all words on the board.
       ***Will eventually compress the two methods into one.
    """
    if len(rack) == 0:
        return [] #no need to search if we have an empty rack.


    legal_words_found = []
    
    for cur_board_word in list_of_board_words: #find valid combos, looking at all words on the board
        
         possible_words = get_possible_words(cur_board_word, rack) #get all possible combinations that can be made on the board. 
         
         for word in possible_words:   #for all those words retrieved, see which ones are actually legal.
             plain_word = word.replace("->", "")
             plain_word = plain_word.replace("<-", "")
             if plain_word in all_valid_words:        
                 legal_words_found.append(word)
    return legal_words_found




def word_permutations(string):
    if len(string) == 1:
        return string

    recursive_perms = []
    for c in string:
        for perm in permutations(string.replace(c,'',1)):
            recursive_perms.append(c+perm)

    return remove_duplicates(recursive_perms)

#print(list(get_rack_combos("dly")))
#print(word_permutations(""))
#print(remove_duplicates(["Chinny", "Chinny", "Alex", "Paul"]))


