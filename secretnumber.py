secret = 3

guess = int(input("Please think of a number between 1-10: "))

if guess == secret:
    print("Congratulation! You win!")

elif guess < secret:
    print("Your guess is too low. Try again.")

elif guess > secret:
    print("Your guess is too high. Try again.")

else:
    print ("Error")

