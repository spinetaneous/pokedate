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
#   mom would have wanted to help someone different and in need
#   pikachu loves player because player fought off his childhood bullies bc she genki af
#   with enough ditt_pts, you call him dumb names like fluffy egg

#   INCORPORATE GARY GARY (OAK) KUN!!!
#   also incorporate okie doki doki ddeokbokki
#   remember to introduce pokedex properly
#   events based on number of affection pts need a backup event (since the only stats that will trigger anything are affection pts)
#   secret bishounen unlockable mode released after beating the game (everyone is human lel)
#   human silhouette in pokedex

#FAVORITE ITEMS:
#pikachu: lemonade and lumiose galette
#charm: berry juice and lava cookie
#diglett: casteliacone and moomoo milk
#ditto: soda pop and shalour sable (but not really bc AHEM read below)
#fav = +=5 pts
#meh = +=3 pts
#ugh = -=3 pts
#EXCEPT DITTO!! everything is +=3 bc he doesn't actually have a fav

#UGH ITEMS:
#pikachu: water, lava cookie, shalour sable
#charm: water, casteliacone, lumiose galette
#diglett: soda pop, shalour sable
#ditto: nothin'

#FUTURE EVENTS:
#   charmeleon fucking dies at the beach
#       happens at the beach event on the first saturday
#       will only happen if you and char rly don't like each other lol
#   camping adventure with everyone but u get lost with charmeleon and he makes a lil fire for u (cuz he's made of fire)
#       but only if he doesn't die lmao
#   ditto gets kidnapped and u rescue him
#   PIKACHU EARNS PERFECT ATTENDANCE AWARD AND U DON'T *RIFT CREATED* but pikachu has never taken it srsly so u are offended
#       THEN HE GIVES U THE MEDAL wow pika confirmed han yi an
#   the "I never needed you" ending for not choosing pikachu (worst ending)
#   fight fight fight 4 ur luv
#############################################################

# Some characters that are used in events in the game.
init:
    define narrator = Character(' ')
    define unknown = Character('??????')

    define t = Character('Teacher')
        #stern but fair
    define player = Character('[name]', color="#0d4b72")
        #little common sense
        #LOVES POKECROSSING
        #one hell of a dancer. not kidding. will win at every dance battle
        #yells a lot. mostly out of excitement
    define dad = Character('Dad', color="#e74c14")
        #makes dad jokes
        #is very dad
        #typical dad
        #mom is feebas. she died.
    define pdex = Character('Pokedex')
    define trap = Character('Riley', color="#a3daf6") #works at la pokesserie
    define popo = Character('Police')
    define gscp = Character('Gamemon Store Clerk Person') #works at gamemon. elekid. holds game for u for 30 days cuz he kno that feel bro

    #pokemon (besides dad)
    define pbc = Character('Pikabelle Chutendo', color="#ffd700")
    define jynx = Character('Jynx', color="#70018b") #works at salon
        #info-chan
        #thinks she's popular
        #genki girl. all up in ur face. nice once u get used to her
    define bulb = Character('Bulbasaur', color="#008080") #works at florist/is the florist
        #normal guy. boo
    define elek = Character('Elekid', color="#f3f15d") #works at gamemon. gscp
        #knows that gamer feel
        #very passionate about games
        #always playing on his Chutendo TS behind the counter
    
    #pokemon that you can date
    define digl = Character('Diglett', color="#ab4221") #works at gym
        #tsundere. works at gym. is secretly hella ripped
        #insecure about his looks
    define pika = Character('Pikachu', color="#ffd700") #at school... maybe one day u can go to house????
        #the childhood friend. sweet and nice
        #neglected by mom aka Pikabelle Chutendo who works too much to pay for dad's medical bills
        #doesn't like mom
        #likes player. obviously
    define char = Character('Charmeleon', color="#ff760d") #at park all the time
        #the aristocrat. suave and lame
        #is the bastard child of a rich man
        #lives with his mom who has been kicked outta the rich house and is now an alcoholic
        #goes to park to escape home life but doesn't run away cuz deep down he loves his mom
        #gets embarrassed easily around the person he likes
        #doesn't understand teen slang
        #koreaboo
    define ditt = Character('Ditto', color="#c9a0dc") #works at sleezy store 
        #silly and weird
        #wants to fit in bc he's a scared and tiny freshman who is also a blob with no form
        #also the LAMEST
        #weeaboo
    
    #fake dittos
    define dpika = Character('Pikachu', color="#c9a0dc")

init:
    # First up, we define some simple events for the various actions, that
    # are run only if no higher-priority event is about to occur.
    python:
        #default events for when nothing interesting is happening
        event("class1", "act == 'class'", event.solo(), event.choose_one("class"), priority=1000)
        event("class2", "act == 'class'", event.solo(), event.choose_one("class"), priority=1000)
        event("work", "act == 'mall'", event.solo(), event.depends("get_hired"), priority=1000)
        event("skip_work1", "act == 'skip_work'", event.solo(), priority=1000)
        event("eat_lunch1", "act == 'lunch1'", event.solo(), priority=1000)
        event("eat_lunch2", "act == 'lunch2'", event.solo(), priority=1000)
        event("eat_lunch3", "act == 'lunch3'", event.solo(), priority=1000)
        event("salon", "act == 'salon'", event.solo(), priority=1000)
        
        #the process of finding a job. can take place over many days. stops once player gets hired
        event("where_job_hunt", "act == 'job_hunt' and not has_job", priority=1)
        
        #the first time player goes to salon after knowing jynx, she gets a haircut
        event("get_haircut", "act == 'salon' and jynx_dex", event.once(), priority=999)
        
        #player meets ditto in courtyard
        event("meet_ditto", "act == 'class'", event.once(), priority=10)
        
        #the player forgets her lunch one time. event differs depending on where player decides to go during lunch
        event("forgot_lunch1", "act == 'lunch1' and digl_dex and not forgotlunch2 and not forgotlunch3", event.once(), priority=998)
        event("forgot_lunch2", "act == 'lunch2' and not forgotlunch1 and not forgotlunch3", event.once(), priority=998)
        event("forgot_lunch3", "act == 'lunch3' and jynx_dex and not forgotlunch1 and not forgotlunch2", event.once(), priority=998)
        
    
#Below are the boring events that happen when there are no higher priority events.

label class1:
    "I run to school and make it well before the bell rings."
    "Although {i}inside{/i} of the school, I speed-walk."
    "One is not supposed to run in the hallways!"
    "..."
    "Nothing interesting happened during class."
    return
    
label class2:
    "I run to school and make it well before the bell rings."
    "Nothing worth mentioning happens."
    return

label work: #this only happens after you get hired
    #perhaps add variable 'salary' and use that instead of numbers
    #and add events that notify the player that their pay is being reduced
    "I head to my job at the mall and strengthen my resolve as I sell pokepuffs."
    "I've got to work hard if I want to get {i}PokeCrossing: Happy Ball Designer!{/i}"
    python:
        if skipped_work < 3:
            inventory.earn(35)
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
    "I go to the salon."
    if jynx_dex:
        "But Jynx is no where to be found..."
        "Maybe she as a day off? Maybe I just suck at finding people?"
    "..."
    "Ooo, look at all the fancy hair products!"
    "After I finish carefully examining the bottles, I leave the salon."
    return
    
