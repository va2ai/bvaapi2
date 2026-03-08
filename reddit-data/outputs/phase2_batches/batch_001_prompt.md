# Prompt 1: Need Extraction

You are a market research analyst specializing in the U.S. veteran community.
I’m going to give you a batch of Reddit posts and comments from veteran subreddits.
For each post, identify:
1. PRIMARY NEED: What is the veteran trying to accomplish or solve?
2. PAIN POINTS: What specific frustrations or blockers do they describe?
3. CURRENT SOLUTION: What are they currently doing to solve this? (DIY, paid service, nothing?)
4. EMOTIONAL INTENSITY: Rate 1–5 (1=mild inconvenience, 5=desperate/life-impacting)
5. CATEGORY: Assign one: Claims/Ratings, Appeals, Healthcare, Mental Health,
   Employment/Transition, Education/GI Bill, Housing/VA Loan, Financial, Legal,
   Community/Social, Other.

Output strictly as a JSON array, one object per post.

## Input JSON

```json
[
  {
    "subreddit": "disability",
    "id": "1qozcjc",
    "title": "To the lady who tried to turn in my \u201clost\u201d cane to the bus driver: disabled people look like this.",
    "body": "Just a goofy story to interrupt the drudgery of everything (especially here in the US, sheesh). \n\nI got on the bus at the terminal but was last in the line, and everyone in the accessible seats needed them more than me so I scooted up the stupid bus stairs and sat wayyy in the back. This seat had space behind it so I wedged my cane behind it using my backpack to make sure it wouldn\u2019t go flying if the bus suddenly braked. \n\nThis lady gets on a few stops after and sits on the seats across from my seat, so she\u2019s facing me and apparently saw my cane behind me. After about 20 minutes she stands up at a stop and I think she\u2019s leaving, but she approaches me. I\u2019m like uhhh? She doesn\u2019t even look at me before reaching OVER, not around, and not saying \u201cexcuse me\u201d or anything polite like that. Just OVER me with my face in her whole armpit and side of her boob while she tries to untangle my cane from my backpack straps. Which she does, and then tries to walk to the front of the bus with my cane (a nice one, mind you!). She only got as far as she did because I was so shocked??? Like I get I don\u2019t necessarily look disabled while seated but like. ?????  It was RIGHT NEXT TO ME. Tangled up in what is clearly MY BACKPACK (it\u2019s very visually apparent the backpack is mine). This lady must have made some wild assumptions about me to not say \u201cexcuse me is this your bag, and can you move it so I can give this lost walking cane to the bus driver?\u201d Like she fully leaned over my body to grab my cane, and wiggle it around to get the foot out from under my backpack to lift over my head and deliver to the bus driver. \n\nSo obviously I LOUDLY said \u201cuhm can I have my cane back please?\u201d Because I\u2019m a meek human and was super tired from classes, but also didn\u2019t really process anything besides this stranger taking my mobility aid after being FAR more privy to her upper half than I cared to be, and I say that as a certified queer. Like lady I love the bajingas in general but gimme some SPACE yanno? \n\nShe immediately gave it back and explained she thought it was left behind by somebody who looks more like they\u2019d use a cane than I do, and sat down and didn\u2019t look away from the window until she got off the bus (another 10ish minutes). \n\nSo lady, for one, chill the fuck out on public transit lol. For two, TALK to people! Like even making the assumption that it was left by somebody else, if it\u2019s clearly underneath another person\u2019s item, SAY something. Again, she rangjangled my cane around for like 10 seconds. That is a LONG time to be bent over a stranger on a fucking public bus. My face was in her sweaty side boob for 10 seconds and I DIDNT LIKE IT. For three, I get you\u2019re embarrassed after trying to do something good that was not good, but ya gotta let it go girl. I really hope once you got off the bus you focused on more important things, but retained the memory enough to fucking ASK before grabbing the mobility devices of cute, stylish ladies because you assume disabled people can\u2019t look this good. \n\nPhoto bc this is what I looked like on the bus when this lady assumed I wasn\u2019t disabled enough to use a cane that was beneath my backpack, directly behind me, about 6\u201d away. Also, disabled people can be hot and cute and stylish. There is no way to LOOK disabled. I\u2019m sick to death of getting sneers and looks because I use some of my little energy on looking the way that I want to. I go in public twice a week and wanna look good and I use some energy on that. I already saved all that energy for that day! I\u2019m going to USE IT! I\u2019m adorable AND I\u2019m disabled and I\u2019m fucking angry. ",
    "flair": null,
    "score": 1903,
    "comment_count": 153,
    "created_at": "2026-01-28T02:55:49+00:00",
    "top_comments": [
      {
        "id": "o25fvoh",
        "score": 488,
        "body": "I had someone tell me that I didn\u2019t need my cane in a waiting room last week."
      },
      {
        "id": "o25gm80",
        "score": 236,
        "body": "Wow! They have X-ray vision? I\u2019m so impressed! /s \n\n(I hate people like that. Like who even are you to get to make that assumption)"
      },
      {
        "id": "o25rwp6",
        "score": 182,
        "body": "I've noticed that a lot of able-bodied people feel weirdly entitled to touching disability aids. There are way too many stories of people in wheelchairs being pushed or moved by total strangers who don't ask for permission at all. Disappointing but not surprising that canes are treated the same way :/"
      },
      {
        "id": "o25gdx6",
        "score": 175,
        "body": "It's such a bad feeling and incredibly stressful. I hope you're recovering from that interaction, and i'm sorry that happened to you.\n\nI'm 25 and I alternate between using a cane and forearm crutches. I've had something similar happen to me and it's just like this person is running off with my autonomy and i'm just internally screaming and praying it'll come right back.\n\nWhen i have two forearm crutches and need a hand to use, i'll lean my left crutch against my chair/table. My crutches match each other and have spiderweb decals on them. Was in a restaurant (i was 23 at the time i think) and needed to use a hand to pay. Sat my crutch at the table my friends and i were going to be using (with our bags and winter coats on it too). Went to order and pay and turned around to see a woman *bolting* towards the door with my crutch??? Literally sprinting. We hollered at her to wait. She had made it out the door, but heard and came back. She was mortified and explained that she had thought the older man who had recently walked out had forgotten it. He didn't even have a cane or anything, she just assumed mobility aid = elderly."
      },
      {
        "id": "o25x4yg",
        "score": 171,
        "body": "My disability wouldn\u2019t even show up with X-Ray vision.  I use a cane for vertigo and vision."
      },
      {
        "id": "o25a8xj",
        "score": 85,
        "body": "That's fucking horrible. Are you OK?"
      },
      {
        "id": "o2674ih",
        "score": 82,
        "body": "I use a rollator for vertigo and joint subluxation and I also have our vision. Explaining to people that you don't need it to go short distances into places with chairs, but that you do need it to do a lap around the mall is difficult. And if you so much as let go of the handles once, you must be faking, obviously. I'm glad my vision sucks enough that I don't see all the dirty looks, but my family catches them sometimes."
      },
      {
        "id": "o25iq0l",
        "score": 73,
        "body": "Yes you are beautiful and that must have been infuriating and your story gave me a much needed laugh.\nAvast, sweaty side-boobs!\nSeriously. There should be a troop of disabled comedians sharing stories about ridiculous ableist people/ events/ architecture \nIn the same general style of \n\"The Axis of Evil Comedy Tour\""
      },
      {
        "id": "o260sjs",
        "score": 70,
        "body": "Thats so wild bc wouldn't it be easier to assume that the old man walking fine with no mobility aids doesn't use the mobility aid?? Lmao?"
      },
      {
        "id": "o262x8j",
        "score": 64,
        "body": "For real. Not to mention the fact that i was actively using the matching crutch, lol. \n\nThough if i ignore the dread i felt/the actual situation here, it was kind of her. She didn't want an ambulatory user to forget his crutch and was willing to sprint through the heavy snow to make sure he had it. Kindness was certainly the intention, but panic was the impact lol."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1maabdr",
    "title": "My best friend found me this button at a vintage store",
    "body": "",
    "flair": "Image",
    "score": 1523,
    "comment_count": 54,
    "created_at": "2025-07-27T01:49:58+00:00",
    "top_comments": [
      {
        "id": "n5d9idc",
        "score": 119,
        "body": "Then you haven't thrown one at a doctor hard enough."
      },
      {
        "id": "n5dk7mc",
        "score": 47,
        "body": "\"Any chrystal can repel negativity - if you throw it hard enough\" \n\nBeen meaning to cross-stitch that, thx for the reminder"
      },
      {
        "id": "n5d6ump",
        "score": 39,
        "body": "Lol great button.\n\nAlso love your tattoos! That flower on your bicep is beautiful but I love the mix of styles!"
      },
      {
        "id": "n5dienr",
        "score": 36,
        "body": "I\u2019m also a power wheelchair user and I have an apple allergy which makes this hilarious on so many levels\ud83d\ude06"
      },
      {
        "id": "n5ddxco",
        "score": 24,
        "body": "thank you! I really like going to a bunch of different people and telling them to do whatever it always comes out so cool!"
      },
      {
        "id": "n5djata",
        "score": 16,
        "body": "Dude you need this pin"
      },
      {
        "id": "n5de1zx",
        "score": 14,
        "body": "the tattoos or the bulging muscles? ( thank you lol)"
      },
      {
        "id": "n5mwi9m",
        "score": 9,
        "body": "I fucking love this \ud83e\udd23"
      },
      {
        "id": "n5dfsbe",
        "score": 8,
        "body": "Love the button, love the fit, love the tattoos, SLAY \ud83d\udd25\ud83e\ude75"
      },
      {
        "id": "n5ff66q",
        "score": 8,
        "body": "I\u2019m gonna see if I can find it online \ud83d\ude06 P.S. your tattoos are so cool!!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1l438mf",
    "title": "Shoutout to all the disabled parents finding ways to adapt.",
    "body": "he loves falling asleep in the chair. ",
    "flair": "Image",
    "score": 1521,
    "comment_count": 79,
    "created_at": "2025-06-05T16:13:03+00:00",
    "top_comments": [
      {
        "id": "mw5qxka",
        "score": 235,
        "body": "Omg girl I\u2019m literally pregnant with my first,\nAnd I use a wheelchair completely lack the ability to walk, I\u2019m scared sometimes but seeing people like you sharing your pictures/stories really, really give me hope that it\u2019s going to be okay \ud83d\udc95"
      },
      {
        "id": "mw5tjk4",
        "score": 163,
        "body": "I have figured out so much- i actually own this strap that goes around your waist with velcro. it won\u2019t be useful until your baby can sit up but if you DM me your address I will mail you it for your baby. it helped me SO much. it kept him secure to my lap, it has clips for toys so he can\u2019t throw them. If your not comfortable giving a stranger your address here\u2019s a link to it:\n\n[Baby Chair Strap](https://www.primobaby.com/products/primo-lapbaby?utm_source=chatgpt.com)"
      },
      {
        "id": "mw5u0d7",
        "score": 59,
        "body": "I will definitely send you my address!! Thank you so so much, I have so much to learn and I think there aren\u2019t a lot of things out there to help parents adapt when disabled so I can t thank you enough for showing me!"
      },
      {
        "id": "mw5q1wi",
        "score": 47,
        "body": "You go, mama. That little one looks so comfortable and loved. You\u2019re doing great, you got this!"
      },
      {
        "id": "mw6gf9p",
        "score": 45,
        "body": "I'm not sure it'll be a good idea for me to have kids (pregnancy is riskier for me and might disable me more, potentially resulting in me becoming a wheelchair user) but seeing disabled parents is huge for me. \n\nWe already have limited visibility and representation. I had such little and such ableist representation growing up. Disabled parents? Vastly less representation. \n\nI grew up with able-bodied, white, married, middle-upper\u2013class parents. I always assumed that one day, my disability (I knew only about my birth nerve injury in my left arm for most of my life) would just become manageable. I'd just *figure it out* somehow and live the \"normal\" lives that my parents did. My disabilities got worse, and I developed more of them. *Hello, fibromyalgia. Hate to know you.* \n\nSo, now, in my mid-20s, I'm fighting with this lifelong desire to be a parent, and realizing that it *will* look and function extremely different than expected, and that's if it's even feasible for me. I follow as many disabled parents as I can find on social media. I want to see the beauty and pains of that. I want to see the ups and downs and the NORMAL LIFE of disabled parents. \n\nSo, yes, shoutout to all the disabled parents finding ways to adapt. You are serving as an inspiration to disabled people like me, not for \"overcoming\" your disabilities (\ud83e\udd74), but for charting your path despite the fact that society hates disabled parents."
      },
      {
        "id": "mw5s7bu",
        "score": 27,
        "body": "Yes to this but also you are STUNNING!!!\n\nEdit: I\u2019m not a parent myself but follow a lot of disabled content creators, some of which are moms!! It drives me nuts the ignorance of people who are incapable of understanding disabled people can have kids (no, I\u2019m not kidding) and some of the rude things these women deal with. It makes me angry! People just out here casually suggesting eugenics, without a clue for how it sounds. It\u2019s angering"
      },
      {
        "id": "mw6ojlj",
        "score": 21,
        "body": "My mom became disabled when I was young due to disease.  I wouldn't have traded her for the world.  Now I am disabled when my son is young.  She was very active, I was very active.\n\nI still spend time with my son.  I don't get to hike with him anymore, or ride bikes and stuff, but I sit and watch him ride his bike.  I play other games with him, etc.  Do I wish it was different, yeah, would I change my life with him, no.\n\nHe does tell me we can go hiking when the doctors fix my legs, which is a bit sad, but you got to play the cards you are dealt with in life."
      },
      {
        "id": "mw6mug0",
        "score": 19,
        "body": "YES!! You do have my exact chair (i love it, good battery life, easy for transport plus the company is amazing!). And my joystick cover is from [Granted Engineering](https://www.etsy.com/shop/GrantedEngineering)He did such a good job for me. I ordered a custom rose and it didn\u2019t turn out well becuase of the colors i chose, not his fault. But the next time i ordered he sent a complimentary joystick cover (an adorable koala). He\u2019s just a really nice guy."
      },
      {
        "id": "mw5pz50",
        "score": 18,
        "body": "My daughter loves to tickle fight even though she knows I can't feel my paralyzed arm and is more an excuse for me to tickle her with my good arm."
      },
      {
        "id": "mw5vpk2",
        "score": 18,
        "body": "Thank you. I definitely prepared for this with getting my brows and eyeliner tattooed on knowing i was going to be tired with another baby in the house again lol. I really respect those creators because i watch them but i could never do it. before i got this far down being sick i had been on social media for veterans nonprofit stuff (im an army veteran) but once i got ill i got off of everything but reddit. takes a lot of effort and strength to maintain that."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1mf7zqm",
    "title": "Thought You Should Be Aware.",
    "body": "Given that most of us are already in enough systems, I thought we should be aware of this info. Be safe, my friends.",
    "flair": "Article / News",
    "score": 1456,
    "comment_count": 130,
    "created_at": "2025-08-01T20:54:54+00:00",
    "top_comments": [
      {
        "id": "n6f5rgc",
        "score": 183,
        "body": "The only thing I trust more than the government is a private tech comp- ahahahahaha. Couldn't even finish the sentence.\n\nTotally not fascist though /s\n\nSeriously, capitalism is a perfect vehicle for eugenics. We all know where this leads."
      },
      {
        "id": "n6fdjb5",
        "score": 114,
        "body": "the fact that this is happening again so soon and people are fucking falling for it is so depressing to me. I was a small child during the beginning of the AIDS epidemic and even I know this shit; to see people older than me, who should know better, falling for this just makes me so sad."
      },
      {
        "id": "n6fna85",
        "score": 107,
        "body": "When the SCOTUS removed abortion protection, I downloaded the app to track your pregnancy and told it I was pregnant. I\u2019m a dude\u2026 because fuck those guys!"
      },
      {
        "id": "n6fuf2i",
        "score": 75,
        "body": "That's actually a genuine way to fight back, sort of. Fucking up data sets can be very important"
      },
      {
        "id": "n6fehmk",
        "score": 68,
        "body": "I believe that Palantir has been given Medicaid records by the Republican Administration, so I'd say they already have. I refuse to use any tracking apps for periods.steps walked/food/etc., but some people are apparently fine with handing over info to easily hacked sites."
      },
      {
        "id": "n6fdz5u",
        "score": 62,
        "body": "So basically HIPAA is about to go out the window?"
      },
      {
        "id": "n6fe22z",
        "score": 58,
        "body": "It is frightening how quickly people forget."
      },
      {
        "id": "n6fjdta",
        "score": 50,
        "body": "Not everything should be privatized"
      },
      {
        "id": "n6f6vce",
        "score": 50,
        "body": "Too bloody right."
      },
      {
        "id": "n6gq9gv",
        "score": 44,
        "body": "I love that you did that! When Trump banned Muslims from entering the country, I wore a Hajib for a long while. I had it in my mind that if we all presented as Muslims....oh, who knows. I didn't have the power/influence to get others on board."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1m8zsp8",
    "title": "Just saw the best thing, have a good laugh today!",
    "body": "",
    "flair": "Image",
    "score": 1334,
    "comment_count": 77,
    "created_at": "2025-07-25T13:54:34+00:00",
    "top_comments": [
      {
        "id": "n53agtw",
        "score": 169,
        "body": "\"You don't look dis- ** ZAAAAAP ** oh god...oh god no...how can I live like this? AND WHY IS THE SUN SO LOUD?!\""
      },
      {
        "id": "n538u16",
        "score": 166,
        "body": "honestly i just wish more people who suffered with disabilities could be doctors, people should understand what it's like to live with disability before treating it (and that's true whether they've been through it personally or not)"
      },
      {
        "id": "n53d537",
        "score": 90,
        "body": "The best physician I ever had was disabled yeah"
      },
      {
        "id": "n53d2wa",
        "score": 86,
        "body": "I wouldn't mind letting my first neurologist live for a month with my illness\n\nhe might learn some humility after having to literally crawl out of bed let alone crawl anywhere until he figures out how to stand up"
      },
      {
        "id": "n53rqvt",
        "score": 78,
        "body": "I would love to see more people with disabilities enter medical careers, but I am not convinced that it will result in empathy because there are plenty of people with disabilities who are either infected with toxic positivity or self-loathing."
      },
      {
        "id": "n53v7x1",
        "score": 50,
        "body": "I\u2019ve seen those videos of guys wearing those electromagnetic machines that simulate period cramps so I guess the doctor can wear that \ud83d\ude02"
      },
      {
        "id": "n54s9w0",
        "score": 34,
        "body": "only need to look at the tx governor on this one"
      },
      {
        "id": "n5478j7",
        "score": 33,
        "body": "Oh wow I wish this existed!  I just dealt with a cardiologist who wasn\u2019t interested at all in my medical history (multiple autoimmune conditions, Cushing\u2019s syndrome from steroids, etc.) and yes, I\u2019m obese because I was on prednisone for 2.5 years!  He kept using the phrase \u201cpeople like you\u201d and recommended I lose weight in way that implied I\u2019d never thought of that.  I\u2019m in constant pain and can barely move sometimes but I don\u2019t sit around all day eating bon bons.  The exercise I do get comes at a great cost in terms of pain and anguish but I do it.  Anyway, my heart was fine and I\u2019m glad i won\u2019t be dealing with that asshole anymore but I kept wishing there was some way to make him understand what it\u2019s like to be me."
      },
      {
        "id": "n56x0ei",
        "score": 23,
        "body": "My first rheumatologist would need at least a year or two, and even that wouldn't work if he knew it would end. Dude read this one study on fibromyalgia and actually said I could run a marathon if I just really wanted to because I'm not really in pain, my brain is just telling me I'm in pain (neurologically not mentally). I said so those people with that rare disease where they can't feel pain, like they can cut off a limb or burn themselves and not feel anything -- they're actually lying then, they're in excruciating pain but their brain is just telling them they're not? We feel what our brain says we feel. (You can't acknowledge their lack of pain but ignore our pain because you think it's faulty nerve signals or whatever.)"
      },
      {
        "id": "n54dreh",
        "score": 20,
        "body": "I have complained about this at length to my partner, about able-bodied people making decisions for disabled people, not having an understanding of the chronic, ever-present nature of our conditions, and how it gnaws at every corner of your life.\n\nI agree, much like how police have to be tased and pepper sprayed so they understand the pain, if there was a sensation-wired VR, so surgeons, insurance adjusters etc. would understand what their patients go through for recovery- I think understanding and empathy would be more present, if they had a glimpse into the ever-present pain and reduced function we face."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1mqk6pi",
    "title": "\u267f\ufe0fIf you\u2019re gonna make something wheelchair accessible, don\u2019t make it a thing!",
    "body": "",
    "flair": null,
    "score": 1307,
    "comment_count": 113,
    "created_at": "2025-08-15T01:51:32+00:00",
    "top_comments": [
      {
        "id": "n8ri5cv",
        "score": 231,
        "body": "Transcription: \n\nurbancripple\n\nFollow\n\nIf You're Gonna Make Something Wheelchair Accessible, Don't Make it a Thing\n\nHere's some examples awkward accessibility being a thing:\n\nYour at a hotel that has a lift to get you from one sub-floor to another, but the lift can only be unlocked and operated by one specific person that the hotel now has to go find. Sure, they've made the entrance to the sub-floor accessible, but now it's a thing.\n\nThe buses are wheelchair accessible but the driver has to stop the bus, take 30 seconds to lower the goddamn ramp, move passengers out of their seats, hook up the straps and then secure you in the bus. Sure, they've made the buses accessible but now it's a thing.\n\nThe restaurant has an accessible entrance, but it's past the trash room and through the kitchen. Sure, the restaurant is accessible, but now it's an insulting thing.\n\nHere's some great examples of accessibility not being a thing:\n\nThe train to the airport pulls up flush with the platform. I board with everyone else and sit wherever the fuck I want. Riding the train is accessible and not a thing.\n\nIn Portland, I press a button the side of the streetcar and a ramp automatically extends at the same time the door opens. I board in the same amount of time as everyone else. This is not a thing.\n\nI get that it is difficult to design for wheelchair accessibility, but folks need to start considering the overall quality of the experience versus just thinking about meeting the minimum requirements.\n\n---\n^(Accessibility/transcriber note:) This is a transcription of the image so it\u2019s readable by screen readers and helpful for people with visual difficulties. Wording, formatting, and any typos match the original image. If you spot an error that would improve accessibility, please reply and I\u2019ll fix it."
      },
      {
        "id": "n8rfk6x",
        "score": 198,
        "body": "This is like when I use an \u201caccesible bathroom\u201d and my chair doesn\u2019t fit so I get stuck. One time I got so wedged my fianc\u00e9 had to come rescue me and it took a good 30 mins. Another time I sliced my finger open real bad trying to escape an \u201caccessible\u201d bathroom. Why bother making something accessible if it isn\u2019t actually accessible? \n\nEdit: I no longer go to public bathrooms alone. If my fianc\u00e9 is there he just always comes in with me now and if it\u2019s someone like my mom, she waits by the door just in case"
      },
      {
        "id": "n8regvb",
        "score": 136,
        "body": "Make accessibility not \"A Thing\"! \n\nFor example, include image descriptions so people who use screen readers don't have to pass your post, wonder what it's about, comment to ask, follow the post, and periodically check through all the comments to see if anyone has transcribed the image!"
      },
      {
        "id": "n8sgiem",
        "score": 105,
        "body": "If the accessible thing needs a staff member to operate for you, it's not accessible."
      },
      {
        "id": "n8rudiq",
        "score": 78,
        "body": "The wheelchair getting stuck in the so-called accessible bathroom also happened to my neighbor. One would think that construction contractors would take the proper measurements, but I guess they just don\u2019t care."
      },
      {
        "id": "n8rs539",
        "score": 48,
        "body": "I agree in the bus thing is ridiculous. My chair has brakes. There is no reason you need to strap all of my wheels down using three different straps per wheel. I mean the wheel me in and then there's a located spot with little grooves and then each wheel has straps and then there's a seat belt that comes around me from both ends it's like what the hell? Do they think I'm going to turn on my rockets and just shoot out of the fucking bus? It's ridiculous. It takes like 20 minutes to unstrap me. Anybody else just be standing up and walking around through the bus with not a single seat belt and I'm strapped in 15 different ways."
      },
      {
        "id": "n8t2tca",
        "score": 35,
        "body": "I get real pissed if i go to use a wheelchair bathroom (nowadays i use it because most times it is the one that gets assigned in as gender neutral in a country where gender bias is heavily in factor) and i can see that it has no real use to an actual person in a wheelchair. Like, im talking the toilet not having the bowl cut so you can wipe and the toilet paper being reachable while sitting. Then i see the sink being  too low so i cant reach (but that is good, it means it is in reach for a person in a wheelchair) but the paper towels are so high i have to have my shoulders up and in a 90\u00b0 angle, which the person in a wheelchair would not reach while sitting. \n\n\nThey should always assume wheelchair users will be sat during 99% of stuff in the bathroom. Not assuming that the person will have someone to carry them up at all times or that all people in wheelchairs can get up even for small periods. \n\n\nMost wheelchair bathrooms ive been in only have the handle bars on the sides of the toilet, that is it. And for the brief two months i was in a wheelchair i was deeply aware of how poorly general bathrooms are designed AND how much my people did not follow the regulations for the accessible ones. And i had a leg injury AND a ARM injury at the same time, which was the reason i needed the wheelchair instead of crutches (surgery on the knee  and i broke the arm on the same fall)"
      },
      {
        "id": "n8rn61w",
        "score": 34,
        "body": "This is a great example of why UX is important"
      },
      {
        "id": "n8ts93s",
        "score": 34,
        "body": "Thank you!"
      },
      {
        "id": "n8rz32r",
        "score": 31,
        "body": "[Quantum Q'Straint Mobility Securement System Explained | Sun Tran Buses](https://www.youtube.com/watch?v=X-IkQ0Mghws)\n\nActually this is what my bus uses. We are good. \n\nAlso the ramp can be lowered by the driver with there are controls so they don't even need to get out. If there's one of these good boys in the bus that means that it's actually possible for a wheelchair user to go completely from the sidewalk into the bus and secure all by themselves. No driver needed."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1obyhk3",
    "title": "Oh boy\u2026",
    "body": "Info from the caption:\n\nThe Trump administration is rolling back disability protections for air travelers.\n\nThe Transportation Department announced it will no longer enforce Biden-era policies requiring airlines to reimburse passengers when wheelchairs are damaged or when accessible flights cost more.\n\nAlso, airlines will no longer be required to give passengers written notice of their rights when checking mobility devices.\n\nAccording to disability advocates, an estimated 5.5 million Americans rely on wheelchairs and airlines damage or lose about one wheelchair for every 100 they transport.\n\nSource: Reuters",
    "flair": "Article / News",
    "score": 1276,
    "comment_count": 214,
    "created_at": "2025-10-21T00:22:29+00:00",
    "top_comments": [
      {
        "id": "nkix7wh",
        "score": 544,
        "body": "They really just want us to die at home"
      },
      {
        "id": "nkj1d43",
        "score": 438,
        "body": "I feel like the trump administration does a new completely abysmal and disgraceful thing every day, I've lost count. What's even the point of rolling back this policy outside of the ableism?? How does anyone cheer for this?"
      },
      {
        "id": "nkizssd",
        "score": 359,
        "body": "They don\u2019t care where we die. Just die."
      },
      {
        "id": "nkj20na",
        "score": 221,
        "body": "Hatred. That\u2019s all I can think of"
      },
      {
        "id": "nkjuj29",
        "score": 195,
        "body": "People who don\u2019t see the issue don\u2019t realize that a custom wheelchair costs as much as a car and Medicare won\u2019t cover a replacement for five years. People just DON\u2019T UNDERSTAND how terrible it is to lose your wheelchair."
      },
      {
        "id": "nkjf0ls",
        "score": 166,
        "body": "Correct, Project 2025 is a genocide plan laying the groundwork for the Network State. This current admin is functioning as the demolition crew to dismantle the United States so that tech billionaires can swoop in (and they're already doing so) and create a modern form of feudalism where everyone able-bodied is enslaved to work on farms, or assembles killer drones in factories like the one that will be built in a town dubbed \"California Forever\".\n\nThey've been working on this for over a decade now, and the plan includes human trafficking and non-consensual experimentation. This is also why they killed Epstein, because he was involved with the think-tank and some of the human trafficking logistics:\n\n[www.vcinfodocs.com/what-is-the-network-state/](http://www.vcinfodocs.com/what-is-the-network-state/)  \n(Collection of research on venture capitalist money flow from the last decade)\n\n[Private jets, parties and eugenics: Jeffrey Epstein's bizarre world of scientists | Jeffrey Epstein | The Guardian](https://www.theguardian.com/us-news/2019/aug/18/private-jets-parties-and-eugenics-jeffrey-epsteins-bizarre-world-of-scientists)  \n(Article from The Guardian 6 years ago)"
      },
      {
        "id": "nkjbgg1",
        "score": 160,
        "body": "The sad part is there are some disabled people who voted for this clown."
      },
      {
        "id": "nkjmn08",
        "score": 125,
        "body": "It\u2019s also following a fascist playbook. Nazis went after disabled Germans first."
      },
      {
        "id": "nkj2uo4",
        "score": 122,
        "body": "This is the shit I explain to people that puts us 50 years back. These companies have millions and can afford if *they* cause damages to peoples mobility devices"
      },
      {
        "id": "nkll1am",
        "score": 111,
        "body": "The cruelty is the point"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1qt4aqg",
    "title": "The fact people think our labour is free is upsetting",
    "body": "Alt: Oval glossy vinyl sticker with the phrase \u201cDisabled Labour Isn\u2019t Free\u201d in bold purple lettering on a soft pastel sky background with light clouds and small sparkles.\n\n\n\nI designed these because I was truly fed up with how many times I\u2019ve been exploited for free labour or people profiting off of my work without me seeing any return. I hate that this is so truly rampant in our community. ",
    "flair": "Image",
    "score": 1277,
    "comment_count": 92,
    "created_at": "2026-02-01T17:15:39+00:00",
    "top_comments": [
      {
        "id": "o3034e3",
        "score": 306,
        "body": "\"This is the least you can do to give back to the community since disabled people like you are almost always freeloaders\" seems to be the disgusting and misguided righteous attitude"
      },
      {
        "id": "o303pdc",
        "score": 138,
        "body": "And when we do contribute we are expected to not want anything in return which is completely out of touch.\nIt\u2019s a \u201cwe\u2019re damned if we do,\nWe\u2019re damned if we don\u2019t\u201d situation\u00a0"
      },
      {
        "id": "o308n2c",
        "score": 132,
        "body": "Why don\u2019t disabled people work? \n\nBECAUSE NOWHERE WANTS TO HIRE US?!?!?!"
      },
      {
        "id": "o305hil",
        "score": 107,
        "body": "The amount of times people have suggested volunteering and I will not even get into \u201cjob training\u201d or \u201csupported employment\u201d or \u201cworkshops\u201d. It\u2019s infuriating. This is over and above the defacto discrimination disabled people face by requesting accommodations IF they are even given them"
      },
      {
        "id": "o30hrq6",
        "score": 61,
        "body": "Oh and then they\u2019ll also go on to call any disability benefits or funds \u201cfree money\u201d \n\nall while not considering that it\u2019s only like that because having a disability is hard and people take advantage of you exactly like this\n\nThe whole thing is messed up"
      },
      {
        "id": "o3098gz",
        "score": 47,
        "body": "There\u2019s that too - and I don\u2019t shame people who can\u2019t work.\nI had to start my own endeavour because oftentimes external work doesn\u2019t accommodate my needs.\u00a0"
      },
      {
        "id": "o30sb8q",
        "score": 46,
        "body": "If I got paid every time I was asked to provide accessibility advice for free, I would be a damn millionaire. \ud83e\udd23 It is especially discouraging when you do it and they ignore the advice anyway. Like I will be asked how to make an event accessible, and they end up going with an inaccessible option anyway because it was easier for them or within their budget or whatever. Then why the fuck did you bother me??"
      },
      {
        "id": "o30702k",
        "score": 45,
        "body": "There\u2019s an organization here in BC that is about employment being accessible and all their stats and PR is about how the disabled employee benefits the business and how their profit increases when they hire disabled people.\nI know that the employee will rarely see any of those numbers so even when we are paid, it\u2019s oftentimes exploiting our hiring for increased profits which is infuriating.\n\nOne business owner who is part of this organization plainly said that it \u201chelps our bottom line\u201d in a promotional video.\n\nI was disgusted.\u00a0"
      },
      {
        "id": "o31xjli",
        "score": 30,
        "body": "Also, calling SSDI \"free money\" is especially bullshit because you have to have worked and paid into the system to receive it."
      },
      {
        "id": "o30d8r6",
        "score": 29,
        "body": "Like what I have to offer clearly isn\u2019t worth compensation"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1mzfivx",
    "title": "Today I paid $100 to be treated like a normal adult, and it was the best money I've ever spent",
    "body": "I have CP and use a wheelchair. Today I went to Discovery Place with someone who doesn't work for an agency, isn't a trained caregiver, and has zero disability awareness training. \n\nAnd that's exactly why it was perfect.\n\n## Here's what DIDN'T happen today:\n\n- Nobody grabbed my chair and started pushing without asking\n- Nobody hovered over me \"just in case\"\n- Nobody spoke to me in that special voice reserved for children and disabled people\n- Nobody called me \"brave\" for existing in public\n- Nobody made decisions for me about where I could or couldn't go\n- Nobody treated me like I was made of glass\n\n## Here's what DID happen:\n\nShe ran after her kids through the museum. I had to haul ass across the entire place to keep up. My muscles actually got to WORK. I got to choose my own path, my own speed, my own direction. I existed in the group not as \"the disabled one\" but just as another adult trying to keep up with chaotic kids.\n\nWhen I almost got hit by a car in the parking lot, she didn't rush over to save me. She just yelled \"MOVE TO THE RIGHT!\" Like she would to literally anyone about to walk into traffic. She assumed I had a functioning brain and could execute a simple instruction.\n\nDo you understand how fucking RARE that is? To have someone assume competence as the default?\n\n## The dessert moment that broke me:\n\nAt the restaurant, I ordered dessert. She looked at me and said \"Gordy would probably like this\" about her 4-year-old autistic child. We fed him bites. He ate 75% of my dessert (kid is a very picky eater). Every time I tried to take a bite, he'd open his mouth and make these hilarious noises. We were dying laughing.\n\nNobody accused me of being inappropriate with a child. Nobody monitored our interaction. Nobody made it weird. I just got to share cake with a kid who likes me. That's it. That's all. And it was everything.\n\n## The fucked up part:\n\nThis person could NEVER work as my caregiver through an agency. Because what I need - someone who treats me as default capable - is literally against every protocol they have. The system would call her neglectful for not hovering, not helping, not constantly intervening.\n\nBut she gave me something no trained caregiver ever has: the dignity of being unremarkable.\n\nI spent $100 today on museum tickets and lunch. But what I actually bought was a few hours of being treated like everyone else. Not special. Not inspiring. Not fragile. Just... a person who might need to move right when a car's coming.\n\n## The real tragedy:\n\nI'm sitting here grateful that someone yelled at me to get out of the way of a car instead of rushing to rescue me. I'm thankful that someone \"neglected\" to help me. I'm celebrating that nobody gave me special treatment.\n\nThis is where we're at, folks. The bar is so fucking low that basic human dignity feels revolutionary.\n\nSome people get this by default. The rest of us have to strategize, pay for it, treasure it when we accidentally find it.\n\nToday was remarkable because it was so utterly unremarkable. And I'm going to hold onto that feeling as long as I can.\n\n---\n\n**Edit to add:** I know some of you need more support and that's valid. I need support too - just not the infantilizing kind. What I need is someone who assumes I'm capable until I ask for help, not someone who assumes I'm helpless until I prove otherwise. There's a huge difference.\n\n",
    "flair": "Rant",
    "score": 1262,
    "comment_count": 79,
    "created_at": "2025-08-25T03:06:32+00:00",
    "top_comments": [
      {
        "id": "naizl36",
        "score": 266,
        "body": "This is the big reason why I don\u2019t like to do things without my fianc\u00e9. If I go with anyone else I\u2019m infantilized and everyone is always grabbing me/being cautious/treating me different/etc. My fianc\u00e9 is the only person who I\u2019m just a person, he doesn\u2019t act like im completely incapable"
      },
      {
        "id": "naje51p",
        "score": 120,
        "body": "Are you stuck dealing with an agency? Please look into self-directed (also called consumer directed) Medicaid programs in your area. With self directed care, you can choose who works for you, and they don\u2019t have to be a licensed home health aide or follow lots of stupid agency rules.\u00a0\n\nYou can find someone who treats you with respect, and if they don\u2019t, you can fire them and hire somebody else. You can also generally have a family member work for you, with some exceptions depending on where you live and the program rules. But it\u2019s so much more flexible.\n\nIf you\u2019re comfortable sharing which state you\u2019re in, I can help you find out more about self directed care there. I live in Indiana and have self directed care. I\u2019ve chosen my own caregivers and almost never have to deal with condescending BS. Hope this helps!"
      },
      {
        "id": "najtn39",
        "score": 59,
        "body": "> I need support too - just not the infantilizing kind. What I need is someone who assumes I'm capable until I ask for help, not someone who assumes I'm helpless until I prove otherwise.\n\nThis resonates with me so much. It's definitely a reason why I'm so much happier with my partner and why I'm happy living with my sister and BIL than I have with my parents. They treat me like a person, and not fragile. Meanwhile to my parents it just feels like I'm a clipboard of medical information they constantly want to know about, and they question my choices constantly as if I'm not an adult who knows how her disability affects her.\n\nSurround yourself with people who treat you like a person first, and not your disability. I will definitely be remembering your quote, and I'm glad you had such a happy experience!"
      },
      {
        "id": "nakdgpa",
        "score": 54,
        "body": "It all made sense when you said she has an autistic kid. She knew better than to see the disability not the person. Its her normal to just be normal about someones differences."
      },
      {
        "id": "nam61ln",
        "score": 54,
        "body": "Same! My wife goes everywhere with me. She knows what I\u2019m capable of, what I need help with, and doesn\u2019t treat me with kid gloves. Going out with anyone that isn\u2019t her makes me a ball of anxiety bc they don\u2019t know what to do and try to over-help or don\u2019t know how to help. I\u2019d rather my wife push my wheelchair and run me into doorframes (she\u2019s a bad wheelchair driver) than someone who would be excessively cautious and fretful over every little thing. I\u2019d rather not leave the house than go somewhere without her"
      },
      {
        "id": "naiuwjn",
        "score": 41,
        "body": "im so sorry you have to go through this. thank you for sharing, it was very insightful to read."
      },
      {
        "id": "nan6vd8",
        "score": 25,
        "body": "It seems like she's one of the better parents of an autistic child, which does give me hope. \n\nUnfortunately, many parents of autistic children are still out there shoving them in 40 hours a week of ABA, trying to cure them with alternative therapies and fad diets, and wearing \"autism warrior mom\" shirts covered in puzzle pieces."
      },
      {
        "id": "naktva1",
        "score": 25,
        "body": "I am a musician, and one of my collaborators saw a post I made on instagram about an article I wrote about Medicaid protection; and he was 'low-key' (as the kids say) interrogating me about Medicaid; why was I on it? etc.; kind of prying a bit about my disability - afterward said that he likes to know what's going on with all his collaborators.  It felt a bit tone deaf."
      },
      {
        "id": "najwbh7",
        "score": 24,
        "body": "Sounds brilliant, thats all any of us want. And those who are privileged to hide (or selectively hide) our disabilities do it for just those reasons. People are such jackasses. I worked in a disability org as a site manager, I hired a bunch of PwD staff and updated policies, and I still got ableism (including from other PwD) when I came out about my disability. WTF!"
      },
      {
        "id": "naleapt",
        "score": 21,
        "body": "As someone who\u2019s mentally disabled I feel this so much. I\u2019m not stupid, I can figure out what\u2019s going on I just need a little extra time to process it. I don\u2019t need you to explain it slowly and methodically. And I definitely don\u2019t need you to repeat yourself. Just give me a minute. \n\nAnd yes I can make my own decisions and understand consequences!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1qit1xh",
    "title": "Watching the rest of America finally figure out how much this country sucks.",
    "body": "",
    "flair": null,
    "score": 1169,
    "comment_count": 79,
    "created_at": "2026-01-21T09:05:03+00:00",
    "top_comments": [
      {
        "id": "o0ts8nq",
        "score": 110,
        "body": "CW: Queerphobia and ableism. I\u2019m sorry but I need to let this out. I predict this and everyone called me overacting. I told them that the systems in the USA will continue to increase its cruelty and the range of victims will go wider. I was laughed at by everyone including my history teacher, same guy who said that transgender people don\u2019t matter when I told him about Florida passing new Queerphobic bills. I told them that more than just disabled people will die from medical misinformation and policies changes, they said it\u2019ll only kill disabled people(which is horrible that they acted like that\u2019s not a big deal within itself). Every single day, it feels like I can use First They Came poem to describe the reality that people like my history teacher will be facing. This situation is already a nightmare for us disabled people, the fact that most able people ignore us even when we\u2019re trying to help them is worse."
      },
      {
        "id": "o0ut0ga",
        "score": 58,
        "body": "Watching other marginalized groups tell me I dont know suffering and wasnt aware of how shit the country was, is quite the experience. Absolutely 0 intersectionality with disabled folks. I knew how bad it was before I knew what the word politics meant. Also if other countries could stop cheering on those who didnt vote for this to suffer, that'd be great. You dont suddenly become the good guy on wishing 70 mil to die (including kids and sick people who didnt vote for this), and yet if I point out I could never go to your \"great\" country because every single immigration system practices eugenics and capitalistic worth, I get downvoted to hell and back and told I'm a \"drain\" to society, okay yeah but you totally dont sound like MAGA when you talk like that."
      },
      {
        "id": "o0utyfw",
        "score": 52,
        "body": "'Oh you're a white woman you'll be fine!'\n\nHomey, I promise you, once you're disabled we matter just as much as non-white folks. Plus, personally, I'm gay and I'm trans. I'm fucked, my man."
      },
      {
        "id": "o0ugr2j",
        "score": 39,
        "body": "Me when I tell people about the situation in the US and they're like: Oh, but it's in the US! We don't care! Europe is so much better! \n\nNo. Recently, I heard a professor telling me 'disability is just a new trend theme in research, same like queerness' like no?? It's not?? We seriously care about both and it's not just a trend? We need those topics now more than ever. \n\nSo many academic researchers, especially in the queer and disability studies are afraid to do their job because of serious consequences for their life."
      },
      {
        "id": "o0uw7c4",
        "score": 35,
        "body": "I don't think that they are figuring anything out. I think they're under the impression that this is just because of trump and things will go \"back to normal\" once he's gone. I don't believe they realize how disabled people, people of color, women, and LGBTQ+ people have always been treated. I don't believe they care to know. I think they just want things to go back to where they can operate on autopilot the majority of the time and not give conscious thought to much of anything. 50%+ of the population of the US operates at the critical thinking level of a child."
      },
      {
        "id": "o0tsvni",
        "score": 30,
        "body": "America is absolutely terrible to those who lack privilege. Right now it's being very blatantly shown in everyone's face with ICE agents violating the human rights of basically every American that doesn't support Trump, but for those of us with disabilities, it's been obvious for decades. (The same template could be used for people of color, queer people, etc)"
      },
      {
        "id": "o0u44zf",
        "score": 29,
        "body": "Basically:\n\n  \nIf you're disabled, you're fucked.\n\nIf you're a POC, you're fucked.\n\nIf you're LGBT+, you're fucked.\n\nIf you're a woman, you're fucked.\n\n\n\nIf you're all four? You're super dee duper fucked as one can possibly fucking be.\n\n  \nThe rest of America is waking up to what is normal life to these people. They're used to getting screwed over constantly/being ignored, harassed, etc. And that's *bare minimum, and on a good day.*"
      },
      {
        "id": "o0uw41v",
        "score": 27,
        "body": "Not denying racism in america but people forget classism is a big deal too, you think they want a bunch of disabled people who cant make some rich asshole money? When disabled people are killed off as some of the first during fascism? *and this country has all our addresses logged because you have to to get aid as a disabled person*\n\nAnd same, LGBTQ+ pan, demi, in the process of a gender journey, under the poverty line my entire life born to neglectful addicts, mentally ill since 4 yrs old, and AFAB who experiences a fuck ton of medical bias especially when fat from PCOS. I do have privilege more than POC but claiming I have as much as a healthy, white person with a support system and assets? Nah. I knew which party wanted me dead, which one was trying to constantly cut services that kept me alive. People didnt do their damn research and they had the privilege of not worrying about any of this until now.\n\nWe're too busy infighting about it too, we have to stick together but I'm tired of being invalidated and ignored."
      },
      {
        "id": "o0ukebq",
        "score": 26,
        "body": "Just because someone has it worse doesn\u2019t make everyone\u2019s else\u2019s problems magically go away. Many disabled people still face difficulties in the so called \u2018better\u2019 countries and we shouldn\u2019t just shut up and take it because others have it worse, we should speak up and attempt to improve anyway we can."
      },
      {
        "id": "o0tszq9",
        "score": 23,
        "body": "I can help fill in as best as I can. Disabled people face a lot of oppression in the USA. Most able people trend to treat us as overacting. In the last year, the USA as a whole has alienated the majority of people in the USA(including able people). Everything from ICE kidnapping and either murdering people and or trafficking them into slavery to threatening invasions of other countries to stealing our taxe money to cutting funding for necessary stuff(like research, healthcare, housing, etc) to so many other things."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1ps7dqp",
    "title": "Michaela Benthaus, a 33-year-old German aerospace engineer is the first wheelchair user to travel to outer space!",
    "body": "Michaela Benthaus, a 33-year-old German aerospace and mechatronics engineer, made history as the first wheelchair user to travel past the K\u00e1rm\u00e1n Line, a common marker for outer space. \n\nHer voyage on a Blue Origin New Shepard capsule launched Saturday morning in West Texas.\n\nhttps://www.cnn.com/2025/12/20/science/blue-origin-koenigsmann-benthaus-wheelchair",
    "flair": null,
    "score": 1172,
    "comment_count": 24,
    "created_at": "2025-12-21T14:10:27+00:00",
    "top_comments": [
      {
        "id": "nv8u710",
        "score": 54,
        "body": "So proud of her. I'm also a paraplegic woman interested in Physics, and I'm amazed about space, even though I'm not an engineer."
      },
      {
        "id": "nv8go4n",
        "score": 14,
        "body": "Wow that is incredible."
      },
      {
        "id": "nv7pq2w",
        "score": 14,
        "body": "\ud83d\ude0d\ud83d\ude0d\ud83d\ude0d\ud83e\udef6\ud83c\udffd\ud83e\udef6\ud83c\udffd\ud83e\udef6\ud83c\udffd"
      },
      {
        "id": "nvcunhd",
        "score": 12,
        "body": "I would like to see long term how she would cope on a space station, if there's more or less barriers than in regular life. I imagine it would be easier."
      },
      {
        "id": "nvb7ri0",
        "score": 10,
        "body": "This is so awesome! The 33-year-old German engineer, who's also an aerospace expert, made history as the first wheelchair user to reach space,totally breaking barriers for disabled people."
      },
      {
        "id": "nvf0usj",
        "score": 7,
        "body": "Repeating what people say or write can be an accomodation style depending on reasons (for example i have to do it due to TBI and memory issues & processing)"
      },
      {
        "id": "nvgcqtk",
        "score": 6,
        "body": "Im sorry to be the boring d*ck pointing it out and this is amazing for her but this is essentially a promo stunt using her to give good publicity for a company owned by someone who treats disabled workers like sh*t. And that\u2019s really the very tip of the iceberg. It\u2019s not like many of us would be even remotely close to affording a trip."
      },
      {
        "id": "nvb5mud",
        "score": 6,
        "body": "Saw the landing and her emerging."
      },
      {
        "id": "nvke4np",
        "score": 5,
        "body": "Same! I hope she writes a book or something \ud83d\ude0a"
      },
      {
        "id": "nvkb0xa",
        "score": 5,
        "body": "[deleted]"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1p3zwl6",
    "title": "picture of me at a concert yesterday looks awefully renaissance coded",
    "body": "",
    "flair": null,
    "score": 1118,
    "comment_count": 61,
    "created_at": "2025-11-22T18:06:47+00:00",
    "top_comments": [
      {
        "id": "nq8hzf0",
        "score": 152,
        "body": "This photo goes so hard omg I love it"
      },
      {
        "id": "nq8i4wg",
        "score": 143,
        "body": "This is an incredible photo! Not only does it celebrate inclusion in the best way possible, the composition and lighting make it worthy of hanging in an art gallery. It definitely does give off Renaissance vibes. I hope it was as much as it looks."
      },
      {
        "id": "nq8le32",
        "score": 102,
        "body": "You are brave because I just don\u2019t have that level of trust in people."
      },
      {
        "id": "nq8n32r",
        "score": 64,
        "body": "I can tell you that people use it as an excuse to sexually assault strangers, I felt multiple hands under my bra and in my underwear back when I could crowd surf."
      },
      {
        "id": "nq8ov90",
        "score": 38,
        "body": "Eww.  I\u2019m so sorry that happened to you."
      },
      {
        "id": "nq8t6y8",
        "score": 31,
        "body": "this is legit beautiful lol, I love the soft lighting and the grace of your pose with everyone reaching to lift you. this picture is love and art."
      },
      {
        "id": "nq8m2h1",
        "score": 27,
        "body": "Oh my god. This is great!!!! It really does look hecka resistance. I hope this is a core memory for you."
      },
      {
        "id": "nq8o528",
        "score": 21,
        "body": "This is sick as hell \ud83e\udd18"
      },
      {
        "id": "nq8zglp",
        "score": 18,
        "body": "i think its just the photographer's camera settings"
      },
      {
        "id": "nq94rwz",
        "score": 16,
        "body": "[removed]"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1n1u1ff",
    "title": "My wedding ceremony cane",
    "body": "I struggled with my balance when walking, and my poor balance made it super difficult to walk while holding something in each hand. So I combined both together, my cane and my bouquet, so that I\u2019d be able to have a bridal bouquet at my wedding \ud83d\ude42\u2728 This is some of the lemonade I made when life threw me it\u2019s lousy lemons \ud83c\udf4b\u267f\ufe0f ",
    "flair": "Image",
    "score": 1110,
    "comment_count": 83,
    "created_at": "2025-08-27T21:40:34+00:00",
    "top_comments": [
      {
        "id": "nb108ig",
        "score": 70,
        "body": "Absolutely gorgeous. Well done!\n\nAlso, congratulations!"
      },
      {
        "id": "nb10v8q",
        "score": 27,
        "body": "Lol had to zoom in...\u00a0 \u00a0\u00a0\n\n\nThe cane looks beautifull tho..i mean that was a perfect idea..\n\n\n...whoever got you is lucky id say\ud83d\ude0c"
      },
      {
        "id": "nb14y9m",
        "score": 15,
        "body": "What a stunning bouquet and a clever way to incorporate it!! I love this so much :D Congratulations on the wedding!!"
      },
      {
        "id": "nb10jj8",
        "score": 14,
        "body": "Aww \u263a\ufe0f \nThank you!"
      },
      {
        "id": "nb1uerj",
        "score": 14,
        "body": "You're welcome. FWIW, I am an artist, complete with a BFA and made my living as a Scenic Artist for stage and screen. So, I'm a bit of a snob, and you truly did a fantastic job. Cheers!"
      },
      {
        "id": "nb2gslb",
        "score": 12,
        "body": "Oh!  Well in that case, SUPER yay for me!"
      },
      {
        "id": "nb118hi",
        "score": 8,
        "body": "Omg this is stunning!\u00a0"
      },
      {
        "id": "nb165ic",
        "score": 8,
        "body": "That\u2019s beautiful!! Amazing job! \n\nI\u2019ve thought of doing something similar, my fiance and I are waiting to get married until I can stand at our wedding (my own little desire). Looking at ways to decorate a walker to look better but keep me safe. Yours rocks!"
      },
      {
        "id": "nb1oau1",
        "score": 8,
        "body": "Thank you! And yea, decorating a walker would be super cute too! Like maybe put the bouquet of flowers in the middle and hang some lace or something similar behind the flowers, and then cascade the lace onto each one of the front legs of the walker? That\u2019s probably how I would start and just adjust as I go."
      },
      {
        "id": "nb116l8",
        "score": 7,
        "body": "Genius!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1oiqxv1",
    "title": "Mind your own business",
    "body": "",
    "flair": "Image",
    "score": 1094,
    "comment_count": 31,
    "created_at": "2025-10-29T00:53:27+00:00",
    "top_comments": [
      {
        "id": "nlxi2be",
        "score": 97,
        "body": "also, just sort of a shit thing to do in general"
      },
      {
        "id": "nly17oa",
        "score": 63,
        "body": "Sounds like my grandma. She hated people on welfare unless it was her than she needed it and she worked hard and deserved it. She\u2019s the worst honestly I\u2019m so glad I don\u2019t talk to her. When my brother stopped being able to walk (he had surgery that fixed that but we didn\u2019t know if it would work at the time) she told my mom she needed to smile more. But sure we are the horrible drains on society."
      },
      {
        "id": "nlxmfav",
        "score": 62,
        "body": "I also dont understand this common belief people have that everyone on welfare in the US is MAGA and that they all deserve what they voted for. Sweeping generalizations are bad but also vengeance against the most vulnerable isnt a good look either."
      },
      {
        "id": "nlydx1p",
        "score": 48,
        "body": "You think those who shame welfare recipients care about disabled people?? I fear this tactic will be successful"
      },
      {
        "id": "nlxns52",
        "score": 47,
        "body": "i hate this argument anyways. i live in the deep south and im disabled and dont even have insurance. i dont want any of the trump voters to lose their fucking food and healthcare lmfao. if we\u2019re all going to be petty and go \u201creap what you sow\u201d we will never have a better country. \n\ndecades of propaganda and defunding education got us here. i\u2019m also queer and neurodivergent and trans. i know it\u2019s not easy dealing with these people, but i don\u2019t believe that maga deserve to starve to death because they voted within their understanding of the world due to intentional defunding of education and social services from the gov\u2019t. \n\nwe need to get away from shaming literally anyone on welfare. disabled or not. a society that cannot feed and house its people despite having an abundance of housing and food, is a failure of a society."
      },
      {
        "id": "nlysf5t",
        "score": 27,
        "body": "i think they do think about who needs it most, they just don\u2019t care/want disabled people to die"
      },
      {
        "id": "nlxosu2",
        "score": 18,
        "body": "Absolutely.\n\nAlso as an aside I am also queer neurodivergent and trans. So I get it believe me."
      },
      {
        "id": "nlyf5fb",
        "score": 17,
        "body": "arrest unite whistle automatic spotted roof compare aware chief bag\n\n *This post was mass deleted and anonymized with [Redact](https://redact.dev/home)*"
      },
      {
        "id": "nlxq8cf",
        "score": 16,
        "body": "Its a shitty thought to have and I think a lot of people could benefit from schooling for critical thought and empathy!"
      },
      {
        "id": "nlxp3hv",
        "score": 14,
        "body": "it\u2019s truly a struggle! it also always kind of sucks to get lumped in w the maga folks. my soul dies any time i see a northern or blue state liberal callously talk about how they hope we get what we wanted with natural disasters killing us and stuff lol."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1l6w42p",
    "title": "My first time at pride with my cane and the queens helped me up to dance with them",
    "body": "If this doesn\u2019t belong here let me know! Just wanted to share my moment of joy it\u2019s nice to be included!",
    "flair": "Image",
    "score": 1087,
    "comment_count": 68,
    "created_at": "2025-06-09T04:47:20+00:00",
    "top_comments": [
      {
        "id": "mws353g",
        "score": 48,
        "body": "Anytime we can have a bit of happiness is a good thing.  \nFantastic!"
      },
      {
        "id": "mws8o8c",
        "score": 41,
        "body": "This was incredibly heartwarming to hear. I adore drag queens. They've always been so kind to me. Happy pride, my friend! \ud83e\udd79\ud83d\udc4f We should all unapologetically celebrate however we can \ud83c\udf08\ud83d\udc96"
      },
      {
        "id": "mws75f4",
        "score": 18,
        "body": "Happy pride\ud83c\udff3\ufe0f\u200d\ud83c\udf08"
      },
      {
        "id": "mws67ca",
        "score": 14,
        "body": "Yay! Happy pride!"
      },
      {
        "id": "mwsfm4z",
        "score": 12,
        "body": "Love everything about this, I hope you had the best time! Happy pride!!"
      },
      {
        "id": "mww0oii",
        "score": 12,
        "body": "Agreed! Hope you have a happy safe month!"
      },
      {
        "id": "mwt74hw",
        "score": 9,
        "body": "Looks like everyone is having a great time!  Thanks for sharing your moment."
      },
      {
        "id": "mwu005l",
        "score": 9,
        "body": "I have never, not once, felt unsafe around a drag queen. I love them so much and I\u2019m really happy to see you having a good time! Happy Pride \ud83c\udf08"
      },
      {
        "id": "mww0wn8",
        "score": 9,
        "body": "Yesss we need more queens! Happy safe pride!! \u2665\ufe0f"
      },
      {
        "id": "mww0l6y",
        "score": 8,
        "body": "Happy pride \ud83d\udc95"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1qr5zj2",
    "title": "I survived a train accident and lost both of my arms. I use my feet to type on a PC keyboard and navigate life. AMA!",
    "body": "Hi everyone,\n\nA few years ago, I was involved in a train accident that resulted in the loss of both my arms. It turned my world upside down, but I refused to give up. I\u2019ve spent a lot of time learning how to adapt and regain my independence.\n\nI am writing this post right now using my feet on a standard PC keyboard. I also use a webcam \\[to help with navigation/for head tracking - to stay connected and be productive. I want to show that life doesn't stop after a major trauma, it just changes shape.\n\nFeel free to ask me anything about my daily routine, the technology I use, the accident itself, or how I deal with the mental challenges. I\u2019m here to be open and answer your questions!\n\nAMA!",
    "flair": null,
    "score": 1081,
    "comment_count": 156,
    "created_at": "2026-01-30T13:50:40+00:00",
    "top_comments": [
      {
        "id": "o2mr8d2",
        "score": 124,
        "body": "Yes, but I'm good at typing. I've been typing for 12 years."
      },
      {
        "id": "o2lqz1o",
        "score": 116,
        "body": "Did you have to really practice to get your toes as dextrous as our fingers are?"
      },
      {
        "id": "o2lsfta",
        "score": 96,
        "body": "Do you do any gaming? \u00a0If so, what games have you found accessible and enjoyable to you?"
      },
      {
        "id": "o2nyp9w",
        "score": 93,
        "body": "I was 23 years old when I had the accident. I'm 60 now. The accident changed me 100%. In thinking, in behavior. In everything."
      },
      {
        "id": "o2lu1cb",
        "score": 76,
        "body": "I\u2019m not gonna lie super cool and impressive \ud83d\ude0e"
      },
      {
        "id": "o2lwxh4",
        "score": 67,
        "body": "[removed]"
      },
      {
        "id": "o2ltu8a",
        "score": 63,
        "body": "Where you already an adult by time of your accident? \nWhat do you think it was the most challenging aspect of becoming disabled?\nAlso, are you doing okay now? \n\nHave a excellent day \ud83e\udd70"
      },
      {
        "id": "o2mtdsu",
        "score": 63,
        "body": "It's true that the picture is older. I'm using Windows 10 now."
      },
      {
        "id": "o2msh88",
        "score": 48,
        "body": "Honestly, I don't know what Dragon Naturally Speaking is. But I'll look into it. Thanks for the advice."
      },
      {
        "id": "o2lrcv8",
        "score": 47,
        "body": "Have you ever tried speech to text software such as dragon naturally speaking? If so, why do you prefer a standard keyboard?"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1no433o",
    "title": "Today my fortune cookie chose violence\u2026",
    "body": "At lunch today I got a fortune cookie, when I cracked it open I had a good cackle. Note the AFO\u2019s and wheelchair footplate in the background. \ud83d\udc4c\ud83c\udffb",
    "flair": null,
    "score": 1036,
    "comment_count": 40,
    "created_at": "2025-09-23T01:08:54+00:00",
    "top_comments": [
      {
        "id": "nfpgjrk",
        "score": 122,
        "body": "Oof... Accidental r/FuckYouInParticular :("
      },
      {
        "id": "nfpeccr",
        "score": 90,
        "body": "A few years ago, my New Year's fortune cookie said \"You have great physical powers and an iron constitution.\" The whole table got a laugh."
      },
      {
        "id": "nfpdmhb",
        "score": 48,
        "body": "That's the problem though - this *is* considered \"universal\". People don't stop and consider diversity when they think of normal."
      },
      {
        "id": "nfpoelh",
        "score": 41,
        "body": "It's actually telling you that you'll gain wealth as a shoe model."
      },
      {
        "id": "nfp7a8r",
        "score": 33,
        "body": "I can't believe they didn't write something more universal, like: \"depend on your will\"...then again, they probably pay people minimum wage to type these things..."
      },
      {
        "id": "nfphujj",
        "score": 25,
        "body": "\ud83d\ude02\ud83d\ude02"
      },
      {
        "id": "nfp92cn",
        "score": 17,
        "body": "Dare is say... peak"
      },
      {
        "id": "nfrsj9j",
        "score": 14,
        "body": "How did I not know about this subreddit!? Thanks for sharing!!"
      },
      {
        "id": "nfpsm4t",
        "score": 12,
        "body": "Good cause nobody would want to look at my feet. \ud83d\ude02\ud83d\ude02\ud83d\ude02"
      },
      {
        "id": "nfptzuw",
        "score": 11,
        "body": "That's an unfortunate cookie"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1r8jc0v",
    "title": "The paperwork required to stay disabled is designed for people who are not disabled. I cannot be the only one who sees this.",
    "body": "**FINAL EDIT: **r/thismatters** holds this advocacy movement!**\n\n**Edit 12: This thread is now on X. 293 of you told me your story here. I put seven of them into a thread so the rest of the internet could see what you built in this room. If you want this to reach beyond Reddit \u2014 that is where it goes next. @PhoenixMSeat on X. #ThisMatters and so do you.**\n\n**Edit 11: 17,000 people showed up for this. From the US, Canada, the UK, and countries I haven\u2019t even checked yet. Someone posted their very first comment ever and asked if they were allowed to stay. Someone else wrote an entire article about administrative burden being a policy choice. And right now, someone is sitting alone thinking they are the only one fighting this system.**\n\n**They are not. But they don\u2019t know that unless you tell them.**\n\n**If this said what you\u2019ve been carrying, share it. In your disability groups. Your chronic illness pages. Your caregiver communities. Your local subreddits. Not for me. For the person who hasn\u2019t found this room yet.**\n\n**We talk about the Pink Tax. We need to talk about the Disability Tax \u2014 the extra hours, extra money, extra energy, extra paperwork, extra phone calls, extra proof that disabled people pay just to exist in systems that were not built for us. Every one of those 260+ comments is a receipt.**\n\n**This is not my post anymore. It\u2019s yours. Take it where it needs to go. #ThisMatters**\n\nI am on SSDI. I am legally blind. I also have ADHD and post-surgical brain fog from cervical fusions and a brain tumor removal. My executive function on a good day is maybe 70 percent of what it used to be. On a bad day it is maybe 30 percent.\n\nAnd yet. The amount of paperwork, phone calls, form-filling, deadline-tracking, and bureaucratic navigation required to maintain my disability benefits, my health insurance, my housing situation, and my basic existence requires executive function that my disability specifically impairs. That is not an accident and it is not an oversight. It is the system working exactly as designed.\n\nLast week I had a day where my brain was sharp. Clear, focused, ready to go. But my body was in a pain flare from a wind storm. So I had the clarity to understand what needed to be done and zero physical capacity to sit at a desk and do it. By the time the pain subsided two days later, the executive clarity was gone. The window closed.\n\nI have started thinking about this as a mismatch between two axes. One axis is cognitive clarity, the other is physical capacity. They almost never line up at the same time. And every form, every phone tree, every deadline assumes they are always lined up. The whole system assumes you are either fully functional or fully incapacitated. There is no form for 'I can think clearly but I cannot sit up' or 'my body works fine today but my brain is full of static.'\n\nI live in an RV in New Mexico. I am 54. I am building a life on $1,570 a month and trying not to let the administrative requirements of being disabled consume the few good hours I get each day. Some days I can do the things. Some days I cannot. And the system does not care which day it is.\n\nAnyone else feel like the cognitive load of managing disability is itself a disability? How do you handle the days when you have one axis but not the other?\n\nEDIT: I did not expect this response. Every comment here is proving the point \u2014 this is not a personal failing, it is a design failure. The system requires executive function to prove you lack executive function. It requires physical effort to document physical limitations. It requires meeting deadlines to maintain benefits for conditions that make meeting deadlines impossible. We are describing the same trap from different angles and different diagnoses. Thank you for sharing your experiences. I see you.\n\nEDIT 2: This post now has over 60 responses and every single one is describing the same system from a different body. Psoriatic arthritis and forms that require handwriting. ADHD and deadlines that require executive function. Progressive blindness and vision questionnaires in the smallest font possible. Mail-based deadlines for people who cannot reliably check mail. A year to apply for a process that takes three years to approve. Caregivers asking who helps the people who cannot help themselves. Someone in Canada describing an 18-month round trip for paperwork that could be digital. Someone who was physically injured filling out renewal forms.\n\nThis is not anecdotal. This is data. Exposed every single gap in the system across conditions, across countries, across decades of lived experience. If any disability policy researcher, journalist, or system designer is reading this \u2014 this thread is your focus group. We have already done the work. We are telling you exactly where it breaks and how. The question is whether anyone is listening.\n\nEDIT 3: Someone in this thread had to hire a lawyer just to handle the paperwork for benefits they were already entitled to. Someone else would be homeless and dead without their mother doing the administrative labor the system never provided. A person with psoriatic arthritis in their hands was physically injured filling out forms that require handwriting. This thread now has over 75 responses and it is becoming something I did not expect \u2014 a real-time map of every failure point in the disability benefits system, built entirely by the people living inside it. I am saving every response. This matters.\n\nEDIT 4: Someone in the comments asked how to fit all of this on a t-shirt. I have been thinking about that since they said it. Every comment here \u2014 every story about forms that arrive late, deadlines that have already passed, systems that injure the people they are supposed to serve \u2014 all of it comes down to two words. This matters. Your experience navigating a system that was not built for you \u2014 this matters. The cognitive load that nobody measures and nobody funds \u2014 this matters. The invisible labor of staying enrolled in your own survival \u2014 this matters. I did not expect this post to become what it became. But 80 people showed up and said the same thing from different bodies and different diagnoses and different countries. That is not a complaint thread. That is a design brief. And it matters.\n\nEDIT 5: I have read every single comment in this thread tonight. Some of them made me cry. Some of them made me angry. All of them made me feel less alone. But I do not want this to be a thread we all vent in and then walk away from. Over 80 people described the same broken system tonight from different bodies and different diagnoses and different countries. None of us broke it. But every single one of us knows exactly where it fails because we live inside the failure every day. That makes us the most qualified people in the world to fix it. I do not know exactly what that looks like yet. Maybe it starts with just being able to talk to each other \u2014 not to complain about it but to actually work on it together. If you are interested in being part of that conversation, follow me here. I am not selling anything. I am not building a brand. I am one person in an RV in New Mexico who posted something honest tonight and found out that 186 people felt the same way. That is not nothing. That is the beginning of something. And it matters.\n\nEDIT 6: A few of you have asked how we keep this going beyond one Reddit thread. I have been thinking about that. If you share your experience on other platforms \u2014 Instagram, TikTok, Twitter, anywhere \u2014 consider using #ThisMatters. Not as a brand. Not as a campaign. Just as a way to find each other. A way to say this is part of the same conversation that started here tonight. 200 people in one thread should not be the only place this exists. If your story matters \u2014 tag it. Let other people find it the way you found this.\n\nEDIT 7: This post has been seen by 9,500 people in three countries. 380 of you said yes. 184 of you told your story. 126 of you shared it somewhere else. Nobody disagreed. Not one person. In 17 years of this subreddit, that almost never happens.\n\nI have read every single comment. Some of you made me cry. Some of you told me things I don\u2019t think you\u2019ve said out loud before. Some revealed struggles I haven\u2019t yet revealed. A few of you scared me, and I reached out to you directly because you matter more than a post. Anyone can DM me anytime!\n\nWhile I sleep, the thread stays open. Keep talking to each other. The people in this room understand what you\u2019re carrying better than anyone in your daily life. If you\u2019re new here and scrolling at 3 AM because you can\u2019t sleep \u2014 you\u2019re not alone. Write your story. Someone will read it. I\u2019ll be back in the morning.\n\nIf you\u2019re hurting right now: 988 Suicide and Crisis Lifeline \u2014 call or text 988. Crisis Text Line \u2014 text HOME to 741741. You don\u2019t have to be \u201cbad enough\u201d to reach out.\n\n\\#ThisMatters \u2014 and so do you. All of you.\n\nEDIT 8: I just want to say something to the people reading this at 2 AM, 3 AM, whenever you found this. I see the view count climbing. I know you\u2019re out there. Some of you are in the UK waking up to this. Some of you are in the US and can\u2019t sleep \u2014 maybe for the same reasons this post exists.\n\nThis thread crossed 200 shares tonight. Somebody wrote an article in the comments. Somebody created a Facebook page. Somebody used the hashtag #ThisMatters without me asking them to. And as of right now, not one single person has disagreed.\n\nIf you\u2019re new here and you have a story, the room is still open. Write it. Someone will read it. I\u2019ll read it. I\u2019ll be back in the morning but this thread isn\u2019t going anywhere.\n\nEDIT 9: It\u2019s 1:45 AM. This post just crossed 500 upvotes. The ratio is still 100%. I don\u2019t even know what to do with that. Five hundred people said yes and not one person said no. Over 200 of you shared this somewhere else. Someone in New Zealand read this today. Someone in the UK is reading it right now on their morning commute. 223 of you told your story in the comments.\n\nI have read every single one.\n\nA few of you used a hashtag I didn\u2019t plan \u2014 #ThisMatters. It showed up on its own because it was already true. I\u2019m going to sleep now but this thread stays open. If you\u2019re reading this at 3 AM or 4 AM or whenever you found it \u2014 you\u2019re not late. The room is still here. The people in it are still here. Write your story if you have one.\n\nI\u2019ll be back in the morning. Thank you doesn\u2019t feel like enough but it\u2019s what I have. Thank you.\n\n\\#ThisMatters \u2014 and so do you. All of you. Every single one.\n\nEdit 10: It\u2019s 3 AM and I still haven\u2019t been able to walk away from this thread. Not because of the numbers. Because of what you\u2019ve been telling me.\n\nA woman with bipolar told me she\u2019s terrified of her own mailbox because paranoia is a symptom and the government sends threatening letters. The system uses her diagnosis against her and calls it a review. A man with ADHD described setting up a meeting just to help another disabled person fill out a form \u2014 two people building the infrastructure the system was supposed to provide. Someone lost benefits because they missed an appointment, and the reason they missed it was the disability they were being reviewed for. A nurse told me her body, eyes, and mind haven\u2019t worked together in six years.\n\nA woman told me SSA\u2019s own doctor found her disabled. She was denied three times anyway. A judge approved her in fifteen minutes. Fifteen minutes to confirm what years of denials refused to acknowledge. She came back a second time tonight to tell me she has styrofoam in her brain and on good days it\u2019s down to bubble wrap. Someone else said they\u2019re \u201cnot technically disabled\u201d \u2014 just chronic conditions \u2014 and I had to stop them. The line between technically and not technically was drawn by the same system this entire thread is about. If you\u2019re managing a body or a mind that fights you every day and a system that doesn\u2019t believe you, you belong in this room.\n\nAnd I need to say this. Some of you told me things tonight that scared me. Not the anger. Not the frustration. The quiet ones. The ones who sounded like they were running out of reasons to keep going. I reached out to some of you directly. If you\u2019re one of those people and you\u2019re still reading this \u2014 you matter more than a form. More than a review. More than a budget line.\n\nThen just now, someone said something that stopped me cold. They said this isn\u2019t a design failure. It\u2019s a design success. The success is that they pay us less.\n\nI need you to understand something about me. I was a paralegal for 22 years. I spent my career organizing other people\u2019s legal paperwork. I managed documents that decided people\u2019s futures. I kept deadlines for attorneys. I was the person they brought the complicated cases to. And I wasn\u2019t just getting by \u2014 I was getting good. I was hitting the part of my career where all those years were supposed to start paying off. The senior roles. The salaries you\u2019re supposed to retire on. I could see the top of what I\u2019d spent my whole adult life building toward.\n\nAnd then my eyes started failing. My body started shutting down. I didn\u2019t step off the ladder. I was pulled off it. And instead of the peak I\u2019d spent 22 years climbing toward, I landed on $1,570 a month and a system that challenges me at every single turn. Not once. Every review. Every form. Every appointment that assumes maybe this time I got better. I went from managing million-dollar litigation files to proving I still can\u2019t see well enough to manage my own mail.\n\nNobody applies for disability because it sounds like a good deal. I didn\u2019t choose this. None of us chose this. And after the denials and the appeals and the years of waiting and the doctors who said yes while the system said no \u2014 they finally let me in. And then they handed me the same kind of paperwork I used to do for a living, except now it\u2019s pointed at me. The skill I built my career on is the weapon the system uses to test whether I still deserve help.\n\nAnd the whole time, people on the outside call it free money. Like we just showed up and someone handed us a check. Like we didn\u2019t have lives before this. Jobs. Careers. Plans. Things we were building before our bodies or our minds made the decision for us. Every single person in this thread had a before. The system acts like the before never happened.\n\nWounds heal. Disabilities don\u2019t disappear. So why do we have to keep proving it?\n\nAnd it\u2019s not just the paperwork. It\u2019s everything around it. The people who don\u2019t believe you. The ones who are uncomfortable when you talk about it. The friend you\u2019ve known your whole life who finally admits they thought you were faking it. The stranger who tells you to get a job. The family member who does your paperwork because the system won\u2019t, and nobody thanks them or pays them or even counts what they do. The benefits system is broken. The medical system is broken. The way people talk to us and about us is broken. Every part of the structure that was supposed to be there for us \u2014 all of it, broken.\n\nAnd here\u2019s the thing that makes all of it worse. If you\u2019re reading this and you don\u2019t live it \u2014 if you\u2019re someone who stumbled into this thread from the outside \u2014 read what these people wrote tonight and ask yourself: does this sound too broken to be real? Does it sound like it can\u2019t possibly work this way? Because that\u2019s exactly what we\u2019ve been trying to tell you. And that is exactly why no one listens. The system is so absurd that describing it accurately sounds like exaggeration. So when we try to explain it, people assume we\u2019re being dramatic. They think we\u2019re milking it. They think if we can write a Reddit post we can hold a job. They don\u2019t believe the system is this broken because it shouldn\u2019t be. And they don\u2019t believe us because it\u2019s easier not to. We are fighting a system that is designed to exhaust us AND a public that thinks the system we\u2019re describing can\u2019t exist AND the same people telling us it\u2019s all in our heads. All at the same time. On the same battery. With no separate budget for any of it.\n\nAnd I think I just realized something. I think I finally understand what happened here tonight.\n\nWe didn\u2019t break a language barrier. We broke a silence barrier. Every single one of us had the words. We\u2019ve always had the words. We say them to ourselves at 2 AM when we can\u2019t sleep. We say them in our heads while we\u2019re on hold with SSA. We say them to the one person in our lives who gets it, if we\u2019re lucky enough to have that person. The words were never the problem. The problem was that we were never in the same room at the same time with permission to say them out loud.\n\nAnd then tonight, over 500 people ended up in the same room. And every single one of you said the thing you\u2019d been carrying alone. And every single other person understood it immediately. Not because I explained it well. Because you already knew. You\u2019ve always known. You just never heard someone else say it first.\n\nThat is what happened here. The silence broke. Not the language. The silence.\n\nAnd now that it\u2019s broken \u2014 now that the cat is out of the bag and 500 people have laid every failure point on the table in plain language \u2014 I don\u2019t want to waste this. I don\u2019t want us to fight. I don\u2019t want to bicker. I don\u2019t want to point fingers at who broke what or when. I want to talk to the other side of this with an open hand.\n\nHere\u2019s what I want to say to the people who run these systems, the people who write these policies, the people who think we\u2019re all trying to game it: we are not your enemy. The fraud is your enemy. And we want the people abusing this system gone just as much as you do \u2014 because every person gaming it makes it harder for every person drowning in it. We are on the same side of that.\n\nSo instead of spending money fighting us, re-verifying us, denying us, and processing appeals that take years for conditions that will never change \u2014 take that money and get it to the people who actually need it. Put everybody back in the right places. The people who need permanent support, give them permanent support. The people who need monitoring, monitor them. The people who are defrauding the system, find them. But stop treating all of us like suspects because you can\u2019t tell the difference. We can help you tell the difference. We just told you \u2014 read this thread.\n\nI\u2019ll make it simple. I am legally blind. I have asked my doctors a million times \u2014 can my optic nerve ever be replaced? Can it heal? Can it regenerate? The answer is no. It has always been no. It will always be no. So why am I filling out paperwork every few years to prove I\u2019m still blind? What exactly are we checking for? My optic nerve is not going to grow back between reviews. That is not hope. That is not medicine. That is a waste of your money and mine.\n\nIf a condition is permanent, the review should be permanent. One and done. That alone would save the system money, free up resources for the cases that actually need monitoring, and stop punishing people for having conditions that don\u2019t change. That\u2019s not radical. That\u2019s not political. That\u2019s common sense. And every single person in this thread could have told you that years ago if anyone had thought to ask.\n\nNobody asked. So we\u2019re telling you now. The laws and regulations already say most of what needs to happen. The rules are already written. The system just isn\u2019t following its own instructions. This thread is over 500 people telling you exactly where it\u2019s failing and exactly how to fix it. Not from a study. Not from a focus group. From the inside. In real time. For free.\n\nThis is the opportunity. Not to fight. Not to waste more money on both sides bickering over whether we\u2019re really sick. To take what just happened here tonight \u2014 this room full of people who finally said the thing they\u2019ve been carrying alone \u2014 and use it. Build something with it. Because we just handed you the blueprint.\n\nI almost didn\u2019t post this. I was nervous. I didn\u2019t think anyone would care. I typed it out and almost deleted it and then just hit submit anyway.\n\nAnd now it\u2019s after 2 AM and over 500 people are here and someone just posted their very first comment ever and asked if they were allowed to stay. They were nervous too. Just like I was. Just like all of us have been every time we thought about saying this out loud and didn\u2019t.\n\nThe silence was the barrier. And we just broke it. Together. All because one nervous person in an RV in New Mexico decided to stop deleting and hit post.\n\nI thought I was the only one. I wasn\u2019t. You weren\u2019t. None of us were. We just never had the room.\n\nNow we do.\n\n\\#ThisMatters \u2014 and so do you.",
    "flair": "Concern",
    "score": 1007,
    "comment_count": 482,
    "created_at": "2026-02-18T23:42:12+00:00",
    "top_comments": [
      {
        "id": "o65o06k",
        "score": 225,
        "body": "I wrote an article about this [The Crip Chronicle: ADMINISTRATIVE BURDEN IS A POLICY CHOICE, NOT A SIDE EFFECT](https://thecripchronicle.org/administrative-burden-is-a-policy-choice-not-a-side-effect/)"
      },
      {
        "id": "o65h542",
        "score": 98,
        "body": "Yep I was finally able to check my mailbox because it is difficult for me to walk in the heat for even small distances. I found out that they mailed something on Jan 28 for me to describe my disability, and it was due on Feb. 7. So by the time I read it I was already late. But even if I did manage to check my mail in time I am supposed to fill out these big behind forms through the migraines it will give me and get an uber to the post office because I can\u2019t drive, all in a week."
      },
      {
        "id": "o65oioh",
        "score": 84,
        "body": "Thank you for sharing this. Administrative burden as a policy CHOICE is the exact framing. It is not an accident that the system works this way. Somewhere a decision was made that the cost of making the process accessible was higher than the cost of people falling through the cracks. That is a choice. And the people who made it were not the people who have to live with it."
      },
      {
        "id": "o65k2vx",
        "score": 80,
        "body": "It really is. And the cruelest part is that the work of managing disability uses the same limited energy you need for everything else. There is no separate battery for paperwork."
      },
      {
        "id": "o65gbfu",
        "score": 76,
        "body": "It\u2019s so much work"
      },
      {
        "id": "o65k62a",
        "score": 62,
        "body": "This is exactly what I mean. They mailed it January 28 with a February 7 deadline and you are supposed to navigate that through migraines and not being able to drive. The timeline alone is designed for someone who does not have the condition they are asking you to describe. I am sorry that happened to you."
      },
      {
        "id": "o65plob",
        "score": 49,
        "body": "100%. It's one of the conundrums of living with disabilities. When you become disabled, you now need to be able to do new, additional things that would have been difficult enough without a disability and now that you're disabled, it can approach impossibility. It's like the financial challenges - your costs soar at the exact same time as your ability to earn money crashes. It's a very hard life and people who aren't disabled usually have no clue about the challenges that aren't just from the disabilities themselves, but the requirements and needs put on you because of the disabilities. It's so hard to articulate this. Is paradox the right word?"
      },
      {
        "id": "o65k84t",
        "score": 44,
        "body": "Last few years I've been adding a comment about date of letter, when it showed up, and days I had left to do it, all while disabled..  I also add a solution, of them sending it sooner and allowing a month to fill it out."
      },
      {
        "id": "o65rfhl",
        "score": 42,
        "body": "\"Prove you're disabled.\"\n\n\\*Takes weeks/months/years to organize and fill out the required forms that an able-bodied person could sort out in a few days.\\*\n\n\"What took you so long?!\"\n\n\"I'm disabled.\"\n\n\"That's not an acceptable excuse.\" \n\n  \nSadly, this seems by design to shake out people unable to self-advocate. This is, in my opinion, the main reason why disabled and sick people live longer with family support than those without and it's not 'loneliness' like pulp-academia likes to purport. Many of us are too damn tired to be lonely! \n\nFor example: good luck dragging yourself to all the appointments required for an organ transplant, or the constant appointments for infusions / dialysis / chemo / therapy / etc.. Heck, before all these delivery services just getting food and over-the-counter medicine if you were sick could be a hellish experience. Still is for those who don't have access to said services or are priced out of them. \n\nPulp-academia always seems so surprised when disabilities begin to rise in developing nations. Is it a lifestyle thing? Diseases of wealth? No you dorks! People got access to clean water and now don't die because they were alone and housebound for a week. They get calories. They get medicine. They get doctors. They survive. And pulp-academia is always just... where did all these disabled people manifest from? It reminds me of how academics of the past thought flies were born from spontaneous generation because some dumb asses couldn't figure out their life-cycles. Then if you engage in philosophy you realize how influential Aristotle has been, and are reminded his goofy-ass was a proponent of flies spontaneous generation. No wonder eugenics keeps popping up, and we socially operate the way we do. This Aristotle asshole was happy to further the ideas of state controlled reproduction and the culling of disabled and deformed infants. Real shame he's part of the foundations of civilization. \n\nAt the end of the day it's really a matter of social philosophy. Are you more concerned with redirecting a budget and prevention of fraud, or do you want to make the lives of the vulnerable, and thus everyone easier (see curbside effect). On one hand you can hire and train social workers, doctors, support-nurses, and medical admin to support these things. On the other you can replace those supports with auditors to hunt for efficiencies and fraudsters. Sure, this doesn't need to be either/or, but our politicians and budgets do like to make it an either/or option. \n\nI suppose there's a third option which is to just defund everything and watch it collapse in on itself. That's a popular one these days. Up in Canada, which has it better than most of the world, I had to interact with our tax agency for some support programs. The digital filing option bugged out, and I had to physically mail in the paper work. Due to defunding of our doctor's offices, tax entity, and our postal service the round-trip response has been 4-6 months. I'm expecting a conclusion of my situation after around 18 months of back-and-forth. That should be an unacceptable system in this age. \n\n  \n\\*climbs off soapbox\\*"
      },
      {
        "id": "o65nune",
        "score": 34,
        "body": "That is smart and I am stealing it. Documenting the timeline gap is exactly the kind of evidence that makes the problem visible. They can say they gave you 10 days without acknowledging that 4 were in transit and 3 of the remaining 6 might be days you physically cannot hold a pen or read a screen. You are building a paper trail that proves the design flaw. That should not be your job but I am glad you are doing it."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1lrftv7",
    "title": "As a newly recent ambulatory wheelchair user this made me feel seen \ud83d\udc9c",
    "body": "",
    "flair": "Image",
    "score": 998,
    "comment_count": 68,
    "created_at": "2025-07-04T10:53:22+00:00",
    "top_comments": [
      {
        "id": "n1afy7x",
        "score": 150,
        "body": "While the message is good, I wish they wouldn\u2019t say \u201cparalysed\u201d to mean non-ambulatory or not able to move their legs. There is degrees of paralysis and some paralysed people can move their legs/walk/stand. \n\nThere\u2019s also people that can move their legs but can\u2019t weight bear/stand or walk who aren\u2019t paralysed. \n\nWe have a great diversity in the wheelchair user community !"
      },
      {
        "id": "n1ap8g4",
        "score": 56,
        "body": "Came to say this, I get really annoyed at the *paralysed\" stuff as I know people with paralytic conditions that can walk.\n\nNon - ambulatory would do fine."
      },
      {
        "id": "n1ahvij",
        "score": 18,
        "body": "Seconded! I like the idea that in these discussions of diversity we can look at how there's so many different types of disability that might lead someone to use a wheelchair user, and that's true for non-ambulatory users as well as for people with paralytic conditions who are not wheelchair users."
      },
      {
        "id": "n1axghb",
        "score": 18,
        "body": "Your point is valid and matters! I did not make this banner I just saw it and it inspired me so I wanted to share it here. I believe the creators name is on the banner so maybe can let them know and if they adjust it it can be reposted. There is so much that needs to be done for us disabled people to be understood in all our unique ways and needs"
      },
      {
        "id": "n1agx9h",
        "score": 16,
        "body": "I love this! I'm ambulatory, and the amount of looks I get from non wheelchair users because I stood up, or walked a little bit pisses me off to no end"
      },
      {
        "id": "n1ayhgc",
        "score": 16,
        "body": "Thanks for replying, I understand. I just wanted to combat any misinformation here as I know it\u2019s a common refrain around ambulatory wheelchair users online - I think if you\u2019ve been isolated from a disabled community previously (through fatigue/social isolation/how your family are/how your culture is etc.) you might not know all the ways someone is a wheelchair user! I just wish people would do a little more research before making graphics or doing advocacy \ud83d\ude05\n\nNo hard feelings to you at all either, and welcome to being a wheelchair user \ud83d\ude0a I hope you always can find dropped curbs, your ramps are never steep and your doors are automatic!"
      },
      {
        "id": "n1cfxet",
        "score": 14,
        "body": "Yep, I have paralysis but I can walk"
      },
      {
        "id": "n1c9rwd",
        "score": 10,
        "body": "Agreed. I am paralyzed and I can stand and walk short distances with help. I really don\u2019t like the phrasing here because it just further complicates things"
      },
      {
        "id": "n1biswr",
        "score": 10,
        "body": "I'm at a point, being an ambulatory user myself, that after a full on year of it, next week actually, that I'm kind of starting to get amused by the reactions. I dunno if thats just me or if finally having found proper pain management that works is finally making me mellow out more and be less irritated at it, cause it *used* to really piss me off. \n\nLast week I had someone at work freak out that I stood up, and they say to me, \"YOU CAN STAND?!\"\n\nSo I responded with an over-exaggerated reaction of \"OH MY GOD, I CAN?!\" and then just went back to grabbing the thing I needed. They used to be a regular (almost daily,) but they haven't been back in since lmao. \n\nIt's made me want to start coming up with different reactions or responses in regards to it to just take the piss out of people wigging out."
      },
      {
        "id": "n1awnni",
        "score": 10,
        "body": "Yes it\u2019s information that needs to be known. I cannot stand for more than a few minutes or walk long distances. Having a wheelchair allows me to be able to do many things I could not do otherwise even something as simple as going to the grocery store"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1o2j9kl",
    "title": "Update: I made the cards!",
    "body": "I made a post earlier this year on this sub asking for some input on my idea to make cards/notes that I could put on the windshields of cars illegally parking in places like handicap spots, in the lines next to parking spots, or blocking ramps.\n\nI said I especially wanted to make them since it was such a huge issue at my university and the police refuse to do anything about it, so maybe these cards might help people think twice. I plan on giving them to people in my disability group to use, too. \n\nI just wanted to show you what they turned out like! :) They\u2019re made like business cards so they\u2019re thicker and sturdier than paper, I haven\u2019t used any yet but I hope they won\u2019t crumple up or fly away in the wind since they\u2019re made out of that sturdier material.\n\n(The card says \u201cYour parking may have harmed a disabled person today. Please do better next time. If you have a placard and are legally parking in a disabled parking spot, please disregard.\u201d)\n\nhttps://www.reddit.com/r/disability/s/KvcKQi0N92",
    "flair": "Image",
    "score": 991,
    "comment_count": 121,
    "created_at": "2025-10-09T22:00:36+00:00",
    "top_comments": [
      {
        "id": "nioetiw",
        "score": 348,
        "body": "not to criticize, but tbh, \u201cyour parking harmed a disabled person today\u201d would have been better and more direct. \n\n\u201cMay have\u201d gives them an out because they always argue *no one was using it, it was only a minute, and no one needed the spot, so it\u2019s fine*. \n\nReality is that illegal parking *always* harms a disabled person because it takes away a needed and reserved resource,  making expected parking accommodations unreliable at best, which discourages many from even trying (to go to the movies, shop, etc)."
      },
      {
        "id": "niohkrn",
        "score": 192,
        "body": "I think it's important to stress ONLY putting them on cars blocking ramps or someone who parked on the lines. I think many of us have been stopped by people who think they have the right to guess whether we're \\*really\\* disabled (or, worse, really disabled \\*enough\\*) and it's an awful experience...and really, do we want to risk hurting our own? because lateral abelism is a thing and it's gross...and hopefully, something we don't want to be promoting."
      },
      {
        "id": "niooju1",
        "score": 91,
        "body": "\"yOu ShOuLdN't bE uSiNg yoUr pArENt'S bLuE bAdGE!\" - then I flip it over and they see my photo."
      },
      {
        "id": "nip3i5y",
        "score": 62,
        "body": "Love this!\n\nI also use the parking mobility app almost daily to report these assholes. You snap a few pics showing their license plate and where they're parked, and they get a ticket in the mail. \n\nZero confrontation, and I love that the consequences come much later/after the fact.\n\nBonus: the nonprofit that does this work uses the data to advocate for more parking spots and better enforcement when they get enough reports in the same places. They also employ disabled folks to do this awesome work!"
      },
      {
        "id": "nip9au6",
        "score": 62,
        "body": "I kinda have to agree with taking out the may have. I don\u2019t have a placard myself but it always drives me crazy seeing someone do something that would not be beneficial to someone who may need it (ex I don\u2019t mind steps personally but if it\u2019s somewhere the steps are on display but the elevator is hidden if I don\u2019t see it near the stairs I\u2019m a little like uh what. Personally I think stairs and elevator should be in view because both are needed and important)"
      },
      {
        "id": "niqgiz6",
        "score": 58,
        "body": "Completely valid point, I\u2019ll be making other designs in the future so I will keep this in mind! Thank you :)"
      },
      {
        "id": "nipanhi",
        "score": 36,
        "body": "Genuinely asking: I've seen this since I started freely using the internet, literally in 1993. Why in the world is this ableist?"
      },
      {
        "id": "niqggnf",
        "score": 31,
        "body": "I made these mainly to put on cars with no placard and no disabled license plate parking in disabled parking spots. There are very few of those spots at my university and there are almost always people with no placard / plates pulling into those spots either \u201cto run inside really quick\u201d, to pick up/drop off their friends, or to just have a spot closer to the party they\u2019re going to. I\u2019ve missed class many times because there\u2019s no way for me to get into the building in time due to the 1 or 2 spots per building being taken by people without placards.\n\nWhile I do recognize the possibility of someone using these to try to bother invisibly disabled people, the potential to reduce the harm that able bodied people are perpetuating by refusing to let us use are accommodations is much more important than potentially annoying a fellow disabled person who doesn\u2019t have their placard visible. The harm being caused in those situations aren\u2019t the same.\n\nObviously I do not condone harassment or fake-claiming, but that\u2019s not what these cards were made for nor am I advocating for that in any way. If someone is acting like that, the cards are not the reason. In case someone with these cards happened to slip up and put them on a legally parked car, I added the disclaimer at the bottom as well to dispel any ideas that I\u2019m trying to invalidate anyone who would happen to get the card on their window."
      },
      {
        "id": "nipp1lz",
        "score": 27,
        "body": "I actually hate these card things. I get them on my car all the time even when my placard is visible."
      },
      {
        "id": "nir5vq7",
        "score": 26,
        "body": "I'm not comfortable with this at all. You are drawing a conclusion that the person is likely violating the law or faking their need for disabled spot, when in reality they could have merely forgot to out their placard up on their mirror, or like me have it stolen. DMV told me to always hide the tag in my glovebox when not actually parking in a Disabled Parking Spot.\n\nAs much as it pissses me off to no end to have fakers take our spots, I don't think it's our right to step up as enforcers. Take a picture if you want and document it to the school administration or the police. If it's school property then you take it to the dean and Disabled Student Services. \n\nI had my parking permit stolen from my car and it took a month for DMV to issue me a new one. All I could do was park and be prepared to fight the ticket in court if I got one. I had a paper printout from DMV that I kept with my registration, but it says Receipt Only - DO NOT DISPLAY. The ticket and violation fines get dropped if you have a valid permit. I had to get 4 tickets cancelled after that.\n\nIn that month though I had a barrage of self righteous people, openly harass me, scream at me, all presuming the worst. I even had one crazy woman stalk me in the grocery store. I literally had to call the cops myself more than once because I feared my car would be vandalized. Just because my placard gets stolen doesn't mean that I don't still very much need to park there, and the law does allow you to still utilize the spot without it. You just have to prove you had the legal right to park there on that date.\n\nIf the problem is that there are not enough spaces, then you petition the school to create more disabled parking space. Going all Lord of the Flies on other people who may have hidden and severe disabilities is just being trash to our fellow disabled people. \n\nNot one of us are required to account to John Q Public on this matter for any reason. When people harassed me I told them call the cops, I'll wait, and sometimes I did. The cops can look up your DL and see you have the permit. The problem is so persistent and common that cops typically run your license plate to see if it comes back to an owner with a permit. \n\nAlso as disabled people, we are often more vulnerable to being injured in a confrontation - in either direction. You are putting a \"Scarlet Letter\" on someone's car who truly may not deserve it. That could empower another person who needed the spot enough that they vandalize your vehicle. I've seen vehicles targeted for lesser reasons. \n\nIn a comment elsewhere in this thread, someone mentioned putting them on cars where the person took the spot but didn't need a spot with a ramp. Honestly it'\u00a8s none of your business what their full needs are. Many people who are disabled but ambulatory often need ramp access. \n\nSo I understand the motivation. I know people abuse the hell out of it and really suck. However I do not think this is a helpful way to deal with the problem. Ask for more disabled spots to be painted. Ask for more ramp accessible spots. Ask that all spots be designed to accommodate wheelchairs with the extra space to the side, because A non-wheelchair user has as much right to that spot if it's their only good option as someone in a wheelchair."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1mq4fyt",
    "title": "My super evil cycle",
    "body": "Imposter syndrome is hell",
    "flair": "Image",
    "score": 990,
    "comment_count": 41,
    "created_at": "2025-08-14T15:50:06+00:00",
    "top_comments": [
      {
        "id": "n8o74ps",
        "score": 67,
        "body": "Literally me every time I go to get in the car: I don't need my braces/as many braces it's fine! -> omg why am I actually screaming and crying this is so bad -> sleep for 3 weeks -> its not that bad, I won't need my braces"
      },
      {
        "id": "n8o7k36",
        "score": 55,
        "body": "Oh this is a game I play constantly! I\u2019m in mind numbing pain, I spend several days in bed, now I feel okay so it must have been nothing, do way too much the next day, back in mind numbing pain \n\nDo I know it\u2019ll happen? Yes. Do I constantly second guess myself and think I\u2019m being a baby? Also yes. \n\nI\u2019m slowly getting better at breaking the cycle but man does it creep in easily"
      },
      {
        "id": "n8o8gqv",
        "score": 34,
        "body": "And not just the imposter syndrome, it's the damned hope too. Life would just be so much easier if I could walk without braces and crutches or without needing a wheelchair"
      },
      {
        "id": "n8oehmz",
        "score": 21,
        "body": "How do we get over imposter syndrome"
      },
      {
        "id": "n8p4nr9",
        "score": 18,
        "body": "me - \"my hip feels good, maybe it'll stay in place today!\"  *tries to walk* \"oh, i'm on the floor\""
      },
      {
        "id": "n8qc1an",
        "score": 15,
        "body": "The constant pressure to validate our disabilities to others means that the moment we actually find relief in the accommodations we seek for ourselves we begin to feel a sense of invalidation about that same disability that led us to seek those accommodations to find that relief. It's a stupid little cycle that's based on the idea that you have to prove something to somebody else"
      },
      {
        "id": "n8p6gt1",
        "score": 13,
        "body": "I'm the same way, except for some reason my brain has no grasp on permanency.\n\n\"Oh shit, I'm not in pain. I feel great. Maybe I'm fixed.\" Go back to work, in extreme pain, definitely not fixed. Rinse and repeat every 4-5 days (I work two days a week)"
      },
      {
        "id": "n8pn33e",
        "score": 11,
        "body": "Sometimes when I have my seizures I\u2019m like \u201cokay maybe I\u2019m just faking this let me try to move\u201d and then I can\u2019t move \u201cokay I can\u2019t move because I\u2019m thinking about moving, I\u2019m still faking it somehow\u201d meanwhile I just look like that family guy meme all sprawled apart on the floor"
      },
      {
        "id": "n8pjhol",
        "score": 10,
        "body": "Literally just happened to me three seconds ago before I opened Reddit"
      },
      {
        "id": "n8pulx9",
        "score": 9,
        "body": "Any time my chronic pain is in remission"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1m50mdu",
    "title": "Omg it happened again!",
    "body": "Went for a \"walk\" with my fianc\u00e9, I'm in a wheelchair and this old guy in a scooter comes up to me and asks why I'm in a wheelchair.\n\nI just tell him that I've been in one since I was 5 due to a virus.\nSo then he tells me he knows a man upstairs (and proceeds to point up) that's named Jesus that can help me.\n\nSo my fianc\u00e9 tells him no that's okay, we know it's not necessary and after telling him no thank you 3x this man gets offended and said well you get what you deserve and stormed off.\n\nWhy do people feel the need to spout their religion at me and make me feel like crap when I don't agree with it. I don't do this to other people. \n\nHas this happened to you, and what do you do?",
    "flair": "Question",
    "score": 984,
    "comment_count": 229,
    "created_at": "2025-07-20T21:27:32+00:00",
    "top_comments": [
      {
        "id": "n48gqrs",
        "score": 386,
        "body": "I could understand his attitude if he came up skipping and jumping and had recently prayed to get out of a wheelchair, but he was using a mobility scooter?  Hows that work?"
      },
      {
        "id": "n497m9b",
        "score": 213,
        "body": "I had someone ask to pray for me, and I politely turned them down, and when they continued to insist,  I told him I would pray for us and said, \" Lord, please help this man in front of me. He's about to get a crutch to the face if he doesn't fuck off immediately, in God's name we pray, Amen.\"  He called me a bitch etc and walked away."
      },
      {
        "id": "n48maja",
        "score": 165,
        "body": "Him: \u201cI know a guy upstairs (points to the sky) that can help you!\nMe: Oh really, where\u2019s he been? Too busy to heal my genetic mutation? He created the biologic system and it was going ok but the wheels came completely off and he was nowhere to be found. I had to see a guy on the 15th floor (points to large university hospital in top 10 in the nation) for help getting out of the ditch and for a chance to keep living! I think I\u2019ll stick with my guy \ud83e\udd37\ud83c\udffd\u200d\u2642\ufe0f I know where he is, and he\u2019s very reliable - I\u2019ve been waiting to see your guy for 50 years and all I seem to get are his enthusiastic representatives that always need my money at regular intervals. Seems like I\u2019ve paid your guy regularly but he\u2019s apparently a no show. Next time you talk up your guy be sure to tell everyone he \u201cghosts\u201d people a lot!"
      },
      {
        "id": "n4afn8k",
        "score": 130,
        "body": "Well, he got what he deserved /s"
      },
      {
        "id": "n495on5",
        "score": 80,
        "body": "My mom is really religious and has many church ladies praying for me. So many things have gone wrong in the past 3 years. After my wife died, I told her to stop with the prayers, prayers are going to kill me!"
      },
      {
        "id": "n4ala7m",
        "score": 74,
        "body": "How do you storm off on a disability scooter? It's hilarious to imagine and I need to know so I can do it when people are rude to me \ud83d\ude02"
      },
      {
        "id": "n48q16q",
        "score": 66,
        "body": "Certain evangelical and charismatic Christians have complex and very fundamentalist beliefs around faith healing and faith in general. I grew up in this \u201cChristian\u201d tradition and I\u2019m a wheelchair user (Becker Muscular Dystrophy.) They believe their version of Christianity needs to be demonstrated, not just believed quietly and internally. So, they often are quite pushy about \u201cgetting saved\u201d for example. They believe they are literally saving people from a literal place of torment called hell. The same thing happens with faith-healing. Their churches will preach the idea of \u201cstepping out in faith\u201d in order to convince their members that miracles will happen after they demonstrate their faith. They demonstrate by offering strangers a glimpse of these so-called miracles by offering to pray for people they see as sick or down-and-out. An actual miracle never happens but they have \u201cbuilt their faith.\u201d I was a music leader at a few churches that believed this way. I was constantly being singled out as someone who needed \u201ca touch from God\u201d and I spent many, many hours being prayed for. I believed for way too many years that I would get my miracle and have strong muscles again. It was very confusing and discouraging. These types of Christians are mostly incapable of understanding the harm this faith-healing causes. I\u2019m sorry this happened to you\u2014it must have been unnerving and awkward at the very least! \n\nI had this experience a few years ago shortly after I had officially told my friends and family I was now an atheist. An awkward man came up to me as I was doing my self checkout at the grocery store. I could clearly see he was nervous as he \u201cstepped out in faith\u201d to talk to me and share the good news of Jesus. I was very direct and told him I was a church leader who used to believe but over time saw it was BS. He talked with me for a minute or two but it felt so good to say a firm \u201cno thank you.\u201d \n\nI take the time to challenge their beliefs and discuss it but if that\u2019s not your jam (really, arguing about faith is kind of a niche hobby) just send them on their merry way. Good luck! There are a lot of bizarre beliefs and people out there!!"
      },
      {
        "id": "n48v5e5",
        "score": 59,
        "body": "The first time someone asked if they could pray for me I just awkwardly said \u201cyes?\u201d Thinking that they\u2019d like go home that night and pray\u2026.. instead they put their hands in my knees and did the prayer right there. I\u2019m not paralyzed and I highly considered standing up and acting like a miracle happened."
      },
      {
        "id": "n49lpqg",
        "score": 57,
        "body": "Lmao \ud83e\udd23 love this will have to try it sometime \ud83d\ude02."
      },
      {
        "id": "n4axx37",
        "score": 52,
        "body": "[Abby Lee Miller](https://youtu.be/TdGF0Jxv3eU?si=UxmrSWllZynh9Du6)"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1lft2yc",
    "title": "How I styled my mobility aid!",
    "body": "Sorry if this isn\u2019t allowed I wasn\u2019t sure.\n\nBut this is my triumph prestige 2 in 1 rollator/transport chair. The sky blue color made me want to add clouds! I love fashion and figured if I had to use it all the time it should look good too! \n\nI decorated it with stickers from Amazon and Etsy. Wish I could do something with the seats, but they have Velcro on the bottom so I guess they\u2019ll have to stay. ",
    "flair": "Image",
    "score": 982,
    "comment_count": 89,
    "created_at": "2025-06-20T02:40:25+00:00",
    "top_comments": [
      {
        "id": "myr4p67",
        "score": 67,
        "body": "This is probably the most well done customization of mobility equipment I\u2019ve seen posted here"
      },
      {
        "id": "myqy45k",
        "score": 21,
        "body": "Oh, this is niiiiiice \ud83d\ude0d\n\nI love the iridescent clouds!"
      },
      {
        "id": "mysr1l0",
        "score": 19,
        "body": "Omg thank you! It was hard finding inspiration online so I had to wing it"
      },
      {
        "id": "myrajzt",
        "score": 18,
        "body": "This is so cute! Thank you for sharing the model as well because this looks like it might work really well for me - so it can turn into a push wheelchair from a walker basically? All it needs is a cup holder added on lol"
      },
      {
        "id": "myqugvc",
        "score": 12,
        "body": "It looks so good!!"
      },
      {
        "id": "myu74cd",
        "score": 12,
        "body": "You did a great job, I thought the clouds on the blue were actually done by the factory at first. It fits with the colour really well."
      },
      {
        "id": "myr8r9f",
        "score": 11,
        "body": "that is pretty \n\ni wish i had the motor skills to do the pretty art i see on reddit \n\ni want to stickerbomb my chair fully one day with stickers I find at musems and stuff"
      },
      {
        "id": "mysr4i9",
        "score": 11,
        "body": "They sell a custom cup holder for it! The bars are weird so normal ones don\u2019t fit on it."
      },
      {
        "id": "myru2rd",
        "score": 8,
        "body": "This is so cutee and sooo soo prettyyyy, I just want to make mine look like this on my wheelchair + walker but i\u2019m not an artist and i\u2019m not creative whatsoever"
      },
      {
        "id": "myqvejw",
        "score": 8,
        "body": "Thank you!!! \u2601\ufe0f\ud83e\ude75"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1o9tlem",
    "title": "I just got my first wheelchair, and my life is already changed for the better",
    "body": "Back in December 2023, I had an accident that ended up changing everything. I was riding my cargo bike home from church with my son, who was about to turn five, and my friend\u2019s eight-year-old daughter on the back. I don\u2019t remember much of it, but I think the kids leaned over the side and I couldn't correct the movement it caused, and I clipped a tubular steel fence along the side of the bike track, went over the handlebars, and hit the bitumen hard. I remember trying to slow down, since we\u2019d been going around 20 km/h, and yelling for the kids to hold on. After that, everything goes blank.\n\nI\u2019m still so thankful the kids were okay. They walked away with just a few grazes, and after a few months, we were even back on the bike again. I wasn\u2019t as lucky though, and came to with a paramedic leaning over me, and I was apparently not very cooperative lol. I ended up with what I now know was a mild traumatic brain injury and post-concussion syndrome. I actually led the Christmas service just over a week later with a huge black eye and the most insane knee grazes I've ever had, which wasn\u2019t exactly festive, lol.\n\nAt first, I didn\u2019t connect the dots between the accident and the way things started to spiral afterwards. Recovery was rough, and it took me a long time to realise how much had shifted. Before the crash, I\u2019d lived with chronic illness and pain for years, things like POTS, joint pain, and fatigue, but I could manage it. It made life slower and more tiring, but I could still push through. I\u2019d rest afterwards, but I could still do things. After the accident, that balance disappeared. My body just stopped bouncing back.\n\nOver the following months, everything got harder. My previously manageable POTS got worse than it had ever been, and I developed moderate-to-severe ME/CFS. I had to give up riding my bike because I couldn\u2019t manage the weight or balance safely anymore. I started getting headaches that mimicked the initial head injury, and these have never gone away to this day. I\u2019ve since been diagnosed with hEDS, which actually explains a lot, and in a weird way I\u2019m grateful for that clarity. My physiotherapist even half-jokingly said that my hypermobile shoulders probably saved me from breaking bones that day.\n\nBy October last year, things had gotten really bad. I could barely walk without needing to stop and sit after a few minutes, and even short outings completely wiped me out. I got a walker around that time, which helped for a while. I still use it for things like hydrotherapy and quick errands, but eventually there were more and more days where it just wasn\u2019t enough. Sometimes it even felt unsafe. I had never been so fatigued or unwell in my life. I was mostly housebound apart from the school run, and some days I couldn\u2019t even get out of bed.\n\nFor a long time, I felt really stuck and hopeless. My world had shrunk to school drop-off, resting all day, and school pick-up. That was it. I\u2019d gone from being someone who loved being part of my church, on worship teams and volunteering in the cr\u00e8che for women\u2019s Bible study, to someone who could only make it to church four times in eighteen months. It nearly broke me. I was caught in this constant cycle of rolling PEM, where every bit of energy I had went into taking my son to school in the morning, then resting for hours so I\u2019d be able to pick him up again. After school, I\u2019d push past my limits to get through the afternoon and evening routines, and by the time he went to bed, I was so shattered that I was too exhausted to actually sleep. The next day would start, and I\u2019d do it all over again.\n\nIt took a while to come to terms with the idea of using a wheelchair, and to feel like I \u201cdeserved\u201d it, like I was disabled enough. But eventually, it just made sense. I\u2019d already crossed the mental hurdle of using a walker, so transitioning to a wheelchair felt like the next step. The people around me already saw me as someone who used mobility aids, so I knew it wouldn\u2019t be a huge shock.\n\nAustralian summers are brutal, and I\u2019d always struggled with the heat, but since the accident, my intolerance had gotten so much worse and started earlier in the season, and I knew I couldn\u2019t face another summer relying only on my walker.  I started seriously looking into power chairs then, but it wasn\u2019t a quick or easy decision. I did a lot of research, talked to my OT and physio, and got great advice from other wheelchair users, before finally deciding on the Whill C2.\n\nThe NDIS, which is basically our version of disability insurance here in Australia, didn\u2019t cover it, so I had to fund it myself. That was a huge barrier. I\u2019d actually talked myself out of getting one for months until I met someone at a disability expo who let me try theirs, and I realised it was exactly what I needed. I was able to get a $5,000 no-interest loan through a low-income support program, but I still had to come up with the remaining $4,000 upfront. As a single parent on disability and unable to work, that was a big stretch, and honestly part of why I waited so long to take the leap.\n\nI\u2019m so glad I did though.\n\nI\u2019ve had my chair for about a month now, and this week was the first time I felt up to going a bit further with it. Up until now, I\u2019d just been using it for the school run, which is about a four-mile or 6.5 km round trip, but this week I actually managed a full day out plus two shorter trips. I took it into the city to run errands, went to a disability expo, and even took my son to a birthday party this afternoon. I know I've over done it, and I'll suffer for it, but I was also able to overdo it, it wasn\u2019t completely impossible, and that\u2019s the difference. I got to choose to do those things rather than miss out entirely.\n\nBefore, I\u2019d have had to pick one of those things and skip the rest, knowing I\u2019d pay for it later anyway, eventually I just wasn't able to do most things. Now I can actually do them and still have something left in the tank, as long as I prioritise resting afterwards. Tomorrow I\u2019m heading to church, which I\u2019ve really missed over the past year and a half. Since getting my wheelchair, I\u2019ve been able to go back three times already, which is something I honestly thought might never happen again.\n\nIt\u2019s definitely been a learning curve, and not everything has gone smoothly, but I\u2019m so thankful I went for it. The difference it\u2019s made is massive. Getting used to the newness of it all has been challenging, but so worthwhile.  \n  \nI wanted to share my experience with all of this, because I know how isolating it can feel when your chronic illnesses limit your life and become disabilities, but you start doubting if you\u2019re \u201cdisabled enough\u201d to ask for help or whether you're entitled to using mobility aids.   \n  \nIf your chronic illnesses are disabling to the point where you\u2019re wondering if you\u2019re \u201cdisabled enough\u201d for a wheelchair, or a walker, or any other mobility aid, please talk to your doctor, OT, or physio. I put it off for way too long, and I really wish I\u2019d done it sooner.  In the last eighteen months, I\u2019d completely lost the person I was before. But in the month that I\u2019ve been a wheelchair user, I finally feel like I\u2019ve found myself again. \n\nxx",
    "flair": null,
    "score": 973,
    "comment_count": 27,
    "created_at": "2025-10-18T11:44:39+00:00",
    "top_comments": [
      {
        "id": "nk4oygw",
        "score": 33,
        "body": "Wow congrats! You have been through a lot. I also have ME/CFS, POTS, HDS and got my Whill C2 delivered a couple of days ago! I hope it helps me as much as yours has been helping you already. Sounds like it was much needed and improving the quality of your life. Can't imagine those Australian summers, yowch! Enjoy your chair, and wishing you lots of successful pacing."
      },
      {
        "id": "nk5h73z",
        "score": 10,
        "body": "Yay! you got your chair! I am very inspired by your story about this because I am homebound right now and falling almost daily, which is pretty terrifying. Also, when I push myself, it feels good and I feel like I\u2019m making muscle, but then I have insane fatigue to try to rest and gain strength again. I\u2019m going to be looking for a used chair here in Colorado."
      },
      {
        "id": "nk5n9tb",
        "score": 10,
        "body": "I'm so glad your life is improving.  I'm living in a sober living house rn and one of the women here had a car accident and no longer has a knee in one of her legs.  She was told by her doctor she would need a wheelchair and she's been refusing it.  Yesterday she had a fall, but she refuses to use a chair, even if she is given access to one.  I wish there would be something we could do because she is in constant pain from walking"
      },
      {
        "id": "nkc4i09",
        "score": 9,
        "body": "We are strongly told, hinted and encouraged to NEVER use a mobility device, especially a chair, because THEN, we are disabled! Lol. Many people believe that once you get in a chair, you will never get out\u2026 which is absolutely ridiculous, we just get to do things that we couldn\u2019t do before, or we couldn\u2019t do without extreme pain or consequences."
      },
      {
        "id": "nk5q676",
        "score": 7,
        "body": "Thank you for sharing. Fellow MECFS hEDS friend- electric wheelchairs are the best!"
      },
      {
        "id": "nkcauic",
        "score": 5,
        "body": "Wheelchairs --chairs with wheels--are freedom!!  They are a crucial tool there's no reason to go without if you have any difficulty staying on your feet/walking enough to live how you want to. \n\nAnyone trying to gatekeep that doesn't understand how solidarity or access works.\n\nCongrats!!"
      },
      {
        "id": "nk61vg6",
        "score": 4,
        "body": "It looks comfy, I like how it lets your knees and feet rest"
      },
      {
        "id": "nkcb140",
        "score": 4,
        "body": "Allllll the prevailing beliefs around wheelchairs are wildly warped by ableism."
      },
      {
        "id": "nk6ctfk",
        "score": 3,
        "body": "Oh I'm so happy for you! That's an awesome chair (does that one break down and fit in a car trunk/boot?) I'm a big fan of using mobility aids to conserve your energy for getting things done and having fun once you get there... it's definitely a mental and emotional adjustment, but you've taken a chance and now the sky is the limit \ud83d\udc4f\ud83c\udffb\ud83d\udc4f\ud83c\udffb\ud83d\udc4f\ud83c\udffb"
      },
      {
        "id": "nkcp6ls",
        "score": 3,
        "body": "I don\u2019t think I can possibly like your comment enough. Wish I could give more likes. I am not yet at the point of needing a wheelchair. But I use a cane and have been for over a decade several years ago. I got a Rollator walker with a fold down seat. Using it in places like shopping malls, and such where the temperature is steady and you\u2019re not dealing with bad weather I was able across the span of a week to complete many 5K walks and I have a whole rack of metals to show for it. I went through a bad spell, followed by breast cancer, which being off certain meds made my chronic illnesses even worse. I\u2019m just starting to get back to my usual self but last year I knew I couldn\u2019t do things that I had done before that even the walker would not be able to help me with such as going to Renaissance fairs Something I look forward to every year as does my husband. We finally bought an electric scooter. I call it zippy lol. It allows me now to spend a day shopping at the mall with my husband or going to a park that has walking trails and even the Ren fares. This thing can handle some rough terrain. It has given me so much freedom. In the back of my mind, I know that probably someday I will need a chair and I love reading about how getting a chair has helped someone regain parts of their life. You are correct having these device devices allow allows us to do more to do things thatwere completely off the table and that makes them worth it. Much respect to everyone who takes that leap."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1mvkzx3",
    "title": "Decorating my Walking Canes - Complete",
    "body": "Art student \nI decorated an old cane for a class project and my professors encouraged me to do the ones I use daily. Since they\u2019re a set I decided to go opposites that attract instead of matching, like yin yang. \n\nDecided to go all out because if they\u2019re gunna stare anyways let\u2019s give them something\u2019s stare at.\n\nInspired by Hades and Persephone \n\n**Last picture is before\n",
    "flair": "Image",
    "score": 953,
    "comment_count": 110,
    "created_at": "2025-08-20T17:16:19+00:00",
    "top_comments": [
      {
        "id": "n9r6pcw",
        "score": 63,
        "body": "Wow. I'd ask you to do something like that for me if I took better care of it. As is, I use it to whack the bumper of cars in the crosswalk. I also use it as a drum stick on surfaces because I can't clap with one hand. \n\nYou may be interested in making some and gifting them to the Easterseals Foundation or any other well recognized Disability orgs that can display them. This would both be a way for them to display disability art but also gain recognition for your work. Either way, they deserve to be shared with a wider audience."
      },
      {
        "id": "n9rb931",
        "score": 44,
        "body": "Bhahaha I do that to with my other canes and will have to refrain now \ud83d\ude02 that and busting ankles when people kick my cane (inattention) \n\nWow um I\u2019ve never considered that they could be put on display as an actual art piece \ud83e\udd79 it\u2019s giving happy tears that you think they are good enough for that"
      },
      {
        "id": "n9rhno8",
        "score": 22,
        "body": "Us in the disability community have voices, our work has merit. I made a documentary about my life as a traumatic brain injury survivor that got into Festival and won some (albeit minute l minor) awards. \n\nJust keep working on them, refining your style and method. You're the only person creating art like this, you're an original. Imagine a gallery owner in SOHO explain \"they turn the stigma of having a disability on their heads, using the crutches not as support for weakness, but as a source of power to amplify strength. The asking price is here in the ledger\""
      },
      {
        "id": "n9rca1l",
        "score": 19,
        "body": "I have 2 back ups, but they are still functional, I plan to use these daily. The black (right) one I use more so it\u2019s less flamboyant, I use 1-2 depending on severity of symptoms. I\u2019ve also been testing them throughout the process to make sure I could still easily use them. The black one I\u2019ve also been putting through durability tests, and was initially having problems with the spikes and flowers but I layered different strength superglue, epoxy welding glue, and sealant for the final draft. I\u2019m sure I\u2019ll have to update them every now and then but that\u2019s okay to me. Since I went back in with the second layer of epoxy nothing has moved, but trial and error is good so I can make them better. My BF suggested I sell or make them for other people but it needs to be extremly durable before that stage."
      },
      {
        "id": "n9raswr",
        "score": 17,
        "body": "They look incredible, I love the theme and I mean absolutely no offense, but are they still practical? I just know how much I bump mine into stuff or drop them (which is both a daily event lol) and as an artist I'd hate to put in this much blood sweat and tears into a project (and for it to turn out this great) just for it to get damaged.\nAre they for daily use or do you have backups in case you need to go somewhere you know they might get dirty or damaged?"
      },
      {
        "id": "n9rlvu1",
        "score": 14,
        "body": "I love this. I have a heavily decorated wheelchair. I think it\u2019s great to express style with your aids. Love that they don\u2019t match. I love a good clash."
      },
      {
        "id": "n9revch",
        "score": 13,
        "body": "Oh damn, I didn't even see the knee rest before you mentioned it. How have I never seen crutches with knee rests before? They seem really practical"
      },
      {
        "id": "n9rdrjh",
        "score": 12,
        "body": "They can honestly even still be collapsed or height adjusted, though I never used those features before. It\u2019s more time consuming to do those things now but I already needed tools to do it because of the knee rest so \ud83e\udd37\u200d\u2640\ufe0f"
      },
      {
        "id": "n9qy2tx",
        "score": 8,
        "body": "those are so freaking cool omg"
      },
      {
        "id": "n9rx0ly",
        "score": 8,
        "body": "Hell yes! Everyone loves \"outsider art\" though that term is so degrading. Highlight the disability angle and you'll get greater recognition. It's a shame but it's a way to set yourself apart."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1lzyewm",
    "title": "Every establishment needs this sign",
    "body": "",
    "flair": null,
    "score": 946,
    "comment_count": 234,
    "created_at": "2025-07-14T21:00:19+00:00",
    "top_comments": [
      {
        "id": "n35piah",
        "score": 241,
        "body": "I use a wheelchair in public and often have the issue of the stall being occupied. But I assume they need the stall because of a disability I can\u2019t see.\n\nImo if someone abled and healthy is using an accessible stall, this sign won\u2019t stop them."
      },
      {
        "id": "n35a2fs",
        "score": 194,
        "body": "As someone with mostly invisible disabilities, please let\u2019s *not*. I get enough dirty looks as it is."
      },
      {
        "id": "n35s01m",
        "score": 86,
        "body": "[removed]"
      },
      {
        "id": "n35dcdr",
        "score": 80,
        "body": "You\u2019re missing the point.  u/zz9za may need the disabled stall, but since they have an invisible disability, others may think they\u2019re using it for the ambiance and give them a hard time.  \n\nI also have an invisible disability and use the disabled stall.  I don\u2019t feel the need to share that info with coworkers, nor do I want to be subjected to their judgmental stares."
      },
      {
        "id": "n35v33x",
        "score": 64,
        "body": "Yeah and sometimes the baby thing is in the disabled stall."
      },
      {
        "id": "n3631jg",
        "score": 63,
        "body": "I literally just went to an event the other day and had this dilemma. Many of the Stalls were full but the handicapped one was open, and I know that I'm allowed to use it obviously since I'm disabled, but I definitely don't look like I am at all, and I didn't want to be judged, or seem like a terrible person.\n\nI decided to just wait until the regular stall was open. I just told myself that even though people wouldn't judge me if I had a Mobility Aid like a cane of some sort, I should still just be grateful that I'm not at the stage where I need to use anything like that yet."
      },
      {
        "id": "n35snh4",
        "score": 63,
        "body": "In the UK we have a sign which says \nRemember not all disabilities are visible.\n\nYou can have both signs.\nDisabled toilets aren't for being sick in, having a poo when not disabled, or taking drugs"
      },
      {
        "id": "n3620a0",
        "score": 41,
        "body": "That drove me crazy when I had a child small enough to need to use it. I\u2019d be trying to hurry so fast, still being careful that my son didn\u2019t roll off, mentally preparing an apology if a disabled person was waiting\u2026. I don\u2019t know what genius thought of that. Sure there needs to be one in the disabled stall for disabled moms but put another one out for those who need one too."
      },
      {
        "id": "n36ekgw",
        "score": 37,
        "body": "I have to use it occasionally because I need the bars to get up and down, and they are generally bigger, so if I pass out, I generally only smash my face and not everything else"
      },
      {
        "id": "n3ds36k",
        "score": 33,
        "body": "No, they weren't being considerate. They ignored their needs in fear of public judgement"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1od405a",
    "title": "this one got me rolling",
    "body": "",
    "flair": null,
    "score": 926,
    "comment_count": 60,
    "created_at": "2025-10-22T09:54:53+00:00",
    "top_comments": [
      {
        "id": "nkr6f0a",
        "score": 266,
        "body": "Reminds me of that one tiktok where a guy w a prosthetic leg was given a ticket for parking in the handicap spot because he didnt look handicapped. He had to take off his leg to prove it. It was both funny and sad"
      },
      {
        "id": "nkr5mi2",
        "score": 165,
        "body": "it looks like they are saying men are disabled \ud83d\ude02 or atleast that\u2019s what I got"
      },
      {
        "id": "nks0r5o",
        "score": 158,
        "body": "Ah, the three genders: cane users, wheelchair users, and men."
      },
      {
        "id": "nkr5kdj",
        "score": 125,
        "body": "\ud83d\ude02 I know the implication here is that they don\u2019t use a disability aid but the way it just looks like they are saying men are disabled \ud83d\ude02"
      },
      {
        "id": "nkr4mrl",
        "score": 114,
        "body": "Rolling as in laughing? Why?"
      },
      {
        "id": "nkr8lzp",
        "score": 105,
        "body": "Didn't your wheel chair get you rolling? /jk"
      },
      {
        "id": "nks53vl",
        "score": 88,
        "body": "He didn\u2019t \u201chave to\u201d do anything. That\u2019s fucked up if they didn\u2019t believe him."
      },
      {
        "id": "nku2fui",
        "score": 82,
        "body": "Oh we don\u2019t \u2018have to\u2019 prove our disabilities to anyone, but after years and years of people saying that stuff it gets to a point where you just show it off to spite them and humiliate them for being dumb lol. Same with my Ostomy when I go to the accessible stall and people call me out, Like okay, no one else is using it and I need lots of squatting space, would you like to see the bag of shit? I can absolutely show you if you want to. Most people apologize sometimes I get the \u201cI don\u2019t believe you\u201d crap. Bam. Flash the bag \ud83d\ude05"
      },
      {
        "id": "nkt0zqh",
        "score": 44,
        "body": "They see me rollin. They hating.\u00a0"
      },
      {
        "id": "nksccc5",
        "score": 38,
        "body": "It is unintentionally saying that being a man is a disability which is very funny for OP (and me haha) because the message is clear but to OP, it looked awkward haha"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1nuk2xa",
    "title": "\"Too potato-y\"...Thought this belonged here!",
    "body": "",
    "flair": "Image",
    "score": 927,
    "comment_count": 52,
    "created_at": "2025-09-30T17:51:23+00:00",
    "top_comments": [
      {
        "id": "nh2jqq5",
        "score": 148,
        "body": "My mom met my dad at the train museum they both volunteered for, so uh ..."
      },
      {
        "id": "nh3atkb",
        "score": 104,
        "body": "Hot take, if autism is actually becoming more common, it's because women have more freedom to choose who they have kids with and people have easier ways to meet others who share their interests. We are out here fucking each other wooo."
      },
      {
        "id": "nh1qlb3",
        "score": 59,
        "body": "OK. So Trump is claiming Autism/people being on the spectrum is due to women having taken Tylenol when they were pregnant. FWIW, this is not backed by any science or research.\n\nThe joke/humour is the part where she describes her on the spectrum type behaviour, (specific shoes and food issues), as well as her husband's (in depth knowledge of a specific topic, and inability to comprehend social cues), as being the reason why she has kids on the spectrum.\n\nI think the humour lies in the fact that it's absurd to blame being an Aut/on the spectrum on Tylonal, when the parental traits/genes are being dismissed and ignored.\n\nHope that's helpful, as I've never tried to explain a joke."
      },
      {
        "id": "nh35vum",
        "score": 44,
        "body": "So, you value volunteering?!"
      },
      {
        "id": "nh3jkn6",
        "score": 40,
        "body": "That, better testing and those of us with disabilities/NDs/MH/etc not being locked away out of site. When I was growing up in the UK, cancer was still referred to as the \"Big C,\" or some such. My Grandma got either cervical or bowel cancer in the late seventies, and the disease wasn't even talked about, let alone the type. Yes, I am ancient."
      },
      {
        "id": "nh35ozc",
        "score": 33,
        "body": "Two of my children are on the spectrum. It took YEARS before my MIL would admit that half of the men on my husband's side were. We ALL knew. Everyone KNEW."
      },
      {
        "id": "nh3ess0",
        "score": 21,
        "body": "Yes? I mean this was the 60s and 70s for them but Dad's train museum work led to a lifelong career without going to college for electrical engineering or physical engineering. Not that that is something that would happen nowadays. But I would volunteer if I could at a train museum or at the aquarium like Mom is in retirement or elsewhere. I'm just too sick to manage it now and neither a train museum nor the aquarium is anywhere near me. I've thought about volunteering at the local art community when I'm more able. I'd also love a job. What I have is surgeries and disability and the need to start the ssdi paperwork. Yay."
      },
      {
        "id": "nh1s8ep",
        "score": 20,
        "body": "This was my impression as well, good explanation"
      },
      {
        "id": "nh453pv",
        "score": 18,
        "body": "I enjoy constantly pointing out things my parents do that are either autistic or adhd. Every time my poor dad is like \"I didn't know that\" or \"are you sure?\" And I'll turn to him as deadpan as possible and tell him \"who sang (insert lyrics here)\" and he can tell you the song name, album name, singer name and year without skipping a beat."
      },
      {
        "id": "nh2215f",
        "score": 18,
        "body": "Yes. My understanding is those traits she is describing would be generally associated with people on the spectrum. It's far more likely that the genetic material of your parents play a massive part of your makeup, than some rigorously tested, 140+ year old, over the counter drug like acetaminophen.\n\n*Whether you call it acetaminophen (in the United States and Japan) or paracetamol (in Europe and most of the rest of the world), it\u2019s one of the most widely used pain relievers. It was first prepared by H. N. Morse in 1878. Although many studies on its use as an analgesic were performed, it wasn\u2019t until 1950 that it was marketed under the name Triagesic. Today, its most common trade names are Tylenol and Panadol, but a large percentage of its sales are as a generic drug.*\n\n[https://www.acs.org/molecule-of-the-week/archive/a/acetaminophen.html](https://www.acs.org/molecule-of-the-week/archive/a/acetaminophen.html)"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1k3pk9f",
    "title": "After 2 years in a wheelchair, Martin and I are finally getting off the couch!!",
    "body": "I am so full of gratitude for the people that donated to my fundraiser. I got my Firefly 2.5 this week. If anyone wants a bit of a review, I can elaborate more. \n\nWe went FAST. I had to test it without having Martin on a leash. Walking him on leash in my wheelchair had me crashing into curbs \ud83d\ude06\n\nI know he's smart. But it's been awhile since we went out together. This dog fell right into a trot next to me off leash. \n\nI cannot begin to explain how I feel. It feels like my life is in a new chapter. ",
    "flair": null,
    "score": 918,
    "comment_count": 67,
    "created_at": "2025-04-20T15:50:41+00:00",
    "top_comments": [
      {
        "id": "mo3vuz8",
        "score": 42,
        "body": "Here is to the new chapter in your life, may it be filled with happiness and good fortune!"
      },
      {
        "id": "mo4faot",
        "score": 18,
        "body": "I've been so blessed. I had no idea so many people actually cared about me. I've felt very isolated for so long, seeing those donations continues to make me speechless"
      },
      {
        "id": "mo3zy0j",
        "score": 15,
        "body": "You both look so happy!"
      },
      {
        "id": "mo40kpz",
        "score": 15,
        "body": "There was a bit of screaming \ud83d\ude2c"
      },
      {
        "id": "mo3xwyp",
        "score": 14,
        "body": "that looks awesome and congrats on getting the firefly.   Keep them wheels a rolling onto new adventures with Martin!"
      },
      {
        "id": "mo4m5ep",
        "score": 9,
        "body": "You\u2019re a human being, of course people care about you! I can tell by your smile and how happy your dog looks that you have a good heart."
      },
      {
        "id": "mo3x5lg",
        "score": 8,
        "body": "I\u2019m so happy for you and Martin."
      },
      {
        "id": "mo4g3j5",
        "score": 8,
        "body": "It's kind of post that definitely puts a smile on me. I'm so glad the people can't help you. You and your puppy joy that will share and Firefly do the max. Best wishes to you and your puppy!"
      },
      {
        "id": "mo3yhao",
        "score": 7,
        "body": "So happy for you!"
      },
      {
        "id": "mo4bsxu",
        "score": 7,
        "body": "You both look so happy!! I am thrilled for you!!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1oxm5gr",
    "title": "Alice Wong writer of Teen Vogue's Disability Visibility column, has Died.",
    "body": "",
    "flair": "Article / News",
    "score": 895,
    "comment_count": 44,
    "created_at": "2025-11-15T08:04:59+00:00",
    "top_comments": [
      {
        "id": "noy5k4h",
        "score": 134,
        "body": "It\u2019s so hard to believe. I\u2019ve only known of her existence for a few years but her work was so impactful to me that I can\u2019t imagine a world without her in it."
      },
      {
        "id": "noy9mpt",
        "score": 100,
        "body": "I read Disability Visibility last year and it was really helpful for me being newly diagnosed. Sad to hear this"
      },
      {
        "id": "noye7nc",
        "score": 54,
        "body": "Oh shit, this is terrible. She was a great writer and activist. This is a huge loss."
      },
      {
        "id": "nozlvm0",
        "score": 54,
        "body": "[Here is an article](https://time.com/6960765/alice-wong-muscular-dystrophy-essay/) Alice wrote last year (2024,) for Time Magazine.\n\nRest in Power, Alice."
      },
      {
        "id": "noyzyai",
        "score": 48,
        "body": "And this is shortly after they ended her column (and canned their political writers) :("
      },
      {
        "id": "noy7tfl",
        "score": 46,
        "body": "I never had the fortune to meet her myself, but she was local and we had mutual friends. This is devastating, may her memory be a blessing..."
      },
      {
        "id": "noyhepm",
        "score": 37,
        "body": "Oh Alice, you've been such an amazing role model to me the past few years. I will miss you. Thank you for all you've done for us."
      },
      {
        "id": "noyxvmi",
        "score": 35,
        "body": "No, not Alice! Oh man, that's terrible news.\n\nHer books are wonderful, this is a huge loss for the community and the world. She was a light in the darkness for a lot of us."
      },
      {
        "id": "np0cii7",
        "score": 26,
        "body": "This is so sad. Only 51 years old. But she achieved so much in her life. I love this shot of her virtual visit with Barack Obama, it really captures how progressive she was despite her limitations. I hope she\u2019s able to feel free again and at peace. \n\nhttps://commons.wikimedia.org/wiki/File:Alice_Wong_participated_at_the_25th_anniversary_of_the_Americans_With_Disabilities_Act_via_robot_(cropped).jpg"
      },
      {
        "id": "noziurn",
        "score": 25,
        "body": "Me too. It was also around last year that I read Disability Visibility and I really needed it to process a lot of self hate. The world is going to miss her"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1nzpnku",
    "title": "It is a horror movie",
    "body": "",
    "flair": "Image",
    "score": 878,
    "comment_count": 68,
    "created_at": "2025-10-06T17:34:15+00:00",
    "top_comments": [
      {
        "id": "ni3ufh9",
        "score": 69,
        "body": "Sponsored by the Trump administration"
      },
      {
        "id": "ni4mfr9",
        "score": 44,
        "body": "It was always a hard process but I will say this is the worst time in history to be applying"
      },
      {
        "id": "ni4yt9k",
        "score": 30,
        "body": "I just got notice that my benefits are being eliminated because I went back to work part-time. The system is a joke."
      },
      {
        "id": "ni3sv5q",
        "score": 20,
        "body": "I needed this \ud83d\ude2d"
      },
      {
        "id": "ni422o9",
        "score": 20,
        "body": "r/disabledmemes"
      },
      {
        "id": "ni5b8aa",
        "score": 17,
        "body": "Thanks. The main reason I went back to work is because it\u2019s really hard to get by on $1500 a month these days. And all I really did was trade my SSDI benefits for the same amount of pay each month. Pretty pointless."
      },
      {
        "id": "ni7vf89",
        "score": 12,
        "body": "Oh..then no need to even apply. That money needs to be used for a much needed ballroom."
      },
      {
        "id": "ni4mo0l",
        "score": 12,
        "body": "I just so happened to have applied last July... lol f my life"
      },
      {
        "id": "ni82aer",
        "score": 11,
        "body": "when my brother lost his leg he applied for disability and they told him \u201cyou are not disabled, you are dismembered,\u201d"
      },
      {
        "id": "ni59x7a",
        "score": 11,
        "body": "What bullshit!  I\u2019m so sorry to hear this"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1lhdmr6",
    "title": "Anyone else have a disservice animal?",
    "body": "This will always be my favorite joke. My girl thinks my chair is for her and I often have to try and prevent her from getting back in while I transfer ",
    "flair": "Image",
    "score": 851,
    "comment_count": 82,
    "created_at": "2025-06-22T02:50:12+00:00",
    "top_comments": [
      {
        "id": "mz3husc",
        "score": 193,
        "body": "I have an emotional abuse cat. Keeps me from getting too arrogant."
      },
      {
        "id": "mz3ync7",
        "score": 141,
        "body": "My little jerk was busy licking his own crotch while I was writhing on the floor having a seizure last week.\n\nCompletely.  Worthless.  But so cute \ud83e\udd23"
      },
      {
        "id": "mz4ee1p",
        "score": 68,
        "body": "That crotch wasn't going to lick itself, was it?!?!"
      },
      {
        "id": "mz3j5h5",
        "score": 51,
        "body": "Yeah, I'm my emotional support animals' emotional support human."
      },
      {
        "id": "mz3w80m",
        "score": 50,
        "body": "I had been calling my cats my disservice animals for stealing my wheelchair for quite some time *before* discovering one of them managed to punch holes in my cushion air bladder through the cover. Then they were *really* disservice animals"
      },
      {
        "id": "mz3dhzp",
        "score": 47,
        "body": "Love this post. She is adorable."
      },
      {
        "id": "mz42u89",
        "score": 37,
        "body": "Yes. A havanese I inherited from my mom. \n\nI call her \"little momma\". She's a bully, who will jump up next to you but just out of reach, roll onto her back, and growl then bark at you until you rub her belly.  She also insists on being first one in and out of the door, will come sit in front of you and bark until she gets a treat and doesn't let you pick her up, but waits until you sit down to jump up on your lap to be scratched and petted. Then growls if you stop scratching or petting too soon, but when she's satisfied she jumps down and takes her position of authority on top of the back of the couch.\n\nEverything on her terms.  It's a love/hate thing we have going on. She's my monster."
      },
      {
        "id": "mz3hfwd",
        "score": 25,
        "body": "I have a black hairy rug (lab mix). Some labs may be service dogs but mine is just a trip hazard."
      },
      {
        "id": "mz4pjda",
        "score": 19,
        "body": "I have a corgi, everytime I see a service corgi I'm like \"THAT jackass is your service animal?\""
      },
      {
        "id": "mz5a663",
        "score": 18,
        "body": "There is a TikTok where the woman is talking to her dog and tells him \u201cI adopted you to help with my anxiety, but im pretty sure now your anxiety is worse then mine\u201d"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1mr9dfv",
    "title": "Perfect Card For The Nosy Parker.",
    "body": "A lot of us are exhausted by not only trying to negotiate living in an ableist world, but having to answer (well meaning) strangers poking their nose into our personal business. I saw this and knew that I had to share it here! Enjoy.",
    "flair": null,
    "score": 850,
    "comment_count": 71,
    "created_at": "2025-08-15T20:29:05+00:00",
    "top_comments": [
      {
        "id": "n8wsuuk",
        "score": 97,
        "body": "I'd like to add \" no one's prayers has helped\""
      },
      {
        "id": "n8wkd03",
        "score": 41,
        "body": "please tell me the back of the card is a single emoji : \ud83d\udd95\ud83c\udffb"
      },
      {
        "id": "n8wwhvm",
        "score": 40,
        "body": "id also like to add \"stop judging me for what I eat/drink. no putting down the pepsi and living off milk, and x diet will cure me.\"\n\n\"Yes i am aware i am young that doesnt change the fact I need a rollator. yes I'm aware that when you were my age you did some demanding psychical activity.\""
      },
      {
        "id": "n8xkhlg",
        "score": 24,
        "body": "Absolutely blows my mind how many people act genuinely shocked about young/non-elderly people using certain aids. I\u2019ve had hearing aids since I was 4, and I\u2019m far from alone. Plenty of people use wheelchairs, canes, walkers, or crutches from the time they are toddlers."
      },
      {
        "id": "n8xicn7",
        "score": 22,
        "body": "Omg yesss and my parents weren\u2019t chosen by God to love and nurture me! \ud83d\ude02\ud83d\ude02"
      },
      {
        "id": "n8wx2yf",
        "score": 17,
        "body": "\u201cBut have you tried yoga?\u201d Is a famous one for me \ud83d\ude02"
      },
      {
        "id": "n8xdphg",
        "score": 16,
        "body": "I'd like to add, \"Illness and pain do not care about age.\"\n\nI've had to say that to so many people in the last 2 years."
      },
      {
        "id": "n8wzw6e",
        "score": 14,
        "body": "It hasn't \"fixed\" me, nor do I expect it to.  But I absolutely do believe prayers and good wishes and positive thinking and good vibes (and whatever else folks wanna call it) have often made things easier to accept/cope with.\n\nSometimes it's just nice to know people wish good things my way."
      },
      {
        "id": "n8wzv8f",
        "score": 13,
        "body": "Oh yes! I don't drink, smoke or eat animals, but my meds blew me up. People think that workouts we can't do, lifestyle changes we tried, or some crap they believe in will crack the code. Same twats who swear masks are torture and Bovine Dewormer stops COVID."
      },
      {
        "id": "n8x8kup",
        "score": 12,
        "body": "People always suggest I try marijuana, lol."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1pik3qa",
    "title": "Apparently I am a prop for my son's amusement...",
    "body": "This was at the National Space Centre in Leicester, which does have an accessible lift.",
    "flair": null,
    "score": 839,
    "comment_count": 46,
    "created_at": "2025-12-09T21:38:26+00:00",
    "top_comments": [
      {
        "id": "nt6s57h",
        "score": 275,
        "body": "image description: a person in a wheelchair poses next to a sign reading \u201cWhy not take the stairs? There are 54 steps to the next exhibition deck, which is a third of the distance travelled by the Sojourner mars rover in 1997.\u201d"
      },
      {
        "id": "nt7af9l",
        "score": 252,
        "body": "Alt text is an accessibility tool"
      },
      {
        "id": "nt79ng7",
        "score": 171,
        "body": "nuh uh"
      },
      {
        "id": "nt74wsy",
        "score": 161,
        "body": "\ud83e\udd23 cheeky \ud83e\udd23\n\nMy wife will absolutely do the same to me given the chance \ud83d\ude0a"
      },
      {
        "id": "nt7bhw5",
        "score": 150,
        "body": "It's not an analysis, it's a description, and it can help people using text-to-speech."
      },
      {
        "id": "nt8wdk4",
        "score": 129,
        "body": "Okay, even if they were a bot, a bot that provides alt text is a GOOD thing. They should honestly have one available, as writing alt text can be tricky for some folks"
      },
      {
        "id": "nt7clfk",
        "score": 111,
        "body": "Oh thats neat! Thanks for doing that. I just had not seen anybody do that before!"
      },
      {
        "id": "nt7ubjc",
        "score": 86,
        "body": "Thanks! Provided some good insight!"
      },
      {
        "id": "nt7u1xm",
        "score": 85,
        "body": "You may want to read [this post](https://www.reddit.com/r/disability/s/DPsyEokX1p)."
      },
      {
        "id": "nt7uetd",
        "score": 62,
        "body": "because some people are blind?"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1qc5vym",
    "title": "Autistic woman who with a brain injury and can\u2019t walk is abducted by ice out of her car: posted in r/Minnesota today",
    "body": "I knew this would be next. Motherfuckers. This would be me.  Would it be you?\n\nAutistic lady with brain injury who can\u2019t walk and is going to doctors appointment gets abducted. \n\nI have\u2014TBI, mild, cognitive impairment and neurological complications I am an ambulatory wheelchair user. I still drive. \n\n",
    "flair": "Image",
    "score": 807,
    "comment_count": 133,
    "created_at": "2026-01-13T22:41:01+00:00",
    "top_comments": [
      {
        "id": "nzfuamv",
        "score": 314,
        "body": "I saw this. The fact 1930s Germany started with culling disabled and LGBT+ says it all. What\u2019s going on is outright fascism and I don\u2019t get why so many cannot see it. It\u2019s scary, it\u2019s real. It\u2019s not going to end until citizens start full on fighting back and start the beginning of the end for it. However horrid and scary that may sound. 2nd amendment is there to protect yourself against this. They have no jurisdiction to randomly take people because they don\u2019t like you, especially citizens. They have no rights to raid houses, businesses or other places as they have no warrants. This is all illegal and is disgusting that there are still far too many people thinking this is ok. It is not ok. This is the same reason Anne Frank and her family hid in an attic. This. Douglas Kelley tried to warn the US and no one wanted to listen back then! He knew all those decades ago already"
      },
      {
        "id": "nzg9bug",
        "score": 168,
        "body": "I am very much like this woman. Autistic with neurological disorders, and I have a spinal implant for paralysis issues. I\u2019ve been sitting here rewatching this and ruminating on it since just a few minutes after you posted this. I\u2019m getting to the point with all of this where my grief, shock and panic is so immense that I can\u2019t formulate words to describe the emotions anymore. So intense it\u2019s actually triggering my aphasia horribly\n\nI\u2019ve been scared of this since trump was first elected years and years ago because of what was happening then, it\u2019s getting worse every day. I don\u2019t know why I feel like it\u2019s gone so fast but it\u2019s been a decade of my life of this fear growing and life getting harder because of the policies of that man."
      },
      {
        "id": "nzg0l4w",
        "score": 118,
        "body": "Yeah... Not a surprise.\n\nKilling pets, Random people, Prison camps, Murder of an innocent mother... Yeah.\n\nSorry americans."
      },
      {
        "id": "nzgjfqs",
        "score": 96,
        "body": "Not to mention ICE isn\u2019t documenting everything they do, so there\u2019s no real way to tell how many people they\u2019re putting in chokeholds and taking against their will and everything."
      },
      {
        "id": "nzfv5ds",
        "score": 52,
        "body": "Even though this was more incidental for this woman, it won't be when they start going house to house. They did it 90 years ago.\u00a0\n\n\nMy advice is to go dark where you can. Pay cash for as much as possible. Obfuscate your social media presence. Use VPNs.\u00a0 Get off minimally necessary medication. Go to the store before dawn or after dusk. Of you can lower your medical footprint, do so.\u00a0"
      },
      {
        "id": "nzgky9r",
        "score": 51,
        "body": "Exactly this. I\u2019m glad people are recording things. Folks need to download and save those videos on an external drive. All will become evidence"
      },
      {
        "id": "nzg33f8",
        "score": 48,
        "body": "I hate this country\u2026"
      },
      {
        "id": "nzgcb00",
        "score": 45,
        "body": "Beyond angry, nauseating, sickening, can\u2019t sleep.\n\nTomorrow morning I\u2019m literally doing what she was doing."
      },
      {
        "id": "nzfrrow",
        "score": 41,
        "body": "The link:  https://www.reddit.com/r/minnesota/s/g9oGNAEFf0"
      },
      {
        "id": "nzg9xkx",
        "score": 37,
        "body": "Yes, me too\ud83d\udc80\ud83e\uddca"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1lc4kce",
    "title": "I'm sorry",
    "body": "My girlfriend has several disabilities including severe allergy induced asthma, Celiac and ADHD. We were at a wedding yesterday where she was not able to eat anything, even though the bride wanted her to be able to eat, and asked us months ago how to accommodate her. \n\nThere's also been so many instances of event staff telling us that pets will not be present in the venue, just to find out when we arrive that there are pets (not service animals, which we totally would have been understanding of) and we could only stay an hour or two before she gets an asthma attack.\n\nAs an able bodied person, I used to be in the \"it's impossible to accommodate everyone\" camp. But I'm seeing now that this phrase is only used as an excuse by people who don't even want to try to accommodate. \n\nI'm sorry that as a society we failed you, I wish we could be better from now on. Just remember that your disabilities are not a burden and you deserve accessible and welcoming spaces \u2764\ufe0f",
    "flair": "Rant",
    "score": 793,
    "comment_count": 151,
    "created_at": "2025-06-15T16:34:28+00:00",
    "top_comments": [
      {
        "id": "mxxn2ph",
        "score": 442,
        "body": "You\u2019re not the only one, friend. Before my accident, I would see a wheelchair accessible toilet and think cool, this coffee shop is accessible. I wouldn\u2019t notice the door thats too narrow for a chair, or the fact the counters are too high. \n\nI\u2019ve learned that 99% of \u201caccessible\u201d places are not indeed accessible. It\u2019s a hard pill to swallow."
      },
      {
        "id": "mxxush5",
        "score": 151,
        "body": "Yeah, I used to think we are doing pretty good on accessibility but now I see we're nowhere close to how it should be. And also that it isn't up to the able-bodied people to decide when accessibility is \"good enough\". I'm sorry that things are so bad."
      },
      {
        "id": "mxyh3yg",
        "score": 107,
        "body": "> And also that it isn't up to the able-bodied people to decide when accessibility is \"good enough\".\n\nYou can say that again. I get so frustrated when people say, \"But it meets the ADA requirements.\" The ADA is a starting point, the ADA isn't all encompassing. The person asking to have their needs met is the expert on their disability and accessibility requirements."
      },
      {
        "id": "mxxno7n",
        "score": 99,
        "body": "People are willing to accommodate you until it requires they actually do something and then all the excuses start raining down."
      },
      {
        "id": "mxxzdzb",
        "score": 67,
        "body": "My girlfriend says she often has to pretend to be perky and friendly when asking for accommodations, while extremely anxious that she will be rejected, just to maximize the chances. It must be so exhausting. Sometimes I think able-bodied people are the disabled ones cause the lack of empathy is crazy lol"
      },
      {
        "id": "mxxmrbp",
        "score": 61,
        "body": "Thank you. For the most part, our accommodations are not that big of things. We have \u201csafe foods\u201d that we are able to eat(a lot of disabled people have these. Not just austic people). The event people should\u2019ve absolutely asked what your girlfriend\u2019s safe foods are and gotten them. It\u2019s really sad and frustrating that most of the time, we don\u2019t get our accommodations even though they are not big things. I\u2019m not asking for an entire couch. I\u2019m just looking for a simple chair somewhere in a room that doesn\u2019t usually have them. I\u2019m so sorry for you and your girlfriend"
      },
      {
        "id": "mxxwttl",
        "score": 57,
        "body": "Staying in a hotel at present and the beds are too high, I need assistance to get in and out, toilet is too low have to grab door handle to get up. Shower has no shelving to put shampoo or body wash.no grab rails.i shall be glad to leave."
      },
      {
        "id": "mxxp7q7",
        "score": 54,
        "body": "I'm in the same boat as you. Able-bodied, disabled partner. You really start to see how insidious it is. I'd go so far as to say the ableism is baked in. :\\\n\nHonestly though, the accommodations aren't what's hitting me, it's the medical negligence and general bigotry. The number of times I've had to explain the difference between complete blindness and legal blindness, what EDS is, how narcolepsy can affect other things downwind....  -sigh-"
      },
      {
        "id": "my0eyun",
        "score": 32,
        "body": "The saddest thing is to realize how self-centered so many Americans really are and how many really do consider disabled people to be burdens. Those people really don't think about or care about anything that doesn't affect them personally. \n\nIf you have a job, I would encourage you to help advocate for disabled people by joining a DEI committee (if your company has one) or even just scheduling a meeting with your VP of HR to discuss how your workplace could be more welcoming and inclusive for the disabled. For example, when so many companies recently returned to the office, after years of working remotely during the pandemic, it pushed a lot of disabled people out of their jobs. \n\nMy disability is very poor vision. It is dangerous for me, and for other people on the roads, to drive in dim or dark conditions, but it's been impossible for me to find a job that pays a livable wage that has a daytime only schedule. I don't have access to any public transportation nearby, can't afford to Uber everyday and don't know anyone who could drive me back and forth. If I can't find a remote job, I won't be able to work at all. \n\nAnd that's a real shame. Because I need to work, I want to work and I'm more than capable of doing great work. But if all the jobs are onsite, and I can't get there, it doesn't make sense for me to even apply."
      },
      {
        "id": "mxxr9kk",
        "score": 29,
        "body": "I suggest reading about the medical model of disability, how healthcare treats disabled people as problems that need fixing, and the Disability Justice movement."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1lqxccb",
    "title": "The \u201cBig Beautiful Bill\u201d just passed in the House",
    "body": "Unfortunately, the bill passed. We only got 2 republican nays and not the amount we needed. I have no idea when the bill goes into effect. Some people say next year or in 2028, but I have no idea. I\u2019m angry and scared. This is an injustice to Americans. People are gonna die and a lot of people can\u2019t work for Medicaid requirements. I have no idea what to do. I\u2019m on ssi & medicaid and working is not an option for me. The republicans have just signed the death sentence for Americans. it\u2019s truly unfair and cruel how they get to have healthcare and we don\u2019t. I\u2019m tired of this.",
    "flair": "Discussion",
    "score": 787,
    "comment_count": 399,
    "created_at": "2025-07-03T18:40:33+00:00",
    "top_comments": [
      {
        "id": "n16dv6e",
        "score": 371,
        "body": "The Congressional Republican fools were chanting \u201cUSA, USA,\u2026\u201d, after passing it. Utter disgust at these ignorant clowns."
      },
      {
        "id": "n16cjoq",
        "score": 150,
        "body": "The medicaid changes go into effect december 2026"
      },
      {
        "id": "n16cxo5",
        "score": 144,
        "body": "What the hell are disabled people who can\u2019t work gonna do?"
      },
      {
        "id": "n16dkl2",
        "score": 127,
        "body": "who will they hire to clean our dead bodies off their doorsteps"
      },
      {
        "id": "n16bz67",
        "score": 106,
        "body": "Anyone who followed republicans for years knew this is how it would go. Anyone who voted for this and chose not to vote is also responsible, they all have blood on their hands."
      },
      {
        "id": "n16jjw4",
        "score": 105,
        "body": "Nothing USA, Patriotic about it ! \n\nYes. Ignorant Clowns. But also Mostly Millionaires that get the Best Health Care and other benefits, Expenses etc... all while continuing to Lie on Fux Comedy Channel & other Right wing media that all their Voters listen to almost Daily ! And they buy it all, hook line and Sinker !!!\n\nAll on our Tax Dollars!!! They don't care about Destroying America or Us ! \n\nMy Neighbor is one of those Fux fake news watchers, he Believes what they say, plus he Never hears the Truth on Other Media Outlets !! Won't watch them ! \n\nHe asked me why I Fly my Flag upside down and didn't like my answer."
      },
      {
        "id": "n16zcvp",
        "score": 103,
        "body": "SSA: \"We've determined that you are too hireable\"\n\n\"Okay, to do what?\"\n\n\".....\"\n\n\"Okay SSA, would you hire me?\"\n\n\"Of course not, we'd have to accommodate you\"\n\n\ud83d\ude43"
      },
      {
        "id": "n16fxij",
        "score": 99,
        "body": "wtf? it took me a long time to get ssi bc i got denied once bc they didn\u2019t think i was \u201cdisabled enough\u201d. that\u2019s atrocious"
      },
      {
        "id": "n16dhgf",
        "score": 87,
        "body": "I\u2019m so sick of republicans destroying this country. I hope they all suffer with the rest of us when their dumbass votes go into effect"
      },
      {
        "id": "n16msbw",
        "score": 87,
        "body": "Yeah. I\u2019ve applied seven times for disability. They claim I\u2019m not disabled enough too but every job interview I go to says they want to hire me but I\u2019m too unreliable due to my many many disabilities."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1n8g7u1",
    "title": "don\u2019t have a child if you can\u2019t handle/don\u2019t want a disabled child.",
    "body": "when you have a child, you are automatically consenting to having ANY TYPE of child. a gay child, a child with behavioral problems, a child who wets the bed, a child who hates your interests, and yes, a disabled child. you should not have a child if you\u2019re not prepared for that possibility. ",
    "flair": "Rant",
    "score": 780,
    "comment_count": 119,
    "created_at": "2025-09-04T17:16:18+00:00",
    "top_comments": [
      {
        "id": "ncetm6u",
        "score": 283,
        "body": "*I AGREE.* \nHowever.\nNo one, absolutely no one, prepares you for that possibility when you are young. No one wants to \"scare you off\" as a potential child-bearer, so everyone tiptoes around you and tells you none of the possible things that could go wrong with pregnancy or child rearing. They just tell you what a blessing children are and how great it is to be a parent."
      },
      {
        "id": "nceu54i",
        "score": 112,
        "body": "i agree and i think that\u2019s BS! when unprepared parents have kids and don\u2019t consider that their child could be born disabled, disabled kids end up in homes with resentful parents who don\u2019t know how to care for them."
      },
      {
        "id": "nceoirz",
        "score": 105,
        "body": "I hear you. I feel the exact same.\n\nI used to tell my mother this and she would get upset because she believes her job is to mold me into whatever she thinks a good person is. And we have some major disagreements there, because her idea of a \"good person\" is religious and capitalistic. She treated me like a defective doll she couldn't take to the toy store for a refund. Just an object to create a \"Look\" for to show off to other people, but I failed at looking right, so i'm on a shelf."
      },
      {
        "id": "ncesbsv",
        "score": 66,
        "body": "i see parents of disabled kids saying things like \u201ci got the short stick\u201d and it makes me sick to my stomach. i get that parenting is hard, parenting disabled kids is hard, but you literally sign up for that when you become a parent. parents inherently sign up for a kid with down\u2019s syndrome, cerebral palsy, limb differences, any disability. i\u2019m so sorry for your experience, that\u2019s not fair. i hate that it\u2019s socially acceptable to say you wish your child were born differently as long as they\u2019re disabled."
      },
      {
        "id": "nceycoo",
        "score": 47,
        "body": "Yeah I feel you op. My parents adopted me at birth (I found out on my own at 18, suspected it most of my life though), my birth mother was on cocaine, and likely weed tobacco and possibly more while carrying me. I was cleared as a baby and toddler with no health issues (aside from eczema and a couple deficiencies). \n\nI had tons of weird and bothersome symptoms and headaches and pains growing up, I was openly and obviously depressed and severely anxious, showed signs of OCD as a child, not to mention I was blatantly and obviously autistic. And my parents constantly told me nothing was wrong with me, \u201cwhy do you want there to be something wrong with you\u201d, that it\u2019s just life and bodies hurt and everyone is incapable of making friends. \ud83e\udd26\ud83c\udffb\u200d\u2642\ufe0f  hell, I was diagnosed with depression anxiety and panic disorder as a teen and my parents acted like I wanted to be mentally ill just cause I told them I was relieved that I had a name for my emotional pain. \n\nI had periods so bad starting at 11 years old that I would vomit and pass out from the pain regularly. I was never taken to the doctor once and when I was my parents talked over me and said \u201cit\u2019s not that bad he doesn\u2019t show any of this around us\u201d (yeah I wonder why \ud83d\ude44)\n\nI\u2019m now diagnosed with Depression, generalised anxiety disorder, panic disorder, adhd (combined), autism, chronic joint, muscle and bone pain, hypermobility, POTs, chronic migraine, occipital neuralgia, OCD\nAnd I\u2019m not officially diagnosed but I likely have ME/CFS and Fibromyalgia. \n\nIf I had gotten help for these things instead of being met with defensiveness, distrust, and disgust I would likely be much healthier now and not so disabled I can\u2019t work at 22 years old \n\nParents really should be forced to sign something that states they understand all the risks of having a child, highlighting chronic mental and physical health issues"
      },
      {
        "id": "ncevajx",
        "score": 44,
        "body": "Yes. And it's super isolating, because no one you know has ever talked to you about this stuff, so you don't even have a chance to know other folks with disabled kids and befriend them. You have to bumble your way through alone because life left you completely blindsided."
      },
      {
        "id": "ncey1nr",
        "score": 41,
        "body": "I am the mother of five autistic children. The oldest was born before the MMR vaccine was invented, and I carried him after I had the R portion of that vaccine. I never felt. I got the short end of the stick. But that he did.I have always wished for him, not for me, that that never happened. His life would have been so much easier and so much more. The one thing that really stands out for him is he is just shy of a genius."
      },
      {
        "id": "ncgou6a",
        "score": 37,
        "body": "Totally! It really makes you wonder why they\u2019re so invested in \u201cnot scaring us off\u201d"
      },
      {
        "id": "nchngyo",
        "score": 35,
        "body": "It\u2019s like that one saying \u201cEvery child deserves parents, but not every parent deserves a child.\u201d"
      },
      {
        "id": "ncf1mzs",
        "score": 32,
        "body": "As an autistic person my self thank you for the way you talk about your kids. You talk about him so kindly, I don't see that a lot unfortunately. I hope all of you guys are happy"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1lwu8m3",
    "title": "Thoughts on this bumper sticker?",
    "body": "Not gonna lie I love it so much. As a physically disabled person I think it's funny and it makes me happy :) \nMy boyfriend sent me this picture, I think he said it had a veteran sticker as well!! \n\nTLDR: I love this bumper sticker that my partner sent me a picture of, what do you think? ",
    "flair": "Image",
    "score": 785,
    "comment_count": 208,
    "created_at": "2025-07-11T01:32:44+00:00",
    "top_comments": [
      {
        "id": "n2h5uod",
        "score": 505,
        "body": "I'm sending to a relative. They and their spouse both used wheelchairs (spouse has passed) and they had a pretty intense sex life and some kids as a result.\n\n\nWhen my relative broke their leg (disuse osteoporosis) they informed the whole family it happened during sex.\u00a0\n\n\nI feel it will speak to them.\u00a0"
      },
      {
        "id": "n2h8vor",
        "score": 212,
        "body": "Lmao. Not the kind of thing I'd display, but it made me chuckle. \ud83e\udd18"
      },
      {
        "id": "n2hn6fd",
        "score": 201,
        "body": "Insurance company be like, \"How exactly did your chair get damaged? \ud83e\uddd0"
      },
      {
        "id": "n2h4nlt",
        "score": 164,
        "body": "[removed]"
      },
      {
        "id": "n2h9l05",
        "score": 130,
        "body": "I love this so much"
      },
      {
        "id": "n2hbt2t",
        "score": 118,
        "body": "I don't drive and I'm not a dater, and more importantly, I live in a senior facility. If I were to slap one on the spoke guard of my wheelchair, somebody, either a resident or a nurse, would call me out on it and might have me remove it. \n\nHaving said all that, I am pro-disabled sex, and like seeing these stickers (I've seen a few). I just hate explaining myself."
      },
      {
        "id": "n2h9iq0",
        "score": 108,
        "body": "I mean, I don\u2019t find it offensive. I think it\u2019s in the same category as \u201cCalvin pissing on stuff\u201d in terms of class, but whatever stuffs your Twinkie."
      },
      {
        "id": "n2h1z3b",
        "score": 83,
        "body": "I think some people will find it tacky or crude. I am with you, I kinda like it. I am also a disabled and a vet, though not in a wheelchair. I like their style."
      },
      {
        "id": "n2hnmc0",
        "score": 68,
        "body": "It took me a second, but that's the [lady off the semi truck mud-flaps.](https://i.pinimg.com/736x/c9/62/d5/c962d565f36f7f74d30d1da055ba1cc8--mud-career.jpg)  10/10 fucking hilarious."
      },
      {
        "id": "n2hg5u9",
        "score": 65,
        "body": "And you, too. These conversations are important. We're too easily desexualized."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1oh2zwu",
    "title": "Spotted creative handicap parking signs depicting different parasports outside a sporting goods store",
    "body": "",
    "flair": null,
    "score": 778,
    "comment_count": 55,
    "created_at": "2025-10-27T02:26:22+00:00",
    "top_comments": [
      {
        "id": "nllsw4n",
        "score": 129,
        "body": "This brought me more joy than I thought it would."
      },
      {
        "id": "nlm9bf2",
        "score": 103,
        "body": "That is so many disabled parking spots!! I'm used to seeing one, maybe two max"
      },
      {
        "id": "nlmqvdr",
        "score": 68,
        "body": "Okay outside a sports goods store that\u2019s kinda genius"
      },
      {
        "id": "nlmymye",
        "score": 50,
        "body": "At least in my area, these wouldn't actually be disabled parking because there's no sign. None of them seem to have adjacent areas to unload either. So I think these are just decoration. Still neat!"
      },
      {
        "id": "nlm0z34",
        "score": 40,
        "body": "Right?? I absolutely love this level of inclusion!"
      },
      {
        "id": "nlorr0w",
        "score": 33,
        "body": "They aren\u2019t handicapped spots, though.  They are regular spots, painted with the logo, but without a handicap sign or hash marks."
      },
      {
        "id": "nlowbgy",
        "score": 30,
        "body": "That's confusing and disappointing"
      },
      {
        "id": "nloxlvv",
        "score": 29,
        "body": "I agree.  If I wasn\u2019t familiar with handicap signs, I would not know if I was allowed to park there or not if I didn\u2019t have a placard-but without the hash marks and the sign, they aren\u2019t even legal spots, and they aren\u2019t helpful for many folks that need the extra space.  I\u2019m not sure what this is for?"
      },
      {
        "id": "nlmspjm",
        "score": 25,
        "body": "Very cool, I do wonder though if some people wouldn't understand some of these"
      },
      {
        "id": "nlp9mg1",
        "score": 25,
        "body": "not to hijack but i use the word for the parking spots and placards because thats often what its called on paper but i never saw it as a slur, just outdated for day to day purposes. i\u2019d rather they changed it to accessibility parking spots or whatever but its not that serious either considering what we are going through daily at least in comparison"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1qwyqtw",
    "title": "I\u2019m a double hand amputee (train accident survivor). I\u2019m tired of the \"overcoming\" narrative\u2014let\u2019s talk about the reality of living in an inaccessible world.",
    "body": "Hi,\n\nI lost both hands in a train accident, and after the initial recovery, I realized something: I\u2019m not \"struggling\" with my body as much as I\u2019m struggling with a world that doesn't account for my existence.\n\nI\u2019ve adapted my routine and I\u2019m comfortable with my \"new normal,\" but I find myself constantly hitting walls\u2014whether it's literal infrastructure, technology, or the exhausting assumptions/pity from non-disabled people. I just want to exist and navigate my day without being a walking lesson for others.\n\nAlso, if you're non-disabled and lurking, feel free to ask the \"logistical\" questions you\u2019ve been afraid to ask. I\u2019d rather explain how I use my PC than deal with more awkward staring.\n\nAsk me anything.\n\n( I don't speak English. I did the translation with the help of google translate. There may be mistakes. )\n\n",
    "flair": null,
    "score": 775,
    "comment_count": 48,
    "created_at": "2026-02-05T21:47:22+00:00",
    "top_comments": [
      {
        "id": "o3so1m8",
        "score": 143,
        "body": "We are only as disabled as the world is inaccessible!\n\nYour English is easy to understand in this post. \n\nYou mentioned being used as a lesson for other people\u2014is this something strangers do? \n\nThank you for posting, hello :)"
      },
      {
        "id": "o3t3axk",
        "score": 64,
        "body": "No problem. I'll be happy to answer you.Yes, it's true. I use my toes, only for minor things: typing on the keyboard, turning on/off a faucet to drink water, opening/closing a door.Otherwise, my wife helps me with everything I need.And I'm turning 60 this year. I'm not young anymore. I get tired much faster now."
      },
      {
        "id": "o3syhai",
        "score": 55,
        "body": "Us wheelchair riders have it rough because most places aren\u2019t accessible to us but I can't even imagine how difficult it is to have to endure that inaccessible problem with practically most everyday items since they're designed to be used with hands/fingers.              \n\nI've met a few double-arm amputees and they usually had extremely dextrous feet and legs. Is that the case with you too?                 \n\nIf so, do you always have to wear light footwear like slippers so you can use your toes to grasp something when you need to?               \n\nI apologize if my questions seem insensitive, I don't want to be too nosey or anything so it\u2019s completely fine if you don\u2019t feel comfortable answering them.               \n\nIt would be nice to spread awareness about people like you so I'm glad you made this post."
      },
      {
        "id": "o3t09b1",
        "score": 51,
        "body": "The first thing he has to do is accept his disability, because his life has changed 100%.Then they have to adapt to their new life.They need to go to a party, take a walk in the park, go to a movie.The idea is not to isolate themselves, not to run away from people.And life will be much easier.That's what I did, and believe me, I'm okay."
      },
      {
        "id": "o3spng5",
        "score": 30,
        "body": "Hello. Yes, my thoughts are a little scattered."
      },
      {
        "id": "o3v147v",
        "score": 30,
        "body": "This is what I learned in years. The hardest thing was my psyche. I went into severe depression. 10 years lasted until I was cured of depression. But now it's ok. "
      },
      {
        "id": "o3u3xtg",
        "score": 29,
        "body": "It's exhausting being our own advocates, but if we don't speak up, how will there be change? "
      },
      {
        "id": "o3swh3p",
        "score": 23,
        "body": "Hi, i\u2019m disabled but not physically disabled\u2014 I\u2019m writing a character with similar circumstances to yours (double arm amputee). Prior to losing her arms, she enjoyed cooking and chemistry, and had to adapt in how she did those activities. How have you adapted to your work/hobbies/pastimes, or have they had to change?"
      },
      {
        "id": "o3tb59j",
        "score": 19,
        "body": "Hi, I'm not disabled so please forgive any insensitivity. What helped you the most when it came to the mental/emotional aspects of adjusting to a new normal? Thanks, wishing you well"
      },
      {
        "id": "o3uxwqb",
        "score": 19,
        "body": "I don't know if you will believe me, but faith in God helped me a lot. I am an Orthodox Christian, and I often went to church, I said prayers, and over time I accepted and understood that now this is my life. And I have to adapt to what I am now, that is, without hands. "
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1n7xnew",
    "title": "This made me laugh.  I hope you to do.",
    "body": "",
    "flair": null,
    "score": 772,
    "comment_count": 15,
    "created_at": "2025-09-04T01:56:30+00:00",
    "top_comments": [
      {
        "id": "ncaxuv6",
        "score": 80,
        "body": "That made me laugh. They could also eat soup with a fork and never take an elevator."
      },
      {
        "id": "ncb9z6k",
        "score": 56,
        "body": "Shoes, glasses, grocery carts\u2026"
      },
      {
        "id": "ncc05ol",
        "score": 48,
        "body": "people will mind as well stop carrying water bottles and using backpacks. stop being lazy. \n\nwashing machines and dryers, stop using them and wash by hand and hang dry. \n\nflying, just drive.\n\nbuying food that is pre made or cake mix and dried pasta, just make it from scratch. \n\nusing direct deposit, just put it in the bank yourself than having your work do it for you."
      },
      {
        "id": "ncdc7bc",
        "score": 31,
        "body": ">flying, just drive.\n\nDont be absurd. They should walk.\n\nLike how they want us to walk if \"technically we can\" without caring if \"i will spend two days in severe pain afterwards \". \n\nThey can walk 20h to meet their friends next weekend. Who cares if it wastes their time and makes them ill?"
      },
      {
        "id": "ncdcj9o",
        "score": 20,
        "body": "Absolutely. It is absurd how much we normalize pain. And wasting time.\n\nLike i recently oiled a table we have. It needed to be done, so i just acepted that i would be in pain for the next 2-4 days. Or i go visit my grandma (help her move around, take her to the toilet, bring her drinks...) knowing that at minimum it takes me 3 days and a lot if pain."
      },
      {
        "id": "ncdluax",
        "score": 9,
        "body": "Mop the old-school way, abled folks: a rag or sponge, down on the floor with a bucket.\u00a0"
      },
      {
        "id": "ncbyxkb",
        "score": 7,
        "body": "ok I lol'ed"
      },
      {
        "id": "ncbj1x7",
        "score": 4,
        "body": "Hahahahahahahahaha!"
      },
      {
        "id": "nes1ohk",
        "score": 2,
        "body": "Haha. I get asked about my cane/staff all the time. I also constantly get asked if I was in the military, like only they can get disabled."
      },
      {
        "id": "ncj5oj9",
        "score": 1,
        "body": "This is brilliant & gave me a good chuckle."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1qxll6b",
    "title": "My biggest pet peeve of this subreddit is the stuble disrespect of autstic people",
    "body": "It's 2026 why tf are we still asking autistic people \"oh so why can't you work\". THE AUTISM. Autism is a disability I don't care if level 1 autism isn't disabling to you. It's disabling to many, I don't care if you know someone with level one autism who can do this and that. Every single time an autistic person comes around it's the same crap. \n\nPeople will be like \"I have autism and mild joint issues\" and everyone will be like \"joint issues isn't enough to not work\". What. About.The.Autism. \n\nLevel 1 autism is a disability that leaves many homeless and suffering. A lot of us die just like other disabled folks. I'm fucking tired of people acting like all of us are just mild. \n\nIt's mild compared to level 3, it's still a disability. Autism makes everything harder for me. I'm fucking tired of people acting like it does nothing. I don't care if you could work with autism. I also work with autism but it's genuinely destroying my mental health due to burnout and constant meltdowns. \n\nWhenever I mention that to others it's always \"oh but I can do it\". I don't want special treatment, I want people to understand  that my struggle is a fucking struggle. I'm lucky to be able to work the little amount I do, most autistic people. Yes level 1 cannot work at all. \n\nI keep trying but it's so hard when everyone is stuck in the 2000s around autism, even disability groups.  Let me repeat, I don't care if you're not disabled by autism, I'm not saying you have to be. I'm saying leave space for those who are. \n\nI'm scared, I'm scared I'll fucking be homeless one day due to this. It's not a personality trait for me it's suffering. ",
    "flair": null,
    "score": 763,
    "comment_count": 205,
    "created_at": "2026-02-06T16:02:43+00:00",
    "top_comments": [
      {
        "id": "o3xkjeg",
        "score": 385,
        "body": "Agreed. I've known autistic people who can work just fine and others who can barely function at all. Huge variation in their presentation of symptoms and abilities. It's almost like it's a spectrum or something...."
      },
      {
        "id": "o3xmjy3",
        "score": 171,
        "body": "I am able to work with autism but I couldn't do 99% of jobs. I recognize that I lucked into a career and work situation that accommodates me, and I still struggle. And I'm very high functioning when it comes to work/achievement, and I still deal with these issues because of workplace culture. "
      },
      {
        "id": "o3xx3dt",
        "score": 151,
        "body": "It's sometimes made worse when a well meaning autistic person or ally does a presentation and says something like \"Autism is a superpower!\" but misses out the \"If you've met one person with autism, you've met one person with autism\" and people go away thinking it's not a disability but an advantage in all situations."
      },
      {
        "id": "o3xxh1l",
        "score": 98,
        "body": "I have what most would consider mild autism. I am able to speak well and communicate pretty effectively and my masking skills are insane. However, in order for me to work, I have to have people drive me, stay with me at my job, and after a day of work I'm extremely burnt out and frustrated. After a week I'm completely run down and I have no spoons left for cleaning the house or even taking care of myself. This is also due to other disabilities I have, but my autism still plays a huge part in that. It's crazy to me anyone is surviving alone and working 8 hours a day forever. I need massive amounts of support just to do it myself."
      },
      {
        "id": "o3xm5ix",
        "score": 83,
        "body": "This is my biggest gripe when people don\u2019t understand that neurodivergence is.a.disability!! Especially when it comes to adhd and autism\u2026 god it annoys me so damn much. A lot of ableism too.. There are many people who can\u2019t work due to adhd and/or autism. I know for me I either can\u2019t work or struggle to work due to autism and adhd for the longest. Now combined with other comorbidities it\u2019s just even harder now."
      },
      {
        "id": "o3xna5f",
        "score": 65,
        "body": "That's ok, nothing wrong with that. I'm happy you found a job that works for you. Just please take care of yourself and don't push yourself towards burnout, if possible."
      },
      {
        "id": "o3y0l36",
        "score": 55,
        "body": "This is what I needed to see today. I'm AuDHD and I literally just got off the phone with my parents trying to explain to them that yes I was able to work for a decade but now I'm no longer able to work. My body and mind just won't. I suffered during that decade and there was no reason for me to do that then and there's no reason for me to go back into the working world to do that to myself again now."
      },
      {
        "id": "o3ynw28",
        "score": 54,
        "body": "People who aren\u2019t autistic, regardless if they\u2019re in proximity to autism, cannot fathom the autistic experience. It\u2019s truly wild. No matter the \u201clevel\u201d, it is disabling period. Full stop. I wish there was a simulator but I don\u2019t think that would ever be possible given the complexity and diversity of autistic traits and such. Not to mention, being multiply disabled simply makes life much harder. Autism plus other neurodivergent and even physical disabilities is exhausting and infuriating to say the least."
      },
      {
        "id": "o42fo7p",
        "score": 45,
        "body": "I hate the superpower shit so much because I always hear it from people who don't have symptoms as deliberating and who just assume everyone else is the same as they are, and it feels like they don't want their condition to be associated with mentally ill and disabled people. As someone who has AuDHD paired with chronic illness it makes living with my other disabilities so much harder and hearing people say this shit always pisses me off."
      },
      {
        "id": "o3xr8nk",
        "score": 41,
        "body": "Preach. No levels in my country but I\u2019ve never been able to work and I cannot function in every day life without caregivers ensuring my survival and they represent me in all legal matters. \n\nThe idea that autism isn\u2019t a disability is so harmful and it sucks when other autistic people, who are supposedly your community, work overtime to distance themselves from those of us who are deemed harmful stereotypes or whatever. All while they\u2019re able to live their lives doing things I could only ever dream of."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1o7iwex",
    "title": "You are granted permission to look into any mobility aid you need to make living with your medical issue easier. You can discuss it with your doctor, too. It's okay, I promise.",
    "body": "Alt text: A picture of a cat being very close and having its face down at the camera, above it greentext that reads:\n- \"I'm not disabled, can I use mobility aids?\" post \n- look inside \n- posted by a disabled person",
    "flair": "Image",
    "score": 763,
    "comment_count": 58,
    "created_at": "2025-10-15T18:23:53+00:00",
    "top_comments": [
      {
        "id": "njo5rvd",
        "score": 84,
        "body": "Yep, 100%.\n\nInstead of asking us if you can use it, try asking us how best to advocate for yourself with your doctor. doctors kind of suck, but we have a lot of experience collectively and can help you!!\n\nobligatory copy paste:\n\n----\n\nhere's the copy paste we have for one of our most frequently asked questions:\n\nas a long-time mobility aid user, you really need to see a professional before using anything. PLEASE seek a doctor over this ASAP and disregard the people who will comment telling you to just use one because you feel like it. they're trying to help but it isn't going to be helpful for you in the long run.\n\nThe way to determine what kind of mobility aid you need, if it's going to help you, is by going to a physical therapist. We on the internet do not know enough about your condition to prescribe a mobility aid to you. All mobility aids work by redistributing force and weight onto other parts of the body, and they all incur some type of damage. The point is that the ability to live your life should be worth the amount of damage a properly sized, properly used, and properly selected mobility aid can cause. But we can't do that selection and neither can you, you need somebody with a knowledge of human anatomy who has gone to school for this.\n\nPeople who have not used mobility aids for significant periods of their life will comment here to try to affirm you and tell you that you know your body best. And yes, you should self-advocate! But please listen to those of us who use mobility aids; they are contraindicated for some disorders and can make some WORSE.\n\nI've been saying this for months but we desperately, desperately need an FAQ explaining to people that we cannot safely recommend this for them. we need a moratorium on \"am I allowed to use a cane? can I use a cane? what type of cane should I get?\" posts and to redirect then all to an FAQ. we just get too many.\n\nit's to the point that every time i open this subreddit i get the copy/paste ready lol.\n\nand since i need to add this to the copy/paste: i've been handling these posts for a year, up to 5x a day, and can count on one hand the number of posters who lack medical access. i lack medical access; i am aware it can happen but that's not what's happening on this sub."
      },
      {
        "id": "njq242s",
        "score": 56,
        "body": "\u201cI\u2019m not disabled but I experience pain on the daily that limits my ability to work or even do daily tasks. Sometimes I push myself but then I faint and cracked my head on the pavement, requiring stitches. I also regularly experience fatigue so extreme I can\u2019t get out of bed. Am I allowed to maybe possibly start using a cane? Obviously I will just suffer for ever if this is offensive to real disabled people. I apologize for even posting, let me know if I am out of line\u201d"
      },
      {
        "id": "njof7gr",
        "score": 44,
        "body": "I kinda love and kinda hate the implication that if a bunch of people on Reddit say you can\u2019t do something that would make your life so much easier because it can come off as disrespectful that people would just listen to them. \n\nLike, I can imagine someone crying to a doctor saying something like \u2018I know I can hardly walk and a wheelchair would help me but Redditors said I can\u2019t!\u2019"
      },
      {
        "id": "njr3oh9",
        "score": 37,
        "body": "Society really trains us to think we\u2019re being babies if we factually our acknowledge our disability, especially if it\u2019s a non-visible disability."
      },
      {
        "id": "njog4ek",
        "score": 35,
        "body": "\"I'm sorry doctor, reddit user DMmejuicybreasts said I am not allowed a walker \ud83e\udd40\""
      },
      {
        "id": "njp5o86",
        "score": 29,
        "body": "Fun fact! You can be disabled even if you don't meet the government definitions of disability. You can be disabled even if you work full time. You can be disabled even if you don't have your issues diagnosed yet. You can be disabled even if you have some days that are symptom free.\n\n\nDo you have a health condition that impacts your day to day living? (Even if it's not every day). If so you are definitely welcome to consider yourself disabled. Some people prefer not to, and that's ok too!"
      },
      {
        "id": "njo6k8a",
        "score": 29,
        "body": "I'm laughing to myself because this feels like my emotional support copy paste that I need to get a letter from my therapist to have in my apartment with me at all times."
      },
      {
        "id": "njoeh22",
        "score": 23,
        "body": "Yeah I've seen so many of these posts, it would be easiest if there was a thread to direct them all to rather than just copy pasting the same comment every time you spot it. Or an automod comment one can summon. I've told so many people outside of Reddit too that it's totally fine to use a mobility aid if you obviously need it, it's just important to talk to a professional about it first so you get the right one and don't hurt yourself with it. But that's really all there is to it, there is no ceritificate of disability or something you have to show when you want one lol."
      },
      {
        "id": "njo3gs0",
        "score": 21,
        "body": "We should pin this to the top.\n\nEdited to add: learning how to use it properly from a doctor or pt is also important. \ud83e\udde1\ud83d\udda4\ud83e\udde1\ud83d\udda4\ud83e\udde1"
      },
      {
        "id": "njowi8g",
        "score": 18,
        "body": "Thankyou for the alt text much appreciated"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1j8tcaj",
    "title": "First time being able to walk in months without the help of a cane!",
    "body": "I (f19) am so happy omg, these functional knee braces were so expensive but so worth it, I'm still getting used to them (and a little insecure about that) but I'm so happy, for short/medium walks I have the freedom back to use 2 hands instead of having to use a cane while I walk, trying not to overdo it out of excitedness and hurt myself lmao\nJust wanted to share some happiness and positivity :)",
    "flair": "Image",
    "score": 754,
    "comment_count": 40,
    "created_at": "2025-03-11T15:25:16+00:00",
    "top_comments": [
      {
        "id": "mh7vedc",
        "score": 19,
        "body": "Woohoo! That\u2019s great :)"
      },
      {
        "id": "mh7xapc",
        "score": 16,
        "body": "Hey, congratulations! That is a good achievement. You should be very proud."
      },
      {
        "id": "mh8t7dh",
        "score": 14,
        "body": "I brought them independently with approval from my physiotherapist and GP, (they couldn't directly prescribe because my cane meant I didn't qualify, as I already had support walking from that, the NHS is odd lol) \n\n\nThey are some of the cheaper ones on the market (\u00a3150 each) but work well and are quite comfy surprisingly!"
      },
      {
        "id": "mh81kmm",
        "score": 10,
        "body": "Can you please give me link of functional knee brace"
      },
      {
        "id": "mh7xghu",
        "score": 9,
        "body": "Congrats! I'm happy that you're enjoying it."
      },
      {
        "id": "mh7yyrm",
        "score": 8,
        "body": "DUDE!!! That\u2019s so sick!!!"
      },
      {
        "id": "mh81s7r",
        "score": 8,
        "body": "thats awesome!!!! im so happy for you <3"
      },
      {
        "id": "mh8n67a",
        "score": 7,
        "body": "I\u2019m going to have to write you at ticket you are going too fast my friend \ud83d\ude39"
      },
      {
        "id": "mh8ojpr",
        "score": 6,
        "body": "Congrats!! \n\nDid you get those through your doctor or on your own? I def need to look into getting these as well. Thank you for sharing! Keep up the good work\u2026 one step at a time!! Get it!!!"
      },
      {
        "id": "mh8rgnq",
        "score": 6,
        "body": "Cute skirt \ud83c\udf44"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1pjhn8g",
    "title": "Anyone else notice that groups for loved ones of disabled people are kinda ableist?",
    "body": "I'm not only talking about reddit, I've been on different sites over the years and always noticed that after scrolling for a few minutes that you'll eventually get a \"never date a [person with this certain disability]\". Some have been normal and just people venting but like 89% of the time is falls into this. \n\nI've first seen this in loved ones/exes or unfortunately victims from people with mental disorders and because i still got internalized ableism i just shrugged it off and thought \"well after a months they won't be ableist anymore\" and many mental disorders do cause people to unfortunately be toxic. But than i also saw this in physical disabilities and that is when i just became kinda annoyed. Like damn, not every blind guy will cheat on you with 22 chicks, Janice. It kinda suuuuucks that I've seen soooo many people generalizing disabilities just because they got 1 or 2 bad experiences. I get not wanting to get close/interact with certain people because of trauma but calling them \"all the same\" is disgusting and dehumanizing.\n\n\nWorst of all? When it's family members. The most awful one i remember was a post about a dad talking about how his daughter was diagnosed with bipolar and a few comments said something like \"give up on her\" \"disown her\" \"she will be terrible to have around, put her into a insane asylum\" and so on and so on. It's so disturbing to see. \n\nDoes anyone also notice this or do i always run into the bad apples?",
    "flair": "Discussion",
    "score": 753,
    "comment_count": 196,
    "created_at": "2025-12-10T23:10:14+00:00",
    "top_comments": [
      {
        "id": "ntdib8f",
        "score": 319,
        "body": "Oh yeah, 99.99% of them are circle jerks for people who resent their disabled loved ones"
      },
      {
        "id": "ntdxxhk",
        "score": 171,
        "body": "Lol. \"Not every blind guy will cheat on you with 22 chicks, Janice\" really made my day. \n\nThis is yet another reason why I despise the \"my disabled family member / roommate / neighbour / whatever\" defensive response whenever I try to bring up issues of ableism. \n\nPeople do it like it's supposed to prove they aren't ableist when the fact they're doing it at all proves the opposite."
      },
      {
        "id": "ntdna8b",
        "score": 161,
        "body": "\"I'm so virtuous for putting up with this horrible waste of space that is my disabled family member. Won't anyone think about how hard this all is for me?\" worlds tiniest violins as far as the eye can see..."
      },
      {
        "id": "nterzw5",
        "score": 112,
        "body": "The autism mom groups are *whewww*. I'm an autistic parent of an autistic kid but I have way more in common with my kid than those warrior moms who fight autism daily."
      },
      {
        "id": "ntdkdl8",
        "score": 104,
        "body": "100% Ableism exists in those groups. Yes they deserve support too but a lot of what is shared is about the burden of someone else's disability and people wonder why disabled people feel like a burden and unlovable. Of course disabled people in general aren't angels lol but there's a strong resentment towards us."
      },
      {
        "id": "nte2z30",
        "score": 75,
        "body": "It\u2019s the autism moms for me. Some are wonderful but the ones that blog about it and broadcast their (oftentimes distressed) children without their understanding or consent while lamenting about what a burden and a curse it is (and pushing herbal \u201ccures\u201d) are just *awful*."
      },
      {
        "id": "ntdjjxu",
        "score": 68,
        "body": "Yikes. Thanks for confirming my suspicion.\u00a0"
      },
      {
        "id": "ntevoy0",
        "score": 66,
        "body": "Same and I'm joining the war on autism, on the side of autism."
      },
      {
        "id": "ntdysrj",
        "score": 64,
        "body": "Thank you, i try to be funny.\u00a0\n\n\nAnd yeaaaah it's the \"i have a black friend\" all over again.\u00a0"
      },
      {
        "id": "ntdrcya",
        "score": 48,
        "body": "Nah, not kinda, extremely. Lol"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1nywe47",
    "title": "People are clueless.",
    "body": "Came across this video on my TikTok\u2019s fyp today. Immediately I understand her concern. The door opens in which makes it impossible to close. I\u2019ve had this happen so many times and I legit had to leave the door open and shout to anybody I heard to not to come back there. I\u2019ve soiled my pants so many times trying to find a bathroom to fit me.\n\nI go to the comments\u2026 they\u2019re all focused on the tray? EVEN IF THE TRAY WASNT THERE IT DEFINITELY WOULDN\u2019T FIT A FUCKING WHEELCHAIR.\n\nOH MY GOD.\n\nI\u2019m genuinely so pissed at this. There is NO reason she shouldn\u2019t fit in there. If she doesn\u2019t fit, I definitely wouldn\u2019t! I\u2019m in a wheelchair! \n\nI can tell you right now if I didn\u2019t have a caregiver that helped me in bathrooms I\u2019d never be able to use one. EVER. I\u2019ve literally broken a flimsy ass stall divider because I had to shove myself in and STILL COULDN\u2019T SHUT THE DOOR. \n\nI almost at one point broke my foot because I was so far up against the wall. \n\nPersonally, I think anybody in wheelchairs and any mobility device should be able to do a full 360 without hitting ANYTHING in bathrooms. Otherwise why make a fucking handicap stall. ",
    "flair": "Rant",
    "score": 744,
    "comment_count": 111,
    "created_at": "2025-10-05T18:44:15+00:00",
    "top_comments": [
      {
        "id": "nhxxc4f",
        "score": 376,
        "body": "This would not be considered accessible, if it were here in Canada. You need at least a 1500 mm turning circle (and that's the smallest possible size: many places require 1700 mm nowadays) and based on the photo, that certainly isn't it.\n\nI work in accessibility consulting and that photo also shows a VERY common mistake that architects make: a door that swings inwards, overlapping with the aforementioned turning circle. That is not allowed. In fact, I saw that on a floor plan as recently as Friday (and today is Sunday). For whatever reason, people think that is acceptable.\n\nPeople who say the wheelchair tray is a problem have never seen a wheelchair before, because it typically goes above the user's legs, which are also part of the wheelchairs' footprint and wouldn't change the amount of floor space needed to maneuver. Taking it off wouldn't make a lick of difference.\n\nFrom my professional/job lens, this stall would not be even close to compliant, if it were here in Canada."
      },
      {
        "id": "nhxt78n",
        "score": 175,
        "body": "The comments are fucking making me livid. I need to stop looking but oh my god the amount of comments going \u201cI\u2019m a ProfESsiOnAl\u201d \u201cI\u2019vE wOrkEd WiTh DiSaBlEd Kids\u201d \u201ciTs AdA cOmPliAnt\u201d OH MY GOD IM GONNA RIP MY HAIR OUT."
      },
      {
        "id": "nhxzm8b",
        "score": 166,
        "body": "THANK YOU! It\u2019s terrible how many comments about \u201cprofessionals\u201d were saying it was the tray\u2019s fault. Honestly, might see myself moving to Canada LOL.\n\nI agree with that standard, there HAS to be turning space and the door opening inward? Horrid design flaw."
      },
      {
        "id": "nhy2nsb",
        "score": 112,
        "body": "OMG i love when people pull the \u201cI work with disabled kids\u201d card. It tells me you literally know nothing of the lived experience of disabled people \ud83d\ude2d\ud83d\ude2d"
      },
      {
        "id": "nhyorek",
        "score": 95,
        "body": "What's worse is they're targeting their nasty comments at a video *of a child.* If this kid needs their tray on their chair in order to access the world, they should not have to remove it from their chair (and put it... where?) in order to use the bathroom. This is enraging."
      },
      {
        "id": "nhy1t1j",
        "score": 64,
        "body": "Any \"professional\" claiming that this is compliant and accessible is lying or don't know what accessibility is, in my opinion.\n\nI'm including the architects I mentioned in my other comment, who THINK they know their stuff but often don't. There is a lot of that. My business often gets subcontracted work from architects and engineers, who are great at fire codes, structural codes, etc. but tend to struggle with accessibility codes. So yes, there might be \"professionals\" but they might not even realize that they're getting accessibility wrong.\n\nRe: your question... Yes, there has to be a turning circle. The door CAN open inwards but it must NOT overlap with the turning circle. The only exception for \"overlap\" would be for a sink in a universal washroom, where SOME overlap is allowed if the sink has clear space underneath (which is required anyhow). But typically, I don't recommend that the turning circle overlaps anything at all, if possible.\n\nRegarding standards in Canada, we used to be aligned or slightly short of ADA, but we've also been rapidly updating the standards. I think today, there is an argument that the new standards surpass ADA entirely.\n\nFor example, I found out that our new standards for lowered service counters are better than ADA. And we're pushing for a 1700 mm to 2100 mm turning circle for public toilets, which also exceeds ADA.\n\nAnd I recall that our accessible toilet stalls require a \"D-handle\" (which is a small cabinet-style handle on the near/hinge side of the toilet stall), which allows for the stall door to be closed without having to reverse at the same time.\n\nI'm actually doing a webinar on Canadian building codes vs. accessibility standards next month, and we might touch a bit on ADA. So your post is very timely."
      },
      {
        "id": "nhy27vg",
        "score": 53,
        "body": "I feel so bad because the Louisiana purchase comment was so specific I laughed \ud83d\ude2d but damn these people can\u2019t even think about the fact that a regular wheelchair can\u2019t even turn in that stall?? Ughhhh this is why accessibility in the US is abysmal"
      },
      {
        "id": "nhzcn4h",
        "score": 44,
        "body": "I am also thinking of the kids who are non-verbal, who may need to rely on a communication device mounted on the chair or tray. Or kids whose trays have a communication board taped on them.\n\nFor them, it isn't just a tray. It is literally how their way to connect with the world."
      },
      {
        "id": "nhycuxx",
        "score": 43,
        "body": "Speaking as an actual accessibility professional with a disability, I'd argue that even having a disability doesn't automatically make someone an expert. I know a ton of folks who would see accessibility through their own experiences and not consider others' challenges.\n\nThe accessibility training course I took (required for my professional designation) taught us to look at it from as many disability perspectives as possible, as it should be.\n\n\"I work with disabled kids\" MIGHT make you an expert on working with disabled kids. That's it. It doesn't give someone an expert lens into what other disabled people go through. And I think that's what many people don't get."
      },
      {
        "id": "nhxtvn4",
        "score": 40,
        "body": "Unfortunately, it is ADA compliant, because they only require a standard chair to fit. I feel the pain, though. My mobility scooter doesn\u2019t fit in a lot of accessible stalls, either. \n\nThe people saying to take off the tray are dumb. Most of those are part of the system of securing the user."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1putpc2",
    "title": "Able-Bodied People: This Isn\u2019t Your Trauma Dump",
    "body": "What\u2019s up with able-bodied people commenting here? I mean, this sub is for disabled people. Yet all I see are able-bodied family members talking about how hard it is for them and how the disabled person \"ruined their life\". This space is for disabled people, not for family members who see themselves as eternal victims.",
    "flair": "Rant",
    "score": 737,
    "comment_count": 192,
    "created_at": "2025-12-24T18:16:52+00:00",
    "top_comments": [
      {
        "id": "nvr6100",
        "score": 441,
        "body": "I honestly don't understand why they don't post in r/caregiversupport"
      },
      {
        "id": "nvrp54w",
        "score": 220,
        "body": "They probably don\u2019t consider themselves \u2019care givers\u2019 if they just think the disabled person is a burden"
      },
      {
        "id": "nvs6tcn",
        "score": 208,
        "body": "Weirdly enough, we get this same thing over on the asexuality subreddits, too. Half of the posts there are people complaining/venting/trauma dumping about their asexual partner. And I\u2019ve definitely seen similar bullshit in this subreddit, too. And a couple of other subreddits that are meant for marginalized communities as well. \n\nLike the amount of entitlement it takes for them to go into a space that is specifically for a marginalized group & then make it about them and complain about us is *mind-boggling*. I\u2019ll never understand it. I have no problem with these folks hanging out in the community & commenting when appropriate. But to make posts venting in *our* subreddits? It just isn\u2019t okay"
      },
      {
        "id": "nvr5xdx",
        "score": 117,
        "body": "I think we are seeing different things or having a different interpretation of the posts here. It seems to be mostly disabled people or the loved ones of disabled people asking how they can better assist us. Only had one major issue"
      },
      {
        "id": "nvsrvqe",
        "score": 113,
        "body": "I\u2019m on a subreddit for adult children estranged from their parents & saw an estranged parent post today just to complain & guilt-trip. Thankfully mods removed it but yeah it happens on them all."
      },
      {
        "id": "nvrocde",
        "score": 112,
        "body": "Maybe they don\u2019t know it exists?"
      },
      {
        "id": "nvreh2z",
        "score": 104,
        "body": "ablebodied people can comment here. there are plenty of disabled people here who are intellectually or psychiatrically disabled ONLY.\n\nhowever, i know you mean abled people. i think they SHOULD comment here to a point, so we can teach them and give them feedback."
      },
      {
        "id": "nvs5zav",
        "score": 81,
        "body": ">ablebodied people can comment here. there are plenty of disabled people here who are intellectually or psychiatrically disabled ONLY.\n\nLots of people here are going to ignore this. Even amongst the disabled, \"invisible\" disabilities are challenged and demeaned. There's always an undercurrent of competition."
      },
      {
        "id": "nvrn2nt",
        "score": 75,
        "body": " I think it's ok to be upset when able bodied people come into a space that's supposed to be for us and try to center their experience. This is not a zero sum game or a competition. It's reasonable if someone who isn't part of this community comes into this space and is disrespectful to us and it no way stops me from being furious at lawmakers, corporations, politicians as well. If they are here asking about ways to support a disabled person etc that's different. But so much of the world is built for able bodied people, wanting to have a space that is ours where we feel accepted and comfortable and supported is understandable."
      },
      {
        "id": "nvt9488",
        "score": 68,
        "body": "shitty people don't respect boundaries\u00a0"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1r5qwjt",
    "title": "Felt this :/",
    "body": "digitally giving a hug to all those that need and want it <3",
    "flair": "Image",
    "score": 730,
    "comment_count": 16,
    "created_at": "2026-02-15T21:39:45+00:00",
    "top_comments": [
      {
        "id": "o5kzm91",
        "score": 24,
        "body": "This is not quite for me, it\u2019s deafening!"
      },
      {
        "id": "o5lx27x",
        "score": 24,
        "body": "Amen. I'm not what anyone would call severely disabled, just multiply disabled, and even so, it's erased not only my plans, but between the extra demands on my time and energy, and the sheer unpredictability of it all, not to mention the poverty of not being employable, has made even my backup plans impossible."
      },
      {
        "id": "o5nzgh8",
        "score": 14,
        "body": "I had to sell my beloved horse and let go of all my dreams when I became disabled. I was then belittled and told to stop moaning by my now ex husband. Nobody really appreciated or cared what I'd lost."
      },
      {
        "id": "o5te3tv",
        "score": 10,
        "body": "Grieving oneself is so complicated and dissociating \ud83d\ude22"
      },
      {
        "id": "o5nt37e",
        "score": 7,
        "body": "This is so simple yet explains it so well. I don't know what path I would've gone down had I not gotten sick, but I know it wouldn't be this one. \n\nI'm starting to be okay with that now, but it's still hard."
      },
      {
        "id": "o5mewul",
        "score": 5,
        "body": "\\*hugs back at you\\* I feel this so much."
      },
      {
        "id": "o5vfv3j",
        "score": 5,
        "body": "I'm glad he's your ex now. I'm so sorry."
      },
      {
        "id": "o5umnfa",
        "score": 3,
        "body": "Yes going to college for 6 years only to not be able to work is a special kind of grief. \u2764\ufe0f"
      },
      {
        "id": "o5sseb3",
        "score": 2,
        "body": "It's not like I can go skiing or skating anymore or play any sport publicly or professionally so I say the grief is quiet."
      },
      {
        "id": "o5vr9o0",
        "score": 2,
        "body": "Oh chronic illness does **not** ask. It just gets in your way until you give up."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1jjkrca",
    "title": "I\u2019m waiting in a food bank right now and wondering how my life turned out this way.",
    "body": "I have 2 music degrees. Paid off all my school loans and have no debt. My house is paid for outright due to my divorce. I worked as a board certified music therapist for a local hospice for 9 yrs. Then I got sick myself. I\u2019m so angry. I\u2019m in year 4 of treatment and I\u2019m so effing tired. \n\nIt wasn\u2019t supposed to be this way. I was supposed to work as a music therapist and help people. That\u2019s my niche. It\u2019s one of the few places I belong. \n\nThe food pantry opened at 9:00 am. I came right at 8:50 and there was a line out the door. How did I end up in this position? Why do all these people need food?? Why is our govt such a big piece of shit? I get snap benefits and disability and all that but UGH. No one says \u201cI want to grow up and be disabled\u201d. \n\nI\u2019ll keep my ticket and always remember how humbling this was. How low and unworthy I feel. \n\nHeads up everyone. We didn\u2019t ask for this. Thanks for listening. I just wanted to get this out. \n\nETA: Wow. I got back from my IV infusion, laid on the couch, and opened Reddit to end up reading very meaningful stories in response to my post. Keep sharing everyone. We are all suffering and deserve to be heard. We are not alone in this. \u2764\ufe0f\ud83d\ude4f Sending love and grace to all of you. ",
    "flair": "Rant",
    "score": 725,
    "comment_count": 128,
    "created_at": "2025-03-25T14:32:37+00:00",
    "top_comments": [
      {
        "id": "mjntcr7",
        "score": 200,
        "body": "And see this is the thing that makes me mad. People really do think there's some magical way we could heal our bodies and be fully able bodied but we just choose to not. Cause for some reason we like this.\n\nI have litterally had people say to me that my disability isn't as severe as I make it sound. And it's like >.> it is. Because the stories come from my lived experiences in childhood and adult life with medicine.\n\nWhich is to say, you are very right. no one fucking chooses this!. But I will say with it forced upon us so many disabled people choose to continue to live through it and do their best to live a life with it right there.\n\nI really wish able bodied people got that. That we are already fighting past so much to just show up sometimes"
      },
      {
        "id": "mjnyv0g",
        "score": 82,
        "body": "My mother, a couple days ago, \"the human body is an incredible healing machine if you give it what it needs to do so\" aka if I just worked out, thought positive, and ate from Whole Foods I'd magically be fine."
      },
      {
        "id": "mjnxlis",
        "score": 71,
        "body": "i never thought i'd be in a homeless shelter waiting for hot food. one worker didn't like me and would give me the burnt pieces of meatloaf, yes i'm not kidding"
      },
      {
        "id": "mjo4s3t",
        "score": 47,
        "body": "\\*random internet stranger hugs if you'd like them\\*\n\nI can relate to this a lot-- I've been working for years as a medical laboratory scientist, doing cancer and autoimmune disease and transplant testing, wanting to help people get the information about what's going on in their bodies so they can get appropriate medical care.  I got a repetitive use injury at work 13 months ago and the original surgeon botched my first surgery so badly, basically disabling my dominant hand for the rest of my life.  I've had 3 surgeries at this point and going back to work sounds near impossible with how much constant pain I have in my wrists now, but I miss it like crazy and want to get back to the work I love doing, the work that I worked so hard to go to school for.  We didn't ask for this, and we aren't lazy.  We are worthy of love and care and still have beautiful things to offer this world.  Our country just makes you feel like shit for asking for any kind of help for any reason.  You definitely aren't alone.  If you'd like a friend to chat with, I'm always happy to listen-- feel free to drop me a DM."
      },
      {
        "id": "mjodx6e",
        "score": 45,
        "body": "I have a rare, incurable disease that has left me completely immobile. I lost a 45-year career as a professional director-choreographer of live musical theatre. My heart bleeds for my old life every day, BUT over time, I have found a new purpose. You have to feel like you are a productive member of society in some way. It can take a long time to figure it out, but it is a must.\n\nLife can be cruel, but you can turn it around, baby steps every day. \n\nStay strong \ud83d\udcaa Go with Love \u2764\ufe0f"
      },
      {
        "id": "mjozihc",
        "score": 41,
        "body": "I did all that and still turned out disabled and chronically ill. My doctors told me, \u201cYou have done and are doing everything right, it just doesn\u2019t always turn out the way we planned.\u201d :/"
      },
      {
        "id": "mjo1yq4",
        "score": 38,
        "body": "Nope. Nobody asks to become disabled. \n\nAnd nobody asks to be born disabled as in my case and unable to work. \n\nIt\u2019s shit.\n\nAble bodied people do not and will never get it.\n\nAnd to the people in the back thinking we voted for the OrangeStain, we didn\u2019t."
      },
      {
        "id": "mjowbej",
        "score": 35,
        "body": "This reminds me of my mom... I went on medication for my disability and it made me gain weight. So then it was \"you'll feel so much better if you just lost weight\""
      },
      {
        "id": "mjo4l6s",
        "score": 34,
        "body": "If it helps, gott ms after working as a public defender for 20 years. I found some disability rights activists online and that's good.  Can send link\n I think becoming disabled later in life is different than being born disabled.  Not easier or harder, just different.. I hear you.."
      },
      {
        "id": "mjozwwx",
        "score": 31,
        "body": "\"Yes mother, it would be really healing to give my body some much needed fresh air and a fresh set of parents who don't entirely believe in this deranged idea that humans can heal themselves eternally and never age or fall sick if they just eat well, think well and go to the gym.\""
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1nw88zm",
    "title": "This is EXACTLY what my Autism assessment looked like when I got one as a kid AND as an adult. (Well it was 1986 when I got the one I got as a kid so go figure!",
    "body": "This is EXACTLY why I cannot watch Love On The Spectrum!  They send the message just ASSUMING That everyone is blessed with these rich loving and supportive families who pay for everything support and otherwise.  Well I am one of many who has no family or relatives to help and is making due with what they have!  \n\nFor example: I need a paid supporter/buddy to go places with me but I have always just gone without, sucked it up, and did everything myself as I still do today.  My insurance (Meridian or any of the other plans with Medicaid available) will NOT pay for that.  If it's Autism related reasons you have to be under 18, if it's disability related you have to be either a shut in, bed bound, or 62 or over.  I just got used to it, learned to live with it and be grateful that or bed bound!  \n\nI can't be Pollyanna 24 hours a day but I sure try!  Lol.  That's MY \"glad game\"!   Lol.  My reasons for being glad that I don't meet the criteria for the services I need: I'm GLAD I don't have any of those problems!  \ud83e\udd17.  \n\nI used the same technique when perimenopause reared it's ugly head in and my insurance company wouldn't pay for the GLP1s. (You have to have a BMI over 35 and have a type 2 diabetes diagnosis ).  \n\nWell the weight gained took longer to come off but it did with the right medications (nowhere near as strong as the GLP1s but they helped! With a high protein whole foods diet and exercise of course). \n\nI receive SSI, Section 8, Medicaid, food stamps, AABD, free bus card for elderly and disabled, license plate discount, and Paratransit services.  For social needs, I work the allotted 20 hours a week allowed to keep your benefits as a peer counselor at a mental health clinic, volunteer at the Salvation Army Women's Transitional Center on weekends and holidays, I have church, meet ups, and a Neurodivergent support group online and in person with meet ups once a month.  \n\nMy friends and I all support and help each other all we can but like many we can't ALWAYS be there to help cause we're all trying to make our own ends meet.  Anyway while the reality of the situation totally sucks, I choose to be happy and grateful for all that I DO have and all that I have going for me!   \n\n",
    "flair": null,
    "score": 716,
    "comment_count": 80,
    "created_at": "2025-10-02T16:17:36+00:00",
    "top_comments": [
      {
        "id": "nhe5wcx",
        "score": 52,
        "body": "Ugh I feel you. I have avoided an adult autism diagnosis for this exact reason. My psychiatrist, who also diagnosis autism, did an off book assessment for me and confirmed it. For me, that's enough, but it sucks so much that adults with higher support needs can't get them."
      },
      {
        "id": "nhe798m",
        "score": 37,
        "body": "My entire existence, more or less.\n\nA lot of resources for \"mental health\" are designed either for children or hyperspecific groups. Talk about the trauma of being left behind..."
      },
      {
        "id": "nhfvkh4",
        "score": 27,
        "body": "Not autistic, but all the Cerebral Palsy resources are the same: They're for parents of kids with CP, or kids with CP, *not* for adults who have Cerebral Palsy. At most, they might have resources under the general Brain Damage/TBI/Neuro issues umbrella, but that may also have a lot of stuff that doesn't apply. This is a disability that you're largely born with, but kids obviously *grow up* and it's not like brain damage can be *cured*. You might find luck with a rehab hospital or maybe your pediatrician/pediatrics service doesn't mind you staying on a couple years but eventually you have to move to adult services, or you move to another state and you have to start all over again. Sure, adults might have a rare study or two, but all the research is on kids, all the resources? On kids and schooling, kids and developmental milestones, kids and..  kids and.. At most you'll find a resource for students in college sometimes. No adult things, nothing about how it is for those with CP to work in the workforce, nothing about people driving or doing taxes or *normal* adult things. No resources on how to adapt to that either, just: \"Ask your parents\" \"Work with your kid\" \"talk to your PT about these exercises\" \"enroll your kid in Early Intervention!\".\n\nCrickets for adults. Absolute *crickets*. Your symptoms get worse because you work now? Your symptoms get worse as you age? Nothing from the medical community besides - sorry, contact these doctors (Who have no idea how to help you because the last time they interacted with those with CP, it was in their Peds rotation years ago). \n\nNo, instead you have to scroll through Reddit and hope that *someone* out there has the same kind of CP, at the same level, with the same issue, with an answer that isn't just: \"Yeah, good luck! That's aging for you!\". Nothing against Reddit, but it's fucking *exhausting* having to figure it out all on your own and to have everyone figuring out the same exact things. I know more about my own damn disability than my doctors do sometimes, and that's fucking *infuriating*. Kids with CP, kids with Autism *grow up*, give us the damn resources we're owed, stop catering to kids when there's a whole *giant* and *growing* subset of us that *need* support.\n\nSorry for the rant, but I feel you so much, and *yes*, it's infuriating, you have the right to be pissed."
      },
      {
        "id": "nhf2xui",
        "score": 22,
        "body": "I definitely feel you, its the same for tourettes. All resources the tourette associated of America provides are for children or parents of children, and pretty much next to nothing for adults. Its hard when all these organizations are ran by people who dont live with it. Adults are left behind and kids are trained like dogs to be normal, and when they have persisting difficulty in adulthood its labeled as their fault."
      },
      {
        "id": "nhejnea",
        "score": 16,
        "body": "Love on the spectrum feels very exploitative towards their higher support needs cast members in general"
      },
      {
        "id": "nhf1kgj",
        "score": 16,
        "body": "> A lot of resources for \"mental health\" are designed either for children or hyperspecific groups. Talk about the trauma of being left behind...\n\nI have cerebral palsy. Used to get services for it through Easterseals. Tried to get services for CP  and mental health as an adult through them but can't because I don't have the right mental health diagnosis and can't get services as someone with CP because I'm not a child with autism nor do I have a co-occuring diagnosis of intellectual disability."
      },
      {
        "id": "nhgxqv4",
        "score": 16,
        "body": "I have a friend with CP and it's amazing how thoroughly she is ignored by the medical community.  It's like since she's not in a chair and able to speak for herself, she doesn't deserve CP services, or mental health services."
      },
      {
        "id": "nheysz7",
        "score": 15,
        "body": "Exactly!  I've actually been BLAMED for mine by mental professionals before."
      },
      {
        "id": "nhh4ks2",
        "score": 13,
        "body": "We talked about Autism in my class today and I specifically asked why we still have so few services and interventions for adults.\n\nWhile I understand the answer I still think it's bs that in 20 years we haven't managed to broaden the services so adults can prosper and get the support they need."
      },
      {
        "id": "nhjy1ib",
        "score": 13,
        "body": "I am very clearly autistic, and in my state, it is literally impossible for an adult to be diagnosed. All existing services are only for children."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1pwahsy",
    "title": "Successfully Made and Hosted Christmas Dinner, Despite Being Disabled!",
    "body": "I wanted to share this win!\n\nI was able to successfully plan, make, and host a Christmas dinner for myself and 3 other disabled friends and their dog, despite being told not to because \"disabled people dont deserve it\".\n\nI wanted to host a Christmas dinner as I havent had a real one in years due to my disability worsening. I reached out to my local queer groups online to ask for help thinking that they would be the most understanding but was met with people saying me and my friends \"dont deserve it\", \"shouldnt do it\", and are \"terrible friends\" for wanting to make an accessible and easy Christmas dinner and mini party. Then I was quickly banned. \n\nTheir reasoning was that if I couldn't figure out  accessibility logistics then I probably wasnt meant/deserve to have a Christmas dinner because Christmas should be easy to plan. They also said my friends were terrible friends for needing accomodation and that they should be giving up accessibility to \"make it easier\" for me. And they wanted my friends to abandon their puppy so we can host at locations that aren't pet friendly.\n\nI dont know if my friends are actually terrible friends or not but I wanted to do this for them and for myself. I never had an actual Christmas that I enjoyed. I always spent Christmas working or at home alone. My friends are elderly witha wheelchair in an SRO with family far away. So... Despite everyone telling me not to, I did it.\n\nI made a turkey, roasted veggies, and got instant gravy and canned cranberry sauce. My friends cleaned their place and got the drinks. I even made the puppy her own dog friendly meal. I bought a folding table to hold the food since they dont have furniture (and it wouldn't be a big deal if the table got stolen, which happens often there) and even made turkey broth with the bones and got them a gift.\n\nThe day of I cooked everything and shoved it all into an uber and met them at their place. The turkey almost didnt cook right and the oven was too small to fit everything but I made it work.\n\nMy friends were saying how much they appreciated it and that this was something they didn't know they needed. I think it healed everyone's mental health a bit that day.\n\nIm very happy I was able to do this. I think disabled people should deserve a Christmas dinner and love, even if accessibility is an issue. I hope my city is kinder next year.",
    "flair": "Image",
    "score": 712,
    "comment_count": 58,
    "created_at": "2025-12-26T17:58:16+00:00",
    "top_comments": [
      {
        "id": "nw26axd",
        "score": 36,
        "body": "What groups? You should share them here so we can shame them"
      },
      {
        "id": "nw28stj",
        "score": 30,
        "body": "eff the nay sayers and haters. we gotta celebrate in any form despite everything.\u00a0"
      },
      {
        "id": "nw243ye",
        "score": 27,
        "body": "Great job I\u2019m so proud of you"
      },
      {
        "id": "nw2azlb",
        "score": 20,
        "body": "Im so proud of you!!!! \n\nI may have overdid it the last few days and am paying for it today, but I feel happy and proud of myself for baking all day for my husband's family (my family are all in a different country), and then making the two of us (and my cat!) Christmas breakfast. \n\nIf I feel better I may make ooooooone more meal, but I'm still counting it as a win!\n\nIt's absolutely disgusting that a queer group, of all groups, would shame you and your friends like that. You'd think a widely misunderstood and persecuted group of people would have more compassion for the disability community."
      },
      {
        "id": "nw26t00",
        "score": 17,
        "body": "Theyre on Facebook. Not sure what the rules are on here for shaming other online groups \ud83d\ude1e"
      },
      {
        "id": "nw2txkz",
        "score": 15,
        "body": "People saying those with disabilities don\u2019t deserve a normal life?\n\nJesus that\u2019s brutal. \n\nWhat the hell is wrong with some people?"
      },
      {
        "id": "nw22wbn",
        "score": 13,
        "body": "\ud83d\udc4f\ud83c\udffe\ud83d\udc4f\ud83c\udffe\ud83d\udc4f\ud83c\udffe"
      },
      {
        "id": "nw2kxa3",
        "score": 12,
        "body": "Who the fuck said anything about anyone \u201cnot deserving it\u201d what the fuck??"
      },
      {
        "id": "nw2ag3a",
        "score": 12,
        "body": "I think so too. I never celebrate anything after identifying as disabled as its seen as an inconvenience in my culture sadly."
      },
      {
        "id": "nw2c0nn",
        "score": 12,
        "body": "Thank you\n\nYea I'm paying for it too with major burn out \ud83d\ude2d\n\nIm proud of you too for doing all the baking, must be so delicious! I can't bake \ud83d\ude02 because the rigid instructions are not compatible with my ADHD \ud83d\ude02\n\nYes, I thought so too, which was why I asked there because I thought a group of minority, especially one with many disability overlap, would be understanding. But it seems that group has been dropping hints of ableism for a while and that was the last straw."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1qieyl9",
    "title": "I never truly realized how many people want to kill disabled people",
    "body": "I was just scrolling on Tiktok when I came across a news post about a woman who killed her disabled child and then herself. Almost every single comment was trying to justify her actions, mothers saying they understand and implying they would do the same, people acting like it was a good thing to do... \n   \n As a severely disabled person, it's terrifying seeing how many people openly admit to having so much hatred towards disabled people they think it's right to kill them for existing and being disabled. I am having a panic attack right now because that is how terrified I am, and I never have panic attacks. It is awful knowing that most people want to kill me. I am so scared. ",
    "flair": "Rant",
    "score": 688,
    "comment_count": 111,
    "created_at": "2026-01-20T21:59:01+00:00",
    "top_comments": [
      {
        "id": "o0r7lcq",
        "score": 357,
        "body": "Disability day of mourning was created because of the amount of disabled people that gets killed by their care givers, and because of those disabled people not getting truly mourned (because people assumed the disabled people were burdens and suffering). If I remember the statistics correctly it's about two disabled people every week that gets killed by caregivers THAT WE KNOW OF. The number is likely higher. It's a harsh world out there for disabled people."
      },
      {
        "id": "o0qwm29",
        "score": 159,
        "body": "It's absolutely not most people, that's just social media algorithms and bots pushing rage bait/extremism. Bots are literally everywhere and indistinguishable from real people making controversial comments to drive engagement.\n\nThat said, there are a lot of people who don't believe disabled lives are worth living, but for most those beliefs stem from ignorance and internalized ableism not hatred.\n\nI think it's important to remember that most people with disabled children/family members do love them and care for them. The people that don't are the minority."
      },
      {
        "id": "o0rbfnm",
        "score": 128,
        "body": "Filicide. \n\nThat\u2019s a thing in the disability world. Unstable parents who bears children with disabilities gets their world turned upside down and can\u2019t see a way out so they kill their own child."
      },
      {
        "id": "o0rpur7",
        "score": 94,
        "body": "This is it. Living in a society where an able-bodied parent can barely sustain their own life if at all, let alone be the guardian of a life that is entirely dependent on them, or send that child into a foster system that is rife with abuse and awful living conditions. The entire system itself is broken. I wish we had more social safety nets that offer medical, financial and assisted living care. That child didn't deserve this fate."
      },
      {
        "id": "o0tz5ej",
        "score": 68,
        "body": "The date is March 1st. They have a website [here](https://disability-memorial.org/)."
      },
      {
        "id": "o0r9a6a",
        "score": 48,
        "body": "And even of the minority that are ableist, most of them wouldn't say people should kill disabled people. They are probably more along lines of \"not my problem\" or \"you are making excuses\"\n\nSocial media is showing us the most extreme political case; and even if they aren't bots, which they probably are, it is also not accounting for that people will behave less so in a public situation vs anonymously online (where they can shitpost for like a minute onto the bandwagon and have no consequences to fear)"
      },
      {
        "id": "o0rxeto",
        "score": 43,
        "body": "Pretty much. Support for caregivers is TERRIBLE, but for them to get adequate support, us as disabled people would have to admit that we DO take a lot more to raise and keep alive, which we have not been doing very good at. We take to attacking caregivers more often than not instead of listening to their struggles and figuring out how to get their needs met too so it's not so hard for them to meet our needs."
      },
      {
        "id": "o0r12bg",
        "score": 39,
        "body": "You're using TikTok. It's time to get off of that crappy app."
      },
      {
        "id": "o0qz88c",
        "score": 38,
        "body": "I agree. This is a really important point. Some people absolutely do hate/fear what they dont understand. However, the majority of people don't think like that. Most people are not evil / lacking in empathy.  It's really big in the media right now though. I blame the Orange one."
      },
      {
        "id": "o0r4la8",
        "score": 36,
        "body": "Totally. Most people just don\u2019t give a flying fuck about us"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1oha0oi",
    "title": "SNAP is gone?",
    "body": "Anyone else on SNAP get a notice that no funds for food will be available due to the shut down? Right for the holidays? This will be the worst holiday ever. I don't know what I'm going to do. Thanks to the current administration.",
    "flair": "Article / News",
    "score": 691,
    "comment_count": 462,
    "created_at": "2025-10-27T09:38:39+00:00",
    "top_comments": [
      {
        "id": "nlmqfmb",
        "score": 485,
        "body": "It's so horrific. The admin is willing to starve its own people in order to try and force through massive cuts to healthcare, SNAP, and most social safety net programs. And if people revolt, they'll use it as a reason to declare martial law. Go to food banks now, while they still have food. They are going to be heavily depleted, especially because Trump already cut their funding.\n\nGet in touch with whatever community you can. It is going to be grueling.\n\nEDIT: I completely understand that food banks are not always accessible or available. Part of why I also mentioned community. I hate this government and I hate that so many people don't have options and I am sorry if I didn't include enough detail. I just didn't want to say like \"well if you don't have community or food banks you're fucked.\" I can say try 211, look into local churches, talk to your neighbors. I just. This is scary and I hate it and I'm sorry if my comment came across as tone deaf."
      },
      {
        "id": "nlnecl8",
        "score": 363,
        "body": "We should be in the streets , he is building a ballroom while we starve"
      },
      {
        "id": "nlmh32j",
        "score": 165,
        "body": "I\u2019m scared right now, and it\u2019s causing me to loss sleep. I don\u2019t know what I\u2019m going to do other than use up my credit cards AGAIN! It\u2019s not the democrats fault either. It\u2019s the administrations, and they\u2019re doing this to avoid the Epstein file releases"
      },
      {
        "id": "nlngv7d",
        "score": 135,
        "body": "We need his own people to finally see who he is. I\u2019m disgusted by benefits being turned off but I hope enough of his followers are hurt that they are willing to stand with the rest of us. They all think his cruel policies are for \u201cthe bad ones\u201d and never thought they\u2019d get hit too."
      },
      {
        "id": "nlmjcya",
        "score": 113,
        "body": "That, and they possibly want to provoke riots so they can enact the insurrection act"
      },
      {
        "id": "nlpv7ku",
        "score": 108,
        "body": "The lines here at food banks are already over 2-3 hours long and some of the food is moldy.  Some senior centers allow disabled people to join and they help with food."
      },
      {
        "id": "nlmz9bq",
        "score": 102,
        "body": "This whole situation is infuriating. We stocked up on non perishable foods, but this is ridiculous.\n\nThe republicans say that dems want to provide health insurance to those who are here illegally, yet when you look it up, it\u2019s skyrocketing health insurance for families, some up to $21,000 a year. The amount of disabled people that will not be able to work emerging from this will be insane. To use starvation to make one side (democrats) concede is the same evils we see in genocide. \n\nFood shouldn\u2019t be a weapon. You\u2019d think with his narcissistic personality, Trump would save ebt last minute so he\u2019s cheered on and loved for it. Yet here we are, many of us won\u2019t be able to make it through November without the assistance of food banks. \n\nYet it\u2019s not just EBT users that will suffer. This will create a domino effect that will affect everyone."
      },
      {
        "id": "nlqxi8e",
        "score": 99,
        "body": "This is also something that homebound disabled people cannot do. Most food pantries do not deliver. They\u2019re already hurting. They don\u2019t carry the foods people need for chronic illness & specialized diets.  People need to be donating directly to disabled homebound folks."
      },
      {
        "id": "nlnaa01",
        "score": 98,
        "body": "Engels called it Social Murder \n\nhttps://en.wikipedia.org/wiki/Social_murder?wprov=sfla1"
      },
      {
        "id": "nlmzjjx",
        "score": 77,
        "body": "To hear that Trump's not doing anything only makes my worry grow more than what it is. Seeing all the anti-SNAP and \"people on SNAP just need to stop being lazy and go get a job\" stuff on social media doesn't help any either."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1qguxps",
    "title": "Restaurant in shopping center in my neighborhood always blocks handicapped accessible parking with chairs etc so I put it in front of their door.",
    "body": "",
    "flair": "Rant",
    "score": 678,
    "comment_count": 91,
    "created_at": "2026-01-19T04:58:08+00:00",
    "top_comments": [
      {
        "id": "o0fedgj",
        "score": 294,
        "body": "If this continues to be an issue, call the local non-emergency police number."
      },
      {
        "id": "o0fihux",
        "score": 154,
        "body": "You\u2019re more polite than me. I mean, if they didn\u2019t want their special little chairs smashed they shouldn\u2019t put it in the place for people with disabilities to park their CAR"
      },
      {
        "id": "o0fhcvi",
        "score": 135,
        "body": "I keep saying that I wish we could start a handicapped violator shame site.  Post pictures and places of people parking in handicapped spots with no placards or just not offering enough spots.  No one is policing any of this.  I saw a women park in a handicapped spot to pick up her take out.  Annoying.  I have felt that it\u2019s gotten worse lately.  Is that just me?"
      },
      {
        "id": "o0fzzrh",
        "score": 86,
        "body": "Yeah, I have a crappy old car that's already beat up. I would just run that chair the eff over."
      },
      {
        "id": "o0fhqhx",
        "score": 80,
        "body": "This restaurant is using it for their delivery deliveries which could explain it getting worse \u201clately\u201d"
      },
      {
        "id": "o0fov2o",
        "score": 74,
        "body": "Report the restaurant to authorities for blocking handicapped parking."
      },
      {
        "id": "o0ho82t",
        "score": 70,
        "body": "Our local force could really not care less."
      },
      {
        "id": "o0hpcv1",
        "score": 52,
        "body": "It\u2019s a violation and likely a ticket. That means revenue for not a ton of work. Have you tried calling them?"
      },
      {
        "id": "o0fmu0n",
        "score": 42,
        "body": "if you or anyone you know has an electric wheelchair, you should park that in front of their door."
      },
      {
        "id": "o0g2rnh",
        "score": 39,
        "body": "cars depreciate so fast anyway that I don't even worry about it even when my car is fairly new x)"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1pty0w0",
    "title": "Someone posted this shit on tiktok and it's the most dehumanising post I've ever seen.",
    "body": "It's supposed to be \"funny\" and you can see that the hashtags are all about the post going viral and it actually did but it's so messed up how people just joke about us as if we're a burden that's supposed to be disposed of. Why do people just keep assuming our lives are horrible? Yes my life comes with challenges but that doesn't mean my life is terrible. If someone wanted a child they should be ready for all the consequences including the child being born disabled.\n\nI genuinely can't stand people who just joke about everything and don't take life more seriously.",
    "flair": null,
    "score": 685,
    "comment_count": 168,
    "created_at": "2025-12-23T16:20:23+00:00",
    "top_comments": [
      {
        "id": "nvknh3d",
        "score": 347,
        "body": "I work with disabled kids and just had one of my clients die, and it\u2019s been wrecking me. I can\u2019t imagine it being my own kid and being this heartless."
      },
      {
        "id": "nvkg79d",
        "score": 218,
        "body": "There is a lot of propaganda pushing hatred and othering of disabled people."
      },
      {
        "id": "nvksp1u",
        "score": 206,
        "body": "Ableism is so normalised \ud83d\ude2d."
      },
      {
        "id": "nvl4o2l",
        "score": 165,
        "body": "This is somewhat even beyond ableism, I\u2019d say this is downright eugenics"
      },
      {
        "id": "nvkpqb5",
        "score": 164,
        "body": "The fascists are manufacturing consent to kill disabled people. The Holocaust didn't start with killings, it started with dehumanization."
      },
      {
        "id": "nvkh4s2",
        "score": 114,
        "body": "Post a person who put it up don't cross out their name. If they post it, they want to be seen."
      },
      {
        "id": "nvl4lu3",
        "score": 92,
        "body": "The amount of casual eugenics ideals all over social media is indeed disturbing. People don\u2019t even realize it either."
      },
      {
        "id": "nvkrxly",
        "score": 84,
        "body": "A few years back in my country a woman wrote a book about how she murdered her disabled infant. She was invited on TV and shit to talk about her book like \"wow that's so interesting and emotional\"."
      },
      {
        "id": "nvkn0wb",
        "score": 61,
        "body": "This doesn\u2019t surprise me the autism parenting sub is full of assholes like that! They abuse their children treat them like a burden and then that sub is full of people to \u2018\u2019understand\u2019\u2019 them, it\u2019s disgusting and I don\u2019t understand how people like this are allowed to carry on with groups like that! The very least they should be banned!"
      },
      {
        "id": "nvkgqr5",
        "score": 53,
        "body": "The painting is not AI. It\u2019s from 1878 titled \u201cAnguish\u201d by French-German oil painter August Schenck."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1mol7w1",
    "title": "people need to stop telling us to \u201cjust\u201d get a remote job",
    "body": "dude it\u2019s fucking insane, they aren\u2019t any remote entry level jobs. i\u2019m autistic and my job is fucking killing me and it\u2019s so easy, fuck. it makes me so angry because no i cannot work at a company for two years than beg to maybe get an accommodating jobs. \n\nno i don\u2019t qualify for ssi or anything because i CAN work. places don\u2019t want to accommodate me because im simply annoying to deal with. \nworking remotely would give me so much independence. \n\ni am a hard worker too! i just can\u2019t do it anymore guys it\u2019s driving me insane. i know they\u2019re no real resources out there for people like me. im just tired of people saying bullshit  that doesn\u2019t exist. \n\n\nif i had a remote job i would be able to shower, clean and not be constantly suicidal due to burnout. i refuse to call out due to my burn out anymore because they have made it clear they\u2019re getting tired of it. \n\n\nit just makes me so mad because they say we all want benefits, no i want a fucking chance to stay alive. i\u2019m only level one, how tf are level 2 people not on ssi dealing with this?",
    "flair": "Rant",
    "score": 680,
    "comment_count": 140,
    "created_at": "2025-08-12T21:14:11+00:00",
    "top_comments": [
      {
        "id": "n8cz33g",
        "score": 225,
        "body": "I filed for disability. They said because I would need 2 days off a month to recuperate, the voc expert said no job would hire me to lose me just twice a month. A month. WTF. This is the current job market?"
      },
      {
        "id": "n8d2ygq",
        "score": 120,
        "body": "I\u2019m on ssi & have epilepsy, among other disabilities. I\u2019m preparing for the possibility of losing my medicaid next year bc of the big ugly bill. i\u2019ve been told that if i can type on my phone, then i can get a desk job & that i\u2019m just lazy. if i stare at a computer for a long period of time, my brain can go haywire & i could have a seizure. i have a phone bc i need to be able to communicate with my family. not to mention the fact that i have oab & i would not be able to go a long time without a bathroom break & my bladder can be unpredictable. able-bodied people will never understand what it\u2019s like for us to be disabled. being disabled IS a job for us & trying to survive is a job. we wouldn\u2019t have to depend on benefits if our government would just give everyone affordable healthcare while THEY get to have all the healthcare we need &  a lot of disabled people are being told they\u2019re \u201cnot disabled enough\u201d to need medicaid."
      },
      {
        "id": "n8d3f54",
        "score": 83,
        "body": "when I had my ssi hearing, I was told by the voc expert that no one would hire me also"
      },
      {
        "id": "n8d3oir",
        "score": 64,
        "body": "My luck was a sympathetic judge who saw the facts."
      },
      {
        "id": "n8dgj5s",
        "score": 60,
        "body": "I\u2019ve been looking for remote jobs for a long time now. I keep applying and no call backs. It\u2019s not as easy as the able bodied non-disabled folks think it is"
      },
      {
        "id": "n8dxq0y",
        "score": 60,
        "body": "It drives me nuts because so many people seem to think remote jobs are also like some kind of miracle cure for disabled people. \n\nMy job is pretty much remote (they would like in one day a fortnight but it's pretty flexible). I've been working within my organisation, it's parent organisation and it's sister organisations for 14 years. The job used to be fully office based and became fully remote in early 2020 when we had our first pandemic lockdown and has remained basically remote since then. Meanwhile when I started I had a relatively mild disability, so much so it wasn't even worth declaring and over time my health has taken a swift decline and it was later found I have a genetic connective tissue disorder and various comorbidities. Then in 2023 I suffered from a freak accident and damaged my back. I ended up off sick for a year and a half whilst awaiting treatments.\n\nI'm now trying to go back to work and it hasn't been easy. Even my work's own Occupational Health doctor said she feels like she's been banging her head on a brick wall. Last year I tried returning to work briefly and I was sent for an appointment with her where it was suggested I dropped from 4 days a week down to 3. She also provided guidance on support I would benefit from in the office (I'd been on the waitlist for ADHD and Autism diagnosis for 5 years and since been diagnosed both). Yet when I returned to work I was told that 3 days a week \"did not meet the business need\" and that I needed to return to my usual 4 days a week and even that was generous as the position is supposed to be full time. She suggested the support again, including more consistency, clearer direction and job expectations. So far I've had 3 line managers in 2 months and still don't know what my job is now due to major team restructuring and staff changes.\n\nThe reality is remote working is just one little piece of it. Companies don't want part time workers, especially in corporate office jobs (it may be different in the service or retail sector), even if that is to better manage your health and your absences. They don't want to give time off for hospital appointments or medical treatments. They don't want people taking weeks off at a time for surgeries and recovery. They don't want the expense of providing extra specialist equipment. They don't want to have to consider accessibility in their organisation, or any of the buildings they use both internally and at external events. I even had to badger them to let me see the Occupational Health doctor this time, and they only did so when they asked my GP to sign off on my work hours for the next few weeks and my GP said they weren't comfortable to, because they're not a specialist Occupational Health professional. \n\nYes being remote can help a lot of people but that's usually not the only part of the equation and it's starting to do my head in when people think working remotely suddenly solves everything."
      },
      {
        "id": "n8eloah",
        "score": 60,
        "body": "Endometriosis doesn\u2019t get the recognition it needs re: how disabling it can be"
      },
      {
        "id": "n8dihfk",
        "score": 51,
        "body": "I had that same conversation in my court hearing 7 years ago, but it was 3 days for endometriosis pain"
      },
      {
        "id": "n8e8e3c",
        "score": 37,
        "body": "I would totally rock the interview and get hired. Then I would call out in my first week. \ud83d\ude44"
      },
      {
        "id": "n8d3l2s",
        "score": 33,
        "body": "I also have epilepsy along with pots syndrome, mcas, small fiber neuropathy, just got my denied for the 2nd time. I currently work part time on a computer all day and my brain feels fried. I have so much brain fog from too much screen time tnat i just space out and mess shit up at work. I hate it"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1kof0mv",
    "title": "A parent has asked a Facebook Photoshop group to make their 2 disabled children able-bodied. I feel nauseous but everyone is praising them for doing this \"wonderful\" \"beautiful\" thing for their children. Am I the bad guy?",
    "body": "I find this horrific and disgusting but apparently everyone else, including people on FB I know with mild invisible disabilities, find it \"heartwarming\". I'm just shocked. I thought it was a troll at first. What do you think, am I the one in the wrong for finding it terribly ableist and cruel? ",
    "flair": null,
    "score": 670,
    "comment_count": 259,
    "created_at": "2025-05-16T23:30:00+00:00",
    "top_comments": [
      {
        "id": "mspno3q",
        "score": 525,
        "body": "What is \"heartwarming\" about trying to rewrite the reality of your kids' lives?  I can think of a lot of words for it, but heartwarming isn't even in the ballpark. \n\nIn addition to the many other wrongs, it's also a massive invasion of their children's privacy and autonomy.  Putting your kids on display for a photoshop challenge? It makes me feel like I'm exploiting those kids just by reading the post."
      },
      {
        "id": "mspm87u",
        "score": 423,
        "body": "Wow. Just wow.\n\nI think most here will agree with you"
      },
      {
        "id": "mspngpg",
        "score": 172,
        "body": "That is bad.\n\nBut at the end of the day I'd want to know how the children feel about it. If they like the idea, then I think it has more merit... though I'd worry it would give everybody involved a back psychological kickback."
      },
      {
        "id": "msppusl",
        "score": 134,
        "body": "My sentiments exactly. I don't know what sort of thoughts these ppl could've put in their children's minds, like maybe that if they're strong enough, they can overcome an incurable disease/disability. My gut tells me they've been told that if they're only positive enough, they will walk one day. And if they don't, they'll be a huge disappointment.   \n\nPlastering their images on the internet for the world to see is diabolical to me. My heart is breaking for these kids. Like I'm literally crying over it. I highly doubt those kids are allowed to accept, and be secure with, their disabilities."
      },
      {
        "id": "mspq8sk",
        "score": 126,
        "body": "I often see this on the photoshop requests sub and I thinks it\u2019s gross as hell.There was a husband wanting t9 photoshop his wife who is in a wheelchair to see her how she was before she became disabled.Like..you already have photos of her,how about you love her as she is now?"
      },
      {
        "id": "mspribh",
        "score": 98,
        "body": "Loved ones refusing to accept reality and grieving as if you died is definitely one of the worst disabled experiences."
      },
      {
        "id": "mspm5w3",
        "score": 88,
        "body": "This is so bad it's hard to believe it's real."
      },
      {
        "id": "mspq2q2",
        "score": 76,
        "body": "I wonder if they'll have it framed, as \"motivation\" to \"get better\". I'd be willing to bet my life on it and it hurts my heart."
      },
      {
        "id": "mspsgvp",
        "score": 59,
        "body": "Yes, what if they themselves want to see a representation of themselves in a different way?  \nI wish we knew"
      },
      {
        "id": "msq4rco",
        "score": 59,
        "body": "Given how its worded it seems very much to be about the parents desire"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1mfkd6m",
    "title": "In honour of those of us who deal with this on the regular",
    "body": "This popped up in my Facebook memories, and I thought it was too good not to share here for those who can relate.",
    "flair": "Image",
    "score": 672,
    "comment_count": 28,
    "created_at": "2025-08-02T07:16:06+00:00",
    "top_comments": [
      {
        "id": "n6j1zzm",
        "score": 27,
        "body": "At least two people need to suggest it\u2019s all in his head."
      },
      {
        "id": "n6hprmx",
        "score": 26,
        "body": "Good thing some of them were smart enough to shit their mouth.\n\nOr actually dead\u2026"
      },
      {
        "id": "n6hw0lr",
        "score": 25,
        "body": "I need this on a shirt."
      },
      {
        "id": "n6kam74",
        "score": 18,
        "body": "Don't forget did you try to drink more water? Did you get a good night's sleep? Try meditation. Just control your stress levels. Doctors love that last one. Gosh did you know that you can cure all chronic illnesses if you just breathe and control your stress levels? I did it guys!! I cured everything! Even cancer! You just have to breathe!!!\n\n![gif](giphy|hPr3UNaOyxYdSqCHKl|downsized)"
      },
      {
        "id": "n6hxqhc",
        "score": 15,
        "body": "Ha, would be a cool shirt. This gave me a good laugh \ud83d\ude03"
      },
      {
        "id": "n6k5jqa",
        "score": 11,
        "body": "haha just got off the phone with a family member who apparently knows the cure to my yet undiagnosed heart condition is food"
      },
      {
        "id": "n6irugb",
        "score": 8,
        "body": "This is hilarious! Just what I needed today in my flare up"
      },
      {
        "id": "n6o4lun",
        "score": 8,
        "body": "And to try drinking water or Tylenol or to just lose weight"
      },
      {
        "id": "n6rtbr4",
        "score": 7,
        "body": "This is funny because the ones who spoke are the ones actually spewing sh*t from their mouths lol"
      },
      {
        "id": "n6krqqg",
        "score": 5,
        "body": "Exercise! Eat healthier foods! Do yoyoga!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1jszke3",
    "title": "Review: I used one of the affordable new exoskeletons, it's a game-changer!",
    "body": "Hi all, I have been disabled since 20, mostly using a crutch or stick and switching to a wheelchair for the big days out. I am 45 now and have rheumatoid arthritis and MCTD with a lot of muscle wastage. I become exhausted, with hot and painful joints after mere minutes of walking, and only have about 20 minutes in me before I *need* to rest. I am almost always short of breath, to the point that talking is difficult.\n\nThis weekend I used a \u2018walk-assistive exo-skeleton\u2019 for the first time, and it has blown me away so far. I did three experiments:\n\n* I walked for 6km, 9000 steps, 1 hour 30 minutes, around a nature reserve, with no stopping at all and no need to rest afterwards. Normally, I would feel absolutely awful, be panting for breath, and need to lie down to recuperate for a time.\n* A little later I went into town and added another 5000 steps, shopping.\n* Yesterday, I did my usual E-bike route. Normally, I\u2019d need to stop to catch my breath, change gear a lot, and risk assess my energy levels. With the exo-skeleton, I never stopped, never needed to change gear, and was never out of breath!\n\nAfter all of these excursions, I felt completely fresh and ready to go again, to the point where I had to be told to be sensible and go and rest! So yes, it's only very early days but I love it so far, and so I wanted to share it with my fellow disabled subredditors.\n\n  \nI think there are more of them coming onto the market now but I only own a [Hypershell Pro X](https://hypershell.tech/en-uk/products/hypershell-x) so I can only talk about that. (As an existing owner, I have a discount code if anyone should want it.)\n\nIf anyone has any questions I will happily answer them.",
    "flair": "Discussion",
    "score": 670,
    "comment_count": 204,
    "created_at": "2025-04-06T17:32:50+00:00",
    "top_comments": [
      {
        "id": "mlqt1nz",
        "score": 114,
        "body": "As someone with chronic fatigue, I wonder lost about how you felt/will feel in the following days. I can sometimes manage numbers like that in a burst of low-pain days, but then I\u2019m wiped for a week afterwards. How have you felt today/how do you expect to feel in the coming days?"
      },
      {
        "id": "mlquaip",
        "score": 89,
        "body": "Great question - one I would also like to know! I will report back tomorrow."
      },
      {
        "id": "mlqu5gb",
        "score": 68,
        "body": "I should probably do another post describing how it works, sorry! Basically, it senses your hip/thigh movements and augments them. So, if you're going up stairs it will help to lift your thigh to reach the next step and then press it down to lift you up. If you're walking or running it seems to just give your thigh a lift. \n\nIf you're familiar with how E-bike motors work, it's kind of like that, but it also learns and corrects your gait I think (I am weaker on one side of my stride)."
      },
      {
        "id": "mltz6mb",
        "score": 43,
        "body": "Copied my reply here for you: Okay, I am sorer today than normal, but it's a different kind of sore to what I feel when I overdo it. It feels more like there is pain in muscles I haven't used for a long time rather than my conditions have taken a big hit. Other than that, I can still walk and I am not bed-bound like I thought might be a possibility. So, that's very promising."
      },
      {
        "id": "mlqfrnv",
        "score": 38,
        "body": "What part of walking did it help with? I'm struggling to see what muscles it's augmenting.\n\nI cannot do stairs without a struggle because my quads are weak. Does this help?"
      },
      {
        "id": "mlr1uu7",
        "score": 36,
        "body": "There is a Hypershell Disability Group on FB already and people list their conditions so you could visit it and see if anyone with MD is already using one."
      },
      {
        "id": "mlqsj0m",
        "score": 34,
        "body": "They start at 799 USD so it's not cheap, but a lot cheaper than most 'disability tech' and it's cutting edge. I was looking at Quickie wheelchairs earlier and it made me sad."
      },
      {
        "id": "mlr238g",
        "score": 28,
        "body": "And I think it's 'cheap' because it's aimed at able-bodied people at the moment so the medical companies haven't added the disability premium rubbish."
      },
      {
        "id": "mlqg19c",
        "score": 25,
        "body": "Congratulations! \ud83e\udd73 You sound delighted. Right on"
      },
      {
        "id": "mlqsmnq",
        "score": 25,
        "body": "Thanks so much, more testing is needed, but it's amazing to have some independence back!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1kuuemu",
    "title": "finally got a wheelchair!",
    "body": "i got an awesome wheelchair (i got it from a thrift store for $90). i went to walmart with it and omg i didn\u2019t have a heart rate spike ONCE i was floored. i\u2019m so happy! i finally got it as i realized the internalized ableism isn\u2019t worth me going thru as many flares. slowly healing my inner thoughts against my own body\u2764\ufe0fi spray painted it purple cuz it\u2019s my favorite color and spray painted the thingys(pls tell me what they\u2019re called) white! i LOVE it, if im gonna use it might as well make it more me\ud83e\udef6",
    "flair": "Image",
    "score": 660,
    "comment_count": 98,
    "created_at": "2025-05-25T04:48:02+00:00",
    "top_comments": [
      {
        "id": "mu4id2q",
        "score": 39,
        "body": "I love that purple, it's so pretty!"
      },
      {
        "id": "mu4kuwd",
        "score": 14,
        "body": "Congrats! I love the color! Looks great!\n\nI need to get one. I have a generic but it doesn\u2019t feel like it fits me well. I need one fit for me. I have no idea how to do it though."
      },
      {
        "id": "mu4jagk",
        "score": 12,
        "body": "thank you!! it\u2019s even more gorgeous in sunlight i love it!"
      },
      {
        "id": "mu4nxf0",
        "score": 10,
        "body": "same this one\u2019s just a generic i\u2019ve been customizing it to fit me a little more but i found a website that does them more customized and on the cheaper side for wheelchairs but still a expensive it\u2019s called notawheelchair cheapest is $999 u.s."
      },
      {
        "id": "mu4sjiz",
        "score": 9,
        "body": "Ahhh the purple is fantastic. I\u2019ve never considered the possibility of spray painting mobility aids! Well done!"
      },
      {
        "id": "mu4l260",
        "score": 8,
        "body": "She purty."
      },
      {
        "id": "mu4o0hq",
        "score": 8,
        "body": "thank you! it was boring before so i thought might as well make it more me and pretty!"
      },
      {
        "id": "mu5u5t4",
        "score": 7,
        "body": "I came here to say that, too! \ud83d\udc9c"
      },
      {
        "id": "mu4th3f",
        "score": 6,
        "body": "it was super easy and you can do it sitting down too! i just took one of my dads wrenches it started taking things off and plastic wrapped the wheels and taped off the handles! had my bf do most of the spray painting cuz it hurt my fingers lol took 24 hours to fully cure and was able to put it back together easy too!"
      },
      {
        "id": "mu4mu9g",
        "score": 5,
        "body": "[removed]"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1jfytee",
    "title": "Good news for us all",
    "body": "A federal judge has blocked Elon Musk and DOGE  from accessing personal information on social security.  That's a win for now. Also Georgia passed a law allowing people with intellectual disabilities  and the disabled in general to receive minimum wage so no more sub minimum wages for them in Georgia.  With all the choas going on in thought it would be nice to hear some good news. ",
    "flair": "Article / News",
    "score": 661,
    "comment_count": 59,
    "created_at": "2025-03-20T20:31:37+00:00",
    "top_comments": [
      {
        "id": "miv0ko4",
        "score": 163,
        "body": "If only they obey the judge's order"
      },
      {
        "id": "mivo8ho",
        "score": 64,
        "body": "and they already said they won't / don't care what judges say"
      },
      {
        "id": "miv30h9",
        "score": 57,
        "body": "A bill like that coming out of Georgia feels like a huge win, that's awesome!"
      },
      {
        "id": "mivtii7",
        "score": 32,
        "body": "They have already accessed the information. Not only that, the way they pulled the info was reckless and put all of our info at huge security risk, and the administration keeps repeatedly disobeying other orders as well.\n\nNot to be a \u201cdebbie downer\u201d, but just being realistic about it all."
      },
      {
        "id": "mivw0vx",
        "score": 29,
        "body": "Yes, no surprise here, the \"republican\" party is a \"party before country\" party that consists of frightened politicians that are afraid of  trump's crazy Maga base, and the newer ones like marjorie taylor greene who would and will do anything to please trump. The power of the people however dangerous and damaging to our countries rule of law it may have to be as a last resort resolution Americans are going to have to take trump out by whatever means necessary unless they have something brewing behind the scenes that hasn't been leaked out yet from the cowardly majority party. I hope and pray for a peaceful plan because this country is worth saving from this group of hitler loving democracy destructive haters of anything and everything good that the majority of Americans still stand for and believe in. We must prevail. We will get through this together because together is the only way."
      },
      {
        "id": "miuz8bb",
        "score": 22,
        "body": "Let's hear it for checks and balances!  Go Judicial!"
      },
      {
        "id": "miwckuq",
        "score": 20,
        "body": "I hope we continue to get good news \ud83e\udd72 SSI is my only income\u2026"
      },
      {
        "id": "miwjkg6",
        "score": 15,
        "body": "It doesn\u2019t matter. They\u2019re not listening to judge\u2019s orders. They had a final deadline to respond to the court by 12:00 noon. They replied with a one page response from an FAA designate.\n\nTrump/Musk ordered both our Anti-Russian counter-intelligence and counter security division to cease.  \n  \nDOGE has ALL of our information including SSN, Credit Card, driver\u2019s license, bank info etc\u2026.  \n  \nI\u2019d bet money that the U.S. is going to get hit with a massive cyber attack. I\u2019m confident of it."
      },
      {
        "id": "miwkyhm",
        "score": 15,
        "body": "I live in Georgia, I'm a Federal Employee, my husband is a 100% P&T disabled Veteran, both my daughters are Federal Employees, my mom is elderly and is on social security, and my adult son has Down's Syndrome.  Right now everything we have is at risk on some level, this is a terrifying time for our country.  I'll take any piece of good news at this point, I spend almost every waking moment in worry and stress. It feels like we are all living a shared nightmare."
      },
      {
        "id": "miva7jl",
        "score": 11,
        "body": "Thank you.\u00a0 Good news is always welcome.\u00a0\u00a0"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1jmpqz4",
    "title": "I just love to wake up to hate....",
    "body": "The account is gone now thankfully, but unfortunately this hateful person is still on reddit",
    "flair": null,
    "score": 656,
    "comment_count": 184,
    "created_at": "2025-03-29T16:13:08+00:00",
    "top_comments": [
      {
        "id": "mkdli34",
        "score": 311,
        "body": "Geeze.... what is wrong with people? \n\nOur club is free to join for everyone. \ud83d\ude09"
      },
      {
        "id": "mkdp7l4",
        "score": 197,
        "body": "I appreciate everyone's kind words.\nKnow that my day has not been ruined by a sad hateful person. I did get a sad chuckle at how much they dug through my reddit account to target my disability.\n\nDon't let the haters bring you or anyone down \ud83e\udd18"
      },
      {
        "id": "mkdudie",
        "score": 155,
        "body": "We can even help this guy make some permanent 'alterations' so he can fit right in with the worst of us!"
      },
      {
        "id": "mkdk094",
        "score": 116,
        "body": "Guy got really butthurt over something you said and decided to bring your disability up in a cruel manner. Had this happen to me. I responded to the fucker and Reddit had the audacity to warn ME lol"
      },
      {
        "id": "mkdyl5s",
        "score": 68,
        "body": "At the very least, there could be a club involved.\u00a0"
      },
      {
        "id": "mkdv1hf",
        "score": 59,
        "body": "Aw, that would be nice. Like a club badge initiation kind of thing? \ud83d\ude39"
      },
      {
        "id": "mkdj7q6",
        "score": 57,
        "body": "Jesus fuck some people are just trash."
      },
      {
        "id": "mkdu06t",
        "score": 53,
        "body": "Considering the username, I would assume it doesn\u2019t really matter what they said. Just that they acknowledged having a disability.\u00a0"
      },
      {
        "id": "mkdm5mf",
        "score": 48,
        "body": "i'm guessing they're a very unhappy person who internalized a lot of hate. \n\nthey spent some effort just to make an account to spread more hate and suffering around that they got from somewhere and made some lasting impression on them. \n\na kind of cautionary tale of where that type of emotional pain can lead people sometimes and a good reminder to me of why to be compassionate to self and others. \n\ni'm sorry you were on the receiving end of such violent words. hope you have a better rest of your day today. take care."
      },
      {
        "id": "mkdqe6j",
        "score": 42,
        "body": "I find stairs are a much easier cockblock to overcome than a dogshit personality."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1joxxar",
    "title": "Call It What It Is: A War on Disabled People",
    "body": "Dear r/disability,\n\nLet\u2019s not waste time with pleasantries. The Trump agenda is a targeted, calculated assault on disabled people\u2014wrapped in the language of \u201cfreedom\u201d and \u201cefficiency\u201d while it grinds our rights into dust.\n\nThis isn\u2019t just conservative policymaking. It\u2019s structural violence. It\u2019s gutting essential programs, gutting oversight, gutting access\u2014then blaming us for the wreckage.\n\nMedicaid? They came for it with knives out\u2014proposing over $1.4 trillion in cuts. That\u2019s not trimming fat. That\u2019s slicing into the bone. That\u2019s home care, prescriptions, assistive devices, community access\u2014gone. And if you're not \u201cproductive\u201d enough to work? Too bad. They\u2019ve got \u201cwork requirements\u201d waiting for you, like disability is some kind of choice.\n\nSocial Security? They pushed policies to make it harder to apply, harder to qualify, and harder to survive while you wait. They\u2019ve gutted the agency so badly that disabled people are dying before their appeals even finish. That\u2019s not neglect. That\u2019s intent.\n\nEducation? They tried to dismantle the very agency responsible for enforcing our legal right to learn. The Department of Education was under siege, and so was IDEA. Their goal? Strip down protections, defund public schools, and call it \u201cschool choice.\u201d For disabled students, that translates to fewer accommodations, fewer services, and more doors slammed in our faces.\n\nCivil rights? They rolled back disability guidance across agencies. They stopped tracking data. They rescinded protections in housing, healthcare, and employment. Because if you delete the evidence of discrimination, you don\u2019t have to do anything about it. Erasure as policy.\n\nVeterans? Cuts to the very benefits promised in exchange for service. No shame. No honor. Just austerity for disabled vets, while they stroke billion-dollar defense budgets.\n\nEarly childhood supports? Slashed. Because why invest in disabled kids when you can abandon them early and call it \u201cparental responsibility\u201d?\n\nThis isn\u2019t tough love. It\u2019s eugenics through bureaucracy. It\u2019s death by a thousand paper cuts, with a smirk and a flag pin.\n\nThis agenda isn\u2019t about \u201cmaking America great again.\u201d It\u2019s about making it cruel again\u2014efficiently, bureaucratically, relentlessly.\n\nAnd we are not collateral damage. We are the target.\n\nWe see it. We remember it. And we will not shut up about it.\n\nJoin, start here: r/50501",
    "flair": "Rant",
    "score": 659,
    "comment_count": 94,
    "created_at": "2025-04-01T15:08:20+00:00",
    "top_comments": [
      {
        "id": "mkvp7om",
        "score": 81,
        "body": "[removed]"
      },
      {
        "id": "mkv8tx7",
        "score": 77,
        "body": "Preach. I\u2019ve been saying this for ages and people tell me to stop overreacting smh"
      },
      {
        "id": "mkvky6n",
        "score": 73,
        "body": "The UK is doing something similar. It's a shame because the UK has historically done so much for accessibility and inclusion and now they're going backwards into ableist policies that are only gonna get worse. I'm very worried for the state of my country and I'm heavily considering moving to Ireland."
      },
      {
        "id": "mkw9oe1",
        "score": 51,
        "body": "I feel compelled to drop this quote...:\n\n\"The Nazis frequently described disabled people as \u201cuseless eaters\u201d, \u201cempty human shells\u201d, and \u201clife unworthy of life\u201d.\""
      },
      {
        "id": "mkwin0j",
        "score": 43,
        "body": "It's not just the disabled though. \n\n**It's about bullying every vulnerable person**\n\nDisabled, LGBTQ2S, POC, the homeless, the poor. Anyone without wealth and political power. Many among the wealthy and powerful deeply, bitterly resent being forced to pay taxes to provide for the commonwealth. Many, perhaps all the people born to wealth and privilege don't like being told the less fortunate are their legal, social and moral equals. \n\nTrump is the platonic ideal of this. He was born to wealth and privilege. His father was a deeply racist and misogynistic man. Donald learned at a young age that \"Those People\" were inferior, born thieves, lazy \"useless eaters\". And so he hates those people. He can't possibly raise himself any higher. So the only way to impose the vast difference in stature he thinks there is is to force \"those people\" lower."
      },
      {
        "id": "mkw4g3m",
        "score": 34,
        "body": "Since at least the 2008 crash the UK has been worse at how they treat the disabled. My sibling is an ivy league grad healthcare worker who nope'd right out of Britain over how they were treating the disabled. At one point they were playing stupid games like asking program claimants how they are (a normal greeting in social environments) and then arguing they're good enough to go back to work if they responded the socially normal way of \"okay...\" instead of \"horrible my XYZ is bad!\" Telling quadriplegics they were well enough to work manual jobs etc. It would be like a bad Monte Python skit if not for how morally wrong it was."
      },
      {
        "id": "mkwastb",
        "score": 34,
        "body": "And the most recent iteration calls disabled people, etc., parasites."
      },
      {
        "id": "mkvtnel",
        "score": 32,
        "body": "I hate that whenever I complain about trump fucking over federal workers people respond with \"well you shouldn'tve voted for him then\" MOST OF US DIDNT??? I DIDNT??? Like who the fuck at the EPA would vote for that monster"
      },
      {
        "id": "mkxzy61",
        "score": 32,
        "body": "> Don\u2019t worry they haven\u2019t done it yet!\n\n> It happens.\n\n> Don\u2019t worry they haven\u2019t done the next thing yet!\n\n> It happens\n\nI\u2019ve noticed a pattern too."
      },
      {
        "id": "mkvm87v",
        "score": 30,
        "body": "Ableism kills. Solidarity from Europe!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1jee5og",
    "title": "It finally sunk in",
    "body": "After almost 20 years of believing my family when they said \"you just have to pull yourself up by your bootstraps.\", it's finally sunk in. I was approved for 54 hours a month of in home care, after being approved for government aid. \n\nI'm a whole part time job! No wonder things were so hard. No wonder I could never sustain a job. No wonder I kept feeling worse.\nTurns out, I'm not weak, or \"sensitive\".\n\nAnd someone is being paid to help me live a dignified, human, life. I feel, for the first time in my life, like there is maybe a sliver of room for me in this society. \n\nAnd I'm very grateful for that. ",
    "flair": "Blog",
    "score": 655,
    "comment_count": 31,
    "created_at": "2025-03-18T19:53:49+00:00",
    "top_comments": [
      {
        "id": "mihz124",
        "score": 96,
        "body": "I'm truly happy for you. I know that feeling, and I just kept pushing forward while working a 40-hour week managing a 3 story, 680 storage unit facility. I would come home with hugh brain fog and literally dragging my butt into my apartment. Forget doing anything once I got home. The only energy I had was enough to care and love on my cat. Doctors couldn't figure out why I had so much pain and lethargic as all get out, for 16 years. I had 2 mini strokes last spring (one at work) and haven't been able to work since then. I honestly don't know how I did it though. Family has never understood, I don't look sick, just looked drained out all the time. Applied for disability last November and was finally diagnosed with Fibromyalgia after ruling autoimmune diseases out. I have narcolepsy as well, on top of other things. Still waiting to hear if I get approved for disability, I'm praying. I just wanted to let you know, I see you and hear you. And I am truly happy that you have gotten the help that you need \u2764\ufe0f"
      },
      {
        "id": "mijbbx9",
        "score": 68,
        "body": "Next time someone tells you to pull yourself up by your bootstraps, make direct eye contact with them, raise an eyebrow and say, \"You know, that's literally impossible. That was the whole point of the expression. A person can not pull themselves up by their bootstraps. But if you're willing to show me, I'm willing to change my mind.\"\n\nIn case you couldn't tell, I despise that expression. Boomers have used it to death and they use it wrong."
      },
      {
        "id": "miixrei",
        "score": 36,
        "body": "Congratulations, and welcome back to society. When you're disabled, many times you feel like you have lost your purpose; lost your place as a productive member of society. Anyone with those feelings needs to rage against them and fight to recreate life as necessary without falling victim to losing. \n\nWe all deserve our dignity, not just when we can work or take care of ourselves.\n\nStay strong \ud83d\udcaa Go with Love \u2764\ufe0f"
      },
      {
        "id": "mijr1zo",
        "score": 35,
        "body": "\ud83c\udfc6\ud83c\udfc6\ud83c\udfc6\ud83c\udfc6\ud83c\udfc6\ud83c\udfc6\nExactly. \n\nOP, I'm glad you have validation. That mental feeling of \"is this just in my head? Am I just lazy?\" is terrible. \n\nTo everyone here: please try to remember that your value is NOT based on how you serve capitalism. I know it's hard, but try to remember to not let capitalism bully you. \nYou are valued."
      },
      {
        "id": "miiaa6g",
        "score": 24,
        "body": "That\u2019s great. It\u2019s very validating to have others recognize our humanity and needs"
      },
      {
        "id": "mihyzgp",
        "score": 19,
        "body": "That\u2019s so great! I hope you benefits continue even with all the cuts they are making"
      },
      {
        "id": "miiwpyr",
        "score": 16,
        "body": "Congratulations \ud83e\udd17 can relate. I\u2019m not on disability but struggled all my life, similar problems. Undiagnosed autism in my case is part of it."
      },
      {
        "id": "miimt60",
        "score": 14,
        "body": "In the USA? They cut office staff which if nothing else will make getting benefits and care take longer.\u00a0"
      },
      {
        "id": "mika05g",
        "score": 9,
        "body": "Love that!"
      },
      {
        "id": "mijrb3y",
        "score": 8,
        "body": "I hadn't thought of it that way. My situation is different (I work full-time, and I have informal, unpaid supports) but it is a part time job to keep my health stable enough to manage life."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1lzzce8",
    "title": "Thought y\u2019all would like this",
    "body": "I find this so hard to explain to people! I have chronic back pain and walking is usually fine for me as long as I don\u2019t push myself a bunch. But I can barely stand in place without pain. Doing dishes is unbearable \ud83d\udc80",
    "flair": "Image",
    "score": 649,
    "comment_count": 45,
    "created_at": "2025-07-14T21:36:16+00:00",
    "top_comments": [
      {
        "id": "n35jban",
        "score": 106,
        "body": "I\u2019ve been working a retail job for a year now and everyone there thinks I\u2019m the hardest worker because I\u2019m always on the move. Really though, I\u2019m just trying to avoid the pain that comes with standing still"
      },
      {
        "id": "n35n545",
        "score": 50,
        "body": "It's not even just bones, it's the muscles, tendons, ligaments etc. Demons are awful."
      },
      {
        "id": "n36aqgj",
        "score": 26,
        "body": "This happens to me when I go to a doctor's office that is full and a bunch of the people don't have an appointment they are just... there with people. So I try and tough it out and stand. I don't look disabled I just look like a average 28 year old dude and now I feel embarrassed to say anything cause I don't look like anything is wrong with me. This is a struggle I've dealt with more than once."
      },
      {
        "id": "n36kqal",
        "score": 25,
        "body": "Human legs are designed for constant motion. Our bodies actually struggle getting blood to the leg muscles if we aren\u2019t walking or jogging in some way"
      },
      {
        "id": "n36c881",
        "score": 19,
        "body": "If you can, I highly recommend getting a collapsible stool! There are a bunch that are designed for camping/hiking that are small and lightweight. They\u2019re not comfortable enough for lounging in or anything but they\u2019re an absolute lifesaver for when you need a seat somewhere you might not get one."
      },
      {
        "id": "n35mdmi",
        "score": 14,
        "body": "Exactly. I have stage 4 OA and staying still is ultimately horrible when I have to walk again."
      },
      {
        "id": "n36bpys",
        "score": 11,
        "body": "Yes, I wish people understood this. I get dizzy and nauseous along with excruciating pain when I'm forced to stand upright for too long, but then people throw out there that I can run up the steps. It's not the same thing!!!"
      },
      {
        "id": "n3845np",
        "score": 11,
        "body": "this is why my rollator makes me feel invincible! I feel like I'm driving a monster truck with that thing, totally unstoppable. And if I have to stop, I have a place to sit."
      },
      {
        "id": "n35teml",
        "score": 11,
        "body": "By the time I became an hourly manager, closing was awful. Sitting down to count the safe was an additional two hours of extra pay because I couldn't walk after that. My day was done if I had to sit down at a computer midshift."
      },
      {
        "id": "n37f2n4",
        "score": 11,
        "body": "Meeee orthostatic intolerance imma pass out if I stand still but can walk okay. Museums are the death of me even though I love them"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1lkxgg9",
    "title": "Some environmentalists seem to forget disabled people exist.",
    "body": "I was watching a video of someone showing the right side of the road, which was full of bushes, trees, and tall grass. And then they showed the other side of the road which had pavements/sidewalks, and houses. They said that the other side should look like the right side, but people on a wheelchair like me would find it very difficult to navigate something like that, and it's so sad that people still somehow forget we exist. Someone even said we should turn pavements into dirt, but this would also make it difficult to navigate in a wheelchair. Don't get me wrong, I don't hate environmentalism, but like when it comes to ruining the lives of disabled people, that's when it crosses a line.",
    "flair": "Concern",
    "score": 644,
    "comment_count": 84,
    "created_at": "2025-06-26T11:13:31+00:00",
    "top_comments": [
      {
        "id": "mzv5e6j",
        "score": 500,
        "body": "Environmentalists should embrace sidewalks, as it would make it easier for people to be automobile-free"
      },
      {
        "id": "mzw5k1h",
        "score": 140,
        "body": "Everyone forgets disabled people exist. And a lot of them, when you remind them, react with disgust and hostility. And most people don\u2019t care"
      },
      {
        "id": "mzx69mz",
        "score": 117,
        "body": "This exactly. They should be aiming that stink eye at the roads, not the sidewalks."
      },
      {
        "id": "mzv4qu8",
        "score": 78,
        "body": "Have you ever seen the anime move, \u201cPrincess Mononoke\u201d? It\u2019s a very deep film about environmentalism vs. humanity.\n\nI wouldn\u2019t worry too much about an environmentalist tearing up the developed landscaping. But you should confront them and explain the effects of his/her ideas. Can you comment on the video you\u2019ve seen? Cross-post the video to other social media platforms and add your perspective? Too often social media creates echo chambers and your understanding can be isolated."
      },
      {
        "id": "mzyo6r8",
        "score": 60,
        "body": "Came here to post \"What sort of environmentalist wouldn't want sidewalks and bicycle lanes?\""
      },
      {
        "id": "mzvw4gr",
        "score": 58,
        "body": "a loved one once went to an event with some environmentalists and got shouted at for having a disposable coffee cup in her hand. she didnt have a reusable coffee cup because her mobility issues & chronic pain meant she couldn\u2019t carry one on top of her reusable water bottle and laptop. environmentalists love to claim inclusion and intersectionality until a disabled person needs a lighter water bottle and gets one that\u2019s single use or cant use a metal straw so they use a plastic or paper one or relies on safe foods that aren\u2019t locally farmed and vegan. \n\nthere is no planet B and the earth is burning but we need to put the blame on corporations not marginalised people."
      },
      {
        "id": "mzvaqeq",
        "score": 57,
        "body": "This. I think abled people honestly forget that other people exist, with no malice intended. It\u2019s human nature, if not the nature of most living things, to focus on the survival of *things like me*.\n\nIt honestly takes a lot of effort to consciously account for the needs of others. But OP, I totally empathize with your frustration. Seeing any absolutist view that totally erases your existence is horrifying, especially when it\u2019s something we may likely support in theory."
      },
      {
        "id": "mzw6zu8",
        "score": 56,
        "body": "It\u2019s not just environmentalists. Unless it\u2019s a disability specific organization., our position regarding the issue is never independently asked  and our concerns become pushed to the very back to remain unspoken."
      },
      {
        "id": "mzvagge",
        "score": 51,
        "body": "Something something plastic straws and disposable cutlery \n\nEnvironmentalists often just want a target"
      },
      {
        "id": "mzw5ruk",
        "score": 41,
        "body": "All too often they just react with hostility and double down on the ableism when you call it out. Most people just are straight ok with ableism"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1qkie2g",
    "title": "ER doctor accussed me of faking and purposefully left me in the waiting room as punishment for physically not being able to talk",
    "body": "It was bound to happen one day but I had to go to the ER bc in the past week I suddenly developed seizure like episodes that have rapidly gotten worse. I saw a new neuro yesterday who was fantastic and put in like a hundred referrals and tests to help figure out why. He told me if I had back to back episodes or wasn't breathing go back to the ER. I had back to back episodes today that my friend witnessed and helped me through. It took over 30 minutes for me to become responsive again so they took me to the ER at the hospital I get literally all my care.\n\nI started to feel sick in the waiting room and when the nurse did my vitals my hr and BP were high but my ox was a bit low. A few minutes after, the doctor comes and wheels me into the consult room. Immediately he jumped down my throat and said \"you've been here multiple times this past week, at this point you're just wasting our time and resources. You have referrals and you're labs are fine so why are you here?\". In these episodes I struggle to speak and couldn't get words out no matter how hard I tried. He said \"you can cut the crap you're not having a stroke you can talk so talk\". I kept trying and would get maybe a couple of syllables out before he would go at me again with the \"youre faking\" comments. I managed out \"I had convulsions\" trying to explain that I was having back to back episodes but he yet again jumped at me and was like \"yea I know and you've been seen by us for them so how about you stop wasting everyones time and tell me why you're REALLY here?\". I couldn't speak not only from feeling ill but just being in shock. He then said \"you can either talk to me right now or I can put you back out in the waiting room and you can wait all night to waste a room\". Surprisingly, shocker, I still couldn't speak so he said \"I gave you your chance\" and wheeled me back into the waiting room. It took an hour before I could sit up or speak. He put in my notes that I refused to talk to him and that I was forcing it to sound like I was struggling to talk.\n\nShift changed happened and I got two new doctors who immediately brought me into a room and immediately started putting in for meds, tests, etc. And giving me things/advice for my friends who I live with to help me. Turns out you can't fake your heart rate being in the 150s while literally just sitting or head injuries from convulsions.\n\nI've had doctors tell me my problems are mental (especially since I have a thorough history of psych issues) and claim I'm just anxious or tell me im being overdramatic but never have I come across quite that level of audacity. \u200b\n\n  \nedit: thank you all for the support and advice \ud83d\udc99. I'm so sorry a lot you understand how much this sucks and how dehumanizing it is. ended up at a different hospital unexpectedly due to the snow storm and had a MUCH better experience. I reported him both to patient relations and the state board of medicine and I plan on contacting his boss Monday and requesting a conversation with him because I am actually also a medical professional (public health) and would LOVE to see him argue with me when I am able to speak. ",
    "flair": "Country-USA",
    "score": 636,
    "comment_count": 97,
    "created_at": "2026-01-23T05:32:42+00:00",
    "top_comments": [
      {
        "id": "o16ul2a",
        "score": 386,
        "body": "The first ER doc really crossed the line and should not be doing that. I am SO sorry you had to deal with a sick like him. \u201cI gave you your chance\u201d\u2026like who the f does he think he is? \n\nHave you filed a request for correction in your file pertaining to the notes from the first ER doc on that visit? If ER doc disagrees, then file a statement of disagreement and they will place it in your file so they have your version of the story to protect you from future doctors drawing judgements on what the ER doc dismissed from you. \n\nI hope there is some way for you - like a complaint to patient relations or the ombudsman. Because clearly this was not right?\n\nAside from all this, I\u2019m grateful to hear that your neurologist has put in tests for you. May those tests provide answers or point to the right direction for both you and your care team."
      },
      {
        "id": "o16w7al",
        "score": 300,
        "body": "Please report that doctor to both the hospital and your regional governing body or bodies. If they've done it to you, they've done it to others and will do it again! It's only a matter of time until somebody faces dire consequences for such reckless and unacceptable behaviour,"
      },
      {
        "id": "o16v66c",
        "score": 206,
        "body": "can you report him by any chance? that is actually abhorrent, i'm so sorry you went through that"
      },
      {
        "id": "o16yuf5",
        "score": 111,
        "body": "Exactly what I came here to say. If he said this to you it's  2000% likely he has done it  before and will do again in the future. Just my 2c. Good luck and take care of yourself.edited for clarity"
      },
      {
        "id": "o17ex8o",
        "score": 93,
        "body": "She can. And more people should. \n\nWe sign hundreds of papers waiving them from any harm done to us, even sometimes waiving negligence chalking it up to \u201c human error \u201cbut guess what isn\u2019t one of them? \nAbuse. \nVerbal, psychological (which was what he was playing at here) and physical abuse give you every right to hold a physician accountable for their behavior\u2026 and I feel this is the only way to finally put a stop to the mental gymnastics they play with patients. \nWe need to take self advocating further and start advocating for the community by advocating for ourselves. \nIf you hit them where it hurts ( their pockets and their pride ) they will correct themselves for the sake of it."
      },
      {
        "id": "o16ywg6",
        "score": 81,
        "body": ">It must say malingerer on my chart\n\nI suspect my notes say something like that too. They won't even let me see them, despite repeatedly requesting access.\n\nI visited my GP for a persistent cough and shortness of breath about a month ago. Before I even sat down the guy asked if this was \"about the anxiety\".  I haven't seen a doctor about anxiety in years, only physical stuff. He then claimed my fast pulse, high temp and high BP were \"clearly anxiety\" and that my cough \"wasn't a real cough\" (??) He even cancelled my repeat prescription for my inhaler which I've used for years to deal with allergic asthma. \n\nAnyway, after returning home the cough got worse so a couple days later I went back and saw a nurse who chastised me for \"not explaining how serious it was to the doctor\" and told me I had a respiratory infection. Despite me having sat there and explained to the prev GP over and over just how bad it was and how much it was affecting me and him dismissing everything I said, I was the one who got blamed, not him. \n\nI ended up with antibiotics which did help, thankfully. Then on the way home I nearly got run over by some \\*\\*\\*hole because I was \"crossing the road too slowly\"; guy kept beeping his horn and screaming that I was a faker and a drain on society because I was using a walking stick."
      },
      {
        "id": "o16yonp",
        "score": 79,
        "body": "Holy shit report that doctor and get a correction on your file. I'm so sorry that you had to go through that."
      },
      {
        "id": "o17gl67",
        "score": 75,
        "body": "And your insurance too. They don't like doctors abusing patients. I would refuse to pay his bill"
      },
      {
        "id": "o16v862",
        "score": 72,
        "body": "All my doctors have told me that. It must say malingerer on my chart because the last time and the LAST TIME I went to the ER I waited 14 hours in a hallway. Now I won\u2019t go unless I need a leg sewed back on. I had a nice ER doc that said it wasn\u2019t his job to figure out what was wrong with me but to keep pushing my doctors for more testing. Even if it\u2019s \u201cJust anxiety\u201d as my last GP yelled in my face, there are still real physical symptoms that need to be treated."
      },
      {
        "id": "o17cqij",
        "score": 51,
        "body": "this. Someone like that should have no right to be a doctor."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1kwyqgo",
    "title": "\u2b50\ufe0f\ud83d\udc95\ud83e\ude75My new Joystick! I matched it to my sleeve!\ud83e\ude75\ud83d\udc95\u2b50\ufe0f",
    "body": "",
    "flair": null,
    "score": 626,
    "comment_count": 32,
    "created_at": "2025-05-27T21:01:34+00:00",
    "top_comments": [
      {
        "id": "mulmnqi",
        "score": 17,
        "body": "This is sooo cute, I've never seen decorative joysticks before ! (edit: typo)"
      },
      {
        "id": "mum0pzs",
        "score": 14,
        "body": "Swanky! It never occurred to me that a joystick could be customized in such a way. Love it!!\n\nNice tattoos also!"
      },
      {
        "id": "mulifaf",
        "score": 10,
        "body": "Slay omg \ud83d\ude2d\ud83d\udc98\ud83e\udd2d\u2728\ufe0f\ud83e\udd29"
      },
      {
        "id": "mulz822",
        "score": 10,
        "body": "Fold & Go. it\u2019s super compact and it\u2019s not super medical looking which i love. has great battery life. it\u2019s light. I can\u2019t recommend it enough. i did however buy it out of pocket :/ it can be fussy using insurance for it."
      },
      {
        "id": "mulw6ie",
        "score": 5,
        "body": "What chair is this? How do you like it? Would you purchase it again?"
      },
      {
        "id": "mulz6wl",
        "score": 3,
        "body": "![gif](giphy|Ztj7cAToJPTZ5StTZY)"
      },
      {
        "id": "mumzihs",
        "score": 3,
        "body": "That's so fucking cool"
      },
      {
        "id": "mv4cnjq",
        "score": 3,
        "body": "OMG THIS IS SO COOOLL. where do you get it?"
      },
      {
        "id": "mv4hsxs",
        "score": 3,
        "body": "[Phil Grant on Etsy!](https://www.etsy.com/shop/GrantedEngineering)"
      },
      {
        "id": "munu2vc",
        "score": 3,
        "body": "it\u2019s not :/ i have to buffer these leaves to be rounded a bit. right now i just place the curve of my hand beneath the design entirely which doesn\u2019t bother me at all but it does need some sanding."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1ozbou3",
    "title": "A small but meaningful moment for my dad today",
    "body": "Today my dad was able to control his wheelchair on his own and move around the store to pick up what he wanted.  \n\nIt may seem simple, but watching him choose things independently again felt like such a big step for us.  \n\nWe were both really happy about it.  \n\nLittle moments like this remind me how important independence is, even in everyday errands.\ud83e\udd17",
    "flair": null,
    "score": 632,
    "comment_count": 37,
    "created_at": "2025-11-17T09:14:02+00:00",
    "top_comments": [
      {
        "id": "npah5m1",
        "score": 49,
        "body": "This is wonderful. I remember this moment for myself and it is surprisingly exciting to be able to choose things for oneself."
      },
      {
        "id": "npajylr",
        "score": 23,
        "body": "It only seems simply HUGE. That\u2019s awesome and I\u2019d be happy too!!!!"
      },
      {
        "id": "npc8mvm",
        "score": 12,
        "body": "I remember the first visit to the shop in my chair and picking up stuff. It was great to have that independence again!"
      },
      {
        "id": "npas2hr",
        "score": 7,
        "body": "Fight for every tiny thing."
      },
      {
        "id": "npbwblq",
        "score": 7,
        "body": "This is super awesome <3"
      },
      {
        "id": "npcnz9y",
        "score": 7,
        "body": "Stuff like this is so important"
      },
      {
        "id": "npao34i",
        "score": 6,
        "body": "That\u2019s fucking awesome.  \nPlease tell me they had single-use plastic bags to put his groceries in when it was time to leave.  \nI swear to fucking god paper bags are a crime against humanity."
      },
      {
        "id": "npc6xrl",
        "score": 6,
        "body": "It's EVERYTHING! \u2764\ufe0f"
      },
      {
        "id": "npctkbv",
        "score": 6,
        "body": "Every little moment counts. \u2764\ufe0f"
      },
      {
        "id": "npbr37z",
        "score": 6,
        "body": "I hope you asked his permission to post a photo on here."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1pcpp7b",
    "title": "Finally feeling more confident!",
    "body": "Hi everyone I have diagnosed POTS and G-HSD and currently seeking a ASD diagnosis. \n\nThis is the first time I\u2019ve been able to look in a mirror using my crutches. First I was terrified to be seen in public. Then I was ashamed to look at my own reflection in any passing reflective surface and now this is my first selfie. Feeling more and more confident and feeling less about having to explain myself and my entire medical history to nosy strangers. Took this pic after coming home from a little neighborhood walk. :)",
    "flair": "Image",
    "score": 632,
    "comment_count": 48,
    "created_at": "2025-12-03T00:36:20+00:00",
    "top_comments": [
      {
        "id": "nrzqufl",
        "score": 40,
        "body": "\ud83d\udd25 This pic goes hard \u26a1\ufe0f\n\nConfidence makes a world of difference for me too. \ud83d\ude0a"
      },
      {
        "id": "nrzywz2",
        "score": 24,
        "body": "Sick fit"
      },
      {
        "id": "ns0f6vy",
        "score": 23,
        "body": "i love seeing other disabled punks \ud83d\udda4 \n\nthe first time i went to a show with my cane in 2018 i was so anxious and scared. now i go in my wheelchair and it\u2019s not always easy physically or mentally but im just glad i can still see my favorite bands and not have my body pay the price"
      },
      {
        "id": "ns0j1w2",
        "score": 23,
        "body": "You are handsome as hell big dog. You\u2019ve just got metal weapons you take wherever you go to help you walk and that looks even cooler."
      },
      {
        "id": "nrzinfx",
        "score": 19,
        "body": "You're looking fine my friend"
      },
      {
        "id": "ns0l371",
        "score": 16,
        "body": "you look badass actually"
      },
      {
        "id": "nrzy2fo",
        "score": 13,
        "body": "That\u2019s awesome. You look cool as hell by the way!"
      },
      {
        "id": "nrzrx1l",
        "score": 12,
        "body": "You look badass"
      },
      {
        "id": "ns0arx7",
        "score": 8,
        "body": "Stay warm out there! You look awesome."
      },
      {
        "id": "nrzmn1g",
        "score": 8,
        "body": "There are WAY too many people to worry what they're all thinking! Glad you're getting out and about!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1jb8z8x",
    "title": "\u201cYou have real symptoms. Just because I don\u2019t have answers for you doesn\u2019t mean there\u2019s not something going on.\u201d - My doctor",
    "body": "That was her response when I thanked her for not dismissing me and trying to find answers. \n\nShe\u2019s such a wonderful, affirming doctor. When I think I\u2019m going crazy and everything is in my head, she pulls me out and lets me know that\u2019s a lie. \n\nAs long as I\u2019m willing to fight, so is she. I\u2019m so thankful for her. ",
    "flair": null,
    "score": 623,
    "comment_count": 57,
    "created_at": "2025-03-14T17:09:59+00:00",
    "top_comments": [
      {
        "id": "mhs5u4q",
        "score": 112,
        "body": "This is probably why a lot of doctor dismiss patients, they dont want to admit they don't know whats going on"
      },
      {
        "id": "mhs2etk",
        "score": 38,
        "body": "Thank you for sharing. Some may be bitter reading this if they haven't experienced it.. But it reminds us to seek other doctors when ours do not treat us well. \n\nI hope you get answers soon friend."
      },
      {
        "id": "mhtwkka",
        "score": 31,
        "body": "Yep! This right here. They don\u2019t want to admit they don\u2019t know, to you and sometimes to themselves. God complex, insane ego, narcissism - they all run rampant in the medical field, especially among doctors. \n\nSometimes it\u2019s also a bit of \u201cI don\u2019t want to do the work to find out since I don\u2019t immediately know\u201d - they don\u2019t want to refer you out/order less common testing/etc. and would rather brand you as a hypochondriac or difficult patient and move along. \n\nAlmost lost my shit on a doctor recently who gave me the \u201cyeah I don\u2019t know\u201d as if that was going to end the discussion. \n\u201cWell, who can you send me to that will know? What can we do to figure it out?\u201d and they didn\u2019t want to proceed further.\nNo, I\u2019m not going to just live with unexplained and uncomfortable symptoms and not at least try to get to the bottom of it, what the fuck?"
      },
      {
        "id": "mhs4gpq",
        "score": 30,
        "body": "That\u2019s a fantastic doctor!  So glad you found her!"
      },
      {
        "id": "mhs5ngh",
        "score": 30,
        "body": "I have a Neurological Disorder that used to be considered a psychiatric disorder. \n\nMy neurologist has validated me since the start of my symptoms. That it could be caused by trauma, and also, my symptoms are very real. They compare it to hardware problem vs software problem in the body. \n\nIt took so much getting used to. And the other diagnoses I have, help offset the shame I associate with this disorder. \"It's all in your head\" yup...\n\nThe least validating things has been people telling me that I need to change my psych meds or that this is psychiatric. My psychiatrist and psychologist (who I was seeing for 7 years at the time) both agreed this is more than \"trauma\". \n\nI'm so grateful for a supportive team. \n\nThere are way too many posts about shit providers and I feel so bad for those people"
      },
      {
        "id": "mht1av4",
        "score": 15,
        "body": "back before fibromyalgia was understood enough you could get a reliable diagnosis my doctor used to call me Abby-normal because everything always tested as being normal but she knew it wasn't but didn't know why. having a doctor that understands medicine doesent know everything yet is definitly a godsend"
      },
      {
        "id": "mhs75us",
        "score": 13,
        "body": "What a gem of a doc! I\u2019m really glad you found someone that wants to listen to what you need to discuss. It ain\u2019t easy to find one like her."
      },
      {
        "id": "mhs981x",
        "score": 9,
        "body": "I'm so glad you have such a supportive doctor. It can be such a good feeling to not be dismissed."
      },
      {
        "id": "mhsjzna",
        "score": 9,
        "body": "I have a consultant like this. She has no idea what the issue is but is very determined!\n\n\nMy previous consultant said the same. He then referred me to her because she has a different speciality."
      },
      {
        "id": "mhsnqm5",
        "score": 9,
        "body": "My god\u2026 \nThe relief I would feel by hearing this from a medical professional. \nI feel like crying just imaging it."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1o383uy",
    "title": "Imagine trying to mug me and I hit you with my fairy prinecess cane like it\u2019s a softball bat and then I throw my vial of fairy dust in your eyes to blind you as I gimp away",
    "body": "",
    "flair": "Image",
    "score": 614,
    "comment_count": 67,
    "created_at": "2025-10-10T17:58:23+00:00",
    "top_comments": [
      {
        "id": "nitc0ob",
        "score": 77,
        "body": "This is hot girl shit"
      },
      {
        "id": "nit8wro",
        "score": 54,
        "body": "That would be a totally fair way to treat a mugger haha :)"
      },
      {
        "id": "nit8m7a",
        "score": 49,
        "body": "Yes I am joking about my own disability no I won\u2019t apologize \ud83d\ude05"
      },
      {
        "id": "nitcxy9",
        "score": 42,
        "body": "i feel like we would be great friends based off this post alone lmao"
      },
      {
        "id": "nitnnfc",
        "score": 24,
        "body": "Damn straight."
      },
      {
        "id": "nitvcmd",
        "score": 23,
        "body": "Right?!?! \ud83d\ude06\n\nNot-yet-disabled people would not understand these kinds of vibes lol but I'm so here for it \ud83d\udc83\ud83c\udffb"
      },
      {
        "id": "niu5j5t",
        "score": 22,
        "body": "The best compliment you could\u2019ve given \ud83e\udd79\ud83e\udd72"
      },
      {
        "id": "nitdyr2",
        "score": 21,
        "body": "No matter how hard they are swung, canes like this just can't do any real damage. Fun post and totally chill, Just putting in the quick $0.02 because a lot of people tend to feel quite protected against threats with makeshift self defense weapons that are about as effective as couch pillows in real life.  Now, if that fairy dust is a canister of high potency pepper spray, you might be in business."
      },
      {
        "id": "nitjip4",
        "score": 15,
        "body": "That is cane is adorable AND lethal? My favourite things!"
      },
      {
        "id": "niu4vu9",
        "score": 14,
        "body": "1000 up votes on the original account!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1puu2ux",
    "title": "Painted myself a froggy eye patch",
    "body": "",
    "flair": "Image",
    "score": 610,
    "comment_count": 19,
    "created_at": "2025-12-24T18:33:18+00:00",
    "top_comments": [
      {
        "id": "nvt0l0r",
        "score": 18,
        "body": "Cute, but we can go deeper. Give him an eye-patch of your face, wearing a frog patch...patch-ception!\n\n\ud83d\ude09 Nice work! I don't have the motor control for painting...but I can draw, mediocrely.\n\n(Oh btw, you look pretty /p. Not trying to be weird or like hit you up, just honest. Merry Christmas too, as long as you're here! \ud83d\ude0a)"
      },
      {
        "id": "nvrvz6p",
        "score": 12,
        "body": "Cute idea\n\nAre u a full time patch user? And have you tried ones with straps they just tend to irritate my face \u2026 \n\nI\u2019m only a part timer"
      },
      {
        "id": "nvvcp3e",
        "score": 8,
        "body": "I love your sweater, necklace, patch, and earrings! They form a cohesive design."
      },
      {
        "id": "nvrgvg7",
        "score": 5,
        "body": "This is awesome and your style is so cute!"
      },
      {
        "id": "nvtgmzb",
        "score": 4,
        "body": "Your style is super cool and it matches the vibrant colors really well! Also those earrings are great"
      },
      {
        "id": "nvsbhbx",
        "score": 3,
        "body": "Fun! I was wearing a patch for a bit due to an injury and I wish I\u2019d had a cute one like this. My elementary students would have loved it"
      },
      {
        "id": "nvxp55q",
        "score": 3,
        "body": "That's adorable and so well-done!"
      },
      {
        "id": "nvrb6ue",
        "score": 2,
        "body": "Love it!"
      },
      {
        "id": "nvvjbwn",
        "score": 2,
        "body": "This is a lovely idea! so cute."
      },
      {
        "id": "nw03e9k",
        "score": 2,
        "body": "I wish I'd seen people with cool eye patches like yours when i was a kid. Silly question - do you paint it flat & then stick it on - or put it on your face, then paint it like make up? I had a nightmare making my patch lie flat."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1oenyl9",
    "title": "The Food Stamps Cut Has Made Ableism Run Rampant",
    "body": "The food stamps cuts have made ableism so rampant over the past week. This really made everyone show their true colors for how they feel about disabled people. \n \n I've noticed that we are almost entirely left out of the conversation, as if we don't exist. But when we are mentioned, its only to dehumanize us. People will say \"stop complaining about SNAP, everyone who gets SNAP has a job so they should be allowed to get it\" as if to say that children and disabled people who are unable to work are undeserving of the assistance. \n  \nAnyone who admits they're disabled and have food stamps is immediately attacked and harassed by tons of people calling them a liar, dehumanizing them.  \n \nJust wait til abled people find out about disabled people who have to eat a strict diet for their health condition and can't just eat anything from the food banks or random donations, then hell will really break loose. Ableists truly do not understand how privileged they are and believe our suffering and survival is a threat to them. ",
    "flair": null,
    "score": 604,
    "comment_count": 144,
    "created_at": "2025-10-24T03:59:40+00:00",
    "top_comments": [
      {
        "id": "nl39eyv",
        "score": 134,
        "body": "Oh man I relate to not being able to eat from food banks. I have to have a special diet....and it's expensive and restrictive and there's nothing I can do about it. Not a day goes by that I don't wish I could just eat normal food. But yeah, people just wanna pretend we don't exist or worse that we should just suffer and die."
      },
      {
        "id": "nl4ujr8",
        "score": 120,
        "body": "People just have no idea how easily one can become disabled.  One serious illness, injury, or accident, etc.  \n\nWhen things are going good, we all take our life for granted - it's only when the shoe is on the other foot that we get an accurate perspective."
      },
      {
        "id": "nl34eps",
        "score": 88,
        "body": "yeah, the defense for these entitlement programs always seems to be about how the people using them work, actually. As though you don\u2019t deserve food or healthcare if you can\u2019t."
      },
      {
        "id": "nl3wrtc",
        "score": 77,
        "body": "I keep seeing people say that food banks are better because everyone gets healthy food because they\u2019ll just buy junk on benefits \ud83e\udd26\u200d\u2640\ufe0f it\u2019s like bruh they are adults trust them to buy their own food. Nobody polices rich people\u2019s eating habits. It\u2019s like if you have a disability you must be stupid or abusing the system.\u00a0\n\nI saw a sad stat about how often food banks and stuff can\u2019t accomadate dietary needs for special requirements and this who situation is so frustrating.\u00a0"
      },
      {
        "id": "nl3wzxa",
        "score": 69,
        "body": "Yeah seems pretty insane to let someone die because they don\u2019t have a job. We\u2019re not allowed to kill people normally, why can billionaires kill people in this way?\u00a0\n\nIt\u2019s so weird how people are okay with others starving and dying"
      },
      {
        "id": "nl4vvuv",
        "score": 60,
        "body": "same! they aren\u2019t set up for those of who need to eat in a certain way. \n\nI\u2019ve even got trauma from an experience at a grocery store style food bank - the woman followed me around and kept offering this or that and I would say \u201coh I can\u2019t eat that, but thank you\u201d. \n\nThe last straw was when I turned down a package of hotdogs and she snapped and said \u201cbeggars can\u2019t be choosers\u201d. I said \u201cit\u2019s just way too much sodium and I don\u2019t need my blood pressure to go haywire\u201d. \n\nShe came back with the old \u201cyou\u2019re too young to have high blood pressure and slipped a package in my cart\u201d. I decided not to fight about it, but I have those hotdogs to another person in the parking lot and never went back.\n\nFor the record, just in case anyone doesn\u2019t know, if you have an anxiety disorder and/or get panic attacks, chances are you will suffer from high blood pressure decades before normies. It hit me in my 30s."
      },
      {
        "id": "nl5tour",
        "score": 56,
        "body": "Yeah, this is why I don\u2019t understand why disability rights lags so far behind civil rights wide. I would expect people to have more empathy because it could one day effect them but nope seems to be actually way way less empathy and more blaming.\u00a0"
      },
      {
        "id": "nl4d8c1",
        "score": 45,
        "body": "Apparently, even disabled people are attacking other disabled people. It's not just the \"able-bodied\". I have about stopped using Facebook because the few disabled friends I have have taken to attacking me because I receive SNAP benefits and SSI. This one lady who said she was housebound due to severe disability and has one of them disabled flags as her profile picture was really nasty with me, even going so far as to say I'm a sinner and my disability is proof of my sin (so, by her logic, wouldn't she be a sinner too?). Family has also turned on me and has also turned into thinking they are doctors, in telling me they \"have observed me\" and don't think I'm disabled at all.\n\nI am getting really scared of the future. It's like everyone woke up in 2025 with a massive attitude problem."
      },
      {
        "id": "nl4ve8u",
        "score": 44,
        "body": "Wealth hoarding isn\u2019t yet treated as symptomatic of mental illness, but I believe it should be. It\u2019s literally delusional to think one could need (or even have a use for) that much excess, and it keeps resources from reaching others. \n\nIf these people aren\u2019t mentally ill, they should be so socially ostracized that they never have even the opportunity to amass wealth. How antisocial must you be to believe you have the RIGHT to hoard excess while people suffer. Like, kindly gtfo of society if you don\u2019t want to be a responsible part of it, because at that point it\u2019s literally not for you. \n\nAhhhhh so much screeching into void these days"
      },
      {
        "id": "nl5scjy",
        "score": 33,
        "body": ">  food banks are better because everyone gets healthy food because they\u2019ll just buy junk on benefits\n\nThen you have people with medical dietary restrictions, like Celiac. Food Banks do not often have gluten-free food."
      }
    ]
  }
]
```
