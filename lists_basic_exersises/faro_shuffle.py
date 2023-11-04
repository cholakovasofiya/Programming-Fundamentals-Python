deck_cards = input().split()
number_shuffles = int(input())

# A = [1,2,3,4,5,6] split the list in two
# B = A[:len(A)//2]
# C = A[len(A)//2:]

for shuffle in range(number_shuffles):
    left_part = deck_cards[:len(deck_cards) // 2]
    right_part = deck_cards[len(deck_cards) // 2:]
    final_deck_cards = []
    for card in range(len(left_part)):
        final_deck_cards.append(left_part[card])
        final_deck_cards.append(right_part[card])

    deck_cards = final_deck_cards
print(final_deck_cards)
