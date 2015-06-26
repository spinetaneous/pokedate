# This is the main program. This can be changed quite a bit to
# customize it for your program... But remember what you do, so you
# can integrate with a new version of DSE when it comes out.

# Set up a default schedule.
init python:
    register_stat("Money", "money", 00, 1000)

    dp_period("Morning", "morning_act")
    dp_choice("Attend Class!!", "class") #YOU HAVE TO GO BECAUSE YOU ARE A GOOD STUDENT OKAY
    
    dp_period("Afternoon", "afternoon_act")
    dp_choice("Go to Mall", "mall")
    dp_choice("Skip Work", "skip_work") #don't have to go to work tho u lazy butt

    dp_period("Evening", "evening_act")
    dp_choice("Go to Park", "park")
    dp_choice("Go Home", "home")
    
    
# This is the entry point into the game.
label start:
    $ day = 2 #after intro, it will be a Tuesday
    $ money = 0
    
    #Affection points.
    $ pika_pts = 10
    $ char_pts = 0
    
    #Pokedex variables.
    $ pika_dex = False
    $ char_dex = False
    $ jynx_dex = False
    $ digl_dex = False
    $ char_dex = False
    $ dad_dex = False
    $ ditt_dex = False
    $ bulb_dex = False
    
    #other variables
    $ digl_know = False
    
    # Show a default background.
    scene black
    
    # The script here is run before any event.

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
    
    # We jump to breakfast. Remember to fade!
    jump breakfast

# This is the label that is jumped to at the start of a day.
label day:
    #Initialize default values for variables to be used in the game.
    # Increment the day it is.
    $ day += 1

    # We may also want to compute the name for the day here, but
    # right now we don't bother.
    
    python:
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

    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available.

    $ morning_act = "class"
    $ afternoon_act = None
    $ evening_act = None
    $ narrator("What should I do today?", interact=False)
    
    # Now, we call the day planner, which may set the act variables
    # to new values. We call it with a list of periods that we want
    # to compute the values for.
    call screen day_planner(["Morning", "Afternoon", "Evening"])

    
    # We process each of the three periods of the day, in turn.
label morning:

    # Tell the user what period it is.
    centered "Morning"

    # Set these variables to appropriate values, so they can be
    # picked up by the expression in the various events defined below. 
    $ period = "morning"
    $ act = morning_act
    
    # Execute the events for the morning.
    call events_run_period

    # That's it for the morning, so we fall through to the
    # afternoon.

label afternoon:

    # It's possible that we will be skipping the afternoon, if one
    # of the events in the morning jumped to skip_next_period. If
    # so, we should skip the afternoon.
    if check_skip_period():
        jump evening

    # The rest of this is the same as for the morning.

    centered "Afternoon"

    $ period = "afternoon"
    $ act = afternoon_act

    call events_run_period


label evening:
    
    # The evening is the same as the afternoon.
    if check_skip_period():
        jump night

    centered "Evening"

    $ period = "evening"
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

