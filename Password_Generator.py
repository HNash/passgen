import random
from values import uppercase
from values import lowercase
from values import numbers
from values import specials


keyLength = int(input('How many characters do you want in your key '))
specialsAllowed = input('Are special characters allowed in your key? (y/n) ')


while specialsAllowed != 'y' and specialsAllowed != 'n':

    print ('Please answer with y or n')
    specialsAllowed = input('Are special characters allowed in your key? (y/n) ')


if specialsAllowed == 'y':
    n = 4

else:
    n = 3


def generate(length):

    print ('Generating...')

    keylist = []

    for i in range(0, length + 1):

        x = random.SystemRandom().randint(1, n)

        if x == 1:

            y = random.SystemRandom().randint(1, 25)

            keylist.append(uppercase[y])

        elif x == 2:

            y = random.SystemRandom().randint(1, 25)

            keylist.append(lowercase[y])

        elif x == 3:

            y = random.SystemRandom().randint(1, 9)

            keylist.append(numbers[y])

        elif x == 4:

            y = random.SystemRandom().randint(1, 14)

            keylist.append(specials[y])

    key = ''.join(keylist)

    print (key)


generate(keyLength)

exit = input()