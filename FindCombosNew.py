import itertools as it

def get_rack_powerset(s):
    """Return a list of characters that can be added to the board"""
    for i in range(len(s)+1):
        for combo in it.combinations(s,i):
            yield "".join(combo)
            

def remove_duplicates(lst):
    lst.sort()
    i = len(lst) - 1
    while i > 0:  
        if lst[i] == lst[i - 1]:
            lst.pop(i)
        i -= 1
    return lst


def get_words(word_on_board, rack):
    """
        Make all possible combinations of characters given a word on the board.
        E.g. given word on board = odd, and rack = dly, can have oddly, dodd etc.
        Can only make new words by adding to beginning or end of existing word. 
    """

    rack_powerset = get_rack_powerset(rack)
    possible_words = []
    for string_seq in rack_powerset:
        append_front = string_seq + word_on_board
        append_back =  word_on_board + string_seq 
        possible_words.append(append_front)
        possible_words.append(append_back)
    return possible_words
        


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

print(get_words("odd", "dly"))
