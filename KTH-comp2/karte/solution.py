d = {"P": [], "K": [], "H": [], "T": []}
theNum = None
num = ""
NOPRINT = False
for x in input():
    # print(x)
    if x.isdigit():
        num += x
    else:
        if theNum:
            if int(num) in d[theNum]:
                NOPRINT = True
                break
            # print(theNum + num)
            d[theNum].append(int(num))
            num = ""
        theNum = x
if int(num) in d[theNum] or NOPRINT:
    print("GRESKA")
else:
    d[theNum].append(int(num))
    print(13 - len(d["P"]), end=" ")
    print(13 - len(d["K"]), end=" ")
    print(13 - len(d["H"]), end=" ")
    print(13 - len(d["T"]))
