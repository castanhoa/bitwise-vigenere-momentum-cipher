from settings import ALPHABET, RANDOMIZER_OFFSET

def split_in_blocks(text:str):
    return (' '.join([text[i:i+5] for i in range(0, len(text), 5)]))

def str_sum(text:str):
    value = 0
    for char in str(text):
        try:
            index = ALPHABET.index(char)

        except ValueError:
            index = 0

        value += index

    return value

def bitwise_mixer(k, i):
    # credits to gemini
    x = (k + i + RANDOMIZER_OFFSET) & 0xFFFFFFFF
    x ^= x >> 16
    x = (x * 0x85ebca6b) & 0xFFFFFFFF
    x ^= x >> 13
    x = (x * 0xc2b2ae35) & 0xFFFFFFFF
    x ^= x >> 16
    return x

def str_indexes(text:str):

    value = ''

    for char in str(text):
        try:
            index = ALPHABET.index(char)
        except ValueError:
            index = 0

        value += str(index)

    return int(value)