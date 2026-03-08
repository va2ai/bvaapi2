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
    "subreddit": "Veterans",
    "id": "1nzs1w7",
    "title": "To think if I\u2019d killed myself\u2026",
    "body": "Today is my 32nd birthday, and as I walked the beach at the campsite I brought my 3yr old on today and looked out at the beautiful scenery before me i thought \u201cto think if I\u2019d kill myself a few years ago when the darkness was so heavy I\u2019d missed this.\u201d \n\nFor those struggling, *I don\u2019t know if it gets better, but you should stick around to find out* helped me and it did indeed get better. Hope everyone stays in the fight to experience days like this. ",
    "flair": "Discussion",
    "score": 911,
    "comment_count": 112,
    "created_at": "2025-10-06T19:03:15+00:00",
    "top_comments": [
      {
        "id": "ni5jp1d",
        "score": 73,
        "body": "I\u2019m a widow who lost her spouse to ptsd 2 years ago and this is our son, I wanna show him there\u2019s another path to take even if life gets hard. Wish his dad was here to see him like this. But thank you everyone. It\u2019s been a good trip so far, we\u2019ve got some more spots along the way! Headed to Washington and Montana next!"
      },
      {
        "id": "ni49gjl",
        "score": 62,
        "body": "Great picture. Enjoy the moments and I hope that things continue to look positive for you."
      },
      {
        "id": "ni4a1vf",
        "score": 29,
        "body": "Great post! In my darkest days, thoughts of my 3 kids pulled me through."
      },
      {
        "id": "ni5zzdi",
        "score": 15,
        "body": "Your son needs you more than ever before! Keep fighting, and continue to show your son what amazing things that living on this earth has to offer!"
      },
      {
        "id": "ni4apy1",
        "score": 14,
        "body": "I mean at the very least if you live long enough you get to piss on the graves of the people who didn\u2019t like you. That right there is worth holding on for, having a little one is worth fighting the good fight til your last breath."
      },
      {
        "id": "ni4a986",
        "score": 13,
        "body": "We need you here. Never forget that. You are always needed even when its darkest. I am glad you are doing better"
      },
      {
        "id": "ni4dnrw",
        "score": 10,
        "body": "My birthday was yesterday, was almost in the mood to fully commit. Then my momma called me. \n\nYour family is beautiful. God bless you all, and happy birthday"
      },
      {
        "id": "ni4eqwy",
        "score": 6,
        "body": "I needed this. Thank you. This shit always gets me so emotional, this world is so dark, but as long as we have hope, we'll be alright..."
      },
      {
        "id": "ni4arxd",
        "score": 6,
        "body": "Dude hell yeah man \u2764\ufe0f"
      },
      {
        "id": "ni66hs1",
        "score": 6,
        "body": "Almost lost a fellow vet to the terminator this week. He survived the attempt/attack and is currently in ICU. Prayers for M please. Good good man. Devoted dad with a loving wife. Two sweet young daughters 3-5. Nobody can ever explain the demons or when/where they\u2019ll attack. So glad you survived to see and love those beauties in the pic! \ud83d\udc4a\ud83c\udffb"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1m0ys1h",
    "title": "I see a lot of veterans  questioning if they can really go back to school and succeed after so much time away\u2026",
    "body": "I\u2019m 49 and have ADD as well as the standard mental health package gifted to us by our time in the service. I just graduated magna cum laude and am headed on to my Masters and PhD program. You can do it, too, and it feels REALLY good. ",
    "flair": "VR&E - Voc Rehab Veteran Readiness",
    "score": 901,
    "comment_count": 165,
    "created_at": "2025-07-16T00:39:14+00:00",
    "top_comments": [
      {
        "id": "n3damdy",
        "score": 159,
        "body": "Ma\u2019am? \u2026Something something work for a living\u2026"
      },
      {
        "id": "n3d7n9z",
        "score": 97,
        "body": "Congratulations ma'am."
      },
      {
        "id": "n3dbz33",
        "score": 49,
        "body": "if you're 49 then I'm bruno mars"
      },
      {
        "id": "n3ddryo",
        "score": 48,
        "body": "Well\u2026 it\u2019ll be Dr. ma\u2019am then. \ud83e\udd23"
      },
      {
        "id": "n3dd2h2",
        "score": 36,
        "body": "[removed]"
      },
      {
        "id": "n3dd44s",
        "score": 34,
        "body": "Sheeit gettin your Phd get used to getting ma\u2019amed ma\u2019am..congrats I too thought this was a spam post..and yes veterans go back to school..I barely graduated HS was an awful student and after leaving active duty with the GI bill and part time work got a BS..literally if I can do it anyone can do it"
      },
      {
        "id": "n3ddzra",
        "score": 32,
        "body": "So you\u2019d catch a grenade for me? That\u2019s so sweet!"
      },
      {
        "id": "n3dabdl",
        "score": 29,
        "body": "VRE! The career I wanted (mental health therapist) is only available with a masters degree or higher. I may attempt to get into a PhD candidate program without VRE, but as a paid researcher working with some of the leaders in alternative mental health therapies that they\u2019re working on at places like Stanford and Johns Hopkins (IYKYK). But VRE is paying for everything through the masters degree."
      },
      {
        "id": "n3d8eft",
        "score": 26,
        "body": "Congratulations! Stories like these are important to share in the community. Can you share how you funded your journey, GI Bill, VR&E? If VR&E, how you approached/ handled justification for advanced degrees? Thank you!"
      },
      {
        "id": "n3dykta",
        "score": 21,
        "body": "RIP to your DMs \ud83e\udd23"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1ktvrtr",
    "title": "Joined an elite club today.",
    "body": "Doc said I was operating on 1.8% restful sleep. High BP and a good friend finally got me to stop messing around and go get checked out. I lift, run, and eat right. I got lots of stress at work, but nothing I can do about that except KOKO for the next 1,043 days. Docs said that my not sleeping was making my BP high which was making my sleep worse which was making my BP worse and so on. \n\nReally looking forward to seeing what the world looks like on more than 1.8% battery. ",
    "flair": "Health Care",
    "score": 900,
    "comment_count": 211,
    "created_at": "2025-05-23T21:58:05+00:00",
    "top_comments": [
      {
        "id": "mtwxwoa",
        "score": 118,
        "body": "I got a severe rating several years ago. I feel way better using the machine, but I'd sure like to NOT need it. I'm not even obese LOL."
      },
      {
        "id": "mtwy2ii",
        "score": 43,
        "body": "Welcome. I joined the club 2 days ago. I feel amazing in the morning now."
      },
      {
        "id": "mtwx9qz",
        "score": 31,
        "body": "Welcome to the CPAP Top Gun Family."
      },
      {
        "id": "mtx13u5",
        "score": 24,
        "body": "I went through 4 maybe 5 masks before I found one I could tolerate.\n\nHoly smokes!!\n\nIt took months to get acclimated, but it is night and day different.\n\nI had no REM sleep and over 30 apnea periods per hour. I never even realized how crappy my sleep was. Now I'm almost up to 6 solid hours of sleep. \n\nI also found a short piece of very lightweight hose between the mask and regular hose that helps a bunch. The VA provided it, and I do not know the part number."
      },
      {
        "id": "mtwzjqx",
        "score": 24,
        "body": "Same here bro"
      },
      {
        "id": "mtx9dtq",
        "score": 21,
        "body": "Don't get discouraged if it doesn't feel the best right away.  It took me a bit to find the right mask and get used to how I liked it set.   Keep at it and you'll get there then you'll feel like a different person when you use it vs when you don't"
      },
      {
        "id": "mtxc3rb",
        "score": 19,
        "body": "Same here. I have central SA. Caused by my my meds & low Testosteron. (Which you should have checked - SA will definitely lower T.) try ice cold water in the reservoir & wearing it while awake in bed to get used to it. I have tried all the masks there's 1 that has foam around the nose & it makes a great seal. I have a beard so I use the nose only one."
      },
      {
        "id": "mtwxpoz",
        "score": 17,
        "body": "Hope it works for you! I feel like I get even less sleep with the stupid thing than I did without it."
      },
      {
        "id": "mtxadps",
        "score": 15,
        "body": "I've been using a CPAP and now a Bi-PAP machine for about 20 years now. Of course I can do that since I'm just now turning 75, but when I was diagnosed 2003 my wife jumped for joy since now she could get some sleep? I started using my CPAP every night from that point on and have adjusted to it. I didn't fight it like some guys do. Mine was both due to overeating and stress at work. While I'm a Vietnam Veteran, I can't actually tie my CPAP use back to my service days. I never went to the medics in my time in the military and I mostly slept in a tent with other snoring guys so no complaints there.\n\nMy advise is again, not to fight it. Make sure you get the setting set right, there shouldn't be too much air blowing up you nose nor should there be too little. You will get used to it. I also wore just a nasal mask for a while, but couldn't keep my mouth shut all night, so now I wear a full-face mask and again, I'm used to it. I've lost a lot of weight since I started using my CPAP, I'm also retired so all the stress I had has gone away, but I still sleep with my mask. I probably could do without it, but I'm used to it so I won't fight it. \n\nOne of the things I notice about most people that say they can't stand wearing the mask at night is their attitude to begin with. My doctor told me upfront that I didn't have to wear the CPAP mask but he said I would probably die pretty soon otherwise and to get my insurance coverage up-to-date for my wife. I had also scared my wife to death a few times when she woke up and noticed I wasn't breathing! So, I just accepted it as part of my life. Once I did, I started getting a reasonable night's sleep and my health is much better now than it was.\n\nSo, good luck on you journey. You need this or your doctor wouldn't prescribe it for you, so suck it up and wear it so you can live with you family a lot longer. Just my humble opinion.  And if you don't have a problem wearing you mask, just ignore everything I said!\n\nOut here!"
      },
      {
        "id": "mtwysx4",
        "score": 15,
        "body": "I hope that\u2019s me tomorrow and Sunday."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1pp2svb",
    "title": "Dating as a rated veteran sucks",
    "body": "Went out on a date last night after 2.5 years of not dating and it reminded me why. I met him at the gym, spoke a few times he asked me out to go dancing last night, which was fun but afterwards we got coffee and went to walk to see the lights and I made a comment about having been overseas nearly 6 months last year with my son and spent Christmas in Iceland, which led to him asking me what I did for a living and I panicked and just said I worked from home which he paused walking and looked at me and said \u201cyou do onlyfans?\u201d And I was like \u201cwhere would you get that from!?\u201d He\u2019s like \u201clook at you, what else does it mean? Insurance? HA.\u201d I got all red and embarrassed and said \u201cno I don\u2019t work I live off my Va disability and my late spouses and take care of our son.\u201d And he started to lecture me on not being honest and how does one just not work etc etc and how lucky it must be to just exist and travel without financial stress\u2026I think the worst part of the date was when he asked how my husband died and I made a joke about how I guess not doing the dishes right away can make a guy snap I guess. He didn\u2019t find it remotely funny but I think it\u2019s because he\u2019s a banker and lacks that dark humor bone. Someone here said something about making an app for us DVs to date lol where is it? Can I download it? Sigh. Any other shitty first dates you guys wanna share? ",
    "flair": "Discussion",
    "score": 817,
    "comment_count": 631,
    "created_at": "2025-12-17T17:40:06+00:00",
    "top_comments": [
      {
        "id": "nuk0qp1",
        "score": 1066,
        "body": "[removed]"
      },
      {
        "id": "nukcr2k",
        "score": 598,
        "body": "She shouldn\u2019t have even gotten to the point where she explained her income. The second he immediately assumed onlyfans should\u2019ve been the second the date was over"
      },
      {
        "id": "nujtnb7",
        "score": 490,
        "body": "Im 100% as well, Told a girl I was retired. I did 14 years oilfield, and live off savings and VA. \n\nShe told me she doesn't date people on welfare and asked if I wanted her to pay for date \"So I can save money\" \n\nKeep in mind she is a cashier at the Gas station i frequent often, and lives with her parents\n\nI own my own house....like wtf people"
      },
      {
        "id": "nuk8603",
        "score": 165,
        "body": "Ugh, no. Have you met us veterans? We're the worst."
      },
      {
        "id": "nuk8nri",
        "score": 117,
        "body": "I never tell people about my VA benefits. Not my friends, coworkers, family, nobody. If I was in your shoes and needed to explain my income I would just say I have some passive income from investments."
      },
      {
        "id": "nuk3rcc",
        "score": 110,
        "body": "That got me reeling lmao."
      },
      {
        "id": "nuk2axf",
        "score": 105,
        "body": "Fuck that chode."
      },
      {
        "id": "null18t",
        "score": 102,
        "body": "Right? Why are we explaining shit to people who don\u2019t deserve our stories. OP, sorry your date was an asshat, please never talk to him again. Save your explanation (and time/energy) for someone who rates it."
      },
      {
        "id": "nukl3bl",
        "score": 95,
        "body": "Agreed"
      },
      {
        "id": "nuk4hif",
        "score": 93,
        "body": "Ive fancied to date a fellow disabled vet. The idea of having the freedom of time and perhaps adventures overseas without the restraints of normal people life. Unfortunately most in our position are way older than us."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1ot3h9o",
    "title": "Fake Veteran discounts",
    "body": "For the longest time, I'd been giving Home Depot much love and respect because of their standing 10% discount for veterans. I'd also been giving them all my Home Depot type business.  \n\nIt used to be that you show your proof at checkout and they'd apply the 10% discount on your purchase. It was legit. Then, a couple years ago, they did away with that old way and made us register one time online with HD HQ. From then on, the discount would be applied automatically when you swipe your card (yes. I know. It eliminated the cash option). \n\nAfter I rem odled my bathroom and repiped my house,  exclusively with HD supplies, I gathered up all my receipts to calculate my savings only to find out that I had saved 10% on a couple Gatorades and a candy bar. Everything else was full price. \n\nI looked into the discount and it had changed to 10% off everything *EXCEPT;* tools, hardware and equipment rentals. Lol in other words, except anything you came here to buy.\n\nThey just use us like everyone else does. They'll spend $1000 to advertise about the $1 they gave to a Veteran",
    "flair": "Discussion",
    "score": 780,
    "comment_count": 284,
    "created_at": "2025-11-10T03:35:34+00:00",
    "top_comments": [
      {
        "id": "no1txi8",
        "score": 382,
        "body": "You can shop HD from the AAFES/NEX websites decent discount and no tax"
      },
      {
        "id": "no1tvsr",
        "score": 154,
        "body": "I go there all the time and use the self checkout, and enter my phone number. It definitely applied the 10% to everything I\u2019ve purchased because it shows the difference on the self checkout screen for each item."
      },
      {
        "id": "no23vzr",
        "score": 94,
        "body": "For appliances I\u2019ve found direct from LG with the veterans discount is much better than HD. Even with tax."
      },
      {
        "id": "no1yw3d",
        "score": 73,
        "body": "Yep, this is how I buy appliances now."
      },
      {
        "id": "no1v73u",
        "score": 67,
        "body": "Works for everything except lumber for me."
      },
      {
        "id": "no1vbt2",
        "score": 64,
        "body": "Nope all honorably discharged can use the websites.  If you have a service connected disabilty at any level can go on base and use the actual bx/commissary with a VA Healthcare card"
      },
      {
        "id": "no1xcbg",
        "score": 55,
        "body": "Lowe\u2019s is much better for Veterans."
      },
      {
        "id": "no21wyr",
        "score": 32,
        "body": "Lumber is excluded at Lowes also"
      },
      {
        "id": "no1vpl5",
        "score": 27,
        "body": "I use the app to generate a QR code that I scan at self check. It works for everything in the store, even 5 gallon bottles of water."
      },
      {
        "id": "no2b8vz",
        "score": 26,
        "body": "Our HD doesn\u2019t offer the military discount on appliances. Wish I had known this when I had to replace my washer!"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1jdq215",
    "title": "You don\u2019t look like a Veteran",
    "body": "So I\u2019m a black dude, I used to have long locs(cut em a while back)\u2026I primarily kick it with other vets for obvious reasons\u2026but when we\u2019re out at a bar or whatever and we\u2019re talking about time served just reminiscing about our prime days more of than not some random mf that never served will butt in and say \u201cwell you don\u2019t look like a Vet!\u201d So my question to yall\u2026have yall experienced this? And WHAT THE FK DOES A VETERAN LOOK LIKE?! I\u2019m sorry I don\u2019t have a blonde buzz cut with blue fkn eyes\u2026but why is it always the same shit\u2026I never understood this and it pissed me off having served and to have some fuckin goofball utter these words.",
    "flair": "Discussion",
    "score": 728,
    "comment_count": 583,
    "created_at": "2025-03-17T22:40:42+00:00",
    "top_comments": [
      {
        "id": "mice3ca",
        "score": 426,
        "body": "People have this specific image of a veteran in their head. Some 6 foot + tall corn fed country boy who wears grunt style shirts, cowboy boots and a hat with an American flag on it. Most of us don\u2019t look like that. Hollywood just portrays us like that and the people love it."
      },
      {
        "id": "mich17e",
        "score": 191,
        "body": "lol all those grunt style shirts make me cringe. I always get the feeling it\u2019s someone who wants to look like they were in the military but their balls were too small."
      },
      {
        "id": "mickj67",
        "score": 146,
        "body": "First appointment at a VA specialty clinic. The nurse opens the door and calls my name. I stand up and walk over. She asks me if the veteran is in the bathroom. I just say I am the veteran. Because this is normal."
      },
      {
        "id": "micm9ag",
        "score": 123,
        "body": "I am a black woman and get that all of the time. And when I tell them I am a disabled vet despite having all of my fingers and toes their eyes bug out."
      },
      {
        "id": "micrf6j",
        "score": 117,
        "body": "All the punisher stickers are cringey too. \ud83d\ude44"
      },
      {
        "id": "micx284",
        "score": 94,
        "body": "Everyone who has a Punisher sticker doesn't understand the Punisher."
      },
      {
        "id": "micshov",
        "score": 67,
        "body": "Wow! At the fkn VA?! They should know we come in all different shapes and sizes! I know that appointment was awkward af after that!"
      },
      {
        "id": "midwrh0",
        "score": 63,
        "body": "I was once working at this place with a ton of veterans, but including myself, only two of us were Marines. The other Marine was this really old lady, super tiny. One time she parked in the veteran parking and this boomer tried to call her out. I was walking over to diffuse things, but she let him have it. I don\u2019t remember all that was said, I was laughing too much, but I remember one line that went something like \u201cYOU CAN SPEAK TO ME WHEN THE COLLECTIVE BALLS OF YOUR ENTIRE BLOODLINE ARE AS BIG AS MINE!\u201d\n\nThis lady was in her 70\u2019s or 80\u2019s. I used to joke she must have served with Opha May Johnson. Usually pretty sweet but that whole tirade\u2026well let\u2019s just say the guy that called her out wasn\u2019t doubting her service after that."
      },
      {
        "id": "midc1qh",
        "score": 57,
        "body": "These are the same dudes that start giving you their reasons for not joining even though you didn\u2019t ask lmao. Usually some kind of medical shit or the tough guys go-to: \u201cI couldn\u2019t let someone get in my face like that, I\u2019d get kicked out real quick\u201d like OP said, there\u2019s a lot of goofballs out there."
      },
      {
        "id": "micgofd",
        "score": 54,
        "body": "I love when they thank my husband instead of me \ud83d\ude02 or I ask for the discount and they tell me he\u2019s qualified but I\u2019m not\u2026 and then I show them my ID and they shit a brick."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1jlbzmj",
    "title": "Took the Leap \u2014 Sitting in Costa Rica with a Strawberry Mojito",
    "body": "Air Force vet here. I\u2019ve been toying with the idea of moving to Costa Rica for a while now. Between frustrations with the VA, the insane cost of living, and just feeling completely drained from family, friends, and everything else \u2014 my body felt like it was screaming for a reset.\n\nRight now, I'm technically homeless \u2014 but not because I'm irresponsible. It's because of the absurd rental requirements back in the States: 3x income, plus deposit, plus first and last month\u2019s rent\u2026 all for a dingy one-bedroom, one-bath.\n\nSo yesterday, I did something wild: I bought a ticket to Costa Rica. Now I\u2019m sitting on a patio with a strawberry mojito, soaking up the sun, and wondering why I didn\u2019t do this sooner.\n\nI\u2019ve got a return ticket for early May \u2014 but honestly, we\u2019ll see. I was able to book a month of luxury Airbnbs here for the same price one week would cost me in the U.S.\n\nNot sure what\u2019s next, but for the first time in a long time, I feel like I can breathe.\n\nIf any of you are thinking of making a move, even just for a break \u2014 you\u2019re not crazy. Sometimes, the system isn\u2019t built for us. And sometimes, peace looks like palm trees and cheap drinks.\n\nStay safe out there brothers, I'll keep you guys updated!",
    "flair": "Discussion",
    "score": 727,
    "comment_count": 149,
    "created_at": "2025-03-27T19:38:49+00:00",
    "top_comments": [
      {
        "id": "mk3qerq",
        "score": 116,
        "body": "Update I had to refill 3 medications because the VA would only give me a 10 day supply for bureaucratic reasons. I talked to a doctor here for 30 minutes and then paid $60 cash for the refills and consultation. Done"
      },
      {
        "id": "mk2f6np",
        "score": 86,
        "body": "**I love this.**  I hope you enjoy the shit outta' your trip, OP!\n\nCan confirm, if you feel like you're about to lose your mind in this hot-garbage rat-race, a trip to the Caribbean can be the best medicine.\n\nI'm originally from South Florida, but trapped in Virginia until my kids graduate high school.  I miss it dearly, especially the past 1/2 weeks.  I made several trips to small islands in my younger/single days, and the effects were incredible.  It's a completely different world.  Five Stars, highly recommend!"
      },
      {
        "id": "mk3q9u5",
        "score": 40,
        "body": "I'm a bit more than a year away from making that jump. I'm hoping you will keep posting, post your progress, experiences, likes, dislike, and anything else you think folks should know."
      },
      {
        "id": "mk3retz",
        "score": 23,
        "body": "I'll keep you updated!"
      },
      {
        "id": "mk2nvwz",
        "score": 17,
        "body": "Stay careful of the crazy taxi drivers, scammers, and hookers."
      },
      {
        "id": "mk50sdr",
        "score": 17,
        "body": "They're referred to as \"Ladies of Negotiable Affection\" for pc purposes now."
      },
      {
        "id": "mk9n6pj",
        "score": 13,
        "body": "I saw a doctor here and had all my medications refilled in an hour for 60 bucks not worth all the hassle"
      },
      {
        "id": "mk2telj",
        "score": 12,
        "body": "Man I loved Costa Rica when I went to Envision Festival. It was a blast. The food, the people, the beaches and jungles. Boy I am so happy for you!! Pura Vida! Keep us up to date on your adventures please"
      },
      {
        "id": "mk3f4e4",
        "score": 12,
        "body": "CR is the most expensive country in Central America (I worked there for 5 years).\n\nMy good Tico friend in San Jose is desperate to move to (in order) Columbia, Mexico City or Peru.\n\nHaving been to Machu Picchu last year I'm down with Peru."
      },
      {
        "id": "mk2vc6w",
        "score": 10,
        "body": "This is it right here, this is the life!!! Enjoying life, living in the moment and doing you. Be safe my friend \ud83c\udf79"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1nqh3k6",
    "title": "This is actually how bad the job market really is regardless if you\u2019ve served or not.",
    "body": "Despite having 7-8 years of food service experience which includes my time as a CS in the Navy, it wasn\u2019t even good enough for a part time job at Waffle House. I\u2019m going on 6 months unemployed and I either get ghosted or receive these bullshit emails. I\u2019m under two temp agencies and have not gotten a consistent shift out of either of them. WTH is really going on?",
    "flair": "Discussion",
    "score": 706,
    "comment_count": 394,
    "created_at": "2025-09-25T20:06:06+00:00",
    "top_comments": [
      {
        "id": "ng7a7b9",
        "score": 642,
        "body": "You weren't combat arms.  If you were, Waffle House probably would have said yes"
      },
      {
        "id": "ng78f9e",
        "score": 260,
        "body": "Dude use the GI bill. Also, no one cares if your a vet (from another vet)"
      },
      {
        "id": "ng7kcdz",
        "score": 217,
        "body": "This joke went over people heads \ud83d\ude02\ud83d\ude02\ud83d\ude02 this is golden - much love from a combat arms vet"
      },
      {
        "id": "ng7arcp",
        "score": 96,
        "body": "The joke is that people are always fighting at Waffle House, especially employees lol."
      },
      {
        "id": "ng79fac",
        "score": 94,
        "body": "You are overqualified for wafflehouse dude. Employers turn down candidates for being overqualified plenty. \n\n  \nWhat is really going on? Most likely you have a shit resume. \n\n  \nGo apply to the post office. At least for temporary work. It beats unemployment."
      },
      {
        "id": "ng7p1iz",
        "score": 81,
        "body": "Apply to Denny\u2019s, it\u2019s Waffle House for people who can\u2019t fight."
      },
      {
        "id": "ng7b0u8",
        "score": 46,
        "body": "Ya what hateplow said! Depending on where you\u2019re at the BAH could be a damn nice paycheck while you\u2019re in school."
      },
      {
        "id": "ng7o0li",
        "score": 33,
        "body": "They need people with hands"
      },
      {
        "id": "ng7dpr8",
        "score": 31,
        "body": "This.\n\n\nCommunity colleges often have degrees for cooks in the hospitality line of classes.\u00a0\n\n\nOr find out if those french schools accept VA money and go hang out with some heavy smoking brigade kitchen assholes for a while."
      },
      {
        "id": "ng7f56v",
        "score": 27,
        "body": "13M 03-07 got denied there and Home Depot lmfao!!!"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1npmpmj",
    "title": "Update on: I didn't kill myself today.",
    "body": "Finally made it over to the mental health walk in clinic today. All that asshole allowed me to do was fill out a change of doctor form. Sat outside and cried until 2 cops came up to me. Nearly got arrested for blowing my stack. They walked me to the patient advocate. She walked me back to mental health and got me in with the social work supervisor. Useless, as always. Told them to piss off and said I was going to the local state university medical center in the city. Ended up in the ER at the VA. The only person who listened thru this entire ordeal was the ER attending physician. Ended up getting one pill for today's episode. Filed a complaint with the state medical board on my psychiatrist for malpractice and malfeasance. Sitting on the porch smoking a joint and I'll be here the rest of the day. Staying alive out of spite at this point. Rant over. ",
    "flair": "Health Care",
    "score": 690,
    "comment_count": 102,
    "created_at": "2025-09-24T20:13:26+00:00",
    "top_comments": [
      {
        "id": "ng0xl4w",
        "score": 100,
        "body": "glad still hear lad from ex british army infantryman  hope your able get self back on the right track you want to be on"
      },
      {
        "id": "ng139kx",
        "score": 77,
        "body": "I love when British dudes call me lad. Thank you."
      },
      {
        "id": "ng0spu2",
        "score": 65,
        "body": "Hey, if spite keeps you going, then own it. Definitely shine a light on the bad care. \n\n**Phone**:\u00a0202-461-7699\n\n* [**Mail**:\u00a0Office\u00a0of\u00a0General\u00a0Counsel\u00a0(022D),\u00a0Department\u00a0of\u00a0Veterans\u00a0Affairs,\u00a0810\u00a0Vermont\u00a0Avenue,\u00a0NW,\u00a0Washington,\u00a0DC\u00a020420.\u00a0](https://www.bing.com/ck/a?!&&p=b53ed526032b4b6e63d99b83c93d4e66f1ff434bf210da47f7e7c1d9a6c42df4JmltdHM9MTc1ODY3MjAwMA&ptn=3&ver=2&hsh=4&fclid=359745b0-1f7a-6ae6-2306-50691ee86b35&psq=make+a+complaint+with+the+vA&u=a1aHR0cHM6Ly93d3cudmEuZ292L09HQy9kb2NzL0FjY3JlZC9Ib3d0b0ZpbGVhQ29tcGxhaW50LnBkZg)"
      },
      {
        "id": "ng130rw",
        "score": 36,
        "body": "I\u2019m glad you\u2019re still here with us. \n\nI\u2019ve had some dark days lately, but I\u2019ve also found reasons to stick around. I guess spite is one too! Unique, but do what works for you \ud83e\udd23.\n\nI hope you get some help and find other reasons to keep watching for the next sunrise."
      },
      {
        "id": "ng16c0a",
        "score": 34,
        "body": "welcome lad Been there my self few times"
      },
      {
        "id": "ng19tke",
        "score": 30,
        "body": "As a mental health counselor who wears a \"survive out of spite\" pin on my hospital badge, sometimes thats the right energy to have. \n\nOn another note, Im so sorry that you're struggling and that everyone is failing you in getting you help. I know how frustrating and isolating that can be, to sit in a waiting room or outside a facility and cry and have no one stop and even ask if you're ok. It sucks ass. \n\nIm glad that you made it another day and if you need a buddy to help you get through a bit more or even just one more, please don't hesitate to reach out to me personally. Your brothers and sisters are here for you"
      },
      {
        "id": "ng111l8",
        "score": 29,
        "body": "Thank you for this. It didn't seem like the OIG was the right department. Appreciate ya!"
      },
      {
        "id": "ng0rvha",
        "score": 23,
        "body": "Glad you survived it! One day at a time and if nothing else, make it your mission to bring an end to the VA\u2019s fuckery! Just one reason to stay keeps you kickin for another day! And other such stuff. But genuinely I hope you find the help you need. I don\u2019t know you personally but I know you have a place in and value to this world, so don\u2019t give up."
      },
      {
        "id": "ng1wizr",
        "score": 19,
        "body": "This is one reason why I took my pension, me kids and moved to Vietnam. I\u2019ve been here a month and already finished all my medical testing and half the treatments that the VA never had time to fit me in. I\u2019m rated 100% and I have a freaking brain tumor, teeth that need to be fixed and moving her I have an actual doctor who cares. I paid a total of $581 to have a FULL BODY scan, MRI, X-rays, Labs, CAT scan, and now I\u2019ll start EBOO, and got my baseline and priceless HOPE! I\u2019ll NEVER GO BACK!! Never!!!!"
      },
      {
        "id": "ng1bt3v",
        "score": 13,
        "body": "We love you. You\u2019re not alone."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1odkbhh",
    "title": "What was the Gas Chamber like for you in Basic?",
    "body": "",
    "flair": "Discussion",
    "score": 684,
    "comment_count": 710,
    "created_at": "2025-10-22T20:57:20+00:00",
    "top_comments": [
      {
        "id": "nkukwha",
        "score": 329,
        "body": "Snot everywhere"
      },
      {
        "id": "nkulibx",
        "score": 131,
        "body": "I was in the middle of the line. Drill Sergeants started at each end, and made guys pull off their masks and say their name and social. Both stopped at the guy on either side of me and thought the other one got to me. I never pulled my mask off and left."
      },
      {
        "id": "nkukv0n",
        "score": 110,
        "body": "Spicy but there were 2 kids who were fucking immune. Came strolling out no snot, no tears, nothing. Just said it cleared their sinuses haha\n\nHad to get CS gassed during every pre deployment work up and the worst part was the gas soaked into your plate carrier and would fuck up my skin for a few weeks after no matter how much I tried to soak it out"
      },
      {
        "id": "nkum5ep",
        "score": 89,
        "body": "Lmfao I was one of those 2 kids and they tried so hard to try to get me to cough. For anyone reading this in the future on their way to basic who finds out they\u2019re resistant, pretend. Pretend it hurts. You\u2019re making it worse on everyone else bc they will keep your entire row longer due to you not coughing."
      },
      {
        "id": "nkumhw7",
        "score": 71,
        "body": "And then, more snot when I opened the dryer"
      },
      {
        "id": "nkumyvm",
        "score": 44,
        "body": "Walked out looking like I\u2019d been in a bukkake porn shoot. Not really proud to have typed this."
      },
      {
        "id": "nkuoqay",
        "score": 37,
        "body": "[deleted]"
      },
      {
        "id": "nkul4qn",
        "score": 33,
        "body": "I dont remember much about it but I know that was clearest my sinuses have ever been."
      },
      {
        "id": "nkuptsv",
        "score": 31,
        "body": "I was also one of those 2 kids. It burned a bit, but nothing like what everyone else was doing - snotting and puking into their (tucked in) shirts. I walked out like nothing had happened. I didn't get hammered like redditlurkin69 did. My RDC just looked at me and said, \"I guess it doesn't get everyone the same.\"\n\nHere's a fun no shitter, though, I joined a little older (early 20's). The junior RDC was the same age or younger than me. One day he came down the row during an inspection, tossing mattresses and drawers, screaming up a storm. He gets to me, leans in, and says \"these fucking kids\" and then moved on to the next one to toss his mattress and empty his drawers on the floor.\n\nBeing just a bit older in basic was golden. Some of the best days of my life, tbh."
      },
      {
        "id": "nkv02p6",
        "score": 30,
        "body": "I had to say Name, Social, then spell city I joined from. I never got past my social"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1nt329j",
    "title": "Hey, y'all. We need to take a moment and catch our breath.",
    "body": "Alright ladies, gentlemen, enbies, and Marines.  Gather round and pop a squat.  We need to have a lil heart to heart.  This doesn't apply to most of you, but I'm betting it applies to someone you're acquainted with.\n\nIn the last 24 hours, America has had two separate incidents involving Iraq veterans shooting up civilian targets.  This isn't okay.  \n\nAs of this writing, the motivations of the shooters is unknown, but let's be real, there's absolutely *ZERO* reason for someone to justifiably unload into a crowded civilian structure, but this is especially true of veterans.  We don't farkin kill helpless civilians.  Period.  \n\nQuite the contrary: our purpose is to *protect* civilians from this kind of attacks.  How many of us literally stood as human shields between hostile insurgents and unarmed civilians when we were overseas?  \n\nLook, we all need to stop, take a step back from everything, and take a few deep breaths.  I understand that stress and anxiety levels in the veteran communities are high right now.  There's a lot of uncertainty on the horizon, and a lot of us are definitely feeling the old, familiar weight of the world once again bearing down on our shoulders.  But we need to keep each other accountable.  Reach out to your brothers, sisters, and uncategorized.  Check on your peoples.  Remind them they're loved and that things are still okay and they're not alone.  \n\nNow, more than ever, we need to be unified... especially as the rest of the nation continues to be further divided.  \n\nTake care of yourselves.  Take care of each other.  Find yourselves a little bit of peace this week.  Reach out if you're struggling.  \n\nI love you.  It's gonna be okay.  We can make it through anything so long as we're together.",
    "flair": "Discussion",
    "score": 669,
    "comment_count": 178,
    "created_at": "2025-09-28T23:34:59+00:00",
    "top_comments": [
      {
        "id": "ngqq7v9",
        "score": 407,
        "body": "Tried to pop a squat but my knees gave out on me. Then I sneezed and threw out my back."
      },
      {
        "id": "ngqq94j",
        "score": 162,
        "body": "We're lucky we made it home. Don't turn America into a war zone."
      },
      {
        "id": "ngqqp92",
        "score": 129,
        "body": "Same, and now I need to change my underwear."
      },
      {
        "id": "ngqttiu",
        "score": 116,
        "body": "Good post, man, but i laughed inappropriately when you separated Marines from \"ladies,\" \"gentlemen,\" and \"enbies.\" On point."
      },
      {
        "id": "ngr1hlq",
        "score": 69,
        "body": "I mean, just being 100%, we all served with a few who were a little off from the get go and a few of us have witnessed the break down of someone. I don\u2019t think that is something that has changed all that much through the years in war or peace(keeping). Whenever I hear a veteran was involved in some craziness I always brace myself in case I read a name I recognize.\n\nJust keep taking care of each other - it\u2019s not just a vet thing."
      },
      {
        "id": "ngqpxdt",
        "score": 57,
        "body": "Get laid, get paid, and don't shoot up the civilians. Got it?"
      },
      {
        "id": "ngr84w8",
        "score": 54,
        "body": "What's more we all made it home from countries that were engulfed in the horrors of a civil war. We've seen how horrific it could be, the atrocities that turn a Sunni/Shia neighborhood into a purely Sunni one. None of us should wish that on our own country."
      },
      {
        "id": "ngqse2x",
        "score": 45,
        "body": "Commando baby!"
      },
      {
        "id": "ngr456m",
        "score": 42,
        "body": "That doesn't mean we have to make allowances for it in the veteran community.  We really are responsible for policing our own.  Society already doesn't like us."
      },
      {
        "id": "ngqupr7",
        "score": 37,
        "body": "I always make the inappropriate joke of \u201cYall ain\u2019t gotta worry bout me. I\u2019m way too lazy to shoot anything up.\u201d I do worry about my counterparts tho."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1kvzi1k",
    "title": "For those who want to share",
    "body": "Today is a hard day for alot of us. I wanted to make.a place for us to share our stories, or to just say we miss our friends. To all that have fallen in combat and outside. Till vahalla brothers and sisters. So share your stories here tell the good memories of the ones we all miss. To the ones struggling you are not alone we are all here and we are all one. I may not know you but I love you as a brother or a sister.  IGY6.",
    "flair": "Discussion",
    "score": 615,
    "comment_count": 36,
    "created_at": "2025-05-26T17:00:30+00:00",
    "top_comments": [
      {
        "id": "mudgjx9",
        "score": 37,
        "body": "While society may take a few days a year to remember the military and veterans, to those of us who served and know the true price of freedom, we remember every day.  From one veteran to all veterans, thank you for your service to this country and know it\u2019s appreciated. We all took and oath and live to higher standards. The daily struggles of life are sometimes harder when we focus on what we lost, I try to remember the best about the ones who didn\u2019t make it home and remind others of their legacy!"
      },
      {
        "id": "mudv278",
        "score": 17,
        "body": "1-6 FA here. Was attached to 6-4 Cav out of 1st ID, 3rd Bat. Deployed to Camp Clark Afghan Dec 2010-Dec 2011. It\u2019s crazy how long it\u2019s been, but it still feels like yesterday.\n\nSPC. Sean Walsh\nSSG. Mecolus McDaniel\nSFC. Nicanor Amper\n\nRest easy brothers, til Valhalla."
      },
      {
        "id": "mudogs9",
        "score": 14,
        "body": "*This post was mass deleted and anonymized with [Redact](https://redact.dev/home)*\n\nchubby insurance salt literate imagine squash consider employ elastic busy"
      },
      {
        "id": "mudgf7v",
        "score": 12,
        "body": "Second to none"
      },
      {
        "id": "muegf7w",
        "score": 12,
        "body": "I've got three good friends I lost overseas. I have 11 more I lost in 2019 between ending themselves, car accidents, and one murdered. Today reminds me of them, and I hate it."
      },
      {
        "id": "mudgbrs",
        "score": 12,
        "body": "Thanks for sharing this. Truly. All of us GWOT troops have the same bracelets....sometimes I wear mine and sometimes it honestly makes it too tangible for me. 20 years gone by in my case since my last KIA experience...rest in peace, Eric. \n\nHope you have time today to remember them and celebrate them."
      },
      {
        "id": "muekuqg",
        "score": 11,
        "body": "You can order your own at https://tilvalhallaproject.com/collections/memorial-bracelets/products/customize-your-band-gc1c2a68b?gad_campaignid=19486331511&gad_source=1&gadid=643958130712&gbraid=0AAAAAC9uP4iXfug4WgYhvP-jPqG_NYxbJ&gc_id=19486331511&gclid=Cj0KCQjwotDBBhCQARIsAG5pinPIqHFz6o6L4aP-GnGWrlyWoSvAgolywpYwZa_NzYrlPxnOnWTUcO8aAgn1EALw_wcB&h_ad_id=643958130712&utm_campaign=19486331511&utm_content=144548890506&utm_medium=paid&utm_source=google&utm_term=kia%20bracelet"
      },
      {
        "id": "mudlz16",
        "score": 8,
        "body": "3-17FA vet here, I never knew these guys but knew one of the NCO\u2019s in the same incident (from the 5-2SBCT deployment). \n\nI\u2019ll never truly know how blessed I am to have not endured that experience\u2026"
      },
      {
        "id": "muejjt9",
        "score": 8,
        "body": "I\u2019m from the Cold War era. I started in Germany (81-84) in the  59th Ordinance Bde. President Reagan was just sworn in. I was in a Huey unit and we hauled nuclear and chemical warheads for 155 rounds. Site 59 which has become public finally. https://wwmt.com/news/local/site-59-secrets-local-man-says-nerve-agent-exposure-ignored-by-department-of-defense\n\nMany of my fellow crew chiefs have died of various cancers and many are fighting it now. Agent Orange of the 80s. We were concerned however the missions had to be completed. The commies were not far away we were constantly told."
      },
      {
        "id": "mugzz1n",
        "score": 8,
        "body": "A Co ammo dawg with 402D BSB, 5/2 SBCT during that round and I share the same sentiment. May all our brothers and sisters in arms who did not make it back, rest easy"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1p1rsn7",
    "title": "Had to bite my tongue at the VA today.",
    "body": "I am a veteran and I am also gay. There was another veteran in the lab today, that kind of pissed me off, but I bit my tongue because I did not want to be confrontational. He thought it was great that the VA had removed all of the signage informing the fags as he called us about the services that the VA offers to help keep gay men and women who served safe. He thought is was awesome that signs had been removed. I wonder if I should have said something or if I did the right thing by not opening my mouth.",
    "flair": "Discussion",
    "score": 598,
    "comment_count": 456,
    "created_at": "2025-11-20T02:43:56+00:00",
    "top_comments": [
      {
        "id": "nptopqg",
        "score": 770,
        "body": "Man, I\u2019ll never understand another vet wishing harm on fellow service members. Fuck that guy."
      },
      {
        "id": "npu5zpc",
        "score": 206,
        "body": "I have and will again confront other vets and their spouses about shit they say in a VA. But fair warning, the VA police can and will intervene and you can get into trouble.\n\nI got sat down and lectured about conduct policies over what I said to a spouse after she shot her fuckin mouth off about how OIF/OEF vets don't know what war is like and didn't go through what her husband who was a Viet Nam vet did. I will not let anyone denigrate someone's service. And certainly wouldn't let some dependapotomus do it.\n\nSo say something if you want, just know there are regulations about conduct so don't cross them or at least be prepared for the consequences if you do. Personally, for me, standing up for  the right thing is more important than being in compliance. So I'll be that asshole yelling in the waiting room at someone for being a pile of burning ostrich shit.\n\nIf you want to avoid the confrontation, you can report them through either security or patient advocate. They are creating a hostile environment. You need a time, location and if you can, take a subtle picture. They have cameras all over so they will verify. But yea. That is a route as well."
      },
      {
        "id": "npu62v2",
        "score": 141,
        "body": "I was in when don't ask don't tell was repealed. It was amazing to see my friends and colleagues not have to live in fear of losing something they loved. I'm sorry you had to hear that today but there are many who support us (i didn't have to \"worry\" about it because I'm in a hetero marriage but it applied to me, as well).\nHugs"
      },
      {
        "id": "npwgao2",
        "score": 131,
        "body": "I shall never forget watching Senator Barry Goldwater back in 1964 reply to a question concerning gays in the military by saying \"I don't care who is in the foxhole with me as long as they can shoot straight!\" {Paraphrased from the memory of a 78 year old man)"
      },
      {
        "id": "npuoij6",
        "score": 116,
        "body": "It's because they don't accept us as one of them."
      },
      {
        "id": "nptuxhx",
        "score": 114,
        "body": "He would have doubled down.  Maybe even tripled down if he was a real asshole.  The people that work at the VA and hear this stuff should be the ones to say something honestly.  It\u2019s their workplace in this case.\n\nAdd on-For some that say it\u2019s not the staffs job.  If you were at work and a customer said anything like this to your co worker or another customer, you wouldn\u2019t say anything?  That\u2019s sounds way worse to me.  Plus at that point you are condoning it. You are responsible for your workplace and keeping it appropriate."
      },
      {
        "id": "npv24gq",
        "score": 113,
        "body": "Then they are idiots. Everyone who stood and swore the oath is my brother/sister."
      },
      {
        "id": "npxs21b",
        "score": 64,
        "body": "[removed]"
      },
      {
        "id": "nptqwkk",
        "score": 63,
        "body": "\"Do you hate gay people or are you afraid you'd enjoy the way dick tastes? \"\n\nI've said it to a few homophobic people & it absolutely confounds them. I'd have zero problem saying that in a VA setting either"
      },
      {
        "id": "npu7o06",
        "score": 56,
        "body": "That\u2019s gay /s"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1o1f7nl",
    "title": "So tired of people hating on my benefits",
    "body": "I currently live with my brother and we currently share a 2 bed 2 bath apartment. Due to my VA disability compensation, I agreed to split rent 60/40 with the bonus being I get the master bedroom and covered parking spot. However, my brother keeps saying I should pay more of the rent or bills since my \u201cfree\u201d money covers my half of the rent while he needs to dedicate at least 40% of his monthly income to rent alone. \n\nI care for him but also want to tell him that he can still join the army and bust his back. \n\nA family friend named John also often criticizes me for collecting benefits. John is an older man who\u2019s close to collecting social security. John always asks how I\u2019m collecting disability compensation when I\u2019m \u201cclearly not disabled.\u201d I try to explain to him that just cause I\u2019m not in a wheelchair or missing a limb doesn\u2019t mean I\u2019m not hurt or suffering from illness. \n\nJohn claims that \u201cyou were just fine a few years ago. So all this stuff suddenly started hurting?\u201d I again try to explain that he\u2019s not with me 24/7 and I\u2019ve dealt with pain, sleep issues and mental issues for years and only started collecting compensation after avoiding it for years. \n\nI then turn it on him and say he\u2019s about to start collecting social security on top of his day job and he says that\u2019s different because he\u2019s \u201cearned\u201d those benefits. \n\nAnd please no snarky \u201cthat\u2019s why you keep your benefits to yourself\u201d comments. I realize that now but back then, I didn\u2019t think anyone would\u2019ve offended by me collecting benefits. \n\nSorry fam just venting here. Hope you\u2019re well all. ",
    "flair": "Discussion",
    "score": 603,
    "comment_count": 498,
    "created_at": "2025-10-08T16:23:55+00:00",
    "top_comments": [
      {
        "id": "nig5vjg",
        "score": 757,
        "body": "Tell him he can pay 100% of it when you find a new roommate and tell the other guy to fuck off."
      },
      {
        "id": "nig4ugk",
        "score": 226,
        "body": "Give him the address to your nearest recruiting station."
      },
      {
        "id": "nig6013",
        "score": 225,
        "body": "You earned disability by trading your physical and mental health and well-being."
      },
      {
        "id": "nihcr5z",
        "score": 140,
        "body": "I made that comment once .  A friend of mine told me I was lucky to be getting free money after I had been medically retired.   All the things that I loved to do in my life.. gone forever.  I dropped him after that and never spoke of my time in service, my disabilities or the benefits again.  Lastly..never tell anyone.. especially co-worker about any of this .."
      },
      {
        "id": "nig81bb",
        "score": 139,
        "body": "I let it slip to a few people my VA Compensation that I thought I could trust. Almost immediately the snide and jealous comments about \u201cfree money\u201d started. I then told them that I was reduced to 10% and whatever that dollar amount is and the comments stopped. Moving forward, don\u2019t tell ANYONE. Good luck."
      },
      {
        "id": "nigec1r",
        "score": 87,
        "body": "You need to stop associating with people that think less of you for receiving benefits. They are not your friends and if they're family, they're shitty. Either way you'd be better off without them."
      },
      {
        "id": "nig7qkv",
        "score": 68,
        "body": "It's not \"free\" money, it was earned. One afternoon,  ask him to go for a ride with you, dont  tell him where you are going, take him to a recruiter"
      },
      {
        "id": "nih3pez",
        "score": 65,
        "body": "This where I compare it to WORKMANS COMP. Joe blow gets his arm ripped off in a sorting machine at the factory. Has to amputate arm, can't save it. Workman comp covers his bills/paycheck until all lawsuits are settled. After a year or two of fighting the system Joe gets a final settlement of 1 million dollars for pain and suffering + loss of his job. The company sends Joe a final email/snail mail saying \"Here, here is 1 million dollars, do with it what you will. We consider this case as closed, good luck for the rest of your life trying to find a Doctor, AND trying to find a prosthetic company that will replace your prosthetic arm every few years.\"\n\nNow here is GI Jane. Driving down the desert road in the sandbox. Her Humvee hits a roadside IED. GI Jane gets her arm ripped off. Has to amputate arm, can't save it. The Army is not in the habit of handing out 1 million dollar checks. HOWEVER the Army takes responsibility for putting GI Jane in that position in the first place. The Army's answer is to medically retire her with a small cash severance package and then hands her off to VA. The Army considers this case as closed, after the hand-off to VA. VA will compensate Jane maybe $3,000 every month for the rest of her life, + free healthcare + prosthetics replacements. Over GI Janes lifetime, she will have EARNED close to 1 million dollars.\n\nIt's almost exactly the same, these 2 scenarios.\n\nTell your family members to \"fuck off, we will NOT discuss this any further. The recruiters station is right down the road, go on and join up.\""
      },
      {
        "id": "nig87nw",
        "score": 61,
        "body": "These people seem to be cunts. My policy is I don\u2019t deal with cunts anymore. Any relative or friend can go fuck off in my book."
      },
      {
        "id": "nih83h4",
        "score": 55,
        "body": "It's almost like war is bad for you or something.\u00a0"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1lrn29w",
    "title": "Part 193883 of why I don't tell people I am a vet",
    "body": "",
    "flair": "Discussion",
    "score": 584,
    "comment_count": 233,
    "created_at": "2025-07-04T16:32:20+00:00",
    "top_comments": [
      {
        "id": "n1c4sl0",
        "score": 430,
        "body": "If someone makes a comment over the internet that you know they'd be unwilling to say to your face, it's usually safe to ignore.  As Mike Tyson pointed out, the internet has made us all too comfortable with talking trash because we know we're not going to get punched for it.  \n\nBut I actually like leaning into this shit with something like, \"I wasn't that particular.  Any would do.  You wanna know the hardest part of bombing children?  My penis.\"\n\nThey're trying to make you mad.  Fuck em.  Make them shocked instead."
      },
      {
        "id": "n1cim8g",
        "score": 193,
        "body": "How can you shoot women and children like that?!\n\n\"Easy, don't lead as much.\""
      },
      {
        "id": "n1c3xh3",
        "score": 182,
        "body": "This is where I have no self control and just lean into it with my reply."
      },
      {
        "id": "n1c56u2",
        "score": 152,
        "body": "I read a book in high school about (I think) a LRRP in Vietnam. He was either back for mid tour or completed his year and was on a date with a girl. \n\nShe asked how many babies he killed. \n\nHe promptly replied \u201cnot enough and that\u2019s why I\u2019m going back\u201d poured his beer on her and left."
      },
      {
        "id": "n1cy9gg",
        "score": 127,
        "body": "That is wrong. Just wrong. Those little fucks are small and fast. You need to lead them as much or more. Stop going around giving bad advice"
      },
      {
        "id": "n1clmhx",
        "score": 82,
        "body": "What do you feel when you shoot a child? Recoil."
      },
      {
        "id": "n1d0e15",
        "score": 68,
        "body": "*\"I don't see race, only target coordinates...\"*"
      },
      {
        "id": "n1c83l8",
        "score": 61,
        "body": "All races, I try to kill everyone equally."
      },
      {
        "id": "n1c7gju",
        "score": 55,
        "body": "This is exactly how to deal with these people who are purely ignorant and are only trying to be antagonistic"
      },
      {
        "id": "n1c3xwm",
        "score": 43,
        "body": "Block trolls and move on."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1jpayku",
    "title": "Update to my best friends su*cide post",
    "body": "Hey yall. I made a post a bit ago because my best friend passed and I was to perform honors. My rank said specialist, I got out as sergeant. I had a beard, didn\u2019t know to shave or let it slide as a vet. I saw a few people ask for an update as they are in similar situations. Well, this is how I went. I performed honors. Then I posted a tiktok that has 200,009 views. Nobody had an issue except a couple \u201cback in my day\u201d vetbros. So in my opinion, honor your friends best you know how and don\u2019t let anyone tell you different (as long as it\u2019s not stolen valor or anything wild). This was just an untimed moment",
    "flair": "Discussion",
    "score": 586,
    "comment_count": 64,
    "created_at": "2025-04-02T00:04:10+00:00",
    "top_comments": [
      {
        "id": "mkyqg3s",
        "score": 306,
        "body": "They\u2019re just jealous to still fit your dress my G."
      },
      {
        "id": "mkyt1lj",
        "score": 62,
        "body": "Glad you were there to support your friend until the end. Had a similar situation but wasn\u2019t able to attend due to being overseas."
      },
      {
        "id": "mkyxxvv",
        "score": 43,
        "body": "Yea fr, ain\u2019t no fucking way that\u2019s happening now for me\ud83d\ude02\n\nHell, I had to go get my goddamn pants loosened for my first DA photo months before getting out lol"
      },
      {
        "id": "mkz1dx2",
        "score": 32,
        "body": "Hey, good on you. I won't say 'be proud' because it was a funeral after all, but I will say 'I am sure you did him justice.'"
      },
      {
        "id": "mkz38gv",
        "score": 32,
        "body": "You did well. Remember your friend. F the vet bro\u2019s"
      },
      {
        "id": "mkz2ca7",
        "score": 28,
        "body": "Sorry for your loss brother. Glad you were able to be there for your friend and his family. You looked neat, groomed, and professional and wore your uniform with pride. You've already sacrificed enough for the Army and you didn't let it take another few months worth of beard from you.\n\nI think you did right and your intentions were well. And we all already know the type of person who would get pissy over something like this. Screw em. \n\nTake care man"
      },
      {
        "id": "ml12eom",
        "score": 25,
        "body": "My tie still fits\u2026."
      },
      {
        "id": "mkz1j6v",
        "score": 24,
        "body": "A-fucking-men brother. I was about to pop a button 6 months before separating, let alone 6 months after the fact."
      },
      {
        "id": "mkze6im",
        "score": 19,
        "body": "Dude you fit in your blues that's all that matters, sorry for your loss brother"
      },
      {
        "id": "mkzfrh4",
        "score": 19,
        "body": "Bro I showed up to my nephews first salute at west point shaggy and without any headgear. We have colonels in the family. There was brass everywhere,\nYou showed up, let yourself feel good about that, till Valhalla."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1o959je",
    "title": "Thankful for VA Healthcare",
    "body": "I had to go to an in-network non VA ER x2 for potential DVT and lower leg extremity swelling with massive throbbing pain that took me out from moving anywhere in the house. Just thankful that my ER visit costs were all covered! so if you get 50% and more, definitely be grateful because this alone is the major benefit. Even as 10%, go sign up for VA Healthcare!",
    "flair": "Question/Advice",
    "score": 584,
    "comment_count": 124,
    "created_at": "2025-10-17T16:00:23+00:00",
    "top_comments": [
      {
        "id": "nk02pco",
        "score": 130,
        "body": "VA paid for my sons NICU stay (wife served as well) 350K. So thankful."
      },
      {
        "id": "njztihk",
        "score": 56,
        "body": "It\u2019s worth it. They recently paid $116,000 for my hospital stay earlier this year"
      },
      {
        "id": "nk03whb",
        "score": 50,
        "body": "Yeah, socialized healthcare is great"
      },
      {
        "id": "nk0j184",
        "score": 28,
        "body": "8 years of cancer treatment for me. I'll be monitored for the remainder of my life.\n\nI'd be terrified to add it all up. \n\nThe care has been fantastic, the keeping up the paperwork meh. I'm not gonna complain at all. \n\nI now have Medicare. \n\n99% of the time, I pick the VA. For me, it's just better care all around. \n\nLPT: check your pits, tits and reproduction bits often. Cancer sucks."
      },
      {
        "id": "nk12wep",
        "score": 28,
        "body": "We still have tricare our son spent a week in the nicu from his birth. The bill was over $100k we paid $2k. I'm so grateful for it and the VA healthcare I receive."
      },
      {
        "id": "nk01y2p",
        "score": 28,
        "body": "definitely agreed \ud83d\udc4d\ud83c\udffb without the VA I would\u2019ve been screwed financially for medical costs like this"
      },
      {
        "id": "nk0bjep",
        "score": 25,
        "body": "Agreed.  I\u2019ve worked in private, public, university, and VA medicine and when appropriately staffed, the VA outperforms them all by most metrics.  The data supports this as well."
      },
      {
        "id": "nk0i5l6",
        "score": 22,
        "body": "Im only 10% rated, and the VA covered cancer screening MRIs, ultrasounds, and mammograms for 4 years. Last year, they fully covered my preventative double mastectomy and implant reconstruction. The only thing I have ever paid for is prescriptions"
      },
      {
        "id": "nk13rnr",
        "score": 21,
        "body": "350k is insane"
      },
      {
        "id": "nk095zc",
        "score": 19,
        "body": "\u201cITs N0T S0ciALized iTs pArt of OuR sErVice\u201d"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1ravp1w",
    "title": "Honesty from a Combat Medic",
    "body": "I was 19 when we deployed to Afghanistan, the Korengal Valley. I was a platoon medic, I saw some of the worst shit I've ever seen and will ever see. \n\nOur OP was constantly under attack from mortars, rockets, machine guns, you name it. Patrols turned into ambushes at least once a week, usually more. I lost some of the best men out there, my best friends even, and saw many more get maimed to the point of going home early, disfigured for life. And that was within the first month.\n\nBy the grace of some Higher Power, I survived an IED ambush during a convoy, subsequently earning a BSM w/ V and a PH all in the span of three hours or so. Medals for what? Living while our RTO lay in a pool of blood? An \"atta boy\", when I failed to do my job? A \"good job\", pat on the back, for being a stupid kid in a stupid war? \n\nI was genuinely, without a doubt, terrified. Like truly terrified. Constantly. Maybe more so scared for my guys (especially watching too many die in my arms) because I knew, as a medic, I was failing. Failing to keep my boys alive and get them home to their families. Failing to prevent them from getting hurt. Failing to preserve life. I would've given them my own life if they could still be here today. I had no one and nothing but a family I grew up with that pretty much ignored me my whole childhood. I would take that deal in a heartbeat.\n\nI close my eyes and I can vividly recall the screams of men dying, the chaotic cacophony of warfare, the unsettling quiet after all the blood has been shed and the feeling of emptiness after being exposed to combat for so long and so constantly. Violence became \"Just Another Day At The Office (tm)\". \n\nI actually did like the locals. The best days were when I got to go into the village with my terp, and shoot the shit with these people. Give them basic aid. Listen to stories of the mujahideen fighting the Soviets. I loved the culture, and I loved my job.\n\nBut I would always fall victim to the racism, the prejudices and the hatred that the military culture instills in you against these people. Everyone's an enemy, right? Can I trust that elder to not let the Talk an plant an IED along our route? Well, too bad. We dropped a bomb on his house and killed some kids. Just give them 200 bucks and a new cow, call it good.\n\nAt 19, your brain isn't done forming connections and growing. At 19, that brain of mine got traumatized early and often. Not to mention the TBIs that only exacerbate these feelings of hopelessness, terror and immense sadness. I've been disillusioned with the military ever since. I'm a cynic when it comes to it, some have called me. And I have to agree, yes, I am, because I am the product of that broken system that uses, abuses then abandons their fellow man.\n\nFYI - I go to therapy once a week, and I have an amazing support system of veterans and citizens that help me through it. I'm 36 now and finally open to speak about my experience after 16\\~ years.\n\nI just needed to vent. Thank you.",
    "flair": "Call for Help",
    "score": 561,
    "comment_count": 106,
    "created_at": "2026-02-21T16:39:16+00:00",
    "top_comments": [
      {
        "id": "o6mm27f",
        "score": 241,
        "body": "You did your job Doc. To quote Col. Potter from M*A*S*H, \u201cRule #1 Young men die, Rule #2 Doc can\u2019t change rule #1.\u201d"
      },
      {
        "id": "o6mt9kw",
        "score": 127,
        "body": "A doc here also, thank you for sharing your story brother.  You are so fucking loved.  I just wanna share something I learned years later from my time as a corpsman.  I was in a mass shootout state side before I could deploy and placed on a psych hold.  The shootout occurred 2 weeks after I got out of FMSS.  I was set on saving lives, motivated as hell.  All I wanted to do was bring Marines back safely.  That night, with no medical equipment I lost a marine and a sailor. The marine in my arms while I tried to provide medical care with just knowledge, my t-shirt and bystanders.  I had to testify in court years later with it being a capital murder case.  Before trial I met the Marines family (leaving names out for privacy) and for 3 years they didn\u2019t know someone was with their son/brother when he died.  I shared my story with them, and the closure I saw it bring to them is ineffable.  I learned this day, that as docs, our only job wasn\u2019t only to provide care, try our best to save lives, but also be the witnesses.  The witness that sees them off, that watches their last breath, here\u2019s their last word.  I realized that I wasn\u2019t there by mistake but that God had placed me there to be a witness, that he would give me the strength I needed to carry the final chapter of their story for those that needed closure and peace.  Our stories and experiences are different, I realize that and am under no illusion of it.  But I offer this to you, and invite you to share in this perspective as it has brought me some solace and strengthened my faith while I continue to heal."
      },
      {
        "id": "o6mpvpv",
        "score": 47,
        "body": "I was in Afghanistan 3 times at 19, 21 and 22 also as a medic. I don't know where you were exactly, I am Danish so I was in Helmand, but the experience sounds similar.\n\nWhat is important is that you realise that our job is often a losing battle and that's not your fault, it is the fault of the circumstances. On my first deployment I beat myself up so much over losing a guy. I approached that guy expecting lost limbs and saw a pelvic and abdominal cavity injury. It took an ass beating from a CO to make me stop feeling guilty. We see things that experienced surgeons couldn't fix in the field and sometimes our job is just drugging someone up, holding them and waiting for whatever happens to happen. That doesn't make watching someone bleed out easier or the feeling/memory less helpless, but it doesn't mean you're at fault or should judge yourself so harshly."
      },
      {
        "id": "o6myy92",
        "score": 35,
        "body": "I felt this post. Thanks for sharing. We are about the same age. Iraq at 19 Afghan 21. K9 handler and spent sometime in Korengal myself supporting units. I have seen almost every base in afghan some my worst days were in that valley. I didn\u2019t really talk about anything until recently. Finally stopped drinking a few years ago. Today my battle is with my brain and the VA. I\u2019m not sure which one is more broken. I\u2019m glad I found this subreddit it\u2019s good to know as alone as I may feel back home I\u2019m not alone."
      },
      {
        "id": "o6mkagb",
        "score": 34,
        "body": "It blew my mind coming home after all of that myself and seeing life just continue like nothing was going on.  To think that my brothers were in contact while my wife was asking what I wanted to go eat.  It is hard to find others that can relate.  To grasp what we have been through.  I just typically shut my mouth and live to see another day.\n\n  \nPS:  Thanks Doc for all that you DID do.  I have so much respect for you guys and the work you do.  Right after I got in an IED strike what did I wake up too.............Doc feeling over my body checking for blood.  That right there is just amazing."
      },
      {
        "id": "o6mqx45",
        "score": 30,
        "body": "we are here for you brother. i'm an OIF vet, 07 and 09. i lost my best friend during my second deployment to an EFP.. vent if you need to but just know you are not alone and live your life to fullest for the ones that didn't make it back. \ud83e\udee1"
      },
      {
        "id": "o6n1h6c",
        "score": 27,
        "body": "I was a Combat Medic as well. Been through some shit, but I found my peace going back into medicine on MY TERMS. I became a respiratory therapist. One of the most cathartic things that ever happened to me was when I hit the CODE button, the sound of thunder erupted from everywhere as what sounded like thousands of foot steps came crashing into the room slamming carts and equipment. I started tearing up in that moment because I wasn't alone. Help was here. In that moment, I was no longer the lone medic trying to keep 3 of my friends alive by myself. I knew in that moment that my worst fight was behind me...until covid hit. That felt like a deployment in his own right. I watched so many people die that I stopped remembering faces. It became so normal to pull people off of life support because we've done all we can against a virus that didn't play by the usual rules. I even watched one of my co-workers end up on one of our ventilators before he passed. Its a special kind of hurt when it is one of your own. I've had to witness things I'd rather not describe, but I came out stronger. \nBecause I treated it like another deployment, I already had some tools developed mentally. I was ready to say good bye to my family in order to help people. I learned how to compartmentalize myself. While it sucked to LITTERALY give many people their last breaths. I saved so many.  \nI'm in my mid 30s as well, and happy where I'm at."
      },
      {
        "id": "o6mqeyh",
        "score": 25,
        "body": "If you believe in a higher power I'd encourage you to look into who and what that is. If a higher power does exist they deserve to be sought. Maybe you being saved can place you in a spot to save someone else. \n\nAlso, I enjoy your writing. Have you considered writing as an outlet? Blogs. Books. Articles. Whatever. Let the pen be your escape. Give voice to the life behind the death. God bless Doc"
      },
      {
        "id": "o6mp5rk",
        "score": 24,
        "body": "I just turned 36. Was also a combat medic in Afghanistan at 19. I get it."
      },
      {
        "id": "o6nsfka",
        "score": 20,
        "body": "Have you reconnected with any of those you saved? I would highly recommend it. It allows you to focus on the stories of those still alive because of your intervention. I reconnected with a guy who lost both legs during a time when IEDs weren't yet a thing and we didn't really know who to protect against them. Dude was laying in the dirt and cussed me out, told me to let him die, all sorts of shit while I worked to keep him from bleeding out. \n\nA decade ago I went to a reunion, he came walking in on his VA supplied legs and gave me the biggest bear hug I've ever had. Turns out he married his physical therapist, has five kids (and counting last I heard), and told me he was grateful that I didn't let him bleed out.  \n\nI also tried to reconcile with the ones I couldn't save. I searched out one family and was able to tell them about their son, his bravery, and what really happened to him. After all most families only get the generic version, so I felt it only right to offer them the truth, if they wanted to hear it. \n\nI'll always be f'ed up, but all this has helped me to cope, much, much better. Today I get to work with the VA as a consultant making sure all you knuckleheads get what's coming to you. I love you all my Warrior brothers and sisters, keep moving forward, there are plenty of people like me out here fighting for you, we just don't shout about it. "
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1kkcj45",
    "title": "Im ashamed of myself",
    "body": "\nLast week , I had a full-on meltdown after a road rage incident that escalated way too far. Two individuals cornered me in my own complex after a near-accident,they actually followed me all the way to my parking spot. My fight-or-flight kicked in hard, and I ended up grabbing a tire breaker bar from my car not to threaten, just to protect myself in case things went south.\n\nWhile they were shouting, some kids got out of their car, crying and begging their family to stop and go back inside. That\u2019s when I snapped out of it and tried to defuse things, saying, \u201cNot in front of the kids.\u201d Thankfully, that calmed things enough for everyone to get back in their cars.\n\nBut just as they were leaving, one of them yelled some racially charged stuff saying people like me and my wife \u201cshouldn\u2019t be here.\u201d I\u2019m Latino, and hearing that just broke something in me. I blacked out in rage, yelled something back about serving this country and still being treated like this.\n\nNow that I\u2019ve calmed down\u2026 I feel ashamed. Disgusted with how I let it get to me. I wish I\u2019d been the bigger person and just walked away. But in that moment, I felt humiliated, targeted even.\n\nI don\u2019t really have a point here. I just needed to get it off my chest because I feel like a complete POS right now.",
    "flair": "Question/Advice",
    "score": 555,
    "comment_count": 185,
    "created_at": "2025-05-11T21:58:04+00:00",
    "top_comments": [
      {
        "id": "mrtpc1x",
        "score": 140,
        "body": "Brother. I still love you, and I\u2019m not ashamed of you or your actions one bit. \n\nYou got backed into a corner, protected yourself and your property and no one got hurt. You\u2019ve done a far better job than most police officers who are professionally trained and paid to do that. \n\nYou showed compassion to young souls, who needed it and learned a valuable lesson. \n\nNothing you said was worse than the action of those children\u2019s family members, even if you started the road rage. \n\nWe have buttons, the military adds some and disables some. We spend our entire lives understanding these buttons and how hard, when, in what orders and where they can be pushed. You learned from this button being pushed, don\u2019t be ashamed brother. \n\nI\u2019m proud of you brother."
      },
      {
        "id": "mrthxd9",
        "score": 87,
        "body": "Doesn't sound like you actually did anything."
      },
      {
        "id": "mrtqju3",
        "score": 71,
        "body": "Next time that you see that you're being followed, don't go home. You don't want them knowing where you live."
      },
      {
        "id": "mrtrjds",
        "score": 62,
        "body": "You didn\u2019t involve them, their parents did. You diffused when you saw they were part of the equation.\n\nThe hardest part is not being self aware enough to asses what happened and here you are - good on you, brother.\n\nWhat\u2019s helped me is learning to be constantly aware of yourself on the inside as you are with SA on the outside. It\u2019s definitely not a light switch, and we will have our moments, but just as we learned to be warriors we can learn to walk away. You\u2019re doing the right thing by talking about it and reflecting."
      },
      {
        "id": "mrtlcg6",
        "score": 55,
        "body": "I catch myself in these moments more often than I would like to admit. My wife drives me around most days I need to leave the house. I drove myself today and had two incidents. My brain understands everyone is just in a hurry and isn't being a dick on purpose. My body however reacts as if a car just entered our convoy. The important thing is you recognized the behavior and were able to deescalate before you couldn't take it back anymore. \n\nIt's normal for a vet with PTSD to have trouble regulating all the time. I have to forgive myself and remember that I'm worth keeping around."
      },
      {
        "id": "mrtpxlh",
        "score": 46,
        "body": "People stalked you back to where you live, anyone would be upset. They escalated things by following you home. That is far more embarrassing and psychotic behavior than grabbing a tire bar to protect yourself. I think a lot of people in your situation would have had similar reactions because normal people don\u2019t follow other people home. \n\nNext time someone is following you (although, hopefully there isn\u2019t a next time) or you think someone is, don\u2019t go home. Drive to the nearest police station or to a well lit, well populated area and call the police from there."
      },
      {
        "id": "mru2bnl",
        "score": 46,
        "body": "Bro I\u2019m white as shit  and an old white man told me to brush up on my Spanish for when I get sent to El Salvador, because I have tattoos. Those people just need someone to be angry at to justify their misery."
      },
      {
        "id": "mrtij44",
        "score": 46,
        "body": "Just regretting kids had to be involved in the situation and feeling that, yea the racism was bad but the way I blew up may have been even worse or made it worse."
      },
      {
        "id": "mrtik24",
        "score": 44,
        "body": "I'm sorry you had to experience that!\n\nNow, just take what you learned from the situation, move forward, and be kind to yourself.\n\nAprecio su servicio!  \ud83e\udee1 \ud83c\uddfa\ud83c\uddf2"
      },
      {
        "id": "mrtow7h",
        "score": 40,
        "body": "You\u2019re human. Sounds like you were angry, but you didn\u2019t lose control."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1oeb75i",
    "title": "what do veterans think of stuff like this?",
    "body": "Delete if not allowed because i literally just came here to ask this question. I\u2019m a civillian, never been in the military or even around anyone who\u2019s been in the military. What do US military veterans think of stuff like this? for some reason it bothers me because i feel like this does nothing for our veterans who truly need help. I\u2019m not saying i\u2019m anywhere in a position to even judge but it just seems so redundant to me plus i\u2019ve never seen other veterans supporting stuff like this, only other civilians. It would be nice to have a veterans perspective.",
    "flair": "Discussion",
    "score": 553,
    "comment_count": 365,
    "created_at": "2025-10-23T18:32:22+00:00",
    "top_comments": [
      {
        "id": "nl0zocj",
        "score": 821,
        "body": "As long as they aren't scamming anyone's donations, then sure."
      },
      {
        "id": "nl13nyy",
        "score": 362,
        "body": "My back and sciatica hurt just by looking at them lol."
      },
      {
        "id": "nl12mft",
        "score": 212,
        "body": "crush sort ten close rock aspiring liquid sip axiomatic tender\n\n *This post was mass deleted and anonymized with [Redact](https://redact.dev/home)*"
      },
      {
        "id": "nl10trk",
        "score": 189,
        "body": "Reminds me of the guys who march across America to bring attention to veterans suicide that no one remembers or even knows about. I had a young student working for me at the university who asked me if I knew about his brother and a friend who had walked from Oklahoma to California and back to raise awareness - I had never heard of them and couldn't find anyone else who had."
      },
      {
        "id": "nl10fhr",
        "score": 128,
        "body": "I went to a ruck group in town a couple of years back and none of the people there were veterans. They sure loved talking about how they regret not joining and the \u201cboot camps\u201d they went to. \n\nI don\u2019t say this lightly, it\u2019s in my top 5 most \u201cwhat the fuck did I just walk into\u201d moments. \n\nThat said there\u2019s a few people I\u2019ve met over the years that were veterans who actively competed in ruck competitions. Those guys and gals absolutely loved doing it too."
      },
      {
        "id": "nl1ady4",
        "score": 100,
        "body": "[deleted]"
      },
      {
        "id": "nl21vkd",
        "score": 67,
        "body": "In 25 hours I went from Iraq to the United States. I hugged my family and then had a week to \"debrief\". Then I was sent home. I trained for years to be the heartless violent person Uncle Sam wanted me to be. I had to be that, violence was always an option and the best one, you were high fived and celebrated whenever you did something extremely violent. Then 25 hours later I'm home. \n\nNo class on how to react if some old guy cuts me in line at Wal-Mart. No class on how my body would react to things without my brain even thinking. Just sent out into the world to deal with it.\n\nWar was easy, coming home has been one of the hardest things I've ever done. I'm still not adjusted... I have all sorts of theories on how to make that transition better but in all honesty we're rewired and not meant to come back to society after what we did."
      },
      {
        "id": "nl16tda",
        "score": 59,
        "body": "I remember those guys. We followed them on Facebook throughout their journey. Some members of the GORUCK community actually met up with them near one of the east coast states."
      },
      {
        "id": "nl1nhdl",
        "score": 57,
        "body": "Get the military that causes these issues to provide better help for their services other than a PowerPoint you have to sit through by the driest person on planet earth or a shitty VA."
      },
      {
        "id": "nl12p4s",
        "score": 53,
        "body": "This is more like the nonsense from a few years ago about doing 22 pushups to bring awareness to military/veteran suicide - which accomplished nothing long term."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1k9ljfr",
    "title": "A thank you to this wonderful community!",
    "body": "This is my graduation cap! Commemorating my father, who passed during Operation Enduring Freedom. The cloth used was from one of my dad's uniforms that I inherited. You will no longer see the posts on my profile, but this community has been nothing but helpful and welcoming when I've come here with questions or struggles. Despite not being a vet myself, I have always received a warm welcome, and that means a lot to me. I wanted to say thank you! The only reason I can attend college is due to the diligent help I received when it came to the GI Bill; members of this sub even helped me find a plan to solve the debt that was unfairly placed upon me. Finally, my cap design was something I was only able to design after receiving some guidance on what was allowed and what wasn't. So, once again, thank you from the bottom of my heart to every member here for the sacrifices you've made, as well as the guidance and support you've given me. When I am walking at graduation, the people here will be among those I think of when being handed my diploma. ",
    "flair": "Discussion",
    "score": 557,
    "comment_count": 41,
    "created_at": "2025-04-28T02:56:59+00:00",
    "top_comments": [
      {
        "id": "mpfunfn",
        "score": 63,
        "body": "I'd love to share a memory I have, but I was born June 20th, a little under a month after he passed, not a story per se, but my entire family swears it's like he's here still. I had absolutely no idea how, but somehow, without anyone telling me, I ended up playing every sport he did in high school and the clubs he was in. Every single one. Entirely on accident. This is the one that cracks everyone up, we're both super happy and go-lucky people, high energy goofs, but style and clothing-wise, we randomly went hardcore alternative junior year. There's a picture of us at the same age, both rocking smudged eyeliner and distressed band tees. Pretty sure the alt look would have stuck with him and will stick with me."
      },
      {
        "id": "mpfg3pl",
        "score": 46,
        "body": "Congrats! This made my day. Cheers to you, your family, and your father \ud83c\uddfa\ud83c\uddf2"
      },
      {
        "id": "mpfi8sy",
        "score": 15,
        "body": "I'm glad! Thank you! :D"
      },
      {
        "id": "mpfrj1l",
        "score": 14,
        "body": "Can you tell us something about your dad?"
      },
      {
        "id": "mpg1ldq",
        "score": 14,
        "body": "It does, my grandparents especially get a little freaked out. I don't remember why, but I was telling a story, and my grandma got emotional and had to leave. I asked my grandpa what was wrong, and he said, \"It's just a little hard sometimes, we see you and sometimes it's your dad, our son, looking back.\" Most of the time, it's silly and not so heart-wrenching."
      },
      {
        "id": "mpg2n6o",
        "score": 11,
        "body": "Your father did this for you. I'm sorry you never met him, but he lives on through you. Congrats on your accomplishment OP. You know he'd be proud, and you should be too. Good luck in life."
      },
      {
        "id": "mpie9b4",
        "score": 11,
        "body": "Hello! I'm also an Army OEF veteran who served during the same period as your dad (2007\u20132011) and was around the same age as he was when he passed.\n\nI spend most of my time lurking here, but I wanted to take a moment and thank you for sharing this with us. Aside from the occasional Veteran's Day celebration, I haven't really gotten involved in anything military-related since leaving the service. That said, your post hit extremely close to home for me (and for others, too, I'm sure), especially since I'm now a father with a daughter of my own.\n\nI saw your dad is buried about twenty minutes away from me. With your and your family's blessing, I'd be honored to stop by and visit him sometime (he's on my commute home), and, with the weather getting warmer, I'd be more than happy to bring him flowers and/or a beverage of your choosing."
      },
      {
        "id": "mpfsj5z",
        "score": 8,
        "body": "What story about/memory of him gets everyone around the dinner table laughing about remembering again? Or that his friends have told you multiple times but you still pretend like it\u2019s the first time just to hear it again?"
      },
      {
        "id": "mpfrx00",
        "score": 7,
        "body": "Absolutely, what would you like to know?"
      },
      {
        "id": "mpfzpfa",
        "score": 6,
        "body": "That\u2019s an amazing amount of similarities to have shared with him!!! Does it trip your family out with each new thing that get added to the list?!"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1ntwmzn",
    "title": "VA STAFFER BLINDLY APPROVED 85,000 CLAIMS",
    "body": "VA STAFFER BLINDLY APPROVED 85,000 CLAIMS \n\n[https://www.militarytimes.com/news/your-military/2025/09/29/va-staffer-accused-of-blindly-approving-over-85000-disability-claims/](https://www.militarytimes.com/news/your-military/2025/09/29/va-staffer-accused-of-blindly-approving-over-85000-disability-claims/)",
    "flair": "Discussion",
    "score": 533,
    "comment_count": 368,
    "created_at": "2025-09-29T22:50:12+00:00",
    "top_comments": [
      {
        "id": "ngwvbj8",
        "score": 372,
        "body": "Well it wasn't any of mine....\nEdit:  you can check on your decision letters. It'll say what office it came out of, somewhere near the end of the stack of papers. For example my only one that fell within this time frame came out of the Florida regional office."
      },
      {
        "id": "ngwz1x7",
        "score": 237,
        "body": "What about the 8,000,000 that they blindly denied???"
      },
      {
        "id": "ngww0z9",
        "score": 97,
        "body": "Looks like they are going to cancel 85,000 approved claims made in 2024."
      },
      {
        "id": "ngwv05x",
        "score": 96,
        "body": "Between 2022-2024"
      },
      {
        "id": "ngww5c3",
        "score": 88,
        "body": "HAHAHA. Me either dude, me either \ud83d\ude06"
      },
      {
        "id": "ngx00r2",
        "score": 86,
        "body": "\"While it was known that the employee was firing off approvals at slapdash speed, the individual was backed strongly by supervisors in the regional office, who shielded them from being held accountable.\"\n\nLmao slapdash speed."
      },
      {
        "id": "ngwunz7",
        "score": 76,
        "body": "Good for that staffer."
      },
      {
        "id": "ngwwkji",
        "score": 73,
        "body": "In Philadelphia Regional."
      },
      {
        "id": "ngww9iq",
        "score": 65,
        "body": "This is how you reduce the backlog."
      },
      {
        "id": "ngx2mu5",
        "score": 51,
        "body": "Fly Eagles! \ud83e\udd85 Fly! \ud83d\ude07\ud83d\ude06"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1owfx89",
    "title": "Met a real life \u2018almost joined\u2019 today",
    "body": "Guy in his 60s came out to give me a quote on garage floor today. Seemed nice were talking he saw my veteran plates and then it began\u2026. How many benefits we get, how he almost joined and how he would have retired in 2002 and since it was before any wars he wouldn\u2019t have deployed and just did his time. When he said how great of a career choice it is for someone with no direction in life and then you\u2019re set up for life, honestly it felt offensive a bit. Tried to tell him a little bit sacrifice involved to get these benefits, but the almost joined of course knew better\u2026 anyway I thought these people were kind of made up, like are there really these not self aware individuals? Yeah there are! Not getting my business ! ",
    "flair": "Discussion",
    "score": 528,
    "comment_count": 178,
    "created_at": "2025-11-13T23:02:22+00:00",
    "top_comments": [
      {
        "id": "nopt0i8",
        "score": 306,
        "body": "Civilians cannot IMAGINE just the Garrison work, let alone Combat and Field Problems. There is  little in the civilian world that would even compare enough to grasp.\n\nNot really saying because it's tough, more like demanding and foreign. \n\nBeing property for 20 years is something I think people overlook lol."
      },
      {
        "id": "nopuz9s",
        "score": 177,
        "body": "I hope you almost thanked him; the man is a goddamn almost-hero."
      },
      {
        "id": "noq22g7",
        "score": 107,
        "body": "[deleted]"
      },
      {
        "id": "noptpul",
        "score": 93,
        "body": "Yeah, if I didn\u2019t show up to my civilian job I\u2019d get fired. If I didn\u2019t show up for duty I\u2019d go to prison."
      },
      {
        "id": "nopxdzu",
        "score": 92,
        "body": "Yeah, because every veteran out there is living like the Kardashians with that sweet VA compensation while juggling crippling depression and/or a broken body.\n\nSetup. For. Life."
      },
      {
        "id": "noqdw0y",
        "score": 73,
        "body": "Guy at work became a Marine in the early 80s. Did his 4 and got out. I became a Marine in 97, got out after 4. \n\nOne day at work a few people were whining because we were going to end up getting OT. Old guy and I started  swapping stories about BS we put up with. \n\nHaving to work late cause SSgt's wife was cheating on him and he didn't want to go home. Whole section having to work late cause one person had a bad attitude. Being out in the field for a few weeks straight. Being made to work on a Saturday cause someone fucked up. \n\nWe're laughing about it. Everyone is looking at us like we're crazy because that stuff is just funny to us years later. \n\nPeople stopped complaining about having to work OT around me after that. \n\nThey have no idea how much easier it is to be a civilian."
      },
      {
        "id": "nopz32w",
        "score": 57,
        "body": "My supervisor has always been a military/operator LARPer. Plays paintball and talks about it like he's clearing houses in Iraq. Dude has more camouflage than any two active duty bases combined. \n\nHe told me his almost veteran story the other day. Apparently, he was going to be Army special forces, but his mom tore up the contract. If only the technology existed to print up another copy. He's such a tool."
      },
      {
        "id": "nopusza",
        "score": 54,
        "body": "I worked nights, and one of the scariest moments of my military career was being woken up because I overslept for a meeting with a full bird. \n\nYeah, way different stresses in the military."
      },
      {
        "id": "nopzow4",
        "score": 44,
        "body": "LMFAO that was almost PERFECT. \ud83e\udd23"
      },
      {
        "id": "noqtjs3",
        "score": 42,
        "body": "I always like to talk them about UAs and how other men had to watch urine leave my dick directly into a cup."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1mxskvt",
    "title": "F--k cancer. Go get your shit checked out.",
    "body": "Subject line says it. I just got the word this week. I've got colon cancer, because of course it's the literal shittiest cancer (that's a joke, there are worse, but... you know, colon cancer... shitting. It's a joke. Get it? Rah).\n\nI started having some stomach issues a while back, and they weren't your usual 'hey, maybe I should eat less fried food' type shits, they were the 'I haven't had beats in a couple months and there's a lot of red, and it smells like a sewer when I fart' type shits. So that was a red flag.\n\nTook more convincing than I would have liked, but I was able to book a colonoscopy and endoscopy, and they ID'd it. Waiting for a more full scan to gauge spread -- getting that next week -- but the main point of this post is: Trust your gut (yes, another joke) and if your shits (heyoo) are suddenly different, listen to your body and get checked out.\n\nI'm 38 and while I'm a fat, nasty ass civilian these days, I'm not so utterly unhealthy that I think this is entirely a 'me being a dumbass' type thing. Between this and some other health issues that are frankly abnormal for my age and medical history, I'm thinking there's more to this than my own poor barracks and 20s life choices, and probably due (at least in part) to the two deployments to Helmand, where burning shit and JP-8 were our daily air freshener.\n\nOnce I get the final results from my doctors, I'll be heading to the VA to do a screening with them and I'll be filing for care and benefits under the PACT Act. I'm optimistic that this was likely caught early, but I did want to share it because for those of us who came up during GWOT... this sort of crap (there I go again) is something we've gotta look out for.\n\nSo, get yourself checked out. Take care of yourself, and if you end up in the same boat: Reach out to your buddies, get your support network in place, and if you need to (as I do, right now), find a place to just vent this shit so you can get it out.\n\nThanks for hearing me out.\n\n*\\[I copy/pasted this over from the USMC subreddit because 1. I'm an old out-of-touch old fart and don't know if there's a more efficient way to do this. 2. I think the 'hey, check yourself out' reminder is something we all need. I certainly did. 3. I'm in a rough spot, and, selfishly, I could use the random kindness and well wishes from other belligerent shitheads like me online. 4. I also had to copy-edit this to remove all the f---s, which was a* ***lot*** *of work.\\]*",
    "flair": "Question/Advice",
    "score": 508,
    "comment_count": 106,
    "created_at": "2025-08-23T05:02:19+00:00",
    "top_comments": [
      {
        "id": "na7fzc0",
        "score": 88,
        "body": "Well, shit."
      },
      {
        "id": "na7h7bb",
        "score": 73,
        "body": "We need to have screenings earlier. I was in my early twenties when they found pre cancerous polyps that would have likely developed into cancer by the time I was due for a routine colonoscopy. I\u2019m now on a 3-5 year schedule. \n\nI\u2019m sorry to hear about your diagnosis, OP."
      },
      {
        "id": "na7jjfa",
        "score": 30,
        "body": "If you have to have surgery, will they at least leave you a semi colon? Aww I'm sorry that was a crappy joke. I'm turdally out of line. I better log out for a while. You know why turds are tapered at the end? Because if they weren't, your asshole would slam shut! \nSeriously though, three time cancer survivor here. You need to talk with someone who has gone through it, hit me up. You're not alone brother."
      },
      {
        "id": "na8trth",
        "score": 17,
        "body": "I personally went and got checked the first time I went for one because there was a family history on my mom's side. At the time, my mom was looking at having a large part of her colon removed and needing a colostomy bag for the rest of her life at 56. Her Dr. recommended I and my brother should both be checked. \n\nI was 36 when I went for my first colonoscopy, and it took some convincing the Dr. that I needed one at that age, I had 3 polyps removed and was scheduled for my next one at 39 where everything was clean (as clean as it could be).\n\n\nMy second colonoscopy was in the VA. My PCP (VA Dr.) scheduled some genetic testing for me at UK in Lexington, which screened for predisposition for some cancers but also came with the option that if i had genetic markers member's of my family could be screen for it free as well. All this to say, get checked. If you are the VA system, talk to your PCP about genetic testing if not for you do it for the people you care about, do it for the people who care about you, and if you feel you don't have that I care about all of you.\n\nI worry about my brother because he doesn't go to the Dr. for anything, he left the emergency room with chemical burns on his leg and worked for 3 days before he went back and was hospitalized to have a skin graft.\n\nOP, I hope everything works out for you.\n\n(Also, I am not a Dr. if the terminology I used is incorrect, don't hang me for it.)"
      },
      {
        "id": "na8adhe",
        "score": 16,
        "body": "Don't wait on the claim at the very least submit an intent to file. Benefits go back to the earliest filing date not the date of a diagnosis. An intent to file holds the effective date to the day you submit the intent to file.for up to 1 year. Get it done by the end of the month and you will be be paid for this month. Life might get hectic for you once treatment starts.\n\nTake care of yourself! That includes getting paid."
      },
      {
        "id": "naabshu",
        "score": 16,
        "body": "Cancerous shit if I may"
      },
      {
        "id": "na7j12h",
        "score": 13,
        "body": "Just booked my appt at the VA last week. Definitely getting checked just because. Been seeing it hit you a lot of people lately"
      },
      {
        "id": "na8blrl",
        "score": 12,
        "body": "Thank you so much for posting this. We were exposed to SO MUCH, we\u2019ll be finding out for years to come, but yes, early detection is key. I was diagnosed with breast cancer in 2019 but caught it super early, stage zero, and had a minor surgery and took a preventative medication. I remain vigilant. This was caught through a routine mammogram and my family has no history of breast cancer. \n\nI was in Maiwand, just between Kandahar and Helmand, 2009-2010. We burned so much trash, and a shit ton of heroine (I know how to spell, fucking computer won\u2019t allow it without the e) we seized. The VA deemed my breast cancer NOT service connected but I\u2019m willing to bet that will change in the future. I know breast cancer incidence in military women is extremely elevated. \n\nGet your screenings. It\u2019s important. If not for you, then for the people in your life you love - because it\u2019s not just about you. All the best to you Brother and thank you again for reminding us all."
      },
      {
        "id": "na7znu1",
        "score": 9,
        "body": "Why did you get checked out in the first place?"
      },
      {
        "id": "na85fxo",
        "score": 8,
        "body": "??? The person you replied to wasn\u2019t asking the original poster, but a commenter."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1lzmvud",
    "title": "This Barbie holding a gun at my VA has me cracking up.",
    "body": "Orlando VAMC at Lake Nona",
    "flair": "Discussion",
    "score": 507,
    "comment_count": 32,
    "created_at": "2025-07-14T13:48:56+00:00",
    "top_comments": [
      {
        "id": "n330tgq",
        "score": 108,
        "body": "Disgruntled Veteran Barbie is seriously done with your shit."
      },
      {
        "id": "n330ihj",
        "score": 58,
        "body": "Man. They are really serious about vaccinations there."
      },
      {
        "id": "n339ien",
        "score": 38,
        "body": "I bet it was \"We have determined your PTSD is not service related.\""
      },
      {
        "id": "n33h51a",
        "score": 27,
        "body": "We have an amputee Barbie at my VA \ud83e\udd23"
      },
      {
        "id": "n34cs8e",
        "score": 14,
        "body": "*whoosh*"
      },
      {
        "id": "n33p5yc",
        "score": 11,
        "body": "She's pointing out from behind the check in desk like she's gonna sh\u00f8\u00f8t you as you're checking in."
      },
      {
        "id": "n33ujsq",
        "score": 11,
        "body": "How can even see her?"
      },
      {
        "id": "n34k9c4",
        "score": 10,
        "body": "*\"Say something about the wait. I dare you...\"*"
      },
      {
        "id": "n331flv",
        "score": 8,
        "body": "Yeah you don\u2019t want to get the LU!"
      },
      {
        "id": "n36ci8e",
        "score": 7,
        "body": "Happens more than you think."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1mbyi16",
    "title": "vehicle update",
    "body": "i posted about a week ago asking for car buying advice. just wanted to share in case anyone cares:\n\nso i was hunting and calling dealerships for info all week looking for the best deals as far as year/mileage/price and all that combined. i was set on a toyota rav4 (dream vehicle for as long as i can remember) \n\ni found a unicorn deal on wednesday and went back and forth until yesterday afternoon. this is the final breakdown-\n\n2024 Toyota Rav4 14k miles otd- $28,432\n\nI put $22,000 down and financed a little over 6k for 36 months for the sake of establishing good credit history. \n\nplease don\u2019t lecture about blowing all my money at once\u2014 i paid off all debt and still have plenty left over after the down payment/tags/tax/title/insurance\n",
    "flair": "Discussion",
    "score": 501,
    "comment_count": 143,
    "created_at": "2025-07-29T01:29:00+00:00",
    "top_comments": [
      {
        "id": "n5px33g",
        "score": 183,
        "body": "[deleted]"
      },
      {
        "id": "n5qbacv",
        "score": 60,
        "body": "lol ik i look like a boot but idk what to do with my hands\ud83d\ude02"
      },
      {
        "id": "n5pxpr1",
        "score": 34,
        "body": "Only way people can shit on you for paying the car outright is if they offered like 0% interest and you didn't take it even though you wanted to build history.\n\nBut in this environment, no one is offering that anymore and its closer to 5%-6% with excellent credit. The only company offering 0%-2% is Subaru from my understanding and I think that has to do with hurt sales and trying to get some movement going on their cars in lots.\n\nCongrats on the vehicle purchase. I had the old school RAV4 back when it was only a 2-door. Fun little vehicle back then and can't really go wrong with Toyota reliability.\n\nAnd if that price is all they would negotiate out and you're happy with it to sign, then that's all there is to it.\n\nEdit: Just added last last sentence."
      },
      {
        "id": "n5qew9p",
        "score": 34,
        "body": "women\u2019s pockets do not"
      },
      {
        "id": "n5q1szd",
        "score": 22,
        "body": "My mom has a 2005 Rav 4, that shit won't die \ud83e\udd23"
      },
      {
        "id": "n5q696o",
        "score": 19,
        "body": "You know when your dream car is a Toyota RAV4 you have a pragmatic mind and reasonable goals."
      },
      {
        "id": "n5qsqe8",
        "score": 18,
        "body": "It took me 8 years to break that habit\nGood luck with that"
      },
      {
        "id": "n5pylba",
        "score": 16,
        "body": "lol. Good catch. One hand holding up keys, other hand with thumb along the trouser seam."
      },
      {
        "id": "n5puxd2",
        "score": 15,
        "body": "Nice, I have a 2023 RAV4. Did a road trip and put over 10K milage in the first two months"
      },
      {
        "id": "n5qesev",
        "score": 14,
        "body": "Pockets exist, friend.\n\nAnd with the RE-1A protection, nobody yells at you for putting them in there."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1jpcmqf",
    "title": "WOW anybody else receive this?",
    "body": "About sht my pants ",
    "flair": "Question/Advice",
    "score": 479,
    "comment_count": 76,
    "created_at": "2025-04-02T01:25:46+00:00",
    "top_comments": [
      {
        "id": "mkz0cw1",
        "score": 152,
        "body": "I would send them back a BIR.pdf that's just pictures of my ass on a scanner."
      },
      {
        "id": "mkzslug",
        "score": 144,
        "body": "I'd end up in the ER i'd bust a gut so hard! I'm 11 years out, 30 lbs over weight, and at my age if you ever see me running... You should probably be running, too!"
      },
      {
        "id": "mkyz8vh",
        "score": 132,
        "body": "this is amazing"
      },
      {
        "id": "ml006sl",
        "score": 93,
        "body": "He\u2019s a marine. The fact he got that much right is outstanding"
      },
      {
        "id": "mkz061e",
        "score": 72,
        "body": "You can legally goatse someone for this."
      },
      {
        "id": "mkzqylj",
        "score": 51,
        "body": "[deleted]"
      },
      {
        "id": "mkz00qo",
        "score": 48,
        "body": "\ud83d\ude02\ud83d\ude02\ud83d\ude02\ud83d\ude02 that was a good one."
      },
      {
        "id": "mkyzcoc",
        "score": 46,
        "body": "Some things you just don't joke about. I think this might be one of em."
      },
      {
        "id": "ml0ld0t",
        "score": 45,
        "body": "As someone that got pulled off IRR then stop lossed in theater, I'd probably lose my shit"
      },
      {
        "id": "ml12s9l",
        "score": 42,
        "body": "Lmfao! I was thinking something similar. Say \u201cHello, thanks for the notification, please see the attached documents.\u201d Just straight cheeks scanned."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1kw1nwy",
    "title": "It\u2019s not much, but it\u2019s my tradition. What is your Memorial Day tradition?",
    "body": "Every Memorial Day I find an open pub or bar and buy 2 beers. 1 for me, and 1 for the four names on the top of the list in the photo since I served with them. I ask the bar keep to leave the beer and paper on the bar the rest do the day. I don\u2019t have a printer that can print color anymore so I\u2019m trying a new thing. This way people can add names to the list and have a beer with the fallen. It\u2019s not much, but this is my tradition. ",
    "flair": "Discussion",
    "score": 469,
    "comment_count": 88,
    "created_at": "2025-05-26T18:26:23+00:00",
    "top_comments": [
      {
        "id": "mudy4yu",
        "score": 64,
        "body": "I hide in my house and avoid Facebook, so I dont see who lost the battle this year."
      },
      {
        "id": "mudunt2",
        "score": 63,
        "body": "I have a notebook. Big fan. \n\nBar & Pint not so much. Sober since May 2024"
      },
      {
        "id": "mue42k8",
        "score": 59,
        "body": "This is pretty cool. I have a name if you don't mind,\n\nCpl. Aleina Ramirez, US Army, 3ID, Killed by a rocket attack on FOB Dagger. Tikrit, Iraq. 15 April 2005"
      },
      {
        "id": "mue4h20",
        "score": 26,
        "body": "I will add to the list while I\u2019m still sitting here. Thank you!"
      },
      {
        "id": "mudxtu3",
        "score": 25,
        "body": "USN- AMS3 Wendy Pankow. 11/11/1997, NAS Sigonella Sicily"
      },
      {
        "id": "mudw8ou",
        "score": 23,
        "body": "Congrats on your sobriety. I rarely drink, but I definitely have one on Memorial Day. This is what we did while I was in, so I continue it."
      },
      {
        "id": "mudzzqs",
        "score": 22,
        "body": "Jimmy Stewart Willoughby USMC KIA 05/29/1968. Gone but not forgotten"
      },
      {
        "id": "mudz57k",
        "score": 17,
        "body": "I don\u2019t blame you there"
      },
      {
        "id": "mudz6aw",
        "score": 15,
        "body": "Love the tradition, I normally go on a run and do 1 mile for each of my boys, and follow it with a beer when I get home."
      },
      {
        "id": "mue4f7i",
        "score": 14,
        "body": "I 3D printed 80 poppies in honor of the 80th anniversary of the end of WWII and placed them around the yard with my \"deer\", which are decorated year round. \nWe don't \"do\" most holidays, but we did decide homemade Philly cheesesteaks are a nice homage to the birthplace of liberty."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1pf10et",
    "title": "Salty and Angry old vets",
    "body": "Never understood this attitude. When the war was going on I was in grade school. I\u2019m sorry I never got into a gunfight. ",
    "flair": "Discussion",
    "score": 462,
    "comment_count": 410,
    "created_at": "2025-12-05T17:24:17+00:00",
    "top_comments": [
      {
        "id": "nsgrgbz",
        "score": 371,
        "body": "0/10 ragebait"
      },
      {
        "id": "nsguw8z",
        "score": 195,
        "body": "Nobody hates veterans as much as veterans."
      },
      {
        "id": "nsguvak",
        "score": 170,
        "body": "I'm a sorta old vet, 63. That's why I stay away from VFW and AL.  Just a bunch of angry, old, whining bastards drinking beer and living in the past."
      },
      {
        "id": "nsh08gd",
        "score": 123,
        "body": "They got me bro \ud83d\ude2d\ud83e\udd40\ud83e\udd40"
      },
      {
        "id": "nsh0h3a",
        "score": 121,
        "body": "I promise those that actually have seen combat give zero fucks about anybody else or what those others did and mostly just want to be left alone to live in peace."
      },
      {
        "id": "nsh1dto",
        "score": 118,
        "body": "I love when these guys show up.  It makes it easier for me to avoid them like a venereal disease on liberty."
      },
      {
        "id": "nshf1r5",
        "score": 79,
        "body": "I looked into joining our local vfw with my dad. They weren't very open to new members. We both agreed it wasn't a good fit for us. And they wonder why nobody's joining..."
      },
      {
        "id": "nshiggx",
        "score": 73,
        "body": "[removed]"
      },
      {
        "id": "nsgrirq",
        "score": 71,
        "body": "They seem insecure"
      },
      {
        "id": "nsgw0eg",
        "score": 71,
        "body": "I'm a combat vet and I'd tell anyone like this to fuck off."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1kfwy7z",
    "title": "Green Beret attempts escape from MILMAX Prison - fails epically.",
    "body": "Context:\n\u201cThis is former SSG Mason Wollersheim, formerly a Green Beret with 10th SFG.\nOn 31 January 2025, at a general court-martial convened at Fort Carson, CO, SSG Mason L.\nWollersheim, U.S. Army, was convicted by a military panel composed of officers and enlisted members, contrary to his pleas, of one specification of broadcasting an indecent recording, three specifications of attempted larceny, one specification of wire fraud, and one specification of larceny in violation of Articles 80, 121, 134, and 120c, UCMJ.\nThe accused was acquitted of one specification of indecent recording, one specification of extortion, one specification of assault consummated by battery, and one specification of false official statement in violation of Articles 120c, 127, 128, and 107, UCMJ. The military judge sentenced the accused to be reduced to the grade of E-4, to be confined for 28 months, and to be discharged from the service with a bad-conduct discharge.\nAfter being found guilty he tried to run and was tased by the MPs at Fort Carson.\nApparently last Thursday, he tried to escape Leavenworth. This is where they found him.\u201d\n\nSources:\n\nhttps://www.jagcnet.army.mil/ACMPRS/cases/df85dfa8-fe49-448a-8007-c063f897554f",
    "flair": "Article/News",
    "score": 461,
    "comment_count": 124,
    "created_at": "2025-05-06T05:30:14+00:00",
    "top_comments": [
      {
        "id": "mqv2s87",
        "score": 244,
        "body": "You're not supposed to use SERE training for this lmao"
      },
      {
        "id": "mqv4zbc",
        "score": 131,
        "body": "Really looking forward to the recasting of this person as a badass operator, unfairly railroaded by scheming politician-officer types and fighting to clear his name."
      },
      {
        "id": "mqvm4eq",
        "score": 115,
        "body": "My man couldn\u2019t be confined in a military prison for 28 months? I think CQ and shit details as an E4 could prepare anyone for that."
      },
      {
        "id": "mqvcrky",
        "score": 70,
        "body": "Mark Wahlberg already signed for the movie rights."
      },
      {
        "id": "mqv9fk4",
        "score": 68,
        "body": "Looks like he was submitting fraudulent insurance claims and double dipping on tuition assistance and GI Bill."
      },
      {
        "id": "mqveits",
        "score": 63,
        "body": "I've closely known two serious special forces guys.    \n\n\n\nOne was a true american hero, the finest man Ive known. The other was the devil, a mean, nasty crooked devil.   \n\n \n\nThese guys are extreme"
      },
      {
        "id": "mqv5nv2",
        "score": 47,
        "body": "What did he do, in non legal-ense please"
      },
      {
        "id": "mqvjv17",
        "score": 47,
        "body": "lol \\*movie trailer voice\\*\n\n*Mason Wallersheim was a Green Beret... They tried to take his freedom... Mark Wahlberg in.... Concertina Pants*"
      },
      {
        "id": "mqvkvtw",
        "score": 47,
        "body": "He didn\u2019t hear a damn word of that safety briefing."
      },
      {
        "id": "mqw60wg",
        "score": 43,
        "body": "Pretty sure they still make you split rocks at Leavenworth. I never had to do that as an E4. \n\nEither way, a discharge like that means his opportunities for a successful life after discharge are slim at best. Prison break won't make that reality any worse."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1oa54bp",
    "title": "Getting a dog for PTSD and life.",
    "body": "I just picked up Zoe today. I am an army vet with PTSD and some days I just want to not be sad.\n\nI am so happy! I have never loved anything this much before (people especially included).",
    "flair": "Discussion",
    "score": 454,
    "comment_count": 63,
    "created_at": "2025-10-18T19:37:21+00:00",
    "top_comments": [
      {
        "id": "nk7tgup",
        "score": 57,
        "body": "My baby is one of my big motivators for getting out of bed everyday"
      },
      {
        "id": "nk7urup",
        "score": 28,
        "body": "I don\u2019t know if I\u2019ll get to sleep tonight yet. But she\u2019ll be a great reason to wake up!"
      },
      {
        "id": "nk7van9",
        "score": 23,
        "body": "Yup. She has peed inside twice already. Fortunately, I don\u2019t have any carpet.\n\nEdit: She just pooped outside! Partay!"
      },
      {
        "id": "nk7yv1a",
        "score": 19,
        "body": "I just got one last year, gave me a reason to get out of my bed or couch many times throughout the day and focus on my buddies needs over my anxiety (PTSD) and depression! Best wishes!!"
      },
      {
        "id": "nk7uyza",
        "score": 18,
        "body": "Just get used to cleaning pee and poop for a bit but they are worth all the trouble"
      },
      {
        "id": "nk84ykp",
        "score": 15,
        "body": "Bad idea. No good. Better let me have her \ud83d\ude09"
      },
      {
        "id": "nk8ahda",
        "score": 13,
        "body": "As noted below: she has almost exclusively peed in the house today (day 1), but she pooped outside and we had a party! \ud83c\udf89\n\nShe then tried to eat her poop, but progress is progress."
      },
      {
        "id": "nk7p0s2",
        "score": 13,
        "body": "Yes. Having a dog is a commitment. But having something outside of me to care about is important to me."
      },
      {
        "id": "nk7r297",
        "score": 12,
        "body": "Cute little stinker"
      },
      {
        "id": "nk85n49",
        "score": 9,
        "body": "They absolutely help, a lot.  Mine isn\u2019t a bonafide service dog, but seeing her big dumb face bring me her ball or just put her nose on the arm of my chair for a scratch and being completely content to nap beside my chair. They are totally worth it."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1pgvtxf",
    "title": "Any Utah veterans looking to play Magic The Gathering?",
    "body": "Greetings, I'm trying to put together an in-person MTG veteran group in the Northern Utah area. I'm happy to host and provide cards for new players. \nIf you're in the area and looking to make some new friends, please reach out. ",
    "flair": "Question/Advice",
    "score": 455,
    "comment_count": 129,
    "created_at": "2025-12-07T22:38:14+00:00",
    "top_comments": [
      {
        "id": "nsubhi6",
        "score": 165,
        "body": "I don\u2019t live in Utah nor do I play MTG, but I just wanted to say that\u2019s a sick hobby room and hopefully you find some vets to put a good group together."
      },
      {
        "id": "nsucqwr",
        "score": 39,
        "body": "Dude why arent you in CT!!!!"
      },
      {
        "id": "nsu9qjx",
        "score": 30,
        "body": "I should mention that I don't charge anything. I just enjoy spending time with fellow vets."
      },
      {
        "id": "nsufudr",
        "score": 27,
        "body": "Thank you."
      },
      {
        "id": "nsuf2qe",
        "score": 20,
        "body": "If you lived in Vegas we could play D&d \ud83d\ude1e"
      },
      {
        "id": "nsvc646",
        "score": 16,
        "body": "Hey OP, I am a vet, I do play MTG, but I am in NY.   However, I\u2019d always be down to play online on MTG Arena."
      },
      {
        "id": "nsucvjt",
        "score": 15,
        "body": "I don\u2019t live there or play MTG but I wanna come. Nice set up"
      },
      {
        "id": "nsut5wd",
        "score": 15,
        "body": "Oh shoot another ct person I play magic in enfield at a lgs there super nice"
      },
      {
        "id": "nsuez52",
        "score": 12,
        "body": "You play Commander? I\u2019m in the SLC area and only really play Commander with relaxed rules\nEdit: I am concerned though since I have a large German Shepherd service dog who gets along with all dogs so dunno how yours would be?"
      },
      {
        "id": "nsufpio",
        "score": 12,
        "body": "That is how my buddies and I love to play. I'm down to host or travel if you want play a few games and shoot the breeze."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1p89vci",
    "title": "Unaccompanied Veteran Funeral, Killeen, Texas, Dec 3",
    "body": "",
    "flair": "Article/News",
    "score": 454,
    "comment_count": 30,
    "created_at": "2025-11-27T18:47:24+00:00",
    "top_comments": [
      {
        "id": "nr3isz7",
        "score": 169,
        "body": "Unaccompanied means no friends or family could be located to attend the funeral. Therefore, the public is invited to ensure this veteran is not alone."
      },
      {
        "id": "nr3nbmy",
        "score": 133,
        "body": "There should be a service to alert other veterans about situations like this.  I mean he should have never been alone to begin with but fuck."
      },
      {
        "id": "nr3okor",
        "score": 39,
        "body": "I concur. I'd love to be there for them, as they were there for the country.\n\nIf there's a specific way to be notified I hope it gets posted here!"
      },
      {
        "id": "nr3ilih",
        "score": 31,
        "body": "How do I get on this email or notification list? I would love to participate in my area"
      },
      {
        "id": "nr3t43q",
        "score": 28,
        "body": "I did find this! I emailed the organization about a notification list and if they do send outs.\n\nAlso there's a calendar of events. \n\nhttps://www.miap.us/calendar?y=2025&m=12#ss-block-container-33\n\nSorry to piggie back your comment twice. Since I commented and found it I thought I'd share here through it"
      },
      {
        "id": "nr3kf1j",
        "score": 21,
        "body": "We don't normally allow links to social media, but I will make an exception as you are directing them to where you found this. Here is some more info on the program.\n\n  \n[https://news.va.gov/126762/burial-and-honor-for-unclaimed-veterans/](https://news.va.gov/126762/burial-and-honor-for-unclaimed-veterans/)\n\n  \n[https://www.cem.va.gov/burial-memorial-benefits/unclaimed-Veteran-remains.asp](https://www.cem.va.gov/burial-memorial-benefits/unclaimed-Veteran-remains.asp)"
      },
      {
        "id": "nr3jfvf",
        "score": 16,
        "body": "This was posted on the U.S Army W.T.F! moments Facebook group.  \nhttps://www.facebook.com/usawtfm  \n<edit> it's also on their Instagram page.  \n\nI don't know of any regular notification list for such things. It's just random if someone posts it to the right place and it goes viral."
      },
      {
        "id": "nr3zr6i",
        "score": 15,
        "body": "Someone please reach out to the VFW or Legion Riders in this area to give this fellow a proper send off."
      },
      {
        "id": "nr3vvjp",
        "score": 15,
        "body": "Another reply above, someone found this site:  \nhttps://www.miap.us/calendar?y=2025&m=12#ss-block-container-33"
      },
      {
        "id": "nr3zu2m",
        "score": 9,
        "body": "Bless his soul"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1ou76dj",
    "title": "Happy Veterans Day in Heaven, Uncle T!",
    "body": "I come from a long line of military men!  I couldn\u2019t post all their pictures here. But they shaped me into the woman I am today. Taught me resilience and courage through the struggle and storms of life. \n\n",
    "flair": "Discussion",
    "score": 453,
    "comment_count": 14,
    "created_at": "2025-11-11T11:35:45+00:00",
    "top_comments": [
      {
        "id": "no9nmo6",
        "score": 5,
        "body": "Semper Fi!"
      },
      {
        "id": "no9tcju",
        "score": 4,
        "body": "Semper Fi! \n\nAlso your uncle looks like Mr Milcheck in this picture"
      },
      {
        "id": "no9z784",
        "score": 3,
        "body": "May he rest in power."
      },
      {
        "id": "noa2smr",
        "score": 3,
        "body": "I don\u2019t think i have ever seen a Gunny smile like that."
      },
      {
        "id": "nocmasf",
        "score": 3,
        "body": "Marines do have the best dress uniform of all the branches, hands down."
      },
      {
        "id": "noa59j7",
        "score": 2,
        "body": "Slow Salute!"
      },
      {
        "id": "noa7i7e",
        "score": 2,
        "body": "A day later but Happy Birthday GSgt."
      },
      {
        "id": "nodgvje",
        "score": 2,
        "body": "Thank you Uncle \u201cT\u201d."
      },
      {
        "id": "nom1eoa",
        "score": 2,
        "body": "Uncle Gunny!"
      },
      {
        "id": "noakr41",
        "score": 1,
        "body": "Rest in peace and Semper Fidelis\u00a0"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1mr9l18",
    "title": "The VA summed up in 1 picture",
    "body": "",
    "flair": "Health Care",
    "score": 434,
    "comment_count": 169,
    "created_at": "2025-08-15T20:36:52+00:00",
    "top_comments": [
      {
        "id": "n8wnhsd",
        "score": 128,
        "body": "You gotta respond faster duh"
      },
      {
        "id": "n8wr8bq",
        "score": 97,
        "body": "Your sniper-like reflexes aren't what they once were"
      },
      {
        "id": "n8wo4au",
        "score": 85,
        "body": "They had an opening. They texted a few people to see if anyone wanted to move up their appointment. Someone else replied before you did."
      },
      {
        "id": "n8wv98g",
        "score": 68,
        "body": "Out of all the shitty things the VA does, this isn\u2019t one of them. It was first come first serve and he wasn\u2019t first."
      },
      {
        "id": "n8wzj8a",
        "score": 49,
        "body": "1 minute too late lmao \ud83e\udd23"
      },
      {
        "id": "n8wrfab",
        "score": 45,
        "body": "OP was too busy posting on reddit to reply to the appt lol."
      },
      {
        "id": "n8x6hba",
        "score": 25,
        "body": "Someone's a bit testy.... tsk tsk tsk"
      },
      {
        "id": "n8wzauw",
        "score": 18,
        "body": "Lol literally got this exact same text and responded within 30 seconds and it was still like, gotcha!"
      },
      {
        "id": "n8xk125",
        "score": 18,
        "body": "That's all it takes. I'd have slid in over you too, no offence."
      },
      {
        "id": "n8x8nzs",
        "score": 18,
        "body": "Teste*\n\n(He called you numb nuts)"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1lkxth8",
    "title": "Quick Veteran \"shower thoughts\"",
    "body": "Directed at GWOT Veterans:\n\n1.) No civilian gives a f about us nor even will care or try to understand.\n\n2.) Family and/or those closest to you are often the ones who are jealous/hate you the most. All the rappers/hip-hop artists we grew up listening to were correct in their lyrics that they tried to warn us about.\n\n3.) Blue collar civilians and supposed \"patriots\" are quick to scoff at Veteran problems, diminish their issues, and would be the first to push for taking our benefits away. Gun enthusiasts/tactical bro's are the worst types.\n\n4.) I've known 3 people who killed themselves who I deployed with. One of them my own former soldier...... Civilians I've spoken to; including family, about this, as I bring up statistics on post 9/11 sucides etc;  use verbiage and phrases to insinuate that we are weaker than WW2 or Vietnam vets.........\n\n5.) COPS are in no way shape or form equivalent to Veterans.\n\n6.) Sometimes Veterans from other branches and or the same branch are our own worse enemies. A lot of jealousy and hatred towards other branches just because they deployed or were in combat and you weren't. This is dumb.\n\n7.) The VFW/American Legion/JWV is going to continue to lose more Veterans if they do not adapt and change. Caveat to this: Officer position's in these organizations should NOT depend on the individual actually being a prior-Officer. It's dumb. These organizations do not speak loud enough for us Veteran's in Congress.\n\n8.) As we get older those who deployed multiple times in GWOT era and the things we were exposed to is going to be revealed/get worse. We are ticking time bombs. Cancers, PTSD, sleeping issues, microplastics, and breathing issues/OSA; all related but not publicly acknowledged or studied. We need more of a spotlight on this. Looking at you Veteran organizations.",
    "flair": "Discussion",
    "score": 427,
    "comment_count": 133,
    "created_at": "2025-06-26T11:34:11+00:00",
    "top_comments": [
      {
        "id": "mzv9v6z",
        "score": 140,
        "body": "I want to disagree with this so much, but can't."
      },
      {
        "id": "mzvadtr",
        "score": 85,
        "body": "People in general tend to be very insecure and jealous. Veterans are perceived as receiving special treatment from society and overly generous benefits. This is why you\u2019ll almost never find a civilian who can empathize with veteran issues."
      },
      {
        "id": "mzvddxd",
        "score": 59,
        "body": "Same.\n\n2 - Family... Ugh!! I love how my Mother thinks she's a bigger Patriot than me because she always voted for Republicans and way he's Fox News. When I try to have a conversation with my parents, it's a brick wall. They won't get mad when the VA endures funding cuts, but are constantly telling me to go see a VA counselor to deal with my 'anger issues'. (DON'T VOTE FOR THE GASCIST CRIMINAL AND I PROBABLY WON'T BE ANGRY, MOM!!!)\n\ud83d\ude06 - Yeah, we all have our issues \n\n3 - Very similar situation to number two, but these are Union guys who think I get 'free everything' on their tax dime. I have to correct them that I'm not Jeff Bezos or a Walton family member... Also, even though I have guns, most people with them should never be allowed within twenty meters of one. We all know someone we served with who wasn't allowed near the armory for any number of reasons, but these same people can go buy even deadlier weapons online now.\n\n5 - Seriously?? You'd put the fat-ass booger picken' Deputy who got that job because his uncle is the Mayor in the same category as the men who stormed Omaha Beach or Tarawa, the men who went toe-to-toe with the IJN's Southern Force in Taffy 3 or fought house to house in Italy, Fallujah or Hue City???\n\n6 - I may give my Brothers and Sisters in the US Chair Force crap for those immaculate bases and cushy living, but I also have mad respect for someone flying a bomber with the RCS of the Great Pyramid of Giza that happens to be eligible for social security! Sure they deployed to Saudi with the rest of us, but back when the Patriot system was first introduced it was still easier to move a ship than move an airbase when SCUDs were incoming."
      },
      {
        "id": "mzvku67",
        "score": 43,
        "body": "I feel like it\u2019s not my place to interject here, but as a civilian, I just wanted yall to know I don\u2019t at all think you receive \u201cspecial benefits.\u201d I think everything yall get is the *minimum* of what you are due - worked for, earned. \n\nI can\u2019t say you\u2019re wrong about how most people feel, and maybe my impression is colored by the fact that my dad was in Vietnam and I\u2019m with him at the VA all the time, and talk to a lot of Veterans,\n\nand I do think you\u2019re dead on, that that\u2019s a natural instinct, when someone else appears to be getting something you aren\u2019t, to be jealous of it. I can totally believe that is an unconscious feeling most people have. Even more, I feel like people would just rather ignore Veterans entirely and not have to think about any of this, and that it just so happens that\u2019s very easy to do. \n\nBut I just wanted you to know some folks see it how it is - you are not being given anything you didn\u2019t earn, it\u2019s compensation. I don\u2019t feel competitive or jealous of that, bc I didn\u2019t work and sacrifice to earn that stuff. What many of you go through after you are no longer active, that\u2019s also got to be compensated imo."
      },
      {
        "id": "mzwf76r",
        "score": 36,
        "body": "Ugh number 2 resonates too much with me. \n\nMy family didn\u2019t just avoid serving in Vietnam, they actively deterred me from joining the military. I mean not to the point where they offered their support in anything that would have kept me from service, but everyone told me how bad of an idea it was. \n\nThen I get home from boot camp and everyone has a \u201cMom/Dad/Aunt/Uncle of United States Marine\u201d t-shirt or bumper sticker, they\u2019re all flexing MY service for their friends and community members like they did anything, and then the minute I say I don\u2019t agree with them politically, they accuse me of not being patriotic. Ironically, my cousin who served in the Army and I are both very aligned politically, and they say both of us aren\u2019t patriots. Were the only ones who actually served in the military though. You don\u2019t get to tell people who voluntarily signed up to serve their country during war that they don\u2019t love the country just because they believe in things like constitutional rights."
      },
      {
        "id": "mzvd2hk",
        "score": 29,
        "body": "One big thing is that we are literally trained and have had our brains rewired from psychological conditioning - in ways that they didn\u2019t used to do\n\nhttps://a.co/d/2mugHoN \n\nOn Killing - the psychological costs of learning to kill in war and society \n\nWe are literally brain washed and programmed differently so we are more effective in war.  In ways those WW2 soldiers were not."
      },
      {
        "id": "mzvfmwl",
        "score": 29,
        "body": "I was thinking about this a lot the other day\u2026my friends and I would joke about when we knew we were brainwashed, and we all had the same answer: when standing in a giant platoon size formation at Ft. Benning shouting \u201cKill Kill Kill\u201d and answer \u201cBlood Makes the Green Grass Grow\u201d as we thrust out bayonets into imaginary enemy. \n\nThe truth is that a small percentage of people in our society are trained, unabashedly, to kill another person. An even smaller percentage of that group is trained as their primary job within the military to kill another person and do it effectively and without prejudice. \n\nEven if you never pulled the trigger, if you were deployed in a combat zone and were put in situations where that was a possibility, then your brain and psyche are not the same as they were before. \n\nThere\u2019s something smart to be said about all that, but I guess I\u2019ll need to read the book you linked to find out exactly what that is."
      },
      {
        "id": "mzvdrhq",
        "score": 28,
        "body": "[deleted]"
      },
      {
        "id": "mzvkevp",
        "score": 26,
        "body": "Here\u2019s a study that shows training sets you up for PTSD because it\u2019s already stressing you out and acclimatizing you to kill others \n\nRandom:  you know why they push that battle buddy bullshit so much?  \n\nIt\u2019s a way to get you to kill.\n\nYou are WAY more likely to shoot an enemy to defend your battle buddy / squad mates, than you are to do it to defend yourself.\n\nYour automatic response to doing what you are told, over and over and over?  Yah - it\u2019s so when you are told to fire - you don\u2019t even question it - it\u2019s automatic \n\nThese are just some of the ways you are intentionally rewired to be able to be effective in combat.  Whether you go to combat or not, those triggers, that \u2026. destruction of the normal human aversion to killing\u2026 is severe damage on its own.  Everyone\u2019s brain handles it differently"
      },
      {
        "id": "mzvfrkw",
        "score": 22,
        "body": "Pretty sure my deployment was worse than yours .\n\n\n/s"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1lbb8m7",
    "title": "Supreme Court Rules Unanimously Against Time Limits on Combat-Related Disability Pay",
    "body": "",
    "flair": "Article/News",
    "score": 424,
    "comment_count": 73,
    "created_at": "2025-06-14T15:23:05+00:00",
    "top_comments": [
      {
        "id": "mxrnx7y",
        "score": 142,
        "body": "Good, a lot of us go on without even making claims for years. The \u201cnot broke\u201d mentality that\u2019s indoctrinated in the military carries on for a long time. \n\nI\u2019m still meeting Vietnam vets that are just starting the paperwork. \n\nAnd let\u2019s highlight who it is pushing these bills? They should be known for their anti veteran stances so they can\u2019t claim to support us in their next elections."
      },
      {
        "id": "mxr7ham",
        "score": 52,
        "body": "This is really promising. I was medically retired a few years ago and just filed for CRSC a few months ago. I\u2019ve been worried this whole time if it\u2019s too late so here\u2019s hoping all goes well."
      },
      {
        "id": "mxrr3nz",
        "score": 36,
        "body": "I hate that those that send us into harm's way penny pinch about the harms caused to us in harm's way."
      },
      {
        "id": "mxs85ri",
        "score": 25,
        "body": "Guess."
      },
      {
        "id": "mxrub68",
        "score": 24,
        "body": "Who TF tried to establish time limits!"
      },
      {
        "id": "mxsad2a",
        "score": 19,
        "body": "[removed]"
      },
      {
        "id": "mxr7zks",
        "score": 14,
        "body": ">In 2009, he was awarded disability compensation for his medical condition by the Department of Veterans Affairs and, in 2016, he applied for combat-related special compensation -- pay that is awarded to some service members who retire as a result of a service-connected medical condition.\n\n\n>He was approved, and his pay was backdated to July 2010 based on the interpretation of a law known as the Barring Act, which requires veterans to file compensation claims within six years of receiving a VA disability ratings decision.\n\n\nOh shit I got out in 2015 medical retirement, but my last VA disability rating was in 2020. So even though I'm past 6 years would it still be back dated?\n\n\nIm 100% P&T so I really dont want to push things\u00a0"
      },
      {
        "id": "mxr8srp",
        "score": 14,
        "body": "CRSC does not come from the VA, it comes from your service branch. \n\nOne does not have a status effect on the other"
      },
      {
        "id": "mxr94hv",
        "score": 12,
        "body": "Mind if I PM you? Got medically retired back in 2015, but never filed because of the conflicting information like not being able to double dip CRSC with VA disability pay"
      },
      {
        "id": "mxtpwan",
        "score": 10,
        "body": "CRSC/CRDP was created back in 2002 then amended in 2008 so most of the congress members are retired by now"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1kxl3ws",
    "title": "Forced to kill dogs, now I can't even be around them.",
    "body": "I'm posting this because I'm at my wit's end and frankly, I don't know where else to turn. I served in Kabul, Afghanistan, and something happened there that has absolutely destroyed me, and it continues to haunt me every single day.\n\nThere was an incident on base \u2013 one of the contractors was attacked by a dog. As a result, our leadership made a decision that I still can't comprehend, let alone live with. They ordered us to kill all the dogs on base. Not just the strays, but all of them.\n\nOver the course of about two weeks, we systematically killed maybe 50-60 dogs. Dogs that were friendly, dogs that were just trying to survive, dogs that some of us had even grown attached to. It was a massacre, pure and simple. And we were the ones forced to carry it out.\n\nThe sounds, the sights, the feeling of doing something so fundamentally wrong\u2026 it's all burned into my brain. I've been really fucked up ever since.\n\nThe worst part? I had to get rid of my own dog. My best friend. Not because I don't love him \u2013 I love him more than anything \u2013 but because now, when I'm around dogs, I get these intense, debilitating flashbacks to that shit in Kabul. The fear, the helplessness, the feeling of betrayal\u2026 it all comes rushing back. It's not fair to him, and it's not fair to me to live like that.\n\nI tried to get help through the VA, seeking a service connection for my mental health struggles related to this. But the VA seems to think it isn't service-connected. My VA rep who did my evaluation and handles my claim actually told me he doesn't see how it affects my day-to-day life. I was stunned. How can anyone say that after hearing what I went through? My daily life is affected. I can't even have a dog, for Christ's sake!\n\nSo, Reddit, what do I do? Has anyone been through anything remotely similar? How do you fight the VA on something like this? Is there any hope for me to get the help I desperately need and deserve?\n\nI'm lost, I'm hurting, and I feel incredibly alone with this. Any advice or shared experiences would be appreciated. Thanks for listening.",
    "flair": "Question/Advice",
    "score": 416,
    "comment_count": 134,
    "created_at": "2025-05-28T16:11:15+00:00",
    "top_comments": [
      {
        "id": "muqgwgk",
        "score": 222,
        "body": "You experienced moral injury. https://www.ptsd.va.gov/professional/treat/cooccurring/moral_injury.asp\n\nThe VA is on the fence about this. It's currently being treated more by the VA chaplain's service, so you should be able to get help there. https://www.mirecc.va.gov/visn17/moralinjury/resources.asp\n\nThe VA doesn't recognize moral injury as a disability. The treatment for it is folded into PTSD treatment because they are so similar. You may be able to make a case for PTSD and get rated, but you may need a lawyer."
      },
      {
        "id": "muqcafl",
        "score": 147,
        "body": "[deleted]"
      },
      {
        "id": "muqp2lm",
        "score": 120,
        "body": "I hope someday moral injury is recognized as a disability. My personal opinion is that many things that are called PTSD is exactly this. A spiritual wound. We have to do and see a lot of morally awful things in service. Both in combat and not."
      },
      {
        "id": "muqkgxa",
        "score": 45,
        "body": "As an animal control officer, I put down maybe 100 to 200 dogs over a couple of years. At that time I could never even conceive of owning a dog again. But as the days went by, I remembered that dogs are not a problem, but a friend - a family member. Give it time. You will recover eventually and once again enjoy the love of a dog."
      },
      {
        "id": "murfaxe",
        "score": 37,
        "body": "They don\u2019t recognize it cause alot of what the military does is immoral and they don\u2019t want to admit that.\n\nI\u2019m sorry OP for what you\u2019re going through and I hope you get the help you deserve. You\u2019re a good person, remember that."
      },
      {
        "id": "muqr1s1",
        "score": 36,
        "body": "This\u2b06\ufe0f I actually heard of that due to them not having their shots and basically a threat to our guys in and out of the compound. \n\nA moral injury is the one thing that they can\u2019t label properly, apparently not there yet. Keep asking for help and cognitive behavioral therapy to increase your paper trail. I\u2019m so sorry you had to experience such nauseating pain. Please hang in there until we get out of the dark ages of moral injuries."
      },
      {
        "id": "murg8kk",
        "score": 31,
        "body": "Being made to go actively round up and shoot a bunch of dogs is mental and physical trauma, yeah there's the moral injury aspect but this is trauma trauma."
      },
      {
        "id": "muqjxe3",
        "score": 28,
        "body": "Hey OP, I just finished a 3 week Cognitive Processing Therapy through the VA. Call the crisis line if tyyou need too and they will line tou out with intakes and appointments to get you started. I was in Kabul, also, and have had similar occurrences that I've struggled to process. Please, do the therapy!! It can bring tyou some relief and change the way you think about your experiences. Feel free to PM me ."
      },
      {
        "id": "muqahtn",
        "score": 24,
        "body": "I don\u2019t have any advice to give you except that this is and was terrible and I am so sorry for what you\u2019re going through. I hope you can find some peace."
      },
      {
        "id": "mutlnno",
        "score": 24,
        "body": "Yeah it\u2019s wild. They want to exploit the whole \u201cveterans struggle to adapt to civilian life\u201d but will deny the existence of the actual issues we have with adjusting. \n\u201cWe turned off our humanity, we had to\u201d \nI\u2019m not sure that\u2019s something that ever totally comes back. \nI did however read a book that\u2019s helped me not feel so lost in it called \u201cthe untethered soul\u201d \nHighly recommend it for other vets who want to maybe actually get a better understanding or perspective than what were told at the VA."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1m73g5f",
    "title": "Army veteran Donte Perez Jones found hanging under suspicious circumstances \u2013 seeking answers",
    "body": "Donte Perez Jones, a 35-year-old U.S. Army veteran and father of three, was found hanging from monkey bars in Whitpain Township on June 17, 2022. Authorities ruled it a suicide, but his family and many community members believe something is amiss.\n\n\n\nKey concerns:\n\n\\- He was found far from home on a park playground.\n\n\\- His feet were touching the ground beneath the equipment.\n\n\\- His wallet was missing.\n\n\\- Bruising on his body hasn't been explained.\n\n\\- There was no note, and police closed the case quickly.\n\n\n\nAs fellow veterans, let's ensure his story isn't forgotten and push for transparency. A recent podcast episode explores these troubling details and systemic issues:\n\n[https://crookedwhitpain.com/crooked-whitpain-podcast-episode-4-whitpain-township-cover-up-the-mysterious-death-of-donte-perez-jones/](https://crookedwhitpain.com/crooked-whitpain-podcast-episode-4-whitpain-township-cover-up-the-mysterious-death-of-donte-perez-jones/)\n\n\n\nAny insights, support, or advocacy from this community would mean a lot to his family.",
    "flair": "Discussion",
    "score": 408,
    "comment_count": 40,
    "created_at": "2025-07-23T08:07:58+00:00",
    "top_comments": [
      {
        "id": "n4orft9",
        "score": 117,
        "body": "At a minimum, this seems like awfully lazy police work."
      },
      {
        "id": "n4p9q0n",
        "score": 57,
        "body": "Monkey bars? That already sounds racially motivated."
      },
      {
        "id": "n4rcwl2",
        "score": 45,
        "body": "Disagree. At a minimum this is a deliberate cover-up."
      },
      {
        "id": "n4rxvzv",
        "score": 29,
        "body": "This place has too many coincidences. They just had to respond to a Nazi flag being flown in the same community.\n\n [https://www.lowerprovidence.org/home/news/statement-board-supervisors](https://www.lowerprovidence.org/home/news/statement-board-supervisors)\n\nSomeone has already noted their crimes against humanity. \n\n[https://crookedwhitpain.com/](https://crookedwhitpain.com/)"
      },
      {
        "id": "n4pgvtg",
        "score": 27,
        "body": "Totally reasonable assumption for where this happened."
      },
      {
        "id": "n4pmgn4",
        "score": 23,
        "body": "The man's feet were touching the ground. It is nearly impossible to commit suicide like that. Public display of minorities bodies is a part of racially motivated crimes as it is intended to intimidate the community."
      },
      {
        "id": "n4pjgld",
        "score": 19,
        "body": "Northern Pennsylvania is one of the most racially backwards areas that I have ever lived in. I am a born and bred Texan and have lived in Louisiana, Mississippi, and Alabama. Bradford County, PA does not tolerate black folks, at all. Stranger still, Bradford County was a part of the Underground Railroad that helped escaping slaves. We, as people, are a weird sort."
      },
      {
        "id": "n4pda7q",
        "score": 16,
        "body": "Not likely the DOJ will pick this up seeing the current administration. But that doesn't mean people still should try. I hope the family reaches out. Contact their local elected officials and the press for leverage."
      },
      {
        "id": "n4pprvo",
        "score": 10,
        "body": "Show some respect a veteran was probably murdered here."
      },
      {
        "id": "n4r03qe",
        "score": 8,
        "body": "Not likely any \u201cadministration\u201d would pick this case up."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1kv6tdl",
    "title": "Wasn\u2019t Expecting To See This at Home Depot",
    "body": "I\u2019m always here and loved to see this this morning as a reminder for all ",
    "flair": "Discussion",
    "score": 398,
    "comment_count": 59,
    "created_at": "2025-05-25T16:36:08+00:00",
    "top_comments": [
      {
        "id": "mu85rq3",
        "score": 47,
        "body": "Pretty sure Lowe's does this too, nice little gesture"
      },
      {
        "id": "mu8qbkd",
        "score": 36,
        "body": "They won't even apply the veteran discount to lumber\n\nDo you know how upsetting it is to pay full price? I'm trying to build the twistiest patio on earth, and they're hoarding the most crooked lumber on earth behind their lack of a discount! \ud83d\ude21 lol"
      },
      {
        "id": "mu85cog",
        "score": 28,
        "body": "I am okay giving up the spot for one day to honor my dead friends\u2026."
      },
      {
        "id": "mu90qlt",
        "score": 27,
        "body": "Why can't they take a civilian space? Lol"
      },
      {
        "id": "mu7u6tv",
        "score": 26,
        "body": "Its memorial day, not veterans day. \n\nI\u2019d gladly give up that spot to have my friends back."
      },
      {
        "id": "mu7yaoq",
        "score": 22,
        "body": "Home Depot is big with veteran stuff"
      },
      {
        "id": "mu8bz07",
        "score": 22,
        "body": "The spot is left vacant for the service member who cannot enjoy this holiday buying garden equipment."
      },
      {
        "id": "mu8eb13",
        "score": 21,
        "body": "Yeah, was just at my local Lowes and they also blocked off one of the veteran spaces for a little display."
      },
      {
        "id": "mu7tv5v",
        "score": 15,
        "body": "Another day to be a Waldo. \n\nThe only guy not wearing anything related to"
      },
      {
        "id": "mu9ftcg",
        "score": 8,
        "body": "Corporate still has the discount - you created an account, add your military verification, and use your phone number when you check out and the discount is applied. Instructions are here: https://www.homedepot.com/c/military"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1mppqr0",
    "title": "Do y\u2019all think the VA should provide access to gyms?",
    "body": "I\u2019m not trying to be all entitled \u201cgive me more shit\u201d. \n\nI just wonder how much money the VA would save if patients had access to a gym network. Patients that are physically fit typically are less expensive in the long run\n\nMedicare has it, with programs like \u201csilver sneakers\u201d. Enrollees can go to any gym in the network for free.\n\nJust something that\u2019s been on my mind lately..I know there\u2019s free ways to exercise, just seems like from a purely cost perspective it would save the VA money in the long run. Open heart surgery and diabetic treatments are expensive.\n\nWhat do yall think?",
    "flair": "Health Care",
    "score": 397,
    "comment_count": 171,
    "created_at": "2025-08-14T03:41:47+00:00",
    "top_comments": [
      {
        "id": "n8lbjcr",
        "score": 189,
        "body": "I'd support the hell out of it. Granted I have been on the Active and Fit program since before they ruined it"
      },
      {
        "id": "n8mog4t",
        "score": 93,
        "body": "Right now the VA is getting gutted left and right. Im just happy im still getting a disability check still."
      },
      {
        "id": "n8libwp",
        "score": 53,
        "body": "What the VA should do is look into buying well maintained but defunct shopping malls. You'd have room for a few gyms with that kind of square footage.\u00a0\n\n\nAnchor stores as wings. Lots of walking space. Optometry, audiology and quick care probably already exist or did at one point in the mall. Tons of parking. Generally well located to highways, interstates, etc.\n\n\nCould even keep the food court running with all the stuff your doc is telling you to avoid."
      },
      {
        "id": "n8lfhj0",
        "score": 46,
        "body": "Used to be pay $28/month and have up to 4 gym memberships. No extra fees at all like sign up or annuals. But they ruined it by making it $28/month and any gym after that is $23 extra"
      },
      {
        "id": "n8lquj1",
        "score": 34,
        "body": "Replace \"VA\" with \"da guberment\" and hell yeah. Make malls a place with healthy food options, gyms, and low cost medical care. Let local artists take up the remaining space to give people a reason to hang out."
      },
      {
        "id": "n8lga8t",
        "score": 28,
        "body": "It used to be 25 a month for as many gyms as you wanted\ud83d\ude29 they got too greedy I cancelled as soon as they decided i could only pick one"
      },
      {
        "id": "n8lf66w",
        "score": 26,
        "body": "What\u2019s the active and fit program?"
      },
      {
        "id": "n8ldq5t",
        "score": 24,
        "body": "I don\u2019t think many vets will turn their fitness around on account of a free gym membership.\n\nThe ones who want to do, the ones who don\u2019t want to don\u2019t, and I\u2019m guessing that\u2019s probably as complicated as it will ever be.\n\nIt would be nice for we knuckle draggers that like to work out though."
      },
      {
        "id": "n8newot",
        "score": 20,
        "body": "Yea for real things feel like they are holding on by a string just because no one has turned their attention to the VA too hard yet."
      },
      {
        "id": "n8nnvx5",
        "score": 18,
        "body": "Still easier to escape gym annual fees and be able to cancel easily. Gyms make you give up a kidney to cancel."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1nuw9n2",
    "title": "Just wanted to share!",
    "body": "FYI",
    "flair": "Article/News",
    "score": 386,
    "comment_count": 65,
    "created_at": "2025-10-01T02:17:43+00:00",
    "top_comments": [
      {
        "id": "nh5aw2i",
        "score": 51,
        "body": "Of all the Shutdowns I've been a part of, this is definitely one of them.  Thanks for the info"
      },
      {
        "id": "nh7rti2",
        "score": 21,
        "body": "Destruction of the United States. Its mandatory spending so it does not shutdown due to disagreement over discretionary spending. There may be less workers to help dispense it causing delay but it would never stop being dispensed."
      },
      {
        "id": "nh8psxq",
        "score": 18,
        "body": "OK so just so I'm getting this correct. My Ch 31(Vr&e) will still be paid but my councilor won't be working, so no changes can be made?"
      },
      {
        "id": "nh6zkw1",
        "score": 10,
        "body": "What would it take for disability payments to actually stop?"
      },
      {
        "id": "nh5ehze",
        "score": 9,
        "body": "I assume FOIA requests are shutdown?"
      },
      {
        "id": "nh7jngs",
        "score": 7,
        "body": "I called the gi bill hotline and they are still working. I asked if they knew if they might shutdown and they reported that they will not shutdown."
      },
      {
        "id": "nh9b5xn",
        "score": 6,
        "body": "Does it affect ChampVA? If it mentioned it, just know I was army and can\u2019t read."
      },
      {
        "id": "nh8v5gj",
        "score": 6,
        "body": "That graphic is misleading- that line should read: VA Regional Offices closed to the public"
      },
      {
        "id": "nh9q03k",
        "score": 5,
        "body": "yup"
      },
      {
        "id": "nh8vvzp",
        "score": 5,
        "body": "I'd email them as ask. But if your councilor is anthing like mine they will take a month to respond anyway."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1jpyv8y",
    "title": "I am cancer free thank to the amazing team at the VA!",
    "body": "I was diagnosed with breast cancer in Nov and the other day I got my pathology results back after surgery and your girl is cancer free!  \n\nAlthough it has been a VERY stressful journey and I had to take a break in my plans, I see it as a blessing in disguise. Early detection is better protection. I am dealing with so many different emotions, but this situation has really made me want to do my best to get back to being super healthy. I\u2019ve been processing my time in as active duty and was medically separated due to so much I had to experience. I can feel myself looking for purpose again. It\u2019s hard but I am able to just sit, process, (while being sober), and re-analyze what I want to do with my life not just going through the motions. I separated 2 and half years ago. I tried the wife/dependent thing for 8 months, but I knew I needed to be alone. Going through my divorced and jumped right into school to the point I was burned out. I was still moving like I was in the military in fight or flight mode. Being diagnosed with cancer oddly has made me sit down more with myself and really be honest with myself about what I want, who I am outside of the military, outside of being a wife, and now I can truly begin to heal knowing I am cancer free. \n\nI say this to say we are a resilient breed of folks and having the VA is amazing because their level of care especially with my traumas, fears, and diagnosis \u201cCPTSD\u201d (it\u2019s pretty bad, I am aware an struggle with it but am a wip). I was able to get through surgery and come out cancer free. I am only 31 and feel like I am just starting my life or truly my second life and idk what to do with myself. I am excited to live but am taking my time. I truly believe God wanted me to sit down and so here I am. \n\n***venting***\n\n",
    "flair": "Health Care",
    "score": 389,
    "comment_count": 20,
    "created_at": "2025-04-02T20:25:46+00:00",
    "top_comments": [
      {
        "id": "ml3okr5",
        "score": 18,
        "body": "Congratulations. VA treated my Prostate Cancer and I've been cancer free for 3 years - still have to do follow-up appts with urology every 6 months for 2 more years then it goes to annual follow-ups with urology but everything on the tests show I'm clean."
      },
      {
        "id": "ml42jrg",
        "score": 12,
        "body": "Me also - bladder cancer in remission 3 years now. They caught it early and cured it. They are the best."
      },
      {
        "id": "ml4v41p",
        "score": 5,
        "body": "Yes thank to the VA and great medical care we get. Thank God for being cancer free."
      },
      {
        "id": "ml52ptd",
        "score": 3,
        "body": "Good shit guys. This should be an advertisement for them tbh."
      },
      {
        "id": "ml4v5z6",
        "score": 3,
        "body": "Likewise and thank you."
      },
      {
        "id": "ml5it5k",
        "score": 2,
        "body": "Congratulations!!!!!!  I am so happy for you to be cancer free.  What an emotional roller coaster you have been going through.  I would suggest journaling your thoughts.  A support group for you to sort through your emotions.  Finally, individual therapy.  You have gone through so much for someone so young.  You are strong.  You are a warrior.\n\nTake time now for you to heal.  To breathe and take things slowly.  Have some fun.  Live in the moment.  Travel if you are able.  Just be and enjoy.   Then figure out what you would like to do at a later time.\n\nYes, we are a resiliant bunch.  \n\nAgain, I am so happy for you."
      },
      {
        "id": "ml5pu6v",
        "score": 2,
        "body": "Congratulations! Never met you, don\u2019t know you, but I\u2019m elated for you!!\u2764\ufe0f love from California!"
      },
      {
        "id": "ml5wgjc",
        "score": 2,
        "body": "Fuck yeah!"
      },
      {
        "id": "ml6uff6",
        "score": 2,
        "body": "Congratulations!  the VA saved my life too, cancer free for 6 months now"
      },
      {
        "id": "ml8ogav",
        "score": 2,
        "body": "That is awesome!! Congratulations!"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1l452af",
    "title": "VA Employees who Call Vets on the Phone, Please Read",
    "body": "Some veterans use a Video Relay Service (VRS) or an Internet Protocol (IP) relay. When you call the vet and you hear \u201cOperator #xxx, now connecting your call.\u201d It\u2019s not an answering service. It\u2019s because the vet is deaf and can\u2019t hear the phone. The operator is signing or typing EVERYTHING they hear. Just talk like you\u2019re taking to the vet directly.\n\nDo not say \u201ctell them\u2026\u201d,\n\nDo not talk like it\u2019s a voicemail.\n\nDo not hang up if there\u2019s a pause.\n\nDo not talk directly to the operator.\n\nDo not say \u201cI\u2019ll call back when I can talk to you directly.\u201d\n\nThe same thing goes for when you answer a call from a relay operator. There are more female VRS interpreters and relay operators. You will have male veterans calling and hear a woman\u2019s voice. They\u2019re saying exactly what the vet is typing or signing. The relay is approved and funded by the FCC. It\u2019s secure. It\u2019s private. We wouldn\u2019t give all our PII to verify identity if it wasn\u2019t.",
    "flair": "Discussion",
    "score": 389,
    "comment_count": 24,
    "created_at": "2025-06-05T17:24:56+00:00",
    "top_comments": [
      {
        "id": "mw6z591",
        "score": 62,
        "body": "This should absolutely be part of standard training. I've never worked for the VA, but I worked phone service for a different government department and every one of us was expected to know how to communicate with a relay service. Messing it up too many times was grounds for termination.\n\n\nThat said, people did mess up, because it doesn't come up very often, but I would expect it comes up slightly more often when you're dealing exclusively with veterans, and the training should reflect that."
      },
      {
        "id": "mw7vv74",
        "score": 26,
        "body": "I work for Vet Center, under VA. I can confirm that we don\u2019t know this. Thanks for posting."
      },
      {
        "id": "mw8qoud",
        "score": 11,
        "body": "If you get those surveys from the VA asking what you thought of your services received etc. please put this information in there. *They* (the powers that be) read that stuff and I can tell you this information is not in any mandatory trainings we receive, at least in my section in Mental health. \nThis is solid advice, as a provider, it\u2019s skills I learned over the years of using translation services while working in community mental health and social services agencies."
      },
      {
        "id": "mw75mz2",
        "score": 11,
        "body": "[removed]"
      },
      {
        "id": "mw79ayv",
        "score": 7,
        "body": "According to the website, there is a number to call if you\u2019re using a TTY phone, but those are aging fast and most late deafened people have never seen one. It still doesn\u2019t help when you need to call clinics directly."
      },
      {
        "id": "mw8qnqc",
        "score": 6,
        "body": "In the private sector, having employees on the phone with customers who don't know about this is no different than an employee removing grab bars from the public restrooms or scraping the braille off of elevator buttons.... a big fucking deal ADA violation. The things were there and worked fine, until an employee went out of their way to break it."
      },
      {
        "id": "mw6w264",
        "score": 6,
        "body": "Yeah. It\u2019s constant and horribly distracting. Hearing aids only help so much. I stream music pretty much whenever I can. I\u2019m bilateral SNHL due to spending years in an engineroom with 3M earplugs."
      },
      {
        "id": "mw6q00v",
        "score": 5,
        "body": "Unrelated to this, I am SSD and have terrible tinnitus on my deaf ear, do you have tinnitus in both ears constantly?"
      },
      {
        "id": "mw8zvgt",
        "score": 5,
        "body": "I'm conversationally deaf so I can usually do fine if I just wear Bluetooth earbuds on the phone. VA nurse called me today and was using the speaker phone. I finally had to tell her I couldn't understand a word she was saying."
      },
      {
        "id": "mw77rch",
        "score": 4,
        "body": "That sounds incredibly frustrating to deal with people who may not be aware of that service. I'm so glad that it is available for folks who need it, though."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1jcqjcy",
    "title": "Scientists make alarming discovery about health impact of drinking bottled water",
    "body": "[https://www.yahoo.com/news/scientists-alarming-discovery-health-impact-101513788.html](https://www.yahoo.com/news/scientists-alarming-discovery-health-impact-101513788.html)\n\n\"As more plastic waste is being released into the environment, microplastics in drinking water and food are being ingested by humans, causing damage to internal organs after being absorbed through the digestive system. That's most notably occurring in the kidneys, as found in\u00a0[a study](https://www.nature.com/articles/s42003-025-07641-8)\u00a0published by Communications Biology.\n\n# What's happening?\n\nThe study has found that microplastics \u2014 tiny plastic particles less than 5 millimeters in length \u2014 are the primary carriers of the environmental pollutant Benzo\\[a\\]pyrene into the body. The specific pathways are not fully understood, but there is evidence that BaP is being absorbed primarily through the intestines after oral ingestion, posing health risks.\n\nThe study has found that bottled water is the main source of microplastics, doing damage to the intestinal wall and kidneys and causing systemic inflammation.\"\n\nGWOT veterans: /seeing hundreds of thousands of Iraqi/Afghani made plastic bottles baking in the sun for months on end before drinking\n\n\".........................and I took that personally.\"",
    "flair": "VA Disability",
    "score": 382,
    "comment_count": 106,
    "created_at": "2025-03-16T17:21:31+00:00",
    "top_comments": [
      {
        "id": "mi4bvat",
        "score": 215,
        "body": "I always wondered about that when those pallets of hot water were the only potable water we had. More bad news for us"
      },
      {
        "id": "mi4c90e",
        "score": 124,
        "body": "Correct.  We joked about it back in 2005-2006 that it would somehow be negative to our health years from then and that it couldn't be healthy."
      },
      {
        "id": "mi4b5uk",
        "score": 75,
        "body": "I wonder how bad it is and what it would take for this to be the next \"burn pit\""
      },
      {
        "id": "mi4cd1x",
        "score": 72,
        "body": "\"cost of doing business\" - some Senator probably somewhere"
      },
      {
        "id": "mi4i42u",
        "score": 67,
        "body": "We made the same jokes but damn man, our agent orange is fucking plastic bottles of sun water."
      },
      {
        "id": "mi4eo3u",
        "score": 54,
        "body": "Add it to the list of the VA claims that will be \"not service connected\""
      },
      {
        "id": "mi4gn3u",
        "score": 53,
        "body": "Since every Rebuplican Senator voted against continued funding of the PACT Act I'm less than confident it would ever get covered as service connected. I knew in 2004 when I was over there it had to be terrible for us. Then I got seriously wounded in an ambush and had alot bigger problems than the water."
      },
      {
        "id": "mi4ocn8",
        "score": 37,
        "body": "Remember how you could tell the age of a pallet by how much the water tasted like dirt?"
      },
      {
        "id": "mi54yp3",
        "score": 32,
        "body": "I remember grabbing the plastic case wrap and it crinkling to pieces so you had to carry the waters back like you were trying to use a wet paper bag."
      },
      {
        "id": "mi4i26n",
        "score": 26,
        "body": "I figure this is exactly why my guts are fucked up now and why I think I'm gonna get some weird cancer that will kill me before I'm 50."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1n35bxd",
    "title": "Oof, what about on pallets in the desert? \u201cUrgent health warning as drinking water left in your car could be poisoning your body slowly over time\u201d",
    "body": "https://www.dailymail.co.uk/health/article-15040639/Urgent-health-warning-drinking-water-left-car-poisoning-body-slowly-time.html \n\nThey discovered that four common plastics, including polyethylene, released microparticles and nanoparticles when they were heated to 98.6F.\n\nHowever, the particles are considered potentially toxic because they are so small that they can enter directly into blood cells and the brain.\n\nThey are 'linked with developmental, reproductive, brain, immune, and other problems', according to the National Institute of Environmental Health Sciences.\n\n",
    "flair": "Article/News",
    "score": 379,
    "comment_count": 91,
    "created_at": "2025-08-29T11:52:59+00:00",
    "top_comments": [
      {
        "id": "nbawviy",
        "score": 205,
        "body": "\"Not service connected...\""
      },
      {
        "id": "nbazhoe",
        "score": 72,
        "body": "Nah, that was military grade water. It was going to kill you even if it was stored in the fridge."
      },
      {
        "id": "nbayc6z",
        "score": 65,
        "body": "I wonder how many bottles of water are subject to 96 degree shipping conditions\u2026I would guess all of of them for 3-4 months a year."
      },
      {
        "id": "nbazn37",
        "score": 62,
        "body": "[deleted]"
      },
      {
        "id": "nbayg0l",
        "score": 53,
        "body": "Haha we\u2019re in danger - Ralph Wiggum"
      },
      {
        "id": "nbbumbc",
        "score": 29,
        "body": "Shipping conditions? Those things were left out in the son near the barracks because no one wanted to fess up they had a forklift licenses. We were told to take what you want back to your room."
      },
      {
        "id": "nbd3r48",
        "score": 21,
        "body": "[removed]"
      },
      {
        "id": "nbcbgx8",
        "score": 21,
        "body": "Technically, the Army requires a license for just about everything. Our troop Master Driver liked me, and licensed me for everything he could. I had lanterns, lawn mowers, chain saws, etc on my license, as well as every vehicle."
      },
      {
        "id": "nbbi0pt",
        "score": 18,
        "body": "As someone that used to unload trucks in Alabama I\u2019d say 7-8 months"
      },
      {
        "id": "nbc6qdp",
        "score": 17,
        "body": "We needed licenses to drive the forklift? \ud83e\udd23"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1kypza9",
    "title": "Please use your GI Bills wisely.",
    "body": "I see and hear too many vets say I wasted my GI Bill. Don\u2019t go to small schools with little to zero connections. Start at a community college if you need then transfer to the biggest university near you. The GI Bill almost guarantees you a spot. You don\u2019t have to take a test to get into the universities. The bigger the school the better. It leads jobs seeing you\u2019ve graduated from a top school. Top schools offer great curriculums and opportunities. Take full advantage of the fact we don\u2019t have to stick small. ",
    "flair": "Discussion",
    "score": 375,
    "comment_count": 306,
    "created_at": "2025-05-29T23:53:02+00:00",
    "top_comments": [
      {
        "id": "muzb9uo",
        "score": 118,
        "body": "Just stay far far away from for profit schools."
      },
      {
        "id": "muzgxnt",
        "score": 96,
        "body": "Until they improve the Transition Assistance Program (TAP) for every branch, I assume many veterans will not be informed on how to effectively use their GI Bill. When I attended TAP, I remember seeing DeVry University (maybe University of Phoenix too) being recommended as a top tier school to attend."
      },
      {
        "id": "muzaqs0",
        "score": 74,
        "body": "And this is why I transferred from a typical diploma mill to an actual recognized school when I got out and started using my GI bill."
      },
      {
        "id": "muz9402",
        "score": 66,
        "body": "[deleted]"
      },
      {
        "id": "muzcc48",
        "score": 65,
        "body": "You guys should also look into VR&E before using your Gi bill, essentially better benefits."
      },
      {
        "id": "muzbzjt",
        "score": 40,
        "body": "Used the Pell Grant for CC. GI Bill for the big stuff. You can pay for McDonald's, make them pay for Ruth Chris"
      },
      {
        "id": "muzb74t",
        "score": 37,
        "body": "A lot of military colleges aren\u2019t good and aren\u2019t recognized."
      },
      {
        "id": "mv0birb",
        "score": 33,
        "body": "Yep same here. Or AMU. Fuckin wild. And nobody respond to me if you got your degree at AMU and you\u2019re doing well. I do not care and that school still sucks."
      },
      {
        "id": "muzgsym",
        "score": 32,
        "body": "To piggyback: Some colleges offer programs where you can take graduate courses that will count toward both your undergrad AND grad. When I depleted my GI Bill I was only about $5,000 away from my masters."
      },
      {
        "id": "muzjjqm",
        "score": 32,
        "body": "I can't agree with you enough on this. I wasted my GI bill on a for profit school."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1mfizrv",
    "title": "Well, today I learned the value of keeping my mouth shut about my disability.",
    "body": "For context I am 100% p&t and got a job as a TIG welder (TIG welders generally get to sit during their shifts while welding so I figured this was a safe pick). I started my new job a few weeks ago and figured I\u2019d just sit and weld in the shop for the entirety of my shift. Unbeknownst to me because it was never discussed or brought up during the hiring process, we are also supposed to leave the shop to install parts. Well a recent install didn\u2019t go so great. My coworker and I had to climb a 2-story set of stairs that led to a short platform with ladders on either side that was also followed by a similar platform with stairs on either side. Needless to say there was a lot of up and down and we also had to carry our tools and welder up this platform. The coworker is an older gentleman and asked me to carry all of mine and his tools to the top and being the younger newer employee I obliged. After all this we ran into an issue because the welder we were using kept tripping the breaker and guess where the breaker was located? All the way back down the stairs. So I also had to make multiple trips to go reset the breaker. When lunch came around my coworker told me that we were going too slow and that the boss would get mad, at this point I confided in him that I had VA disability and that my knees and back were in terrible pain and that I was probably going to continue to be slow for the remainder of the day. Fast forward to today and I\u2019m helping another coworker out and he walks over, makes some conversation and then starts making a strange face. I asked him \u201cwhat\u2019s up?\u201d And he said \u201coh, my feet are really bothering me\u201d and then walked off. At the start of the shift he also told me that the boss will get mad if I\u2019m sitting down despite there being a stool at every station. I\u2019m feeling very frustrated and am wondering, for those of you that also have jobs, what would you do if a day at work was a little too much for you?\n\nTL;DR: had to travel to a job site and had a rough time navigating the platform and hauling tools because it was aggravating my knees and back, confided in my fellow employee that I had VA disability and that I was going to be slow the rest of the day, now that employee seems to be mocking/ harassing me. What would you do if your day at work was a little too much to handle?",
    "flair": "Discussion",
    "score": 378,
    "comment_count": 166,
    "created_at": "2025-08-02T05:51:43+00:00",
    "top_comments": [
      {
        "id": "n6i1s2z",
        "score": 262,
        "body": "Put in a disability accommodation with HR. By law they have to provide reasonable accommodations for you\n\nIf you get made fun of for being a disabled veteran, that\u2019s a pretty shitty hostile workplace. It also opens them up for lawsuits"
      },
      {
        "id": "n6hfty6",
        "score": 247,
        "body": "Honestly, I would quit. You are always in pain in general. If continuing with the daily physical draining and pricks of co-workers, you will be worse off soon. How do you think you would feel in a year? There has to be other less straining jobs out there for you."
      },
      {
        "id": "n6hkozi",
        "score": 186,
        "body": "The person making fun of you is the older person who asked you to carry his tools for him? If he's going to make fun of you, then I would confront him about him making you carry all of his stuff. If he wants to be a jerk about your disability, then he doesn't get any special treatment and can carry his own shit. If you didn't have to carry all of his equipment, you might not have been in as much pain and might have been able to go faster.\n\nI would just keep doing what you're doing and don't worry about anything until your boss or manager says something. If they can't accommodate your disability, that's one thing, but for this guy to ask you for special treatment because he's old and then make fun of you for being disabled, that's a crock of shit.\n\nBut also, like another person said, maybe this job isn't for you. If this job puts you in pain at the end of the day, you're doing more damage to your body and it will only get worse. Hopefully there can be another welding job out there where you don't have to be climbing a bunch of flights of stairs all the time."
      },
      {
        "id": "n6iwtfc",
        "score": 185,
        "body": "This. Several years ago I (100%PT) had an open lesion on my leg. Told my manager I could not work past 8 hours due to pain and swelling. He told me, in front of several other people, that he \u2018could not use me then.\u2019 This, despite the other sales crew telling me that since my arrival, we had the best sales team since they had been working at that location. HVAC & Plumbing. So, I wrote a letter to HR expressing my concerns. No reply. Got fired the next day. \n\nFast forward 4 years after my lawsuit. Big settlement on my end. \n\nLearned that the manager was let go & HR person was forced to retire. \n\nYou are protected."
      },
      {
        "id": "n6hn839",
        "score": 53,
        "body": "I would quit.  It's too much for your body to handle.  You have no reason to push past your limits."
      },
      {
        "id": "n6ii1fr",
        "score": 46,
        "body": "Yeah if it\u2019s this bad now just imagine. I\u2019m not going to cripple myself for anyone. And that coworker would have one more time to try me"
      },
      {
        "id": "n6hueb1",
        "score": 37,
        "body": "If it is too physically demanding, leave the job. No ned to put your health in jeopardy. Also, I don't understand why people feel the need to state they are VA-disabled. Saying \"I was in the military and have a bad back and knees\" has the same effect and raises fewer questions. Instead of mocking you, the co-worker would probably be thanking you for your service."
      },
      {
        "id": "n6jjz7y",
        "score": 35,
        "body": "So glad to hear that you won in the end. As someone who once worked in maintenance (aircraft), and now work in hr, I know how shitty it is to be in pain and dealing with shitty supervisors who don\u2019t know how to properly manage in general. I\u2019d echo these stories by highlighting that documentation is key in HR."
      },
      {
        "id": "n6hjq3d",
        "score": 33,
        "body": "First and foremost, always best to document your disabilities with employer. They can make accommodations if it helps, but also they could use their heads and keep you on jobs where you could use their stool.  The ADA is your friend and literal rule book."
      },
      {
        "id": "n6hkgte",
        "score": 31,
        "body": "Rule of thumb never discuss your va benefits with anyone outside of your spouse. People get really weird and jealous about it. They don\u2019t understand what we went through to get these ratings."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1ooi7u8",
    "title": "Is this Ok to wear this old jacket as a civilian?",
    "body": "I live in Texas and found this at a local army shop called Omahas. Was considering getting this but wanted to ask if it was legal or ok to wear as a civilian.? I have never served but did have a family member serve.\n\nIt doesn\u2019t have any ranks or insignia, just the Army name and a last name that says svec.",
    "flair": "Question/Advice",
    "score": 370,
    "comment_count": 266,
    "created_at": "2025-11-04T20:23:10+00:00",
    "top_comments": [
      {
        "id": "nn4a30m",
        "score": 476,
        "body": "I see a lot of non-vets wearing old military gear. As long as you're not using it to pass yourself off as something you're not, nobody's going to bat an eye. Most of us who served wouldn't even take a second look at it. First glance would tell us that jacket is probably older than you."
      },
      {
        "id": "nn4czfe",
        "score": 135,
        "body": "No, you\u2019ll be recalled to active duty and get a court martial\u2026"
      },
      {
        "id": "nn4l2du",
        "score": 131,
        "body": "Lol this!! That field shirt is more than likely 100% older than OP. Was issued that stuff at Fort Carson in 1969 :)  No one is going to care a wit!!"
      },
      {
        "id": "nn4f7xt",
        "score": 111,
        "body": "Only if you drive a cab and have a mohawk."
      },
      {
        "id": "nn4bv2c",
        "score": 63,
        "body": "Yes.\n\nFricking Ralph Lauren is selling old BDU pants for 80 dollars"
      },
      {
        "id": "nn4oufd",
        "score": 38,
        "body": "I too spent time at Fort Carson. Just MUCH later. 2010-2014\n\nAlso, to reiterate what other people are saying, nobody cares  about a civvie wearing army surplus gear. It's cool shit. And I actually like seeing people who are interested in our culture and customs.\n\nFor instance, OP could look for markings or names or whatever and try to find the story of this jacket. Feeling connected to history is super cool.\n\nSo OP, go and wear it with pride. And when you do, tell people what you've learned about it. Alternatively, add band/artist patches and decorations and make it your own. Like a punk jacket."
      },
      {
        "id": "nn4i9iv",
        "score": 34,
        "body": "Are you talking to me?"
      },
      {
        "id": "nn4am23",
        "score": 32,
        "body": "You do you boo boo"
      },
      {
        "id": "nn4b5qh",
        "score": 24,
        "body": "As long as you\u2019re not pretending to be a service member no one will care. It wasn\u2019t long ago that a few more \u201chip\u201d retail stores were selling ACU and ABU pants. I also see so many people wearing multicam pants these days."
      },
      {
        "id": "nn4ssoa",
        "score": 23,
        "body": "Correction: Recalled to active duty and made to go through basic training.  Make sure you bring your jacket and wear it upon reporting."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1j85vte",
    "title": "Don't give up folks, there is hope...after a year with the Board of Veterans' Appeals, I've finally been granted service connected disability for my cancer",
    "body": "Initially diagnosed in May 2022, surgery, chemo, and in remission since October 2022. Initially denied, and after a lot of independent research and collecting of studies and nexus letters, it's been granted! Keep up the good fight and check your balls!",
    "flair": "Question/Advice",
    "score": 375,
    "comment_count": 57,
    "created_at": "2025-03-10T18:38:14+00:00",
    "top_comments": [
      {
        "id": "mh469co",
        "score": 17,
        "body": "Unsure, but I have documentation of exposure to burn pits, possible chemical weapon storage sites, and jet fuel"
      },
      {
        "id": "mh45wfo",
        "score": 15,
        "body": "Hmm, I had testicular cancer too. Wonder if it's something we ran into while serving or just random."
      },
      {
        "id": "mh4705u",
        "score": 9,
        "body": "I had exposure to JP5 and who knows what else. Anyways, glad the V.A is taking care of you"
      },
      {
        "id": "mh4oie2",
        "score": 8,
        "body": "I\u2019m sure that\u2019s such a relief! I have never seen as much testicular cancer as I did at while working at Tripler, all in otherwise healthy young SMs."
      },
      {
        "id": "mh66nni",
        "score": 6,
        "body": "Lookup the chemicals used in the Armed forces that cause testicular cancer. I know Trichloroethylene does. I used it 5 days a week for at least 6 months to clean jet engine parts. I've been waiting for the bomb to drop and hoping it never does."
      },
      {
        "id": "mh4j150",
        "score": 5,
        "body": "Holy shit dude.  This is brutal.  Congrats tho."
      },
      {
        "id": "mh53e8q",
        "score": 5,
        "body": "Damn, makes you wonder about teabagging the JP8 tank now doesn't it?"
      },
      {
        "id": "mh6yx49",
        "score": 5,
        "body": "So a word of caution. I had ball cancer while I was leaving Iraq. I was rated 100% service connected. About 8 years later they kept it SC but dropped it down to 0%. Nevermind that I'll have to do test for the rest of my life because of it."
      },
      {
        "id": "mh41dz7",
        "score": 4,
        "body": "Congratulations on work hard and winning your appeal. I wish you continued good health and success."
      },
      {
        "id": "mh78wrx",
        "score": 4,
        "body": "I\u2019m surprised they kept it at 100% that long. I went from 100% to 0% in about a year and a half for leukemia. Because cancer isn\u2019t static once they consider the service member in remission off to 0% you go! It\u2019s a lifetime disease for me too, I see my Hematologist on a quarterly basis."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1pu061m",
    "title": "What in the AI Slop is this??? Is the VA too cheap to use real artists?",
    "body": "I appreciate the thought, but come on. The fubar flags alone should have got this denied from being sent.",
    "flair": "Discussion",
    "score": 372,
    "comment_count": 183,
    "created_at": "2025-12-23T17:45:10+00:00",
    "top_comments": [
      {
        "id": "nvkzxxq",
        "score": 153,
        "body": "Or REAL VETERANS?"
      },
      {
        "id": "nvky252",
        "score": 116,
        "body": "Lmao I kept enhancing enhancing and it just kept getting worse and worse."
      },
      {
        "id": "nvl2601",
        "score": 98,
        "body": "But it\u2019s nice that the kids born at Camp Lejeune have not only found fulfilling jobs, they\u2019re having fun"
      },
      {
        "id": "nvl648w",
        "score": 56,
        "body": "My wife is a fed contractor who, as a graphic designer, creates a lot of static images for VA marketing and website info and all that. She uses real pics of real people (vets, active, guard, whoever) and does all the graphics herself alongside a team of others. \n\nCertain people in control of certain types of funding have determined that this work is unnecessary, and she and her teammates have thus been furloughed multiple times. \n\nSo, now we get these masterpieces to look forward to, as real people get less opportunity to work. She may soon add to the unemployment numbers that will most certainly not be misrepresented by certain individuals in charge of reporting such things."
      },
      {
        "id": "nvl2uj7",
        "score": 56,
        "body": "The man in front of the tree.... growing out of the table.... with a creature growing out of his shoulder....\n\n100% VA Rating coming his way!"
      },
      {
        "id": "nvl2e8g",
        "score": 52,
        "body": "I know several veterans doing photography that would love the opportunity."
      },
      {
        "id": "nvl2f0y",
        "score": 40,
        "body": "[removed]"
      },
      {
        "id": "nvld6dm",
        "score": 36,
        "body": "Even if they don't want to hire actual photographers who are veterans, they literally have the different MOS in all 5 branches that does photography and they don't even need to pay them if DOD/DOW allows it."
      },
      {
        "id": "nvldlav",
        "score": 32,
        "body": "Lots of EOD Vets in that image"
      },
      {
        "id": "nvl8g63",
        "score": 31,
        "body": "Nah, not service connected.\u00a0"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1jldaes",
    "title": "For my mid life crisis I quit my job today.",
    "body": "And went home to ride my motorcycle. Was a sysadmin for a small/medium company. Been taking all of my meds but becoming more and more down as I watched the corporate growth chew through my peers. \n\nI dunno, maybe a bad decision but I feel better. My wife's income and our savings plus my disability mean we won't starve. I'm looking forward to spending some time with the kids and maybe pick up a part time gig at the gas station down the street.\n\nHow are you all doing today?",
    "flair": "Discussion",
    "score": 372,
    "comment_count": 93,
    "created_at": "2025-03-27T20:49:23+00:00",
    "top_comments": [
      {
        "id": "mk2l4ox",
        "score": 80,
        "body": "\ud83d\udc46took courage! Rare that a man gets the opportunity to tend to the things that really matter. Your family needs you and you guys will be okay, I promise. Go enjoy and LIVE your life brother."
      },
      {
        "id": "mk2m9io",
        "score": 39,
        "body": "I'm near the same boat. My disability will cover my bills, but I'm saving up for my a month long trip to Europe this year, so I'm just gonna embrace the suck. \n\nWatching how this once family owned company turn into a corporate shrill and expect more out of employees but pay less is a fucking joke. \n\nIll probably quit after my trip and find a easy part time job and coast. I know they're always looking for school bus drivers, but kids fucking suck."
      },
      {
        "id": "mk2r3bb",
        "score": 38,
        "body": "Seems like you realized that you didn\u2019t need to chase what you\u2019ve been chasing. Congratulations on your epiphany.\u2764\ufe0f"
      },
      {
        "id": "mk2p41f",
        "score": 18,
        "body": "Grab a beer and bang the wife! Have a great weekend"
      },
      {
        "id": "mk377id",
        "score": 18,
        "body": "Don\u2019t mind if I do, and thank you for your hospitality!"
      },
      {
        "id": "mk2zcf9",
        "score": 16,
        "body": "I was so busy working and providing for my family that I missed all of my kids' first steps and every special event. By the time I finally slowed down, the three of them were ready to go to college. I missed the best part of having kids\u2014the chance to relax and enjoy watching them grow. Make sure to give them all the love you have."
      },
      {
        "id": "mk30qe2",
        "score": 14,
        "body": "Quit a year ago and never looked back. My mh was steadily and rapidly declining."
      },
      {
        "id": "mk2ky92",
        "score": 12,
        "body": "Better, finally getting the dog soft and fluffy"
      },
      {
        "id": "mk2thbc",
        "score": 10,
        "body": "Good for you! I'm feeling the same. I'm just out of gas anymore, angry, agitated, burned out, mentally unwell...sigh. Glad you are able to focus on what matters!!"
      },
      {
        "id": "mk2uhur",
        "score": 10,
        "body": "Ha! I did that...said fuck it I quit...after 10 days (still being paid)...now that you've cooled off we need you back...no vacation days charged, no sick days charged....boss said sometimes you just need to do that...."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1ouc7q3",
    "title": "Thank You Vets!",
    "body": "For your service and pledge to uphold our.  Constitution. ",
    "flair": "Discussion",
    "score": 367,
    "comment_count": 27,
    "created_at": "2025-11-11T15:23:03+00:00",
    "top_comments": [
      {
        "id": "noara0a",
        "score": 15,
        "body": "Money Pweaaaaase!!!!! \ud83e\udd32"
      },
      {
        "id": "noapr40",
        "score": 8,
        "body": "UR WELCOME FUR MY SERVICE"
      },
      {
        "id": "noayvlu",
        "score": 6,
        "body": "People: \u201cthank you for your service\u201d\n\nMe: don\u2019t thank me, just be the American worth serving for"
      },
      {
        "id": "noaz1tm",
        "score": 5,
        "body": "\ud83e\udd2e  It was a job.  No more, no less."
      },
      {
        "id": "nobbxzu",
        "score": 4,
        "body": "This extremely wide range of replies is why I love my fellow vets."
      },
      {
        "id": "noar367",
        "score": 3,
        "body": "No problem - I had a blast!"
      },
      {
        "id": "noc4atq",
        "score": 3,
        "body": "Some given, some received."
      },
      {
        "id": "noe6v27",
        "score": 3,
        "body": "Be an American worth fighting for."
      },
      {
        "id": "noalhjp",
        "score": 2,
        "body": "You are welcome. Where I live nobody or very few appreciate us, so this is cool to read this morning. Have a wonderful day \ud83d\ude0e\u00a0"
      },
      {
        "id": "noc82g4",
        "score": 2,
        "body": "My pleasure"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1n9q2iy",
    "title": "What was the dumbest (valid) reason you saw an officer lose his commission?",
    "body": "Looking for some entertainment on a Friday. I went through ROTC with a guy who got a pilot slot but had one year of school left. All he had to do was graduate, pass a PFT, and not do drugs or get arrested. \n\nThe guy was an arrogant prick who once referred to enlisted personnel as \u201cthe little people\u201d when talking with an E7. That\u2019s what makes this next part so delicious. \n\nFall semester he winds up on academic probation. The det commander defends him to the bureaucracy, convinces them to let the cadet keep his pilot slot, then calls the cadet into the office and tells him in no uncertain terms to stop slacking and take his classes seriously. Cadet swears up and down he\u2019ll straighten up and fly right. \n\nA month later the commander asks the cadet\u2019s professors how he\u2019s doing. They all say he stopped showing up after the first week. \n\nDude was disenrolled immediately. The best part is that - per the terms of the contract he signed when he started ROTC - he was obligated to serve four years active duty, going in as an E3. He went to basic (again) then was assigned to a base an hour away from the university. Instead of becoming a pilot he was given some desk job where he\u2019d occasionally have to process paperwork for cadets who went to the base for whatever reason. ",
    "flair": "Question/Advice",
    "score": 368,
    "comment_count": 226,
    "created_at": "2025-09-06T04:11:45+00:00",
    "top_comments": [
      {
        "id": "ncojaca",
        "score": 364,
        "body": "Major drove drunk in Germany and killed a woman. Sentenced to 8 years hard labor at Coleman Barracks. \n\nI saw him get in processed by an E6 who read him the riot act. The \"major\" said to the SSG: \"I'm a major. You can't talk to me that way\".\n\nThe SSG said: \"No, you were a major. Now you're here and belong to me\". \n\nThe immediate shoulder slump by the major once he heard that was epic."
      },
      {
        "id": "ncomt1l",
        "score": 127,
        "body": "Academy grad PCSing to ENJJPT (pilot training with guaranteed fighters at the end) loaded his dity move with cinder blocks from Home Depot, and returned them at the new base...and told the clerk what he was doing. Clerk called the base and he was gone.\n\nAll for maybe an extra $1k."
      },
      {
        "id": "ncp1gga",
        "score": 119,
        "body": "Full bird colonel chaplain got caught embezzling chapel funds to fuel his gambling addiction.\n\n\nAbout $250,000 in chapel funds."
      },
      {
        "id": "ncoqcgw",
        "score": 81,
        "body": "Not sure if he lost his commission, but he was relieved of his position as CO. \n\nHe got mad at (a very autistic) joe and threw a fire extinguisher clear across the room at him. This was the climax and culmination of a string of highly regarded things this guy had done such as: \n\n-  Chain up the weights in the COF so platoons would run for PT instead of lift\n\n- Wrote \u201cclean me\u201d with grease or something all over the cement floor of the COF, which stained permanently"
      },
      {
        "id": "ncp79a9",
        "score": 76,
        "body": "1LT got caught committing BAH fraud.  He was claiming a wife he no longer had.  Ended up getting court martialed.\n\nS4 pissed hot at UA.  He was having marriage problems and claimed his wife gave him a mystery pill from a gas station.  Never saw him after that.\n\nAnother 1LT got pulled over for DUI.  He was popping percoset while driving.\n\n2LT went AWOL while snowbirding at BOLC.  Received a letter of reprimand.  Went to his first duty station and went AWOL again.  When being chewed out, he insulted the BN XO by calling him a bad leader.  Article 15.\n\nAbsolutely fucking worthless fire support officer gets moved out of BN by getting a position at Eighth Army HQ (yes, his incompetence was rewarded with a 4187 to a very cush job.). He immediately got a DUI in Yongson.\n\nBDE S4 had a side chick who was an E3.  Gone.\n\nBrand new female MP 2LT goes to the club and gets rejected by an E7.  She goes outside and gets his licence place number, and then runs the plate in the database the next day.  She then fucking detains the E7.  She disappeared fast.\n\nPL went to the arms room, draws his NODS, puts them in his POV and then goes to the club.  Yeah, his car got stolen."
      },
      {
        "id": "ncpr2qk",
        "score": 63,
        "body": "When I went through the Special Forces Qualification Course, the last two things you did were language school and SERE School. The language instructors were typically very cool and this held true, apparently, for the Korean teacher. She was very laid back when it came to learning and saying Korean profanity and dirty slang. Apparently, some students thought that this was accepted behavior outside of the schoolhouse.\n\nFlash forward to SERE, the last step before you get your long tab (back then). An Army Captain, going through the chow hall at good old Camp Mackall, decided it was a good idea to say \u201cshow me your tits\u201d in Korean to the nice Korean lady behind the counter. He laughed and she\u2026..immediately freaked the fuck out and started screaming at him and everyone went crazy in the kitchen.\n\nThat idiot O-3, with only a few weeks left in the arduous SF pipeline, was kicked out of the Q Course to \u201cneeds of the Army\u201d.\n\nWhat a dumbass."
      },
      {
        "id": "ncoxaye",
        "score": 56,
        "body": "What do they make them do for hard labor?"
      },
      {
        "id": "ncoo5hr",
        "score": 56,
        "body": "Good Lord. I want to buy that clerk a beer."
      },
      {
        "id": "ncrinlj",
        "score": 56,
        "body": "Dig holes and fill them back in. Bust down big rocks into smaller rocks. Shit like that."
      },
      {
        "id": "ncp25zz",
        "score": 41,
        "body": "Lol what is it about majors lol, the absolute worst. (Not to make light of the incident he was involved with, that's absolutely terrible)"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1n7klzg",
    "title": "Divorce after retirement. Spouse couldn't adjust.",
    "body": "I retired less than a year ago and I'm getting divorced. My spouse couldn't adjust to me not being active duty anymore. \n\nI had a difficult career while I was in. I drank way too much, I smoked, I was extremely depressed and had suicidal thoughts more than I actually admit out loud. I tried medication and therapy while I was active but they didn't really do much for me then. I was miserable but she was happy. Her and the kids were always taken care of even if I wasn't the best husband and dad in the world.\n\nSince retirement though I've seen a lot of personal growth/improvement. I don't drink any more at all, I quit smoking and the meds and therapy seem to be working. Depression has lessened and no more suicidal thoughts. I picked up gardening and decorative painting as hobbies. I am way more engaged with my kids and I began taking my dogs out more and just things that normal people do. \n\nWhen I started getting better is when things started getting worse. She started demanding more. No matter how hard I worked at being a better person, no matter how much of a better person I became, it was never enough. I asked her to see her own therapist and she refused. She was steadfast that I was the problem and had all the problems. \n\nI managed to convince her to go to marriage counseling because maybe a third party could help me understand what she was trying to communicate. After a initial session we agreed that the counselor was a good fit for us. At that point I also authorized the marriage counselor to talk to my therapist so I could really tackle the problems she thought I had head on.\n\nTurns out that the marriage counselor and my therapist agreed that I was doing really well. Making great progress from who I was to who I am now. The counselor even told her that in session. Counselor suggested that she focus on herself with her own therapy.\n\nI don't think she was expecting to hear that because she really went off the deep end. She started stealing and abusing prescription pills, drained the bank account became verbally abusive to me and started to try to manipulate the kids against me. She then became physically violent to where police were called and she was arrested. \n\nThe marriage counselor, my therapist and my psychiatrist know the story and seem to agree  that my personal improvement after retirement somehow left her feeling some type of way about herself that she couldn't reconcile on her own. They've suggested that she needed me to be the one with the problems so she could feel better about herself, and once she felt exposed she lashed out.\n\nLike the title says, I'm divorcing her now. I'm curious if anybody else has a similar story.\n\nTL:DR Spouse didn't like the person I became after retirement. Getting divorced. Anyone else?\n\n\n\n",
    "flair": "Call for Help",
    "score": 373,
    "comment_count": 110,
    "created_at": "2025-09-03T17:07:18+00:00",
    "top_comments": [
      {
        "id": "nc8534k",
        "score": 267,
        "body": "Just wanted to say congrats on the quitting drinking and smoking. Did too much of both myself, but off both and doing better now. Good job!"
      },
      {
        "id": "nc8eesw",
        "score": 78,
        "body": "Yeah OP, this is real. My mom is dealing with this dynamic in some friendships after celebrating some significant milestones in work and personal health. Unfortunately, some people depend on your dysfunction in order to perceive themselves as functional. The more wins you earn, the more resentful they get. Come to think of it, my wife also dealt with this with her childhood best friend.\n\nHopefully for your family's sake, your wife gets the help she needs. Be secure in your victories--you fought hard for them."
      },
      {
        "id": "nc87hqo",
        "score": 69,
        "body": "Yea man!!  I\u2019m about 2.5 years no booze after retiring from the army."
      },
      {
        "id": "nc8a24p",
        "score": 42,
        "body": "First, excellent work on yourself. You are putting in the hard work with the self reflection that is so healthy! This must be acknowledged. So many people never do this but here you are. Hold space for your accomplishment! \n\nUnfortunately the side effect of unhealthy people being in a relationship is when one person puts in the work and the other doesn\u2019t, it causes light to shine on the ever growing chasm between you. This pattern exceeds the veteran community. I\u2019ve gone through this myself. \n\nHonor the relationship you had that served you both for the time and while she spirals out of control, keep working with your care team to get yourself through it. Try not to broad brush all women with the same shade she slings. Avoiding connection because \u201chalf the women\u2026\u201d is a reflection of an equally unhealthy mindset. You deserve love and be loved if that\u2019s what you want. \n\nKeep healing. Get through the suck. Relationships can be a season, reason, or a lifetime. Brush yourself off when you\u2019re ready and live your life well. I\u2019m sorry you\u2019re going through this but it does get better. Love and light dude. Love and light."
      },
      {
        "id": "nc880fe",
        "score": 36,
        "body": "I have up the booze over covid. Cold turkeyed nicotine last year for a spinal surgery. Damn, nicotine was hard to quit. I still crave the stress relief that came with a smoke break. And I know if I pick one up again, I'll never quit again. So I make sure not to pick one up again."
      },
      {
        "id": "nc84om3",
        "score": 23,
        "body": "Seems like there might be another relationship"
      },
      {
        "id": "nc86snt",
        "score": 20,
        "body": "Can never understand why the person who's supposed to be your biggest supporter can turn into your biggest opp but you don't need that in your life at all. Enjoy your money and don't get married again."
      },
      {
        "id": "nc8d0bf",
        "score": 20,
        "body": "No disrespect, but sounds like my ex wife. She was there for the free ride through life. Once i retired things went down hill because i was now home all the time and she didnt like that."
      },
      {
        "id": "nc872d9",
        "score": 18,
        "body": "Yeah I\u2019m curious what her boyfriend thinks about all this"
      },
      {
        "id": "nc8pyt2",
        "score": 16,
        "body": "Thanks. Your words seem like they come from a very wise place. I know I'll end up in a better place as long as I keep doing the work. I am going to be guarded for a while, I am working in therapy to avoid painting all or half of women as anything. For now I just need to get through the divorce process before I even think about pursuing a new relationship."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1k87ndg",
    "title": "Warfare Movie; warning to those with PTSD.",
    "body": "It's 2:28 AM. I'm sitting here writing this after finally calming down. I'll try not to dive into spoilers, but I wanted to share my experience with this movie (because, truthfully, I was never able to make it to the end).\n\nAmy (that's what I call my PTSD, short for amygdala) hasn't shown her face in a long time. I went into this movie knowing almost nothing about it. I don't know exactly when the discomfort started, but the sounds (the sharp whiz and crack of gunfire) set my heart racing. Watching them slice corners and clear rooms made my fists clench without me even realizing. The ringing, the shell shock, the way it all played out... it brought the sand of OEF right back into my mouth.\n\nBut I lost my grip when they called out \"six minutes until the Bradleys arrive.\" Without thinking, I started a timer on my watch (muscle memory from another life). When those Bradleys actually rolled up almost exactly six minutes later, something inside me broke loose. I had to get up and leave the theater.\n\nThe rest of the night, my wife sat with me, gently pulling me back to the present (reminding me I was safe).\n\nI want to be clear: this isn't a condemnation of the movie. I\u2019m not saying it\u2019s bad. But I am saying this: if you live with PTSD, please go into it with caution. Prepare yourself (or maybe wait until you\u2019re somewhere safe before watching).\n\nI take full responsibility for putting myself in that situation. But I know I won\u2019t be the only veteran who walks into this movie unaware. I hope sharing my experience brings a little awareness (maybe even spares someone else from going through the same).",
    "flair": "Discussion",
    "score": 365,
    "comment_count": 121,
    "created_at": "2025-04-26T07:47:35+00:00",
    "top_comments": [
      {
        "id": "mp433rt",
        "score": 95,
        "body": "Amy is a sneaky SOB.  Glad you have a supportive and understanding wife!"
      },
      {
        "id": "mp4kmug",
        "score": 94,
        "body": "Smells occasionally get me. Totally rando smells. Sounds of course, but smells are an odd trigger for me. I\u2019m like some type of gd hound dog."
      },
      {
        "id": "mp4317j",
        "score": 61,
        "body": "I rewatched Jericho (the TV series) with my new wife last year\u2026I forgot about the bad \u201cneighbors\u201d mortaring the town\u2026same effect\u2026it caught me off guard. (Two tours to Balad/LSA Anaconda, i.e. \u201cMortaritaville\u201d). I feel ya brother\u2026thanks for the heads up!"
      },
      {
        "id": "mp498w2",
        "score": 59,
        "body": "Ya I\u2019m not trying to watch that. Me and Iraq are cool now."
      },
      {
        "id": "mp43vqj",
        "score": 46,
        "body": "Good lookin out. I remember some of the sniper scenes in that one American Sniper movie making me twitch uncomfortably quite a bit - my 2nd tour we had Iraqi snipers taking shots at us pretty regularly and in one instance nailed the guy I was standing \u201cnext to\u201d (like, 5-10 feet away, but directly in line with the shot, and next closest person was about 20 feet away). \n\nThere\u2019s a rooftop scene in the movie where the sniper is aiming out of some latticework or something, and I remember hunkering down behind a humvee door scanning a nearly identical rooftop maybe 300-400y away trying to figure out if I should take a shot at the movement I saw there, but unsure if that was actually the sniper. No more shots came from that area or anywhere else so we evac\u2019d back to base asap but dude died en route (don\u2019t want to say his name to doxx myself here, but RIP). \n\nAlso, my unit was the same division as the one portrayed in the movie getting hunted by the sniper, so\u2026yeah. Lots of triggering stuff there to get the heart going even if it was still a bit of Hollywood embellishment at the end of the day. I feel ya."
      },
      {
        "id": "mp6av7z",
        "score": 39,
        "body": "Smells are strongly linked to memory."
      },
      {
        "id": "mp44dv4",
        "score": 29,
        "body": "1. It's sounds like your wife is a ROCK! Anchor to her and keep her close.\n2. Pre army me would have naively said \"it's just a movie bro\" but retired veteran me says \" youre home brother. You're alive, breathe and put Amy back in her place\"\nLastly, I haven't seen the movie, but I'm sure I'll react the same. Stay strong dude"
      },
      {
        "id": "mp4603b",
        "score": 24,
        "body": "CRAM was the goat"
      },
      {
        "id": "mp5gmlj",
        "score": 21,
        "body": "Reminds me of when they had an \u201copening\u201d for Saving Private Ryan for actual D-Day veterans. Half of them walked out during the beach invasion. They had the stare as they did so."
      },
      {
        "id": "mp6n5st",
        "score": 21,
        "body": "Ugh\u2026for real! We live rural, and my neighbor is a complete douche! Burns his garbage (plastics and all), whenever I smell it \u2026 the rage! \ud83d\ude21"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1j8yhv8",
    "title": "Thank You VA411",
    "body": "I got some Community Care through the VA. Then the hospital that performed the Community Care sent me the bill not the VA. It was over $1000. When I got the bill I called the hospital billing office and told them it  was paid for by the VA. The billing dept said they'd look in to the issue 'soon'.  \nWhat did I do?  I called VA411 and got through to the Community care phone. And lucky me I got help from a young man who said to my story \"I'm the guy who will fix that for you.\" So he kept me on line , called the billing department separately sorted out the paperwork, then told me the end results , dates etc.\n\nAll fixed. Total time 11 minutes!!!!\n\nThank you VA411!!!\n\nEDIT: I forgot to give the VA411 phone number 800-698-2411 END EDIT",
    "flair": "Health Care",
    "score": 367,
    "comment_count": 47,
    "created_at": "2025-03-11T18:57:01+00:00",
    "top_comments": [
      {
        "id": "mh97etx",
        "score": 94,
        "body": "[removed]"
      },
      {
        "id": "mh9te1i",
        "score": 36,
        "body": "I totally agree. Today\u2019s VA is not the crappy VA that was years ago."
      },
      {
        "id": "mh9thkr",
        "score": 12,
        "body": "VA Community Care (CC) employee here. Glad you were able to get it resolved. When referred to CC, always ask them for a copy of your referral/authorization. It will have your referral/authorization number, valid dates and what services are covered. It comes in handy if you receive a bill in error. Just call the billing provider and give them the auth info."
      },
      {
        "id": "mhaio8g",
        "score": 11,
        "body": "I agree to that. On a regular check up, I was given a form to fill out. That nurse is why I'm still around today..."
      },
      {
        "id": "mh95es7",
        "score": 9,
        "body": "It takes a while but they will pay it. I get my dental care through the VA and they send me bills all the time.  My dental place KNOWS the VA pays for it and told me not to worry and that the bills go out automatically.  I became concerned when it had been four months but then it was finally paid. \n\nAll that to say, the medical facility you went to should know you were community care referred because they have to register in the community care system. It\u2019s not like the VA just sends people out all Willy nilly, they can only send to places that are willing to accept that form of payment. \n\nCall the facility and make sure they are aware you got the bill, remind them it\u2019s through VA community care, and you should be good to go. Not every employee knows about community care so them \u201clooking into it\u201d is a good thing. Don\u2019t worry!"
      },
      {
        "id": "mh94jbu",
        "score": 7,
        "body": "I had a similar experience with a community care provider trying to charge me for something \u201cinsurance doesn\u2019t cover\u201d . I called the number on the back of my statement of care and she immediately called the person with me on the line. She asked if the office needed to be retrained because veterans will never have to pay anything out of pocket. I was impressed."
      },
      {
        "id": "mh9vkyr",
        "score": 5,
        "body": "I didn't know that. I think everybody reading your post  is benefiting from your suggestions."
      },
      {
        "id": "mhboedt",
        "score": 5,
        "body": "And pay attention to the dates! If your authorization ends on a certain date, get a NEW AUTHORIZATION before being seen again."
      },
      {
        "id": "mhhyq2k",
        "score": 5,
        "body": "Idk. The physical health side is great and I haven\u2019t had too many issues, but the mental health leaves a lot to be desired with the primary care providers. I have yet to have one where I actually feel like they\u2019re being beneficial, with my latest diagnosing me with Borderline Personality Disorder and not telling me she was giving me that. I had to find out by being recommended to a group therapy session that was designed for BPD patients, but when I asked her if that would work since I didn\u2019t have that, she said \u201ceven though you don\u2019t, I think it would work.\u201d \n\nIt took me talking to the scheduler to find out that I indeed **was** diagnosed, so when I went back to talk to my psych about it, she told me \u201cthis isn\u2019t up for discussion. I know what I\u2019m doing here and you need to just accept it.\u201d And since then, she had been extremely cold and unresponsive to me up until this Valentine\u2019s Day, where I had waited 120+ days for an appointment with her only to have her cancel an hour prior. \n\nHaving dealt with govt psychs since the Army, I\u2019m just about positive at this point that these guys suck, so I\u2019m only utilizing them so I keep my benefits and I\u2019ll get mental help elsewhere."
      },
      {
        "id": "mhbaysg",
        "score": 5,
        "body": "I had 2 surgeries using Care in th Community and the same outside Dr. His office kept trying to bill my regular insurance (because they pay the Dr more per their contract) and then when they finally billed the VA, they coded it wrong and way over charged. Also called my pain mefs to CVS and finally got them to send it to the VA pharmacy.  ALL this info was in the packets they got from the VA but the 70yr old office manager thought she knew better."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1jdh6d7",
    "title": "Trump administration announces end to gender-affirming care for transgender veterans",
    "body": "",
    "flair": "Article/News",
    "score": 364,
    "comment_count": 10,
    "created_at": "2025-03-17T16:41:23+00:00",
    "top_comments": [
      {
        "id": "miagohn",
        "score": 112,
        "body": "As a trans veteran who works as a VA nurse, this announcement is fun \ud83d\ude43."
      },
      {
        "id": "miafkih",
        "score": 83,
        "body": "Craziness. The number of super aggro dudes I knew under the SF umbrella that ultimately transitioned after leaving service is shockingly high. People struggling with gender dysmorphia overwhelmingly try to conform to their born identity - a huge portion of an already small population joins the military for that reason alone. More gross behavior from this admin \ud83d\ude12"
      },
      {
        "id": "miagek1",
        "score": 31,
        "body": "I think the world would be a very dreary, dark place without rainbows. Sincerely."
      },
      {
        "id": "miajqzl",
        "score": 2,
        "body": "[removed]"
      },
      {
        "id": "miajau7",
        "score": 1,
        "body": "[removed]"
      },
      {
        "id": "miajvnk",
        "score": -5,
        "body": "Thank you sin_seranade for your submission to r/veterans, but it's been removed due to one or more reason(s):\n\nRule 1\n\nBe civil and respectful. You may not always agree with others but once you start insulting the other person, you are a problem. You are not winning the argument by calling them names or calling out their reddit profile history. \n\nNo Gatekeeping \n\nYou don't decide if someone is a \"real\" veteran or not - nor try to diminish someone's service because they never saw combat or deployed. \n\nIf someone personally attacks you, Report them to the mod team. \n\nHate speech can be sexist, ableist, racist, bias, bigotry, homophobic, prejudiced, etc and will not be tolerated.\n\nSee our Wiki for more details on this rule.\n\nhttps://www.reddit.com/r/Veterans/wiki/rules\n\n\n\nPlease feel free to [send a modmail](https://www.reddit.com/message/compose?to=%2Fr%2Fveterans) if you feel this was in error."
      },
      {
        "id": "miajtp2",
        "score": -10,
        "body": "Thank you Odd-Meat-1988 for your submission to r/veterans, but it's been removed due to one or more reason(s):\n\nRule 1\n\nBe civil and respectful. You may not always agree with others but once you start insulting the other person, you are a problem. You are not winning the argument by calling them names or calling out their reddit profile history. \n\nNo Gatekeeping \n\nYou don't decide if someone is a \"real\" veteran or not - nor try to diminish someone's service because they never saw combat or deployed. \n\nIf someone personally attacks you, Report them to the mod team. \n\nHate speech can be sexist, ableist, racist, bias, bigotry, homophobic, prejudiced, etc and will not be tolerated.\n\nSee our Wiki for more details on this rule.\n\nhttps://www.reddit.com/r/Veterans/wiki/rules\n\n\n\nPlease feel free to [send a modmail](https://www.reddit.com/message/compose?to=%2Fr%2Fveterans) if you feel this was in error."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1kqf7wh",
    "title": "Scam Alert Please Read and Don\u2019t Fall For It",
    "body": "Just wanted to let you guys know about a scam that almost got me, so hopefully it doesn\u2019t get you guys. I had a phone call come in three times back to back, same number too. I finally answered and it stated someone was attempting to login to my ID.me account and said if it wasn\u2019t me to press 1. After pressing one I immediately got a text from ID.me with a six digit code. The automatic voice system then told me to enter it. I DID NOT. But I reset my password from my computer and the calls did not stop. I got a total of 9 calls. All same number and back to back. \n\nI wanted others to know because it happened so fast that I almost fell for it. Please let others know as well.",
    "flair": "Question/Advice",
    "score": 356,
    "comment_count": 74,
    "created_at": "2025-05-19T15:54:26+00:00",
    "top_comments": [
      {
        "id": "mt5m5cu",
        "score": 88,
        "body": "Cybersecurity professional here.  You absolutely did the right thing here, OP.  We've been seeing a lot of this kind of stuff lately.  The scammer calls and tries to trick you into giving them the 2FA code for the password reset they just initiated on your account. You should never share 2FA codes you get with anyone."
      },
      {
        "id": "mt55us7",
        "score": 57,
        "body": "This is a common scam with all sorts of online accounts.  They're trying to change your password so they can hijack your account.\n\n\nHaving you press 1 at the beginning of the call does two things.  First, it lets them know they've got a human on the line and second, it starts to condition you to doing what they say."
      },
      {
        "id": "mt5butb",
        "score": 35,
        "body": "Huh, I've been wondering who could possibly want to get into my VA stuff, but apparently people do.  Guess I'm glad for the 2FA logins now. . ."
      },
      {
        "id": "mt5mxbu",
        "score": 34,
        "body": "If they can get into your VA Account, they can change your direct deposit information to their own account"
      },
      {
        "id": "mt54k65",
        "score": 20,
        "body": "Thank you for sharing this."
      },
      {
        "id": "mt5yiwd",
        "score": 15,
        "body": "Yeah, that's fair.  I always think of it just as my medical info, which, like, if you really feel like getting depressed, go for it."
      },
      {
        "id": "mt5pdqp",
        "score": 14,
        "body": "My wife put something on facebook for sale and craigslist. They texted her pretending to be interested,  then they told her to send them the code to verify she is a real person. Luckily I saw it happening and told her to never do that. I said why would someone on Facebook want a google voice code.\n\nThe really crazy ones nowadays are the pig butchering scams and how sophisticated they have become. Its insane"
      },
      {
        "id": "mt6nq2q",
        "score": 14,
        "body": "Hmm.  Sometimes I worry I'm something of an evil bastard, and then things like this come along and that kind of thing hadn't even crossed my mind.  And I'm suddenly reminded that, no, I'm not an evil bastard, just a surly dick."
      },
      {
        "id": "mt65k4u",
        "score": 13,
        "body": "They can steal your entire identity with what the va has on file. It would be very very bad if someone hacked your va.gov account. Social, medical history, address, direct deposit information."
      },
      {
        "id": "mt5boda",
        "score": 12,
        "body": "r/scams"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1r39thz",
    "title": "Never felt a gut punch like this before.",
    "body": "It\u2019s been 20 years since my deployment to Iraq. During my time before and after I had the privilege of serving with a SSG who became a great friend and inspiration. After we got out we lost touch. This morning as my wife and I were laying in bed some feeling came through me. I couldn\u2019t place it and as my wife was asking what\u2019s wrong I asked her to look him up on social media. He had died a few weeks ago. I\u2019ve never felt an emotional drunkenness or gut punch like this before. I just wanted to talk about this to the only people who understand the bond of brotherhood.",
    "flair": "Question/Advice",
    "score": 357,
    "comment_count": 43,
    "created_at": "2026-02-12T23:59:55+00:00",
    "top_comments": [
      {
        "id": "o5305we",
        "score": 86,
        "body": "I don\u2019t think your feeling to look him up was a coincidence"
      },
      {
        "id": "o533qgz",
        "score": 65,
        "body": "It's hard to come to terms with not knowing that the last time you talked to someone was the last time you would talk to them."
      },
      {
        "id": "o5328ss",
        "score": 50,
        "body": "It sucks to lose people we served with. \n\nI recently lost a battle of mine who died of brain cancer. \n\nHe was dead within four months of them catching the brain cancer. \n\nIt was pretty awful."
      },
      {
        "id": "o5326uv",
        "score": 43,
        "body": "I don\u2019t think it was either. I\u2019ve never felt this much emotional pain. My chest is so tight and heavy. Hell I was more cool calm and collected when I was down range."
      },
      {
        "id": "o532te2",
        "score": 36,
        "body": "Maybe it was your friend reaching out to you to say he\u2019s safe. Maybe it was your intuition or you saw something somewhere that urged you to think of him. Or maybe it was maybelline \ud83d\ude0e who knows. I\u2019m sure your friend is and was proud of you and had fond memories of you as well."
      },
      {
        "id": "o53bw5i",
        "score": 17,
        "body": "Had a it happen more than once unfortunately. Most recently this fall. Got to thinking about a buddy for a few days in a row - had someone reach out with the news that he\u2019d lost to his demons. #22istoomany \n\nMy condolences for your loss. We are all here for you however you need us \ud83d\udc4d"
      },
      {
        "id": "o5328k8",
        "score": 11,
        "body": "So sorry for your loss. \n\nYeah, I\u2019ve had \u201cfeels\u201d and dreams like that and I make an effort to reach-out to them (if I still have a method).  Buddy checks are very rarely wrong.  They may wonder why you\u2019re thinking or dreaming of them, but I believe it\u2019s appropriate."
      },
      {
        "id": "o53f1b0",
        "score": 8,
        "body": "I'm really sorry for your loss.   \n  \nAs we get older we lose more and more friends. It's a sad reality. It's best to cherish the memories while we have them.\n\nI don't remember who said it (maybe our unit's chaplain), but he said about someone we lost, \"One day we'll all rendezvous on the high ground.\" The thought that we can all be together one day, and putting it into military parlance, was helpful to me."
      },
      {
        "id": "o53ssav",
        "score": 5,
        "body": "I left the Aemy in 2012, dealt with immediate loss during and after deployments like everyone else...that part seemed easy at the time...this many years later it's harder to accept and understand...it seems like the only time is current bad news...but this feels more like real life than it did back then. Sorry for your loss, but remember that they've had a lifetime of living since then...be happy for them."
      },
      {
        "id": "o53ze40",
        "score": 5,
        "body": "On first Covid Easter, I received a call at 3 am. Phone was on silent. I never received calls after 11 for at least a decade. Never called that number back but I had this strange feeling, not about the missed call but like something was wrong. Few days later a buddy texted me asking me about a friend that I introduced him to. He asked me if I heard? I didn\u2019t have social media so I didn\u2019t know what he was talking about. My best friend from high school passed a way from Covid at 35 years old. I still can\u2019t forget about that \u201csomething is wrong\u201d feeling. I tell myself that he had someone call me from the hospital to say goodbye."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1px86qb",
    "title": "I use D&D to help with my PTSD",
    "body": "Greetings adventures. Over the past 7 years, I have used D&D as a way to express, address, and confront themes from the trauma I've suffered throughout life. Every week, I spin tales of horror, drama, suspense, and emotion as I sit around with a group of friends and play Dungeons and Dragons. \nAt the age of 17 I enlisted in the Army as a airborne combat medic. Afghanistan still weighson me. 16 years of practicing medicine later, I work with patients on life support. I've seen more death and suffering than I can remember, but I use this pain, darkness, anxiety, and trauma to enthrall my players into a dark campaign through the hells. After trying to stop the bleeding caused by weapons of war, I'm great at describing in graphic detail the wounds my players suffer at the hands of enemies. I tell them tales of fictional characters suffering\nbased off of real people I've watched wither and die. D&D helps me cope. I can feel and share my pain in a productive way that provides catharsis.\n\nIt's pretty common for the players and I had to cry at my table. Not every campaign I try to run gets dark but it's just a wellspring of inspiration that I can tap into.\n\nDo any of you use creative outlets like this? If so, I'd love to hear about them. ",
    "flair": "Discussion",
    "score": 360,
    "comment_count": 69,
    "created_at": "2025-12-27T20:48:23+00:00",
    "top_comments": [
      {
        "id": "nw94ww6",
        "score": 26,
        "body": "I really like your setup, especially the gumball machine full of dice, really creative!"
      },
      {
        "id": "nw97i44",
        "score": 18,
        "body": "The rec therapy department at my VA used to have a D&D group, it was great! Sadly the group was discontinued due to budget cuts."
      },
      {
        "id": "nw9x7n0",
        "score": 15,
        "body": "May you always roll a NAT 20 in life!"
      },
      {
        "id": "nw9tce5",
        "score": 13,
        "body": "Fucking ded at \u201cKevin\u2019s Judgement Tower\u201d \ud83e\udd23\ud83e\udd23"
      },
      {
        "id": "nw9m6le",
        "score": 8,
        "body": "I like your Hylian Shield on the wall"
      },
      {
        "id": "nwa0zj5",
        "score": 8,
        "body": "Sick room man, centerpiece in the first photo reminded me of the Spectator from Baldur's Gate 3. Hobbies are a good thing and investing yourself into something so directly is nothing to be awakes of. I got out and started buying every console I never had as a kid, now I have access to every game on every console. It's a good time."
      },
      {
        "id": "nw965ub",
        "score": 7,
        "body": "I play rpgs, read and write. A little of my ptsd ends up in every story, but its an amazing outlet and Ive found a lot of what i write isnt tragic or dark at all. I would love to game (i run a 3d print shop) but my kids dont really have the patience to sit down and play with me yet. Lol \n\nLove the set up!"
      },
      {
        "id": "nwa0g03",
        "score": 7,
        "body": "You too, my friend. You too."
      },
      {
        "id": "nw98rf4",
        "score": 6,
        "body": "D&D was one of those things I could take pleasure in, but haven\u2019t really been looking for it. I have tried online games like Elders Scroll Online and Destiny 2. I used it as a way to learn how to deal with civilians and control my PTSD symptoms. After about ten years of playing though, it consumed too much of my life and had to let it go."
      },
      {
        "id": "nw99joh",
        "score": 6,
        "body": "Wished you lived in Vegas brother. I have an ass ton of minis and love D&d. Also in the medical field. I\u2019m a perma dm and would love to be on the other side sometime \ud83d\ude02"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1pjk2iy",
    "title": "Welcome home, Superman!",
    "body": "NASA Astronaut Jonny Kim displays traditional matryoshka doll after safe Soyuz MS-27 landing in Kazakhstan. He spend 8 months in space aboard the International Space Station. \n\nReturned to earth on December 9, 2025\n\nLCDR Kim enlisted in the Navy as a Seaman recruit after graduating high school in 2002.\n\nAfter completing Hospital Corpsman \u201cA\u201d school training, he reported for Basic Underwater Demolition/SEAL (BUD/S) training in Coronado, CA.\n\nAfter completing his training at Naval Special Warfare, Kim reported to the John F. Kennedy Special Warfare Center and School in Fort Liberty, NC, for the Special Operations Combat Medic Course.\n\nHe was assigned as a Special Warfare Operator to SEAL Team THREE in San Diego and obtained various qualifications, including:\n\nMilitary Freefall Parachutist\n\nAdvanced SCUBA\n\nCombatant Diver (closed circuit rebreather)\n\nNaval Special Warfare Special Reconnaissance Scout and Sniper\n\nand Advanced Special Operations Techniques\n\nKim served as a special operator on more than 100 combat operations in support of Operation Iraqi Freedom.\n\nIn 2012, Petty Officer First Class Kim was commissioned as a naval officer through the Navy\u2019s enlisted-to-officer commissioning program, Seaman to Admiral-21, following graduation from the University of San Diego with a Bachelor\u2019s degree in Mathematics, summa cum laude.\n\nHe obtained his medical degree from Harvard Medical School and completed his internship with the Harvard Affiliated Emergency Medicine Residency at Massachusetts General Hospital and Brigham and Women\u2019s Hospital in Boston, MA.\n\nKim is an Aeromedical Dual Designated (AMDD) Naval Aviator and Flight Surgeon. He completed his primary flight training at Naval Air Station (NAS) Corpus Christi, TX, helicopter advanced flight training at NAS Whiting Field in Milton, FL, and the Naval Flight Surgeon course at the Naval Aerospace Medical Institute at NAS Pensacola, FL.\n\nSpaceflight Experience:\n\nOn April 8, 2025, Kim launched to the International Space Station aboard the Soyuz MS-27 spacecraft, accompanied by Roscosmos cosmonauts Sergey Ryzhikov and Alexey Zubritsky.\n\nHe spent eight months aboard the station as an Expedition 72/73 flight engineer, conducting science experiments and maintaining the space station.\n\nHe returned to Earth on December 9, 2025.\n\nDuring the science expedition, Kim logged 245 days in space, orbiting the Earth 3,920 times and traveling nearly 104 million miles. He saw the arrival of nine visiting spacecraft and the departure of six during his time in orbit.\n\nAwards & Honors:\n\nSilver Star Medal\n\nBronze Star Medal with Combat \u201cV\u201d\n\nNavy and Marine Corps Commendation Medal with Combat \u201cV\u201d\n\nCombat Action Ribbon and various campaign and service awards\n\nCommodore\u2019s List with Distinction, Naval Advanced Flight Training\n\nNaval Special Warfare Medic of the Year\n\nSpecial Operations Medical Association\n\nCommandant\u2019s List, Special Operations Combat Medic Course, Joint Special Operations Medical Training Center (JSOMTC)\n\nSEAL Junior Sailor of the Quarter, SEAL Team THREE\n\nDistinguished Honor Graduate\n\nNavy Hospital Corpsman (HM) \u201cA\u201d School\n\nTillman Scholar, Pat Tillman Foundation\n\nPhi Beta Kappa, Kappa Gamma Pi, and Mortar Board Honor Societies\n",
    "flair": "Article/News",
    "score": 359,
    "comment_count": 27,
    "created_at": "2025-12-11T00:57:14+00:00",
    "top_comments": [
      {
        "id": "nteoh48",
        "score": 55,
        "body": "I don\u2019t know of anyone that has achieved so much as this dude. Proud to call him shipmate. Go Navy!"
      },
      {
        "id": "ntem9xy",
        "score": 42,
        "body": "[deleted]"
      },
      {
        "id": "ntgnyqi",
        "score": 19,
        "body": "His parents are still disappointed in him. Where is his law degree?"
      },
      {
        "id": "ntfpzft",
        "score": 13,
        "body": "Jonny Kim is the only thing that Chuck Norris is scared of"
      },
      {
        "id": "ntesqgb",
        "score": 10,
        "body": "Me, too, and I'm not even a dude!"
      },
      {
        "id": "ntemv65",
        "score": 8,
        "body": "[TLDR](https://youtube.com/shorts/nfkGzMrtEh4?si=K1V_KMZygyk-IACw)"
      },
      {
        "id": "nter8f3",
        "score": 7,
        "body": "I have the weirdest boner right now"
      },
      {
        "id": "nth8zln",
        "score": 6,
        "body": "Read about his childhood, came out of an insane environment and explains his incredible resilience.  Perfect example of extreme pressure creating a diamond."
      },
      {
        "id": "ntemtht",
        "score": 5,
        "body": "You don\u2019t burn too much energy floating\u2026.maybe. But I agree BAMF for sure"
      },
      {
        "id": "ntgpelv",
        "score": 4,
        "body": "Yikes."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1mtvy8f",
    "title": "Paramount plus gives 50% off for veterans",
    "body": "Just found out that paramount plus gives a 50% off discount to veterans, it was difficult to find through the paramount website but a quick google search brought me straight to the correct page where I was able to verify service.",
    "flair": "Discussion",
    "score": 357,
    "comment_count": 87,
    "created_at": "2025-08-18T19:29:58+00:00",
    "top_comments": [
      {
        "id": "n9emnwi",
        "score": 64,
        "body": "Correct, this is through SheerID\n\n[https://shop.sheerid.com/product/military-discount-50-off-any-plan-for-life/](https://shop.sheerid.com/product/military-discount-50-off-any-plan-for-life/)"
      },
      {
        "id": "n9f2mmp",
        "score": 36,
        "body": "Free w/Walmart+"
      },
      {
        "id": "n9en6g8",
        "score": 18,
        "body": "I think I pay like $1.99 for paramount!"
      },
      {
        "id": "n9fqmd9",
        "score": 18,
        "body": "Now all they have to do is have something worth watching"
      },
      {
        "id": "n9h0v54",
        "score": 17,
        "body": "Active duty can get the Amex Platinum which gives them Walmart+, thus Paramount+ too"
      },
      {
        "id": "n9eszhi",
        "score": 12,
        "body": "Neat! Thanks for this. I found [this article](https://www.military.com/discounts/best-military-discounts-streaming-services.html) about more of them too"
      },
      {
        "id": "n9fveor",
        "score": 12,
        "body": "I got verified got my discount code but when I tried to use it it said it was invalid."
      },
      {
        "id": "n9evzo2",
        "score": 11,
        "body": "You can contact support and have them flag your account as a veteran member and it will stay that way. They may require you to send proof."
      },
      {
        "id": "n9fnjp9",
        "score": 11,
        "body": "Mine is the same, it was the black Friday promotion"
      },
      {
        "id": "n9fb5uo",
        "score": 10,
        "body": "This is a huge steal for ufc fans"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1peiig5",
    "title": "Suicide confirmed in parking lot of Audi Murphy VA Hospital, patrol officer says",
    "body": "Check on your people, folks.",
    "flair": "Call for Help",
    "score": 356,
    "comment_count": 81,
    "created_at": "2025-12-05T01:50:29+00:00",
    "top_comments": [
      {
        "id": "nscrzod",
        "score": 168,
        "body": "If you feel like you've heard this story before, it's probably because you have. Veteran suicides at VA hospitals are on the rise.\n\n\nhttps://www.onceasoldier.org/category/va-parking-lot-suicides/"
      },
      {
        "id": "nscskja",
        "score": 82,
        "body": "There are no better days without you. Please stay."
      },
      {
        "id": "nsd354c",
        "score": 64,
        "body": "As a mom left behind and a veteran, I can assure you that we are not better without you, and never will be. Please reach out, we're here to take that hand."
      },
      {
        "id": "nsdagnb",
        "score": 55,
        "body": "As a vet who isn't getting the help they need because the VA is nigh useless, it's really tough. It's an everyday battle, and I for one am exhausted."
      },
      {
        "id": "nscx0bd",
        "score": 42,
        "body": "A couple years back I called the suicide line when I was mentally down bad. I was a broken man and needed to talk to someone. You know what they had to say? Pretty much just read off a script."
      },
      {
        "id": "nsd3gt3",
        "score": 38,
        "body": "with the way the some of the mental health folks at the VA treat peoples its a wonder it doesnt happen more often"
      },
      {
        "id": "nse957q",
        "score": 33,
        "body": "Constantly having to form a new relationahip or retell your story due to the turnover rate of counselors and psychiatrists doesn\u2019t help either."
      },
      {
        "id": "nsd0es9",
        "score": 30,
        "body": "I have to go to Audie Murphy for a lot of my stuff. Parking there is a nightmare. This really hit me hard for some reason."
      },
      {
        "id": "nsddx0v",
        "score": 29,
        "body": "I felt worse after calling the suicide line.\n\nLike I didnt even matter to them. Sure, im just a voice and they are probably doing it because its a job, but could you please not phone that job in? There are so many other jobs you can phone in."
      },
      {
        "id": "nscsgvi",
        "score": 24,
        "body": "Fucking shame. Hate to hear that a brother or sister thought that was the only way out.\n\nBe there for each other."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1looh6g",
    "title": "The least expected call from the VA",
    "body": "\nA few hours ago I got a call from the VA letting me know that my appointment with my Psychiatrist had been canceled and needed be rescheduled. \n\nNormal enough I\u2019ve had that before but I asked the operator when I could see my psychiatrist who has been treating me through the worst of times and his been an amazing VA psyche for the last 5 years. \n\nInstead I was told that he passed away. That\u2019s why they need to reschedule me. \n\nI don\u2019t know why I am crying so hard. Thinking over this. He was someone who actually cared. I\u2019ve never had this situation before. I just want to offer condolences to his family and tell them how much he helped. \n\nThat\u2019s all. ",
    "flair": "Question/Advice",
    "score": 348,
    "comment_count": 34,
    "created_at": "2025-07-01T00:55:03+00:00",
    "top_comments": [
      {
        "id": "n0ohlvq",
        "score": 53,
        "body": "I am so sorry for your loss. I know its a helluva shock and we grow so close to our therapists when we have a good one. I hope knowing how much he cared about you is a comfort."
      },
      {
        "id": "n0oimfu",
        "score": 28,
        "body": "I\u2019m sorry for your loss. I have a therapist that I feel really close to, I can relate. Just remember the good conversations and advice that he gave you. If there is a heaven, you know that he\u2019s there."
      },
      {
        "id": "n0orlat",
        "score": 20,
        "body": "Thank you brother. I actually did. I hope they know how many of us he helped. If anyone goes to Sepulveda VA medical center and has experienced Dr Ghaznavi as a MH provider and he helped please share if you don\u2019t mind."
      },
      {
        "id": "n0olxkl",
        "score": 17,
        "body": "I'm so sorry for your loss.\n\nIf you wish to reach out to his family, watch the obituaries and they will tell you what the family would appreciate."
      },
      {
        "id": "n0okzju",
        "score": 15,
        "body": "I completely understand your grief. My psychiatrist passed away in a car accident a couple of years ago. I\u2019m sorry for your loss."
      },
      {
        "id": "n0ry26h",
        "score": 10,
        "body": "Is this him my friend? I'm so sorry for your loss. \n\nJahangir Hussain Ghaznavi - 2025 - Conejo Mountain Funeral Home Memorial Park & Crematory https://share.google/8Tibfg6GoQj9tX6KQ"
      },
      {
        "id": "n0tbomo",
        "score": 8,
        "body": "@jcoll9708 That\u2019s him. I didn\u2019t want to put his info out there because this is the time for the family. And I am just a patient so it would be taking away from his service if I went. His son is also a psychiatrist and he did his residency at the VA too. I just want his family to know how much he helped and the gratitude he\u2019s owed. \n\nThank you to everyone who responded to this post. I know it\u2019s a bit strange having a vet crying about his psyche. Instead of yelling at him. If any of you do go to the Sepulveda VA and you remember him. Please pass on the good memories."
      },
      {
        "id": "n0oo9x9",
        "score": 4,
        "body": "I'm so very sorry."
      },
      {
        "id": "n0oq5as",
        "score": 4,
        "body": "Aww ma'am that really sucks. Seems my shrink changes every year or so. Interns I guess. Mine have all seemed to care a good bit. Had a beautiful one a while back and she actually made me look forward to sitting in rush hour traffic to see her. Hope you find another good one."
      },
      {
        "id": "n0unvbn",
        "score": 4,
        "body": "Absolutely normal that you would be mourning the loss of someone important to you. As you said, he genuinely cared and had been making a difference in your life for five years. Enough so that you feel strongly about wanting to tell his family how much of a difference maker he was.\n\n My condolences to you, his family, and all the other veterans he must've been helping as well. I hope you're able to find another doc that's just as good! A doc you trust and feel is good for you is just as important as the treatment itself."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1kmtjbe",
    "title": "Congress pushes VA to explain why it regularly overpays veterans and then asks for the money back",
    "body": "",
    "flair": "Article/News",
    "score": 352,
    "comment_count": 95,
    "created_at": "2025-05-14T23:17:52+00:00",
    "top_comments": [
      {
        "id": "msd1ep3",
        "score": 140,
        "body": "Thassa good question"
      },
      {
        "id": "msddz6a",
        "score": 88,
        "body": "Wait till you hear about the military."
      },
      {
        "id": "msekwd3",
        "score": 87,
        "body": "[removed]"
      },
      {
        "id": "msdgqyu",
        "score": 61,
        "body": "\"Hey supply, here's the request for a replacement circuit board for x,y,z weapon system. I think it can wait until we get back home, but this commander taking a ridealong says it's mission critical because he wants to keep blasting active SONAR for the next 12 hours because he's convinced there's Russians nearby.\" \n\nWe're in the middle of the fucking Atlantic Ocean, and this commander had a helo deliver a tiny ass circuit board the size of a DIY raspberry-pi. It cost us around $20k just for the part alone, for something I could have re-soldered and repaired myself-- like they trained me to do. But god forbid they utilize that training investment before pandering to the big companies with military contracts."
      },
      {
        "id": "msd6kiv",
        "score": 41,
        "body": "I can't wait to hear what their response was."
      },
      {
        "id": "msdfxxv",
        "score": 33,
        "body": "Probably because the systems run on abacuses powered by doped up squirrels running on wheels."
      },
      {
        "id": "msd8r7l",
        "score": 32,
        "body": "We made and oopsie so fuck the veteran."
      },
      {
        "id": "msdkeld",
        "score": 29,
        "body": "This drove me insane, replacing entire boards at dumb prices 10K+ when you could physically see it was just a blown capacitor, god forbid they let me actually troubleshoot and fix it."
      },
      {
        "id": "msdkr7w",
        "score": 24,
        "body": "This shit drove me up the fucking wall. \nYou would think while in a submarine, surely you don't wanna surface for a supply run when we can fix this internally? \n\n\" No, fuck you, write the supply req.\"   \ud83d\ude11"
      },
      {
        "id": "msd9evx",
        "score": 23,
        "body": "Because regularly underpaying would be worse?"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1o8jhok",
    "title": "I think I ruined my life",
    "body": "This shit sucks dude. I joined the Army in 2017 to escape poverty, drug addiction, depression, and became an intelligence analyst. I thought I really turned my life around and that I could do anything after that. I was highly successful in the Army, got out and went to school.\n\nWas doing great in school. 3.8 GPA, Dean's List, multiple leadership roles. A couple different things happened. A several year long relationship of mine ended, it slowly got too expensive to live, my school had a mass shooting, and one of my best friends I served with took his own life. \n\nI moved back into my parent's, which wasn't a good idea either, as they charged me essentially rental price to live with them. I got zero emotional support from my family after everything had happened. \n\nI bounced around some jobs. My girlfriend got pregnant. We live together now, with our baby, and despite me working full time, we don't make enough to pay the bills. I feel like everything I did in life was for nothing.",
    "flair": "Discussion",
    "score": 347,
    "comment_count": 156,
    "created_at": "2025-10-16T21:54:42+00:00",
    "top_comments": [
      {
        "id": "njvdg4o",
        "score": 336,
        "body": "You haven't ruined your life, you hit a rough spot... Time to plan a path forward and implement it... \n\nFind a career counselor, discuss your options and your desires and get to it... The drive that you had while serving and while at school aren't gone, you simply got focused on other things... You may also want to get a personal counselors to help you get your mojo back..."
      },
      {
        "id": "njvj5b6",
        "score": 149,
        "body": "We all hit obstacles and throughout our lives . You got this , just keep pushing forward. \n\nSeveral years ago , I became homeless after an expensive, ugly divorce. Lost everything . I eventually filed for bankruptcy because I was being sued by a debt collection company. \n\nI now own my own home , have good credit , remarried , drive a badass truck . Have money in the bank .   I share my story because you can do anything you set your mind too"
      },
      {
        "id": "njvmli2",
        "score": 72,
        "body": "you\u2019re not dead from drug addiction. that\u2019s a huge win."
      },
      {
        "id": "njvmr1u",
        "score": 42,
        "body": "It could, in fact, be worse. At least there's that."
      },
      {
        "id": "njvu120",
        "score": 41,
        "body": "I second this! Sounds like life is getting rough but guess what you've been through tougher shit than this! It seems like a lot but if you're here In the states lookup your local VetCenter they got people who can help you get your mind right. Do your VA claim, through one of the veterans service organizations like the American Legion. Life threw you some lemons but guess what you're able to process it and talk about it that means you're in a great place to seek help! Don't let your pride drag you into struggling unnecessarily get out your lemon squeezer cry out some sugar water and let make these lemons into lemonade! You will crush this because this isn't bigger than you! this is the workout to help you realize what you are capable of! This is the character building chapter that helps you define the good times!"
      },
      {
        "id": "njvgweu",
        "score": 39,
        "body": "Transfer the credits to another school, you and the gf work opposite schedules to not have to pay for daycare. Hang in there, it\u2019s gonna be tough for a few years but you\u2019ll make it through."
      },
      {
        "id": "njvf66c",
        "score": 33,
        "body": "[deleted]"
      },
      {
        "id": "njvmucy",
        "score": 26,
        "body": "it could always be worse, AND what you\u2019re going through sucks."
      },
      {
        "id": "njvkby4",
        "score": 24,
        "body": "Charter Oak state college is very generous with the transfer credits and that BAH from the GI Bill could help. I was a sigint Marine, if you pm me your resume I can look it over and maybe give you an idea of possible contracting opportunities. You haven't done anything wrong. The struggle is real, especially with a new kid.\u00a0"
      },
      {
        "id": "njvq1sd",
        "score": 23,
        "body": "I went to college 4 different times and graduated when my first kid was 2. Years after I completed service. With the right mindset you've got this. It could be a night class at a time. Or slow steps to your goal. Or a second job. You'll figure it out. Keep grinding.\n\nI'm in my 40's and filed for bankruptcy 3 years ago after almost successfully ending my life and being alone and homeless.\n\nI own my home, 3 vehicles, and my 3rd child is on the way. There have been rough times but also many great times. This one moment in time doesn't define you. It's every step you take forward."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1n2h7vs",
    "title": "Job market is so bad",
    "body": "Applied for over 16 jobs since separating from the military, my resume is valid\u2026 I don\u2019t get what I\u2019m doing wrong. I network with ppl as well, at the point to where I feel like the military was a waste of time. I\u2019m even being denied Janitor jobs/applications just waiting for weeks. At this point I may just lie on all my applications.\n\n\n\n****Update**** \nSo random but since this post I\u2019ve gotten calls back from companies and I have interviews incoming \ud83d\udd25 universe works in strange ways",
    "flair": "Employment",
    "score": 343,
    "comment_count": 246,
    "created_at": "2025-08-28T16:37:25+00:00",
    "top_comments": [
      {
        "id": "nb5x6pr",
        "score": 115,
        "body": "Gonna be real, 16 jobs is nothing, even in a good job market."
      },
      {
        "id": "nb5srzn",
        "score": 86,
        "body": "You still have post 9/11 gi bill? Use it for a certificate or degree."
      },
      {
        "id": "nb5sxsr",
        "score": 39,
        "body": "That\u2019s what I\u2019m doing rn (trade school)"
      },
      {
        "id": "nb60l8z",
        "score": 29,
        "body": "Just my opinion, but there's a lot of saturation of applicants for part-time work at places like that. I suspect it's not something you're doing wrong it's that there are people with a lot more direct experience applying for those jobs.\n\nYou mentioned you're in a trade school, which is great. I recommend reaching out to veteran specific organizations that look to place vets with companies looking to hire them. You may be able to get an internship / apprenticeship in your future trade. \n\nhttps://www.hiringourheroes.org/career-services/fellowships/internships/"
      },
      {
        "id": "nb77d68",
        "score": 28,
        "body": "Agreed. 16 might seem like a lot if this is your first time after getting out that you\u2019re actively looking but honestly you should be pumping out like 5-10 applications per day at least if you\u2019re serious about finding work. Until you find a job, finding a job is your job."
      },
      {
        "id": "nb5th3c",
        "score": 19,
        "body": "Defense contractors usually give priority to veterans, and if you had a security clearance before getting out that will help even more."
      },
      {
        "id": "nb5xcp4",
        "score": 19,
        "body": "Everything almost but part time because I will be a full time student. Tried janitor, pet groomer/pet bather, ikea (store associate/stocking), gnc, JCPenney, Ross, finishline, adidas so many I can\u2019t even remember all of them"
      },
      {
        "id": "nb6vyqh",
        "score": 19,
        "body": "You\u2019re not getting those jobs because you deserve a better job. Real money and real benefits. Don\u2019t sell yourself short. I did when I first got out and wasted a year making $21 an hour. Focus on school, get that GI bill money. Apply for VA disability then apply for VR&E. Apply for jobs in your field. Be patient, it always works out!"
      },
      {
        "id": "nb5xnk1",
        "score": 17,
        "body": "It's much less \"government work\" than you think. I'm a defense contractor and work with both the civilian side and defense side. It's a fairly easy life without all the military bs. And it pays well"
      },
      {
        "id": "nb5zo7m",
        "score": 13,
        "body": "I'm working as a recruiter, we opened a job for software engineers and had 50 applicants in 3 hours. Tons of labor in the market, but not enough jobs. The whole economy is weaker than we are being told."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1relxiv",
    "title": "Would you, as a Veteran of Iraq/Afghan, like to see a VFW more catered to a different generation of Vet's?",
    "body": "Wife and I both Veterans. And when I talk to people who are also Vet's, they say they don't go to VFWs because of all the posturing and egotism. So I ask this, Would a VFW be more appealing if it catered more to a different generation or Vet's? ",
    "flair": "Question/Advice",
    "score": 336,
    "comment_count": 312,
    "created_at": "2026-02-25T18:45:05+00:00",
    "top_comments": [
      {
        "id": "o7dko2n",
        "score": 340,
        "body": "Yes, and it needs to be if the VFW wants to stick around."
      },
      {
        "id": "o7dy1r3",
        "score": 154,
        "body": "\ud83d\udc46100%\n\nAnd the same goes for the American legion.\u00a0\n"
      },
      {
        "id": "o7dnsp1",
        "score": 144,
        "body": "It's definitely a generational issue but I don't think catering to one over the other is going to help in the long run either.  Just tell members that they need to be accepting of all or they can find the door."
      },
      {
        "id": "o7dr4fa",
        "score": 123,
        "body": "The lack of ripits in the VFW is unsettling."
      },
      {
        "id": "o7dpbk4",
        "score": 101,
        "body": "The VFW and other similar organizations have always been that way, and if you really think about it, it's normal.  I joined the VFW in Vietnam.  At that time the Saigon post was run by Vietnam Veterans, but all of the ones in the States were WWII and Korea Vets. I'm sure it's the same now, perhaps not run by Vietnam vets because I just realized I'm 78 years old.\n\nTrust me, 25 years from now the veterans of the first interplanetary war will be complaining about you GWOT people who are running the organization.\n\np.s.  After leaving Vietnam I never bothered to keep up with any veterans organization, and I think that's the case with most vets.  Just move on."
      },
      {
        "id": "o7e6xub",
        "score": 71,
        "body": "This. Would love to get to know some of the \"Old timers\" but the disrespect shown by them toward veterans of newer wars is disgusting."
      },
      {
        "id": "o7f3oyw",
        "score": 52,
        "body": "My wife's grandfather was head of his VFW and got me to go a couple times. I had zero in common with those old boomer vets and zero interest with anything they wanted to do."
      },
      {
        "id": "o7ffqet",
        "score": 46,
        "body": "Legion seems to have gotten that memo, at least as far as their social media/advertising goes."
      },
      {
        "id": "o7g8ayv",
        "score": 46,
        "body": "It has started my friend, I joined in 2019 after retiring in 2015. I\u2019m now my VFW post\u2019s commander and Legions vice commander. Our posts are small, about 15 active members but we do a lot for our community and veterans.  3 free breakfasts a year for our community - anyone can come in and break bread with us. We even do a summer bbq specifically for our towns senior group. Also an inexpensive summer chicken bbq. But what we are most proud of is providing a full honor/color guard detail for every veteran\u2019s funeral in our county ensuring that no veteran is laid to rest without the dignity and respect they have earned through their service. There is no bar at either post and smoking is not allowed indoors. We do have a friendly nickel/dime poker game about two times a month and it\u2019s a byob deal but no one gets hammered. I\u2019m trying to steer both posts to start doing more family/kid friendly functions but I need younger members. I\u2019m one of the youngest at 57."
      },
      {
        "id": "o7dlid0",
        "score": 43,
        "body": "I'm a peacetime/garrison veteran. I know I'll be unwelcome as soon as I set foot in any establishment."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1lv4xdw",
    "title": "My employer told me to stop talking to veterans about their VA education benefits.",
    "body": "Hey Reddit, I\u2019m looking for some honest input here. For context, I\u2019m a professional recruiter in the education space\u2014I work for a school that trains students in skilled trades. I\u2019m also a disabled veteran who started recruiting in the Army over six years ago.\n\nRecently, I was working with a 60-year-old veteran who applied to our program from out of state. He has a VA disability rating and qualifies for Chapter 31 benefits (Voc Rehab), which would cover his tuition in full. The only thing he\u2019d need to pay out of pocket is housing since he\u2019s coming in from out of state.\n\nWe discussed options, and he asked me to help him find the most affordable way to get into training. I submitted his application under Chapter 31 benefits with our VA certifying official.\n\nThe school denied it.\n\nThey told me he\u2019d need to either finance the full tuition or pay it all upfront before they\u2019d even consider working with the VA. For context, tuition ranges from $5,600 to $10,000 depending on the track\u2014but for this veteran, it would cost $6,800 due to housing. All due upfront.\n\nTheir reasoning? It\u2019s \u201cfaster\u201d than waiting on the VA, and the sooner the student enrolls, the sooner we can \u201cget them a job.\u201d But obviously, this isn\u2019t what\u2019s best for the student\u2014it just forces a disabled veteran to take on debt he doesn\u2019t need to. And we know he\u2019s eligible for benefits that would fully cover him.\n\nIn a team meeting with all recruiters, my manager announced that we are no longer allowed to bring up Chapter 31 benefits until the veteran has no other way to pay. The new policy is: \u201cGet the money first, then if that fails, talk VA.\u201d He also sent me an email with that student\u2019s application attached and told me to refrain from discussing Chapter 31 with other veterans. I haven\u2019t replied yet.\n\nI believe what the school is really afraid of is that if a veteran is approved for Chapter 31, the VA might find them a closer school to use their benefits. But in my particular field, there just aren\u2019t many schools that accept Chapter 31\u2014so realistically, they\u2019d probably still end up choosing us anyway.\n\nIt\u2019s worth noting: veterans eligible for Chapter 31 make up a small portion of our student body. They\u2019re usually older and don\u2019t qualify for Post-9/11 GI Bill (Chapter 33). We maybe enroll 30\u201340 veterans per month total. So this isn\u2019t about volume\u2014it\u2019s about principle.\n\nAnd for me, this is the hill I\u2019m willing to die on. Either I put in my two weeks, or I get fired. But I\u2019m not going to withhold information from people who\u2019ve paid for their benefits with their bodies, time, and mental health.\n\nSo I\u2019m asking:\nWould you stay and try to fight from the inside, or walk away?\nHas anyone else dealt with something similar in the education or veteran services space?\n\nAppreciate any insight.\n",
    "flair": "GI Bill/Education",
    "score": 339,
    "comment_count": 178,
    "created_at": "2025-07-09T00:24:28+00:00",
    "top_comments": [
      {
        "id": "n237y9b",
        "score": 228,
        "body": "This is a for profit school, isn't it? A company, more than a learning institution....\n\nI ask as a tradesman who is a veteran and has used many different forms of schooling for my trades both VA covered and not. Your employer sounds like a piece of work. I'd walk, and see if there were a way to report them. Make the dishonesty hurt."
      },
      {
        "id": "n23le5b",
        "score": 49,
        "body": "Paper trail, paper trail, paper trail.\n\nNever discuss in person, or over the phone. Email, always. No exceptions.\n\nForward every single email to your personal, because the second they let you go they'll remove your work email access.\n\nPersonally, I wouldn't quit, I simply wouldn't comply.\n\nForce them to fire me, if that's the way they want to handle it.\n\nI'm sure an employment lawyer would have a field day with an employer telling a disabled vet he can't talk shop with other disabled vets."
      },
      {
        "id": "n23ah87",
        "score": 41,
        "body": "You\u2019re definitely misconstruing my terminology. I submitted his application for school approval under ch31 benefits, meaning on my side the school approves the vets application into the program. As he continues with his ch31 application process VR&E counselors contact us (depending on the regional office) for any information needed as-well as the letter of acceptance into our program."
      },
      {
        "id": "n2387s9",
        "score": 34,
        "body": "Do what you morally think is right. Is the policy I always follow."
      },
      {
        "id": "n238sia",
        "score": 28,
        "body": ">I submitted his application under Chapter 31 benefits with our VA certifying official.\n\nKey point - the veteran didn't apply to VA to be found entitled to VR&E and approved to attend this school. OP skipped a several month process and the VR&E actual approval."
      },
      {
        "id": "n246c45",
        "score": 19,
        "body": "I think you need to speak with your states veterans affairs dept or the VA directly about this. Your employer is most possibly breaking the law by their directive to you. Document everything they tell you because you'll need it. Verify anything they tell you with the VA or your state."
      },
      {
        "id": "n23qous",
        "score": 17,
        "body": "This is some really good advice. \nOnly thing I\u2019m worried about is the other recruiters ripping off vets. I can operate in the Shadows of course and play the game, I\u2019m unsure on what exactly to do. I may stew on it some more."
      },
      {
        "id": "n23d279",
        "score": 16,
        "body": "Can you just tell them about it anyway, but instead of trying to help them navigate the VR&E process, let them do that part on their own?"
      },
      {
        "id": "n23rva1",
        "score": 14,
        "body": "No problem with the VA at all (on this matter\ud83d\ude02)\n\nThis is definitely just me and my employer at a disagreement on when information should be passed along."
      },
      {
        "id": "n23v1xl",
        "score": 13,
        "body": "The simple answer is, send your manager an email confirming what you were told. Be very specific and spell out exactly what you are and are not allowed to say. BCC yourself. \n\nThen send an email to your State Rep and Senators explaining the school policy. Maybe add in a news station or two. \n\nBuy popcorn, sit back and watch the show."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1reaqlp",
    "title": "An Army pilot shot three times during the Maduro Raid just received the Medal of Honor",
    "body": "",
    "flair": "Article/News",
    "score": 341,
    "comment_count": 34,
    "created_at": "2026-02-25T11:29:16+00:00",
    "top_comments": [
      {
        "id": "o7b6z7x",
        "score": 210,
        "body": "Am I crazy, or was that kinda quick?"
      },
      {
        "id": "o7bfsnz",
        "score": 199,
        "body": "CWO5 Eric Slover is no doubt a top notch soldier, consummate professional and American hero.  I\u2019m sure he is deserving of the MoH, considering he was shot 3x and was able to execute his mission flawlessly, without crashing and saving the lives of his passengers onboard his CH-47.\n\nThat being said, I felt like he was being used as a political prop by Trump last night.  This is not CWO5 Slover\u2019s fault.  Just think following the normal MoH determination route, followed by a dignified ceremony, outside of the very politically charged State of the Union address, would have been more appropriate.  Just my opinion, feel free to disagree."
      },
      {
        "id": "o7bjxx0",
        "score": 101,
        "body": "I feel bad for the dude. He\u2019s going to have imposter syndrome and people aren\u2019t going to take his MoH seriously. That\u2019s a rough position. Going through that fast smacks of someone having an agenda. \n\nI\u2019m not saying he deserves the medal or doesn\u2019t deserve it. I just feel bad for the guy\u2019s situation."
      },
      {
        "id": "o7banao",
        "score": 89,
        "body": "I\u2019m not gonna shit on my aviation brother but yea, that was really fast. Politics has kept many from being rightly awarded the CMoH so I guess politics will also greatly accelerate it in some cases. \n\nPutting that aside, Slover has already shown he\u2019s among our badasses. "
      },
      {
        "id": "o7bf6u4",
        "score": 84,
        "body": "Not to belittle his award, but comparatively doesn\u2019t his citation appear a little\u2026weak? \n\nI\u2019m sure there\u2019s more that we don\u2019t know, but on the surface it reads\u2026weak"
      },
      {
        "id": "o7b98f6",
        "score": 84,
        "body": "The carrier he launched from is still deployed\u00a0"
      },
      {
        "id": "o7be2ig",
        "score": 73,
        "body": "I know the first guy to receive the MoH while still alive since Vietnam. I was deployed with him in OEF 8 and remember when they put him in for silver star for actions in Oct 07. We literally got back from deployment, he PCS'd, we trained up and deployed again in late 09. We got word that he had been upgraded and due to receive it around Fall of 2010 before we ended that rotation. So 3 years.\n\nThe other non posthumous MoH recepient i know went to another guy in my battalion from another company - Kyle White. Happened around late 07 but he didn't receive it until after I was out of the army (mid 2012). So 6+ years"
      },
      {
        "id": "o7bhfwk",
        "score": 68,
        "body": "Yeah. I am by no means the award gatekeeper or anything, and this dude is in no way in control of what award someone else submits on his behalf. And when you're in the military, you're a prop for someone or other pretty much all the time. So this is nothing against CW5 Slover. He had a job to do and he executed.\n\nBoth the speed and what I perceive to be a willful lack of rigor in writing and reviewing, threaten to cheapen the meaning of CMoH. It's clear what this was all about."
      },
      {
        "id": "o7bns6y",
        "score": 63,
        "body": "I was under the impression that the MoH was only awarded for actions during war."
      },
      {
        "id": "o7bdlw5",
        "score": 47,
        "body": "This felt like a political stunt."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1nredmb",
    "title": "I did a thing!",
    "body": "After being sedentary for a while, I decided to take a 4 mile hike. I did it in an hour and a half. Not bad for a 51 year old. ",
    "flair": "Discussion",
    "score": 335,
    "comment_count": 46,
    "created_at": "2025-09-26T22:04:46+00:00",
    "top_comments": [
      {
        "id": "nge3whi",
        "score": 19,
        "body": "Not bad at all keep it pushing"
      },
      {
        "id": "ngefosf",
        "score": 15,
        "body": "I need to do a thing more often."
      },
      {
        "id": "nge034x",
        "score": 13,
        "body": "Nice!"
      },
      {
        "id": "ngej9gr",
        "score": 11,
        "body": "Walks are underrated. Cardio is about time, not exertion. Plus, unless you're irresponsible, it keeps your nose out of your phone."
      },
      {
        "id": "ngef8x1",
        "score": 8,
        "body": "Hell yeah. That looks like a great walking neighborhood."
      },
      {
        "id": "ngfxee7",
        "score": 7,
        "body": "I don't measure the distance,  but the steps. After years of just barely getting 1500 to 2000 steps a day, now average 18000 to 20000 a day. Doing good for a 58 year old man, that still smokes,even lost the weight I wanted to."
      },
      {
        "id": "ngg72du",
        "score": 5,
        "body": "That wasn\u2019t what they meant when they suggested \u201cboxing\u201d \ud83e\udd23"
      },
      {
        "id": "ngegefl",
        "score": 5,
        "body": "Good for you getting out there, exercising and getting some fresh air!"
      },
      {
        "id": "ngftm9v",
        "score": 5,
        "body": "Awesome!  I need to get off my fat lazy ass and do the same thing"
      },
      {
        "id": "ngj56zn",
        "score": 4,
        "body": "I need to do this. I haven\u2019t really felt like doing much bc my knees and hip have been real bad lately but I feel like not doing much is a contributor so I\u2019m stuck in a catch 22"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1n46hll",
    "title": "Does anyone else encounter people lying about their military service almost always say they were a navy seal?",
    "body": "Once they find out I was in the navy they usually respond \u201coh really, me too!\u201d Then I ask what their rate was and they try to act all secretive like they can\u2019t tell me because they did highly classified seal stuff. \n\nThen when they keep talking, they include details that I clearly know is a lie because it doesn\u2019t make sense/possible. \n\nDoes this happen to other people in other branches or is it just because I was navy. \n\nDo you guys call them out or just give them a \u201cwow that\u2019s crazy\u201d then walk away? ",
    "flair": "Question/Advice",
    "score": 335,
    "comment_count": 447,
    "created_at": "2025-08-30T16:51:01+00:00",
    "top_comments": [
      {
        "id": "nbiq0n7",
        "score": 325,
        "body": "Im convinced im the only vet that wasn't SOF at this point"
      },
      {
        "id": "nbiu4h4",
        "score": 132,
        "body": "I\u2019m convinced my uncle was the only generator mechanic in Vietnam."
      },
      {
        "id": "nbiq8hr",
        "score": 122,
        "body": "Don't think I've ever seen one of those in real life, but I do get the \"I almost served\" as if they need to explain themselves.\n\nI literally do not care why you didn't sign up. Leave me alone."
      },
      {
        "id": "nbircsl",
        "score": 75,
        "body": "Oh the amount of snipers I've met outside the military quadruple the amount i met in the military."
      },
      {
        "id": "nbiq1vd",
        "score": 73,
        "body": "Just once I want to run into a stolen valor loser who claims to be an admin clerk for three years and got out."
      },
      {
        "id": "nbirxwd",
        "score": 60,
        "body": "I was at Walmart looking at video games once. This short fat kid employee, probably 21 with coke bottle glasses was talking to me about games. Dude was literally like 5\u20195 250\n\nI was looking at a sniper game. He proceeded to tell me how realistic it was because he was in the army and becoming a sniper. While also in boot camp. When he got sent home for some bullshit reason. (Probably did TOO MANY pushups or something)\n\nI told him I was a veteran, he kind of looking like he wanted to back track on his story. I was like \u201cso you were a sniper DURING boot camp? He looked nervous by my questioning. \n\nThen I stopped myself. This dude probably had nothing going for him in life. I felt bad for him so I just left him alone. Normally I\u2019d call people out on their bullshit. (Like my cousins friend who claimed to be the \u201cranger rick\u201d guy from Black Hawk Down\u2026. That\u2019s a whole other story). But I just let this dude be. \n\nSometimes a made up bullshit story makes them feel like they are something. Gotta know when to just let it go"
      },
      {
        "id": "nbiwesf",
        "score": 58,
        "body": "I'm sure he did great work while everyone else was a special forces sniper (there's no records of their existence, of course) or pilot."
      },
      {
        "id": "nbisba0",
        "score": 36,
        "body": "\u201cNot to brag but I saw some shit I don\u2019t like to talk about during my 2 year stint in DFAC\u201d"
      },
      {
        "id": "nbixuwa",
        "score": 31,
        "body": "Poor guy must have been busy as fuck though."
      },
      {
        "id": "nbiov7y",
        "score": 30,
        "body": "Never.\u00a0 Who are these people?"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1mcrg2z",
    "title": "VFW Post visit gone wrong",
    "body": "I just had the most unpleasant experience at a VFW post in my entire life. I\u2019m out of town for work and decided to pop into a local VFW in Conroe. I walked in, go to sign in and shit was weird. The young bartender came up to me and said \u201cwho are you signing in under\u201d. I asked if this was not where she wanted me to sign in? She said well are you a member? I said no. Isn\u2019t anyone welcome? She said no, this is a place for vets who\u2019ve seen combat, are you a vet? I said of course but are you not open to anyone? She said no. I said then idk if I want to be here. Never in my life have I been in a VFW that isn\u2019t welcoming to everyone. I qualify, but I\u2019m not becoming a member at your post, I\u2019m not local, and this is the worst first impression I\u2019ve ever had at a post. I\u2019ll see myself out. She said I\u2019m sorry, I\u2019m new. WTF does that have to do with anything? A VFW is the only damn place I\u2019ve ever felt completely welcomed and free from any judgement. This shit rubbed me so wrong. \n\nEvery VFW I\u2019ve ever been in has welcomed anyone and everyone with open arms. Sure, they\u2019re there for us, but I\u2019d never turn anyone away. Talk about making me feel completely unfuckingwelcomed and that I have to \u201cprove\u201d to anyone that this is where i belong. \n\nMaybe I\u2019m wrong here, maybe I\u2019ve only ever had good experiences, idk. Anyways, the Walk-On\u2019s up the road has a great beer selection. ",
    "flair": "Discussion",
    "score": 329,
    "comment_count": 375,
    "created_at": "2025-07-29T23:48:23+00:00",
    "top_comments": [
      {
        "id": "n5w0myv",
        "score": 352,
        "body": "I\u2019ve never been to a welcoming VFW or AL so idk what that\u2019s like."
      },
      {
        "id": "n5wwj5w",
        "score": 164,
        "body": "I'm a woman. I walk into a VFW and everyone turns to stare because I must obviously be lost."
      },
      {
        "id": "n5wuc1g",
        "score": 133,
        "body": "This has been my experience at every VFW. The American Legion is barely better. Pretty sure no one under 60 is welcome."
      },
      {
        "id": "n5x3wh0",
        "score": 130,
        "body": "Last Christmas season one of the guys in my platoon from Afghanistan killed himself.  All the guys flew in to Denver so we could drive to the funeral in Kansas - I\u2019m local and coordinate things for a living so I coordinated all the guys coming in.  I\u2019m a young GWOT vet, called the Lafayette, CO VFW and explained what was going on - and that none of us are members but we needed a place to drink and get together.  The VFW rolled out the red carpet for us and bought us beers at their bar all night and we went to the funeral blindly hungover.  \n\nI\u2019ve been to bad VFWs, it\u2019s hit or miss.  I\u2019m still not a member but I\u2019m deeply thankful for the guys at the VFW who squared us away last year."
      },
      {
        "id": "n5w4tsk",
        "score": 125,
        "body": "My first time visiting a VFW I was asked if I was \u201csomeone\u2019s kid\u201d.  I was 26 and had just gotten out of the Navy.  I never felt welcome there and wasn\u2019t going to put up with Vietnam War gatekeepers.  \n\nOddly the one near my hometown is open to everyone and lots of people I graduated with party there.  None of them served."
      },
      {
        "id": "n5w1ltj",
        "score": 62,
        "body": "I know in Pennsylvania, those types of liquor licenses are restricted to serving to bona fide members only. Even guests can\u2019t order drinks, the member has to. Doesn\u2019t explain the rudeness of the bartender but people pay to be a member of a VFW or AL. So no, it\u2019s not open to everyone."
      },
      {
        "id": "n5x5ayd",
        "score": 56,
        "body": "Conversely, I am too, and I just got elected into an officer position next to another woman. Every post is different."
      },
      {
        "id": "n5w45mq",
        "score": 55,
        "body": "Ok I know what happened.\n\nIn some states VFWs get \"club\" licenses for alcohol. Which means ONLY members can buy. So you need to have a member \"buy\" the alcohol or they could be fined or lose their license."
      },
      {
        "id": "n5wixwv",
        "score": 46,
        "body": "Yeah, this is generally the vibe I've gotten. Most of the time its down right hostile."
      },
      {
        "id": "n5w88fc",
        "score": 38,
        "body": "I am saying this in another post hoping OP reads it but this is 100% true for the VFW in Conroe.  They can't serve alcohol to non-members."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1o5kqqg",
    "title": "Vietnam Vet LRP patches.",
    "body": "Hello My Father in Law passed. I\u2019m heartbroken. No one talked/s about him. I know next to nothing. I did however find a batch of photos and patches in his belongings. Can anyone help identify these men or patches? ",
    "flair": "Question/Advice",
    "score": 321,
    "comment_count": 45,
    "created_at": "2025-10-13T14:09:52+00:00",
    "top_comments": [
      {
        "id": "nja9vm3",
        "score": 52,
        "body": "Vietnam Vet here.\n\n  \nThe airborne wings with LRRP designator is unofficial as is the Airborne Ranger Co pin, 173rd Airborne Brigade patch, Ribbons - Bronze Star, Army Commendation, National Defense Service Medal, Vietnam Campaign Medal, Vietnam Service Medal (Republic of Vietnam Award).\n\nDamaged 3/4 Ton vehicle with 101st Airborne, Company F, 58th Infantry (Long Range Patrol).\n\nPhotos are pre-1969 as Company F, 58th Infantry LRRP became Company L, 75th Ranger Regiment when the 75th Ranger Regiment was reconstituted to take over all LRRP companies.\n\nGary Linderer is probably the best source of information about the 101st Airborne LRRP's"
      },
      {
        "id": "njabg5e",
        "score": 19,
        "body": "Was part of 173rd LRRP from 2011-2014 before they were done away with. Here\u2019s a little write up one of our LT\u2019s did on the history.\n\nhttps://commanderschallenge.wordpress.com/2013/10/23/reconnaissance-platoon-hhc-1st-bn503rd-infantry-regiment-2012-deployment-present-challenge-coin-2/"
      },
      {
        "id": "njb26p1",
        "score": 12,
        "body": "That is a great history rundown!"
      },
      {
        "id": "nja0m9j",
        "score": 11,
        "body": "173rd Airborne Patch in the second to last photo! I\u2019m guessing he was a part of some company unit or something. \n\nYou\u2019ve got some cool LRRP stuff. Those airborne ranger pins are the OGs! I see a ranger regiment crest in there too. Bet there\u2019s an old Vietnam guy in here who could help you out a little more. I\u2019m just an old 173rd GWOT guy. \n\nSorry for your loss OP. Fly high sky soldier!"
      },
      {
        "id": "njalmxg",
        "score": 5,
        "body": "[removed]"
      },
      {
        "id": "njajh6e",
        "score": 4,
        "body": "sleep abundant square middle bear axiomatic grandiose abounding governor tap\n\n *This post was mass deleted and anonymized with [Redact](https://redact.dev/home)*"
      },
      {
        "id": "njatb3v",
        "score": 4,
        "body": "That\u2019s cool. You were getting to 173rd when I was leaving"
      },
      {
        "id": "nja2ccf",
        "score": 3,
        "body": "Long Range Reconnaissance Patrol"
      },
      {
        "id": "njbowt1",
        "score": 3,
        "body": "A true badass. RLTW"
      },
      {
        "id": "njboiap",
        "score": 2,
        "body": "He was one brave man, sorry for your family's loss"
      }
    ]
  }
]
```