label park:
    "I spend the evening relaxing at the park."
    "Since I don't see any of my friends here today, I play with the local kid pokemon instead."
    "We play tag at the playground while screaming and yelling a lot."
    "I make sure to laugh maniacally every time I tag someone."
    "After I'm tired, I decide to go back home."
    return

label home:
    "At home, I work on my town in {i}PokeCrossing: New Ball{/i}."
    "After all, I have to fulfill my duty as mayor! Can't let my villagers down!"
    #perhaps at a certain number of char_pts, player can play with him? hehe
    return

#Below are the events actually matter.

label where_job_hunt:
    $ tried_job_hunt += 1
    #fade mall
    "Where should I try to get hired at?"
    menu:
        "Gamemon":
            if not tried_gamemon:
                jump job_hunt_gamemon
            else:
                "I already tried Gamemon."
                jump where_job_hunt
        "Salon":
            if not tried_salon:
                jump job_hunt_salon
            else:
                "I already tried the salon."
                jump where_job_hunt
        "Gym":
            if not tried_gym:
                jump job_hunt_gym
            else:
                "I already tried the gym."
                jump where_job_hunt
        "Florist":
            if not tried_florist:
                jump job_hunt_florist
            else:
                "I already tried the florist."
                jump where_job_hunt
        "Bakery" if digl_dex and jynx_dex:
            jump job_hunt_la_pokesserie
        "I've had enough!" if tried_gamemon or tried_salon or tried_gym or tried_florist:
            if tried_job_hunt < 4:
                "This is harder than I thought..."
                "Maybe I should just try some other day."
                jump evening
            else:
                "Sigh... I still can't find a job..."
                "But I need that game..."
                "No choice but to keep going!"
                jump where_job_hunt
            return

label job_hunt_gamemon:
    #fade gamemon
    "I walk into Gamemon."
    player "Excuse me! I'd like a job!"
    "No one answers."
    player "{size=+5}Hello! I would like to get a job here!{/size}" with vpunch
    "People start looking at me."
    "...But no one is hiring me!"
    "I wonder if I'm being ignored... Maybe I should try somewhere else..."
    "..."
    "...!"
    "What's this...?"
    "A flyer?"
    "\"THE GYM IS CURRENTLY HIRING!!! COME BY FOR MONEY {i}AND{/i} MUSCLES!!!\""
    "Hm... Interesting..."
    $ tried_gamemon = True
    jump where_job_hunt
    return

label job_hunt_salon:
    #fade salon
    "I walk into the salon."
    "There's a long line outside, but since I'm not here to get a haircut, I just walk on in."
    player "Excuse me! I'd like a job!"
    if jynx_dex:
        jynx "YOU CAME!!!" with vpunch
        jynx "Come here, come here, sit down!!"
        player "What?"
        player "No, I'm not--"
        jynx "Honey, don't worry. I'm a professional. Making people pretty is my job."
        player "Speaking of jobs, I'm here for one."
        jynx "..."
        jynx "You're here for what?"
        player "A job!"
        player "I need to earn money and a job is the only way!"
        jynx "Oh, sweetie..."
        jynx "Sorry, but we're not hiring."
        if go_salon_advice:
            player "Wait, but someone told me that you were!?"
            jynx "That pokemon must have heard wrong, then."
            jynx "Sorry, sweetie."
        player "Aw, man..."
        player "Do you know any place that's currently hiring?"
        jynx "Hm..."
        #if player knows diglett, then jynx says go to the bakery
        #if not, then jynx says to go to the gym
        #this to help the player be introduced to both these characters
        if digl_dex:
            jynx "I think the bakery needs employees."
            jynx "The cutie working there is all alone... Such a shame!"
            player "!"
            "So the bakery is looking for people..."
        else:
            jynx "Sorry sweetie, I'm not too sure..."
            jynx "Maybe try the gym?"
            player "!"
            "So the gym is looking for people...?"
            $ go_gym_advice = True
        player "Thanks, Jynx!"
        jynx "No problem, honey."
        jynx "Just remember to come back soon!"
    else:
        unknown "DANG, GIRL!!" with vpunch
        unknown "YOU NEED A LIL FIXER-UPPER!!"
        player "H-Huh...?"
        "Someone is yelling at me while she's cutting hair."
        "Who is this person? What does she mean by \"fixer-upper\"?"
        if gender != "girl":
            "And I'm not a girl..."
        unknown "Honey, I'm talking about your hair!"
        player "My hair?"
        "She shoves a slip of paper into my hands."
        unknown "That there's a coupon for a stylin' by Yours Truly!"
        unknown "For the next time you come here, of course."
        player "Eh?"
        unknown "Usually I'd take care of you right now, but I've got a lot of people waiting."
        unknown "Come by some time, and I'll fix you up all nice and pretty!"
        player "Wait, that's not what I came here for--"
        unknown "Sh, sh, sh! I have a lot of customers today!" with vpunch
        unknown "If you want to talk, just hit me up at school!"
        player "School?"
        unknown "You're wearing the PokeCreek uniform, right?"
        unknown "I go there too. Haven't you noticed the girl who always steals all the attention?"
        jynx "The name's Jynx!"
        $ jynx_dex = True
        pdex "Jynx has been added to your Pokedex."
        player "Um... I--"
        jynx "Sorry sweetie, but I gotta focus here! Get in line if you're so eager for a haircut!" with vpunch
        player "W-Wait!"
        player "Are you hiring!?"
        jynx "Nope! Sorry!"
        if go_salon_advice:
            player "But someone told me that you were!?"
            jynx "That pokemon must've heard wrong, then!"
        player "Oh... {w}Well, do you know any place that {i}is{/i} looking for employees?"
        jynx "Hm..."
        #if player knows diglett, then jynx says go to the bakery
        #if not, then jynx says to go to the gym
        #this to help the player be introduced to both these characters
        if digl_dex:
            jynx "I think the bakery needs employees."
            jynx "The cutie working there is all alone... Such a shame!"
            player "!"
            "So the bakery is looking for people..."
        else:
            jynx "Sorry sweetie, I'm not too sure..."
            jynx "Maybe try the gym?"
            player "!"
            "So the gym is looking for people...?"
            $ go_gym_advice = True
        "I don't think there's any use staying here."
        "With the coupon in my hands, I leave the salon."
    $ tried_salon = True
    jump where_job_hunt
    return
    
