####################################################
# TOPIC 1

label start_topic0:
    scene bg subwayclosed
    show npc neutral
    "It’s almost midnight...."
    "Hardly anyone left on the train..."
    "Gosh, I’m so tired..."
    "I wonder who that guy is?"
    "I feel like I’ve seen him on the train before..."
    "Then again you see a lot of people on the train."
    "Eventually they all kind of blend together."

    menu:
        "Put in headphones":
            "It's been a long day."
            "I just want to go home."
        "Talk to stranger":
            #show npc confused
            menu:
                "Excuse me?":
                    p "Excuse me?"
                    s "Sorry?"
                    p "Hi, sorry to bother you. I just feel like I’ve seen your face somewhere."
                    s "Oh. Maybe we’ve been on this train before? I usually leave work pretty late."
                    p "I don’t know, I usually don’t ride the train this late."
                "Hi!":
                    p "Hi!"
                    s "Um, hello."
                    p "Pretty quiet tonight, huh?"
                    s "I guess? The train’s usually empty when I’m going home."
                    p "Yeah, I’m usually not up this late."
            #show npc neutral
            s "Busy night?"
            menu:
                "Yeah, I was just at a party":
                    #show npc happy
                    s "Oh, fun!"
                    menu:
                        "Honestly, wasn't really my scene":
                            #show npc neutral
                            s "At least you get to see your friends, right?"
                            p "Well, I knew a couple people there, but it kind of got way too loud."
                            p "I like when it's quiet."
                            s "Like now?"
                            window hide
                            p "Yeah, I guess."
                        "Yeah, basically all my friends were there":
                            s "Nice."
                "No, I'm just riding the subway for fun":
                    #show npc confused
                    s "You're serious?"
                    p "Yeah, I just like riding around the city sometimes."
                    s "Oh, sorry if that came off rude."
                    s "I've just never heard of anyone who's done that before."



    jump menuTopics

    # This ends the game.
    return
