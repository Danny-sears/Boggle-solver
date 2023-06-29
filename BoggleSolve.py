
def main():
    print('Loading dictionary...')
    wordTrie = load()
    print('Done')

    word = input('What letters should we use: ')
    minLength = 3
    print("")

    count = 0
    for word in sorted(findWords(wordTrie, word, "")):
        if len(word) >= minLength:
            count = count+1
            print(word)
    print(str(count) + " words found.")

def load():
    with open('words.txt') as wordFile:
        wordList = wordFile.read().split()

    trie = {}
    for word in wordList:
        addWordToTrie(trie, word)

    return trie

def addWordToTrie(d, word, idx = 0):
    if idx >= len(word):
        d['leaf']=True
        return
    if word[idx] not in d:
        d[word[idx]] = {'leaf':False}
    addWordToTrie(d[word[idx]], word, idx+1)

def findWords(trie, word, currentWord):
    myWords = set()      
    for letter in word:
        if letter in trie:
            newWord = currentWord + letter
            if trie[letter]['leaf']:
                myWords.add(newWord)
            myWords = myWords.union(findWords(trie[letter], word, newWord))
    return myWords

# Call the main function
if __name__ == "__main__":
    main()
