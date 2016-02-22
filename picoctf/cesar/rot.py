# import codecs
s   = "drocombodzkcczrbkcoscvptgsvkhjooewbkzzcxrqpvlynbvrc"
# enc = codecs.getencoder( "rot-13" )
# os  = enc( s )[0]
# print(str(os))


def rotx(s, rot):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[rot:]+chars[:rot]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s ) 

for i in range(26):
	print(rotx(s,i))