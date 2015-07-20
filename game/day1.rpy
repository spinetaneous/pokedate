# This is the script for the events that occur on Monday, day 1 of PokeDate.
# These appear before the day planner surfaces, as to introduce the player
# to the characters before making any real choices.

label breakfast:
    "It's the start of a new day."
    "My name is [name], and I'm just a regular human in the pokemon world."
    "I'm a second-year in a high school called PokeCreek. It's full of very diverse pokemon!"
    "When I was 3, I was adopted by a single father."
    "He's the most caring person I know."
    "We eat breakfast together every morning..."
    player "Good morning, Dad!"
    dad "Good morning, [name]."
    player "Guess what, Dad? Something exciting is happening today!"
    dad "How could I forget?"
    dad "It's the special meet-and-greet with the creator of that game you love so much."
    dad "{i}PokeCrossing: New Ball{/i}, right?"
    player "Yeah! I can't believe I'll get to meet Pikabelle Chutendo in person!"
    player "They're holding it in the park. I'm going to go after school and get her autograph!"
    player "Then I'll frame it on the wall and keep it forever!"
    dad "I'm so happy for you, [name]."
    player "Thanks, Dad."
    player "What's for breakfast?"
    dad "Your favorite: waffles!"
    player "Thanks, Dad! I love your cooking."
    "I take a bite."
    player "Wow, this is delicious! New recipe?"
    dad "Yes, this time I tried adding more seaweed."
    player "The saltiness from the seaweed really brings out the sweetness of the syrup."
    dad "I knew you'd like it, [name]. Here's some milk to wash it down."
    player "Thanks, Dad. You're the best! I love you."
    dad "I love you, too."
    dad "..."
    dad "Don't you start school at 8AM?"
    dad "Better get to school before you're late!"
    "I briefly glance at the clock."
    player "Oh shoot, you're right! It's 7:50AM already!?"
    player "I'll have to run if I want to make it before the bell rings!"
    "I quickly gather my backpack and lunchbox before racing out the door."
    #add fade when u hav bg images ok
    jump school_day1
    
label school_day1:
    "..."
    "...I can... see the school...!"
    "...It's... 7:59AM..."
    "...I can... totally... make it...!"
    "DING -- DONG -- DING -- DONG --"
    "..."
    "...I can still... make it...!"
    #fade to class
    "**SLAM**" with vpunch
    player "{size=+5}TEACHER...! I AM HERE!!!{/size}" with vpunch
    t "Wow, and it's only 8:03AM." with vpunch
    player "{size=+5}I... AM NOT LATE!!!!{/size}" with vpunch
    "From the door, I can see my childhood friend, Pikachu, looking worried for me."
    "I flash him a brief thumbs up and wink, as if saying, \"Don't worry, I got this!\""
    "..."
    "Hey, did he just shake his head?"
    t "Just take a seat, [name]."
    player "{size=+5}WAIT, DID YOU JUST MARK ME LATE--{/size}" with vpunch
    t "[name]."
    t "Take a seat."
    "She probably didn't mark me late, right?"
    "As I take my seat, the teacher resumes her lecture."
    t "Now, class... Remember that next week is finals week."
    t "If you do well enough, you might even win a prize!" #reward is gary gary oak kun
    t "Today we will be learning about the First Fundamental Theorem of Calculus."
    "..."
    "I rest my head against my hand."
    "..."
    "I still taste some seaweed."
    #fade out to lunch
    jump lunch_day1
    
