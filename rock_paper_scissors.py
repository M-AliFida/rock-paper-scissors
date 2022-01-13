import random

print("How many times do you want to play?" , end = ' ')
number_of_games = int(input())

def main():
    introduction()
    total_score = 0
    last_winner = 0
    last_user_mover = 0

    for i in range(number_of_games):
        if (i == 0):
            # random move
            ai_move = get_ai_move()
        else:
            ai_move = ai_move_win_strategy(last_winner, last_user_mover)

        user_move = get_user_move()
        last_user_mover = user_move
        winner = get_winner(ai_move, user_move)
        last_winner = winner
        total_score = update_score(winner, total_score)
        print('\nYou:', user_move)
        print("AI:", ai_move)

        if(winner == "tie"):
            print("TIE!")
        else:
            print(winner.upper(), "WINS!")
        print("----------------------------------------------")
        print("Current Score:", total_score)
        print('')
        
    print('Final Score:', total_score)
    play_again = input("\nPlay again (y/n)? ").lower()
    if(play_again == "y"):
        main()
    elif (play_again == "n"):
        exit()
    exit()

def ai_move_win_strategy (last_winner, last_user_mover):
    # Strategy:
    # WIN: If you win, play the hand your opponent played.
    # LOST: If you lose, play the hand that would beat what your opponent just played.
    # e.g. if user wins and picks rock, AI will pick paper. 
    # e.g. if AI wins using rock, it will pick scissors (what user picked).
    if (last_winner == 'ai'):
        return last_user_mover
    if (last_winner == 'user'):
        if (last_user_mover == 'rock'):
            return 'paper'
        if (last_user_mover == 'paper'):
            return 'scissors'
        return 'rock'
    if (last_winner == 'tie'):
        return get_ai_move()

def update_score(winner, total_score):
    # updates and returns total score
    if (winner == 'user'):
        total_score += 1
    if (winner == 'ai'):
        total_score -= 1
    if (winner == 'tie'):
        total_score += 0
    return total_score

def get_winner(ai_move, user_move):
    # rock beats scissors
    # scissors beats paper
    # paper beats rock
    # tie if the same
    if ai_move == user_move:
        return "tie"
    if ai_move == "rock":
        # if ai move is `rock` two options for 
        # user move can be paper | scissors
        if user_move == "paper":
            return "user"
        return "ai"
    if ai_move == "paper":
        if user_move == "rock":
            return "ai"
        return "user"
    if ai_move == "scissors":
        if user_move == "paper":
            return "ai"
        return "user"
    print('you are in the danger zone!')

def get_ai_move():
    # uses random int to generate move for the ai
    value = random.randint(1, 3)
    if value == 1:
        return "rock"
    if value == 2:
        return "paper"
    return "scissors"

def get_user_move():
    # gets and returns a valid move for the user
    while True:
        user_move = input("Enter Move (rock ✊ | paper ✋ | scissors ✌): ").lower()

        if is_valid_move(user_move):
            return user_move
        print("\nInvalid move!", "\U0000274C", "\n")

def is_valid_move(move):
    # check to see of move was valid (parameter check)
    if move == "rock":
        return True
    if move == "paper":
        return True
    if move == "scissors":
        return True
    return False

def introduction():
    print('\n----------------------------------------------')
    print("\nWelcome to", "Rock", ("\U0000270A"), "Paper", ("\U0000270B"), "Scissors", ("\U0000270C"))
    print("\nYou will play " + str(number_of_games) + ' games against the AI\n')
    print("The outcomes are: \n")
    print("1. rock beats scissors")
    print("2. scissors beats paper")
    print("3. paper beats rock")
    print("4. tie if the same\n")
    print("Good Luck!")
    print('----------------------------------------------')
    print("")


if __name__ == "__main__":
    main()