def rlc_encode(data):
    encoding = []
    i = 0

    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1
        encoding.append((data[i], count))
        i += 1
    return encoding

def rlc_decode(encoded):
    return ''.join(char * count for char, count in encoded)

# Test
text = "AAAABBBCCDAA"
encoded = rlc_encode(text)
decoded = rlc_decode(encoded)

print("Encoded:", encoded)
print("Decoded:", decoded)
