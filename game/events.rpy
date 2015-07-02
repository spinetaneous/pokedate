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
#############################################################

# Some characters that are used in events in the game.
init:
    define narrator = Character(' ')
    define unknown = Character('??????')

    define t = Character('Teacher')
    define player = Character('[name]', color="#0d4b72")
    define dad = Character('Dad')
    define pdex = Character('Pokedex')

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
    
    
        event("salon", "act == 'salon'",event.solo(), priority=1)
    #$ event("hang1", "act == 'hang'", event.choose_one('hang'), priority=200)
    #$ event("hang2", "act == 'hang'", event.choose_one('hang'), priority=200)
    #$ event("exercise", "act == 'exercise'", event.solo(), priority=200)
    #$ event("play", "act == 'play'", event.solo(), priority=200)
    # This is an introduction event, that runs once when we first go
    # to class. 
    #$ event("introduction", "act == 'class'", event.once(), event.only())
    
        event("get_hired", "act == 'mall'", event.solo(), event.once(), priority=1000)
    
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

#This only happens after you get hired.
label work:
    "I head to my job at the mall and strengthen my resolve as I sell pokepuffs."
    "I've got to work hard if I want to get {i}PokeCrossing: Happy Ball Designer!{/i}"
    $ inventory.earn(30)
    return
    
label eat_lunch1:
    "I head over to the underclassmen classes."
    "...But I don't see anyone here."
    "Eh, whatever. I don't want to go back to my own classroom after having walked all this way."
    "I don't really care if people give me weird looks."
    return
    
label eat_lunch2:
    "Since people eat their lunches in classrooms, and I'm already in my own classroom, I might as well eat here."
    "Conserving energy for important times is a very crucial skill!"
    return

label eat_lunch3:
    "I head over to the upperclassmen classes."
    "...But I don't see anyone here."
    "...But then again, it's not like I really care. We're all students at the same school, so I can eat wherever."
    "It doesn't matter if people look at me weirdly."
    return

label skip_work1:
    "why didn't u go to work huh"
    return
    
#Below are the events actually matter.

label salon:
    "yo u at salon"
    return

label get_hired:
    #the first time player goes to the mall, trap hires her
    "u got job yay"
    $ has_job = True
    pass
    return
    
label meet_ditto:
    #player's room
    if char_dex == True:
        "I stayed up late last night texting Charmander, so it's difficult to wake up in the morning."
        "But I do it."
        "I wipe the sleep from my eyes because I am {i}determined not to be late!{/i}"
        "Not to mention that I've also got to be awake if I want to get a job after school..."
    elif char_dex == False:
        "What a good night's sleep! I feel so refreshed and awake."
        "I'm totally ready to get a job after school!"
        "Wait for me, {i}PokeCrossing: Happy Ball Designer{/i}..."
    #fade to school
    
    ""
    return
    
    