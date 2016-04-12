def printWords(wordsCount):

    cwords = 0
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(26):
                    print(chr(97 + i) + chr(97 + j) + chr(97 + k) + chr(97 + l), end=" ")
                    cwords += 1
                    if cwords == wordsCount:
                        return

minWords, maxWords = list(map(int, input().split()))

words = max(minWords, int(maxWords/2) + 1)
# print(words)
printWords(words)
