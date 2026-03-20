import time
import os
import getpass

if os.name == 'nt':
    _ = os.system(f'title {"Momentum cipher"}')


print('Application has been initiated.')

initiation_start_time = time.perf_counter()

print('loading...',end='\r')

# get the important stuff
from main_mechanisms import feed_text
from settings import ALPHABET
al = len(ALPHABET)

initiation_end_time = time.perf_counter()

# print that it was loaded
print(f'\rloaded! ({(initiation_end_time - initiation_start_time):.2f}s)\n',flush=True)

# welcome the user
print('Welcome to the chaotic momentum cipher test!')


time.sleep(1.3) # style points

while True:

    print('\n========================')

    cipher_mode = (input('Type "c" to enter CipherMode, type "d" to enter DecipherMode or just press Enter to clear the logs: ')).strip().lower()

    if cipher_mode == 'd':
        cipher_mode = False
        print('DecipherMode selected')
    elif cipher_mode == 'c':
        cipher_mode = True
        print('CipherMode selected.')
    else:
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

        continue


    input_text = ''

    if cipher_mode == False:
        input_text = input('\nEnter your input text: ')
    else:
        try:
            input_text = getpass.getpass(prompt='\nEnter your input text (german spaced): ',echo_char='X')

        except TypeError:
            input_text = getpass.getpass('\nEnter your input text (phantomized): ')

        except Exception:
            input_text = (input('\nEnter your input text: '))


    if input_text == '':
        print('invalid text. now your input text shall be a bunch of "A"s')
        input_text = "A"*(al*4)

    try:
        key = getpass.getpass('\nEnter your key (phantomized): ')

    except Exception:
        key = (input('\nEnter your key: '))

    if key == '':
        print('invalid key. now your key shall be "A"')
        key = 'A'

    print('\nprocessing...',end='\r')

    start_time = time.perf_counter()

    direction = 1 if cipher_mode == True else -1

    output_text = feed_text(text=input_text,key=key,direction=direction)

    end_time = time.perf_counter()
    
    print(f'\rprocessed! ({(end_time - start_time):.2f}s)\n',flush=True)

    time.sleep(0.2)

    print('===Output text (in yellow) below===\nSTART:')
    print("\x1b[33m"+output_text+"\033[0m")
    print('END.')
    
    time.sleep(0.5)

    continue_in_app = input('Press Enter to continue, or any letter to exit: ')
    if continue_in_app != '':
        exit()
        

    
