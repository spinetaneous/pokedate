# This file contains the events that will be part of the game. It's
# expected that the user will add and remove events as appropriate
# for this game.

#event format: $ event("event name", "act == required act and other requirements (e.g. stats), event methods, priority")

#############################################################
#notes:

#   player thinks single parents are normal and doesn't know that parents come in pairs
#   pikachu hates his mom for neglecting him bc she's pikabelle chutendo aka v busy
#   ditto just wants to fit in :(
#   player's mom was fished out of the ocean before dad's very eyes :(((((
#   player was adopted out of all the other orphans bc she's a human and
#     mom would have wanted to help someone different and in need
#   pikachu loves player because player fought off his childhood bullies bc she genki af

#   remember to introduce pokedex properly
#   events based on number of affection pts need a backup event (since the only stats that will trigger anything are affection pts)
#############################################################

# Some characters that are used in events in the game.
init:
    define narrator = Character(' ')
    define unknown = Character('??????')

    define t = Character('Teacher')
    define player = Character('[name]', color="#0d4b72")
    define dad = Character('Dad')
    define pdex = Character('Pokedex')
    define trap = Character('Riley', color="#a3daf6")

    define jynx = Character('Jynx', color="#70018b")
    define bulb = Character('Bulbasaur', color="#008080")
    define digl = Character('Diglett', color="#ab4221")
    define pika = Character('Pikachu', color="#ffd700")

init:
    # First up, we define some simple events for the various actions, that
    # are run only if no higher-priority event is about to occur.
    python:
        event("class1", "act == 'class'", event.solo(), event.choose_one("class"), priority=1000)
        event("class2", "act == 'class'", event.solo(), event.choose_one("class"), priority=1000)
        event("work", "act == 'mall'", event.solo(), event.depends("get_hired"), priority=1000)
        event("skip_work1", "act == 'skip_work'", event.solo(), priority=1000)
        event("eat_lunch1", "act == 'lunch1'", event.solo(), priority=1000)
        event("eat_lunch2", "act == 'lunch2'", event.solo(), priority=1000)
        event("eat_lunch3", "act == 'lunch3'", event.solo(), priority=1000)
        event("salon", "act == 'salon'", event.solo(), priority=1000)
    
        event("get_hired", "act == 'mall'", event.solo(), event.once(), priority=1000)
        event("salon1", "act == 'salon'",event.solo(), event.once(), priority=990)
        event("meet_ditto", "act == 'class'", event.solo(), event.once(), priority=990)
    
    
#Below are the boring events that happen when there are no higher priority events.

label class1:
    "I run to school and make it well before the bell rings."
    "Although {i}inside{/i} of the school, I speed-walked."
    "One is not supposed to run in the hallways!"
    "..."
    "Nothing interesting happened during class."
    return
    
label class2:
    "I run to school and make it well before the bell rings."
    "Nothing worth mentioning happens."
    return

label work: #this only happens after you get hired
    "I head to my job at the mall and strengthen my resolve as I sell pokepuffs."
    "I've got to work hard if I want to get {i}PokeCrossing: Happy Ball Designer!{/i}"
    python:
        if skipped_work < 3:
            inventory.earn(30)
        elif skipped_work >= 3 and skipped_work < 6:
            inventory.earn(20)
        elif skipped_work >= 6 and skipped_work < 9:
            inventory.earn(10)
        else:
            inventory.earn(5) #you can't get fired because riley really needs an employee
            "It's difficult with such little pay, though..."
    return
    
label eat_lunch1:
    "I head over to the underclassmen classes and sit down."
    "...But I don't see anyone I know here."
    "Eh, whatever. I don't want to go back to my own classroom after having walked all this way."
    "I don't really care if people give me weird looks."
    "I begin eating my lunch."
    return
    
label eat_lunch2:
    "Since people eat their lunches in classrooms, and I'm already in my own classroom, I might as well eat here."
    "Conserving energy for important times is a very crucial skill!"
    return

label eat_lunch3:
    "I head over to the upperclassmen classes."
    "...But I don't see anyone I know here."
    "...But then again, it's not like I really care. We're all students at the same school, so I can eat wherever."
    "It doesn't matter if people look at me weirdly."
    return

label skip_work1:
    "I don't feel like working today."
    "Sorry, Riley."
    "I'm sure the store can run with one less person today."
    $ skipped_work += 1
    return
    
label salon:
    "I went to the salon, but Jynx is nowhere to be found."
    "Maybe she has a day off? Or maybe I'm just really bad at finding people..."
    "I spend the rest of the time looking at all the fancy hair products."
    return
#Below are the events actually matter.

label get_hired: #the first time player goes to the mall, trap hires her
    "u got job yay"
    $ has_job = True
    pass
    return
    
label meet_ditto: #the first time player goes to class, she notices ditto
    if char_dex == True:
        "I stayed up late last night texting Charmander, so it's difficult to wake up in the morning."
        "But I do it."
        "I wipe the sleep from my eyes because I am {i}determined not to be late!{/i}"
    elif char_dex == False:
        "What a good night's sleep! I feel so refreshed and awake."
        "I'm totally ready to get a job after school!"
        "Wait for me, {i}PokeCrossing: Happy Ball Designer{/i}..."
    return
    
label salon1: #the first time player goes to salon, she gets a haircut by jynx LOL surprise
    "So this is the salon that Jynx works at..."
    "It looks like a popular salon. There's even people lining out the door."
    unknown "Hey, [name]! You finally came to visit! Glad to see you!"
    "Who's calling me?"
    jynx "How's it going?"
    "Oh, it's Jynx!"
    player "Hey, Jynx! How are--"
    jynx "So you decided to listen to my advice, right!?"
    player "H-Huh?"
    jynx "You came because you wanted me to make you pretty, right?"
    "Oh yeah, she said that she would 'fix me up all nice and pretty'..."
    player "W-Well, I didn't--"
    jynx "{size=+5}Sit down here, honey!{/size}"
    "Jynx grabs me by the shoulders and drags me to a chair."
    "She drapes fabric around my shoulders and clips the edges to prevent it from falling."
    "..."
    "Did I just cut everyone waiting in line?"
    jynx "Now then, don't worry about a thing! I'll make sure you walk outta this room looking better than ever!"
    player "Y-You know, I really--"
    jynx "This is the first time I've ever cut a {i}human's{/i} hair! Thank you for giving me experience!"
    player "{i}You're cutting my hair?{/i}"
    jynx "Don't worry! {size=-10}-snip-{/size} I trim the fur {size=-10}-snip-{/size} on Furfrou pokemon {size=-10}-snip-{/size} all the time!"
    "My eyes are downcast the entire time, so I can only watch in horror as locks of my hair flutter to the floor."
    "I don't dare to look up at the mirror."
    jynx "Oh my goodness! {size=-10}-snip-{/size} This haircut is {size=-10}-snip-{/size} going to be so {size=-10}-snip-{/size} amazing!"
    "{size=-10}snip...snip...snip...snip...snip...{/size}"
    "{size=-10}......snip......snip......snip......{/size}"
    "{size=-10}...snip...snip...snip...{/size}"
    jynx "There you go--You're gorgeous!"
    "At this point, I'm so tired of being dragged around that I don't even bother to look in the mirror."
    player "Thanks, Jynx. Well, I'd best be going! See you tomorrow!"
    jynx "No problem, sweetie."
    "And with that, I get out of that salon."
    return