label lunch_day1:
    "DING -- DONG -- DING -- DONG --"
    "Before I know it, it's lunch time!"
    t "Alright class, you're dismissed!"
    t "If you have any questions, speak to me after class."
    t "Not during lunch. I value my lunch time."
    "And with that, she leaves."
    pika "Hey, [name]!"
    pika "That was quite a scene this morning."
    "This is Pikachu. I've known him for over 10 years now."
    "He lives across the street from me, and we spent our childhood playing together."
    "Even now, we're still very good friends."
    "He's a really kind and considerate guy."
    "Out of all the people in this school, Pikachu probably knows me the very best."
    player "What's up, Homiechu!"
    pika "I told you not to call me that."
    player "Aw... But it's such a cute nickname!"
    player "Homiechu~"
    pika "Okay if you get to call me that then..."
    pika "I get to call you [name]-tan."
    player "!!!"
    player "That's not cute at all!"
    pika "You have a weird sense of what's cute and what's not."
    pika "The point is, just don't call me Homiechu."
    player "Okay..."
    "I pout a little."
    pika "H-Hey, don't make that face, or I'll feel bad."
    pika "Tell you what, let's go to the mall after school, okay?"
    pika "I'll, uh, I'll buy you a pokepuff from that place you love so much!"
    "...!"
    "After school? Isn't that when the meet-and-greet is?"
    "What should I do?"
    menu:
        "Agree to go with him later.":
            $ pika_mall = True
            "Friendship triumphs over everything!"
            "Even over Pikabelle Chutendo...!"
            player "It's a date!"
            pika "..." #PIKABLUSH
            player "Thanks, Pikachu! I love you!"
            #PIKABLUSH!!! oh my god i feel so sad
            pika "..."
            pika "No problem."
            pika "...Any time."
            pika "We're..."
            pika "...friends, after all." #MUSIC STOPS
            player "Yeah!" #music resumes wow u are so dense
            "I can't wait for class to be over!"
            #fade to after school
            jump mall_day1
        "Decline for the meet-and-greet.":
            $ pika_mall = False
            player "Sorry, I have something to do after school."
            pika "Really? What is it?"
            player "Haven't you heard? Pikabelle Chutendo is coming to the park for an autograph signing session!"
            pika "Oh..."
            player "Want to come along?"
            pika "..."
            pika "Well, I appreciate the offer but..."
            pika "I think I'll pass."
            player "Aw... That's too bad."
            player "Let's go to the mall some other time then, yeah?"
            pika "Alright, sounds good."
            player "It's a date!"
            #PIKABLUSH
            pika "...!"
            pika "Y-Yeah!"
            player "I love you, Pikachu!"
            pika "..."
            pika "Yeah..."
            pika "I..."
            pika "I love you... too."
            player "I couldn't have asked for a better friend."
            pika "..." #MUSIC STOPS
            pika "Same here."
            #fade to park
            player "Pikabelle Chutendo... I'll finally get to see her in real life!"
            player "I can't wait until after school!"
            jump park_day1

