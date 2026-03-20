import string

ALPHABET = string.ascii_letters + string.digits
MAX_INITIAL_VELOCITY = 2**7
ACCELERATION = 3
VELOCITY_PERIOD = 13
REVERSE_ACCELERATION_PERIOD = 7
RANDOMIZES_ALPHABETS = False # Enhances security, degrades performance and reproductability.
RANDOMIZER_OFFSET = 3
BLOCKS_OF_FIVE = True