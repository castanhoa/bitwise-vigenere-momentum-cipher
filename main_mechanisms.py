import random

from settings import ALPHABET, MAX_INITIAL_VELOCITY, ACCELERATION, VELOCITY_PERIOD, REVERSE_ACCELERATION_PERIOD, BLOCKS_OF_FIVE, RANDOMIZES_ALPHABETS

from sub_mechanisms import split_in_blocks, str_sum, bitwise_mixer, str_indexes

def feed_text(text: str="A"*104, key:str="A", direction:int=1) -> str:
        
        # some pre processing

        if BLOCKS_OF_FIVE == True:
            text = text.strip().replace(' ','')
            key = key.strip().replace(' ','')


        #===#

        encoded_chars: list[str] = []

        direction = (direction > 0) - (direction < 0)
        
        my_acceleration = ACCELERATION

        my_alphabet = list(ALPHABET)
        my_alphabet_set = set(ALPHABET)

        seed_key = (str_indexes(key) + str_sum(key))

        last_velocity_in_period = (bitwise_mixer(seed_key,0)) % (MAX_INITIAL_VELOCITY+1)
        my_velocity = last_velocity_in_period

        for index, char in enumerate(text):
            
            if RANDOMIZES_ALPHABETS == True:
                current_seed = bitwise_mixer(seed_key, index + 1)
                random.seed(current_seed)
                random.shuffle(my_alphabet)
            
            if type(VELOCITY_PERIOD) == int and index % VELOCITY_PERIOD == 0:
                new_velocity = (bitwise_mixer(last_velocity_in_period, index + 2)) % (MAX_INITIAL_VELOCITY+1)

                my_velocity = new_velocity
                last_velocity_in_period = new_velocity
            
            if type(REVERSE_ACCELERATION_PERIOD) == int and index % REVERSE_ACCELERATION_PERIOD == 0:
                my_acceleration  *= -1
            
            if char not in my_alphabet_set:
                encoded_chars.append(char)
            else:
                char_index = my_alphabet.index(char)
                key_char = key[(index) % len(key)]
                key_index = my_alphabet.index(key_char)

                encoded_chars.append(
                    my_alphabet[(char_index + (key_index + my_velocity)*direction) % len(my_alphabet)]
                )
            
            my_velocity += my_acceleration 
            
        output_text = "".join(encoded_chars)

        if BLOCKS_OF_FIVE == True:
            output_text = split_in_blocks(output_text)

        return output_text


# plain_text = "Lavit reatum criminis"

# cipher_text = feed_text(direction=1)
# print(cipher_text)

# deciphered_text = feed_text(text=cipher_text, direction=-1)
# print(deciphered_text)

