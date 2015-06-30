# This is the script for the events that occur on Monday, day 1 of PokeDate.
# These appear before the day planner surfaces, as to introduce the player
# to the characters before making any real choices.

label breakfast:
    $ dad_dex1 = True
    "It's the start of a new day."
    "My name is [name], and I'm just a regular human in the pokemon world."
    "When I was 3, I was adopted by a single father."
    "He's the most caring person I know."
    "We eat breakfast together every morning..."

    player "Good morning, Dad!"
    
    dad "Good morning, [name]."
    
    player "Guess what, Dad? Something exciting is happening today!"
    
    dad "How could I forget?"
    dad "It's the special meet-and-greet with the creator of that game you love so much."
    dad "PokeCrossing: New Ball, right?"
    
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
    
    "**SLAM**"
    player "TEACHER...! I AM HERE!!!"
    
    t "Wow, and it's only 8:03AM."
    
    player "I... AM NOT LATE!!!!"
    
    "From the door, I can see my childhood friend, Pikachu, looking worried for me."
    "I flash him a brief thumbs up and wink, as if saying, \"Don't worry, I got this!\""
    "..."
    "Hey, did he just shake his head?"
    
    t "Just take a seat, [name]."
    
    player "WAIT, DID YOU JUST MARK ME LATE--"
    
    t "[name]."
    t "Take a seat."
    
    "She probably didn't mark me late, right?"
    "As I take my seat, the teacher resumes her lecture."
    
    t "Today we will be learning about the First Fundamental Theorem of Calculus."
    
    "..."
    "I rest my head against my hand."
    "..."
    "I still taste some seaweed."
    
    #fade out to lunch
    jump lunch_day1
    
label lunch_day1:
    "DING -- DONG --"
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
            player "Sorry, I have something to do after school."
            
            pika "Really? What is it?"
            
            player "Haven't you heard? Pikabelle Chutendo is coming to the park for an autograph signing session!"
            
            pika "Oh..."
            
            player "Want to come along?"
            
            pika "..."
            pika "Well, I appreciate the offer but..."
            pika "I think I'll pass."
            
            player "Aw... That's too bad."
            player "Let's go to the mall tomorrow then, yeah?"
            
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

label mall_day1: #pikachu introduces you to diglett and jynx
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
    
    unknown "OOO, DANG GIRL!"
    
    player "Huh?"
    
    "Someone pushes their way past other pokemon and grabs my arm."
    
    unknown "GIRL, YOUR HAIR..."
    unknown "Don't tell me you haven't noticed!?"
    
    "I have no idea who this is or why she's talking to me."
    
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
    
    pdex "Jynx has been added to your Pokedex." #pokedex statement
    
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
	#irene is gay
    
    pika "..."
    pika "You could say that."
    
    "He went back to looking at the flowers."
    "I wonder who it is?"