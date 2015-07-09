# This is the main program. This can be changed quite a bit to
# customize it for your program... But remember what you do, so you
# can integrate with a new version of DSE when it comes out.

# Set up a default schedule.
init python:
    #inventory testing
    inventory = Inventory(00)
    
    register_stat("Money", "current_money", 00, 1000) #money is incremented by 30 each time player goes to the mall aka job

    # dp_period() and dp_choice() are only necessary if the day planner will be used
    dp_period("Morning", "morning_act")
    dp_choice("Attend Class!!", "class") #YOU HAVE TO GO BECAUSE YOU ARE A GOOD STUDENT OKAY
    
    dp_period("Afternoon", "afternoon_act")
    dp_choice("Go to Mall", "mall")
    dp_choice("Skip Work", "skip_work", show= "not has_job")
    
    dp_period("Evening", "evening_act")
    dp_choice("Go to Park", "park")
    dp_choice("Go Home", "home")
    
    
# This is the entry point into the game.
label start:
    python:
        day = 2 #after intro, it will be a Tuesday
    
    #Affection points.
        pika_pts = 10
        char_pts = 0
        ditt_pts = 0
        
    #Pokedex variables.
        dad_dex = True
        pika_dex = True
        char_dex = False
        jynx_dex = False
        digl_dex = False
        char_dex = False
        ditt_dex = False
        bulb_dex = False
    
    # Show a default background.
    scene black
    
    # other variables
    $ has_job = False #true after get_hired runs
    $ skipped_work = 0
    $ grabbed_tail = False #true if you decide to light something on fire with charmeleon's tail
    #if true, then player is surprised to see charmeleon at school
    #if false, then player is not surprised bc they already know that they attend the same school
    
    "Hello, and welcome to PokeDate!"
    
    "If you've ever looked a Pokemon and thought, \"Wow, I would totally date that Pokemon!\"
     then this is the dating sim for you!"
    "We are dedicated to provide for you an unforgettable experience."
    "To get things started, we would like to know a few things about you."
    "First of all, what's your name?"
    
    #get player name
    python:
        name = renpy.input("Enter your name: ", default= "Tyrene", exclude=".0123456789", length=20)
        
    player "My name is [name]."
    
    #get player pronouns
    "Are you a boy, a girl, or something else?"
    menu:
        "Boy":
            $ pronoun1 = "him"
            $ pronoun2 = "he"
            $ pos_pronoun = "his"
            $ gender = "boy"
            player "I am a boy."
        "Girl":
            $ pronoun1 = "her"
            $ pronoun2 = "she"
            $ pos_pronoun = "her"
            $ gender = "girl"
            player "I am a girl."
        "Other":
            $ pronoun1 = "them"
            $ pronoun2 = "they"
            $ pos_pronoun = "their"
            $ gender = "person"
            player "I don't fit into gender binaries."
            
    "..."
    "Thank you for providing this information!"
    "Without further ado, let's get started on your romantic adventure! :-)"
    
    #jump park_day1 #for testing purposes
    
    # fade home
    jump breakfast

# This is the label that is jumped to at the start of a day.
label day:
    $ current_money = inventory.money
    # By default, current_money will be updated at the start of every day (i.e. at the statement "It's ____day!")
    # if inventory.money is changed multiple times during a day (without going back to dayplanner)
    # then current_money = inventory.money must be stated to update the displayed value
    # so you don't accidentally have $10, buy something worth $7, and then still have current_money = 10
    # although if day planner is discarded, then money will be displayed in an inventory screen instead of as a stat
    
    python:
        day += 1
    
        if day % 7 == 1:
            today = "Sunday"
        elif day % 7 == 2:
            today = "Monday"
        elif day % 7 == 3:
            today = "Tuesday"
        elif day % 7 == 4:
            today = "Wednesday"
        elif day % 7 == 5:
            today = "Thursday"
        elif day % 7 == 6:
            today = "Friday"
        elif day % 7 == 0:
            today = "Saturday"
        else:
            today = "...I have no idea. This isn't supposed to happen, and if it does, tell the developers."
            
    "Today is [today]."

    $ morning_act = "class" #player always goes to class
    
    if day <= 3:
        $ afternoon_act = "mall" #player HAS to go to the mall and get a job.
    else:
        $ afternoon_act = None
    $ afternoon_act = None
    $ afternoon_act = None
    $ evening_act = None
    
    # $ narrator("What should I do today?", interact=False)
    # call screen day_planner(["Morning", "Afternoon", "Evening"])
    
label morning:
    centered "Morning"
    $ period = "morning"
    $ act = morning_act
    call events_run_period

# player decides where to eat lunch at
# 1-A is an underclassman class and player can talk with ditto and diglett
# 2-B is player's own class where she can talk with pikachu
# 3-C is an upperclassman class and player can talk with jynx and charmeleon
label lunch:
    if check_skip_period():
        jump afternoon
        
    centered "Lunch"
    
    $ period = "lunch"
    
    "It's lunch time!"
    "Where should I go during lunch today?"
    menu:
        "Class 1-A":
            $ lunch_act = "lunch1"
        "Class 2-B":
            $ lunch_act = "lunch2"
        "Class 3-C":
            $ lunch_act = "lunch3"
    $ act = lunch_act
    call events_run_period

# player decides whether to go to work or not
label afternoon:

    # It's possible that we will be skipping the afternoon, if one
    # of the events in the morning jumped to skip_next_period. If
    # so, we should skip the afternoon.
    if check_skip_period():
        jump mall

    # The rest of this is the same as for the morning.

    centered "Afternoon"
    
    $ period = "afternoon"
    
    "Before I know it, school's out!"
    if has_job:
        "Should I go to work?"
        menu:   
            "Time to earn some cash!":
                $ afternoon_act = "work"
            "You know, what? Screw work!":
                $ afternoon_act = "skip_work"
            # there will be other stores available here, but unless a certain
            # character for that store has been met, an uninteresting event will occur
    else:
        "Time to job hunt!"
        $ afternoon_act = "job_hunt"
    $ act = afternoon_act
    call events_run_period

# if player went to work, then now she can hang around the mall afterwards
label mall:
    if check_skip_period() or afternoon_act == "skip_work":
        jump evening
    
    centered "Mall"
    
    $ period = "mall"
    
    if afternoon_act != "job_hunt":
        "Nothing like a day of hard work!"
    else:
        "Still at the mall..."
    "Where should I hang out now?"
    menu:
        "Salon":
            $ mall_act = "salon"
        #other choices later... like perhaps you can go home early and hang out with pikachu instead (^:
    $ act = mall_act
    call events_run_period

# player decides whether to go to the park or to go/stay home
label evening:
    
    # The evening is the same as the afternoon.
    if check_skip_period():
        jump night

    centered "Evening"

    $ period = "evening"
    
    "Wow, the sun is starting to set."
    "What should I do?"
    menu:
        "Go to Park":
            $ evening_act = "park"
        "Stay Home" if afternoon_act == "skip_work":
            $ evening_act = "home"
        "Go Home" if afternoon_act != "skip_work":
            $ evening_act = "home"
    $ act = evening_act
    
    call events_run_period


label night:

    # This is now the end of the day, and not a period in which
    # events can be run. We put some boilerplate end-of-day text
    # in here.

    centered "Night"

    "It's getting late, so I decide to go to sleep."

    # We call events_end_day to let it know that the day is done.
    call events_end_day

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day


# This is a callback that is called by the day planner. 
label dp_callback:

    # Add in a line of dialogue asking the question that's on
    # everybody's mind.
    $ narrator("What should I do today?", interact=False)
    
    return
