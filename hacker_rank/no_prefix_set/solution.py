SETSIZE = ord("j") - ord("a") + 1


class Node():
    """docstring for Trie"""
    def __init__(self, range):
        self.range = range
        self.arr = [None]*range
        self.end = False


def badset(word):
    print("BAD SET")
    print(word)


def goodset():
    print("GOOD SET")


def main():
    root = Node(SETSIZE)
    rounds = int(input())
    for i in range(rounds):
        current = root
        newPath = False
        word = input()
        try:
            data = list(map(lambda x: ord(x) - 97, list(word)))
            for char in data:
                if (char > SETSIZE or char < 0):
                    badset(word)
                    return
                if current.end:
                    badset(word)
                    return
                if (current.arr[char] is None):
                    newPath = True
                    current.arr[char] = Node(SETSIZE)
                current = current.arr[char]
            current.end = True
            if not newPath:
                badset(word)
                return
        except:
            badset(word)
            return
    goodset()

main()