label job_hunt_gym:
    #fade gym
    "Now I'm at the gym. Wow, this place smells of sweat!"
    "But it also smells like potential cash to be made... Heh."
    if digl_dex:
        unknown "It's not enough that you're rude to me, so you follow me to my workplace too!?" with vpunch
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
        digl "Then go get hired somewhere else! The gym isn't hiring right now!" with vpunch
        if tried_gamemon:
            player "What!? But I saw a flyer that said you were hiring!"
            digl "Argh, I already told all the stores to take those down..."
            digl "That flyer is old. We already have the employees we need."
        player "Really!? Dang... That's too bad..."
        player "I guess I need to try somewhere else then."
        digl "..."
        #if player knows jynx, then diglett says go to the bakery
        #if not, then diglett says to go to the salon
        #this is the help player be introduced to both these characters
        if jynx_dex:
            digl "{size=-5}You could try the bakery... \"La Pokesserie\" I think it was called...{/size}"
        else:
            digl "{size=-5}You could try the salon... They might be hiring...{/size}"
            $ go_salon_advice = True
        player "Really? Thanks!"
        digl "Y-You heard that!?"
        digl "Don't think that I want to help you or anything! I just want you to stop stalking me!"
        player "Thanks for the help anyway!"
        player "AND I ALREADY TOLD YOU THAT I'M NOT STALKING YOU."
        digl "Whatever. Get going."
        digl "{size=-5}Good luck.{/size}"
    else:
        "I find the nearest pokemon I can and talk to him."
        player "Excuse me, I would like a job here."
        unknown "Huh?"
        unknown "Who are you?"
        player "I'm [name]! And I'm currently looking for a job!"
        digl "Oh. I'm Diglett."
        $ digl_dex = True
        pdex "Diglett has been added to your Pokedex."
        digl "Go get hired somewhere else. The gym isn't hiring right now."
        if tried_gamemon:
            player "What!? But I saw a flyer that said you were hiring!"
            digl "Argh, I already told all the stores to take those down..."
            digl "That flyer is old. We already have the employees we need."
        
        player "Really!? Dang... That's too bad..."
        player "I guess I need to try somewhere else then."
        digl "..."
        #if player knows jynx, then diglett says go to the bakery
        #if not, then diglett says to go to the salon
        #this is the help player be introduced to both these characters
        if jynx_dex:
            digl "{size=-5}You could try the bakery... \"La Pokesserie\" I think it was called...{/size}"
        else:
            digl "{size=-5}You could try the salon... They might be hiring...{/size}"
            $ go_salon_advice = True
        player "Really? Thanks!"
        digl "Y-You heard that!?"
        digl "Don't think that I want to help you or anything!"
        player "Thanks for the help anyway!"
        digl "Whatever. Get going."
        digl "{size=-5}Good luck.{/size}"
    $ tried_gym = True
    jump where_job_hunt
    return
    
label job_hunt_florist:
    #fade florist
    if bulb_dex:
        "Maybe Bulbasaur is looking for employees?"
        player "Hey Bulbasaur, remember me?"
        bulb "Oh yeah, didn't you come here with your boyfriend or something?"
        player "Haha, we're not dating."
        bulb "Is that so? I see."
    else:
        "I walk into the florist."
        "The store, not the person running it. I wonder why the word 'florist' is used for both?"
        "As soon as I walk in, someone greets me."
        "According to his name tag, his name is Bulbasaur."
        $ bulb_dex = True
        pdex "Bulbasaur has been added to your Pokedex."
    bulb "May I help you? Are you looking for anything in particular?"
    player "In fact, I am!"
    player "I'm looking for a job!"
    bulb "Oh, I see."
    bulb "Well, you're in luck! I'm currently hiring."
    player "Really? That's great! When do I start!?"
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
        "They're really pretty?":
            bulb "Well, I can't deny that..."
        "What are flowers?":
            bulb "..."
            bulb "Um..."
    bulb "I see... Finally, are you experienced in working a cash register?"
    menu:
        "The click-clack cash thingy?":
            bulb "Um..."
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
    player "It's ok! I won't let this failure get me down!"
    player "I WILL CONQUER THE JOB MARKET!"
    player "Do you know any store that's hiring?"
    bulb "I don't. Ask other people."
    bulb "They might be more helpful. {w}Might."
    player "Oh, okay."
    player "Seeya!"
    bulb "Bye."
    $ tried_florist = True
    jump where_job_hunt
    return

label job_hunt_la_pokesserie:
    #fade la pokesserie
    "Wow, the bakery sure smells nice... Working here would probably make me smell nice too!"
    unknown "..." #this is riley
    "Whoa... I wonder who that is..."
    "I've never seen this person at La Pokesserie before..."
    "...Oh no! What if La Pokeserie just hired someone new! Did I just miss out on a job opportunity!?"
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
    "{size=+5}{i}THE SUPER SPECIAL LIMITED EDITION {color=#ffd700}GOLD{/color} VERSION OF{/i} POKECROSSING: HAPPY BALL DESIGNER{i} SIGNED BY PIKABELLE CHUTENDO HERSELF FEATURING NEVER-BEFORE-SEEN EXTRA MATERIAL{/i}{/size}... {w}is mine!"
    $ has_job = True
    return
    
label meet_ditto: #the first time player goes to class, she notices ditto
    if char_dex and not grabbed_tail:
        "I stayed up late last night with Charmeleon, so it's difficult to wake up in the morning."
        "But I do it."
        "I wipe the sleep from my eyes because I am {i}determined not to be late!{/i}"
    else:
        "What a good night's sleep! I feel so refreshed and awake."
        "I'm totally ready to get a job after school!"
        "Wait for me, {i}PokeCrossing: Happy Ball Designer{/i}..."
    #fade school
    "Another day of getting to school on time!"
    "Not surprising though... After all, I've had perfect attendance for my entire school career!"
    "And I have never, ever been absent or late."
    "Ever."
    "So now I'm here at school early!"
    "But now I have some time to kill..."
    "Maybe I should just walk around campus for a little while."
    #fade courtyard
    "..."
    "...!"
    "Hey, is that Pikachu?"
    "I wonder why he's at school so early. Maybe he likes to be punctual just like me."
    player "Hey, Pikachu! What are you doing here?"
    dpika "Hey, baby. What's up?"
    player "..."
    dpika "Why the long face, shawty?"
    player "......"
    dpika "Come on cupcake, lemme see you smile."
    player "Pikachu..."
    "Pikachu is being really strange. What should I do?"
    menu:
        "Ask him why he's being like this.":
            player "Why are you acting all weirdly...?"
            dpika "Am I acting weird, or is {i}you{/i} acting weird?"
            dpika "Oh wait, I know why you ain't got no chill."
            dpika "It's cuz you just can't control yourself around me, correct?"
            dpika "Ain't that right, sweetcheeks?"
            player "!!!"
            player "Don't call me that. You're being gross."
        "Go along with it.":
            $ ditt_pts += 5
            player "Bruh, you askin' me to smile, but why ain't you smilin'?"
            dpika "Damn, you hella sharp fo'sho."
            player "Yeah, as sharp as my di--"
    pika "[name]!!" #two pikas on screen with SHAKY SCREEN 4 footsteps
    player "P...Pikachu...?"
    player "I..."
    player "But aren't you..."
    player "Are there two of..."
    player "...What?"
    "Wait, I think I figured it all out! I'm a genius!"
    player "Pikachu, do you... {i}have an {b}evil twin!?{/b}{/i}"
    pika "???"
    pika "No, I--"
    dpika "Of course! I come from {b}another dimension{/b}!"
    dpika "Nice to meet you... Or as they say on my home planet..."
    dpika "YO - RO - SHI - KU - O - NI - GA - I - SHI - MA - SU"
    player "O-Oh? Then, uh..."
    player "Yoro..."
    player "Yoroshi...ganimasou to you too! Yoroshiganimasou!"
    pika "[name]..."
    pika "I don't have a twin... I have no idea who this is..."
    pika "Don't you remember!? I'm an only child!"
    pika "{i}We're childhood friends!{/i}"
    player "Oh yeah..."
    player "Then wait, who's this!!??"
    dpika "Haha [name], you're silly."
    dpika "I like you!"
    pika "!"
    pika "[name], can you come here for a sec..."
    "Pikachu pulls me aside and starts whispering in my ear."
    pika "{size=-5}This guy is giving me the creeps...{/size}"
    pika "{size=-5}He's impersonating me and playing this weird prank on you...{/size}"
    pika "{size=-5}We should just leave him right now.{/size}"
    "I turn around to look at Mr. Pikachu Imposter."
    "...!"
    player "Where'd he go?"
    unknown "Down here!"
    pika "Huh?"
    "Pikachu and I look down at the direction of the voice."
    unknown "Hey guuuuuuuuuuys!"
    ditt "It's me, Ditto! ♥"
    $ ditt_dex = True
    pdex "Ditto has been added to your Pokedex."
    "Pikachu and I glance at each other."
    pika "{size=-5}This guy's weird...{/size}"
    player "You're...You're a blob!"
    ditt "Hey! You're a {i}human{/i}!"
    player "{i}That is a sensitive subject!{/i}"
    "DING -- DONG -- DING -- DONG --"
    pika "Oh hey would you look at that it's time to go to class let's go [name]--"
    "Pikachu grabs me by the arm and starts to lead me away."
    ditt "Hey, Pikachu-senpai, [name]-senpai!"
    ditt "I'm in class 1-A! Come visit me!"
    ditt "I'll be waiting, babylips~♥"
    pika "Haha that is very funny now come on [name] we'll be late for class--"
    "Before I can say anything, Pikachu runs off while grabbing me by the wrist."
    "We make it to class before the second bell rings."
    "..."
    "I wonder what a senpai is?"
    return
    
