cards = [i + 1 for i in range(int(input()))]

while True:
    if len(cards) == 1:
        cur_card = cards.pop(0)
        break
    
    if len(cards) % 2 == 0:
        cards = cards[1::2]
    else:
        last_card = cards.pop()
        cards = cards[1::2]
        cards.insert(0, last_card)
print(cur_card)