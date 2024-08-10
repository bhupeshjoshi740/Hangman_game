import random
word_List=["apple","beautiful","potato"]
Lives=6
chosen_word=random.choice(word_List)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter:").lower()
    for position in range(len(chosen_word)):
        Letter = chosen_word[position]
        if Letter==guessed_letter:
            display[position]= guessed_letter
    print(display) 

    if guessed_letter not in chosen_word:
        Lives -= 1
        if Lives == 0:
            game_over = True
            print("You lose!!")
    if '_' not in display:
        game_over=True
        print("You win!!")                       
