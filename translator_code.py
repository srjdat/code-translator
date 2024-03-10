import random

rand_num = random.randint(1,10)
print(rand_num)
user_input = int(input('guess a number from 1-10 '))

while(rand_num != user_input):
    user_input = int(input('that was wrong, guess again '))

print(f'you guessed right! the number was {rand_num}')