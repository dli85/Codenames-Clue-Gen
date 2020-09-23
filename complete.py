import gensim

DEFAULTPATH = 'D:/Temp Downloads/GoogleNews-vectors-negative300.bin'

class Clue:
    def __init__(self, word, score, connected):
        self.word = word
        self.score = score
        self.connected = connected

if __name__ == '__main__':
    pathToModel = input('Please enter the path to the word2vec model (ends in .bin): ')

    if len(pathToModel) == 0:
        pathToModel = DEFAULTPATH

    model = gensim.models.KeyedVectors.load_word2vec_format(pathToModel, binary=True, limit=500000)

    numWords = int(input('How many words do you need to flip(should be 8 or 9)? '))

    if not (numWords == 8 or numWords == 9):
        print('ERROR: invalid input')
        exit()

    words = []
    for i in range(numWords):
        userInput = input('Please enter word ' + str(i+1) + ' : ')
        userInput = userInput.strip()
        userInput = userInput.lower()
        words.append(userInput)

    blackWord = input('Please enter you assassin/black word: ')
    blackWord = blackWord.strip()
    blackWord = blackWord.lower()

    wordsSet = set()
    for i in words:
        wordsSet.add(i)

    print(wordsSet)
    input()

    clues = []


    i = 0
    while i < len(words):
        p = i+1
        while p < len(words):
            wordsToConnect = [words[i], words[p]]

            raw = model.most_similar(positive=wordsToConnect, negative=blackWord, restrict_vocab=50000, topn=20)

            results = []

            #TODO filter raw and sort by score.

            p+=1

        i+=1

