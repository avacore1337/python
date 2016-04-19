def main():
    charCount = {}

    chars = input()
    totalLen = len(chars)
    for c in chars:
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1

    if len(charCount.keys()) == 1:
        print(chars[0])
        return

    minVal = totalLen
    for key in charCount.keys():
        if charCount[key] < minVal:
            minVal = charCount[key]

    blockSize = 0
    for key in charCount.keys():
        if charCount[key] % minVal != 0:
            print(-1)
            return
        charCount[key] = charCount[key]//minVal
        blockSize += charCount[key]


    for i in range(1, totalLen//minVal + 1):
        if totalLen % i != 0:
            continue
        s = chars[:i]
        fail = False
        print(s)
        for j in range(0, totalLen - i, i):
            if s != chars[j:j + i]:
                fail = True
                break
        if not fail:
            print(s)
            return
    print(-1)
    print("endfail")
main()
