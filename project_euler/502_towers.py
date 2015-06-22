import math

def largeTenPowersWithMod(base,tenPowers,modulo):
	base = base % modulo
	for i in range(tenPowers):
		base = base**10 % modulo
	return base

def towers(hight, base):
	pass

sum = largeTenPowersWithMod(100 + 1, 12, 1000000007)
print(sum)
sum -= largeTenPowersWithMod(100, 12, 1000000007)
print(largeTenPowersWithMod(100, 12, 1000000007))
sum += largeTenPowersWithMod(10**12 + 1, 2, 1000000007)
sum += largeTenPowersWithMod(10000 + 1, 4, 1000000007)
sum -= largeTenPowersWithMod(10**12, 2, 1000000007)
sum -= largeTenPowersWithMod(10000, 4, 1000000007)
print(sum%1000000007)

