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
    define dad = Character('Dad', color="#e74c14")
    define pdex = Character('Pokedex')
    define trap = Character('Riley', color="#a3daf6") #works at la pokesserie

    #pokemon (besides dad)
    define jynx = Character('Jynx', color="#70018b") #works at salon
    define bulb = Character('Bulbasaur', color="#008080") #works at florist/is the florist
    define digl = Character('Diglett', color="#ab4221") #works at gym
    define pika = Character('Pikachu', color="#ffd700") #at school... maybe one day u can go to house????
    define char = Character('Charmander', color="#ff760d") #at park all the time

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
    
        event("get_hired", "act == 'job_hunt'", event.solo(), event.once(), priority=999)
        event("salon1", "act == 'salon'",event.solo(), event.once(), priority=999)
        event("meet_ditto", "act == 'class'", event.solo(), event.once(), priority=999)
    
    
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
    
label skip_work1:
    "I don't feel like working today."
    "Sorry, Riley."
    "I'm sure the store can run with one less person today."
    "Instead, it's time for me to play video games! {i}PokeCrossing: New Ball{/i}, here I come..."
    $ skipped_work += 1
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

label salon:
    "I went to the salon, but Jynx is nowhere to be found."
    "Maybe she has a day off? Or maybe I'm just really bad at finding people..."
    "I spend the rest of the time looking at all the fancy hair products."
    return
#Below are the events actually matter.

label get_hired: #the first time player goes to the mall, trap hires her
    player "The time has come..."
    player "I'm not leaving the mall today unless I get a job!"
    player "It shouldn't be that hard, right?"
    #fade gamemon
    "I walk into Gamemon."
    player "Excuse me! I'd like a job!"
    "No one answers."
    player "{size=+5}Hello! I would like to get a job here!{/size}"
    "People start looking at me."
    "...But no one is hiring me!"
    "I wonder if I'm being ignored... Maybe I should try somewhere else..."
    #fade florist
    "Maybe Bulbasaur is looking for employees?"
    player "Hey Bulbasaur, remember me?"
    bulb "Oh yeah, didn't you come here with your boyfriend or something?"
    player "Haha, we're not dating."
    bulb "Is that so? I see."
    bulb "May I help you? Are you looking for anything in particular?"
    player "In fact, I am!"
    player "I'm looking for a job!"
    bulb "Oh, I see."
    bulb "Well, you're in luck! I'm currently hiring."
    player "Really? That's great! When do I start?!"
    bulb "Hold on, I didn't hire you yet."
    player "What?"
    bulb "Well, I have to see if you're suitable for the store after all."
    bulb "Why do you want this job?"
    menu:
        "Money.":
            bulb "Hm..."
        "Fame.":
            bulb "I'm not sure if working here is a good start for that..."
        "To make my father proud of me.":
            bulb "I see..."
    bulb "Next, do you know anything about flowers?"
    menu:
        "Roses are red?":
            bulb "Most of the time, yeah..."
        "Violets are blue?":
            bulb "At least you know that they aren't violet..."
        "What are flowers?":
            bulb "..."
            bulb "Um..."
    bulb "I see... Finally, are you experienced in working a cash register?"
    menu:
        "The click-clack cash thingy?":
            bulb "Uh..."
        "Yeah, totally!":
            bulb "Really? Did you use one in a previous job?"
            player "No, but it's kind of like a big calculator, right? I know how to use a calculator!"
            bulb "..."
        "What's a \"cash register\"?":
            bulb "..."
            bulb "Are you serious?"
    bulb "Uh... I think you're better off looking elsewhere."
    bulb "Sorry."
    player "Aw..."
    player "It's ok! I won't let another failure get me down!"
    player "I WILL CONQUER THE JOB MARKET!"
    player "Seeya!"
    bulb "Bye."
    #fade gym
    "Now I'm at the gym. Wow, this place smells of sweat!"
    "But it also smells like potential cash to be made... Heh."
    unknown "It's not enough that you're rude to me, so you follow me to my workplace too!?"
    player "!?"
    digl "What's with you!?"
    player "Y-You..."
    player "You work here?"
    digl "You followed me here without even knowing that? How dumb are you?"
    player "I didn't follow you! I came to get a job!"
    digl "A job? Here?"
    digl "You're even going as far as to work in the same place as I do?"
    digl "That's going too far. Are you a yandere?"
    player "First of all, I don't even know what that is."
    player "And secondly, you're not the reason I want to work! I just want money!"
    digl "Oh, so any place is good as long as you get hired?"
    player "Yeah!"
    digl "Then go get hired somewhere else! The gym isn't hiring right now!"
    player "Really?! Dang... That's too bad..."
    player "I guess I need to try somewhere else then."
    digl "..."
    digl "{size=-5}You could try the bakery... \"La Pokesserie\" I think it was called...{/size}"
    player "Really? Thanks!"
    digl "Y-You heard that!?"
    digl "Don't think that I want to help you or anything! I just want you to stop stalking me!"
    player "Thanks for the help anyway!"
    player "AND I ALREADY TOLD YOU THAT I'M NOT STALKING YOU."
    digl "Whatever. Get going."
    digl "{size=-5}Good luck.{/size}"
    #fade la pokesserie
    "Wow, the bakery sure smells nice... Working here would probably make me smell nice too!"
    unknown "..." #this is riley
    "Whoa... I wonder who that is..."
    "I've never seen this person at La Pokesserie before..."
    "...Oh no! What if La Pokeserie just hired someone new! Did I just miss out on a job opportunity?!"
    unknown "May I help you?"
    player "Oh, uh, yes! I was wondering..."
    player "Are you a new employee here?"
    unknown "No, I'm not. I'm actually the manager here."
    player "!"
    player "But I've never seen you here before!?"
    unknown "Yes, well... I have to fill the gap at the register now that my only employee left--"
    player "DOES THAT MEAN YOU'RE HIRING!?"
    unknown "Are you looking for a job?"
    player "YES! PLEASE HIRE ME!"
    unknown "Alright, as long as you work!"
    player "..."
    player "No interview?"
    unknown "I can't really be picky at this point..."
    "I gasp and break into a huge smile."
    player "Thank you for hiring me! You won't regret it!"
    unknown "Welcome to La Pokesserie."
    trap "My name is Riley."
    player "When do I start!?"
    trap "Tomorrow."
    trap "Make sure to be on time!"
    player "Oh boy, I can't wait to start earning money!"
    "Now... It begins..."
    "Soon it will be in my hands..."
    "{size=+5}{i}THE SUPER SPECIAL LIMITED EDITION {color=#ffd700}GOLD{/color} VERSION OF{/i} POKECROSSING: HAPPY BALL DESIGNER{i} SIGNED BY PIKABELLE CHUTENDO HERSELF FEATURING NEVER-BEFORE-SEEN EXTRA MATERIAL{/i}{/size} is mine!"
    $ has_job = True
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
