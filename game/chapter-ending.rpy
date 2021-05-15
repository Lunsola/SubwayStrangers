####################################################
# ENDING

label start_ending:

    n "START ENDING CHAPTER"
    n "THIS IS YOUR FINAL DESTINATION"
    n "COMMON PART HERE, THEN BASED ON THE FRIENDLINESS SCORE YOU GO TO ONE OF THE ENDINGS"

    # ENDING 1: LOW SCORE
    if friendliness_meter<end2_requirement:
        jump start_ending1

    # ENDING 3: HIGH SCORE
    if friendliness_meter>=end3_requirement:
        jump start_ending3

    # ENDING 2: INTERMEDIATE SCORE
    jump start_ending2

    # This ends the game.
    return



####################################################
# ENDING 1

label start_ending1:
    n "LOW SCORE ENDING"
    # This ends the game.
    return


####################################################
# ENDING 2

label start_ending2:
    n "MEDIUM SCORE ENDING"
    # This ends the game.
    return


####################################################
# ENDING 3

label start_ending3:
    n "HIGH SCORE ENDING"
    # This ends the game.
    return
