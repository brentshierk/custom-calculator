print('welcome to my calculator')
""" 
this calculator is going to take two words and return the sum for each letter.
"""
alphabet = [["a",0],["b",0],["c",0],["d",0],["e",0],["f",0],["g",0],["h",0],["i",0],["j",0],["k",0],["l",0],["m",0],["n",0],["o",0],["p",0],["q",0],["r",0],["s",0],["t",0],["u",0],["v",0],["w",0],["x",0],["y",0],["z",0]]


"""
this first function takes the input from the user and saves the first result of the input to word1 and the result of the second to word2
"""
firstSplitWord = []
secondSplitWord = []
bothWords = []
def splitWords():
    word1= input('enter a word')
    word2= input('enter a second word')
    bothWords = word1 + word2
    print(bothWords)
    return bothWords
resultWord = splitWords()


def checkMatch():
    for letter in resultWord:
        for subList in alphabet:
            if letter == subList[0]:
               subList[1] += 1
    print(alphabet) 
checkMatch()