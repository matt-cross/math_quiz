#!/usr/bin/python

import random
import time

# Supported modes include multiply, divide, and random.
mode = 'random'
doubles = False
base = 'random'
questions = 30

min=1
max=12

correct = 0
wrong = 0

start_time = time.time()

choices=[]

for question in range(questions):
    if len(choices) == 0:
        choices = range(min, max+1)
    multiplicand = random.choice(choices)
    if doubles:
        actual_base = multiplicand
    elif base == 'random':
        actual_base = random.choice(range(1,12))
    else:
        actual_base = base
    choices.remove(multiplicand)

    good_answer = False
    while not good_answer:
        if mode == 'divide' or (mode == 'random' and random.choice([True, False])):
            prompt = '{}. What is {} --- {}? '.format(question+1, multiplicand * actual_base, actual_base)
            answer = multiplicand
        else:
            prompt = "{}. What is {} x {}? ".format(question+1, actual_base, multiplicand)
            answer = actual_base * multiplicand

        guess_string = raw_input(prompt)
        try:
            guess = int(guess_string)
            good_answer = True
        except:
            print "Invalid entry - not a number"
            good_answer = False

    if guess == answer:
        print "That is correct!"
        correct += 1
    else:
        print "That is wrong, the correct answer is {}".format(answer)
        wrong += 1

end_time = time.time()

total_seconds = int(round(end_time - start_time))
minutes = total_seconds / 60
seconds = total_seconds % 60

if minutes == 1:
    time_str = '{} minute {} seconds'.format(minutes, seconds)
elif minutes > 1:
    time_str = '{} minutes {} seconds'.format(minutes, seconds)
else:
    time_str = '{} seconds'.format(seconds)

print "DONE!  You got {} right and {} wrong in {}".format(correct, wrong, time_str)
