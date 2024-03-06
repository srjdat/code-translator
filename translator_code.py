import random

rand_num = 10
user_input = int(input('guess a number '))

while(rand_num != user_input):
    user_input = int(input('that was wrong, guess again '))

print(f'you guessed right! the number was {rand_num}')