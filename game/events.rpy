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
    
    $ event("class", "act == 'class'", event.solo(), priority=200)
    $ event("mall", "act == 'mall'", event.solo(), priority=200)
    #$ event("hang1", "act == 'hang'", event.choose_one('hang'), priority=200)
    #$ event("hang2", "act == 'hang'", event.choose_one('hang'), priority=200)
    #$ event("exercise", "act == 'exercise'", event.solo(), priority=200)
    #$ event("play", "act == 'play'", event.solo(), priority=200)
    
    # This is an introduction event, that runs once when we first go
    # to class. 
    #$ event("introduction", "act == 'class'", event.once(), event.only())
    

    
#Below are the boring events that happen when there are no higher priority events.

label class:
    "this is class"
    return

label mall:
    "hangin out at the mall desu"
    return
    
label choose_shop:
    "Which shop should I go to?"
    "idk <insert menu here>"
    return