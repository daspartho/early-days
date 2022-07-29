import random

rounds = int(input('How many rounds do you want to play: '))
print()

player_score = 0
computer_score = 0
round_num = 0

while round_num < rounds:
       
       print('Round',(round_num + 1))
       print()
       
       player_guess = input('Player(Stone/Paper/Scissor): ')
       print()
       
       moves = {1: 'Stone', 2: 'Paper', 3: 'Scissor'}
       guess = random.randint(1, 3)
       computer_guess = moves[guess]
       print('Computer: ' + moves[guess])
       print()

       if player_guess == computer_guess:
              print('Draw!')
              print('Computer - ' + str(computer_score) + ' | ' + 'Player - ' + str(player_score))

       elif player_guess == 'Stone' and computer_guess == 'Paper':
              computer_score += 1
              print('Computer Won!')
              print('Computer - ' + str(computer_score) + ' | ' + 'Player - ' + str(player_score))

       elif player_guess == 'Stone' and computer_guess == 'Scissor':
              player_score += 1
              print('Player Won!')
              print('Computer - ' + str(computer_score) + ' | ' + 'Player - ' + str(player_score))

       elif player_guess == 'Paper' and computer_guess == 'Stone':
              player_score += 1
              print('Player Won!')
              print('Computer - ' + str(computer_score) + ' | ' + 'Player - ' + str(player_score))

       elif player_guess == 'Paper' and computer_guess == 'Scissor':
              computer_score += 1
              print('Computer Won!')
              print('Computer - ' + str(computer_score) + ' | ' + 'Player - ' + str(player_score))

       elif player_guess == 'Scissor' and computer_guess == 'Paper':
              player_score += 1
              print('Player Won!')
              print('Computer - ' + str(computer_score) + ' | ' + 'Player - ' + str(player_score))

       else:
              computer_score += 1
              print('Computer Won!')
              print('Computer - ' + str(computer_score) + ' | ' + 'Player - ' + str(player_score))

       print()


       round_num += 1

if computer_score < player_score:
       print('Final Score = ' + 'Computer - ' + str(computer_score) + ' | ' + 'Player - ' + str(player_score))
       print('Player Won!')

elif computer_score > player_score:
       print('Final Score = ' + 'Computer - ' + str(computer_score) + ' | ' + 'Player - ' + str(player_score))
       print('Computer Won!')

else:
       print('Final Score = ' + 'Computer - ' + str(computer_score) + ' | ' + 'Player - ' + str(player_score))
       print('Draw!')
       
