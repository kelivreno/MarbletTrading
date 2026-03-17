import random

money = 1000 #starting money
num_rounds = int(input("How many rounds would you like to do? "))
bag = ['green']*4 + ['red']*3 + ['black'] + ['white']
# green = win amount user bet
# red = lose amount user bet
# black = 10x win amount user bet
# white = 5x lose amount user bet
# marbles are replaced into bag after each round

prev_money = money #initialized previous money to current money

for i in range(1, num_rounds + 1):

   while True:
       #before each round,
       # user will input how much they want to bet
       bet = int(input("How much you want to bet? "))
       if bet > money:
            print("You exceed your money!")
            continue
       else:
           break

   draw = random.choice(bag)
   if draw == 'green':
       money += bet
   elif draw == 'red':
       money -= bet
   elif draw == 'black':
       money += 10*bet
   elif draw == 'white':
       money -= 5*bet

   if money <= 0:print(f"You owe the casino: {-money}")

   print(f"Round {i}: you drew {draw}, money = ${money}")

   if money < 0.5*prev_money:
       #if user loses half of their running money, the game ends
       #the game ends
       print("GAME OVER!")
       break

   prev_money = money




