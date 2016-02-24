for theRound in range(int(input())):
    amount = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    # print(numbers)
    ans = numbers[-1]
    for i in range(0, amount-1, 2):
        if numbers[i] != numbers[i+1]:
            ans = numbers[i]
            break

    print("Case #" + str(theRound + 1) + ": " + str(ans))
