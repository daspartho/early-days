import random
def list_to_string(l):
    s=''
    for i in l:
        s+=i
    return s
words=['apple', 'orange', 'banana']
secret_word = random.choice(words)
guessed_word = ["-"]*len(secret_word)
wrong_guesses = 0
out_of_guesses = False

while list_to_string(guessed_word) != secret_word and not(out_of_guesses):
    print(list_to_string(guessed_word))
    guess=input('Enter Guess: ')
    assert len(guess)==1
    for i in range(len(secret_word)):
        if guess==secret_word[i] and guessed_word[i]=='-':
            guessed_word[i]=guess
            break
    else:
        wrong_guesses+=1
    if wrong_guesses==3:
        out_of_guesses = True
    
    

if out_of_guesses:
    print("You are out of guesses, You lose!")

else:
    print("You Won!")
        
    



        




    



        
    
