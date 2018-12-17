#!/usr/bin/python

import random
import time

doubles = False
base = 7
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
        guess_string = raw_input("{}. What is {} x {}? ".format(question+1, base, multiplicand))
        try:
            guess = int(guess_string)
            good_answer = True
        except:
            print "Invalid entry - not a number"
            good_answer = False

    if guess == base * multiplicand:
        print "That is correct!"
        correct += 1
    else:
        print "That is wrong, the correct answer is {}".format(base * multiplicand)
        wrong += 1

end_time = time.time()

print "DONE!  You got {} right and {} wrong in {:.3} seconds".format(correct, wrong, end_time - start_time)
