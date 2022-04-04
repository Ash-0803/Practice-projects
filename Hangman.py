import random
import hangman_art
from hangman_words import word_list
from os import system


stages_from_module = hangman_art.stages
lives=len(stages_from_module)
chosen_word = random.choice(word_list)

print(hangman_art.logo,'\n')

print(f"chosen word is {chosen_word} \n")

display=[]
for i in range(len(chosen_word)):
    display += "_"

end_of_game = False

while not end_of_game :
    print(f"{' '.join(display)}")
    letter = input("\nguess a letter from a to z  ")
    system('cls')
    temp=0

# to check the if the guessed letter is in the chosen word
    if letter in display:
            print("you have already guessed this letter, no life lost")
            temp=temp-1
    for chk_letter in range(len(chosen_word)) :     

        if chosen_word[chk_letter] == letter  :
            display[chk_letter] = chosen_word[chk_letter]
                        
        else:
            temp += 1 



# to print the hangman
    if temp == len(chosen_word):            #temp variable will become equal to the number of elements in display when no character matches the word.
        lives -= 1                          #to keep count of lives
        print(stages_from_module[lives])                                  
        print(f"ERROR 404, Letter '{letter}' not found \nlives left : {lives} \n")     
    else:
        print('correct guess!!! Good going')

# to check if you won the game    
    if "_" not in display:
        end_of_game=True
        print("you won!\n")
    elif(lives==0):
        end_of_game=True
        print("you lost!")
        print(f"the word was '{chosen_word}'")
    