# "State Capitals" program
# Intro to Python, Final Exam Programming Section
#
# Matthew Sullivan
# December 15, 2015
#
# MAIN ROUTINE

import pickle
from scapmod import *


# ====================================================================
def main():
    # This text file contains the 50 state & capital pairs
    # Pairs are line-separated and internally comma-separated
    txt_fname = "statecapitals.txt"

    # Arbitrary name given to the file that store pickled dictionary
    db_fname = "stcaps.dat"

    print("State capitals guessing game!",
          "Enter XX to end game and proceed to scoring.",
          sep='\n')

    # Call open_file function in read mode
    txt_fobj = open_file(txt_fname, 'r')

    # Test if file opened successfully
    # Proceeding with program operation requires valid file object
    if txt_fobj:

        # Call function to create a dictionary from text file's data
        scap_dict = read_txt_file(txt_fobj)
        txt_fobj.close()

        # Just as a demonstration of the process, pickling the dict
        p_out_fobj = open_file(db_fname, 'wb')
        pickle.dump(scap_dict, p_out_fobj)
        p_out_fobj.close()

        # With the states & capitals dictionary pickled, ready to
        # create the actual gameplay within loop allowing for replay
        do_again = 1
        while do_again:

            # Open file containing pickled dictionary
            # Load pickled dictionary into new dictionary
            p_in_fobj = open_file(db_fname, 'rb')
            state_capitals = pickle.load(p_in_fobj)
            p_in_fobj.close()

            correct = 0
            wrong = 0
            out_of = len(state_capitals)

            # Continue game while more capitals remain to be guessed
            while state_capitals:

                # Using popitem() method to return a random item from
                # dictionary and remove it (ensuring it is asked once)
                q_item = state_capitals.popitem()

                # Obtain user's guess
                q_message = "What is the capital of " + q_item[0] + "? "
                user_guess = input(q_message)

                # Test user's guess against value (capital) within
                # the popped dictionary item (case-insensitive)
                if user_guess.lower() == q_item[1].lower():

                    # Increment count of correct answers if right
                    correct += 1
                    print("You're right!")

                # Condition wherein user opts to end game and go to scoring
                # Breaks out of containing while loop
                elif user_guess.upper() == 'XX':
                    break

                # Condition wherein user's guess is wrong
                else:

                    # Increment incorrect guess count
                    wrong += 1
                    print("Sorry, but that's wrong!"
                          "\nThe correct answer is:", q_item[1])

                # Print running score tally
                print("Your current score is:", correct, "correct,",
                      wrong, "wrong")

            # Upon exit of while loop (either by completion or forced exit)
            # Generate final score message and print
            score_message = ("---\nFinal score: " +
                             str(correct) + "/" + str(out_of) +
                             " (" + str(correct) + " correct, " +
                             str(wrong) + " wrong)")
            print(score_message)

            # Prompt user for replay
            do_again = boolny("Play again? ")

    # If no file object is returned from open_file, end routine
    else:
        print("No text file found! Terminating program.")

# ====================================================================


main()
