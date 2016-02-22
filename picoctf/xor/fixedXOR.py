import base64

def xor(first, second):
	tmp1 = bytes.fromhex(first)
	tmp2 = bytes.fromhex(second)
	xored = bytes(x^y for x,y in zip(tmp1,tmp2))
	return base64.b16encode(xored).decode("utf-8")



if __name__ == '__main__':
	print("1c0111001f010100061a024b53535009181c")
	print("686974207468652062756c6c277320657965")
	print(xor("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965"))
	print("746865206b696420646f6e277420706c6179")