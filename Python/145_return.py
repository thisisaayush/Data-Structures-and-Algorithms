import random
#get_integer function below is to prevent the program from crashing. If the input is invalid, code simply will not work.
#for instance if user enter string or char instead in general code while comparing a number, program will crash.
#string and num are not comparable.
def get_integer(prompt):
    while True:#until the input is valid.
        temp = input(prompt) #is it extracting the argument???
        if temp.isnumeric():
            return int(temp)

        else:
             print("{0} is not a valid number.".format(temp))

answer = random.randint(1,1001)
print("{} is the answer.".format(answer))
guess = 0
print("Guess a number between 1 to 1000:")
while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        print("0 will terminate the code.")
        break

    elif guess == answer:
        print("Congrats!!!, you have guessed it.")
        break

    elif guess < answer:
        print("Please guess higher.")

    else:
        print("Please guess lower.")
