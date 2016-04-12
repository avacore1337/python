amount = int(input())
versions = ["ABC"*amount, "BABC"*amount, "CCAABB"*amount]
score = [0, 0, 0]
text = input()
for i in range(3):
    person = versions[i]
    theSum = 0
    for j in range(amount):
        if text[j] == person[j]:
            theSum += 1
    score[i] = theSum

best = max(score)
print(best)
if score[0] == best:
    print("Adrian")
if score[1] == best:
    print("Bruno")
if score[2] == best:
    print("Goran")
