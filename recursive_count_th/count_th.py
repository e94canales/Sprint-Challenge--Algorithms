'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) <= 1: # if the word only contain one character, "th" can't exist, return 0
       return 0

    if word[:2] == "th": # if the first two letters are "th" recurse, and return +1
        return count_th(word[1:]) + 1 

    return count_th(word[1:]) # otherwise recurse with the next letter in word