
import random
import time

print('Welcome to the game')
print()
time.sleep(1)

player_num = int(input('How many players: '))
print()
time.sleep(1)

user_team = []
comp_team = []
i = 1

while i <= player_num:
    user_team.append('user'+str(i))
    comp_team.append('comp'+str(i))
    i += 1
    
user_score = 0
print('User\'s Batting')
print()
time.sleep(1)
    
while user_team != []:
        
    out = False
        
    while out == False:
        print(user_team[0]+': ', end='')
        user_bat = int(input('(Enter a number from 0 to 6) '))
        assert 0 <= user_bat <= 6
        print()
        time.sleep(1)
        comp_bowl = random.randint(0, 6)
        print('comp:', comp_bowl)
        print()
        time.sleep(1)
            
        if user_bat == comp_bowl:
            out = True
            print(user_team[0], 'Out')
            print()
            time.sleep(1)
                
        else:
            if user_bat == 0:
                user_bat = comp_bowl
                    
            print(user_team[0], 'Scored', user_bat, 'run(s)')             
            user_score += user_bat
            print('User\'s team total score: ', user_score)
            print()
            time.sleep(1)
                
    user_team.remove(user_team[0])
        
print('User\'s team final score', user_score)
print('Target is', (user_score +1))
print()
time.sleep(1)

comp_score = 0
print('User\'s Bowling')
print()
time.sleep(1)

while comp_team != [] and comp_score <= user_score:
        
    out = False
        
    while out == False and comp_score <= user_score:
            
        comp_bat = random.randint(0, 6)
        print('user: ', end='')
        user_bowl = int(input('(Enter a number from 0 to 6) '))
        print()
        time.sleep(1)
        print(comp_team[0]+':', comp_bat)
        print()
        time.sleep(1)

        if comp_bat == user_bowl:
            out = True
            print(comp_team[0], 'Out')
            print()
            time.sleep(1)
                
        else:
            if comp_bat == 0:
                comp_bat = user_bowl
                    
            print(comp_team[0], 'Scored', comp_bat, 'run(s)')                   
            comp_score += comp_bat
            print('Comp\'s team total score: ', comp_score)
            print()
            time.sleep(1)
                
            if (user_score - comp_score)+1 > 0:
                print(((user_score - comp_score)+1), 'Runs needed')
                print()
                time.sleep(1)

    if out == True:
        comp_team.remove(comp_team[0])
        
print('User\'s team scored', user_score, 'and Comp\'s team scored', comp_score)
print()
time.sleep(1)
    
if user_score == comp_score:
    print('Draw!')
        
elif user_score > comp_score:
    print('User Won by', (user_score - comp_score), 'Runs!')

else:
    print('Comp Won by', len(comp_team), 'Wickets!')
