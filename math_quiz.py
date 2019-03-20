#!/usr/bin/python

import random
import time

divide = True
doubles = False
base = 4
questions = 30

min=1
max=10

correct = 0
wrong = 0

start_time = time.time()

choices=[]

for question in range(questions):
    if len(choices) == 0:
        choices = range(min, max+1)
    multiplicand = random.choice(choices)
    if doubles:
        base = multiplicand
    choices.remove(multiplicand)

    good_answer = False
    while not good_answer:
        if divide:
            prompt = '{}. What is {} --- {}? '.format(question+1, multiplicand * base, base)
            answer = multiplicand
        else:
            prompt = "{}. What is {} x {}? ".format(question+1, base, multiplicand)
            answer = base * multiplicand

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
