import os

import time

import sys

import random

os.system('clear')

os.system('xdg-open https://www.github.com/BAYEZID-404')

print(' ')

print('''                       \033[1;36mREMEMBER :

             \033[1;32m WE ARE NOT HERE TO BE FAMOUS

                  WE ARE ALREADY FAMOUS''')

print(' ')

name1 = str(input('  \033[1;33mENTER YOUR NAME : \033[0m'))

os.system('clear')

def minhaz(x):

    for a in x +'\n':

        sys.stdout.write(a)

        sys.stdout.flush

        time.sleep(0.2)

logo = ('''\033[1;32m

    8888888b. Y88b   d88P 888888b.     \033[1;36m[×] BAYEZID MIAH\033[1;32m

    888   Y88b Y88b d88P  888  "88b  

    888    888  Y88o88P   888  .88P    \033[1;33m[×] BAYEZID-404 \033[1;32m

    888   d88P   Y888P    8888888K.  

    8888888P"    d888b    888  "Y88b   \033[1;31m[×] TEAM X FIRE \033[1;32m

    888         d88888b   888    888 

    888        d88P Y88b  888   d88P   \033[1;35m[×] GUESSING GAME\033[1;32m

    888       d88P   Y88b 8888888P"                                                                               ''')

print(logo)

print(60*'\033[1;36m=')

minhaz('                       \033[1;33m HELLO DEAR')

print(60*'\033[1;36m=\033[1;32m')

print(' ')

print('''. [01] GUESSING GAME BETWEEN 1 TO 5

 

  [02] GUESSING GAME BETWEEN 1 TO 10

 

  [03] GUESSING GAME BETWEEN 1 TO 20

 

  [04] DEVELOPER (BAYEZID MIAH)

  

  [05]  FACEBOOK PAGE (TEAM X FIRE)

  

  [06] FACEBOOK GROUP (TEAM X FIRE)

  

  [07] MESSENGER GROUP  (TEAM X FIRE COMMUNITY)

  ''')

print(60*'\033[1;31m×\033[1;32m')

pxb = input("  [ √ ] CHOSE A OPTION : \033[0m")

if pxb in['1','01']:

    print('WAIT A MINUTE...')

    time.sleep(3)

    os.system('clear')

    for x in range(1,100000):

        guessNumber = int(input('\033[1;36mENTER YOUR GUESS NUMBER  : '))

        randomNumber = random.randint(1,5)

        if guessNumber == randomNumber :

            print(' ')

            print('                    \033[1;32mCONGRATULATION',name1)

            print(' ')

            print('                      YOU HAVE WON')

            print(60*'═')

            print(' ')

        else:

            print(' ')

            print('                    \033[1;31mYOU HAVE LOST')

            print(' ')

            print('    THE NUMBER WAS ==×>\033[1;32m ',randomNumber,'\033[1;31m')

            print(60*'═')

            print('\033[0m')

elif pxb in['2','02']:

    print('WAIT A MINUTE...')

    time.sleep(3)

    os.system('clear')

    for x in range(1,100000):

        guessNumber = int(input('\033[1;36mENTER YOUR GUESS NUMBER  : '))

        randomNumber = random.randint(1,10)

        if guessNumber == randomNumber :

            print(' ')

            print('                    \033[1;32mCONGRATULATION',name1)

            print(' ')

            print('                      YOU HAVE WON')

            print(60*'═')

            print(' ')

        else:

            print(' ')

            print('                    \033[1;31mYOU HAVE LOST')

            print(' ')

            print('    THE NUMBER WAS ==×>\033[1;32m ',randomNumber,'\033[1;31m')

            print(60*'═')

            print('\033[0m')

elif pxb in['3','03']:

    print('WAIT A MINUTE...')

    time.sleep(3)

    os.system('clear')

    for x in range(1,10000):

        guessNumber = int(input('\033[1;36mENTER YOUR GUESS NUMBER  : '))

        randomNumber = random.randint(1,20)

        if guessNumber == randomNumber :

            print(' ')

            print('                    \033[1;32mCONGRATULATION',name1)

            print(' ')

            print('                      YOU HAVE WON')

            print(60*'═')

            print(' ')

        else:

            print(' ')

            print('                    \033[1;31mYOU HAVE LOST')

            print(' ')

            print('    THE NUMBER WAS ==×>\033[1;32m ',randomNumber,'\033[1;31m')

            print(60*'═')

            print('\033[0m')  

elif pxb in['4','04']: 

    os.system('xdg-open https://www.facebook.com/profile.php?id=100000879488649')

elif pxb in['5','05']:

    os.system('xdg-open https://www.facebook.com/profile.php?id=100078335700342') 

elif pxb in['6','06']:

    os.system('xdg-open https://facebook.com/groups/663864405056071/')

elif pxb in['7','07']:

    os.system('xdg-open https://m.me/j/AbZONJcca07k1MVd/')

else:

    print(' ')

    exit('\033[1;31mWRONG INPUT!! PLEASE RUN AGAIN AND CHOSE A CORRECT OPTION')    
