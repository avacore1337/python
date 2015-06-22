import base64

wordValue = {}
wordValue["a"]=8167
wordValue["b"]=1492
wordValue["c"]=2782
wordValue["d"]=4253
wordValue["e"]=12702
wordValue["f"]=2228
wordValue["g"]=2015
wordValue["h"]=6094
wordValue["i"]=6966
wordValue["j"]=153
wordValue["k"]=772
wordValue["l"]=4025
wordValue["m"]=2406
wordValue["n"]=6749
wordValue["o"]=7507
wordValue["p"]=1929
wordValue["q"]=95
wordValue["r"]=5987
wordValue["s"]=6327
wordValue["t"]=9056
wordValue["u"]=2758
wordValue["v"]=978
wordValue["w"]=2361
wordValue["x"]=150
wordValue["y"]=1974
wordValue["z"]=74
wordValue[chr(32)]=15000

def xor(first, second):
	return bytes(x^y for x,y in zip(first,second))
	# tmp1 = bytes.fromhex(first)
	# tmp2 = bytes.fromhex(second)
	# xored = bytes(x^y for x,y in zip(tmp1,tmp2))
	# return base64.b16encode(xored).decode("utf-8")



if __name__ == '__main__':
	data = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	hexdata = bytes.fromhex(data)
	print(hexdata)
	print(len(hexdata))
	maxValue = 0
	secret = ""
	secretKey = 0
	for i in range(256):
		value = 0
		xorKey = bytes([i]*len(hexdata))
		# print(xorKey)
		# xorKey = base64.b16encode(keyString)
		result = xor(hexdata,xorKey)
		for x in result:
			if chr(x).lower() in wordValue:
				# print(chr(x))
				value += wordValue[chr(x).lower()]
			if value > maxValue:
				secret = result
				maxValue = value
				secretKey = i
			# print(x)
			# print(chr(x).lower())
		# print(result)
	print(secret)
	print(chr(secretKey))
	# print("686974207468652062756c6c277320657965")
	# print(xor("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965"))
	# print("746865206b696420646f6e277420706c6179")