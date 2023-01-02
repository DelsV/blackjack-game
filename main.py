import random
import os

card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Game variables
player_cards = []
player_score = 0
pc_cards = []
pc_score = 0


# Game functions
def show_pl_cards():
    print(f"\nYour cards are {player_cards}. Your current score is {player_score}")


def pc_draw():
    global pc_score
    new_card = random.choice(card_deck)
    pc_cards.append(new_card)
    pc_score += new_card
    print(f"Computer's first card: {pc_cards}. Current Computer score is {pc_score}")


def player_draw(num_draw: int):
    for i in range(0, num_draw):
        new_card = random.choice(card_deck)
        player_cards.append(new_card)
        global player_score
        player_score += new_card
    show_pl_cards()


def calc_result(pl_score, comp_score):
    if pl_score > 21:
        print("\n>>>> You went BUST! Computer wins! <<<<")
    elif comp_score > 21:
        print("\n>>>> Computer went BUST! You win! <<<<")
    elif pl_score == comp_score:
        print("\n>>>> It's a draw! <<<<")
    elif pl_score > comp_score:
        print("\n>>>> You win! <<<<")
    elif comp_score > pl_score:
        print("\n>>>> Computer wins! <<<<")


def play_on():
    continue_game = True
    global pc_score

    while continue_game:
        draw_again = input("\nWould you like to draw again? Y or N: ").lower()
        if draw_again == "y":
            player_draw(1)
            if player_score > 21:
                print("\n>>>> You went BUST! Computer wins! <<<<")
                continue_game = False
        elif draw_again == "n":
            while pc_score < 17:
                new_card = random.choice(card_deck)
                pc_cards.append(new_card)
                pc_score += new_card

            show_pl_cards()
            print(f"Computer's ending cards: {pc_cards}. Computer score is {pc_score}")

            calc_result(player_score, pc_score)

            continue_game = False


def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def clear_cards():
    global player_score
    player_score = 0
    global player_cards
    player_cards = []
    global pc_score
    pc_score = 0
    global pc_cards
    pc_cards = []


def game():
    print("\n------------------------------------------------------")
    print("Welcome to DV's Blackjack! Press any key to begin!: ")
    print("------------------------------------------------------")


    clear_cards()
    player_draw(2)
    pc_draw()
    play_on()

    play_again = input("\nWould you like to play again? Y or N: ").lower()

    if play_again == "y":
        # clearconsole() << broken
        game()
    else:
        print("\n Thank you for playing. Please come again!\n")


# Game
game()


# TODO: add blackjack functionality!
# TODO: fix ace multi-calc
# Add card names instead of just values


