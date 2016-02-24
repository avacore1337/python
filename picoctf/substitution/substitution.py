import string

wordValue = []
wordValue.append((8167, "a"))
wordValue.append((1492, "b"))
wordValue.append((2782, "c"))
wordValue.append((4253, "d"))
wordValue.append((12702, "e"))
wordValue.append((2228, "f"))
wordValue.append((2015, "g"))
wordValue.append((6094, "h"))
wordValue.append((6966, "i"))
wordValue.append((153, "j"))
wordValue.append((772, "k"))
wordValue.append((4025, "l"))
wordValue.append((2406, "m"))
wordValue.append((6749, "n"))
wordValue.append((7507, "o"))
wordValue.append((1929, "p"))
wordValue.append((95, "q"))
wordValue.append((5987, "r"))
wordValue.append((6327, "s"))
wordValue.append((9056, "t"))
wordValue.append((2758, "u"))
wordValue.append((978, "v"))
wordValue.append((2361, "w"))
wordValue.append((150, "x"))
wordValue.append((1974, "y"))
wordValue.append((74, "z"))
# wordValue.append((15000, chr(32)))
wordValue.sort()


def main():
    d = {}
    for x in string.ascii_lowercase:
        d[x] = 0
    # d[" "] = 0
    myData = ""
    with open("data.txt") as file:
        myData = file.read()
        for x in myData.replace("\n", "").replace(" ", ""):
            d[x] += 1
    # print(d)
    y = []
    for x in d:
        y.append((d[x], x))
    y.sort()
    # print(y)
    trans = {}
    for i in range(len(y)):
        print(y[i][1], wordValue[i][1])
        # trans[y[i][1]] = wordValue[i][1]

    wordDict = {}
    for x in myData.replace("\n", " ").split(" "):
        # print(x)
        if x in wordDict:
            wordDict[x] += 1
        else:
            wordDict[x] = 1
    print(wordDict)

    wordList = []
    for x in wordDict:

        wordList.append((wordDict[x], x))
    wordList.sort()
    for x in wordList:
        print(x)
    for x in string.ascii_lowercase:
        trans[x] = x
    trans["u"] = "a"
    trans["t"] = "i"
    trans["o"] = "t"
    trans["e"] = "h"
    trans["y"] = "e"
    trans["l"] = "b"
    trans["w"] = "n"
    trans["c"] = "d"
    trans["s"] = "w"
    trans["p"] = "o"
    trans["g"] = "l"
    trans["z"] = "f"
    trans["m"] = "r"
    trans["r"] = "y"
    trans["x"] = "u"
    trans["a"] = "g"
    # trans["j"] = "c"
    trans["v"] = "s"
    trans["k"] = "v"
    trans["h"] = "p"
    trans["q"] = "c"
    trans["b"] = "m"
    trans["f"] = "k"
    trans[" "] = " "
    trans["\n"] = "\n"
    for x in myData:
        print(trans[x], end="")
# ftwa
# -in
# zpm
# hmyhumyc
# -re-ared
# rpx
# you


if __name__ == '__main__':
    main()