label get_haircut: #the first time player goes to salon after getting a job, she gets a haircut by jynx LOL surprise
    if tried_salon:
        "I walk into the salon where Jynx works."
    else:
        "So this is the salon that Jynx works at..."
        "It looks like a popular salon. There's even people lining out the door."
    unknown "Hey, [name]! You came to visit! Glad to see you!"
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
    "I look up at the mirror."
    "My hair is so much shorter than it used to be..."
    "I'm not sure if it looks good or not... I've never had a good sense of style."
    player "Thanks, Jynx. Well, I'd best be going! See you tomorrow!"
    jynx "No problem, sweetie."
    "And with that, I get out of that salon."
    $ haircut = True
    return
    
label forgot_lunch1:
    $ forgotlunch1 = True
    "Time to spend lunch with the little ones today!"
    "I head over to class 1-A, the underclassmen's classroom."
    "There, I see Ditto and Diglett from the corner of my eye."
    "They notice me, and I wave. {w}They wave back."
    ditt "'Sup, [name]!?"
    ditt "What's crackalackin'!?"
    digl "Oh, [name]. It's you."
    player "I came to eat lunch with you guys!!"
    digl "Yeah, right. If that's the case, where's your lunch?"
    player "Haha, You're funny! My lunch is right here--"
    player "...!" with vpunch
    player "W-Where's my lunch!?"
    player "I can't believe it... {w}How could I have forgotten to bring my lunch, one of the most important meals of the day!?"
    ditt "I bet you just wanted to see me. Isn't that right, sugar muffin?"
    "Nevermind his question. Right now, there are bigger things to worry about!"
    "What should I do about lunch?"
    menu:
        "Buy your own lunch" if inventory.money >= 7:
            "Hmm... {w}Well, I didn't get a job for nothing!"
            player "I think I'll just go and buy my own lunch."
            player "I'll be back in a bit!"
            if ditt_pts >= 10 and ditt_pts > digl_pts:
                ditt "Hey, baby! No invite?"
                player "Huh?"
                "!" 
                "Ditto wants to come too!"
                "Should I let him tag along?"
                menu:
                    "Yes":
                        player "You can come along too, if you'd like."
                        player "After all, the more the merrier!"
                        ditt "Cool! Let's go!"
                        ditt "Seeya, Diglett!"
                        player "We'll be back soon!"
                        digl "...Like I care."
                        $ ditt_pts += 2
                        $ ditt_getlunch = True
                    "No":
                        player "Well, there's really no need, is there?"
                        player "Your \"senpai\" can buy [pos_pronoun] lunch just fine! {w}Just sit back and relax!"
                        ditt "Alrighty, baby doll."
                        ditt "But come back soon, dear. {w}Otherwise {i}{b}I'll miss you too much{/b}{/i}~~♥!"
                        digl "That's disgusting, Ditto."
                        ditt "Hehe!"
                        "Haha! {w}My underclassmen are so cute!"
            elif digl_pts >= 10 and digl_pts > ditt_pts:
                digl "...{w}I don't know how I feel about you going alone."
                digl "You might get lost or something. After all, you're not too bright."
                digl "It would probably be best if I went with you."
                digl "{size=-5}I can watch over you... in case something happens. {/size}"
                player "!"
                "What's this? {w}Diglett wants to tag along?"
                "Should I let Diglett come with me to get lunch?"
                menu:
                    "Yes":
                        player "That's fine with me!"
                        player "Let's go!"
                        ditt "Come back soon!! I'm going to be so {i}{b}lonely{/b}{/i}~~!"
                        digl "You're so weird, Ditto."
                        $ digl_pts += 2
                        $ digl_getlunch = True
                    "No":
                        player "It's okay, Diglett."
                        player "I'm actually stronger than I look, so you don't have to worry at all!"
                        digl "!"
                        digl "W-who said I was {i}worried{/i}?!" 
                        player "Oh, you weren't? {w}It seemed like it to me."
                        player "Sorry, haha! I interpreted you wrong."
                        digl "W-wait, that's not what I..."
                        player "Okay, I'll be back soon! Don't miss me too much!"
                        digl "..."
            else:
                ditt "Sure thing, hotcakes!"
                digl "As if I care."
            #fade to lunch
            "Wow! So this is the cafeteria."
            "I'm not too familiar with buying my own lunch. I always bring lunch from home."
            if ditt_getlunch: 
                player "Ditto, do you know what's good here?"
                ditt "Hmm..."
                ditt "It really depends on your preference, doll face."
                player "Okay, then what's {i}your{/i} favorite here?"
                ditt "Mmm...{w} I guess... {w}I would go with... {w}the ramen."
                player "..."
                player "Why do you sound so uncertain?"
                ditt "I don't know... I don't really have a favorite food."
                player "Oh, come on. {w}There's {i}nothing{/i} out there that you like?"
                ditt "Well, there's food that I {i}like{/i}, but I don't have a {i}favorite{/i} food." #uncomfortable face
                ditt "It's kind of weird."
                ditt "I don't have a favorite... {w}{i}anything{/i}, actually."
                ditt "..."
                ditt "Hey, what's with that face?"
                player "!"
                player "Oh... {w}It's just that I've never seen this side of you."
                player "You're usually so confident."
                player "So... {w}I'm just kind of surprised that you could be so hesitant."
                ditt "Yeah, well... {w}I guess not everyone is who you think they are."
                ditt "Isn't that right, honey bunny?"
                player "Haha, yeah!"
                player "Okay, Ditto! {w}I'm going to get in line now."
                $ ditt_pts += 5
            elif digl_getlunch:
                player "So Diglett, do you know what's good here?"
                digl "You've never eaten the cafeteria food before?"
                player "Nope! {w}I've always brought my dad's home-made lunch to school."
                digl "{size=-5}T-that's amazing...{/size}"
                digl "Um... {w}I recommend the curry."
                digl "And make sure to get some Moomoo Milk with that. The curry can get rather spicy sometimes, and milk has an enzyme that relieves the spiciness."
                player "...But why specifically {i}Moomoo Milk{/i}?"
                digl "Because it tastes the best!"
                player "Hmm? {w}You have a soft side for {i}Moomoo Milk{/i}?"
                digl "!"
                digl "What's wrong with Moomoo Milk?!"
                player "Nothing! It's just surprising to know that you have a soft side!"
                digl "S-Shut up!" #diglett blushhhh
                player "Okay, Diglett! {w}I'm going to get in line now."
                $ digl_pts += 5
            "I get in line."
            if ditt_getlunch: 
                "Shortly afterword, I receive my ramen and pay $7 for it."
                $ inventory.earn(-7)
                "I grab my food and return to Ditto."
                ditt "So, you still got the ramen?"
                player "Of course! {w}You suggested it, after all."
                ditt "...I see."
                player "Let's get back to class."
                ditt "Yeah, Diglett must be feeling so {i}{b}lonely{/b}{/i} without us by his side. ♥"
            elif digl_getlunch:
                "Shortly afterword, I receive my curry and Moomoo Milk. I pay $7 for it."
                $ inventory.earn(-7)
                "I grab my food and return to Diglett."
                player "Alright! Let's get back to class."
                digl "Yeah, that idiot, Ditto, must be up to no good right about now."
            else:
                "...{w}Where's the menu around here?"
                "..."
                "Oh! {w}There it is."
                "..."
                "I'll get the vegetable soup with fish."
                "It seems like the healthiest option here. I heard fish helps your brain!"
                "I receive my vegetable soup with fish and pay $7 for it."
                $ inventory.earn(-7)
                "Alright! Now I can head back to class 1-A."
            #fade to class
            if ditt_getlunch:
                player "We're baaack!"
                ditt "Did you miss us, Diglett? ♥"
                digl "What did you get, [name]?"
                player "Ramen!"
                digl "Hmph! Curry is better."
            elif digl_getlunch:
                player "We're baaack!"
                digl "You didn't get yourself into any trouble, did you Ditto?"
                ditt "Aww, you worried about me~~♥!"
                ditt "Don't worry! The only thing I've done since you two were gone was eat."
            else: 
                player "I'm baaack!"
                ditt "What did you get, buttercup?"
                player "Vegetable soup with fish!"
                digl "Hmph! Curry is better."
                $ ditt_pts += 5
                $ digl_pts += 5
            "I sit back down in my seat."
            "I spend my lunch talking to Ditto and Diglett."
            "We eat happily together."    
        "Make the underclassmen buy your lunch":
            player "Hey, wait a minute. {w}I'm an upperclassman."
            player "That means you should respect me. {w}And stuff."
            player "So... {w}Y'know... {w}Can you guys go buy me lunch?"
            digl "{i}Huh?{/i}"
            ditt "Oh, I didn't know such a hierarchy still existed in high school!"
            digl "Are you serious?"
            ditt "Well, if [pos_pronoun] highness says so!"
            ditt "Let's go, Diglett!"
            if digl_pts >= 5:
                digl "Okay, okay, I'm coming. Geez."
            else:
                digl "Ugh, fine. Whatever."
            digl "Are you going to give us the money to buy it?"
            digl "And by \"it,\" I mean {i}your{/i} lunch? {w}That {i}we{/i} are buying for {i}you{/i}?"
            player "...How much is lunch?"
            ditt "Hmm... {w}About $7? Our school lunches are pretty good, so they're kinda pricey."
            "Should I?"
            menu:
                "Yes" if inventory.money >= 7:
                    player "Okay. {w}I mean, after all, I would feel bad making you buy my lunch without paying for it."
                    player "Here."
                    "I hand them $7. {w}Lunch is an important meal, and this precious monetary sacrifice is necessary...!"
                    $ inventory.earn(-7)
                "No":
                    player "Um... {w}Uh..."
                    digl "Oh, come on. You're kidding me."
                    player "Well, I'm an upperclassman and--"
                    digl "Whatever. {w}Let's go, Ditto."
                    digl "We have to go get {i}[pos_pronoun] highness's{/i} meal, after all."
                    ditt "..."
                    ditt "Yeah."
                    $ digl_pts -= 2
                    $ ditt_pts -= 2
            "...{w}...{w}..."
            "*SLAM*" with vpunch
            ditt "We're back~"
            ditt "Did you miss us, your highness~?"
            player "Haha... {w}Don't call me that..."
            digl "..."
            ditt "Here's your lunch!"
            "Ditto sets lunch on my desk."
            if ditt_pts > digl_pts:
                "It's ramen."
            elif digl_pts > ditt_pts:
                "It's curry."
            else:
                "It's vegetable soup with fish."
            player "Thanks for getting me lunch!"
            digl "Whatever."
            ditt "Thanks for allowing me to experience the obselete subordination of an underclassman!"
            ditt "..."
            ditt "It was only a {i}little{/i} humiliating." #he is still smiling lel
            player "Oh... {w}Well, let's eat lunch now!"
            "We sit and eat lunch together, making small talk at the same time."
            $ digl_pts -= 3
            $ ditt_pts -= 3
        "Don't eat lunch":
            player "Sigh... I guess there's nothing I can do."
            player "My lunch is at home, and I don't want to spend money to buy lunch..."
            player "Today, I'll skip lunch."
            if ditt_pts >= 10 and digl_pts >= 10: 
                if ditt_pts > digl_pts:
                    ditt "Hey, that's a no-no!"
                    ditt "Lunch is very important. We'll share our lunches with you!"
                    ditt "Right, Diglett?"
                    digl "What???"
                    ditt "Ahem. {w}{i}Right, Diglett?{/i}"
                    digl "..."
                    digl "{size=-5}Well, I never said I didn't like [name] anyway...{/size}"
                    digl "I guess."
                    ditt "Hehe! Okay, let's all eat lunch together now!"
                elif digl_pts > ditt_pts:
                    digl "Hey, you can't do that...!"
                    digl "Lunch is important. You shouldn't skip it."
                    digl "Here, we'll share our lunches with you."
                    digl "Right, Ditto?"
                    ditt "Oh!"
                    ditt "Diglett, that's very smart of you!"
                    digl "Sit down, [name]. Let's eat lunch."
                    digl "..."
                    digl "{size=-5}Together.{/size}"
                "Ditto and Diglett share their lunches with me."
                "I'm so glad I have friends!"
                "We talk and eat happily together."
                $ digl_pts += 5
                $ ditt_pts += 5
            else:
                ditt "Oh, that's too bad!"
                digl "Yeah..."
                ditt "So, what now?"
                digl "Are you leaving?"
                "If I don't have my lunch, should I still stay here?"
                menu:
                    "Yes":
                        player "I'm going to stay."
                        player "Even though I don't have my lunch, I want to stay here with you guys!"
                        digl "!"
                        ditt "Okay, then let's all spend lunch together!"
                        ditt "Here [name], you can have some of my lunch!"
                        if digl_pts > 5:
                            digl "..."
                            digl "You can have some of mine, too..."
                        else:
                            digl "You can't have any of mine."
                        digl "Bring your own lunch next time."
                        "I spend lunch talking with Diglett and Ditto."
                        $ digl_pts += 5
                        $ ditt_pts += 5
                    "No":
                        player "I guess I should leave then...?"
                        ditt "Aw..."
                        ditt "I hope you come by soon!"
                        digl "Bring your lunch next time."
                        "I leave class 1-A and spend lunch sleeping at my desk."
                        "Gotta conserve energy!"
                        $ digl_pts += 1
                        $ ditt_pts += 1
    return
    