label park_day1:
    #still at school
    "DING -- DONG -- DING -- DONG --"
    "School's out!"
    "It's finally time for the meet and greet! I'm so excited!"
    player "Seeya, Pikachu!"
    pika "Have fun, [name]."
    #fade park
    "Wow, there are more pokemon than I expected..."
    "The line is so long... Am I going to be able to meet Pikabelle Chutendo...?"
    "I guess it's my fault for being so late..."
    "Wait..."
    "There was no official starting time!"
    "Without that, there's no way to be late!"
    "Haha, once again, my punctuality persists."
    "..."
    "Maybe I should get in line."
    #footsteps
    "..."
    "Whoa...! I wonder what this pokemon is?"
    "Big and orange..."
    "...On fire..."
    "Oh! I know about this type of pokemon! They're in movies all the time!"
    "I've never seen a fire-type pokemon in real life before..."
    "..." #fade black
    "Man, it's really hot today..."
    "Why does the guy in front of me have to be on fire?"
    "..." #fade black
    "Oh man, this line is so long..."
    "I'm so bored..."
    "...But this is all... for Pikabelle Chutendo...!"
    "..." #fade black
    "I..."
    "..."
    "I am pretty sure I've never been this bored in my entire life."
    "Gotta do something to kill time..."
    "What should I do?"
    menu:
        "Start a conversation with the guy in front":
            "Since this pokemon is in line at a Pikabelle Chutendo event, that must mean that he likes {i}PokeCrossing!{/i}"
            "I tap him on the shoulder. His skin is rough and warm... Kinda weird."
            unknown "!"
            player "Hey there!"
            player "My name is [name]."
            unknown "..."
            "What should I say?"
            menu:
                "What's it like being so hot all the time?":
                    $ char_pts += 5
                    unknown "!"
                    unknown "Well, I suppose one could refer to me as a..."
                    unknown "{i}...force of nature{/i}."
                    player "..."
                    player "I don't get it."
                "Pikabelle Chutendo is pretty cool, right!?":
                    unknown "Well, she {i}is{/i} capable enough to create a plethora of enjoyable entertainment."
                    unknown "However, she is not my type."
                    player "Dude, she's married."
                "You know, I think you're giving me heat stroke...":
                    $ char_pts -= 5
                    unknown "Well... I am a fire-type pokemon after all..."
                    unknown "My..."
                    unknown "{i}...heat...{/i}"
                    unknown "...can be pretty hard to handle sometimes."
                    "I can't believe he just said that."
                    unknown "Maybe you should go to the back of the line or something."
                "Have you played any {i}PokeCrossing{/i} games lately?":
                    $ char_pts += 10
                    unknown "In fact, I have!"
                    unknown "Why, just yesterday I was playing {i}New Ball{/i}, and I was able to put in a campsite!"
                    player "Oh, those are fun!"
                    player "You get non-resident villagers in there, and then you can play cool minigames to get furniture."
                    unknown "How amazing!"
                    player "Sometimes you lose though, and then they take money or items from you..."
                    unknown "Oh..."
                    player "I usually fill my inventory with shells and put all my money in the bank!"
                    unknown "That is smart!"
                    unknown "Perhaps next time I will utilize that technique!"
                    player "Yeah!"
                    unknown "..."
        "Play with the fire-type pokemon's tail":
            $ char_pts -= 5
            $ grabbed_tail = True
            "Wow, this tail is not as hot as I thought it would be."
            "Actually, it's nice and warm."
            "Maybe it gets hotter towards the end of the tail, where the fire is."
            unknown "!"
            unknown "What are you doing!?"
            "Oh, he noticed me."
            "What now?"
            menu:
                "Light something on fire.":
                    "This is very dangerous, but..."
                    "What should I light?"
                    menu:
                        "The fire-type pokemon!":
                            "I start pointing the tail towards the pokemon in front of me."
                            unknown "Wh-What are you doing!?"
                            unknown "Unhand me!"
                            player "Wait, just hold still for a bit..."
                            unknown "OW!" with vpunch
                            unknown "STOP!" with vpunch
                            unknown "THAT HURTS!" with vpunch
                            "The pokemon snatches his tail out of my hands."
                            unknown "WHAT ARE YOU DOING!?"
                            unknown "I DON'T EVEN KNOW YOU!"
                            unknown "WHY ARE YOU ATTACKING ME WITH MY OWN TAIL!?"
                            "People are looking at me worriedly."
                            "Maybe this was a bad idea?"
                            popo "Stop right there!" with vpunch
                            popo "We got calls about an assault taking place at the park!"
                            player "!"
                            player "W-Wait, I--"
                            popo "You have the right to remain silent!"
                            "Apparently, lighting a pokemon on fire with their own tail is a bad idea."
                            "The police arrested me."
                            "Now I await my trial."
                            "BAD END"
                            "CRIMINAL"
                            $ renpy.full_restart()
                        "That tree!":
                            "I start pulling the tail towards a random tree."
                            unknown "HEY, THAT HURTS!" with hpunch
                            "I'm not strong enough to drag him to the tree..."
                            "Guess there's no choice but to let him go."
                            unknown "What the hell was that for!?"
                            player "Sorry."
                            player "The boredom of waiting in line was getting to me."
                            unknown "{i}That doesn't mean you can just grab my tail like that!{/i}"
                            player "Well, sorry!!"
                        "Myself!":
                            "..."
                            "I stand there for a moment, worried about my own intelligence."
                            "Lighting myself on fire would be a very bad idea."
                            unknown "What are you doing!? Give that back!"
                            "He snatches the tail out of my hands."
                            unknown "I know that it is difficult to keep your hands off me, but please exercise some control."
                            player "..."
                        "Nevermind!":
                            $ char_pts += 5
                            player "Sorry! I was just spacing out."
                            unknown "I know that it is difficult to keep your hands off me, but please exercise some control!"
                            player "..."
                "Apologize.":
                    $ char_pts += 5
                    player "Sorry, I didn't mean to grab your tail!"
                    unknown "..."
                    unknown "Well, I suppose if you did not mean to..."
                    unknown "I guess I can let you off just this once..."
    "..."
    player "So uh..."
    player "What's your name?"
    if grabbed_tail:
        unknown "Why should I tell you?"
        player "Hey, I'm sorry, okay!?"
        player "At least let me know your name! Then I can properly apologize."
        unknown "..."
        char "I am called Charmeleon."
        $ char_dex = True
        pdex "Charmeleon has been added to your Pokedex."
        player "Once again, I'm really sorry!"
        player "Please forgive me, Charmeleon!"
        char "...Sigh."
        char "If you are going to be like that then..."
        char "I suppose..."
        player "Phew!"
    else:
        "He chuckles."
        unknown "So... You wish to know my name, huh?"
        unknown "They call me..."
        char "{b}{i}Charm{/i}{/b}eleon."
        $ char_dex = True
        pdex "Charmeleon has been added to your Pokedex."
        "Did he just make a pun with his name?"
        menu:
            "Wow, that's pretty cool!":
                $ char_pts += 5
                char "I know, right!?"
                char "What a shame not many people think it's funny."
                char "You... {w}are different, though. You thought it was cool."
                char "Great minds think alike!"
                player "I know, right!?"
                player "Your puns are so {i}fire!!{/i}"
                char "Fire?"
                player "Get it? \"Fire\" in teenage slang describes something really good!"
                player "And also you're a fire-type pokemon!"
                char "Wow, that is truly clever."
                char "You are so witty. How old are you anyway?"
                player "I'm a second-year in high school!"
                char "Truly? I am a third-year!"
                char "Which school do you go to!?"
                player "PokeCreek!"
                char "!"
                char "I, too, attend that school!"
                char "Perhaps we shall see each other around."
                char "I do wonder why we haven't seen each other before..."
                player "I don't visit other classes that often, but maybe that'll change."
            "Wow, that's pretty lame!":
                $ char_pts -= 5
                char "!"
                char "You just do not appreciate my great sense of humor."
                player "What sense of humor?"
                char "!"
                char "You are very rude... similar to a little kid."
                char "Are you perhaps a 12 year old?"
                player "No! I'm a second-year in high school!"
                char "Pfft, no wonder. You would not understand the wit of a third-year such as I."
                player "You're in high school? You seem like an old man."
                player "What high school would accept you?"
                char "Um, PokeCreek? The one I {i}attend?{/i}"
                player "!"
                player "That's my school!"
    "..."
    "Before we notice, Charmeleon's already at the front of the line."
    "..."
    "He talks with Pikabelle Chutendo and gets her autograph."
    "Then he turns to leave."
    player "Oh, before you go..."
    player "Want to exchange Tomodachi-Codes for our Chutendo TS's?"
    player "I don't know anyone else who plays {i}PokeCrossing{/i}."
    char "Hm... I don't have many people to play either..."
    if grabbed_tail:
        char "Alright."
    else:
        char "Sure!"
    player "Oh wait, I don't have my TS with me..."
    player "Can we exchange numbers too? Then we can text each other our codes!"
    if grabbed_tail:
        char "..."
        char "There is no helping it..."
    else:
        char "No problem."
        char "I would not mind giving my number to such a lovely [gender] such as yourself."
        "He winks at me."
    "Charmeleon hands me a slip of paper."
    char "Recorded here is my number. You may text me tonight, if you wish."
    if grabbed_tail:
        char "...I guess."
    player "Thanks!"
    char "I must return home now."
    if not grabbed_tail:
        char "We shall converse at another time!"
    player "Bye!"
    "He runs off."
    "..."
    "...Now..."
    "...Right before my very eyes..."
    "...Pikabelle Chutendo...!"
    pbc "Hello there!"
    "She hands me an autograph."
    player "{size=+5}OH MY GOD PIKABELLE CHUTENDO I LOVE YOU SO MUCH{/size}" with vpunch
    player "{size=+5}I HAVE EVERY SINGLE ONE OF YOUR GAMES{/size}" with vpunch
    pbc "Really? Each one?"
    pbc "Wow, you must be a big fan! I'm glad you like my games so much."
    pbc "I thought some might not like {i}Happy Ball Designer{/i} since it's a bit different than the rest..."
    player "..."
    player "...Wait..."
    player "{i}Happy Ball Designer?{/i}"
    pbc "Oh, it's my new game. Perhaps you haven't heard of it?"
    pbc "Maybe you have every single game except that one, then."
    pbc "It's alright if you don't have {i}every{/i} one."
    pbc "I love all my fans, no matter what. Fans like you are what make everything worthwhile!"
    player "You have a new game!?"
    player "I have to have it!"
    player "Sorry, I gotta go!"
    player "{size=+5}THANK YOU FOR EXISTING PIKABELLE CHUTENDO I LOVE YOU VERY MUCH GOODBYE{/size}" with vpunch
    pbc "See you!"
    pbc "What a nice [gender]."
    jump see_game_day1
    
