import requests
import config
import random

auth_url = 'https://www.strava.com/api/v3/oauth/token'
url = 'https://www.strava.com/api/v3'

#Map of Jokes
jokes= {
'What did one pirate say to the other when he beat him at chess?':'Checkmatey.',
'I burned 2000 calories today':'I left my food in the oven for too long.',
'I startled my next-door neighbor with my new electric power tool. ':'I had to calm him down by saying \"Don\'t worry, this is just a drill!\"',
'I broke my arm in two places. ':'My doctor told me to stop going to those places.',
'I quit my job at the coffee shop the other day. ':'It was just the same old grind over and over.',
'I never buy anything that has Velcro with it...':'it\'s a total rip-off.',
'I used to work at a soft drink can-crushing company...':'it was soda pressing.',
'I wondered why the frisbee kept on getting bigger. ':'Then it hit me.',
'I was going to tell you a fighting joke...':'but I forgot the punch line.',
'What is the most groundbreaking invention of all time? ':'The shovel. ',
'I\'m starting my new job at a restaurant next week. ':'I can\'t wait.',
'I visited a weight loss website...':'they told me I have to have cookies disabled.',
'Did you hear about the famous Italian chef that recently died? ':'He pasta way.',
'Broken guitar for sale':'no strings attached.',
'I could never be a plumber':'it\'s too hard watching your life\'s work go down the drain.',
'I cut my finger slicing cheese the other day...':'but I think I may have grater problems than that.',
'What time did you go to the dentist yesterday?':'Tooth-hurty.',
'What kind of music do astronauts listen to?':'Neptunes.',
'Rest in peace, boiled water. ':'You will be mist.',
'What is the only concert in the world that costs 45 cents? ':'50 Cent, featuring Nickelback.',
'It\'s not a dad bod':' it\'s a father figure.',
'My wife recently went on a tropical food diet and now our house is full of this stuff. ':'It\'s enough to make a mango crazy.',
'What do you call Santa\'s little helpers? ':'Subordinate clauses.',
'Want to hear a construction joke? ':'Sorry, I\'m still working on it.',
'What\'s the difference between a hippo and a zippo? ':'One is extremely big and heavy, and the other is a little lighter.',
'I burnt my Hawaiian pizza today in the oven, ':'I should have cooked it on aloha temperature.',
'Anyone can be buried when they die':'but if you want to be cremated then you have to urn it.',
'Where did Captain Hook get his hook? ':'From the second-hand store.',
'I am such a good singer that people always ask me to sing solo':'solo that they can\'t hear me. ',
'I am such a good singer that people ask me to sing tenor':'tenor twelve miles away.',
'Occasionally to relax I just like to tuck my knees into my chest and lean forward.':' That\'s just how I roll.',
'What did the glass of wine say to the glass of beer? Nothing. ':'They barley knew each other.',
'I\'ve never trusted stairs. ':'They are always up to something.',
'Why did Shakespeare\'s wife leave him? ':'She got sick of all the drama.',
'I just bought a dictionary but all of the pages are blank. ':'I have no words to describe how mad I am.',
'If you want to get a job at the moisturizer factory... ':'you\'re going to have to apply daily.',
'I don\'t know what\'s going to happen next year. ':'It\'s probably because I don\'t have 2020 vision.',
'Want to hear a joke about going to the bathroom? ':'Urine for a treat.',
'I couldn\'t figure out how to use the seat belt. ':'Then it just clicked.',
'I got an email the other day teaching me how to read maps backwards':'turns out it was just spam.',
'I\'m reading a book about anti-gravity.':' It\'s impossible to put down!',
'You\'re American when you go into the bathroom, and you\'re American when you come out, but do you know what you are while you\'re in there?':' European.',
'Did you know the first French fries weren\'t actually cooked in France?':' They were cooked in Greece.',
'Want to hear a joke about a piece of paper? Never mind... ':'it\'s tearable.',
'I just watched a documentary about beavers. ':'It was the best dam show I ever saw!',
'If you see a robbery at an Apple Store what re you?':' An iWitness?',
'Spring is here! ':'I got so excited I wet my plants!',
'What\'s Forrest Gump\'s password?':' 1forrest1',
'Why did the Clydesdale give the pony a glass of water? ':'Because he was a little horse!',
'CASHIER: \"Would you like the milk in a bag, sir?\" ':'DAD: \"No, just leave it in the carton!\'\"',
'Did you hear about the guy who invented Lifesavers? ':'They say he made a mint.',
'I bought some shoes from a drug dealer.':' I don\'t know what he laced them with, but I was tripping all day!',
'Why do chicken coops only have two doors?':' Because if they had four, they would be chicken sedans!',
'How do you make a Kleenex dance? ':'Put a little boogie in it!',
'A termite walks into a bar and asks':'\"Is the bar tender here?\"',
'Why did the invisible man turn down the job offer?':' He couldn\'t see himself doing it.',
'I used to have a job at a calendar factory ':'but I got the sack because I took a couple of days off.',
'A woman is on trial for beating her husband to death with his guitar collection. Judge says, \"First offender?\" ':'She says, \"No, first a Gibson! Then a Fender!\"',
'How do you make holy water?':' You boil the hell out of it.',
'I had a dream that I was a muffler last night.':' I woke up exhausted!',
'Did you hear about the circus fire?':' It was in tents!',
'Don\'t trust atoms.':' They make up everything!',
'How many tickles does it take to make an octopus laugh? ':'Ten-tickles.',
'I\'m only familiar with 25 letters in the English language.':' I don\'t know why.',
'Why did the cow in the pasture get promoted at work?':' Because he is OUT-STANDING in his field!',
'What do prisoners use to call each other?':' Cell phones.',
'Why couldn\'t the bike standup by itself? ':'It was two tired.',
'Who was the fattest knight at King Arthur\'s round table?':' Sir Cumference. ',
'Did you see they made round bails of hay illegal in Wisconsin? ':'It\'s because the cows weren\'t getting a square meal.',
'You know what the loudest pet you can get is?':' A trumpet.',
'What do you get when you cross a snowman with a vampire?':' Frostbite.',
'What do you call a deer with no eyes?':' No idea!',
'Can February March? ':'No, but April May!',
'What do you call a lonely cheese? ':'Provolone.',
'Why can\'t you hear a pterodactyl go to the bathroom?':' Because the pee is silent.',
'What did the buffalo say to his son when he dropped him off at school?':' Bison.',
'What do you call someone with no body and no nose? ':'Nobody knows.',
'You heard of that new band 1023MB? ':'They\'re good but they haven\'t got a gig yet.',
'Why did the crab never share?':' Because he\'s shellfish.',
'How do you get a squirrel to like you? ':'Act like a nut.',
'Why don\'t eggs tell jokes? ':'They\'d crack each other up.',
'Why can\'t a nose be 12 inches long? ':'Because then it would be a foot.',
'Did you hear the rumor about butter? ':'Well, I\'m not going to spread it!',
'I made a pencil with two erasers. ':'It was pointless.',
'I used to hate facial hair...':'but then it grew on me.',
'I decided to sell my vacuum cleaner—':'it was just gathering dust!',
'I had a neck brace fitted years ago':' and I\'ve never looked back since.',
'You know, people say they pick their nose,':' but I feel like I was just born with mine.',
'What do you call an elephant that doesn\'t matter?':' An irrelephant.',
'What do you get from a pampered cow? ':'Spoiled milk.',
'It\'s inappropriate to make a \'dad joke\' if you\'re not a dad.':' It\'s a faux pa.',
'How do lawyers say goodbye? ':'Sue ya later!',
'Wanna hear a joke about paper? ':'Never mind—it\'s tearable.',
'What\'s the best way to watch a fly fishing tournament? ':'Live stream.',
'I could tell a joke about pizza,':' but it\'s a little cheesy.',
'When does a joke become a dad joke?':' When it becomes apparent.',
'What\'s an astronaut\'s favorite part of a computer? ':'The space bar.',
'What did the shy pebble wish for?':'That she was a little boulder.',
'I\'m tired of following my dreams. ':'I\'m just going to ask them where they are going and meet up with them later.',
'Did you hear about the guy whose whole left side was cut off? ':'He\'s all right now.',
'Why didn\'t the skeleton cross the road? ':'Because he had no guts.',
'What did one nut say as he chased another nut? ':' I\'m a cashew!',
'Chances are if you\' ve seen one shopping center...':' you\'ve seen a mall.',
'I knew I shouldn\'t steal a mixer from work...':'but it was a whisk I was willing to take.',
'How come the stadium got hot after the game? ':'Because all of the fans left.',
'Why was it called the dark ages? ':'Because of all the knights. ',
'Why did the tomato blush? ':'Because it saw the salad dressing.',
'Did you hear the joke about the wandering nun? ':'She was a roman catholic.',
'What creature is smarter than a talking parrot? ':'A spelling bee.',
'I\'ll tell you what often gets over looked...':' garden fences.',
'Why did the kid cross the playground? ':'To get to the other slide.',
'Why do birds fly south for the winter?':' Because it\'s too far to walk.',
'What is a centipedes\'s favorite Beatle song? ':' I want to hold your hand, hand, hand, hand...',
'My first time using an elevator was an uplifting experience. ':'The second time let me down.',
'To be Frank...':' I\'d have to change my name.',
'Slept like a log last night … ':'woke up in the fireplace.',
'Why does a Moon-rock taste better than an Earth-rock? ':'Because it\'s a little meteor.',
'How many South Americans does it take to change a lightbulb?':' A Brazilian',
'I don\'t trust stairs.':' They\'re always up to something.',
'A police officer caught two kids playing with a firework and a car battery.':' He charged one and let the other one off.',
'What is the difference between ignorance and apathy?':'I don\'t know and I don\'t care.',
'I went to a Foo Fighters Concert once... ':'It was Everlong...',
'Some people eat light bulbs. ':'They say it\'s a nice light snack.',
'What do you get hanging from Apple trees? ':' Sore arms.',
'Last night me and my girlfriend watched three DVDs back to back.':' Luckily I was the one facing the TV.',
'I got a reversible jacket for Christmas,':' I can\'t wait to see how it turns out.',
'What did Romans use to cut pizza before the rolling cutter was invented? ':'Lil Caesars',
'My pet mouse \'Elvis\' died last night. ':'He was caught in a trap..',
'Never take advice from electrons. ':'They are always negative.',
'Why are oranges the smartest fruit? ':'Because they are made to concentrate. ',
'What did the beaver say to the tree? ':'It\'s been nice gnawing you.',
'How do you fix a damaged jack-o-lantern?':' You use a pumpkin patch.',
'What did the late tomato say to the early tomato? ':'I\'ll ketch up',
'I have kleptomania...':'when it gets bad, I take something for it.',
'I used to be addicted to soap...':' but I\'m clean now.',
'When is a door not a door?':' When it\'s ajar.',
'I made a belt out of watches once...':' It was a waist of time.',
'This furniture store keeps emailing me,':' all I wanted was one night stand!',
'How do you find Will Smith in the snow?':'  Look for fresh prints.',
'I just read a book about Stockholm syndrome.':' It was pretty bad at first, but by the end I liked it.',
'Why do trees seem suspicious on sunny days? ':'Dunno, they\'re just a bit shady.',
'If at first you don\'t succeed':' sky diving is not for you!',
'What kind of music do mummy\'s like?':'Rap',
'A book just fell on my head. ':'I only have my shelf to blame.',
'What did the dog say to the two trees? ':'Bark bark.',
'If a child refuses to sleep during nap time...':' are they guilty of resisting a rest?',
'Have you ever heard of a music group called Cellophane?':' They mostly wrap.',
'What did the mountain climber name his son?':'Cliff.',
'Why should you never trust a pig with a secret?':' Because it\'s bound to squeal.',
'Why are mummys scared of vacation?':' They\'re afraid to unwind.',
'Whiteboards ...':' are remarkable.',
'What kind of dinosaur loves to sleep?':'A stega-snore-us.',
'What kind of tree fits in your hand?':' A palm tree!',
'I used to be addicted to the hokey pokey':' but I turned myself around.',
'How many tickles does it take to tickle an octopus?':' Ten-tickles!',
'What musical instrument is found in the bathroom?':' A tuba toothpaste.',
'My boss told me to attach two pieces of wood together... ':'I totally nailed it!',
'What was the pumpkin\'s favorite sport?':'Squash.',
'What do you call corn that joins the army?':' Kernel.',
'I\'ve been trying to come up with a dad joke about momentum ':'but I just can\'t seem to get it going.',
'Why don\'t sharks eat clowns? ':' Because they taste funny.',
'Just read a few facts about frogs.':' They were ribbiting.',
'Why didn\'t the melons get married?':'Because they cantaloupe.',
'What\'s a computer\'s favorite snack?':'Microchips!',
'Why was the robot so tired after his road trip?':'He had a hard drive.',
'Why did the computer have no money left?':'Someone cleaned out its cache!',
'I\'m not anti-social. ':'I\'m just not user friendly.',
'Why did the computer get cold?':'Because it forgot to close windows.',
'What is an astronaut\'s favorite key on a keyboard?':'The space bar!',
'What\'s the difference between a computer salesman and a used-car salesman?':'The used-car salesman KNOWS when he\'s lying.',
'If at first you don\'t succeed...':' call it version 1.0',
'Why did Microsoft PowerPoint cross the road?':'To get to the other slide!',
'What did the computer do at lunchtime?':'Had a byte!',
'Why did the computer keep sneezing?':'It had a virus!',
'What did one toilet say to the other?':'You look a bit flushed.',
'Why did the picture go to jail?':'Because it was framed.',
'What did one wall say to the other wall?':'I\'ll meet you at the corner.',
'What do you call a boy named Lee that no one talks to?':'Lonely',
'Why do bicycles fall over?':'Because they are two-tired!',
'Why was the broom late?':'It over swept!',
'What part of the car is the laziest?':'The wheels, because they are always tired!',
'What\'s the difference between a TV and a newspaper?':'Ever tried swatting a fly with a TV?',
'What did one elevator say to the other elevator?':'I think I\'m coming down with something!',
'Why was the belt arrested?':'Because it held up some pants!',
'What makes the calendar seem so popular?':'Because it has a lot of dates!',
'Why did Mickey Mouse take a trip into space? ':' He wanted to find Pluto!',
'Why do you go to bed every night?':'Because the bed won\'t come to you!',
'What has four wheels and flies?':'A garbage truck!',
'Why did the robber take a bath before he stole from the bank?':'He wanted to make a clean get away!',
'Just watched a documentary about beavers.':'It was the best damn program I\'ve ever seen.',
'Slept like a log last night':'woke up in the fireplace.',
'Why did the scarecrow win an award?':'Because he was outstanding in his field.',
'Why does a chicken coop only have two doors? ':'Because if it had four doors it would be a chicken sedan.',
'What\'s the difference between an African elephant and an Indian elephant? ':'About 5000 miles',
'Why did the coffee file a police report? ':'It got mugged.',
'What did the grape do when he got stepped on? ':'He let out a little wine.',
'How many apples grow on a tree? ':'All of them.',
'What name do you give a person with a rubber toe? ':'Roberto',
'Did you hear about the kidnapping at school? ':'It\'s fine, he woke up.',
'Why do scuba divers fall backwards into the water? ':'Because if they fell forwards they\'d still be in the boat.',
'How does a penguin build it\'s house? ':'Igloos it together.',
'What do you call a man with a rubber toe?':'Roberto',
'Did you hear about the restaurant on the moon?':'Great food, no atmosphere.',
'Why was the belt sent to jail?':'For holding up a pair of pants!',
'Did you hear about the scientist who was lab partners with a pot of boiling water?':'He had a very esteemed colleague.',
'What happens when a frogs car dies?':'He needs a jump. If that doesn\'t work he has to get it toad.',
'What did the flowers do when the bride walked down the aisle?':'They rose.',
'Why did the man fall down the well?':'Because he couldn\'t see that well.',
'My boss told me to have a good day...':'...so I went home.',
'How can you tell it\'s a dogwood tree?':'By the bark.',
'Did you hear about the kidnapping at school?':'It\'s fine, he woke up.',
'Why is Peter Pan always flying?':'Because he Neverlands.',
'Which state has the most streets?':'Rhode Island.',
'What do you call 26 letters that went for a swim?':'Alphawetical.',
'Why was the color green notoriously single?':'It was always so jaded.',
'Why did the coach go to the bank?':'To get his quarterback.',
'How do celebrities stay cool?':'They have many fans.',
'What\'s the most depressing day of the week?':'sadder day.',
'Dogs can\'t operate MRI machines':'But catscan.',
'I was going to tell a time-traveling joke':'but you guys didn\'t like it.',
'Stop looking for the perfect match':'instead look for a lighter.',
'I told my doctor I heard buzzing':'but he said it\'s just a bug going around.',
'What kind of car does a sheep like to drive?':'A lamborghini.',
'What did the accountant say while auditing a document?':'This is taxing.',
'What did the two pieces of bread say on their wedding day?':'It was loaf at first sight.',
'Why do melons have weddings?':'Because they cantaloupe.',
'What did the drummer call his twin daughters?':'Anna One, Anna Two!',
'What do you call a toothless bear?':' A gummy bear!',
'Two goldfish are in a tank. ':'One says to the other, Do you know how to drive this thing?',
'What\'s Forrest Gump\'s password?':'1forrest1',
'What is a child guilty of if they refuse to nap?':' Resisting a rest.',
'I know a lot of jokes about retired people':'but none of them work.',
'Why are spiders so smart?':'They can find everything on the web.',
'What has one head, one foot, and four legs?':' A bed.',
'What does a house wear?':' Address.',
'What\'s red and smells like blue paint?':'Red paint.',
'My son asked me to put his shoes on':' but I don\'t think they\'ll fit me.',
'I\'ve been bored recently, so I decided to take up fencing.':' The neighbors keep demanding that I put it back.',
'What do you call an unpredictable camera?':'A loose Canon.',
'Which U.S. state is known for its especially small soft drinks?':'Minnesota.',
'What do sprinters eat before a race?':' Nothing—they fast.',
'I\'m so good at sleeping...':'I can do it with my eyes closed.',
'People are usually shocked that I have a Police record.':'But I love their greatest hits!',
'I told my girlfriend she drew on her eyebrows too high.':' She seemed surprised.',
'What do you call a fibbing cat?':' A lion.',
'Why shouldn\'t you write with a broken pencil?':' Because it\'s pointless.',
'I like telling Dad jokes…':'sometimes he laughs.',
'How do you weigh a millennial?':' In Instagrams.',
'The wedding was so beautiful':'even the cake was in tiers.',
'What\'s the most patriotic sport?':' Flag football.'
}

