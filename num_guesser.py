import math

print("Hi there!")

print("Choose a number between 1 and 100 and i will guess it in 7 chances")

print("Ready")

input()

value = "no"

high = 100

low = 0

counter  = 0

while value == "no" and counter < 7:

    guess = math.floor((high + low)/2)

    print("Is it",str(guess))
    
    value = (input())

    if value == "yes":
        break

    else:

        counter += 1

        if counter < 7:

            print("Is it more or less than",guess)
            
            direction = input("")

            if direction == "more":
                low = guess

            else:
                high = guess

if value == 'yes':
    print("Got it!")

else:
    print("Impossible! You are fooling me")

input()























                
