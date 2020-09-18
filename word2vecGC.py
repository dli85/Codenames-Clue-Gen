import gensim

if __name__ == '__main__':
    pathToModel = input('Please enter the path to the word2vec model (ends in .bin): ')
    model = gensim.models.KeyedVectors.load_word2vec_format(pathToModel, binary=True, limit=500000)

    wordsToConnect = []
    wordsToAvoid = []
    connectMaxLen = 5
    avoidMaxLen = 3

    print('Enter words you would like to "connect". Max of 5 words, enter an empty word to finish\n')
    for i in range(connectMaxLen):
        word = input('Word ' + str(i + 1) + ": ")
        if word == '':
            print()
            break

        wordsToConnect.append(word)

    print('Enter words you would like to "avoid". max of 3 words, enter an empty word to finish')
    for i in range(avoidMaxLen):
        word = input('Word: ' + str(i + 1) + ": ")
        if word == '':
            print()
            break

        wordsToAvoid.append(word)

    if len(wordsToConnect) == 0:
        print('Please enter at least one word to connect')
        exit()

    if len(wordsToAvoid) == 0:
        print('Please enter at least one word to avoid')
        exit()

