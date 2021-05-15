# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

####################################################
# CHARACTERS
define p  = Character("Protagonist",color="#ff0000")                          # protagonist
define s  = Character("Stranger",color="#0000ff")                             # stranger
define n  = Character("Narrator",color="#888888")                             # narrator





####################################################
# START

label start:

    # INITIALIZE VARIABLES

    # NUMBER OF STATIONS
    $ time_destination = 4          # number of rounds / topics
    $ time_current     = 0          # keep track of time

    # FRIENDLINESS MECHANIC
    $ friendliness_meter  = 0       # START WITH THIS MANY POINTS
    $ friendliness_cutoff = 50      # UNLOCK FRIENDLY DIALOGUES WITH THIS MANY
    $ points_high   = 20            # # points for a good conversation
    $ points_medium = 7             # # points for a medium conversation
    $ points_low    = 1             # # points for a bad conversation

    # CONVERSATION TOPICS
    $ topic1_flag = 0               # initialize: no topic discussed yet
    $ topic2_flag = 0
    $ topic3_flag = 0
    $ topic4_flag = 0
    $ topic5_flag = 0

    # ENDING REQUIREMENTS
    $ end2_requirement = 50             # you need so many points to unlock the ending
    $ end3_requirement = 100

    # TESTING?
    $ testing_mode = True

    # BACKGROUND?
    scene bg subwayBackground


    # START WITH LINEAR INITIAL DIALOGUES
    jump start_topic0




####################################################
# MENU OF TOPICS

label menuTopics:
    n "THIS IS THE MAIN MENU"
    n "CHOOSE A TOPIC FOR DIALOGUE"

    menu:
        "TOPIC 1" (disabled=False) if topic1_flag==0:
            $ time_current= time_current+1              # update time
            $ topic1_flag = 1                           # the topic is covered
            jump start_topic1
        "TOPIC 1" (disabled=True) if topic1_flag==1:
             jump start_topic1
        "TOPIC 2" (disabled=False) if topic2_flag==0:
            $ time_current= time_current+1
            $ topic2_flag = 1
            jump start_topic2
        "TOPIC 2" (disabled=True) if topic2_flag==1:
            jump start_topic2
        "TOPIC 3" (disabled=False) if topic3_flag==0:
            $ time_current= time_current+1
            $ topic3_flag = 1
            jump start_topic3
        "TOPIC 3" (disabled=True) if topic3_flag==1:
            jump start_topic3
        "TOPIC 4" (disabled=False) if topic4_flag==0:
            $ time_current= time_current+1
            $ topic4_flag = 1
            jump start_topic4
        "TOPIC 4" (disabled=True) if topic4_flag==1:
            jump start_topic4
        "TOPIC 5" (disabled=False) if topic5_flag==0:
            $ time_current= time_current+1
            $ topic5_flag = 1
            jump start_topic5
        "TOPIC 5" (disabled=True) if topic5_flag==1:
            jump start_topic5




    # This ends the game.
    return
