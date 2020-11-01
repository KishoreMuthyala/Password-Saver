import random
import string
import ast


def encode(password):
    """
    Takes Password as input
    and returns a tuple of encrypted password and keys
    """
    i = 0
    d = {}
    pswdLen = 5
    while i <= 255:
        letters = string.ascii_lowercase + string.digits
        code = ''.join(random.choice(letters) for i in range(pswdLen))
        d.update({i: code})

        i += 1
    inputText = password
    text = ""
    for i in inputText:
        ascii_of_i = ord(i)
        for key, value in d.items():
            if key == ascii_of_i:
                text += value

    return (text, d)


def decode(password, keys):
    """
    Returns the decoded password
    """
    encText = password
    d = ast.literal_eval(str(keys))
    finderLen = 5
    encTextLen = len(encText)
    i = 0
    data = ""
    while i <= encTextLen:
        encText_parts = encText[i: i + finderLen]
        for key, val in d.items():
            if val == encText_parts:
                data += chr(key)
        i += finderLen
    return data
