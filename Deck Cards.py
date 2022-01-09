import random

clubs1 = "clubs 8"
clubs2 = 'clubs 7'
clubs3 = 'clubs King'
clubs4 = 'clubs Ace'
heart1 = 'heart 2'
heart2 = 'heart 4'
heart3 = 'heart 3'
heart4 = 'heart Ace'
spades1 = 'Spades 7'
spades2 = 'Spades Jack'
spades3 = 'Spades King'
spades4 = 'Spades Queen'
diamonds1 = 'Diamonds 2'
diamonds2 = 'Diamonds Jack'
diamonds3 = 'Diamonds 9'
diamonds4 = 'Diamonds 10'

with open("cards_Deck.txt", "w") as file:
    file.writelines(clubs1+'\n'+clubs2+'\n'+clubs3+'\n'+clubs4+'\n'+heart1+'\n'+heart2+'\n'+heart3+'\n'+heart4+'\n'
                    + spades1+'\n'+spades2+'\n'+spades3+'\n'+spades4+'\n'+diamonds1+'\n'+diamonds2+'\n'+diamonds3+'\n'
                    + diamonds4)

with open("cards_Deck.txt", "r") as file:
    cards = file.read().splitlines()
    y=0
    for i in cards:
        y+=1
    if y<=10:
        print('Sunt mai putin de 10 carti! Mai adaugati!')
print(random.choice(cards))
