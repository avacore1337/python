def readData(file):
    return int(file.readline().split()[2])


def readHex(file):
    return int(file.readline().split()[2][2:], 16)

f = open("key_data.txt")
N = readHex(f)
e = readData(f)
p = readHex(f)
q = readHex(f)
d = readHex(f)
print(N, e, p, q, d, sep="\n")
ciphertext = int(open("ciphertext.txt").readline(), 16)
print(ciphertext)
res = pow(ciphertext, d, N)
print(hex(res))
# ans = ""
# for i in range(90):
#     ans += chr(res & 0xFF)
#     res = res // 0xFF
# print(ans[::-1])
