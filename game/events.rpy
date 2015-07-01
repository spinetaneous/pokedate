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
    
    $ event("class1", "act == 'class'", event.solo(), event.choose_one("class"), priority=1000)
    $ event("class2", "act == 'class'", event.solo(), event.choose_one("class"), priority=1000)
    $ event("mall1", "act == 'mall'", event.solo(), event.depends("get_hired"), priority=1000)
    $ event("skip_work1", "act == 'skip_work'", event.solo(), priority=1000)
    $ event("salon", "act == 'salon'",event.solo(), priority=1)
    #$ event("hang1", "act == 'hang'", event.choose_one('hang'), priority=200)
    #$ event("hang2", "act == 'hang'", event.choose_one('hang'), priority=200)
    #$ event("exercise", "act == 'exercise'", event.solo(), priority=200)
    #$ event("play", "act == 'play'", event.solo(), priority=200)
    # This is an introduction event, that runs once when we first go
    # to class. 
    #$ event("introduction", "act == 'class'", event.once(), event.only())
    
    $ event("get_hired", "act == 'mall'", event.solo(), event.once(), priority=1000)
    
    $ event("meet_ditto", "act == 'class'", event.solo(), event.once(), priority=990)

    
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
label mall1:
    "I head to my job at the mall and strengthen my resolve as I sell pokepuffs."
    "I've got to work hard if I want to get {i}PokeCrossing: Happy Ball Designer!{/i}"
    $ inventory.earn(30)
    return
    
label choose_shop:
    "Which shop should I go to?"
    "idk lol"
    #insert menu here lol
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
    if char_dex == True:
        "I stayed up late last night texting Charmander, so it's difficult to wake up in the morning."
        "But I do it."
        "I wipe the sleep from my eyes because I am {i}determined not to be late!{/i}"
    elif char_dex == False:
        "What a good night's sleep! I feel so refreshed and awake."
        "I'm totally ready to get a job after school!"
        "Wait for me, {i}PokeCrossing: Happy Ball Designer{/i}..."
    
    return
    
    