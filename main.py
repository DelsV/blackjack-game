import random

card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# begin_game = input("Start new game? (Y or N): ").lower()


# Player initial draw
player_cards = []
player_score = 0

for i in range(0,2):
    new_card = random.choice(card_deck)
    player_cards.append(new_card)

for i in player_cards:
    player_score += i

print(f"Your cards are {player_cards}. Your current score is {player_score}")

# PC initial draw
pc_cards = []
pc_score = 0
new_card = random.choice(card_deck)
pc_cards.append(new_card)

print(f"Computer's first card: {pc_cards}")