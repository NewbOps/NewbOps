import sys
import random
from enum import Enum

# game_count = 0


def parent_func():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # playagain = True

        playerchoice = input(
            '\nenter ...\n1 for rock, \n2 for paper, \n3 for scissors:\n\n')

        if playerchoice not in ['1', '2', '3']:
            print('you must enter 1, 2, or 3.')
            return play_rps()

        player = int(playerchoice)

        # if player < 1 or player > 3:
        #     sys.exit('you must enter 1, 2, or 3.')

        computerchoice = random.choice('123')

        computer = int(computerchoice)

        print('\nyou chose ' + str(RPS(player)).replace('RPS.', ''))
        print('python chose ' + str(RPS(computer)).replace('RPS.', ''))
        print('')

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return '❤️ you win'
            elif player == 2 and computer == 1:
                player_wins += 1
                return '❤️ you win'
            elif player == 3 and computer == 2:
                player_wins += 1
                return '❤️ you win'
            elif player == computer:
                return '🙌 tie'
            else:
                python_wins += 1
                return '🐍 you lose'

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print('\ngame count: ' + str(game_count))
        print('\nplayer wins: ' + str(player_wins))
        print('\npython wins: ' + str(python_wins))

        print('\nplay again?')
        while True:
            playagain = input(
                ' \n\ny for Yes \n or \nn to quit \n\n')
            if playagain.lower() not in ['y', 'n']:
                continue
            else:
                break

        if playagain.lower() == 'y':
            return play_rps()
        else:
            print('\nboo😒\n')
            sys.exit('\nbye\n')

    return play_rps()


play = parent_func()

play()
