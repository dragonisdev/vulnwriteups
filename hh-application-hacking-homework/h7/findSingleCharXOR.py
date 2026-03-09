def score(text):
    common = b" etaoinshrdlu"
    return sum(1 for b in text.lower() if b in common)

best_score = 0
result = ""


with open("4.txt", "r") as f:
    for i, line in enumerate(f):

        text = bytes.fromhex(line.strip())

        for key in range(256):
            decrypted = bytes(b ^ key for b in text)

            s = score(decrypted)
            if s > best_score:
                best_score = s
                result = decrypted


print(f"Message: {result}")