label mall_day1:
    "After school, Pikachu and I go to the mall together."
    "We first head to the pokepuff place."
    #show la pokesserie
    pika "Pick whichever one you like."
    #insert menu here once i learn how to do imagebuttons
    "The cashier hands a small paper bag to Pikachu."
    pika "I'll hold it for you while we hang out at the mall together."
    player "Thanks, Homiechu!"
    pika "[name]... I told you not to call me that..."
    pika "Isn't that part of the reason why we're here in the first place?"
    player "Teehee. Whoops."
    "Suddenly, I hear an unfamiliar voice."
    unknown "{size=+10}OOO, DANG GIRL!{/size}" with vpunch
    player "Huh?"
    "Someone pushes their way past other pokemon and grabs my arm."
    unknown "GIRL, YOUR HAIR..."
    unknown "Don't tell me you haven't noticed!?"
    "I have no idea who this is or why she's talking to me."
    if gender != "girl":
        "And I'm not a girl..."
    player "What are you talking about? Is there something wrong with me?"
    pika "...!"
    pika "Jynx, is that you?"
    jynx "Pikachu, you remember me? We aren't even in the same class!"
    player "...!"
    player "She goes to our school?"
    jynx "Um... yeah..."
    jynx "Haven't you noticed the girl who always attracts attention when she walks through the halls?"
    player "..."
    player "...Who?"
    jynx "..."
    jynx "She doesn't know who I am?"
    pika "[name], this is Jynx. She goes to our school, but she's in a different class."
    player "Nice to meet you... I guess."
    jynx "Nice to meet you too!"
    $ jynx_dex = True
    pdex "Jynx has been added to your Pokedex."
    jynx "Oh, would you look at the time! My shift starts in a few minutes!"
    player "Shift?"
    "Quickly, Jynx grabs my arm and shoves a slip of paper into my hands."
    jynx "Visit me at work sometime, and I'll fix you up all nice and pretty!"
    jynx "[name] is your name, right?"
    player "Y-yeah."
    jynx "Cool!"
    jynx "Catch you later!"
    "What did she give me, anyway?"
    #show paper
    "A coupon?"
    "Hm... \"Salon\"?"
    "What a generic name..."
    "It's almost as if someone just ran out of store names..."
    "I suppose she works there. I'll keep that in mind."
    pika "[name], let's go to the florist."
    pika "I need to pick out a gift."
    player "Hm? For who?"
    pika "..."
    pika "Someone special."
    player "...!"
    "Whoa! Pikachu has a \'special\' someone!"
    "I wonder who it could be?"
    "Wow, Pikachu has grown up so much."
    "And with that, we head to the florist."
    #fade to florist
    jump florist_day1
    