#For initial authorization
# payload = {
#     'client_id' : config.client_id,
#     'client_secret': config.client_secret,
#     'grant_type':'authorization_code',
#     'code': config.code
# }

#Method for getting the most recent activity and appending a joke from the list
#to the description
def update_joke(): 
    #Retrieving refresh token
    payload = {
        'client_id' : config.client_id,
        'client_secret': config.client_secret,
        'grant_type':'refresh_token',
        'refresh_token': config.refresh_token
    }
    response = requests.post(
        auth_url,
        data=payload,
    )
    access_token = response.json()['access_token']

    #Getting first (most recent) activity id
    headers= {
        'Authorization': 'Bearer ' + access_token 
    }
    param = {
    'page': 1,
    'per_page': 1
    }
    response = requests.get(
        url+'/athlete/activities',
        headers=headers,
        params=param
    )
    activity_id = response.json()[0]['id']

    #Get current description
    headers= {
        'Authorization': 'Bearer ' + access_token 
    }
    response = requests.get(
        url+'/activities/'+str(activity_id),
        headers=headers,
    )
    current_description = response.json()['description']

    #If description is empty, set it to an empty string
    if current_description is None:
        current_description = ''

    #Updating activity description
    setup = str(random.choice(list(jokes.keys())))
    punchline = str(jokes[setup]).strip()
    setup = setup.strip()
    headers= {
        'Authorization': 'Bearer ' + access_token 
    }
    updatableActivity = {
        'description': '🤡 Joke of the day 🤡\n' + setup + '\n' + punchline + '\n- by Joke.py' + '\n\n' + current_description
    }

    #If there is already a joke in the current run, don't put another.
    if('🤡 Joke of the day 🤡' not in current_description):
        response = requests.put(
            url+'/activities/'+str(activity_id),
            headers=headers,
            params=updatableActivity
        )

#Calling method for testing (if you want to just run the joke.py file)
update_joke()