label forgot_lunch2:
    $ forgotlunch2 = True
    "I sit with Pikachu for lunch."
    "Time to eat!"
    "..."
    "...!" with vpunch
    pika "What's wrong, [name]?"
    player "I..."
    player "I forgot my lunch!" with vpunch
    pika "Oh! {w}Then do you want some of my lunch?"
    pika "I made it this morning, as usual."
    "He's offering me lunch. What do I do?"
    menu:
        "Accept the offer":
            "Pikachu's lunch looks really good... {w}Not to mention well-balanced and nutritious..."
            player "You really mean it, Pikachu?"
            pika "Haha, of course!"
            if pika_pts >= 20:
                pika "Here, say \"Ah~\"."
                "Pikachu feeds me a spoonful of his homemade lunch."
                pika "How is it?"
                player "...!"
            else:
                "I take a bite of Pikachu's food."
            player "Wow, it's really good!"
            player "I'm amazed that it's this good. {w}You've improved since the last time I've eaten your food."
            pika "Come to think of it, the last time I made food for you was during middle school, wasn't it?"
            player "Yeah, we haven't had any dinners together recently, huh?"
            pika "Being a high school student really keeps you busy..."
            pika "It's pretty chaotic sometimes."
            player "Oh hey, I haven't seen your dad in awhile. How's he doing?"
            pika "..."
            pika "Well..."
            pika "These days he isn't doing too well..."
            player "...? {w}What's wrong?"
            if pika_pts >= 30:
                pika "..."
                pika "He's in the hospital."
                player "!" with vpunch
                player "What happened!? Wasn't he perfectly healthy the last time I saw him!?" with vpunch
                pika "Well... {w}He was diagnosed with a terminal illness... {w}at the end of middle school."
                pika "I don't want to delve into details since we're still at school, but..."
                pika "It's starting to eat away at his brain."
                pika "Soon... {w}He won't be like he used to be."
                player "If the diagnosis was two years ago... {w}Why didn't you tell me?"
                pika "You're the only person I've told about my dad's situation."
                pika "I feel like I can tell you about anything, so... {w}I won't keep secrets anymore, okay?"
                pika "Don't be sad."
                pika "Please."
                player "I-I won't. Don't worry about me. {w}Worry about yourself."
                player "I'm here for your dad and you. Just call me any time, and I'll be there."
                pika "..."
                pika "Thanks, [name]."
                pika "That means a lot."
                $ know_pika_secret = True
                $ pika_pts += 5
            else:
                pika "..."
                pika "I'm sorry, [name]. {w}I just can't tell you yet."
                player "It's okay. {w}Just tell me whenever you're ready. I'll still be there."
                pika "It's still difficult to come to terms with his situation, but..."
                pika "I promise that I'll tell you one day."
                player "Alright, Pikachu. I don't know what's going on, but I hope you're okay."
                player "Wishing you the best of luck."
                $ pika_pts += 5
            "Pikachu and I eat lunch together."
            "We make some small talk, but for the most part, it's quiet."
            "However, it's a comfortable kind of quiet."
            "There are times where words aren't needed."
        "Decline the offer":
            player "It's okay, Pikachu. I can't always rely on you for things!"
            pika "...? {w}Where did that come from?"
            player "Well, you're always there for me... {w}What if I'm not always there for you?"
            player "If I can't even get my own lunch at times like this, when how reliable of a person am I really?"
            pika "..."
            player "What's wrong, Pikachu?"
            pika "Nothing, [name]."
            pika "So what are you going to do about lunch?"
            "He has a point. What should I do?"
            menu:
                "Buy your own lunch":
                    player "No choice but to buy my own lunch!"
                    pika "Okay, [name]. Come back soon!"
                    #fade cafeteria
                    "...{w}Where's the menu around here?"
                    "..."
                    "Oh! {w}There it is."
                    "..."
                    "I'll get the vegetable soup with fish."
                    "It seems like the healthiest option here. I heard fish helps your brain!"
                    "I receive my vegetable soup with fish and pay $7 for it."
                    $ inventory.earn(-7)
                    "Alright! Now I can head back to class 2-B."
                    #fade class
                    player "I'm baaack!"
                    pika "Oh, welcome back."
                    pika "What did you get?"
                    player "Vegetable soup and fish."
                    pika "Haha, that's so fitting."
                    player "What do you mean?"
                    pika "Well, it's the healthiest option at this school."
                    player "Oh! Hehe, my health is in tip-top shape! {w}Jealous?"
                    pika "Yeah, haha!"
                    "Pikachu and I spent the rest of lunch eating together."
                    "The vegetable soup and fish was delicious!"
                    "But I can't help but feel a twinge of guilt... {w}I wonder why?"
                    "There's nothing wrong with eating fish... {w}I think." #UR DAD IS A FISH
                    $ pika_pts += 5
                "Don't eat lunch":
                    player "I guess I'll just suffer the consequences!"
                    player "This is my punishment so that I'll never forget the bring my lunch ever again."
                    if pika_pts >= 20:
                        pika "Oh, come on, [name]. You're going to extremes."
                        pika "Here, I insist. Take some of my food."
                        player "But, Pikachu, didn't you hear me earlier?"
                        pika "Come on, just rely on me one more time."
                        pika "I don't want to see you hungry."
                        pika "Put your pride aside for just a moment and let me take care of you, okay?"
                        player "..."
                        player "Okay, fine."
                        player "But if I forget my lunch again, you're not allowed to feed me!"
                        player "If you do, I'll stop being your friend!!"
                        pika "Haha, you're being ridiculous. {w}But that's what makes you so fun to be around."
                        $ pika_pts += 5
                    else:
                        pika "..." #sad face
                        pika "I won't eat either then."
                        pika "It isn't fair of me to keep eating in front of you while you're hungry."
                        "...!"
                        "Pikachu is offering to stop eating his lunch to accompany me on my lunch-less lunch."
                        "What should I say?"
                        menu:
                            "Okay.":
                                player "How nice of you, Pikachu!"
                                pika "It's no problem."
                                "We spend the rest of lunch goofing off and talking to each other about our days."
                                $ pika_pts += 1
                            "No! You're eating your lunch!":
                                player "No! You're not allowed to give up your lunch just because I don't have mine!" with vpunch
                                player "What kind of person would I be to make you suffer along with me?"
                                pika "But are you sure? I don't want to make you even hungrier by eating my food in front of you."
                                player "Don't worry about it!" with vpunch
                                player "You're not the {i}only{/i} one eating lunch in front of me. {w}{i}Everyone{/i} is eating around me!"
                                pika "..."
                                pika "That's making me worry even more!"
                                pika "Here!" with vpunch
                                pika "Take some of my lunch, I insist!" with vpunch
                                player "Huh? But I just said--"
                                pika "[name]!" with vpunch
                                player "...Okay, Pikachu."
                                "As I bite into Pikachu's food, I notice his cooking has improved."
                                "Come to think of it, the last time I ate Pikachu's homemade food was in middle school."
                                "It has been two years, huh... {w}Time sure does fly by."
                                "Pikachu and I spend the rest of our lunch time sharing his food."
                                $ pika_pts += 5
    return
    
