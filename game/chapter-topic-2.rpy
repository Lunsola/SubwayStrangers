####################################################
# TOPIC 2

label start_topic2:

    n "THIS IS TOPIC 2"

####################################################
    n "THIS IS THE FIRST PIECE OF CONVERSATION"

    # you should rearrange randomly the order of the answers to make this less obvious
    menu:
        "SHY ANSWER":
            if friendliness_meter<friendliness_cutoff:
                $ friendliness_meter = friendliness_meter+points_high
            else:
                $ friendliness_meter = friendliness_meter+points_low
            n "DIALOGUE FOR THE SHY ANSWER"

        "FRIENDLY ANSWER":
            if friendliness_meter>=friendliness_cutoff:
                $ friendliness_meter = friendliness_meter+points_high
            else:
                $ friendliness_meter = friendliness_meter+points_low
            n "DIALOGUE FOR THE FRIENDLY ANSWER"

        "MEDIUM ANSWER":
            $ friendliness_meter = friendliness_meter+points_medium
            n "DIALOGUE FOR THE SHY ANSWER"

    n "CONTINUE THE FIRST PIECE OF CONVERSATION"



####################################################
    n "THIS IS THE SECOND PIECE OF CONVERSATION"

    # you should rearrange randomly the order of the answers to make this less obvious
    menu:
        "SHY ANSWER":
            if friendliness_meter<friendliness_cutoff:
                $ friendliness_meter = friendliness_meter+points_high
            else:
                $ friendliness_meter = friendliness_meter+points_low
            n "DIALOGUE FOR THE SHY ANSWER"

        "FRIENDLY ANSWER":
            if friendliness_meter>=friendliness_cutoff:
                $ friendliness_meter = friendliness_meter+points_high
            else:
                $ friendliness_meter = friendliness_meter+points_low
            n "DIALOGUE FOR THE FRIENDLY ANSWER"

        "MEDIUM ANSWER":
            $ friendliness_meter = friendliness_meter+points_medium
            n "DIALOGUE FOR THE SHY ANSWER"

    n "CONTINUE THE SECOND PIECE OF CONVERSATION"




####################################################
    if friendliness_meter>=friendliness_cutoff:

        n "THIS IS THE EXTRA PIECE OF CONVERSATION"
        n "THIS IS UNLOCKED ONLY WITH HIGH FRIENDLINESS"

        # you should rearrange randomly the order of the answers to make this less obvious
        menu:
            "SHY ANSWER":
                if friendliness_meter<friendliness_cutoff:
                    $ friendliness_meter = friendliness_meter+points_high
                else:
                    $ friendliness_meter = friendliness_meter+points_low
                n "DIALOGUE FOR THE SHY ANSWER"

            "FRIENDLY ANSWER":
                if friendliness_meter>=friendliness_cutoff:
                    $ friendliness_meter = friendliness_meter+points_high
                else:
                    $ friendliness_meter = friendliness_meter+points_low
                n "DIALOGUE FOR THE FRIENDLY ANSWER"

            "MEDIUM ANSWER":
                $ friendliness_meter = friendliness_meter+points_medium
                n "DIALOGUE FOR THE SHY ANSWER"

    n "CONTINUE THE EXTRA PIECE OF CONVERSATION"



#############################################
    if time_current==time_destination:      # MOVE TO ENDING
        jump start_ending
    else:                                   # RETURN TO MENU
        jump menuTopics

    # This ends the game.
    return
