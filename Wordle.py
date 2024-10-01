########################################
# Name:Salem Fraire
# Collaborators (if any):N/A
# GenAI Transcript (if any):N/A
# Estimated time spent (hr): ~ 4 hours
# Description of any added extensions: 0
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random


def wordle():
    # The main function to play the Wordle game.
    random.shuffle(ENGLISH_WORDS)

    for t in range(len(ENGLISH_WORDS)):
        if len(ENGLISH_WORDS[t]) == 5:
            correct = ENGLISH_WORDS[t].upper()



    def enter_action():
        word_entered = ''

        #use this to elimate the green letter so when the yellow letter checker runs it doesnt say yellow there if green there

        for i in range(5):
            word_entered += gw.get_square_letter(gw.get_current_row(), i)
            #colors letters
        if len(word_entered) == 5:
            compare = [word_entered[0], word_entered[1], word_entered[2], word_entered[3], word_entered[4]]

            #use this to elimate the green letter so when the yellow letter checker runs it doesnt say yellow there if green there
            letters = ''

            for j in range(5):
                if compare[j] == correct[j]:
                    gw.set_square_color(gw.get_current_row(), j, CORRECT_COLOR)
                    gw.set_key_color(word_entered[j], CORRECT_COLOR)

                    if letters in compare[j] and len(letters) > 0:
                        letters += '*'
                    else:
                        letters += '*'
            
                else:
                    gw.set_key_color(word_entered[j], MISSING_COLOR)
                    letters += word_entered[j]



            


            for k in range(5):
                #yellows the somewaht correct letters(Correct letter, wrong area)
                if letters[k] in correct:
                    gw.set_square_color(gw.get_current_row(), k, PRESENT_COLOR)
                    gw.set_key_color(letters[k], PRESENT_COLOR)




        # What should happen when RETURN/ENTER is pressed.
        #display the entered word
        if len(word_entered) == 5:
            gw.show_message(correct)
            

            gw.set_current_row(gw.get_current_row() + 1)
    



    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


    

# Startup boilerplate
if __name__ == "__main__":
    wordle()
