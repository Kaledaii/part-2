#WAP to update the high score of a game 

import random


def game():
    print('🎮You are playing game...')
    score=random.randint(1,101)
    print('Your score is',score)
    with open('hiscore.txt') as f:
        hiscore=f.read()
        if (hiscore != ''):
            hiscore=int(hiscore)
        else:
            hiscore=0
    

    if (score > hiscore):
        print('🎖️New high score!')
        with open('hiscore.txt', 'w') as f:
            f.write(str(score))
    else:
        print('Try again to beat the high score of', hiscore)
game()

#[Emoji's run in terminal but not here]