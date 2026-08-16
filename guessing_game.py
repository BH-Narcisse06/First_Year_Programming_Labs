import random

Number = random.randint(1, 20)
print("Hello, and welcome. You are to guess a whole number between 1 and 20. You will have 5 guesses. Press 'Enter' after each input. Good luck!")

for i in range(1, 6):
  print(f"Guess {i}:")
  guess = int(input())
  
  if guess == Number:
    print("Congratulations! You guessed correctly")
    break
  elif guess > Number:
    print("Your guess is too high")
    print("Try again.")
  else:
    print("Your guess is too low")
    print("Try again.")
