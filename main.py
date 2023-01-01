import random

card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# begin_game = input("Start new game? (Y or N): ").lower()


# Player initial draw
player_cards = []
player_score = 0

def show_pl_cards():
    print(f"\nYour cards are {player_cards}. Your current score is {player_score}")


def draw_card(num_draw: int):
    for i in range(0, num_draw):
        new_card = random.choice(card_deck)
        player_cards.append(new_card)
        global player_score
        player_score += new_card
    show_pl_cards()


draw_card(2)

# PC initial draw
pc_cards = []
pc_score = 0
new_card = random.choice(card_deck)
pc_cards.append(new_card)
pc_score += new_card

print(f"Computer's first card: {pc_cards}. Current Computer score is {pc_score}")

# Calculate blackjack (add fn)

# Next turn?
continue_game = True

while continue_game:
    draw_again = input("\nWould you like to draw again? Y or N: ").lower()
    if draw_again == "y":
        draw_card(1)
        if player_score >21:
            print("You went BUST! Computer wins!")
            continue_game = False
    elif draw_again == "n":
        while pc_score < 16:
            new_card = random.choice(card_deck)
            pc_cards.append(new_card)
            pc_score += new_card

        print(f"\nComputer's ending cards: {pc_cards}. Computer score is {pc_score}")
        show_pl_cards()

        if player_score >21:
            print("You went BUST! Computer wins!")
        elif pc_score >21:
            print("Computer went BUST! You win!")
        elif player_score == pc_score:
            print("It's a draw!")
        elif player_score > pc_score:
            print("You win!")
        elif pc_score > player_score:
            print("Computer wins!")

        continue_game = False




# if draw_again == "y":
#     draw_again = True
#     draw_card(1)
#     show_pl_cards()
#
# else:
#     pass
