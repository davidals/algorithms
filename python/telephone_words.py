//Generate all the possible words from a telephone number
map = {}

map["2"] = ["A", "B", "C"]
map["3"] = ["D","E","F"]
map["4"] = ["G","H","I"]
map["5"] = ["J","K","L"]
map["6"] = ["M","N","O"]
map["7"] = ["P","Q","R","S"]
map["8"] = ["T","U","V"]
map["9"] = ["W","X","Y","Z"]

def gen_Words(number, validWords):
    wordList = []
    recursive_gen(number, 0, "", wordList, validWords)
    print wordList

def recursive_gen(phoneNumber, index, newWord, wordList, validWords):

    if(index == len(phoneNumber)):
        if(newWord in validWords):
            wordList.append(newWord)
    else:
        for char in map[phoneNumber[index]]:
            recursive_gen(phoneNumber, index + 1, newWord + char, wordList, validWords)

gen_Words("4357",["HELP"])