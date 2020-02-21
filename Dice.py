#A dice roller for ars magica 5th edition

import random

# 1 = simple die 
def roll (die_type, bonus):
    if die_type == 1:
        rand_val = random.randint(1,10)
        if rand_val == 1:
            counter = 1
            while rand_val == 1:
                counter += 1
                rand_val = random.randint(1,10)
            output_end = (rand_val * (counter * 2)) +  bonus
        else:
            output_end =  rand_val + bonus
    else:
        rand_val = random.randint(0,9)
        if rand_val == 0:
            output_end = "Botch"
        elif rand_val == 1:
            counter = 1
            while rand_val == 1:
                counter += 1
                rand_val = random.randint(1,10)
            output_end = (rand_val * (counter * 2)) +  bonus
        else:
            output_end = rand_val + bonus
    return output_end
