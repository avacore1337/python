
def printNum(num):
    if len(num) == 0:
        print("YODA")
    elif int(num) == 0:
        print(0)
    else:
        print(num)

num1 = input()[::-1]
num2 = input()[::-1]
num1 += "0"*(len(num2)-len(num1))
num2 += "0"*(len(num1)-len(num2))
ans1 = ""
ans2 = ""
for i in range(len(num1)):
    if num1[i] == num2[i]:
        ans1 += num1[i]
        ans2 += num2[i]
    elif num1[i] < num2[i]:
        ans2 += num2[i]
    else:
        ans1 += num1[i]
printNum(ans1[::-1])
printNum(ans2[::-1])
