#trial blackjack
import random
deck=["┌───┐\n│1 ♠│\n└───┘","┌───┐\n│2 ♠│\n└───┘","┌───┐\n│3 ♠│\n└───┘",
     "┌───┐\n│4 ♠│\n└───┘","┌───┐\n│5 ♠│\n└───┘","┌───┐\n│6 ♠│\n└───┘",
     "┌───┐\n│7 ♠│\n└───┘","┌───┐\n│8 ♠│\n└───┘","┌───┐\n│9 ♠│\n└───┘",
     "┌───┐\n│10♠│\n└───┘","┌───┐\n│J ♠│\n└───┘","┌───┐\n│K ♠│\n└───┘",
     "┌───┐\n│Q ♠│\n└───┘"]
def hit_or_stay():
    player_deck.append(deal_card())
    for card in player_deck:
        return card
def deal_card():
    card_dealt=random.choice(deck)
    return card_dealt

def assign_p_value():
    total_score=0
    for card in player_deck:
        total_score+=deck_key[card]
    return total_score

def assign_value():
    total_score=0
    for card in ai_deck:
            total_score+=(deck_key[card])
    return total_score
face_side="┌───┐\n│???│\n└───┘\n"
ai_deck=[]
ai_value=0
player_deck=[]
player_value=0
deck_key={
    "┌───┐\n│1 ♠│\n└───┘":1,
    "┌───┐\n│2 ♠│\n└───┘":2,
    "┌───┐\n│3 ♠│\n└───┘":3,
    "┌───┐\n│4 ♠│\n└───┘":4,
    "┌───┐\n│5 ♠│\n└───┘":5,
    "┌───┐\n│6 ♠│\n└───┘":6,
    "┌───┐\n│7 ♠│\n└───┘":7,
    "┌───┐\n│8 ♠│\n└───┘":8,
    "┌───┐\n│9 ♠│\n└───┘":9,
    "┌───┐\n│10♠│\n└───┘":10,
    "┌───┐\n│J ♠│\n└───┘":10,
    "┌───┐\n│K ♠│\n└───┘":10,
    "┌───┐\n│Q ♠│\n└───┘":10
}
new_round="y"
play_round=input("Wanna play a round?:\n'y' for yes and 'n' for no\n")
while new_round=="y":
    ai_deck.append(deal_card())
    ai_deck.append(deal_card())
    print("Dealer hand:\n"+ai_deck[0])
    print(face_side)
    ai_value=(assign_value())
    new_round="no"
player_deck.append(deal_card())
player_deck.append(deal_card())
while play_round=="y":
    print("Player1 hand:")
    for card in player_deck:
     print(card)
    player_value=(assign_p_value())
    p_val=player_value
    if p_val>21:
        print("value exceeded 21, you have lost!!")
        break
    elif p_val==21:
        print("YOU SCORED 21!!! YOU WIN!!!")
        break
    next=input("Do you want a card?\n'y' for yes 'n' for no\n")
    if next=="y":
        hit_or_stay()
    else:
        if ai_value>=player_value:
            print(f"Dealer value is {ai_value}. Your value is NOT higher than dealer. You lost!!")
            play_round='n'
        elif player_value>ai_value:
            print(f"Dealer value is {ai_value}. YOUR VALUE IS HIGHER!!!\n YOU WIN!!!")
            break
    if p_val>21:
        print("value exceeded 21, you have lost!!")
        play_round="n"
