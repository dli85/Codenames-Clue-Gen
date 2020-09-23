import gensim

DEFAULTPATH = 'D:/Temp Downloads/GoogleNews-vectors-negative300.bin'

if __name__ == '__main__':
    pathToModel = input('Please enter the path to the word2vec model (ends in .bin): ')

    if len(pathToModel) == 0:
        pathToModel = DEFAULTPATH

    model = gensim.models.KeyedVectors.load_word2vec_format(pathToModel, binary=True, limit=500000)

    wordsToConnect = []
    wordsToAvoid = []
    connectMaxLen = 5
    avoidMaxLen = 3

    print('Enter words you would like to "connect". Max of 5 words, enter an empty word to finish\n')
    for i in range(connectMaxLen):
        word = input('Word ' + str(i + 1) + ": ")
        word = word.strip()
        word = word.lower()
        if word == '':
            print()
            break

        wordsToConnect.append(word)

    print('Enter words you would like to "avoid". max of 3 words, enter an empty word to finish')
    for i in range(avoidMaxLen):
        word = input('Word: ' + str(i + 1) + ": ")
        word = word.strip()
        word = word.lower()
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

    results = model.most_similar(positive=wordsToConnect, negative=wordsToAvoid, restrict_vocab=50000, topn=20)

    trimmed = []
    for i in range(len(results)):
        if len(trimmed) >= 10:
            break

        word = results[i][0]
        canUse = True
        for p in wordsToConnect:
            if p.upper() in word.upper() or word.upper() in p.upper():
                canUse = False

        for p in wordsToAvoid:
            if p.upper() in word.upper() or word.upper() in p.upper():
                canUse = False

        if canUse:
            trimmed.append(word)

    for i in range(len(trimmed)):
        print(str(i+1) + '. ' + trimmed[i])