label florist_day1:
    "Upon entering, Pikachu immediately heads towards the roses section."
    "What a romantic choice."
    "Whoever gets those will probably be very happy."
    "As we browse, the florist comes by."
    "Judging by his name tag, his name is Bulbasaur."
    $ bulb_dex = True
    pdex "Bulbasaur has been added to your Pokedex."
    bulb "Would you like any assistance?"
    pika "No thanks, we're fine."
    bulb "Well, if you change your mind, feel free to ask."
    #bulbasaur leaves
    "..."
    "Pikachu seems very deep in thought."
    "He's looking at every single bouquet."
    player "Hey Pikachu, I could help you out."
    pika "Really? That would be great!"
    player "Can you tell me more about this [gender]?"
    pika "Um..."
    pika "It's a secret."
    player "How am I supposed to help you then?"
    pika "Uh... Pick something that you would like."
    player "...?"
    player "Are we similar or something?"
    pika "..."
    pika "You could say that."
    "He went back to looking at the flowers."
    "I wonder who it is?"
    "..."
    "...!"
    "I wonder what kind of flower this is? I've never seen anything like it..."
    "It's even got a different flower pot compared to the rest. Why are there wheels?"
    "The flower itself looks strange too..."
    "It's more like a brown blob. Is this even a flower?"
    "Should I take a closer look?"
    menu:
        "Eh, why not?.":
            "I pick up the flower pot and examine the plant."
            "It's very brown and very smooth... Like one of those hills in Mario, but brown."
            unknown "Hey!"
            unknown "What are you doing!?"
            player "Huh!? Who said that!?"
            unknown "Put me down!"
            player "!!"
            "Is the voice coming from... the plant?"
            "I turn the pot around and..."
            player "!!!!!!"
            "There's a face!?!?"
            player "Are you a Pokemon?"
            unknown "Of course I am; can't you tell!?"
            unknown "I'm Diglett!!"
            $ digl_dex = True
            pdex "Diglett has been added to your Pokedex."
            player "O-Oh, I'm sorry for--"
            digl "You know, there's something called a \"personal bubble\"!"
            digl "And you invaded the bubble!"
            player "Ah, I'm really sorry about--"
            digl "Put me down!!"
            player "O-Oh, uh, okay."
            "I set Diglett back down on the shelf."
            pika "[name], are you okay!?"
            pika "What's wrong? I heard a lot of shouting!"
            player "Oh, it was just--"
            digl "She tried kidnapping me!"
            digl "All I was doing was looking at flowers, and she just grabs me out of nowhere and--"
            player "N-No! I thought he was another plant!"
            digl "\"Another plant\"!? I'm a Pokemon, you idiot!"
            bulb "Hey!! Stop fighting in my store!!"
            bulb "You can argue all you want, but do it outside!"
            player "No, Pikachu needs to buy his roses!"
            digl "...!"
            digl "Roses?"
            digl "Are you buying them for your girlfriend?"
            pika "U-Um, well, not really..."
            pika "It's complicated..."
            digl "D-Do you want help?"
            digl "I can help, if you want..."
            pika "That'd be great. Thank you!"
            digl "I-It's not like I like flowers a lot or anything."
            digl "Especially not enough to study about them..."
            pika "Oh, okay... Well, all help is appreciated."
            digl "What kind of person are you getting these roses for?"
            pika "Um... Come over here and I'll tell you."
            digl "Alright."
            "Diglett rolls off the shelf and lands with a small thud."
            "I wonder how he didn't break?"
            "He rolls towards Pikachu, and they go off talking about roses."
            "They come back a few minutes later."
            digl "Are you serious, man? You want [pronoun1]?"
            digl "Not exactly the kind of [gender] you'd want to date..."
            pika "Hey, don't say that about [pronoun1]."
            pika "I promise, once you get to know [pronoun1]..."
            digl "...Alright dude."
            digl "I respect your wishes, so I'll help you."
            player "Since he's helping you with the roses, is it okay if I look around the mall?"
            pika "Yeah, don't worry about it. Do what you like."
            pika "Just don't get lost, okay? We'll meet up later."
            player "I'm not a little kid!"
            player "..."
            player "Seeya, Homiechu!"
            "I sprint before he can say anything."
            jump see_game_day1
        "I don't want to touch it...":
            "I decide to leave it alone."
            "..."
            "Wait, maybe Pikachu's \'special\' person would actually like this!?"
            "Hmmm..."
            player "Hey, Pikachu."
            pika "Yes, [name]?"
            player "I really have no idea what this [gender] is like."
            player "Tell me more about [pronoun1]."
            pika "U-Um, well, I--"
            player "Like, what's [pos_pronoun] favorite color?"
            player "And [pos_pronoun] favorite food?"
            pika "Probably Pokepu-"
            player "And [pos_pronoun] favorite anime?"
            player "Favorite Pokemon?"
            player "Favorite manga?"
            pika "Um--" #pikachu gets redder and redder with the questions lol
            player "Favorite thing to hug to sleep?"
            pika "Huh--"
            player "Favorite brand of cigarettes?"
            pika "What--"
            player "Favorite recreational drug?"
            pika "[name]!!"
            player "!"
            pika "O-On second thought..."
            pika "Maybe it would be better if I just looked for flowers myself."
            pika "Why don't you go look around the mall for now? We'll meet up later."
            player "Alright, good luck then!"
            player "Seeya!"
            player "..."
            player "Homiechu!"
            "I sprint before he can say anything."
            jump see_game_day1

