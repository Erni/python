import string

def rotate(text, key):
    cipher = ''
    length = len(string.ascii_lowercase)
    pos = key

    # first, we build the cipher
    for i in range(length):
        cipher += string.ascii_lowercase[pos % length]
        pos += 1

    # then we cipher the text
    ciphered = ''
    for c in text:
        if not c.isalpha():
            ciphered += c
        else:
            if c.islower():
                ciphered += cipher[string.ascii_lowercase.find(c)]
            else:
                ciphered += cipher[string.ascii_lowercase.find(c.lower())].upper()

    return ciphered
