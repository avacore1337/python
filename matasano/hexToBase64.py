import base64

def hexToBase64(hex):
    return base64.b64encode(bytes.fromhex(hex)).decode("utf-8")

if __name__ == '__main__':
    data = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hexToBase64(data))
    print("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")