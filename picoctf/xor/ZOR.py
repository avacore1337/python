#!/usr/bin/python

import sys


wordValue = {}
wordValue["a"] = 8167
wordValue["b"] = 1492
wordValue["c"] = 2782
wordValue["d"] = 4253
wordValue["e"] = 12702
wordValue["f"] = 2228
wordValue["g"] = 2015
wordValue["h"] = 6094
wordValue["i"] = 6966
wordValue["j"] = 153
wordValue["k"] = 772
wordValue["l"] = 4025
wordValue["m"] = 2406
wordValue["n"] = 6749
wordValue["o"] = 7507
wordValue["p"] = 1929
wordValue["q"] = 95
wordValue["r"] = 5987
wordValue["s"] = 6327
wordValue["t"] = 9056
wordValue["u"] = 2758
wordValue["v"] = 978
wordValue["w"] = 2361
wordValue["x"] = 150
wordValue["y"] = 1974
wordValue["z"] = 74
wordValue[chr(32)] = 15000

"""
Daedalus Corporation encryption script.
"""


def xor(input_data, key):
    result = ""
    for ch in input_data:
        result += chr(ord(ch) ^ key)

    return result


def encrypt(input_data, key):

    return xor(input_data, key)


def decrypt(input_data, key):
    return encrypt(input_data, key)


def usage():
    print("Usage: %s [encrypt/decrypt] [in_file] [out_file] [password]" % sys.argv[0])
    exit()


def main():
    if len(sys.argv) < 3:
        usage()

    input_data = open(sys.argv[1], 'r').read()
    maxval = 0
    maxstr = ""
    for i in range(256):
        result_data = decrypt(input_data, i)
        theSum = 0
        for x in result_data:
            if x in wordValue:
                theSum += wordValue[x]
        print(theSum)
        print(result_data)
        if theSum > maxval:
            maxval = theSum
            maxstr = result_data
    print "this is the maxValue"
    print maxval
    print
    print maxstr
    print

    # out_file = open(sys.argv[2], 'w')
    # out_file.write(result_data)
    # out_file.close()

main()