label see_game_day1:
    if pika_mall:
        "While Pikachu's busy at the florist, I walk around the mall."
        "..."
        "Oh, I just remembered!"
        "Pikabelle Chutendo released a new game a few days ago!"
        "{i}PokeCrossing: Happy Ball Designer!{/i}"
    else:
        "I'm at the mall now!"
    "I've gotta go check out the prices at Gamemon!"
    #fade to gamemon
    player "..."
    player "......"
    player "Where could it be...?"
    player "........."
    player "...!"
    player "Oh my goodness..."
    player "Is that..."
    #picture of the game
    player "{size=+5}{i}THE SUPER SPECIAL LIMITED EDITION {color=#ffd700}GOLD{/color} VERSION OF{/i} POKECROSSING: HAPPY BALL DESIGNER{i} SIGNED BY PIKABELLE CHUTENDO HERSELF FEATURING NEVER-BEFORE-SEEN EXTRA MATERIAL!?{/i}{/size}" with vpunch
    player "...But it's probably going to be expensive..."
    "I briefly close my eyes to say a small prayer."
    player "Please let me have enough money to buy it..."
    "My eyes wander down to the price tag."
    player "*GASP*" with vpunch
    player "*COUGH*" with vpunch
    player "*GAG*" with vpunch
    player "{b}$500!?{/b}"
    player "HOW CAN ANYONE AFFORD THAT?"
    player "BUT..."
    player "BUT...!"
    player "{size=+10}{color=#f00}{i}I NEED THIS GAME!{/i}{/color}{/size}" with vpunch
    player "{size=-5}*pant*...*pant*...{/size}"
    player "EXCUSE ME, STORE CLERK PERSON!!" with vpunch
    gscp "Yes!?"
    gscp "May I help you!?"
    player "I would like for you to reserve this game for me!!"
    player "Right now, I don't have enough money, but..."
    player "I WILL!! I {i}WILL{/i} HAVE ENOUGH MONEY!!" with vpunch
    gscp "Okay, I can reserve it for a week--"
    player "A WEEK!?" with vpunch
    player "I can't possible have enough money by then!"
    player "But... I have to have this item!"
    player "After all, it's..."
    player "{size=+5}{i}THE SUPER SPECIAL LIMITED EDITION {color=#ffd700}GOLD{/color} VERSION OF{/i} POKECROSSING: HAPPY BALL DESIGNER{i} SIGNED BY PIKABELLE CHUTENDO HERSELF FEATURING NEVER-BEFORE-SEEN EXTRA MATERIAL!{/i}{/size}" with vpunch
    player "I would jump over canyons, swim up waterfalls, and walk barefoot over burning coals for this!"
    player "PLEASE, GAMEMON STORE CLERK PERSON!!" with vpunch
    player "DON'T YOU UNDERSTAND!?!?!"
    player "MY ENTIRE LIFE HANGS IN THE BALANCE--" with vpunch
    "Suddenly I feel a hand on my shoulder."
    gscp "...Say no more."
    gscp "I..."
    gscp "I know that feel, bro...!" with vpunch
    if gender != "boy":
        player "{size=-5}...i'm not a boy...{/size}"
    gscp "Don't worry; it's against the rules, but I'll reserve this game for you for a whole month."
    gscp "Sorry, I can't go any longer though."
    "There are a few tears in my eyes."
    "I grasp his hands."
    player "No, dude. It's okay."
    player "Thanks. I'll try my hardest to earn enough money."
    gscp "Wishing you the best."
    "We let go of each other."
    player "Thanks again..."
    "I look at his name tag."
    player "Elekid."
    $ elek_dex = True
    pdex "Elekid has been added to your Pokedex."
    elek "No problem."
    player "There's no way I'll be able to afford that on my own..."
    player "Maybe I have to ask Dad..."
    "Regrettably, I walk out of Gamemon unable to purchase anything."
    "I blink back my tears."
    player "I'll be back for you, {i}PokeCrossing: Happy Ball Designer...{/i}"
    if pika_mall:
        "I guess I should return to Pikachu now..."
        jump pika_return_day1
    else:
        "I guess I'll go home..."
        jump home_return_day1

