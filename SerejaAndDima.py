cards_count = input()
cards = input()
cards = cards.split(' ')
cards = list(map(int, cards))

sereja = 0
dima = 0
turn = True
max_value = -1
# print(cards)
# print('================================')
for i in range(0,len(cards)):
    # print(str(cards[-1])+' > '+str(cards[0])+'?')
    if(len(cards)==1):
        if turn:
            sereja += cards[0]
            turn = False
        else:
            dima += cards[0]
            turn = True

    if cards[-1] > cards[0]:
        if turn:
            sereja += cards[-1]
            turn = False
        else:
            dima += cards[-1]
            turn = True

        del cards[-1]
    elif cards[-1] < cards[0]:
        if turn:
            sereja += cards[0]
            turn = False
        else:
            dima += cards[0]
            turn = True
        del cards[0]
    # print(cards)
    # print('[Sereja: '+str(sereja)+' , Dima: '+str(dima)+']')
    # print(turn)

# print('Sereja: '+str(sereja)+' , Dima: '+str(dima))
print(str(sereja)+' '+str(dima))

# def nextTurn(player1,player2,turn_flag,card_value):
#     player1 + card_value if turn_flag else player2 + card_value