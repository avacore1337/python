numbers = [0]*42
for i in range(10):
    numbers[int(input()) % 42] = 1
print(sum(numbers))
