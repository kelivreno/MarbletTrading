import random

money = 1000
num_rounds = int(input("How many rounds would you like to do? "))
bag = ['green']*6 + ['red']*4

i = 1

for i in range(num_rounds):
    draw = random.choice(bag)
    bag.remove(draw)