label forgot_lunch3:
    $ forgotlunch3 = True
    "Let's eat lunch with Jynx today!"
    "I head over to class 3-C."
    if char_dex:
        "There, I see a bright red pokemon... {w}Wait a minute..."
        "That's Charmeleon!"
        player "Hey, Charmeleon!"
        char "...?"
        char "My, my, my... {w}Who could you be?"
        char "Another lost little lamb who just happened to... {w}{i}wander{/i} into the realm of upperclassmen...?"
        player "Wh--"
        char "It seems that you aren't familiar with the school grounds yet."
        char "Would you like me to... {i}show you around...?{/i}"
        "What the heck is this guy saying? What should I do?"
        menu:
            "Grab his tail" if grabbed_tail:
                $ char_pts -= 2
                "I decide to remind him of who I really am."
                "Once again, I grab his tail."
                char "OW!" with vpunch
                char "N-Now, now, little lamb... {w}There is enough of me to go around..."
                char "Just... {w}let go of me for a bit."
                player "You {i}still{/i} don't remember me?"
                char "Huh?"
                "Charmeleon eyes me up and down."
                char "..."
                char "!" with vpunch
                "He retracts his tail."
                char "It's {i}you!{/i}" with vpunch
                char "What are you doing here!?"
                char "How did you find out about my school!?"
                char "..."
                char "You..."
                char "You are not stalking me, are you?"
                char "Are you not what one would call... a {i}sasaeng?{/i}"
                player "No! I don't even know what that is!" with vpunch
                player "I came here to eat lunch with my friend!"
                player "Speaking of whom, I wonder where she--"
                jynx "HEY GIRL!!!" with vpunch
                jynx "WHAT YOU DOIN' HERE!?"
                player "I came to eat lunch with you!"
                jynx "Wow, ain't that sweet of you!"
                jynx "What's Charmander doin' here, huh? He pickin' on you?"
                char "Um, my name is not--"
                jynx "Charmander, why you gotta be so rude?"
                jynx "Just be a nice dear and have lunch with us instead of pickin' on poor lil' [name]!"
                jynx "Let's all be friends!"
                "Jynx puts her arms around our shoulders."
                "She starts to drag both of us to the nearest empty table."
                player "Hey, I--" with hpunch
                char "Wait, let go--" with hpunch
                "*THUD*" with vpunch
                char "Why are you so strong!?"
                jynx "Once again, let's all be friends!"
                player "Huh?"
                char "With this [gender]?! But [pronoun2] grabbed my tail! {w}Twice!"
                jynx "Aren't you supposed to be an upperclassman?"
                char "So??? What does that matter?"
                jynx "Oh, my bad. I need to speak your language."
                jynx "Ahem. {w}How can you be so rude to such an {i}adorable{/i}, lost little lamb?"
                jynx "Look at [pos_pronoun] beautiful eyes."
                if haircut:
                    jynx "And look at that amazing hair! I sure wonder who did it for you!"
                    jynx "Stunning! {w}Amazing! {w}Simply gorgeous!"
                jynx "Surely, you can't be so cruel to such a cute [gender]?"
                char "..."
                char "Heh."
                char "Well, when you put it that way..."
                char "Refusing the requests of a young maiden is not very becoming of a well-seasoned connoisseur of gentlemanly behaviour such as myself."
                jynx "There you go! {w}That wasn't so bad, was it?"
                jynx "[name], what do you say?"
                menu:
                    "Let's be friends!":
                        $ char_pts += 5
                        player "Okay, let's put all that tail pulling and stuff behind us!"
                        char "..."
                        jynx "{i}Charmander...?{/i}"
                        char "!"
                        char "Yeah, okay!"
                    "Screw Charmeleon!":
                        $ char_pts -= 3
                        player "Screw you, Charmeleon!"
                        char "Screw me? That is gross."
                        char "Can that even happen? Are you not a different species?"
                        jynx "No dude, she's cursin' you out..."
                        char "Ohhhh."
                        char "Hey, that is very rude!" with vpunch
                        char "Why, I ought to--"
            "Reintroduce yourself":
                player "Hey, don't you remember me?"
                player "We met at the Pikabelle Chutendo meet-and-greet!"
                char "!"
                if grabbed_tail:
                    char "You were the one who abused me!" with vpunch
                    "He retracts his tail."
                    char "What are you doing here!?"
                    char "How did you find out about my school!?"
                    char "..."
                    char "You..."
                    char "You are not stalking me, are you?"
                    char "Are you not what one would call a... {i}sasaeng?{/i}"
                    player "No!"
                else:
                    char "You were standing behind me!"
                    player "Yeah!"
                player "I didn't know that we both go to the same school!"
                player "I came here to eat lunch with my friend!"
                player "Speaking of whom, I wonder where she--"
                jynx "HEY GIRL!!!" with vpunch
                jynx "WHAT YOU DOIN' HERE!?"
                player "I came to eat lunch with you!"
                jynx "Wow, ain't that sweet of you!"
                jynx "What's Charmander doin' here, huh? He pickin' on you?"
                char "Um, my name is not--"
                jynx "Charmander, why you gotta be so rude?"
                player "Oh, no! He wasn't picking on me at all."
                jynx "Good!"
                jynx "Otherwise, I'd have to cross some lines to protect my cute lil' [name]! ♥"
                char "Uh--"
            "Go along with it":
                $ char_pts += 5
                player "Oh my, what a gentleman~"
                player "I sure would {i}love{/i} to be in your hands!"
                char "Don't worry... Just let me take care of you."
                player "Be careful~ I'm a fragile [gender] ♥"
                "*SLAM*" with hpunch
                jynx "Y'ALL NEED TO STOP FLIRTING RIGHT BY THE DOOR!!!" with vpunch
                jynx "Charmander! What do you think you're doing?"
                char "I was just talking with..."
                char "..."
                char "Hey... I seen you somewhere before?"
                char "!" with vpunch
                if grabbed_tail:
                    char "Didn't you grab my tail at the Pikabelle Chutendo meet-and-greet!?"
                    "He retracts his tail."
                    char "It {i}is{/i} you!" with vpunch
                    char "What are you doing here!?"
                    char "How did you find out about my school!?"
                    char "..."
                    char "You..."
                    char "You're not stalking me, are you?"
                    player "No!"
                    player "I came here to eat lunch with my friend!"
                else:
                    char "Weren't you standing behind me at the Pikabelle Chutendo meet-and-greet!?"
                    player "Yeah!"
                player "I didn't know that we both go to the same school!"
                jynx "Charmander, join us since you're here anyway!"
                char "Huh? Wait, I--"
    else:
        "As soon as I open the door, I run into a bright red pokemon."
        "*THUD*" with hpunch
        unknown "Ow!"
        unknown "What was that for!?"
        player "!?"
        player "It was an accident!"
        unknown "!"
        unknown "...?"
        unknown "My, my, my... {w}Who could you be?"
        unknown "Another lost little lamb who just happened to... {w}{i}wander{/i} into the realm of upperclassmen...?"
        player "Wh--"
        unknown "It seems that you aren't familiar with the school grounds yet."
        unknown "Allow me to formally introduce myself."
        unknown "They call me..."
        char "{b}{i}Charm{/i}{/b}eleon."
        $ char_dex = True
        pdex "Charmeleon has been added to your Pokedex."
        "Did he just make a pun with his name?"
        char "Would you like me to... {i}show you around...?{/i}"
        "What the heck is this guy saying? What should I do?"
        menu:
            "Grab his tail":
                $ char_pts -= 2
                "I take hold of his tail."
                char "OW!" with vpunch
                char "N-Now, now, little lamb... {w}There's enough of me to go around..."
                char "Just... {w}let go of me for a bit."
                "*SLAM*"
                jynx "HEY GIRL!!!" with vpunch
                jynx "WHAT YOU DOIN' HERE!?"
                player "!"
                player "Jynx!"
                player "I came to eat lunch with you!"
                jynx "Wow, ain't that sweet of you!"
                jynx "What's Charmander doin' here, huh? He pickin' on you?"
                char "Um, my name isn't--"
                jynx "Charmander, why you gotta be so rude?"
                jynx "Just be a nice dear and have lunch with us instead of pickin' on poor lil' [name]!"
                jynx "Let's all be friends!"
                "Jynx puts her arms around our shoulders."
                "She starts to drag both of us to the nearest empty table."
                player "Hey, I--" with hpunch
                char "Wait, let go--" with hpunch
                "*THUD*" with vpunch
                char "Why are you so strong!?"
                jynx "Once again, let's all be friends!"
                player "Huh?"
                char "With this [gender]?! But [pronoun2] grabbed my tail!"
                jynx "Aren't you supposed to be an upperclassman?"
                char "So??? What does that matter?"
                jynx "Oh, my bad. I need to speak your language."
                jynx "Ahem. {w}How can you be so rude to such an {i}adorable{/i}, lost little lamb?"
                jynx "Look at [pos_pronoun] beautiful eyes."
                if haircut:
                    jynx "And look at that amazing hair! I sure wonder who did it for you!"
                    jynx "Stunning! {w}Amazing! {w}Simply gorgeous!"
                jynx "Surely, you can't be so cruel to such a cute [gender]?"
                char "..."
                char "Heh."
                char "Well, when you put it that way..."
                char "Refusing the requests of a young maiden isn't very becoming of a well-seasoned connoisseur of gentlemanly behavior such as myself."
                jynx "There you go! {w}That wasn't so bad, was it?"
                jynx "[name], what do you say?"
                menu:
                    "Let's be friends!":
                        $ char_pts += 5
                        player "Okay, let's put all that tail pulling and stuff behind us!"
                        char "..."
                        jynx "{i}Charmander...?{/i}"
                        char "!"
                        char "Yeah, okay!"
                    "Screw Charmeleon!":
                        $ char_pts -= 3
                        player "Screw you, Charmeleon!"
                        char "Screw me? That is gross."
                        char "Can that even happen? Are you not a different species?"
                        jynx "No dude, she's cursin' you out..."
                        char "Ohhhh."
                        char "Hey, that is rude!" with vpunch
                        char "Why, I ought to--"
            "Introduce yourself":
                $ char_pts += 2
                player "My name is [name]!"
                player "I'm a second-year, and I came here to meet with my friend Jynx--"
                char "Sh... Dear..."
                char "All I had to do was peer deeply into your wondrous eyes, and all the answers became clear...!"
                char "You are here... {w}to meet with your friend, Jynx!"
                player "... {w}Um..."
                player "That's what I just said..."
                jynx "HEY GIRL!!!" with vpunch
                jynx "WHAT YOU DOIN' HERE!?"
                player "I came to eat lunch with you!"
                jynx "Wow, ain't that sweet of you!"
                jynx "What's Charmander doin' here, huh? He pickin' on you?"
                char "Um, my name isn't--"
                jynx "Charmander, why you gotta be so rude?"
                player "Oh, no! He wasn't picking on me at all."
                jynx "Good!"
                jynx "Otherwise, I'd have to cross some lines to protect my cute lil' [name]! ♥"
                char "Uh--"
            "Go along with it":
                $ char_pts += 5
                player "Oh my, what a gentleman~"
                player "I sure would {i}love{/i} to be in your hands!"
                char "Don't worry... Just let me take care of you."
                player "Be careful~ I'm a fragile [gender] ♥"
                "*SLAM*" with hpunch
                jynx "Y'ALL NEED TO STOP FLIRTING RIGHT BY THE DOOR!!!" with vpunch
                jynx "Charmander! What do you think you're doing?"
                char "I was just talking with this lovely [gender]."
                jynx "You sure you ain't bein' all weird and romantic? 'Cause it sure sounds like it."
                char "My, whatever do you mean?"
                jynx "Ah, nevermind."
    jynx "Let's eat lunch!!!" with vpunch
    player "...!"
    player "I forgot my lunch!" with vpunch
    char "Hah! That sucks."
    jynx "Shut up, Charmander."
    jynx "[name], what are you going to do?"
    player "Um..."
    "What should I do?"
    menu:
        "Go buy your own lunch":
            player "I guess I'll just go buy my own lunch then."
            player "Be right back!"
            if char_pts >= 10:
                char "Wait!"
                char "I cannot just leave a lost, little lamb to fend for nourishment all alone!"
                char "What if you get lost again? Allow me to accompany you."
                "Charmeleon wants to come along."
                "Should I let him?"
                menu:
                    "Yes":
                        player "Okay, I suppose you can come along."
                        char "Wondrous! {w}Worry not, for you are safe within my care."
                        char "We shall return post-haste, Jynx!"
                        jynx "Yeah, yeah get goin' and hurry back!"
                        $ char_pts += 2
                        $ char_getlunch = True
                    "No":
                        player "It's fine. I can find the cafeteria on my own."
                        player "I was never lost in the first place."
                        char "Alas, it is tragic of a young [gender] to become lost."
                        char "I will pray for your safe return."
            #fade cafeteria
            "Wow! So this is the cafeteria."
            "I'm not too familiar with buying my own lunch. I always bring lunch from home."
            if char_getlunch:
                player "Charmeleon, what's good?"
                char "Hm..."
                char "I quite fancy the ddeokbokki here."
                char "The spice level brings a certain kind of delicious tingle."
                player "Okie-dokie!"
                char "Do you mean... {i}okie-ddeokbokki?{/i}"
                "Was that supposed to be a pun? How should I respond?"
                menu:
                    "Hilarious!":
                        $ char_pts += 5
                        player "Haha, that was so funny!"
                        char "Thank you!"
                        char "The ddeokbokki makes my heart go doki doki."
                        char "..."
                        char "{i}Okie-doki-doki-ddeokbokki.{/i}"
                        "Oh my god."
                    "Lame...":
                        $ char_pts -= 5
                        player "...{w}..."
                        char "..."
                        "That uncomfortable pun brought about an equally uncomfortable silence..."
                player "I'm getting in line now."
                "Shortly afterward, I receive my ddeokbokki and pay $7 for it."
                $ inventory.earn(-7)
                "I grab my food and return to Charmander."
                char "Nice choice."
                char "Now, let us return to Jynx. She must be positively anxious for our return."
            else:
                "...{w}Where's the menu around here?"
                "..."
                "Oh! {w}There it is."
                "..."
                "I'll get the vegetable soup with fish."
                "It seems like the healthiest option here. I heard fish helps your brain!"
                "I receive my vegetable soup with fish and pay $7 for it."
                $ inventory.earn(-7)
                "Alright! Now I can head back to class 1-A."
            # fade classroom
            if char_getlunch:
                jynx "What took you guys so long!?" with vpunch
                char "We were not gone for that long..."
            else:
                jynx "What took you so long!?" with vpunch
                char "I see you found the cafeteria without getting lost."
                char "Being able to learn on one's own is a fine trait."
            "Jynx, Charmeleon, and I all spend lunch together, eating and chatting happily."
            char "And my name is Charmeleon, not Charmander!" with vpunch
            jynx "Oh, is that so?"
            $ char_pts += 5
        "Don't eat lunch":
            pass
    return
    