label pika_return_day1:
    player "Hey Pikachu, I'm back..."
    "Pikachu quickly places something behind a shelf."
    pika "H-Hey, [name]!"
    pika "How was your walk around the mall? Did you find anything interesting?"
    player "Well..."
    player "I saw this game at Gamemon, but it's so..."
    player "{i}expensive.........{/i}"
    "I blink back more tears."
    player "Well anyway..."
    player "Did you pick any flowers yet?"
    pika "Nope. Couldn't find--No--Couldn't decide on--I mean--"
    player "Alright, I guess we'll just come another day."
    pika "Yeah... What a pity... that I couldn't find anything."
    pika "Yeah."
    "Pikachu sure is acting kind of strange."
    "I wonder if there was something that I was supposed to pick up on."
    "Good thing I picked up on {i}that{/i}! Otherwise I would be the oblivious character that everyone hates in manga and anime!"
    "Somehow this cheers me up a little after the whole Gamemon thing."
    player "Let's head home, Pikachu."
    pika "Okay, [name]."
    "We leave the mall and walk home together, talking about our day."
    $ pika_pts += 5
    #fade home
    jump home_return_day1
    
label home_return_day1:
    "Once I get home, I open the door and see my dad sitting on the couch watching TV."
    player "DAD!!"
    dad "Welcome home, [name]."
    player "DAD, I NEED TO TALK TO YOU ABOUT SOMETHING!!!"
    player "IT'S REALLY IMPORTANT!"
    dad "Sure thing, [name]. What is it?"
    player "You know that lady I was talking about earlier? Pikabelle Chutendo?"
    if pika_mall == True:
        player "Well, I didn't go because Pikachu wanted to go the mall, and..."
    player "It turns out that Pikabelle Chutendo released a new game!"
    dad "That's wonderful. Did you get it?"
    player "W-Well, that's the thing..."
    player "You see... It was really expensive."
    player "I don't have enough money, and..."
    dad "Are you asking me for money?"
    player "U-Um... Maybe?"
    dad "[name]. I don't want you to be this kind of person."
    dad "You shouldn't be fully dependent on others to get the things you want."
    player "But... But I'm still young! Aren't I supposed to be financially dependent?"
    dad "That's no excuse!"
    dad "Remember, money doesn't grow on anemones."
    player "Haha, I get it, aneMONEY--"
    dad "Besides the point. You need to get a job!"
    dad "I don't want you to grow up to be an adult who cries at every unaffordable price tag."
    player "But Dad--"
    dad "Uh-uh! You're getting a job, and that's final!"
    dad "You're going to learn what it means to {i}earn{/i} what you want!"
    "Dad looks set on his decision."
    "There's nothing I can do to change his mind at this point."
    player "Okay, Dad..."
    dad "That's a good [gender]."
    dad "Now go get ready for bed. It's getting late, and you don't want to be late to school!"
    "I gasp in horror."
    player "I would {i}never{/i} be late to school!"
    "With that, I go to the bathroom to thoroughly brush and floss my teeth. Hygiene is very important!"
    #add charmeleon event here
    if char_dex and grabbed_tail:
        "Then I text Charmeleon for his Tomodachi-Code."
    elif char_dex and not grabbed_tail:
        "Then I text Charmeleon for his Tomodachi-Code."
        "We play {i}PokeCrossing: New Ball{/i} until late at night."
    else:
        "Then, I lie in bed until falling asleep."
    jump day
    