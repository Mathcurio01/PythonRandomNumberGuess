import random

print("Welcome to S random number guess.")
user_input =int(input("Enter a number from 1 to 100: "))
randomnum = random.randint(1,100)
if (randomnum==user_input):
    print("Congartulations! You Won")
else:
    print(f"Sorry! Your guess is not correct. Your guess is {user_input} and computer generated guess is {randomnum}")

