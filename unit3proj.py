import random
import os
import math
import string
print("On average how many guesses does it take for a computer to spell PYTHON?")
OkSims1 = 0
OkSims2 = 0
CoolSims1 = []
CoolSims2 = []
CoolSims3 = []
CoolSims4 = []

sim = 0 
data = []
sims = int(input("How many simulations would you like? "))
while sim < sims: 
    guesses = 0
    string.ascii_letters
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    P = 0
    Y = 0
    T = 0
    H = 0
    O   = 0
    N = 0

    while P == 0:
        guess = random.choice(string.ascii_letters)
        if guess == 'P':
            guesses = guesses + 1
            P = P + 1
            if guesses == 1:
                OkSims1 = OkSims1 + 1
            #print(guesses)
        else:
            guesses = guesses + 1
    while Y == 0:
        guess = random.choice(string.ascii_letters)
        if guess == 'Y':
            guesses = guesses + 1
            Y = Y + 1
            if guesses == 2:
                OkSims2 = OkSims2 + 1
            #print(guesses)
        else:
            guesses = guesses + 1
    while T == 0:
        guess = random.choice(string.ascii_letters)
        if guess == 'T':
            guesses = guesses + 1
            T = T + 1
            if guesses == 3:
                CoolSims1.append(sim)
            #print(guesses)
        else:
            guesses = guesses + 1
    while H == 0:
        guess = random.choice(string.ascii_letters)
        if guess == 'H':
            guesses = guesses + 1
            H = H + 1
            if guesses == 4:
                CoolSims2.append(sim)
            #print(guesses)
        else:
            guesses = guesses + 1
    while O == 0:
        guess = random.choice(string.ascii_letters)
        if guess == 'O':
            guesses = guesses + 1
            O = O + 1
            if guesses == 5:
                CoolSims3.append(sim)
            #print(guesses)
        else:
            guesses = guesses + 1
    while N == 0:
        guess = random.choice(string.ascii_letters)
        if guess == 'N':
            guesses = guesses + 1
            N = N + 1
            if guesses == 6:
                CoolSims4.append(sim)
            #print(guesses)
        else:
            guesses = guesses + 1
    data.append(guesses)
    

    fraction = (sim/sims)*100
    fraction = round(fraction, 1)
    os.system('clear')
    print("{}% COMPLETE" .format(fraction))
    




    sim = sim + 1

print("LEAST AMOUNT OF GUESSES:")
print(min(data))
print("~~~~~~~~~~~~~~~~~~~~~")
print("MOST AMOUNT OF GUESSES:")
print(max(data))
print("~~~~~~~~~~~~~~~~~~~~~")
print("AVERAGE AMOUNT OF GUESSES:")
numerator = sum(data)
denominator = len(data)
print(numerator/denominator)
print("~~~~~~~~~~~~~~~~~~~~~")
print("AMOUNT OF SIMULATIONS:")
print(sims)
print("~~~~~~~~~~~~~~~~~~~~~")
print("AMOUNT OF SIMULATIONS THAT CORRETLY GUESSED P THEIR FIRST TRY:")
print(OkSims1)
print("~~~~~~~~~~~~~~~~~~~~~")
print("AMOUNT OF SIMULATIONS THAT CORRETLY GUESSED PY THEIR FIRST TRY:")
print(OkSims2)
print("~~~~~~~~~~~~~~~~~~~~~")
print("SIMULATIONS THAT CORRECTLY GUESSED PYT THEIR FIRST TRY:")
print(CoolSims1)
print("~~~~~~~~~~~~~~~~~~~~~")
print("SIMULATIONS THAT CORRECTLY GUESSED PYTH THEIR FIRST TRY:")
print(CoolSims2)
print("~~~~~~~~~~~~~~~~~~~~~")
print("SIMULATIONS THAT CORRECTLY GUESSED PYTHO THEIR FIRST TRY:")
print(CoolSims3)
print("~~~~~~~~~~~~~~~~~~~~~")
print("SIMULATIONS THAT CORRECTLY GUESSED PYTHON THEIR FIRST TRY:")
print(CoolSims4)
print("~~~~~~~~~~~~~~~~~~~~~")
