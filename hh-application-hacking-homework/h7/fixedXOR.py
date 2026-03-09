''' Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179 
'''

hex1 = "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"

b1 = bytes.fromhex(hex1)
b2 = bytes.fromhex(hex2)

xor = []
for a, b in zip(b1, b2):
    xor.append(a ^ b)

result = bytes(xor).hex()

print(result)