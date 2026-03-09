ciphertext = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

with open("output.txt", "w", encoding="utf-8") as f:
    for key in range(256):
        decrypted = bytes(b ^ key for b in ciphertext)
        f.write(f"Key: {key} ('{chr(key)}') | {decrypted}\n")