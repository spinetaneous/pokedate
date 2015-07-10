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

#FUTURE EVENTS:
#   charmeleon fucking dies at the beach (maybe the worst ending??? maybe happens in the middle of the game?? i dunno)
#   camping adventure with everyone but u get lost with charmeleon and he makes a lil fire for u (cuz he's made of fire)
#   ditto gets kidnapped and u rescue him
#   PIKACHU EARNS PERFECT ATTENDANCE AWARD AND U DON'T *RIFT CREATED* but pikachu has never taken it srsly so u are offended
#   the "I never needed you" ending for not choosing pikachu (worst ending)
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
    define popo = Character('Police')

    #pokemon (besides dad)
    define pbc = Character('Pikabelle Chutendo', color="#ffd700")
    define jynx = Character('Jynx', color="#70018b") #works at salon
        #info-chan
        #thinks she's popular
        #genki girl. all up in ur face. nice once u get used to her
    define bulb = Character('Bulbasaur', color="#008080") #works at florist/is the florist
        #normal guy. boo
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
        #gets embarrassed easily
    define ditt = Character('Ditto', color="#c9a0dc") #works at sleezy store 
        #silly and weird
        #wants to fit in bc he's a scared and tiny freshman who is also a blob with no form
        #also the LAMEST
    
    #fake dittos
    define dpika = Character('Pikachu', color="#c9a0dc")

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
        
        #the process of finding a job
        event("where_job_hunt", "act == 'job_hunt' and not has_job", event.solo(), priority=1)
        event("get_haircut", "act == 'salon' and jynx_dex",event.solo(), event.once(), priority=999)
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
        player "Really?! Dang... That's too bad..."
        player "I guess I need to try somewhere else then."
        digl "..."
        #if player knows jynx, then diglett says go to the bakery
        #if not, then diglett says to go to the salon
        #this is the help player be introduced to both these characters
        if jynx_dex:
            digl "{size=-5}You could try the bakery... \"La Pokesserie\" I think it was called...{/size}"
        else:
            digl "{size=-5}You could try the salon... They might be hiring...{/size}"
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
        digl "Go get hired somewhere else. The gym isn't hiring right now."
        if tried_gamemon:
            player "What!? But I saw a flyer that said you were hiring!"
            digl "Argh, I already told all the stores to take those down..."
            digl "That flyer is old. We already have the employees we need."
        player "Really?! Dang... That's too bad..."
        player "I guess I need to try somewhere else then."
        digl "..."
        #if player knows jynx, then diglett says go to the bakery
        #if not, then diglett says to go to the salon
        #this is the help player be introduced to both these characters
        if jynx_dex:
            digl "{size=-5}You could try the bakery... \"La Pokesserie\" I think it was called...{/size}"
        else:
            digl "{size=-5}You could try the salon... They might be hiring...{/size}"
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
    player "It's ok! I won't let this failure get me down!"
    player "I WILL CONQUER THE JOB MARKET!"
    player "Do you know any store that's hiring?"
    bulb "I don't. Ask other people."
    bulb "They might be more helpful."
    bulb "Might."
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
            player "Bruh, you askin' me to smile, but why ain't you smilin'?"
            dpika "Damn, you hella sharp fo'sho."
            player "Yeah, as sharp as my di--"
            $ ditt_pts += 1
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
    player "Then wait, who's this!?!?"
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
    "At this point, I'm so tired of being dragged around that I don't even bother to look in the mirror."
    player "Thanks, Jynx. Well, I'd best be going! See you tomorrow!"
    jynx "No problem, sweetie."
    "And with that, I get out of that salon."
    $ haircut = True
    return