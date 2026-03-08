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
    "subreddit": "VetTech",
    "id": "1rkkyt5",
    "title": "Burnt out and feeling taken advantage of.",
    "body": "I am a VA at a GP that does exotics, I was originally part time going to college for something else and I left college to pursue this full time with the plan to eventually go back to college and get my associates in veterinary technology once I was sure. I have been working full time hours (was working full time hours before I was actually full time) for about 7 months sometimes doing 11 hour shifts (longer if I have to stay late) with my 40-60 minute commute and we only get a 30 minute unpaid break, been working there for a year and a half. So all in all it\u2019s a lot for me. I enjoy what I do and I like the people, I feel like I am not treated well by certain people sometimes but I get along with everyone generally regardless. For additional context if I decided to reduce hours or quit I was going to make the decision to go back to what I was doing previously for work (work from home) + focus on degree. Otherwise I was going to have to find another clinic after I moved in a year or so. Purposely being vague because I worry someone will see this.\n\nI know being a VA I can\u2019t expect to be paid the same as someone with a lots of experience/a license of course, I feel like I\u2019m taken advantage of past what is reasonable. I am still learning and there is many things I need to work on of course, but generally I am able to do the same duties as everyone else + front desk. It is not uncommon for me to be juggling all duties throughout the day even when on appointments or in surgery. The main issue I have is since I began I\u2019ve only gotten a 50cent raise and I only make 16.50$ an hour, however it\u2019s not uncommon for me to be working more hours than most other staff, staying late, coming in early, picking up shifts in an emergency, and I work the weekends. Whenever I take vacation it seems like everything falls apart because people are so used to me managing the \u201cboring\u201d tasks all day and at one point every single shift I was cleaning the entire hospital by myself, it had gotten to a point we had a meeting about it because I finally put my foot down since I physically could not finish closing by myself. People would be chatting and on their phones while I was finishing and even telling me I need to \u201cclean faster\u201d so they could go home. Sometimes they would walk out while I was still closing. After that I purposely started to leave things for other people to clean and manage, but even now when I\u2019m juggling my own appointments I will get asked to clean and do things for people who have plenty of time to do it themselves.\n\nNow I have been asked to take over minor administrative duties and told I will not be disturbed during this time, if someone asks me to do something I need to refuse. Which to me sounds great, I think my main issue is that if I am clearly being told I work hard, am valuable, etc, then why is my pay not reflecting that. In my state standard starting pay for VA is around 18$ an hour right now. In fact, we just filled another position where starting pay for no experience was 18$ an hour, and I joked I should just quit and do that instead since I\u2019m already managing that too! But honestly I thought about it because it would be less work for me! I am our lowest paid employee and I am starting to get burned out because I rarely ever have 2 days consecutively off and I feel like I\u2019m losing my mind.\n\nI was told to wait to hear about a raise by this month a few months ago, and I\u2019m trying to be patient to let them be the ones to pull me aside but I\u2019m thinking I need to just ask now because I\u2019m almost worried they will have simply forgot discussing another raise or not want to give it to me. Originally I was told corporate was the reason I couldn\u2019t get paid more, but that they\u2019d approve for higher pay this month, but I\u2019m not taking that excuse again and considering going back to part time or leaving. I had a horrible day where I was being blamed for things that either I didn\u2019t do, or I was pushed to do when I clearly said it was past what I was comfortable with, had someone double check what I did and yet it was still screwed up. I had multiple people coming to me asking for help or to do things and I blew up and told them all raising my voice \u201cI can\u2019t help you\u201d and everyone got all awkward and walked away. I am constantly being pushed past what I am ok with and past my limits, and I\u2019m tired of it and it\u2019s finally boiling over. I have never received proper training for most things and learned things as I went, which causes a lot of issues because I am interrupting other people to get help which often puts more on them and causes them to get frustrated with me. All of this has just been building up and every time I\u2019ve expressed these things to my boss nothing changes. I finally talked to my therapist about it and I am starting to build up the courage to do something more about it.\n\nI don\u2019t even know what posting this is meant to do, I guess to rant, I am just so worn down and frustrated, and yet I am too afraid to stand up for myself, and finally standing up for myself the other day made me feel good even if I was mean! I often feel like I shouldn\u2019t complain because I am the least experienced and have a lot I need to work on, but at the end of the day I\u2019m in my 20\u2019s and I can\u2019t keep being treated like I\u2019m a teenager. I worked kennels as a teen getting paid horribly and often it feels like I am treated the same now despite the how much of myself I put into this. My partner and friends think that even if I got what I wanted for a raise at minimum that I should still either go part time or consider leaving. This is sucking away my time and energy from maintaining relationships and taking care of my own pets and people are worried about me. I am also physically disabled and I still come in every day, I\u2019ve only been out sick twice! We have people calling out almost every day, and I\u2019m sometimes there not feeling well still getting done what I need to and then some. I am not saying that to say I am better than anyone because I don\u2019t think it\u2019s an achievement for me to do this to myself so often but I feel like it should matter that I show up on time even when it\u2019s hard, I feel like it should count for something towards being paid more fair, and yet it really doesn\u2019t seem to matter to anyone but me which has made me realize how stupid I have been. Being told I work hard and do well isn\u2019t enough, I want it to be reflected in my pay but I feel afraid to ask and being turned down and having to make the decision to either cut my hours in half or leave because I do genuinely love this through everything! Which I wasn\u2019t expecting! But I don\u2019t think it\u2019s worth destroying myself over and know I need to stand up for myself even if that means walking away for now.",
    "flair": "Burn Out Warning",
    "score": 9,
    "comment_count": 2,
    "created_at": "2026-03-04T13:07:46+00:00",
    "top_comments": [
      {
        "id": "o8l9vgn",
        "score": 4,
        "body": "\n\nDon't wait for them to offer you a raise. Get another job lined up just in case then go in and tell them all the reasons you need a raise of at least 18/hr but id ask for 19 based on all you said here. If they don't give you one, quit.\n\nWaiting for the employer is why you're underpaid."
      },
      {
        "id": "o8l6fn6",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rkdspm",
    "title": "Former co workers writing 5 star reviews for the hospital they work at",
    "body": "I used to work at a very popular veterinary ER, and while reading the reviews recently I counted, so far, TEN current employees, one being the hospital manager, who wrote 5 star reviews for their own hospital. \n\nSo damn tacky.\n\nHas anyone else seen people do this? ",
    "flair": "Vent",
    "score": 15,
    "comment_count": 14,
    "created_at": "2026-03-04T06:11:18+00:00",
    "top_comments": [
      {
        "id": "o8k1yeu",
        "score": 17,
        "body": "You can report reviews. One of the options on Google is something to the effect of \u201cthis review was made by a person with a personal connection\u201d. "
      },
      {
        "id": "o8ju384",
        "score": 9,
        "body": "Yeah, that happens a lot tbh. Not just vet clinics. Restaurants, gyms, even tech companies do it.\n\nIt\u2019s pretty obvious when staff write the reviews though. Same tone, same timing, all 5 stars. Most people reading reviews can spot it.\n\nHonestly the better move is just ignore it and focus on the real feedback from clients. Fake reviews don\u2019t hold up long once enough genuine ones come in."
      },
      {
        "id": "o8jvkg5",
        "score": 3,
        "body": "Yep my former GP clinic did this \u2026 our boss would give perks if you wrote a review, or got your friends in on it. It\u2019s not illegal, definitely a bit shady, and as someone else said, everyone does it. Not justifying it at all, but it is what it is."
      },
      {
        "id": "o8juzhl",
        "score": 3,
        "body": "I remember when I was employed there,management was trying to get everyone to write Google reviews so our hospital could surpass the other animal ER\u2019s in the area on Google searches."
      },
      {
        "id": "o8kada1",
        "score": 3,
        "body": "It actually is illegal. It is against FTC regulations to \u201cbuy reviews\u201d or offer direct discounts or rewards in exchange for five star reviews. I have a rule for my staff that they are only allowed to write a review if they brought their pet in for a visit and they wrote it about an ACTUAL experience. They were technically a client during that visit and there is never any pressure either way to post a review."
      },
      {
        "id": "o8jxqm5",
        "score": 2,
        "body": "It\u2019s not new but a waste of time. Modernly an intelligent person knows voluntary reviews are not accurate. That means for any bad or good.\n\nUsually you get the unhappy clients writing way inaccurate reviews, but you can also get employees tampering with them.\n\nI wouldn\u2019t get involved. I go off my experience personally and better resources then the internet land dump of opinions nobody asked for you know lol"
      },
      {
        "id": "o8jw6yj",
        "score": 2,
        "body": "They offered some folks a bonus of $300 or $400, I don\u2019t remember, if they surpassed a certain amount of reviews to beat another local hospital in the area.\n\nIt\u2019s not illegal like you said, just shady and tasteless."
      },
      {
        "id": "o8jtxr8",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o8k9671",
        "score": 1,
        "body": "Yeah same thing happens with restaurants in my personal experience, in both industries managers/owners will bribe their staff in some way to falsify positive reviews. It's simply an additional symptom of the massively diseased society we participate in."
      },
      {
        "id": "o8kpqn6",
        "score": 1,
        "body": "\ud83d\udd35?\n\nIf so, it sounds like people are attempting to keep their jobs.\n\nWe used to get notices at the hospital about customer satisfaction surveys etc. Sounds like they want to drive more people to their location and build employee morale."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rkaqub",
    "title": "Does anyone use smart watches with second hands to calculate heart rates?",
    "body": "For y'all that use smart watches at work, do you use watch faces that have second hands for calculating heart rates or do you do it some other way? I am trying to gauge whether or not I should get a smart watch or a regular watch for this. I am going on externship soon and was told a watch would probably be needed. But also, do most smart watches have analog sticks with second hands? I don't feel as though this would work any other way. Please let me know. ",
    "flair": "Work Advice",
    "score": 9,
    "comment_count": 27,
    "created_at": "2026-03-04T03:32:57+00:00",
    "top_comments": [
      {
        "id": "o8jt5sb",
        "score": 14,
        "body": "I have a Samsung watch and you can set the screen to stay on for exactly 5, 15, or 30 seconds after you tap it. I've got mine set for 15 and I don't even have to look at it, I can just watch for the light to go out in the corner of my eye."
      },
      {
        "id": "o8ja1fw",
        "score": 6,
        "body": "If this is the only thing you\u2019ll use it for a smart watch isn\u2019t worth it in my opinion. I have one and had it prior to this job. It works well but sometimes the screen will dim when I\u2019m counting which is annoying. I do miss a classic standard watch at times but use the Apple Watch plenty in my personal life that it makes sense to keep. "
      },
      {
        "id": "o8j9kze",
        "score": 4,
        "body": "I use an old Apple Watch with a case so I don\u2019t have to worry about breaking it"
      },
      {
        "id": "o8jh0ch",
        "score": 4,
        "body": "My smart watch (a Fitbit) had the option to download different clock faces. I have an analog clock face just because I like how it looks. I have the button on the side programmed to open a 10 second timer when I long-press it, with a vibration not a beep to signal the end. I also use the calculator app constantly."
      },
      {
        "id": "o8jacdi",
        "score": 3,
        "body": "You can download different watch faces for some smart watches but I am old fashioned and I usually use an analog nurses watch pinned to my scrub top because I hate when any screen (phone or smart watch) decides to sleep before I am done counting and I actually prefer my devices going to sleep quickly on a normal basis outside practice so constantly changing things is a headache I don't feel I have to endure when an easier and super cheap solution exists.\n\n\n\n\nThat said, most people I work with lately use their phones.\u00a0"
      },
      {
        "id": "o8nwcyc",
        "score": 3,
        "body": "I have an apple watch, and I have the modular face where it tells you the time, but I have a little widget on the bottom that counts the seconds, and I use that. I hate to admit I can't read a regular clock quickly so its super helpful having the small seconds in the corner counting for me."
      },
      {
        "id": "o8jz1qn",
        "score": 3,
        "body": "Oh, I didn't know I could have my phone on me. I feel like it would take more time to take out my phone and go to the stop watch app tho lol."
      },
      {
        "id": "o8ohkia",
        "score": 3,
        "body": "I have an Apple Watch and you can customize the app icons on the watch face. I have one that\u2019s a 15 second countdown timer and it vibrates when it\u2019s done. Works great for me! "
      },
      {
        "id": "o8jk9je",
        "score": 2,
        "body": "I do! I have an Apple Watch and I use the second hand all the time. Also utilize the calculator and timer every day. "
      },
      {
        "id": "o8jt08j",
        "score": 2,
        "body": "My android smartwatch has an app specifically for nurses that is very useful. It has a second hand, keeps the watch face from going dim for 3 minutes, and it vibrates every 15 seconds. I think it's as good as a regular watch, and better if you're in a dim setting, like the back of a cage."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rk92da",
    "title": "Tips for taking a lead at a wreck of a hospital?",
    "body": "I don\u2019t want to give too much info on the unlikely event someone recognizes me, BUT \u2014\n\nI\u2019m considering taking a lead role at a clinic that\u2019s a hot mess. They\u2019re offering about $10/hr more than average in my area and honestly the job market is sad.\n\nBut this place is\u2026 idk. The manager admitted the culture is bad in the preliminary interview, then at the working one, no one had much positive to say. I asked what they liked about it, and it was sort of like \u201coh, well it\u2019s not as bad as the last place I worked.\u201d\n\nAnd when I asked what they didn\u2019t like or what changes they wanted to see, the list was long. Inefficient workflow, taking too many drop-offs, no one understanding wtf is going on, etc.\n\nSo I\u2019m essentially being hired as lead to fix it. And I have some ideas. I want to see the actual workflow myself, talk to everyone, etc. but idk man. Just wondering if yall have any advice.",
    "flair": "Work Advice",
    "score": 15,
    "comment_count": 13,
    "created_at": "2026-03-04T02:15:58+00:00",
    "top_comments": [
      {
        "id": "o8ivd0m",
        "score": 40,
        "body": "Is it a wreck because there hasn\u2019t been leadership, or is it a wreck because someone higher up throws tantrums and won\u2019t let leads do their jobs?"
      },
      {
        "id": "o8iw4vo",
        "score": 16,
        "body": "It sounds like the lead previously sucked? They said the lead hadn\u2019t been training as expected / not training at all and protocols were mistaught or misunderstood. \n\nI wasn\u2019t able to get a full picture, but that\u2019s how it was explained to me by the manager.\n\nThe owner & manager seemed open to change and had plenty to complain about. I\u2019m not confident they\u2019ll actually allow it."
      },
      {
        "id": "o8iysqe",
        "score": 14,
        "body": "So I took a job as a lead at a hospital that had been under new ownership for a few years. It was a nice hospital that had some recent updates, the staff was small and all had been there less than 2 years. Tge owner had essentially had 200% turnover. A lot was said about the previous lead. I came in bright eyed and bushy tailed ready to change the world (including a six dollar pay raise) and was ready to go. Hint: It was not the previous lead that was the problem. I stuck it out for a year and 3 months, and then took a huge paycut to work as a non-lead tech. It was a good learning experience and I trauma bonded with a few people!"
      },
      {
        "id": "o8iwemk",
        "score": 10,
        "body": "I think you\u2019re right to be skeptical.\n\nIf the last lead was the problem, the staff would have told you.\n"
      },
      {
        "id": "o8j11ge",
        "score": 9,
        "body": "I legit had to check your post history to make sure you weren't in my state \ud83d\ude06\n\n\nPS if you are on Facebook, check to see if there's a group for vet support staff in your area. We have one that lets people post and reply anonymously and I see these questions some times."
      },
      {
        "id": "o8j2c7u",
        "score": 6,
        "body": "Don\u2019t take the job. \nLead tech usually don\u2019t have enough power to turn things around. To do that you will need a support of higher leadership. And based on what you are saying, they don\u2019t really care since, I assume, you were interviewing with the manager at least. \nAt least take a full day working interview to meet the team. It will help you to make a decision. \n"
      },
      {
        "id": "o8ixbvv",
        "score": 6,
        "body": "I wish I would\u2019ve had more one on one time with some of them to get a fuller picture \ud83d\ude2d I feel like I\u2019m setting myself up for failure, but I also need money lmao."
      },
      {
        "id": "o8jp3d7",
        "score": 5,
        "body": "Take the money. Worst case you use it to negotiate salary elsewhere."
      },
      {
        "id": "o8ley0g",
        "score": 2,
        "body": "How long was the previous lead there?\n\nI know these things vary by place, but it comes off like a red flag that management is coming down on the previous lead, when they're the ones responsible for hiring them.\n\nSome places hire people, but then get upset when the person starts demanding changes, holding management accountable."
      },
      {
        "id": "o8nv3lo",
        "score": 2,
        "body": "Ask what the expectations are in the role. Give them time periods for this.\n-in 6 months what are the hospital goals?\n-in 1 year.....?\n\nAsk what deficits the last person in that role had.\n\nAsk what does support look like for you? Are there check-ins? How often? Who is your closest partner in this role? A DVM? Or another tech?\n\nAnd then ask what does advancement look in this role?\n\nBest of luck!"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rk5es5",
    "title": "pet groomer curious about tech's version of these- what are some things owners say/do that makes you realize how incredibly stupid some of them are?",
    "body": "i'm talking about things that are just like, common sense but owners are clueless. not obvious ones like if you brush your dog they won't get shaved but silly unique ones. \n\nI got a few that are groomer centric (except the last one(\n\nowners wanting 1 guard comb length longer because \"it's winter and he'll be cold\" when it's literally a few millimeters different \n\nowners that are told that if they wipe their dogs eyes everyday the eye boogers won't crust. I legit had a client recently who I finally asked if she did that because it builds up, and she said no not every day. she does now and boom zero built up crusties \n\nthis isn't super grooming specific but animal specific and I've seen it SO OFTEN. When there's two dogs of the same family and one is getting enormous while the other is the same size or skinnier, and say yeah he steals his meals. like...feed them in seperate rooms?? or watch them eat?? it's not rocket science! ",
    "flair": "Discussion",
    "score": 95,
    "comment_count": 77,
    "created_at": "2026-03-03T23:36:50+00:00",
    "top_comments": [
      {
        "id": "o8i6omw",
        "score": 243,
        "body": "\"He doesn't seem painful, he's just limping.\"\n\nAh, so he limps for fun? Not because something hurts? Got it. "
      },
      {
        "id": "o8i6r11",
        "score": 166,
        "body": "\u201cMy intact male dog couldn\u2019t have gotten my intact female dog pregnant- they\u2019re littermates\u201d"
      },
      {
        "id": "o8i4nz9",
        "score": 94,
        "body": "\"He doesn't need vaccines, he's not an outdoor dog\" ....okay how did yall get here? Where does he use the bathroom?\n\n\"It just happened overnight!\" ...your dog is skin and bones and severely dehydrated? That doesn't happen in one night"
      },
      {
        "id": "o8iiebe",
        "score": 84,
        "body": "This one killsssss me. \"He doesn't whine or anything\" yeah but he doesn't bear weight on the leg, licks it constantly, and tried to snap at the doctor during the exam when looking at it.... What more do you want?!"
      },
      {
        "id": "o8iquiy",
        "score": 74,
        "body": "When they listen to the breeder instead of the doctor. \"Oh... the breeder said that shih tzus shouldn't get rabies and lepto vaccines because it's toxic to them!\". Or \"His breeder recommended a raw, grain free diet so that's what we'll be doing\". So frustrating. "
      },
      {
        "id": "o8iebii",
        "score": 69,
        "body": "\"he doesn't need a rabies vaccine. He doesn't eat rabbits...\"\n\nWh....who told you that?!"
      },
      {
        "id": "o8i6guu",
        "score": 67,
        "body": "i\u2019ve deadass had someone tell me they didn\u2019t need heartworm/flea prevention because they live in a gated community"
      },
      {
        "id": "o8irf9e",
        "score": 60,
        "body": "\u201cSir, we should intubate your dog on an average Tuesday. She\u2019ll love it.\u201d"
      },
      {
        "id": "o8ihb8s",
        "score": 56,
        "body": "My most recent \u201cuhhh\u2026.\u201d one was a dog who was really not doing well, so we got a CPR code when it arrived. Owner said yes, CPR but DO NOT INTUBATE. It was a bulldog, of course.\n\nSir, trust me, she will breathe better through that tube than she ever has in her life."
      },
      {
        "id": "o8igaoq",
        "score": 48,
        "body": "We recently had a rescue partner send two dogs to the same home for foster to adopt- intact male and intact female before their spay/neuter. Their justification? They\u2019re littermates\u2026. I couldn\u2019t believe it"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rk3kpf",
    "title": "What's the grossest thing that's ever happened to you?",
    "body": "Or something you've witnessed happen to someone else!\n\nOne of my coworkers was talking while expressing some anal glands and it shot right into her mouth \u2639\ufe0f I felt so bad for her because she was already having a bad day.",
    "flair": "Discussion",
    "score": 69,
    "comment_count": 90,
    "created_at": "2026-03-03T22:23:52+00:00",
    "top_comments": [
      {
        "id": "o8htwx9",
        "score": 84,
        "body": "I was restraining a large dog during an acupuncture treatment (not a samoyed but very similar) and the dog was restless/trying to get up. Eventually she stood at the end of the treatment and immediately mucusy, liquid diarrhea flew out of her. This ended up all over the back of her legs and tail. Then..... she shook. \n\n  \nI felt a million micro droplets of diarrhea fly all over me (mouth included.) Any area not covered by scrubs was hit with a million microscopic poop drops. The worst part? NONE OF THEM WERE VISIBLE. I REEKED of shit but you couldn't actually SEE any. I had to shower. "
      },
      {
        "id": "o8hqz20",
        "score": 62,
        "body": "I had a large cat abscess explode all over the side of my face and down my chest. I was trying to get him out of the kennel and had him cradled with his head on my shoulder. I thought he had regurgitated on me at first, but it was just his large head abscess rupturing. "
      },
      {
        "id": "o8hrur0",
        "score": 52,
        "body": "For me it is 100% the parasites that we can pick up from the pets. Scabies, fleas, ringworm, flat flies...\n\nThe grossest is when you get the pet coming in a carrier that is gross and definitely contains bugs too."
      },
      {
        "id": "o8huh2d",
        "score": 49,
        "body": "Eyeball ruptured down my arm "
      },
      {
        "id": "o8hsyt3",
        "score": 38,
        "body": "Parvo poop soaked from my hip, down my thigh, into my shoe. \n\nI also had a crit tube stuck into my fingertip, about 1/4\" or so. "
      },
      {
        "id": "o8idf0i",
        "score": 33,
        "body": "We had a cat a while ago who had a (chicken) wishbone stuck in their throat for over a month. they were still able to eat/drink/breathe around it, but they started throwing up regularly so the owners brought them in. the bone had been there so long that it started to abscess through to the outside of the throat. we managed to safely section the bone and pull it out under anesthesia, and as soon as it exited the mouth the entire room filled with the WORST smell of rotting meat, bone, and hairball. I have an incredibly weak sense of smell and a pretty ironclad stomach, but I almost instantly threw up in my mouth. That smell still haunts me."
      },
      {
        "id": "o8ht99k",
        "score": 30,
        "body": "Similar situation to you, in tech school the professor brought in a few barn kittens for a friend of hers for us to vaccinate and such, and as she held one up and turned him around he let his a/gs loose directly into her mouth while she was talking. She set the kitten down and immediately went into the bathroom. She came out 10 mins later white as a sheet and said \u201cwhere\u2019s my coffee\u201d\u2026..I\u2019ve never laughed so hard \ud83e\udee0"
      },
      {
        "id": "o8hx95l",
        "score": 28,
        "body": "This was back when I was the cleaning lady at my old clinic. A big boxer came in that day for treatment of a large abscess on his buttcheek. They put him in a kennel and just.... didn't look at him for awhile? He decided to chew up and eat the abscess, it of course exploded everywhere (it looked like spaghettios), ATE it and vomited all over. THE SMELL. I showed up for work that evening and the techs were just chatting about it but I was mumble/grumble because it stank AND had dried. It took me over an hour to scrub it all up."
      },
      {
        "id": "o8ic6wl",
        "score": 28,
        "body": "The scream I scrumt at the crit tube"
      },
      {
        "id": "o8iq5hf",
        "score": 26,
        "body": "Ahhhhhh! Gross carriers and gross crusty-ass blankets in them. With some kind of feeble excuse that it isn't like that all the time, when it's clearly been that way for gross years."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rjzcwp",
    "title": "Bad shoulder radiographs",
    "body": "Hey guys I am doing a project for school does anyone have photos of bad shoulder radiographs with bad technique or poor positioning? If so please share! If you don\u2019t mind me using them only my teacher and I will see ",
    "flair": "School",
    "score": 5,
    "comment_count": 1,
    "created_at": "2026-03-03T19:46:40+00:00",
    "top_comments": [
      {
        "id": "o8gsxh1",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rjytmw",
    "title": "This is insane and exactly why cats are less likely to receive appropriate veterinary care",
    "body": "",
    "flair": "Discussion",
    "score": 164,
    "comment_count": 54,
    "created_at": "2026-03-03T19:26:46+00:00",
    "top_comments": [
      {
        "id": "o8gqajj",
        "score": 184,
        "body": "Ain\u2019t nothing wrong with disliking cats or dogs but to say cats are inherently unfriendly is a huge incorrect assumption"
      },
      {
        "id": "o8gqp28",
        "score": 120,
        "body": "man, cats domesticated themselves when they realized what a good deal it was living with humans. i don\u2019t think any other animal did that. "
      },
      {
        "id": "o8h1ucc",
        "score": 46,
        "body": "My 2 cats try to climb inside my skin any time I'm sitting or laying down. They are more in-your-face affectionate than any dog I've met.  I've known plenty of social, outgoing, friendly cats at my clinic.\n \nI think cat hate is sometimes rooted in misogyny. Cats are traditionally seen as feminine. Dogs as masculine."
      },
      {
        "id": "o8hky30",
        "score": 35,
        "body": "This sucks! I love Doechii. Very disappointing to see this from her. Just say you don't like cats, you don't have to invent all this BS about them being unfriendly. Cats domesticated themselves - if they didn't want to be with us, they wouldn't be."
      },
      {
        "id": "o8hkq8w",
        "score": 34,
        "body": "I think their arguement that cat hate being rooted in misogyny is fair and well-documented-\n\n[https://www.researchgate.net/publication/331268759\\_The\\_Crazy\\_Cat\\_Lady\\_Gender\\_Animals\\_and\\_Madness](https://www.researchgate.net/publication/331268759_The_Crazy_Cat_Lady_Gender_Animals_and_Madness)\n\n[https://www.researchgate.net/publication/342051634\\_Not\\_the\\_Cat's\\_Meow\\_The\\_Impact\\_of\\_Posing\\_with\\_Cats\\_on\\_Female\\_Perceptions\\_of\\_Male\\_Dateability](https://www.researchgate.net/publication/342051634_Not_the_Cat's_Meow_The_Impact_of_Posing_with_Cats_on_Female_Perceptions_of_Male_Dateability)\n\n[https://www.npr.org/2024/07/29/nx-s1-5055616/jd-vance-childless-cat-lady-history](https://www.npr.org/2024/07/29/nx-s1-5055616/jd-vance-childless-cat-lady-history)\n\n[https://www.bbc.com/culture/article/20220225-the-batman-the-ancient-roots-of-catwoman](https://www.bbc.com/culture/article/20220225-the-batman-the-ancient-roots-of-catwoman)\n\n[https://web.archive.org/web/20240727150906/https://www.bostonglobe.com/ideas/2017/05/20/the-crazy-history-cat-lady/5DJaZf5QW0KPv8KTYBBGPO/story.html](https://web.archive.org/web/20240727150906/https://www.bostonglobe.com/ideas/2017/05/20/the-crazy-history-cat-lady/5DJaZf5QW0KPv8KTYBBGPO/story.html)\n\n[https://www.psychologytoday.com/us/blog/invisible-bruises/202502/who-exactly-is-a-cat-lady/amp](https://www.psychologytoday.com/us/blog/invisible-bruises/202502/who-exactly-is-a-cat-lady/amp)\n\n[https://thesocietypages.org/socimages/2013/12/04/the-feminization-of-the-cat-in-anti-suffrage-propaganda/](https://thesocietypages.org/socimages/2013/12/04/the-feminization-of-the-cat-in-anti-suffrage-propaganda/)\n\n[https://daily.jstor.org/a-purrrrfect-political-storm/](https://daily.jstor.org/a-purrrrfect-political-storm/)\n\nhttps://preview.redd.it/jblora1njwmg1.jpeg?width=1125&format=pjpg&auto=webp&s=aa3d700aff5fbc74cfc9b8b59622f70b5bee97d4"
      },
      {
        "id": "o8graa3",
        "score": 30,
        "body": "Cats are incredibly lovey and so what if some take effort to earn their trust? As a human, I get it."
      },
      {
        "id": "o8gtzsg",
        "score": 26,
        "body": "nooooo doechii wtf"
      },
      {
        "id": "o8h1s0l",
        "score": 18,
        "body": "Who is this person?\n\nIf I had to hazard a guess, someone who expects people to follow her around and never tell her when she\u2019s being an idiot or a jerk.\n\nCats generally don\u2019t like people who don\u2019t respect boundaries and treat them with respect.\n"
      },
      {
        "id": "o8h6cyw",
        "score": 17,
        "body": "I looked her up and it looks like she's a rapper. She doesn't work in vet med, she's just some rapper who's spreading misinformation to her followers/fans."
      },
      {
        "id": "o8i3whn",
        "score": 15,
        "body": "I typically see it as being rooted in control issues, tbh. Some people who don't like cats don't like that cats tend to be more independent and less easily controlled by force of will. "
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rjyjhz",
    "title": "Projectile vomit feces",
    "body": "Sure, I have been projectile vomited on many a time and I've also been projectile shatted on. Today was the first time where I had a patient (who partipates in coprophagia) projectile vomited their own semi-digested soft feces onto the entire front of my body. It's hard to gross me out so my immediate reaction was to say: \"Aww poor kid, you need some Cerenia\" ",
    "flair": "Gross \ud83e\udd22",
    "score": 35,
    "comment_count": 6,
    "created_at": "2026-03-03T19:16:25+00:00",
    "top_comments": [
      {
        "id": "o8hmypk",
        "score": 8,
        "body": "I bet your shower was GLORIOUS"
      },
      {
        "id": "o8ipvwn",
        "score": 7,
        "body": "You, my friend, are one of our strongest soldiers.\n\n We induced vomiting in my patient the other day. The owner wasn't aware he had eaten anything naughty but we saw an obstrutive pattern on rads. We realized he had eaten a diaper as I was digging through the contents of his vomit ughhh lol (with gloves of course but still!)"
      },
      {
        "id": "o8hpi5d",
        "score": 5,
        "body": "An extra special occasion!!!!!"
      },
      {
        "id": "o8jh4rd",
        "score": 5,
        "body": "Just remember folks: keep your mouth closed when at the front or behind of any animal! \n\nThat's the biggest thing we're being taught right now. XD"
      },
      {
        "id": "o8ioljc",
        "score": 3,
        "body": "I\u2019ve had the misfortune of watching a dog do this and it almost made me vomit. I would\u2019ve had to go home. "
      },
      {
        "id": "o8gmlrk",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rjxc7d",
    "title": "my new lady!!",
    "body": "this is my new gal, Hildy, coming home in a few weeks! she\u2019s about 35lbs and presumed to be an aussie mix - give me your best guesses! she\u2019s also got back dewies!",
    "flair": "Discussion",
    "score": 56,
    "comment_count": 5,
    "created_at": "2026-03-03T18:33:02+00:00",
    "top_comments": [
      {
        "id": "o8ibrgm",
        "score": 3,
        "body": "Back dewclaws are typically (in my experience) on heelers. She\u2019s super cute, obviously some kind of herding dog, which are my favs"
      },
      {
        "id": "o8hkm44",
        "score": 2,
        "body": "She is so friend shaped ,I love her!"
      },
      {
        "id": "o8k0fas",
        "score": 2,
        "body": "She has such a sweet face.. aww congrats"
      },
      {
        "id": "o8gdbrt",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o8ijacp",
        "score": 1,
        "body": "That would make sense!! She\u2019s coming from Texas and just a little thing. She\u2019s SO sweet and I can\u2019t wait for her to come home!"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rjx23f",
    "title": "Weird question...",
    "body": "Can you intubate a giraffe ? How the hell does that even work?!",
    "flair": "Discussion",
    "score": 11,
    "comment_count": 24,
    "created_at": "2026-03-03T18:23:15+00:00",
    "top_comments": [
      {
        "id": "o8gd5l8",
        "score": 9,
        "body": "Yes, you can. Google the pictures, it\u2019s really cool!"
      },
      {
        "id": "o8jeoio",
        "score": 9,
        "body": "Exotic tech here - I do it pretty much daily lol. "
      },
      {
        "id": "o8hhziy",
        "score": 6,
        "body": " My class at vet tech school got to tour the veterinary facilities at the Bronx Zoo, and at the time they could intubate an okapi but not a giraffe."
      },
      {
        "id": "o8h9c1l",
        "score": 5,
        "body": "Yes you can intubate just about anything. It's pretty similar to a really large cow"
      },
      {
        "id": "o8i3ay4",
        "score": 5,
        "body": "You can! You can even intubate an elephant (you have to *palpate* the trachea, it's awesome). \n\nI follow this really cool zoo vet on instagram (dr.jbminterdvm) for all kinds of cool zoo med stuff, highly recommend. "
      },
      {
        "id": "o8jpteu",
        "score": 5,
        "body": "I read that as imitate. Now I have visions of people is scrubs doing the chicken dance but hissing and honking "
      },
      {
        "id": "o8jcu45",
        "score": 4,
        "body": "Yep, it\u2019s not easy, but our exotics team has done it on the more critical rabbit surgeries. I think the last was a liver torsion. "
      },
      {
        "id": "o8jewf5",
        "score": 2,
        "body": "I recently saw a video of an alligator being intubated \ud83d\ude33"
      },
      {
        "id": "o8jmkq7",
        "score": 2,
        "body": "I helped a vet intubate a goose before!"
      },
      {
        "id": "o8lr2wa",
        "score": 2,
        "body": "The real question we should be asking is where would a giraffe wear a tie. At the top of its neck under the chin or at the bottom of the neck resting near the shoulders?"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rjtpao",
    "title": "When GP refers to specialty",
    "body": "I worked ER/specialty medicine for 20 years.  Moved to GP for several years, and recently, I moved back to specialty in a different capacity-not a tech position. \n\nI've encountered many clients that call my hospital looking for consults with various specialties.  All claim that there rDVM gave them a list of specialty hospitals with instructions to call and schedule an appointment. \n\nAre GPs not doing the referring now?  Leaving clients to figure it out on their own?  This was not my experience when I was in GP.  \n\nAnyone else experience this?",
    "flair": "Discussion",
    "score": 9,
    "comment_count": 21,
    "created_at": "2026-03-03T16:22:20+00:00",
    "top_comments": [
      {
        "id": "o8funw8",
        "score": 19,
        "body": "Thats how we do it at my clinic, send a list of referral places home and let the clients make the appointment. Where I live, there can be multiple places for the same specialty service so it gives clients the opportunity to choose where they want to go based on location as well as cost and how soon they can be seen.\n\nReferral forms and records are sent after the client makes the appointment. Either the client lets us know they\u2019ve scheduled or the specialty requests records. \n\nDoing it this way can suck with the timing sometimes, like when a client is able to get an appointment in days so we have to scramble to get the pertinent information and referral form sent out. But the flip side is if we were to get it all ready for every patient we recommend specialty to and 90% of our owners are not interested in pursuing specialty care for whatever reason. It kind of ends up being a waste of time on our end to prepare it all, even if it\u2019s just a tech filling out a referral form online. Our time could be better used elsewhere."
      },
      {
        "id": "o8g9fla",
        "score": 8,
        "body": "When I was in GP, I would give clients a list and tell them I would refer them to a place of their choice. I would usually say they are all good but it was their responsibility to check on wait time and pick one. Inevitably, they would ask if I could just submit a formal referral to EACH of the referral centers. No. I will give you ONE referral. I\u2019m not staying late to right five referrals. Not sure if this could be what is happening?\u00a0"
      },
      {
        "id": "o8gg1zr",
        "score": 4,
        "body": "IDK what the norm is, but that isn't how we do it. We call and/or make referral submission first, then depending on specialist either they reach out to client or client is supposed to reach out to them. But we are also in exotics, leaving us with very limited referral options, so it isn't like our clients could even shop around for a specialist if they wanted to. \n\nIf I was a dog/cat client I could see the upside of being able to research my specialist choices first, so I don't necessarily see that letting the clients take the lead there is a bad thing...so long as the rDVM has given them clear instructions on how to proceed and has prepared thorough records and a referral summary for them to give when they call. "
      },
      {
        "id": "o8iup1u",
        "score": 4,
        "body": "See, I think that\u2019s key - how urgent is the case?\n\nUrgent things get warm or coming-in-hot handoffs.\n\nStable things that don\u2019t need hospitalization can refer themselves.\n\nStatus epilepticus? I\u2019m calling. New epileptic that\u2019s having clusters? We will bust that cluster, and if that goes well, send them home with meds and a list of neuros.\n"
      },
      {
        "id": "o8hbyvu",
        "score": 3,
        "body": "It's so strange to me.  These clients typically have no idea what they need when they call.  They call the ER, or triage line asking for a cardio consult, but they don't know why.  Like, do they need it urgently?  Do I tell them to come to the ER?  \n\nWhen I worked in GP, I never heard of this.  It's like sending a person to a foreign country totally not prepared."
      },
      {
        "id": "o8lidu6",
        "score": 3,
        "body": "I was a Referral Coordinator at an ER/Specialty hospital. \n\nThis varies by GP, but the vast majority either tell clients to call a list of provided hospitals, or if they have a preference, call a specific hospital to schedule with a given doctor.\n\nBecause I'm intimately acquainted with the referral process, I'll usually coordinate it for the clients, when I can, or I will CC the clients in the email I submit to the Referral Coordinators of that Specialty. \n\nI know how swamped Referral can get (I managed multiple Specialties alone. Reviewing records for a formal diagnosis and diagnostics done for some .), but I also know the urgency with which some cases need to be seen vs. others. \n\nNot every GP is as good about communicating these things as others. Some just forward records and sort of have the Specialty \"figure it out\".\n\nI am an aggressive advocate for clients, having been on both sides of the referral table. Honestly, working referral was my favorite role, because you're able to strengthen that bond with clients. But also, because referral is somewhat terrifying. Not because it needs to be, but because some clients see it as their primary \"running out of options\".\n\nI wish that Specialty, could, find a way to be more easily implemented into GP, but I understand why that's not always feasible. "
      },
      {
        "id": "o8hj7uu",
        "score": 2,
        "body": "i find it largely depends on the case and clinic. for example, we have some specialty/ER clinics that you do not need a referral to, and some do require one. we do similar to another commenter where we give them a list of recommended specialty locations and they tell us who they want and if referral is needed, we provide one. "
      },
      {
        "id": "o8iu2sp",
        "score": 2,
        "body": "I work at a rural ER only clinic. We refer when we\u2019re out of our depth and the client wants referral.\n\nIf it\u2019s an \u201cOMG this should see a specialist as soon as they\u2019ll take it,\u201d we will call around to find someone to take it.\n\nIf it\u2019s a \u201cyeah, this could use a specialist, but it\u2019s Friday night and no one is open until Monday and it can wait at home,\u201d we send them with a list.\n\nGone are the days of sending to one specialist. We gotta find the first available appointment that is feasible for the client, so we just cut out the middleman and let the client schedule themselves.\n"
      },
      {
        "id": "o8mwck5",
        "score": 2,
        "body": "I work in specialty and most of the time the clients call and make the appointment. Sometimes we have vets reach out to us first if its an urgent thing, but if its not urgent it seems like its the norm to have the clients call.\u00a0"
      },
      {
        "id": "o8nkhs4",
        "score": 2,
        "body": "These comments are driving me insane. I understand giving the client options, but specialities cannot/should not schedule appointments without referrals. What you can do is provide them a list during the GP appointment and then let them choose there where they want to go. Telling a client to \"shop around\" to specialities, when most of the time those practices have ER sides so they can clog up their phone lines is ridiculous. Especially since clients have no idea what service they need most of the time. \n"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rjs7dg",
    "title": "Petition to Preserve and Protect the Veterinary Technology Program",
    "body": "",
    "flair": "School",
    "score": 21,
    "comment_count": 4,
    "created_at": "2026-03-03T15:26:11+00:00",
    "top_comments": [
      {
        "id": "o8fl7gl",
        "score": 5,
        "body": "Was so disappointed to see this on the other sub, then further saddened to realize the call was coming from my native state. Our profession, our clients and our patients deserve better than this, and I am grateful for the response the Change.org petition has received so far. \u2665\ufe0f\u2665\ufe0f"
      },
      {
        "id": "o8fklq2",
        "score": 3,
        "body": "Hey, thanks for sharing the petition in this subreddit. I\u2019ve been trying to get the word out as much as I can & it means a lot you\u2019re helping to send out this message. I am so deeply devastated with what\u2019s happening to the staff and students. They don\u2019t deserve this."
      },
      {
        "id": "o8fkq0y",
        "score": 3,
        "body": "if anyone has any questions about this feel free to ask me. we need all the help we can get. we have been silenced for months about this entire situation."
      },
      {
        "id": "o8f9qmd",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rjrutc",
    "title": "Intubating cats",
    "body": "Does your practice use lidocaine gel or regular lidocaine (like you\u2019d use for injection)? My practice has always used the gel (but it takes time to kick in), a previous coworker had told me her old practice used plain lidocaine in and just put a drop on the larynx. \n\nI\u2019m always looking for tips to improve my cat intubation skills/be more efficient so I\u2019m curious what you guys do?",
    "flair": "Discussion",
    "score": 24,
    "comment_count": 25,
    "created_at": "2026-03-03T15:12:25+00:00",
    "top_comments": [
      {
        "id": "o8fcf5x",
        "score": 43,
        "body": "I use 2% lidocaine solution (double check you aren\u2019t grabbing lidocaine + epi) for every cat intubation. Draw 0.1-0.2mL in a 1mL syringe, remove needle, apply 1-2 drops on the top of each arytenoids, wait 60 seconds, intubate. Here\u2019s an article from the [Journal of Feline Medicine & Surgery](https://journals.sagepub.com/doi/full/10.1177/1098612X18781391) with more info. Attaching a photo from the study as well for reference.\n\nhttps://preview.redd.it/zf64xwo6oumg1.jpeg?width=1320&format=pjpg&auto=webp&s=d6734b5180d9cc5e6ad0fc9d8db4bb16d3e4a902"
      },
      {
        "id": "o8f7fqt",
        "score": 40,
        "body": "A drop on the larynx of the injectable, then wait a minute before intubating.\n\nIt helps to have your cat deep enough too. I think we tend to be hesitant to get many of our animals deep enough for anesthesia. Waiting that minute really helps.\n"
      },
      {
        "id": "o8fnfed",
        "score": 21,
        "body": "https://preview.redd.it/tf719fj4yumg1.jpeg?width=789&format=pjpg&auto=webp&s=5916417925145e5e602fde95ef3c673ba6e71a61\n\nWe use the spray"
      },
      {
        "id": "o8g6z5e",
        "score": 18,
        "body": "I add a step: after removing the needle, put a 22g IV catheter on the syringe and use that to get the drop precisely on the arytenoids. Complications can occur if you put too much lidocaine on or if you get it in the wrong place.\n\nEdit: spelling a word"
      },
      {
        "id": "o8f8fer",
        "score": 9,
        "body": "I've used both the gel and the injectable and don't notice much of a difference, I let it sit on the larynx for at least 30 seconds. \n\nMake sure you have a good view down the throat, and wait until the cat takes a breath to insert the ET tube quickly but gently. \n\nUse a stylet too if needed to help with the floppy flimsy tubes, just make sure you use it correctly so you don't cause any trauma to the trachea."
      },
      {
        "id": "o8fl8zc",
        "score": 8,
        "body": "Drop of lidocaine 2% - to minimize touching the arytenoids I use a catheter attached to a 1 mL syringe and place a drop on both sides and then wait a minute before intubating "
      },
      {
        "id": "o8ffpsv",
        "score": 6,
        "body": "My doc uses a drop of proparacaine HCL, I think because it's fast acting.\n\n*Edit to fix typo*"
      },
      {
        "id": "o8gco8y",
        "score": 6,
        "body": "Gel??? \ud83d\udc40\ud83d\udc40 I\u2019ve only ever seen the spray \ud83e\udd74 now I\u2019m curious what the difference is "
      },
      {
        "id": "o8jdpmq",
        "score": 6,
        "body": "I love doing this! And you just give it like another 30 seconds to kick in and can continue pre-oxygenating - tube just slides in no problem!"
      },
      {
        "id": "o8ile81",
        "score": 4,
        "body": "This method is falling out of favor within the anesthesia community due to many reported cases of the CTA breaking off and ending up going somewhere you REALLY don\u2019t want it to go! Source: I spent a few years in academia and this was discussed often."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rjdjkf",
    "title": "\"I'll take heartworm for 200 please\"",
    "body": "",
    "flair": "Microscopy",
    "score": 47,
    "comment_count": 11,
    "created_at": "2026-03-03T02:45:25+00:00",
    "top_comments": [
      {
        "id": "o8cvpgf",
        "score": 9,
        "body": "I must be blind in my old tech age"
      },
      {
        "id": "o8fco2x",
        "score": 5,
        "body": "I had to look several times too! Towards the center of the slide, about 9-10 o\u2019clock and about 2 o\u2019clock, you can see the little microfilaria wiggling."
      },
      {
        "id": "o8e7gp7",
        "score": 3,
        "body": "that\u2019s nice slide"
      },
      {
        "id": "o8gb191",
        "score": 2,
        "body": "This is a VERY niche way to test for colorblindness."
      },
      {
        "id": "o8etpi4",
        "score": 2,
        "body": "Husky noises in the background ?"
      },
      {
        "id": "o8g551d",
        "score": 2,
        "body": "Also blind and old \ud83e\udd23"
      },
      {
        "id": "o8ge6lc",
        "score": 2,
        "body": "Shepherd \ud83d\ude02"
      },
      {
        "id": "o8l7bf0",
        "score": 2,
        "body": "Illinois but the pet is from an \"outdoor shelter\" that refused to treat because \"they'll just get it again.\""
      },
      {
        "id": "o8m9qbu",
        "score": 2,
        "body": "How horrible...that poor dog."
      },
      {
        "id": "o8cf4u0",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rj5byf",
    "title": "How long should discharge appointments take?",
    "body": "Hey guys just want to get a general idea of how long people take when discharging patients. I\u2019ve been told by my head nurse that I\u2019m taking too long when discharging, usually I take about 10 mins sometimes 15 depending on whether the owner has questions. My head nurse told me that for cats I should be taking roughly two mins and dog spays and castrates 5 mins. I\u2019m not sure about this because I feel like there\u2019s a bit to go through when discharging, especially after surgery .Do others think I\u2019m taking too long? ",
    "flair": "Discussion",
    "score": 38,
    "comment_count": 27,
    "created_at": "2026-03-02T21:09:37+00:00",
    "top_comments": [
      {
        "id": "o8arnaa",
        "score": 140,
        "body": "Honestly I\u2019ve never been cool with the whole timing as a measure of success when it comes to medical care. I want things done right, not fast."
      },
      {
        "id": "o8awihq",
        "score": 53,
        "body": "A surgical discharge takes as long as it takes. People are paying you good money for your care. If your practice wants to convey value for the service then be prepared to accept that this is something that doesn\u2019t have a time limit. Especially for first timers. I have such a \u201cthing\u201d about surgery\u2026 if your prep of the surgical site looks like shit then the client has every right to wonder what it looks like on the inside. Don\u2019t skimp on a surgical procedure. Take the 5 extra minutes to make sure that patient leaves tip top. Do the sniff test, make sure that IV is out and that boo boo bandage is off. If I can\u2019t remove a bandage for WHATEVER reason I explicitly tell the client to remove it in 30 minutes. \nMy exception to this\u2026 if you have that client who keeps asking you over and over the same questions and is clearly not listening then you go line by line and say if you have any follow up questions please call prior to close or the available ER after hours.  Above all things document your interaction or else it didn\u2019t happen."
      },
      {
        "id": "o8aro2q",
        "score": 42,
        "body": "5-10 mins. more extensive things like TPLO sure maybe 10-15 but what i would recommend is that you make a template of what you discuss at your discharge. review it with your client. if they have questions they can always refer back to the discharge paper you give them about XYZ surgery or they can call. an easy discharge template can be made at AAHA. (google AAHA DISCHARGE TEMPLATE or aaha dental discharge template) easy"
      },
      {
        "id": "o8arw98",
        "score": 39,
        "body": "and FWIW i think 5 mins flat may be too short. people are paying you for their time and *most* owners appreciate being educated"
      },
      {
        "id": "o8b2r5k",
        "score": 28,
        "body": "Imagine if it were the other way around. One of your family members has surgery and you\u2019re expected to take care of them for the days immediately afterwards. You\u2019ve already gone through a lot of emotions that day and it\u2019s still not over yet. Then the nurse takes 2 mins rushing through your instructions. That would leave a pretty bad taste in your mouth, wouldn\u2019t it? I have my regular speech where I summarize each point on the sheet, which does go by pretty quickly, sure. But I always take as much time as the owners need me to answer their questions. I also will take the time to explain any additional diagnoses, like stomatitis on what was supposed to be a routine dental cleaning, or show them xrays or photos we took intra-op, etc."
      },
      {
        "id": "o8bd743",
        "score": 24,
        "body": "It may be an unpopular opinion, but I believe discharge should take as long as it needs to take.\u00a0\n\n\nEvery patient is different, every client is different. Some people may need more hand holding and explaining than others.\n\nIt should never be about the time.\u00a0\n\nThe job of the discharging person is to make sure that client leaves the hospital feeling well informed and capable to carrying out the at home care. And that they had all their questions and doubts addressed.\u00a0\n\nSometimes a discharge may take 5 minutes for a complicated procedure because client has been there before with same or another pet, sometimes a simple procedure discharges may take an hour because client has never dealt with anything like that and is completely overwhelmed.\u00a0\n\nOf course, I will try to be as efficient as possible, but I will not rush through a discharge and leave clients lost and overwhelmed."
      },
      {
        "id": "o8archd",
        "score": 17,
        "body": "i mean if you're dispensing meds to take home - i wouldn't trust the owners to understand the instructions just for those, in under 5mins. unless its a seasoned, unicorn, pet owner. "
      },
      {
        "id": "o8asi1n",
        "score": 16,
        "body": "I go through the discharge instructions point by point, and make sure they understand the meds. I even have them sign the discharge inst. and make a copy for the chart. I would rather a few extra minutes to be certain an owner can care for the pet than have to do a whole 'nother procedure because the dog chewed her abdomen open, or worse was OD'd on nsaids or not get enough."
      },
      {
        "id": "o8bn92b",
        "score": 5,
        "body": "This really depends on the case and the client. Sedated radiographs? 5 min. Small mass removal on the dorsum? Quick, easy 5-10 minutes. Spays and abdominal surgeries a little longer. When you move into more complicated stuff like TPLOs and orthopedics those are going to take longer since there's a lot to cover in regards to exercise limitations and the reintroduction of activity over a specific amount of time. Newly diagnosed diabetics that presented in DKA, esophagostomy tubes, cataract surgeries, hemilaminectomies- I've spent upwards of an hour with these clients at discharge.\n\nThat said, I'm a firm believer in taking as long as the client needs to feel comfortable taking their pet home. This stuff is easy for us, literally our jobs, and I can only imagine how intimidating it is to take home your pet who now needs insulin twice daily and has a freestyle libre placed, how scary it is to have to perform recumbent care and bladder expression on your paralyzed dog, feed your cat 4-6 times a day through a tube after preparing the special slurry prescribed by the doctor, or administer 6+ types of eye medications every 4-6 hours. These things can't be rushed and we are doing the pet and client a disservice if we send them on their way without them having a firm understanding of what they are doing and what to expect when they get home. Additionally, taking more time during discharge will (typically) reduce the amount of calls and time taken later to re-explain everything. I find it's the multiple follow-up calls with questions that become a real time sink. If we do it right the first time, it actually saves us time in the long run."
      },
      {
        "id": "o8clkh2",
        "score": 5,
        "body": "A discharge appointment should take until the owner's questions are answered and they understand the treatment plan"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rj1bun",
    "title": "Seeking advice: Getting out of clinical practice",
    "body": "I've been a veterinary assistant since 2019, and every day I find myself more and more miserable. I finally started making enough money to save and pay off debts when I was a supervisor (by title, manager by workload and expectations), but I couldn't handle the increasing demands and dwindling resources. I left my position in hopes of finding less draining work with the understanding that I'd be making less. After taking an assistant position in another hospital that claimed to value Fear Free practices and strong client relationships, I'm once again stretched too thin and not proud of the work we're doing. I want to leave.  \nMy leadership and supervisory experience doesn't seem to mean much outside of the industry and isn't enough to compete with other applicants for open practice management roles. My friends who have left ended up in communications or have had to go back to school. I'm one semester away from getting my LVT and I dread the idea of starting another program just to be stuck in the same cycle.  \nPlease, anybody who's gotten out, I will take any advice that you have.",
    "flair": "Burn Out Warning",
    "score": 6,
    "comment_count": 4,
    "created_at": "2026-03-02T18:44:52+00:00",
    "top_comments": [
      {
        "id": "o8a26fn",
        "score": 6,
        "body": "You have more transferable skills than you think, even as a veterinary assistant.\n\nTry warehouse work, that\u2019s what I did first when I got out. I made a touch more (night shift) and it was a great transition job until I figured out what I wanted to do from there."
      },
      {
        "id": "o8a79q5",
        "score": 4,
        "body": "I just finally accepted the end game wasn\u2019t doable. That\u2019s largely why I never sat to get licensed despite the education. I got to my last semester and the hatred ran so deep. It was all issues above my individual level to fix in the industry. So I bit the bullet and decided to redo my education. I\u2019m hopeful that the skills I learned here will do me well in finance. I feel like the detail level has insanely prepared me for analytical roles. I\u2019m breezing through accounting and economy classes. "
      },
      {
        "id": "o8czedp",
        "score": 3,
        "body": "I have been in the field since 2016. Started as a kennel tech where I was responsible for 50+ animals during the busy seasons. As well as helping the head tech prep animals for surgery, recovering, holding for nail trims, blood draws, anal glands, laundry, autoclaving...50+ hours were the norm. Got burnt out very fast. Worked for two years to get the privilege of being a vet assistant, where I regularly worked from 7 am until 9 pm. \n\nMoved and got a new job. Left after a vet screamed at me that I wasn't ready for his boarding appointment dogs after he was done with surgery because I refused to pre draw vaccines to leave out for hours. \n\nThe next job felt like a dream come true. Cat only clinic. And for awhile it was. But now I work 4 job descriptions (admin, reception, kennel, and assistant) and I am always pulled so many ways that a couple of years ago I decided to go back to university for business analytics. Not to mention 2 'techs' that were so undertrained and skilled that they were liabilities and working with them made the job 1000% harder. \n\nFinally graduated and just got a job that starts in June in sales. After almost 11 years, I feel so free. You have transferable skills. Talk about selling to people as far as symptomatic treatment vs gold standard (like estimates). Discuss disagreements with coworkers, or how you can handle angry clients. Discuss working in a fast paced, collaborative environment. Communication skills. Think outside the box. It is hard to market yourself in a new way, but it is possible. Discuss how you improved something. For me, it was our inventory reordering system."
      },
      {
        "id": "o89w67v",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1ritfyu",
    "title": "I can\u2019t afford to live on my own",
    "body": "For people that live alone and only have 1 job as a tech, how do you afford it? If you do have a second source of income, what is it? TIA!",
    "flair": "Work Advice",
    "score": 51,
    "comment_count": 20,
    "created_at": "2026-03-02T13:54:50+00:00",
    "top_comments": [
      {
        "id": "o88kxnj",
        "score": 66,
        "body": "Eat a lot of rice, pack a lunch, and don\u2019t have a life it\u2019s easy just work two jobs then you won\u2019t have time to spend money lol. No, it sucks and just this week my one boss because I work full time at er and part time GP, at the GP says he thinks it\u2019s ridiculous that techs want $25 an hour and some assistants to. I told cost of living is insane and cost of school keeps going up to so what do you expect. Yeah there will be a reckoning and I feel like it will be a mass exodus of the field. Everyone is short staffed as it is. People told me 20 years ago this field does pay shit and sadly it is better than it was but still underpaid. Sorry I don\u2019t have an answer for you."
      },
      {
        "id": "o891prt",
        "score": 37,
        "body": "I agree except I don\u2019t think the doctors are overpaid. They are sadly often overworked too. All I know is something has to change."
      },
      {
        "id": "o890mf9",
        "score": 33,
        "body": "Have you ever talked to a DVM? They are definitely not overpaid. The average DVM makes $150,000 which is not much for a doctorate level medical professional. Most of them have so much debt from school they will never be able to pay it off.\n\nThe entire field is underpaid in general, but it is largely regional. Some areas pay much better then others. "
      },
      {
        "id": "o88drh8",
        "score": 29,
        "body": "dog walking and pet sitting is super cliche but it only works if you do it right. my girlfriend used to be a kennel tech and started her own grooming/pet sitting/walking business. she makes about $400/mo walking her regulars, pet sitting varies but if you can pet sit 2 animals a month for 3-5 days that\u2019s another $300-$600 a month. finding a client who will use you consistently is your best friend. you need to advertise everywhere and all the time until you get a solid base of clients"
      },
      {
        "id": "o88mjvl",
        "score": 27,
        "body": "This is what makes me made about the vet field. Veterinarian\u2019s are way over paid and the techs are underpaid. Techs do most of the work and barely get by financially. In the human field a tech only specializes in one thing usually, like x-ray tech, anesthesia, surgical assisting, etc. Vet techs do EVERYTHING, are on their feet constantly, get regular exposure to radiation from the way x-rays are taken, and have soooo much to know and continue to learn with CE. I have a feeling that clinics will eventually suffer when they have a hard time trying to find any techs that want to apply, it\u2019s an overworked/underpaid situation."
      },
      {
        "id": "o88zijq",
        "score": 12,
        "body": "Honestly, if you can, move.\n\nSome places like Texas and Florida pay very low even when accounting for COL.\n\nSome places like the PNW pay much better compared to COL."
      },
      {
        "id": "o8a7hr0",
        "score": 10,
        "body": "i have one job and work full time and have my own apartment (no roommates). but i am an outlier for that situation because i got VERY lucky to have a unicorn job that pays me very well for the field and my pay is above average for RVTs in my area (i make $30/hr). i mean i\u2019m not filthy rich by any means of course but i am grateful that i can reasonably afford my own place. i pay $1,093/month for a 1br 768sqft apartment. that\u2019s actually not even the cheapest rent around here currently, but there were some non-negotiable factors for me personally that i chose over having cheaper rent (size, not being on the first floor, having a balcony, central air, having a parking lot and not street parking, etc). \n\naside from my income, having a detailed budget to consider every single financial decision i make is absolutely crucial IMO (my entire income and budget is on a spreadsheet that i update with every paycheck \ud83e\udd23). \n\nliving alone is definitely possible for some, but  factors like location or title protection laws by state/region REALLY lower that possibility for probably most people in this field in general. i live in the US in southern ohio, for context. the cost of living where i am is not as high as other areas while still being pretty close to larger cities."
      },
      {
        "id": "o88d9i4",
        "score": 7,
        "body": "Really depends on where you live. \n\nI have my own home, but I inherited the down payment and chose a home with a suite. So I have that as a second source of income. I also have a second job with the CVMA but it\u2019s only about 120 hours/yr."
      },
      {
        "id": "o89wprs",
        "score": 6,
        "body": "Eat a lot of rice, beans, cheap meats like sausage. Drink only tap water. Buy in bulk, freeze for later.   \nYour hobbies are going to become things you can do for free. Walking, meditating, etc  \nGet a gf/bf so you can have 2 incomes lol (i guess that doesn't count as living on your own)  \nMove to a place with a lower COL, another state if you have to (keep in mind wages will decrease too)  \nA did a lot of ebay selling in my early days and only bought things if they were used/on clearance. I fixed what I could. If I needed something new, I'd try to drop hints or flat out tell family/friends for christmas  \nOh yeah and don't get hurt, you can't afford it"
      },
      {
        "id": "o89oeow",
        "score": 5,
        "body": "So I got married last August and me and my wife just merged our finances together so I don't have this issue, but prior to her, I just rented a place that I could honestly afford. FAR from a luxury place and lacked a lot of stuff that you'd expect a place to have, but this is the life of living a vet tech wage. For extra money I do a lot of relief work on Roo and I pet sit for people at my job."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rig1x4",
    "title": "Need some vet med/sciency name ideas for a pair of male rats",
    "body": "I'm currently in a vet tech program and my college has some rats that are ex lab rats they use to teach small animal handling and restraint that will be up for adoption at the end of the semester. I've decided I'm going to adopt the pair of big sprague dawley males they have who are super skittish and traumatized but I've fallen in love with the little bits of personality I've seen from them so far.\n\nOne is super shy and likes to just hide in his cave while the other is a lot braver and crazy food motivated which also means he can be a biter at times if he thinks there's food around.\n\nI've thought maybe Pestis and Bubo as references to the plague but I'm not fully sure if I like it or not and I kinda want to find names vaguely vet med related as a reminder of how I got them. Other ridiculous name ideas are also welcome I just don't want to give them the typical generic names like snowball or something like that \ud83e\udd23",
    "flair": "Discussion",
    "score": 24,
    "comment_count": 49,
    "created_at": "2026-03-02T01:58:21+00:00",
    "top_comments": [
      {
        "id": "o85s561",
        "score": 53,
        "body": "Idexx and antech"
      },
      {
        "id": "o85rbbw",
        "score": 37,
        "body": "Pinky and the Brain!"
      },
      {
        "id": "o85s07y",
        "score": 31,
        "body": "not me thinking cerenia and convenia \ud83d\ude2d oh fuck just realized it\u2019s male rats but i mean!!!"
      },
      {
        "id": "o85rp6r",
        "score": 18,
        "body": "Kelly and Crile"
      },
      {
        "id": "o85ziwv",
        "score": 15,
        "body": "Ace and Traz"
      },
      {
        "id": "o85rf0o",
        "score": 13,
        "body": "Obviously Pinky and The Brain ! I know they were mice but still. \n\nOr\u2026\n\nDr. Bunsen Honeydew and Beaker?"
      },
      {
        "id": "o860mti",
        "score": 12,
        "body": "Lepto & Lyme"
      },
      {
        "id": "o86yldi",
        "score": 12,
        "body": "You mean, Cere\u00f1io and Conve\u00f1io."
      },
      {
        "id": "o85rz9s",
        "score": 10,
        "body": "Hopper & Silverstein \nAfter the author\u2019s of the Veterinary Critical Care Textbook \n\nDopamine, Serotonin, Oxytocin, Histamine\u2026"
      },
      {
        "id": "o8677qd",
        "score": 9,
        "body": "Clip and Clean"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rifnp1",
    "title": "Most memorable animal containment methods",
    "body": "If you work in this field, odds are, you\u2019ve seen some interesting things used to transport animals in. \n\nWhat are your most memorable?\n\nI\u2019ve had SO many cardboard boxes with cats inside.\n\nLots of lizards/geckos in Tupperware. \n\nA bird in a purse. \n\nMy personal favorite was a rectangular laundry basket with an oven rack on top - tied together with shoestrings. It contained a fractious cat (of course).",
    "flair": "Discussion",
    "score": 87,
    "comment_count": 83,
    "created_at": "2026-03-02T01:39:28+00:00",
    "top_comments": [
      {
        "id": "o85nhhh",
        "score": 100,
        "body": "Not really contained but I had someone bring in a eagle just holding it. Just walked into the lobby holding an eagle"
      },
      {
        "id": "o85pb69",
        "score": 68,
        "body": "A Pekingese zipped into a roller suitcase because it was so aggressive and wouldn\u2019t stop trying to bite the owners and happened to jump into the suitcase at home."
      },
      {
        "id": "o85q5l2",
        "score": 60,
        "body": "Cat in a lunch box\n\nCat in a bird cage\n\nCat in a backpack (like a normal ass bookbag)\n\nCat in a filing box\n\nCat in some type of decorative basket with a lid\n\nCat in the hoodie the person was wearing\n\nCat in a stroller\n\nCat in a pillow case"
      },
      {
        "id": "o85tdih",
        "score": 44,
        "body": "My two faves:\n1. A bat flying around in a grocery bag. \n2. A stunned squirrel in an open cardboard. It jumped out of the box and straight at our CSR.\n\nWe don't even see wildlife."
      },
      {
        "id": "o85q57v",
        "score": 43,
        "body": "Those zipper laundry/toy hampers - seen cats and small dogs in those. \n\nTwo laundry baskets duct taped together - even brought their own tape for us to use and put it back together when we were done. \ud83d\ude05"
      },
      {
        "id": "o863wbj",
        "score": 40,
        "body": "https://preview.redd.it/afjg9h3gwjmg1.jpeg?width=4032&format=pjpg&auto=webp&s=f861ddf0e5fb95ed97bacc115ba1afd821525a43\n\nAlso, this cat carrier."
      },
      {
        "id": "o85tflu",
        "score": 36,
        "body": "Hamster in a toy school bus that we couldn\u2019t get it out of without rattling its brains."
      },
      {
        "id": "o85uhba",
        "score": 35,
        "body": "One of our clients would drive her pig around in the back seat of her 2 door Honda civic. She\u2019d just open the door and the pig would stroll on out. \n\nAnd I don\u2019t mean like a little potbelly. This was like a full grown, 500lb Yorkshire Sow. The lady put her bed on cinder blocks so it wouldn\u2019t collapse under her weight."
      },
      {
        "id": "o85q78d",
        "score": 33,
        "body": "Ups box where an exacto knife was used to cut slits in the top of the box that another piece of card board was slipped into for a shockingly effective latching mechanism"
      },
      {
        "id": "o8629wq",
        "score": 32,
        "body": "Someone brought a pheasant with a broken wing in a shoe box. It didn't move for a while and triage was crazy so he was moved to the side, presumed dead. U N T I L I was placing a catheter in a patient and the pheasant sprung out of that Adidas box like the Kool Aid Man and scared the absolute shit out of me."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1ribve2",
    "title": "Penn Foster Vet Tech Program",
    "body": "Hello! I just wanted to hop on and ask for any suggestions/advice regarding the Penn Voster Vet Tech Program. I am currently working full time as a phlebotomist, thinking of transitioning into animal med. The only in-person course in my area is 40 minutes away, and takes 2 years to complete. Do you guys recommend this program for someone looking to step into vet med? Are clinics likely to hire someone like me with no experience? I would be open to applying to assistance positions while taking this course, but do you know if most clinics would accept that? Thank you for reading!",
    "flair": "Work Advice",
    "score": 3,
    "comment_count": 31,
    "created_at": "2026-03-01T22:55:36+00:00",
    "top_comments": [
      {
        "id": "o84w9b9",
        "score": 30,
        "body": "I\u2019m in the final externship and I wouldn\u2019t recommend it to anyone. It\u2019s a pain in the ass at nearly every step. Better off looking into in person or other online schools."
      },
      {
        "id": "o84whaw",
        "score": 17,
        "body": "I do not like Penn Foster. They\u2019ve given me a headache. On average, I\u2019d say it does not take 2 years because of wait times and such. Do another distance college, or just do the in-person and bite the bullet on the drive. If I could turn back time, I\u2019d just do in-person - or not do vet tech school at all."
      },
      {
        "id": "o84xnl7",
        "score": 15,
        "body": "Everything was for me - they took forever to process my transcript, so I ended up paying for a class I didn\u2019t need.\n\nThe externships could be their own post. It\u2019s a nightmare. \n\nGrading in general takes way too long. They\u2019ve been working on it, but still. I would\u2019ve finished by now if things didn\u2019t take so long. \n\nThey also didn\u2019t credit me for the 3rd semester classes I had transfer credit for - I had to fight to get that money back. They were going to let it \u201cslide\u201d and pretend I never noticed. I did, and they owed me around $700. That was a pain too, you can just never get a hold of anyone that can actually help.\n\nAs far as the classes - I haven\u2019t really learned a lot, I regret to say. I know most of what I do due to working in the field. The books can be helpful, but when every quiz is open-note\u2026 it doesn\u2019t really encourage people to learn. Have a coworker in the program now like that."
      },
      {
        "id": "o84wcha",
        "score": 10,
        "body": "I recently completed the PF VT program and it\u2019s\u2026 not as easy as they want you to think.  If you don\u2019t have a lot of vet experience I strongly recommend working in a clinic for a bit before enrolling to see if it\u2019s something you enjoy.  The program is 100% self-driven, so you get out what you put in, but if you don\u2019t have previous experience there are a lot of gaps in the program that are hard to fill imo.  \n\nLots of clinics in my area (New England USA) would accept someone with no experience as an assistant, boarding attendant, etc. but they do not pay very well so you\u2019d likely be taking a significant pay cut.  \n\nAll in all I think the program can get you where you want to go, but it\u2019s not as simple as they say"
      },
      {
        "id": "o84zanq",
        "score": 5,
        "body": "I didn\u2019t go through the program, but a friend did and they gave her nothing but bullshit. Like anything that could go wrong on their end did. It took forever and a bunch of of jumping through hoops to graduate from it."
      },
      {
        "id": "o85lpox",
        "score": 5,
        "body": "I graduated from Penn Foster and would not recommend it. The externships are ridiculous."
      },
      {
        "id": "o85a7o1",
        "score": 5,
        "body": "I think this is a take you have because you aren\u2019t on the receiving end. It\u2019s not about the \u201creal world\u201d. It\u2019s because their system is completely and unnecessarily complicated, they are exceedingly nitpicky, and their wait times chew up a lot of their limited semesters. \n\nIt feels like they want to stall progress as much as possible to receive extension fees. I\u2019ve been waiting for an externship approval for four fucking months!!! That is ridiculous!"
      },
      {
        "id": "o85x2nd",
        "score": 5,
        "body": "I'm currently in it. They only give you 8 weeks for it and some fo the things they expect you to do at a GP are ridiculous. They are incredibly picky and take ages to grade everything. What was supposed to be a 2ish year program has turned into 4 for me...and like I said I'm just now hitting the first externship. "
      },
      {
        "id": "o859lrm",
        "score": 4,
        "body": "I\u2019m doing my program 100% online through Dallas College and its been great so far, though I\u2019m in state so it might be pricier for you if you\u2019re not in Texas. No experience with Penn Foster but just based on what I\u2019ve heard it sounds like community college programs might be less of a headache.\n\nA community college program will probably take you 2-3 years to complete depending on how many classes you want to take per semester. \n\nhttps://www.dallascollege.edu/study/veterinary-tech/"
      },
      {
        "id": "o84wdx6",
        "score": 4,
        "body": "Thank you so much for the insight- could you elaborate on what aspects of the program is a pain?"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1ri66bb",
    "title": "Vet Assistant Training Feels Very Rushed?",
    "body": "Hi folks! Thank you for reading. I appreciate it :)\n\ntl;dr: Wondering if four 8 hour days is a normal pace for on-the-job training for a Vet Assistant before being evaluated on drawing blood, vaccines, giving meds, etc. Training is 3 shadow days and 1 evaluation day where I am supervised the entire day but doing everything myself. I have no medical experience but extensive animal/kennel care experience.\n\nContext:\n\nI was just hired as a VA with very little medical experience (I have some personal training with first-aid but not professional). I was very honest in my interview about having a lot of kennel/care/cleaning experience but not medical. They were still interested and hired me. They told me that I would have plenty of training before being on my own and that I would mostly be assisting the hospital with cleaning and going around to give meds. I went in for onboarding and found out that my training process would actually only be 4 days total before I would be evaluated and expected to meet certain criteria to hold the position. These criteria are extremely outside my comfort zone and skillset especially going from 0 - fully independent in 3-4 days. I am expected to draw blood, create prescription labels, give vaccines IM/SQ, tube feeding, etc. and be tested after those 4 days.\n\nI was also told I would be a supplemental 2 day per week employee (16 hrs) but now I am being scheduled 4 days per week (32 hours) even after training week. I found out that each workday, I will be the only VA doing the above tasks in addition to cleaning, nail trims, ear cleans, etc. There are others but they are helping with surgeries all day.\n\nI just feel like this is extremely fast pacing and rushed training but maybe I am overthinking it. I honestly feel like I am not going to be able to meet the benchmarks that soon. Does this sound like a normal pace?",
    "flair": "Work Advice",
    "score": 9,
    "comment_count": 19,
    "created_at": "2026-03-01T19:16:15+00:00",
    "top_comments": [
      {
        "id": "o83ssrq",
        "score": 15,
        "body": "No that is not normal, and frankly it\u2019s dangerous and unacceptable. Are you in the US? If so, what state? A lot of red flags here, and depending on location they may be asking you to do things that are reserved for licensed personnel. They knew you had little medical experience and still hired you knowing the expectations they\u2019d be placing on you. Rushing training. Stating one thing for your hours and immediately placing you on the schedule for double the hours without consulting you. Placing a brand new person on their own after 4 days is absurd, especially with minimal supervision and additional responsibilities not initially disclosed. \n\nThis sounds like a place desperate for bodies, setting staff up for burnout and failure. All this is a sign of bad management. It\u2019s ok to walk away and just say this doesn\u2019t sound like a good fit. We\u2019re not even getting in to the stress and injuries they\u2019re subjecting you and patients to by putting untrained staff in this position."
      },
      {
        "id": "o83vzvq",
        "score": 10,
        "body": "This place sounds\u2026 desperate. In my area it\u2019s hard to even get a vet assistant position without any experience. \n\nHave you started training yet? Maybe there\u2019s some miscommunication? Blood draws, nail trims, AGs and ear cleaning would all normally take 2 people, someone has to hold the animal. Maybe you\u2019re misunderstanding how actually independent they expect you to be? \n\nIf not then yeah that\u2019s pretty insane for someone with no medical experience. Learning to handle fractious animals in itself takes time. It\u2019s dangerous to rush that experience imo, assistants should always have help available."
      },
      {
        "id": "o83vbt6",
        "score": 7,
        "body": "Yes I am in the US - OR to be specific. They seemed pretty tense in their clinic and I just found out they are in a big state of staff transition from top to bottom. So it seems very off and ripe for burnout. I\u2019m recovering from burnout as it is."
      },
      {
        "id": "o845bzn",
        "score": 5,
        "body": "I've done a lot reviewing the protocols/handbooks but not practical training yet. They have a pretty detailed timeline set up for me and it outlines it as: 1. I attempt to do the task independently. 2. Ask for help with restraint or use sedation.\n\nI am expected to do the blood draws, vaccines, SQ fluids, feeding tube, etc. though myself. I am not confident I would be able to do these things, even with someone restraining, by myself after only 2 days of shadowing, 1 day of practice, and then be tested the next day. I could definitely become confident with more practice but it seems so rushed.\n\nedit: typo"
      },
      {
        "id": "o859pdr",
        "score": 3,
        "body": "Yes my state has \u201ctitle protections\u201d but without any real scope of works restrictions, which I think is a lot of the problem. Why hire a licensed tech when an assistant can do the same for less?"
      },
      {
        "id": "o882nar",
        "score": 2,
        "body": "I don't understand why this  would be downvoted."
      },
      {
        "id": "o85o1h3",
        "score": 2,
        "body": "Have you looked at the state laws around techs vs assistant duties and what you're actually legally even allowed to do alone? Because this sounds sus, even just at the expectation-level. For example (and this is only with a little bit of Googling, so apologies if I'm way off) it looks like in OR a vet assistant *can* draw blood but ONLY under direct supervision. Which cannot feasibly be done if you are expected to be doing them alone. This doesn't sound right at all."
      },
      {
        "id": "o85c4us",
        "score": 2,
        "body": "Bingo!\n\nWhich is a vicious cycle in and of itself.\n\nIt's great in an emergency if you don't have a licensed technician on-site that an assistant can adequately complete the task, but it presents a liability.\n\nGiven operations concerns faced by many clinics, doctors opt for the cheaper option.\n\nBut that's part of a much larger discussion relative to how many licensed techs to doctors, and by extension, assistants one needs to realistically hire for the types of cases seen in smaller GP settings."
      },
      {
        "id": "o83ouqh",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o84khsy",
        "score": 1,
        "body": "Okay.\n\nI think you need to go back to your office manager and present them with some feedback.\n\nDo so professionally, and avoid inserting feelings, and instead focus on facts. Cite what you need in order to succeed and best meet their needs. Both of you are investing in one another, and not providing you with the appropriate level of support will not only result  in poor job performance on your part, but them potentially needing to hire someone else, and begin the hiring-training process anew.\n\nPresent them with a tiered training plan, and ask to be precepted by someone that allows you to sign off on a daily/weekly checklist of tasks you should master.\n\nI, personally, don't think the hours is an issue, in so long as you're actively working with someone to learn and master those skills. Which you're not. I am more concerned about the advanced nursing skills that you're required to complete, though this may vary by state. Still, you just started in the field, so... that's not good.\n\nWhen I worked in human med, the new nurses would work closely with more senior nurses, and meet with the nurse educator to get more in depth training and evaluate skills.\n\nI sometimes wish veterinary medicine had an equivalent role for a nurse educator, though I suppose that's what leads are for in practice. \n\nIf you need a resource for a tiered training plan, feel free to reach out.\n\nI wish I would have advocated more for myself in the past, but no use ruminating over the matter."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rhvaa8",
    "title": "Tips to avoid burnout?",
    "body": "Next month I will be moving back to my parents\u2019 house so I can save some money (and also because my lease is up) and they live 1.25hours away(61miles/99kms) from where I work, so I will have a 2.5hour commute daily. I work 40 hours per week (10 per day x 4 days) and honestly even now when I get home I\u2019m already so tired I usually just go to bed. \n\nI\u2019m now going to have this drive to/from work added to my days and I wanted some advice on how best to prepare/not burn out. I could be doing this for the next 6 months or so\u2026 ",
    "flair": "Work Advice",
    "score": 9,
    "comment_count": 6,
    "created_at": "2026-03-01T11:43:19+00:00",
    "top_comments": [
      {
        "id": "o8241dd",
        "score": 26,
        "body": "To avoid burnout? \n\n1 - change clinic to one that is less than 30 minutes away\n\n2 - walk there and back as much as possible (presuming it's not just highways and you have access to descent public transit)\n\n\n3 - change clinic to one that is less than 30 minutes away\n\n4 - spend as much time outdoors  / touching grass / doing your hobbies and **NOT** being \"productive\" as possible \n\n5 - change clinic to one that is less than 30 minutes away\n_____\n3hr transit is INSANE, you can't live like this."
      },
      {
        "id": "o82fszx",
        "score": 6,
        "body": "I think that commute is going to cut into the money savings.\u00a0 Gas/electric will add up.\u00a0 Any maintenance that is expected after a certain mileage.\u00a0 You'll also get to the point of needing a different vehicle a lot quicker.\n\n\nI agree that the commute doesn't seem worth it.\u00a0 I have a 45min each way commute and it's already hard on me."
      },
      {
        "id": "o81tv0g",
        "score": 3,
        "body": "I'm going to, potentially, be dealing with a similar commute, by train.\n\nI don't necessarily want to, but it's complicated!\n\nI would say that your best option is asking if you can come in 15 minutes earlier, and leave 15 minutes prior to your scheduled shift. You still make your hours, BUT at least you get a head start on your rest.\n\nMeal prep on your days off. \n\nIt helps immensely, because coming home after a long shift/commute, is no fun when you also need to cook your meals!\n\nDisconnect as soon as you get home!\n\nNo social media scrolling, checking in on cases etc.\n\nHome is for home!"
      },
      {
        "id": "o83y0ag",
        "score": 3,
        "body": "I did 1.5 hr commute for yeearss, but most times on public transit. Do you have that option? Instead of a stressful drive it was great time for me to read, study, scroll, nap, whatever. If you are driving for sure, find a podcast you love, or audiobooks, it makes the time go by faster. And prep food for the drive so you can relax when you're home. Id eat my breakfast on the road and a sandwich or something for the drive home.  That way when you're home you can shower/unwind/rest fully."
      },
      {
        "id": "o81e30d",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o848m0a",
        "score": 1,
        "body": "Unfortunately not, I\u2019m in semi rural Australia and I think there *might* be 1 bus per day but that\u2019s it \ud83d\ude23"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rhkw7i",
    "title": "Sales Reps",
    "body": "How do those of you who have transitioned to working as sales reps for Chewy, MWI, BI etc. deal with the unique pressures of your job? Both from your employers, and the clinics you work to maintain a relationship with?\n\nI sometimes feel bad given how some doctors speak to sale reps.\n\nThey're only there to do their job. They answer questions to the best of their ability, but sometimes they get treated rather poorly.\n\nSo, my thanks to our sales reps who go above and beyond in maintaining their composure.",
    "flair": "Discussion",
    "score": 18,
    "comment_count": 13,
    "created_at": "2026-03-01T02:05:03+00:00",
    "top_comments": [
      {
        "id": "o7zhvvf",
        "score": 16,
        "body": "Hahaha as a former rep, the doctors were the least of our problems. Hospital managers and techs were way worse. \n\nIt\u2019s a hard job. I worked as a rep for a pet insurance company, a pet food company, and a pet cremation company. I loved the education part. I loved building relationships and teaching folks about things I genuinely believed would make their lives and jobs better. \n\nI hated the quotas. \n\nI wasn\u2019t great at it. Hahaha \n\nSo now I work in veterinary corporate training and support and it\u2019s a way better fit."
      },
      {
        "id": "o7zl23p",
        "score": 12,
        "body": "Eh, too many reps are pushy, seem to feel entitled to drop by any time, and not particularly helpful. \n\nI like some of ours...but feel they are generally unnecessary middle men that dont accomplish anything in their visits that an email or phone call wouldn't."
      },
      {
        "id": "o7zoza6",
        "score": 7,
        "body": "Sure...but the reps virtually never have more info on those than a one-page flyer / email does."
      },
      {
        "id": "o7zjjgz",
        "score": 5,
        "body": "I'm curious about the difficulty with hospital managers and technicians.\n\nI don't ever want a rep to feel like I am grilling them. I've learned that it's not the place to flex what I know, or think I know. If I have a question, I'll read the literature they provide us, and shoot them an email. \n\nTheir jobs are hard enough as it is.\n\nI want to practice kindness in my dealings with people."
      },
      {
        "id": "o7ztf9z",
        "score": 4,
        "body": "When I was the tech in charge of inventory at my first clinic I would be the one to talk to the reps. Most of them I enjoyed visiting with but I could not stand the Zoetis rep that we had. He was pushy, nosey about our personal lives and just a prick."
      },
      {
        "id": "o800x8x",
        "score": 3,
        "body": "Agreed. We had an old Zoetis rep who was the equivalent of a car salesman about Apoquel when they were first advertising it."
      },
      {
        "id": "o831g3p",
        "score": 2,
        "body": "You\u2019re right - a position in industry comes with unique challenges. I have worked for 2 of the \u201cbig 4\u201d animal heath companies and have thoroughly enjoyed my career. Before getting a job in industry, I worked as a credentialed VT. \n\nSometimes I miss the hands on aspect of clinic life. Sometimes I miss feeling like I make a dramatic difference in the lives of pets. \n\nHowever, there are absolutely perks to working in industry. The pay has been significantly better than in clinic, benefits are wonderful, and work/life balance is much improved. I also don\u2019t get covered in scratches or bodily fluids any more! \ud83d\ude06\n\nThe downside? The pressure. Animal health is not immune to downturns or layoffs. Specifically in sales roles, I struggled with the large quotas. And sometimes the reps don\u2019t know their quotas until late in Q1. Additionally, I ran into clinics who put relationships over patient care/medical advances. I called on DVMs who were so in love with a competing rep that they didn\u2019t care what I brought to the table, even if it would improve patient outcomes or clinic efficiency. Those were some of my most frustrating clients. \n\nMost of the reps I\u2019ve worked with have been very personable, intelligent, and hard working. They all do their best to communicate the value of their portfolio without wasting the clinics time. We all know how hard it is to get the staff together! But sometimes they are limited on what information can be shared. Reps have to stay on-label which can be frustrating.\n\nFeel free to reach out with questions! I\u2019ve been in the industry for more than a decade."
      },
      {
        "id": "o7znzts",
        "score": 2,
        "body": "Not every doctor, or tech keeps up with the latest literature on treatments, so having someone whose aim is to showcase new products and facilitate that process, doesn't seem like a bad thing."
      },
      {
        "id": "o7zevr6",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7ztjle",
        "score": 1,
        "body": "Trust me, the pay and lifestyle is better.\n\nI sell products I believe in and don\u2019t waste time with people who are unkind.\n"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rh85ro",
    "title": "Oddly shaped rods?",
    "body": "From an ear cytology to of a 2yo mixed GSD, just curious if anyone knows why it had such odd shaping?",
    "flair": "Interesting Case",
    "score": 74,
    "comment_count": 9,
    "created_at": "2026-02-28T17:16:18+00:00",
    "top_comments": [
      {
        "id": "o7y00dt",
        "score": 40,
        "body": "I just showed your photos to a friend of mine who is a veterinary pathologist\u2026. she essentially said it\u2019s nbd & sometimes bacteria form clusters (but in doctor-y language lmao) \ud83e\udd37\ud83c\udffb\u200d\u2640\ufe0f\n\nDoesn\u2019t help much with your question, but wanted to let you know I tried! Hahaha."
      },
      {
        "id": "o7wxsg4",
        "score": 24,
        "body": "Looks like Bacilli. Also commenting to follow along."
      },
      {
        "id": "o7zshqe",
        "score": 9,
        "body": "I'm embarrased to say I thought this was a tarantula on the moon. I need to go to bed \ud83e\udd23"
      },
      {
        "id": "o7xtp2n",
        "score": 8,
        "body": "Bacilli are rods."
      },
      {
        "id": "o7ynh6g",
        "score": 7,
        "body": "Just looks like clusters of chains"
      },
      {
        "id": "o7z0s97",
        "score": 4,
        "body": "Looks a bit like the palisade arrangement that bacilli can take on."
      },
      {
        "id": "o7wqf7k",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o82r0e7",
        "score": 1,
        "body": "Heheh it looks like a sea anemone..."
      },
      {
        "id": "o85nios",
        "score": 1,
        "body": "I could definitely be wrong but it looks like LONG chains of cocci to me. Too large to be rods."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rh6f3s",
    "title": "Texts on exotic care",
    "body": "Flagged as school bc it\u2019s a learning based question, but I am already an LVT. I just want to improve my knowledge base!\n\nI don\u2019t work with exotics as much as I used to since leaving a toxic clinic a couple years ago, but I own rabbits and a lizard and I just want to feel as prepared as possible for potential nursing care. One of my rabbits recently had a LECR done and it\u2019s making me hyper aware of my own skill levels. I\u2019m def overthinking things, he\u2019s doing great, but I would love to have some texts on hand to refer to for my own comfort \ud83d\ude05 if anyone has any suggestions for texts or resources, I would greatly appreciate it!",
    "flair": "School",
    "score": 8,
    "comment_count": 6,
    "created_at": "2026-02-28T16:07:34+00:00",
    "top_comments": [
      {
        "id": "o7wsltu",
        "score": 4,
        "body": "Thank you! \ud83d\ude0a"
      },
      {
        "id": "o7wnyf0",
        "score": 3,
        "body": "Here you go: \nhttps://www.wiley.com/en-us/Exotic+Animal+Medicine+for+the+Veterinary+Technician%2C+4th+Edition-p-9781119863144"
      },
      {
        "id": "o7y4ff4",
        "score": 3,
        "body": "Lafeber vet website free resources. Theres many conferences like Exotics365 and AAV later this year. Theres mammal, reptile and avian associations that put on online CE classes though out the year. Vet girl had a exotic animal certification"
      },
      {
        "id": "o7wcl78",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7wt3hd",
        "score": 1,
        "body": "You're most welcome."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rgruoq",
    "title": "flea bites in wildlife vet med \ud83d\ude2d",
    "body": "Sounds like such a gross question to have to ask buuuutttt \u2026I work DAILY with flea ridden species and I come home with bites on my tummy and my shoulders. I used to get them on my ankles but started wearing longer socks. Does anyone else work in wildlife or somewhere with lots of flea presence and have any tips to avoid bites?? I think I\u2019m even allergic to the bites and it\u2019s bothering me so bad \ud83d\ude2d",
    "flair": "Work Advice",
    "score": 14,
    "comment_count": 7,
    "created_at": "2026-02-28T03:26:59+00:00",
    "top_comments": [
      {
        "id": "o7tpw37",
        "score": 7,
        "body": "Basically what you do for mosquito and tick prevention long sleeves long pants and long socks tucked into one another. Also immediately treating patients for fleas so they don't infest the building. Bug spray may work but probably not"
      },
      {
        "id": "o7tppjm",
        "score": 6,
        "body": "Apparently OFF brand (deep woods) is made to repel fleas and ticks on top of mosquitoes."
      },
      {
        "id": "o7tr9mn",
        "score": 3,
        "body": "Avon Skin So Soft is a great flea repellent"
      },
      {
        "id": "o7u44je",
        "score": 3,
        "body": "we\u2019d use adams flea and tick spray bc thats what we\u2019d use for the animals \ud83d\ude2c"
      },
      {
        "id": "o7tmjcz",
        "score": 2,
        "body": "I wonder if mosquito repellent would work?"
      },
      {
        "id": "o7xam94",
        "score": 2,
        "body": "I've treated my clothes with permethrin with good results"
      },
      {
        "id": "o7tj56q",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rgm6fd",
    "title": "I need advice",
    "body": "So, I started at my job 2 years ago this month. Recently, I was given the role of taking over the social media. This entails posting promotions, making/creating stuff to post, etc.\n\nI was told at the time, doing so would reflect in my raise.\n\nWe recently were given our yearly raises and it did not reflect in my raise. I got a .50 raise. I\u2019m so pissed off because not only do I have an extra workload, but I have also taken on many more roles at work. I have more responsibilities.\n\nWhat should I do? Do you think a 50 cent raise is reasonable or should I ask for more?\n\nAlso to add, I\u2019ve never been put in a situation to ask for a raise or talk about it, so it makes me more nervous.",
    "flair": "Work Advice",
    "score": 3,
    "comment_count": 10,
    "created_at": "2026-02-27T23:14:20+00:00",
    "top_comments": [
      {
        "id": "o7sgu85",
        "score": 20,
        "body": "Tbh anything under a dollar in this economy is insulting. There\u2019s barely a difference in your paycheck at the end."
      },
      {
        "id": "o7sfj1s",
        "score": 7,
        "body": "Was anything mentioned during your review? I would certainly speak with your manager about your additional responsibilities and ask for some additional compensation. Worst they'll do is say no"
      },
      {
        "id": "o7srgt3",
        "score": 5,
        "body": "I was given a $2 raise when moved to inventory manager. I\u2019ve asked for another $1 in the 6 months I\u2019ve had this position and will get it added to my payroll next cycle. Always ask, the worst is they say no and you should find a better paying job if they don\u2019t budge. (For reference, I work by the Twin Cities making $22.50 as a vet assistant/inventory manager)"
      },
      {
        "id": "o7sey41",
        "score": 4,
        "body": "What were you making before? Having that information would help"
      },
      {
        "id": "o7sf4en",
        "score": 3,
        "body": "15.50, I was bumped to 16. \nMy co worker got a .71 raise, which granted, yes she\u2019s been there longer, but considering she hadn\u2019t taken on any new roles, why was i compensated the same percentage as she was?"
      },
      {
        "id": "o7sfotn",
        "score": 3,
        "body": "We don\u2019t really do reviews, our clinic isn\u2019t very traditional like that. We kinda just get raises every year. I\u2019m just so nervous to even ask about it"
      },
      {
        "id": "o7vvkc9",
        "score": 2,
        "body": "You should ask and be honest. Say that you are happy to be given the opportunity and are enjoying the new position. Tell them how many hours a week you work on social media and that you don\u2019t feel a $0.50 raise reflects the additional time spent.\n\nHonestly, I\u2019m kind of ballsy and would even ask for milestone bonuses, like $100 for hitting 1k followers. $400 for 100 new clients that came from social media, etc."
      },
      {
        "id": "o7wgccj",
        "score": 2,
        "body": "Ask and maybe see if there are better offers out there.\u00a0 You don't have to take a new job, but you can use their offer to renegotiate your current pay."
      },
      {
        "id": "o7sdlv2",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7wixkh",
        "score": 1,
        "body": "This! I was on indeed looking at what other clinics were offering to see what I should ask for raise-wise. My manager saw my resume on there and got scared I was going to quit and gave me a dollar raise on the spot"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rgl3p6",
    "title": "We had a doozy of a dental today.",
    "body": "Incisors literally just saying 'aight, imma head out'. ",
    "flair": "Gross \ud83e\udd22",
    "score": 169,
    "comment_count": 36,
    "created_at": "2026-02-27T22:30:58+00:00",
    "top_comments": [
      {
        "id": "o7s6ata",
        "score": 52,
        "body": "Good gravy, I can smell it just by looking at your X-rays! \ud83e\udd22\ud83e\udd2e"
      },
      {
        "id": "o7s6gsp",
        "score": 48,
        "body": "See now, this is why as a technician, I absolutely refuse to do extractions. Like sure, I could probably grab those incisors with my gloved fingers and remove them, but with all that bone loss, there's a decent chance that bad things are gonna happen and there's going to be some kind of iatrogenic fracture *and I want nothing to do with it.*  \n  \nI don't play much in GP anyway, but I've had a couple GP doctors offer to teach me and I am not interested in adding this to my list of skills. Straight scares me."
      },
      {
        "id": "o7s6gbs",
        "score": 44,
        "body": "And I know you're thinking of the right smell. The whole room started out with rank sour breath smell, ended in coppery blood smell."
      },
      {
        "id": "o7s7b6y",
        "score": 25,
        "body": "Yea, I think the doc was honestly surprised that she didn't fracture anything. Especially with that 09"
      },
      {
        "id": "o7sb2tk",
        "score": 19,
        "body": "those incisors are crazy lmao they\u2019re hanging on by a hope and a prayer but the bone loss is even crazier! \ud83d\ude31"
      },
      {
        "id": "o7sr9ur",
        "score": 14,
        "body": "The Colleges make recommendations, not laws, so it\u2019s not illegal. It is currently legal is my state for techs to do extractions, but that doesn\u2019t mean it\u2019s smart!"
      },
      {
        "id": "o7seno5",
        "score": 13,
        "body": "I feel that - 4y F/S cat had just awful teeth. \n\nShe already had some missing, don\u2019t know why.  8 simple extractions (just plucked out) 2 carnassial, her 3 canines (kept 104), and the rest were premolars. X-rays were horrific. Also kept her incisors, what she had left anyway. \n\nO was like how does this happen? She\u2019s 4, had since she was a kitten \n\nI\u2019m just like sometimes the body doesn\u2019t like its own teeth. \ud83e\udd37\u200d\u2640\ufe0f"
      },
      {
        "id": "o7smde2",
        "score": 7,
        "body": "Oof poor cat. Sometimes the genetics are just garbage, too. One of my cats, who I found as an approx 6 weeks old feral kitten, had all but her incisors and 3 canines pulled at 3 1/2 years old. No stomatitis or FORL, just wicked bone loss. My other 5 have had various teeth pulled over the years but not the extensiveness she did."
      },
      {
        "id": "o7sqppi",
        "score": 6,
        "body": "https://preview.redd.it/lb0a10adr4mg1.jpeg?width=1080&format=pjpg&auto=webp&s=5ca5ebd193bca570349be7c55fc1f56c5f79d2b1"
      },
      {
        "id": "o7tbo76",
        "score": 5,
        "body": "Guidelines\u2260legal"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rgimpi",
    "title": "First time I tested my own pets samples to learn and found roundworms",
    "body": "first time doing a fecal sample and they used my stray wormy boy I kidnapped from the woods' poop as an example",
    "flair": "Microscopy",
    "score": 77,
    "comment_count": 9,
    "created_at": "2026-02-27T20:55:39+00:00",
    "top_comments": [
      {
        "id": "o7s3hun",
        "score": 40,
        "body": "Look like air bubbles to me! But hard to tell because it's blurry and can't tell size. What power were you viewing it at?"
      },
      {
        "id": "o7udcca",
        "score": 15,
        "body": "I'd check them out under 40x to be sure, this is one from a pre-made slide in class\n\nhttps://preview.redd.it/lyr0ac3gs6mg1.jpeg?width=3024&format=pjpg&auto=webp&s=5b6c58e8ed14dc2c7d5999423d0cce7fd104083e"
      },
      {
        "id": "o7t9r33",
        "score": 14,
        "body": "If you have an iPhone put it in portrait mode, then put one camera lens up to the viewing area and snap a photo at zero zoom. Once you have the photo you can crop it if you want."
      },
      {
        "id": "o7t9kfa",
        "score": 14,
        "body": "Most worms from fecal are visible at 10x, since you are collecting onto a cover slide. No need for high view or oil."
      },
      {
        "id": "o7s9o2a",
        "score": 9,
        "body": "10x\n\nSorry it's blurry it's so hard to focus a camera on microscopes lol"
      },
      {
        "id": "o7sq72j",
        "score": 8,
        "body": "I\u2019d always view endoparasites on 100x oil immersion personally especially if looking at ova"
      },
      {
        "id": "o7t2aft",
        "score": 7,
        "body": "they definitely don\u2019t look like air bubbles to me, i see roundworms as well"
      },
      {
        "id": "o804wt8",
        "score": 3,
        "body": "https://preview.redd.it/f3dwjd2n7dmg1.jpeg?width=3024&format=pjpg&auto=webp&s=113b14fbf46fb46cd5f71b063472f7fbd7065f4d\n\nI saw some the just other day!!"
      },
      {
        "id": "o7rmy8d",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rgeqvu",
    "title": "Trazodone back order",
    "body": "Any idea when it\u2019s coming off back order?  What are you guys using instead?",
    "flair": "Discussion",
    "score": 6,
    "comment_count": 9,
    "created_at": "2026-02-27T18:29:51+00:00",
    "top_comments": [
      {
        "id": "o7qy0eq",
        "score": 6,
        "body": "Trazodone is available from most distributors."
      },
      {
        "id": "o7r08bw",
        "score": 3,
        "body": "I\u2019m looking on Vetcove and see both the 50\u2019s and 100\u2019s available in both 100 and 1000 count?!"
      },
      {
        "id": "o7rf380",
        "score": 3,
        "body": "I do! But I only order surgical stuff- I texted my courtier who is in charge of pharmacy inventory."
      },
      {
        "id": "o7qy3bk",
        "score": 2,
        "body": "Can\u2019t get it from Patterson or MWI"
      },
      {
        "id": "o7resri",
        "score": 2,
        "body": "Patterson does have it and it came up for me as available through MWI as well. Do you place orders through Vetcove?"
      },
      {
        "id": "o7qtceo",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7s4mxd",
        "score": 1,
        "body": "We haven't had any issues getting traz recently. That's unfortunate!! At least it's an easy med for clients to get from a human pharmacy, I guess"
      },
      {
        "id": "o7wdks3",
        "score": 1,
        "body": "Totally available here. From 3 different suppliers. But if you really can't get it there's always acepromazine, gabapentin or Silio?"
      },
      {
        "id": "o7r0cmw",
        "score": 1,
        "body": "Thank you!"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rgbu9z",
    "title": "Any small lab alternatives to IDEXX/Antech for fecal send-outs?",
    "body": "I'm curious about what the landscape actually looks like beyond the big two. I know IDEXX and Antech dominate, but I imagine some independent clinics use smaller or regional labs for parasitology and fecal PCR work. Or does basically everyone end up going through IDEXX/Antech duopoly?\n\n(Context: Not a vet, but I was thinking of setting up a \"buying club\" of dog owners who want regular test results, akin to function health etc., but seems like it's impossible to find a lab partner)",
    "flair": "Work Advice",
    "score": 2,
    "comment_count": 10,
    "created_at": "2026-02-27T16:46:23+00:00",
    "top_comments": [
      {
        "id": "o7q80sl",
        "score": 2,
        "body": "There's healthgene as well, or AHL in Guelph, ON if you live in Canada."
      },
      {
        "id": "o7qkz5f",
        "score": 2,
        "body": "We use Moichor predominantly for exotics, but they do offer cat/dog panels."
      },
      {
        "id": "o7qlct6",
        "score": 2,
        "body": "You could likely use a university diagnostic lab, you could call a few to see what they offer. At least our university veterinary medicine diagnostic lab allows this. Clients frequently drop off their own animals for necropsy but I haven't really looked into what other testing can be done. I doubt they do bloodwork panels but PCR and Baermann's go to the diagnostic lab."
      },
      {
        "id": "o7q7fqx",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7qlmye",
        "score": 1,
        "body": "WADDL, Pathogenes, Cornell"
      },
      {
        "id": "o7tnmx4",
        "score": 1,
        "body": "We tried Ellie at the birth of their company. We ended up going back to Antech because we needed a more established company at the time. But Ellie seems to be doing well and continuing to grow. So they might be what you\u2019re looking for."
      },
      {
        "id": "o7vblzo",
        "score": 1,
        "body": "I work close to a big veterinary teaching university/hospital and they have a reference lab. We usually send to idexx over them anyway though"
      },
      {
        "id": "o8cutnx",
        "score": 1,
        "body": "Thanks everyone - good leads!"
      },
      {
        "id": "o7qcddp",
        "score": 1,
        "body": "I\u2019ve only ever used AHL for necropsy. Do they do basic regular health testing as well?"
      },
      {
        "id": "o7rfy1o",
        "score": 1,
        "body": "They do, it's just slow."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rga73d",
    "title": "LPT: Estimates",
    "body": "PLEASE provide staff with updated estimates and do not rush through them!\n\nI had to present a client MULTIPLE estimates yesterday. They were, understandably, frustrated throughout the entire process. \n\nI don't mind presenting a client with a treatment plan, but if I've already collected a deposit, please keep me in the loop of which is the most current/final estimate. Clients need to know what funds they're working with, before proceeding with treatments, procedures, and diagnostics.\n\nI had to put my foot down yesterday, because it kept being updated, with me being pressured to get payment. I can't effectively do that without presenting a more definitive range. \n\nThere's a difference between an estimate that begins at $800-1200, and one that ends up ranging from $1800-2700!",
    "flair": "Vent",
    "score": 11,
    "comment_count": 1,
    "created_at": "2026-02-27T15:46:45+00:00",
    "top_comments": [
      {
        "id": "o7putnr",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rg80s4",
    "title": "Scrubs or business casual for job interviews?",
    "body": "What do yall wear? I was taught either are typically fine so long as they\u2019re clean and professional looking. I have some interviews lined up and unsure which to wear \ud83e\udd70",
    "flair": "Work Advice",
    "score": 15,
    "comment_count": 31,
    "created_at": "2026-02-27T14:23:15+00:00",
    "top_comments": [
      {
        "id": "o7pfwgl",
        "score": 40,
        "body": "Don't go to the initial interview in scrubs. To make a good first impression you should wear attire that is appropriate for a formal interview. Remember - you can't go wrong wearing nice clothes, but you can go wrong wearing scrubs."
      },
      {
        "id": "o7qo8wo",
        "score": 24,
        "body": "I always keep a set of scrubs in the car for interviews just in case they want me to do some work."
      },
      {
        "id": "o7sr4w0",
        "score": 16,
        "body": "Business casual. Never scrubs, shows no effort"
      },
      {
        "id": "o7us659",
        "score": 13,
        "body": "If they want you to switch to a working interview then you can change into scrubs"
      },
      {
        "id": "o7pgugw",
        "score": 10,
        "body": "I\u2019ve worn scrubs for every job interview"
      },
      {
        "id": "o80q84u",
        "score": 9,
        "body": "I'm shocked by the replies, I'm my country there is no way you had to do ANY work at the interview, if someone asked for that they would get laughed at for being ridiculous.\nAlso if you showed in scrubs that would be VERY awkward"
      },
      {
        "id": "o7r5xb6",
        "score": 8,
        "body": "Business casual\n\nBring scrubs in case of an impromptu working interview (though I find any clinics doing those without previous discussion unprofessional)."
      },
      {
        "id": "o7pmu3g",
        "score": 6,
        "body": "Depends on the nature of the interview, but always best to ask.\n\nBusiness casual by default."
      },
      {
        "id": "o7rnyec",
        "score": 6,
        "body": "I'm shocked at the comments. I've never not worn scrubs for an interview. I've gotten an offer at every clinic I've ever interviewed with."
      },
      {
        "id": "o7qf7f7",
        "score": 4,
        "body": "Business casual for formal interview, scrubs for working interview."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rg4nlg",
    "title": "Does Anyone Else Here Have Cubital Tunnel Syndrome From Restraining Dogs For Decades?",
    "body": "How do you keep working without making it worse? I\u2019m thinking it\u2019s not really going to be possible for me much longer and I\u2019ll either end up on workers comp or I\u2019ll have to figure out what kind of new job I can get that doesn\u2019t put so much physical strain on my 46 year old wrecked elbows. I don\u2019t really do anesthesia unless we\u2019re short handed or if someone is out on vacation because I hate it. So  generally keep to doing rooms/appointments because that\u2019s just my thing and always has been. \n\nI actually like working with people and clients which is somewhat rare and therefore (according to me) valuable. I even like working with difficult clients because I get a sense of satisfaction from smoothing things over with the crazies. Id actually be happy to work at the front desk but those people get paid next to nothing so that\u2019s not really a feasible option. I\u2019m at a loss on how to deal with this situation and it\u2019s getting worse pretty quickly.",
    "flair": "Work Advice",
    "score": 16,
    "comment_count": 13,
    "created_at": "2026-02-27T11:52:40+00:00",
    "top_comments": [
      {
        "id": "o7orw8e",
        "score": 17,
        "body": "Being a tech is a very physical job.   I\u2019ve been doing it for 20 years,  now I\u2019m transitioning into a remote role focused on customer support in a clinic.  Look into those companies that offer those roles .  Like NVA, Chewy ,"
      },
      {
        "id": "o7pkbe8",
        "score": 5,
        "body": "I'm only 28 and my doctor says I have early arthritis starting in my hands ): I'm not sure how to to slow the progress and my Dr didn't offer any solutions. I guess I plan on just working until my body gives out and I can't do it anymore."
      },
      {
        "id": "o7pkk6b",
        "score": 5,
        "body": "I guess I should look into those. I\u2019ve never done anything other than this and some light waitressing as a teen. I worry about not really having any marketable skills outside of this particular job."
      },
      {
        "id": "o7ov83d",
        "score": 3,
        "body": "If I were moved from my position to front desk I would not get a pay cut - would your clinic cut your pay?"
      },
      {
        "id": "o7qov2t",
        "score": 3,
        "body": "I'm currently in a thumb brace on my dominant hand from repetitive use injury. Phone and hobbies didn't help, but I think it was really from how many syringes I had to pull on. Do you have a pt? I go to them with a problem with my body and they've always been able to help.\u00a0"
      },
      {
        "id": "o7ovao7",
        "score": 3,
        "body": "I should\u2019ve said *over a physical condition because that\u2019s the only way to get me to front desk \ud83e\udd23"
      },
      {
        "id": "o7rc082",
        "score": 2,
        "body": "No they need more help up front?"
      },
      {
        "id": "o7prshf",
        "score": 2,
        "body": "Same,  only been a vet tech.  No experience in anything else.    There out there , just gotta look.   Some jobs do require certification"
      },
      {
        "id": "o7opx1o",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7smz6q",
        "score": 1,
        "body": "I\u2019ve only been a vet tech for 24 years. . My back went out prior to the elbows but they are both an issue. I work remote now and I don\u2019t think I can go back to clinic work due to pain."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rfyk03",
    "title": "Mechanical dead space question",
    "body": "Hi yalllll, I\u2019ve been a VA for 6 years or so and have learned everything on the job so I have decent gaps in my knowledge. I\u2019ve been going to Penn foster online for RVT program. I\u2019ve recently learned about mechanical dead space and its affect on anesthesia parameters. Today I was monitoring for a TPLO, it was a large German shepherd intubated with a 12 ET tube. Our 12 tube is very very long. She did not breathe on her own throughout the entire procedure and when I gave manual breaths her ETC02 and ITC02 readings were the same . Ex etco2 and inco2 both 42. Her spo2 remained 98 throughout the procedure. Are these capnograph readings due to mechanical dead space as the tube extended maybe an inch from her nose? ",
    "flair": "Work Advice",
    "score": 7,
    "comment_count": 9,
    "created_at": "2026-02-27T05:56:04+00:00",
    "top_comments": [
      {
        "id": "o7nn0ur",
        "score": 16,
        "body": "An inch of dead space is not going to cause an iCO2 of 42. Either something is wrong with your circuit or your monitor."
      },
      {
        "id": "o7z94dy",
        "score": 4,
        "body": "Look at your machine and follow the path oxygen is flowing. Could be an issue with the one way valves getting stuck resulting in exhaled gas to be going back. Also make sure sodasorb is not exhausted. Also could be a good reason to get that machine serviced."
      },
      {
        "id": "o7u5thp",
        "score": 3,
        "body": "Bag definitely too big, but that shouldn\u2019t cause the problem. \n\nI\u2019m wondering if the 02 level was low enough that it wasn\u2019t refilling the circuit, and what you were bagging was just what she had just exhaled."
      },
      {
        "id": "o7quosz",
        "score": 2,
        "body": "She was 88lbs and had a 4liter bag maybe the bag was too big?"
      },
      {
        "id": "o80srya",
        "score": 2,
        "body": "What\u2019s your calculation for the bag?"
      },
      {
        "id": "o80v9s7",
        "score": 2,
        "body": "Gotcha.  I go kgs x 90 and round up so 4L seemed fine to me."
      },
      {
        "id": "o7nloz9",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7quidb",
        "score": 1,
        "body": "If a pet breathes on their own it will give normal readings but I find whenever I give manual breaths it always does this. So it could be an issue with the capnometer ?\nMy clinic management is so aggressively anti capnometer because they\u2019re expensive I feel like they won\u2019t want to repair it"
      },
      {
        "id": "o80tsvm",
        "score": 1,
        "body": "Kgx60ml, round up."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rfs58s",
    "title": "1.54lb fatty mass off pug",
    "body": "",
    "flair": "Gore Warning \u203c\ufe0f",
    "score": 23,
    "comment_count": 0,
    "created_at": "2026-02-27T00:51:29+00:00",
    "top_comments": []
  },
  {
    "subreddit": "VetTech",
    "id": "1rfm4eb",
    "title": "Aspirating after giving the injection? And not before?",
    "body": "",
    "flair": "Discussion",
    "score": 9,
    "comment_count": 23,
    "created_at": "2026-02-26T20:55:12+00:00",
    "top_comments": [
      {
        "id": "o7kzr60",
        "score": 29,
        "body": "There\u2019s just so much I don\u2019t like about this video \u2026"
      },
      {
        "id": "o7l12nj",
        "score": 18,
        "body": "Injecting between the shoulder blades in a cat\u2026 not aspirating before injecting\u2026 not proper restraint\u2026 i agree i do not like this video at all."
      },
      {
        "id": "o7l1zdg",
        "score": 16,
        "body": "I dont think they did a single thing correctly."
      },
      {
        "id": "o7l2mgg",
        "score": 12,
        "body": "Any injection given on a cat should be an area that's easy to cleanly amputate with good margins in the case of feline injection site sarcoma."
      },
      {
        "id": "o7kzysn",
        "score": 11,
        "body": "And injecting right between the shoulder blades... "
      },
      {
        "id": "o7l5ql4",
        "score": 7,
        "body": "Injection site carcinomas are at a higher rate in cats than other common veterinary species. If you cause one to grow between the shoulder blades, it can easily become impossible to excise without severing the spinal cord or a wide array of muscles and other tissue."
      },
      {
        "id": "o7l24tj",
        "score": 6,
        "body": "Wait. I\u2019ve been a tech for 18 years now. Not once have I heard to not I heavy between shoulder blades. Can someone educate me."
      },
      {
        "id": "o7l4sfe",
        "score": 6,
        "body": "cats are prone to injection site sarcomas. vaccines (and other injections if possible) should be given as low in the leg or on the tail as you can, so they can be amputated if the cat develops a sarcoma."
      },
      {
        "id": "o7l2fyb",
        "score": 5,
        "body": "Yea what? We always do SQ injections in the scruff"
      },
      {
        "id": "o7l5c3g",
        "score": 5,
        "body": "I've heard that it can be for any injection, but either way I'd personally prefer not risking it."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rfbh9t",
    "title": "Ever roll your eyes in your mind when a client says...",
    "body": "Oh, nobody told me to hold off food and water before the surgery.\n\nI paid a lot of money for this dog, why is he having these issues?\n\nShe's a rescue, he's affraid of men.\n\nWell, my Facebook group says I should use essential oils for (fill in blank)\n\nThe list goes on and on.....\n\n",
    "flair": "Vent",
    "score": 160,
    "comment_count": 67,
    "created_at": "2026-02-26T14:23:49+00:00",
    "top_comments": [
      {
        "id": "o7itb53",
        "score": 160,
        "body": "\"You must hate animals since you won't squeeze me in at 5:59 for the rabies vaccine I forgot my pet needed for boarding tomorrow.\""
      },
      {
        "id": "o7irpa2",
        "score": 118,
        "body": "\"I don't need flea/tick/heartworm protection, I have an *inside* dog.\""
      },
      {
        "id": "o7it4dh",
        "score": 113,
        "body": "A lot of animals do be hating men though"
      },
      {
        "id": "o7j89yi",
        "score": 79,
        "body": "Or even better, I don't use preventions because I live in a gated community. MA'AM, WE LIVE IN THE DARKEST RED OF THE HEARTWORM PREVALENCE MAP! YES YOUR PET NEEDS IT, YEAR ROUND!"
      },
      {
        "id": "o7iwam1",
        "score": 76,
        "body": "She doesn't really go outside, just to the dog park.\n\nI've had dogs my whole life, dogs never used to get these problems, so why is this happening and is it really a big deal\n\nIn my home country in South America, Asia, or Russia dogs don't get allergies or sick, they're all healthy even with no care, so why is this happening and is it really a big deal\n\n\nThat costs more than my own healthcare\n\nYes I intend to breed them. Yes I would have sex with my own sister\n\nI thought the booster vaccine/recheck exam/recheck diagnostics price were included in the original visit and didn't know I would have to pay anything today \n\n\nI could probably think of more..."
      },
      {
        "id": "o7iy763",
        "score": 73,
        "body": "Yeah that\u2019s the only on where I disagree because my clinic has at least 3 dogs we see on a regular basis that if a male tech/Dr walk in they\u2019re immediately F NO- don\u2019t touch me attitude, but completely lovable and friendly with the female staff."
      },
      {
        "id": "o7j4302",
        "score": 60,
        "body": "one that I really struggle to not roll my eyes to is \n\n\u201cHoney, I\u2019ve owned/ bred dogs for over 10years, I know a thing a or two about dogs\u201d \n\nupon me telling them literally anything because 100% of the time it turns out, they do not know \u201ca thing or two\u201d about the proper medical of dogs and they\u2019re also unwilling to learn and do better."
      },
      {
        "id": "o7iq6dr",
        "score": 44,
        "body": "We were a female only clinic until last summer and the number of dogs that look at our man tech and scream \"why would a man be there????????\" is really funny. I've had him come back to treatment carrying little dogs that have a paw on his chest and are leaning as far away from him as they possibly can \ud83d\ude02 little do they know, he has a 4lb little dog at home"
      },
      {
        "id": "o7jd9aq",
        "score": 42,
        "body": "My own dog doesn\u2019t like being in clinic in general but will allow physical exams / vaccines / jug blood draws and even X-rays (as long as I\u2019m restraining his head) performed by women, but he absolutely will not tolerate any man coming near him. And oop, yep, he is in fact a rescue.\n\nI\u2019m surprised anyone in this field would think this is sus / bullshit. It\u2019s extremely common."
      },
      {
        "id": "o7jt18g",
        "score": 42,
        "body": "Once had a sweet old couple bring in their dog for a distended abdomen. During triage I asked if they have other dogs in the household and how they're doing (that's part of my normal questioning). They said they have a male dog at home and he's fine. I see the dog they brought in is an intact 2 yr old female. I ask if the male is intact as well. He was. I asked if they ever witnessed them mating, and they said \"Yes but she can't be pregnant bc the male is only 10 months old, he's still a baby\".\n\n\ud83d\ude43\ud83d\ude43\ud83d\ude43\n\nSooo the dog was pregnant with 7 puppies. The couple was astounded, but all in for learning about how to help their dog welp. We gave them a bunch of info.\n\nThe dog gave birth to the puppies 2 hours after they got home \ud83d\ude02"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rf0rry",
    "title": "Neurodivergent Tech Support Group?",
    "body": "Would anyone be interested in forming a neurodivergent support group for techs/assistants? Let\u2019s just say today was a really hard day. I\u2019m AuDHD  (amongst other things) and I do my best to work with it/around it but communication is always my worst downfall. Masking is exhausting but I do my best. But it feels like whenever I don\u2019t have the energy to keep it up and accidentally phrase something wrong or am too blunt there isn\u2019t any compassion or understanding at all from some people. I know it can be hard to understand especially when something comes off offensive. I got absolutely torn apart today (not even by the person involved or management )and it just makes me feel like no matter how hard I try to improve my regulation/communication or how great of a technician I am it doesn\u2019t matter. Even if it\u2019s just on this thread I think it would help to not feel so alone .",
    "flair": "Vent",
    "score": 16,
    "comment_count": 8,
    "created_at": "2026-02-26T04:40:52+00:00",
    "top_comments": [
      {
        "id": "o7gs5lu",
        "score": 4,
        "body": "I'd love to! Like a Discord maybe?"
      },
      {
        "id": "o7js6yd",
        "score": 3,
        "body": "I'd love this. I'm also AuDHD and communication is by *far* my biggest issue at work."
      },
      {
        "id": "o7gyfyt",
        "score": 3,
        "body": "Hey, I have ADHD and I know how exhausting it can be in all aspects of life. You're not alone. You're welcome to send me a message to vent if you'd like or you can reply here too, either way you feel comfortable.\u00a0\n\n\nI am heading to bed right now but I promise I'll reply in the morning, you have my word.\u00a0"
      },
      {
        "id": "o7l2qpj",
        "score": 2,
        "body": "Love this idea. Most of my coworkers are on the spectrum in some way so we all vibe and check each others tone. You need some others like you to keep you accountable but be understanding at the same time \ud83d\udc95"
      },
      {
        "id": "o7ndlsq",
        "score": 2,
        "body": "Absolutely. I feel like I clock into work and have to cosplay a neurotypical person. As someone who is heavily neurodivergent this field can really be tough. My ADHD especially has really made navigating vet med very hard.\n\nIf anyone makes a group, I\u2019d love to join"
      },
      {
        "id": "o7qw38b",
        "score": 2,
        "body": "I would genuinely love this, some days are more difficult than others and having a group for support sounds amazing."
      },
      {
        "id": "o7z9jnw",
        "score": 2,
        "body": "Yes please!"
      },
      {
        "id": "o7glvqb",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rez0tm",
    "title": "Deciding on euthanasia sucks",
    "body": "I have a little dog that will be 15 next week. Overall she's \"healthy\" and doesn't have any major diseases. She cannot see anymore and losing her vision a couple of years ago was difficult for her. I think the vision loss seems to have kind of gone hand and hand with some cognitive decline. She seems to hear for the most part, but only recognizes her name. If she's in the yard, we can call her and she will perk her head up but be unable to find her way to us. \n\nShe has a heart murmur, but no symptoms of heart disease. She has some arthritis but does ok with Carprofen and Gabapentin. She went thru a period where she was sun downing badly, but I did a couple of months with Trazodone at night and have been able to discontinue that. She has a great appetite and enjoys eating from slow feeder bowls, snuffle mats, and sometimes a light Kong toy. \n\nMost of the day she sleeps. We've made her a little play pen area with a potty mat and her bed and bowls and that's where she spends most of her time. It's her safe space away from the other animals and she feels less anxious because all of the things she wants in life are right there and easy for her to find. She likes to walk around the yard and potty, but will get confused and cannot find her way to the backdoor most of the time now. She seems anxious outside of her pen inside and paces A LOT. Unfortunately, I think she's mostly at the point where she is simply existing, which is what makes me think of QOL.\n\nI've done so many QOL assessments and do them on a regular basis and she always comes out in the middle. I keep thinking that maybe we need to let her go before her QOL slips away too much. Ive been in vetmed for many years, I know the saying \"better a day early than a day late\", but its still so hard. All of my other animals I've known when it was time. This one is so much harder because she's definitely at a point where euthanasia wouldn't be wrong, especially if we want to make sure she goes on a good day. But how tf does anyone just pick a day? How do you keep on going each day leading up to it knowing that on X day your dog is going to die? The anticipatory grief is something awful. I also feel like this is a little more complicated for me because I've never bonded with this dog... she has always been my husband's girl and now my son is attached. It makes me feel guilty because for my own pets that I was super bonded with, I possibly waited too late for them. But with this dog, because I have enough detachment to say \"hey let's not wait too long\" it also makes me feel like a villain who is cutting her time short. ",
    "flair": "Sad",
    "score": 24,
    "comment_count": 6,
    "created_at": "2026-02-26T03:17:07+00:00",
    "top_comments": [
      {
        "id": "o7gdl2o",
        "score": 11,
        "body": "With your last note about your husband and son being the ones most bonded, it may be best to just let them decide. There\u2019s never a \u201cgood\u201d day, but 1 benefit of scheduling in advance, your husband and son can make sure to spend as much time as possible together beforehand (as much time as needed or within reason): make a bucket list of favorite things and maybe schedule when everyone can be there if they want to be there to say their final goodbyes. \n\nThat\u2019s just my opinion though and how I would approach if I were in your scenario."
      },
      {
        "id": "o7g984a",
        "score": 8,
        "body": "It sucks every single time\u2026\ud83e\udef6\ud83c\udffb"
      },
      {
        "id": "o7gd3j6",
        "score": 3,
        "body": "It's such a hard spot to be in. I dont have any words of wisdom, I just really feel for you and i wish you all the best. It sounds like the decision will come to you when it's meant to"
      },
      {
        "id": "o7gkrw3",
        "score": 3,
        "body": "With quality of life hanging somewhere in the middle I definitely (personally) think that it 's time to pick a day. Choose a day where your husband does not have to go to work the next day and your child can be out of any of their academic obligations (or work obligations depending on how old he is).\n\nHave an open an honest conversation with your child, and see how they would like to memorialize the pet (senior citizen photos, paw prints, hair clippings, clay prints, etc).\n\nDefinitely give them autonomy concerning this choice, especially because they are more bonded to the pet. However, I would definitely make sure they both understand professionally where you stand concerning euthanasia decisions. Maybe even bring up in conversation with your husband that waiting too long could cause the family to have a traumatic euthanasia experience ( dog has such low quality of life that euthanasia becomes an emergency).\n\nThe day you do it make sure everything is planned out, including the meal your family is going to eat that evening. While no one may have an appetite to actually eat dinner, sometimes a hot meal can be a good comfort to those grieving (aka, the death lasagna).\n\nI'm sorry that your family has to go through this, and I truly wish you all the best of luck and the most peace."
      },
      {
        "id": "o7grhod",
        "score": 2,
        "body": "If you have two days off in a row (we'll call them Saturday and Sunday), then spend all day Saturday doing all of your dog's favorite things, or things a dog should do before they die, such as going to a pond with ducks, or the ocean if that's an option, eating McDonald's & chocolate, make some paw prints (include the family's prints, too, if you like), etc. Then have an early appointment on Sunday so you and your family have the rest of the day to grieve together, talk about your favorite memories. You may wake up the next day feeling ok enough to do normal activities, or you may want an extra day off. I like what someone else said about having dinner plans ahead of time - order pizza or Chinese, or whatever special treat your family likes, in case you don't have the energy to cook. I'm sorry you're going through this \ud83e\ude75"
      },
      {
        "id": "o7g8rq0",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rewatc",
    "title": "Anyone a Vet Tech at a Zoo ? How did you get into the field ?",
    "body": "Currently doing my pre-requisites for the Vet Tech program at my school and my dream is to work with exotic / zoo animals, while also contributing to conservation work / education. Just curious as to people get these jobs because I know they're competitive!",
    "flair": "Discussion",
    "score": 10,
    "comment_count": 10,
    "created_at": "2026-02-26T01:15:37+00:00",
    "top_comments": [
      {
        "id": "o7fpwnr",
        "score": 30,
        "body": "Getting a job in a zoo (or with exotics in general) basically boils down to \u201chaving family/loved ones you can split living expenses with so that you\u2019re willing to take a job with a below-livable wage.\u201d Then you spend a lot of time busting ass for very little pay and hope you can climb the ranks before your body gives out. Everyone I know who works in zoos agrees that it\u2019s very fulfilling but also shamelessly exploitative (of the staff, not the animals)."
      },
      {
        "id": "o7j5xyf",
        "score": 9,
        "body": "The short answer is-they don't have to. Everyone in this field is driven by passion/love and the competition is fierce. If they can have 1000 people fighting for it at minimum wage, why pay more?\nThere are great zoo's who don't buy into this (looking at Cheyenne Mountain) but competition is even more fierce and people don't leave because it's so great. \nAlso...to be fair...zoo's don't make money. Animals are expensive, exhibits are expensive to maintain, food costs, specialized environments, staff etc etc....the price of admission doesn't balance the books. It requires a strong donation raising group---sometimes these run the zoo, sometimes they supplement city funding to keep these facilities afloat."
      },
      {
        "id": "o7g6bng",
        "score": 8,
        "body": "As a former keeper...yeah, you pretty much summed it up. Also be willing to move cross country because there are a limited number of zoo's.  Also be willing to work a second or third job. It's rough but rewarding."
      },
      {
        "id": "o7jwghu",
        "score": 6,
        "body": "Zoo vet tech here - what everyone else is saying is correct, it is extremely competitive.   Starting out in private practice with exotics is a great start, that's how I got started.   I will also say that you have to be willing to move.  There are simply too few institutions and too many people applying.   When I was just getting started, I was applying for 2 and a half years before I got hired.  I stopped counting after the 30th job I applied to.  And then even with experience, it's still hard.  Its a long process, and they purposefully make it difficult to weed out people that don't really want it."
      },
      {
        "id": "o7fsv1p",
        "score": 6,
        "body": "Thank you for the honesty! It's crazy how under appreciated zoo staff is :( "
      },
      {
        "id": "o7ibfnr",
        "score": 4,
        "body": "Hey I work as an exotics tech at a university, and it\u2019s pretty great! I interned during my RVT program and then got hired once I graduated."
      },
      {
        "id": "o7iuxz0",
        "score": 3,
        "body": "Ugh that really sucks :( Why can't they pay a livable wage, I don't understand!"
      },
      {
        "id": "o7iulfh",
        "score": 3,
        "body": "That's so cool! I found an animal hospital in my area that has an avian / exotic department, so I'll definitely be looking into that!"
      },
      {
        "id": "o7fnj79",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o8og2o6",
        "score": 1,
        "body": "Ayyyy that\u2019s my dream too! Any info guys??"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1resv1z",
    "title": "Voluntary recall of single serial of rabies vaccine | Boehringer Ingelheim US",
    "body": "",
    "flair": "Discussion",
    "score": 43,
    "comment_count": 17,
    "created_at": "2026-02-25T22:57:39+00:00",
    "top_comments": [
      {
        "id": "o7fnj1s",
        "score": 43,
        "body": "We had nearly 100 patients affected and it's been a pain in the ASS"
      },
      {
        "id": "o7fqnbt",
        "score": 42,
        "body": "We've had to call every single affected client and have them come back to the clinic to be revaccinated. Squeezing 100 free appointments into the schedule of a regular GP clinic hasn't been the worst thing to ever happen, but it has definitely been a hassle. We have probably 10 clients just dodging our calls so we've called, texted, emailed, and sent snail mail. Any of them that haven't replied by the end of March are getting a certified letter sent out and then we're supposed to report them to animal control(per the state vet), which is also insane."
      },
      {
        "id": "o7ft36j",
        "score": 9,
        "body": "Ouch...\n\nI'm sorry to hear that!\n\nIs BI offering anything to clinics, because I'm sure a number of clients are less than pleased..."
      },
      {
        "id": "o7gha9z",
        "score": 8,
        "body": "Great, more fuel for the antivax crowd."
      },
      {
        "id": "o7fw9py",
        "score": 7,
        "body": "They are, but it isn't anything miraculous. It's underwhelming at best"
      },
      {
        "id": "o7g8atu",
        "score": 3,
        "body": "It SHOULDN\u2019T? Can you imagine trying to enter a country, just to be refused or have your dog put into quarantine or PUT DOWN? \n\nThe customers should be compensated for this error and I hope they get a class action lawsuit against them."
      },
      {
        "id": "o7ip6ja",
        "score": 3,
        "body": "You're misunderstanding the recall. There were very few actual vials of sterile water in the lot. The vast majority were rabies vaccines. I imagine that the sterile water vials were clear and the wrong amount, and likely the water diluent for the Purevax rabies that BI also manufactures. We had a patient who previously had a severe vaccine reaction have another severe reaction to the recalled serial number vaccine. It was definitely still a rabies shot."
      },
      {
        "id": "o7fnutm",
        "score": 2,
        "body": "I can only imagine. \n\nHow are you guys managing this?\n\nThankfully this shouldn\u2019t effect those traveling internationally, too much, given the waiting period."
      },
      {
        "id": "o7hxi89",
        "score": 2,
        "body": "Is the vial just clear instead of pink ? how did you know?"
      },
      {
        "id": "o7ht1j8",
        "score": 2,
        "body": "If memory serves, you have to wait at a minimum a month, after receiving a Rabies vaccine in order to travel with your pet, after they receive their Rabies vaccine.\n\nThis batch, produced in February, wouldn't have yet made the month mark. So unless I am mistaken, no patient would have been allowed to travel outside of the country in that time, at least for an initial dose. Booster doses are a different category, but theoretically, I would hope that some degree of leniency would be afforded them for previous vaccine exposure +/_ titering. If any patients traveled during that time, with what these countries thought were valid vaccines, and these patients were discharged without issue, it gets us to the same point."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1reshu9",
    "title": "Scariest part of vet med",
    "body": "Huge aggressive dogs and feral cats lunging at me? I got it.\n\nRisk of zoonotic diseases? Rabies? Meh it\u2019s fine.\n\nMonitoring an extremely critical life/death procedure? Not my favorite but I\u2019ll deal.\n\nBeing covered in every bodily fluid all at once? Anal glands in the hair? Blood in my shoes? Fine.\n\nRunning a code? Shitty and scary for sure, but manageable. \n\nAbusive clients threatening me? Whatever. That\u2019s what the cops are for. Karma will get em or something. \n\nCALLING OUT??? \n\nWhy am I panicking and forgetting how to use words? Why do I feel like I\u2019m about to get executed on the spot for having the audacity to be sick? My coworkers are nice and it wasn\u2019t a big deal\u2026 but man I had to work up STRENGTH to make that phone call \ud83d\ude02",
    "flair": "Funny/Lighthearted",
    "score": 245,
    "comment_count": 26,
    "created_at": "2026-02-25T22:43:31+00:00",
    "top_comments": [
      {
        "id": "o7falgf",
        "score": 111,
        "body": "Employees should not be punished for being sick, or having lives outside of their employer.\n\n*sigh*\n\nI get that feeling, though.  It's a sad byproduct of the Workhorse Mentality from previous generations."
      },
      {
        "id": "o7fe1l9",
        "score": 37,
        "body": "I\u2019ve worked for clinics who wrote people up for calling out sick and not finding their own coverage. What a time to be alive."
      },
      {
        "id": "o7exu2y",
        "score": 34,
        "body": "Yeah, it\u2019s everywhere though not just vet med."
      },
      {
        "id": "o7fho3b",
        "score": 32,
        "body": "we have slowly eased my manager into texting her to call out instead of calling her and actually talking... it took a long time but she has softened. Texting to call out is so much less anxiety inducing for me... Until I see someone else typing at 5am in our management/lead text group to also call out lmao\n\nalso leaving it at \"Im sick, won't make it today\" and not giving all the details... they don't need it."
      },
      {
        "id": "o7gceu5",
        "score": 26,
        "body": "Yup.  I woke up sick as a dog with what was eventually diagnosed as the flu, had a 7am shift, and my managers EXPECTED me to find coverage at 5am.  Was out for 3 days with a doctor's note... coworkers had been showing up sick and told to \"mask up\" despite having 102\u2070 fevers and vomiting... absolutely toxic culture & mindset."
      },
      {
        "id": "o7fo49y",
        "score": 20,
        "body": "If you quit right now,\u00a0 remember that 99% of your current coworkers will never speak to you again, much less think about you.\u00a0\n\n\nI do make a lot of friends at work,\u00a0 but I'm old enough to know that in the long run no one is going to give you points for being a martyr.\u00a0 You do what you need to do.\u00a0 Your job is just that.\u00a0 Labor for money.\u00a0 These people don't give a shit about you otherwise.\u00a0\u00a0"
      },
      {
        "id": "o7fnvez",
        "score": 14,
        "body": "Texting would be SO fucking nice. At our clinic, we HAVE to call. Even if it\u2019s 3am or something \ud83d\ude2d\n\nAnd I agree with the last part. I hate when they\u2019re like \u201cwhat symptoms do you have?\u201c to try to weigh how sick you really are. Nah. You\u2019re not owed my medical history."
      },
      {
        "id": "o7iy1e5",
        "score": 13,
        "body": "I fill myself with righteous anger before I call out. It helps lol. If I'm sick I have the right to take time for myself and heal, otherwise I'm not gonna get any better!!!!!!!!\n\nHad a verbal tussle with my last PM about this because she demanded we find our own coverage since we had a lot of support staff. I was like woman, my back is spasming and I can't feel my right foot, you get a salary to figure this shit out leave me alone!"
      },
      {
        "id": "o7f25dz",
        "score": 12,
        "body": "Oh totally. What a terrible universal experience lol"
      },
      {
        "id": "o7iyzsr",
        "score": 12,
        "body": "Yeah I never understood how the person in charge of creating the schedule for the entire clinic was somehow not responsible for finding coverage when people took leave or called out.  Like, that is *LITERALLY* your job...."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1req57h",
    "title": "This came out of that?!",
    "body": "Had a year old cat under for dental the other day, her bladder was really full so we decided to help relieve some of the pressure. Nearly 60mLs!!!",
    "flair": "Funny/Lighthearted",
    "score": 231,
    "comment_count": 29,
    "created_at": "2026-02-25T21:15:57+00:00",
    "top_comments": [
      {
        "id": "o7etb5s",
        "score": 161,
        "body": "Now freeze it into a disk and slide it into the mail slot of someone who's wronged you."
      },
      {
        "id": "o7ef8s4",
        "score": 116,
        "body": "Holy moly! Obvious next question, she can pee on her own, no crystals?"
      },
      {
        "id": "o7erjk7",
        "score": 112,
        "body": "She can pee just fine! She was just really nervous and didn't like the litter box we offered her prior to her dental, lol. And no crystals either!"
      },
      {
        "id": "o7erv21",
        "score": 52,
        "body": "I'm not sure why my colleague chose to cysto her instead of expressing her bladder. It could have been because it was so full that manually expressing may have been painful, even under anesthesia. Not sure!"
      },
      {
        "id": "o7ey5ux",
        "score": 47,
        "body": "Cysto is way easier and quicker and plenty safe especially under anesthesia"
      },
      {
        "id": "o7eng22",
        "score": 36,
        "body": "I\u2019m wondering why she wasn\u2019t just expressed"
      },
      {
        "id": "o7ez82i",
        "score": 34,
        "body": "This is diabolical. I am saving this for later."
      },
      {
        "id": "o7fuhe8",
        "score": 28,
        "body": "We didn't actually need a sample, her bladder was just so large we didn't want her to be uncomfortable so we helped a girl out, lol."
      },
      {
        "id": "o7fwu7w",
        "score": 25,
        "body": "Thank goodness that's pee. I thought it was abdominal fluid at first."
      },
      {
        "id": "o7ex8m0",
        "score": 20,
        "body": "Interesting. We only do it if a sterile sample is needed. \ud83e\udd37\ud83c\udffb\u200d\u2640\ufe0f"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rep3jb",
    "title": "Need Help Distinguishing The Two",
    "body": "I\u2019m currently studying right now and feel really stupid. I need help distinguishing idiopathic epilepsy vs. syncope. Clinical signs, frequency, and severity and what are some things to tell owners. ",
    "flair": "School",
    "score": 8,
    "comment_count": 4,
    "created_at": "2026-02-25T20:37:28+00:00",
    "top_comments": [
      {
        "id": "o7e9k17",
        "score": 5,
        "body": "Here you go: https://youtu.be/IMPdIEtO4YY?si=ytc84jYTYLgdNiGu"
      },
      {
        "id": "o7e52va",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7ea98s",
        "score": 1,
        "body": "Thank you!"
      },
      {
        "id": "o7eas8p",
        "score": 1,
        "body": "You're most welcome."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rely2u",
    "title": "Using hand sanitizer to stop a snake from eating itself",
    "body": "",
    "flair": "Interesting Case",
    "score": 10,
    "comment_count": 6,
    "created_at": "2026-02-25T18:45:36+00:00",
    "top_comments": [
      {
        "id": "o7dsrf3",
        "score": 5,
        "body": "I feel bad because it looks like hand sanitizer got right in the snake\u2019s eye :/"
      },
      {
        "id": "o7e1y1h",
        "score": 4,
        "body": "FUN FACT: I just learned Snakes have eye caps that keep their eyes covered. So, as long as it's healthy, it shouldn't really interfere. They are hard and shed with the skin."
      },
      {
        "id": "o7e2tq0",
        "score": 4,
        "body": "Yay, that makes me feel better :)\n\nSilly noodle"
      },
      {
        "id": "o7e0o15",
        "score": 3,
        "body": "Ouroboros"
      },
      {
        "id": "o7dgyfr",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7dmnw5",
        "score": 1,
        "body": "Is it common for snakes to try and eat themselves? Also why \ud83d\ude33"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rely0t",
    "title": "Using hand sanitizer to stop a snake from eating itself",
    "body": "",
    "flair": "Interesting Case",
    "score": 16,
    "comment_count": 2,
    "created_at": "2026-02-25T18:45:33+00:00",
    "top_comments": [
      {
        "id": "o7dsb4t",
        "score": 3,
        "body": "Dude put it right on his eyes though, that part seems a little unnecessary."
      },
      {
        "id": "o7dgxza",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1reltqs",
    "title": "Overnight Care: The difference between nursing w/ hospitalization vs. medical boarding",
    "body": "This has been a long time coming.\n\nI know that there are strong opinions, and arguments on both sides regarding the appropriateness of each, but my question is, where do you personally draw the line?\n\nFor me, nursing with hospitalization is the most appropriate form of care that can be offered for patients recovering from surgeries, blocked cats on fluids etc. that require a more in the way of medical monitoring (eg. urine output etc.).\n\nOTOH, medical boarding, is most appropriate for those patients with a history of a given medical condition, that are otherwise well managed (e.g. Non-medicallly complex diabetics, thyroid patients, those with CKD etc.) that may need to be taken care of when an owner is away.\n\nHowever, I know that sometimes the latter is used in place of the former when the ideal is cost prohibitive, or isn't an option.\n\nHow do you all manage to care for those cases, while doing your best to insure appropriate outcomes for patients?",
    "flair": "Discussion",
    "score": 0,
    "comment_count": 10,
    "created_at": "2026-02-25T18:41:18+00:00",
    "top_comments": [
      {
        "id": "o7djn4c",
        "score": 21,
        "body": "Med boarding is a well animal with a chronic condition who needs to board and get medication. This would not be a pet who was admitted for being sick or having a surgery. I would not expect a med boarder to be getting meds more than BID. \n\nFortunately my hospital doesn\u2019t do any boarding so it\u2019s not an issue. My previous hospital did but there was never confusion because mostly the kennel assistants took care of them with the meds being checked by the techs and possibly administered (insulin). Any pet admitted through the hospital was hospitalized."
      },
      {
        "id": "o7drklh",
        "score": 7,
        "body": "Long time coming? Everywhere I've worked that does medical boarding, there's a \\*very\\* clear distinction between these two situations. If this is really an issue at your hospital, that's something you need to take up with hospital administration/medical director. "
      },
      {
        "id": "o7dt8ly",
        "score": 4,
        "body": "It\u2019s a tricky situation for sure, generally only done at general practices. My ER/specialty clinic only very rarely med boards, usually for internal medicine patients with a long established history at the clinic. \u201cMed boarding\u201d more sick patients like a cat with a free dripping urinary catheter is controversial because of the risks and the stress to staff if they do not feel prepared to manage a patient like that. It does however fill a niche of relatively basic but life-saving treatment in what would otherwise be a euthanasia case. I don\u2019t know if there is a right answer here."
      },
      {
        "id": "o7dnx0g",
        "score": 3,
        "body": "This is helpful.\n\nI've seen the latter done in place of the former, especially with clients who cannot afford transfer to a formal ER for hospitalization and monitoring."
      },
      {
        "id": "o7elfts",
        "score": 2,
        "body": "Every clinic I've personally worked at if they need intensive medical monitoring such as a blocked cat they have to be officially hospitalized cause it's taking a technicians time away from other things. Med boarding is they just need a walk or a litterbox clean and maybe a couple oral meds and that's it so it takes maybe 1-2 hours throughout the entire shift. My last hospital we actually had a tier system for boarding animals one was they needed nothing besides basic husbandry level 2 was they need 1-3 oral meds and level 3 they needed more than 3 oral meds or needed daily injections such as insulin or they were non ambulatory."
      },
      {
        "id": "o7dfzib",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7f6lrb",
        "score": 1,
        "body": "When I worked GP with medical boarding, we roughly used these guidelines:\n\n1. Healthy pet on oral meds: boarding with kennel staff. \n\n2. Stable pet that needs injectable meds or closer monitoring (mainly diabetics): medical boarding under tech staff. \n\n3. If it needs an IV, it\u2019s hospitalization."
      },
      {
        "id": "o7dtheq",
        "score": 1,
        "body": "It's not really something that we'd have input about.\n\nI know that in an ideal world, overnight monitoring is the best option, but what about places with no ERs, or ERs that cannot take on additional cases due to their current case load?"
      },
      {
        "id": "o7emyue",
        "score": 1,
        "body": "I like the idea of a tiered system.\n\nI know this is the standard in ER, but I've never seen it applied in GP."
      },
      {
        "id": "o7du59k",
        "score": 0,
        "body": "This is very true.\n\nThere is a new boarding facility opening up near here, that will potentially have overnight staff. \n\nI've wondered if that might be an option, for some, where a doctor can \"oversee\" a case remotely, if they were to hire medicsl staff that could administer those treatments. \n\nPerhaps it's a necessary niche to explore? I don't know.\n\nMost overnight care is exceptionally expensive in my area, and most ER hospitals will not accept a direct transfer."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1relpqg",
    "title": "Have an interview for an internship at a zoo coming up - do any zoo techs here have any advice?",
    "body": "I graduated in november after an externship at a wildlife rehab, and am taking the VTNE tomorrow, so crossing fingers I'll have that passed before my interview. I would love to work at a zoo or with wildlife as a career, and I was wondering if any established zoo technicians had any advice for the sorts of things they might be looking for in an interview?\n\nI am also a bit nervous, as I have an anxiety disorder, and I've managed to get a hold of myself for the beginning parts of interviews and do pretty well, but the longer they go the shakier and more prone to long pauses I get, which I don't think leaves a good impression.",
    "flair": "Work Advice",
    "score": 7,
    "comment_count": 1,
    "created_at": "2026-02-25T18:37:23+00:00",
    "top_comments": [
      {
        "id": "o7df3un",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1re3gu9",
    "title": "Considering quitting the field",
    "body": "So long story short, I work in a state where you don\u2019t have to go to school and pass the VTNE to be considered a vet tech. I was working ECC as an assistant for a year before I leveled up to a tech in October of last year. I\u2019ve been in school because proper education is important to me, and I genuinely love the job. Now the thing is I am very well liked at my job. The doctors really like when I tech for them, management loves me because I\u2019ll cover overnight and day shifts, and my coworkers know I\u2019ll pick up their slack. Now the issue isn\u2019t them or my company or anything, the issue is me. I\u2019ve had struggles with my mental health my entire life, but I\u2019m diagnosed schizoaffective which is a combination of schizophrenia and a mood disorder, which for me is bipolar. Only 0.3% of the population has it, and only 10-15% of people can work. I\u2019ve worked my entire adult life, but I\u2019m currently on medical leave because the stress got my symptoms flared up. Now I\u2019m wondering if I\u2019m not cut out for the field. My current plan is to work for the family business while I get my degree, and then go back to vet med but I\u2019m just so unsure and looking for advice. ",
    "flair": "Work Advice",
    "score": 14,
    "comment_count": 6,
    "created_at": "2026-02-25T04:33:52+00:00",
    "top_comments": [
      {
        "id": "o79yk2l",
        "score": 3,
        "body": "Are you receiving adequate psychiatric and/or psychological help for your diagnoses? I'm in a slightly different boat to you (ASD level 2, where \\~35-85% are unemployed + a few other physical/mental issues), but I can say that finding the right prescription and therapy combo for me was a lifesaver.\n\nAlso, it seems like you are super passionate about the work, and I absolutely think you have what it takes just from what you are describing here-- BUT! Constantly covering shifts and picking up other peoples' slack is detrimental for literally anybody and everybody. You can't reasonably be expected to sustain your physical and mental health when you are overworking yourself, even if the \"work\" is something you enjoy overall. I think you would greatly benefit from a reduced workload. This might look like working 2 days per week to start off with, and it may also look like setting some healthy boundaries between yourself and your coworkers, i.e no last-minute shifts, no compensating for lazy behaviors in others, no pushing yourself beyond what you are comfortable with etc.\n\nRemember, we can't help our patients until we help ourselves. A lifeguard can't save someone who is drowning if they themselves are going under. For your own sake, and the sake of your patients' well-being, you need to look after yourself <3"
      },
      {
        "id": "o7c4h1v",
        "score": 2,
        "body": "I also struggle with mental health. I inherited bipolar and ADHD, I\u2019m almost certainly autistic, and I picked up PTSD and a couple eating disorders throughout my life. Night shifts made mental health so much worse. I feel the only reason I\u2019m able to work, go to school, and upkeep my house is that I\u2019m religious about my sleep. One of the medications I take knocks me out, and I always take it at a certain time so I can be asleep at a certain time. Prior to having this medication I was religious about my night time routine, though that didn\u2019t always work (hence the meds). I\u2019ve found a lot of people with mental health struggles are similar in regard to the importance of sleep. \n\nI think it\u2019s fair to take a bit of time off, especially if you want to go to school during that time. Do you feel your family would be supportive? You mentioned a family business. \n\nSometimes all we need is a breather, some time to connect back to ourselves, and room to grow. I\u2019m rooting for you!"
      },
      {
        "id": "o7dawkv",
        "score": 2,
        "body": "My family would not be supportive, but my boyfriend is the one with the business and would be helpful and supportive. Thanks for the response, I might be trying to switch to days part time"
      },
      {
        "id": "o79savn",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7ki02j",
        "score": 1,
        "body": "I\u2019m also at 8 years in the vet tech field in a state where you don\u2019t need licensing and getting through vet tech burnout, pneumonia and mental health issues. I have no idea what else to do for work as I don\u2019t have a car anymore due to being knocked on my ass from the pneumonia and not wanting to interview at corporate jobs due to being so unsure about how to go forward and not wanting this long term (I\u2019m 38). I really only stayed in the field for pet benefits which change with each practice\u2019s benefits offerings."
      },
      {
        "id": "o7a2paa",
        "score": 1,
        "body": "Thank you so much. I am, the reason why I have issues is two fold lmao. One, schizophrenia is notorious for just\u2026stopping meds that previously worked from working. And two, I\u2019m super sensitive to meds, I\u2019ve been to the ER on four separate occasions because of medication side effects. But I definitely am working on finding a medication combo, which is part of why I\u2019m considering taking a break from the field and doing something less stressful while I finish my degree. \n\nIm thinking about going down to part time, my hospital just isn\u2019t super lenient on part time work. I also think id need to work day shift and they would want to keep me on night shift but overnights are notoriously bad for people with mental health conditions."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1re0022",
    "title": "Slow Days",
    "body": "I'm coming up on my work anniversary soon, and in that time I've seen the ebbs and flows of my current practice, between days when we're slammed, and those where we can barely get a patient through the door.\n\nI know that this is a nationwide concern, and not one limited to GP, but also one experienced at the larger ER and Specialty hospital that I do Relief work.\n\nRecently, my boss has been more flustered than usual over our dip in appointments, which is fair, but I'm concerned about the consequences for our good and loyal client base relative to our exam fees.\n\nWe're $2 shy of $100 for our exam fee alone.\n\nI have no say in whether that's a good price, or not, but I fear that any future price increases are going to push away our loyal clients, who patronize our clinic significantly, and dissuade future clients from becoming established with our practice.\n\nI don't judge our clients who take advantage of opting for vaccine clinic packages, and only visit us for non-wellness, or other chronic issues. Many of them have been priced out for labwork alone, but insist on coming to us, since they've been with us for years.\n\nI've considered working for a vaccine clinic, for my own peace of mind. Not that people don't have their own financial struggles there, but that the work is a bit more straightforward. It's primarily routine wellness exams, without the mental and emotional toll that comes from working in a standard GP and ER. \n\nI don't see any shame in that at this point, and think that's a good option for many. I apologize, I'm babbling at this point, but that came to mind when I was typing this out.\n\nSo the short version is:\n\nHow are your practices managing to remain financially stable, without penalizing your established to make up for loss in revenue?\n\n",
    "flair": "Vent",
    "score": 15,
    "comment_count": 9,
    "created_at": "2026-02-25T01:54:18+00:00",
    "top_comments": [
      {
        "id": "o798j9u",
        "score": 10,
        "body": "We are in a HCOL area, priced accordingly, with a full schedule 90% of the time. We have crazy high support staff and DVM retention. Our clients are not as phased by prices due to our area, but we still  accept care credit and scratch pay, plus Trupanion direct billing.\n\nI think with great staff and marketing, you can build a great client list no matter what. But it also heavily depends on your area. \n\nPricing wise, exams $100+, dentals $1-2k base, bloodwork $300 for full panel with UA/fecal. \n\nWe also heavily recommend insurance so even when it gets pricey, the clients have a safety net of some sort."
      },
      {
        "id": "o7bgff1",
        "score": 5,
        "body": "My GP is slammed everyday we are in MN outside of the metro area. Overall I\u2019d say we\u2019re on the cheap side. My ER is in the more metro area and weekdays are pretty slow, weekends ok but not slammed. ER is expensive obviously and i feel like hospitalizing is a cost concern and we are not seeing as much inpatient."
      },
      {
        "id": "o79ptnh",
        "score": 4,
        "body": "I was gunna ask if we worked at the same place lol.  Everything sounds pretty much the same except we don\u2019t do Trupanion direct billing"
      },
      {
        "id": "o7f39zt",
        "score": 3,
        "body": "My GP clinic is about 45 mins from Baltimore and we charge $80 for annual wellness exam, $85 for sick, and like $30-$50 for recheck/brief/tech appt. We stay fully booked like 90% of the time (usually overbooked \ud83d\ude05), have an UC building, and a mobile vet. Several regular relief vets and a few full time.\n \nWe did have to add on a credit card surcharge recently and our prices went up this year. But we offer cash and Venmo options, as well as regular discount codes/contests through Facebook (they have to see and mention the ad to get the discount)."
      },
      {
        "id": "o7b94g8",
        "score": 3,
        "body": "A lot of our established clients are older, and regrettably, a number of our patients are on the older end of the spectrum. In the year that I've been there, so many of the established patients that I met are no more. \ud83d\ude14\n\nI live in a HCOL area, but most of the people here are just trying to make ends meet. This applies just as much to younger people as it does to the elderly clients we have through the practice.  I've had them ask about discounts, and just general pricing.\n\nWe can't really keep up or compete with places like Bond and Vetco when it comes to vaccine bundles."
      },
      {
        "id": "o7c1v0u",
        "score": 2,
        "body": "Our gp is in a low income area in the desert. Our activity follows pay cycles. Start of the month and mid month we are slammed. Right before the middle of the month and right at the end of the month we are dead. \n\nOur prices are very cheap when compared to surrounding clinics. So we get a lot of office visits but not a lot to follow through on care. We're definitely not making big bucks."
      },
      {
        "id": "o7c3a0m",
        "score": 2,
        "body": "I'm sure that this has its fair share of challenges."
      },
      {
        "id": "o791cdw",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7bkkue",
        "score": 1,
        "body": "Hey!\n\nI lived in St.Paul!\n\nI miss autumn in MN some days!\n\nHere in NYC, the gap between GP and ER/Specialty fees isn't as broad as it used to be in the past.\n\nSpecialty consults have always been in the triple digits, but you get at a bare minimum an hour between the consult, diagnostics etc.\n\nIn GP you get anywhere from 15-30 minute, which isn't quite the same in terms of the expectations clients come in with based on what they're paying."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rdwdyx",
    "title": "Early appointments",
    "body": "Bit of a random question, but if an appointment shows up 30+ min early and someone is available to start the appointment, do you get it started or do you wait till the scheduled appointment time? \n\n  \nTo me, it makes sense to just grab it unless you cant because you're busy or eating or something like that. But ive worked with some people who will refuse to grab an appointment before the scheduled time even of they are doing nothing. I dont really understand why not, but i am curious if im in the minority here or if most people agree with me. And if you dont take appointments if they show up early, what is the reason?",
    "flair": "Discussion",
    "score": 18,
    "comment_count": 17,
    "created_at": "2026-02-24T23:22:49+00:00",
    "top_comments": [
      {
        "id": "o78bd3u",
        "score": 44,
        "body": "If there is time to grab and be done before the next appointment comes in I\u2019ll grab."
      },
      {
        "id": "o78dunn",
        "score": 29,
        "body": "If it's thirty minutes early I'll ask the doctor. Depending on which doctor they'll either almost always take it or always make them wait (lol). 10-15 minutes early I just take them to a room and warn they might be waiting a bit longer since they were early."
      },
      {
        "id": "o78djhb",
        "score": 19,
        "body": "if there\u2019s nothing else, i\u2019m getting them in and out, because odds are if you don\u2019t you get a fit in that shows up at the early person\u2019s scheduled time. \n\nESPECIALLY if it\u2019s towards the end of the night."
      },
      {
        "id": "o78pfrg",
        "score": 9,
        "body": "The important question is if doctor ready to see it? How many rooms you have? If I have enough rooms, I would take cats, nervous , dog reactive dogs to the room. The rest, I won\u2019t if dr not ready to take it yet : the client gets frustrated sitting in the room for long time. If they at front and know they early they can take walk, etc. , plus in some small clinics rooms are quite small and a bit claustrophobic:). Personally, I would prefer to sit at front."
      },
      {
        "id": "o78s8g0",
        "score": 9,
        "body": "We honestly don't check the times very often. If there's a clipboard in the checked in area, we'll just pick it up and go. Sometimes, if we notice they're early, we'll take a moment to reset and tidy and go pee first. Rarely do we make early people sit unless we are actually still working on the one before them. There is no need to make them wait if there is nothing else going on."
      },
      {
        "id": "o79n430",
        "score": 9,
        "body": "This irks more more than anything. Watching a coworker answer a non-urgent email, refill an RX or do literally anything else except grab the appt. Of course it\u2019s all circumstantial but if you run it by the doctor and they are cool with you starting early, why not!?! I work in specialty oncology so we don\u2019t have \u201cwalk ins\u201d or any surprise appts so why not?!"
      },
      {
        "id": "o78hhmj",
        "score": 7,
        "body": "This. It absolutely depends on the doctor and how much you can get done yourself."
      },
      {
        "id": "o79civw",
        "score": 6,
        "body": "This is my biggest pet peeve. Don\u2019t delay to later what you can do now! If it\u2019s a person who was told a specific time, and they show up early regardless, and everyone\u2019s busy, then sure, make them wait. But why leave it?"
      },
      {
        "id": "o7bnb8t",
        "score": 5,
        "body": "I also work in specialty and since people often come from hours away we often have people who are early because they wanted to account for traffic and what not. Theres no reason to make those people wait if we are able to start the appointment. Now if im sitting down for the first time that day and eating my lunch or something, I won't rush to get them. But if im doing busy work or something that can be paused, I see no reason to just get it going. But ive had coworkers that feel differently, I just dont get it.\u00a0"
      },
      {
        "id": "o79nfua",
        "score": 5,
        "body": "Yup! I like making my life easier by letting doctors decide for me when I don't feel like it \ud83e\udd37\u200d\u2640\ufe0f lol"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rdshi9",
    "title": "considering leaving the field altogether",
    "body": "not VT but VA, crosstrained reception and been on and off VA for a while. lately got thrown into being VA fulltime (which to be fair i asked for) and i have just felt nothing but stress since. i feel like i\u2019m messing up all the time, the team is getting frustrated, and my fellow receptionist is in a worse spot for it. ill be honest this is my third clinic ive went to trying to see if it\u2019ll click and it just hasnt. im constantly stressed and my mental health has all but evaporated. \n\nbut this is also the only career path i\u2019ve ever gotten on, and i was so proud of myself for moving up, learning more, and excited to learn but it doesn\u2019t feel worth it. what do I do?",
    "flair": "Work Advice",
    "score": 7,
    "comment_count": 4,
    "created_at": "2026-02-24T20:57:59+00:00",
    "top_comments": [
      {
        "id": "o77icpr",
        "score": 6,
        "body": "Be honest with yourself.\n\nThere is no use in being a martyr if you sincerely believe that this is not the field for you.\n\nSome might encourage you to keep trying, and perhaps that is appropriate, but only you know your limits on the matter.\n\nDon't grow to be resentful, appreciate the knowledge you've gained, and make a decision, one way or the other."
      },
      {
        "id": "o7bgdrx",
        "score": 2,
        "body": "As a person who feels like I'm messing EVERYTHING up, I have to be careful about what is anxiety and what is not liking something. If you're feeling anxiety about these new skills, it might be worth it to push thru and grow your confidence. If you truly dislike the work or the clinic, it's probably better to get out sooner than later. There are other jobs and you can be proud of yourself at those jobs too."
      },
      {
        "id": "o77g35k",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7a873m",
        "score": 1,
        "body": "It takes time to learn and be good at your job. But weigh the pros and cons of the field. If it\u2019s early enough, find something you can excel in while making a lot of money, because that\u2019s not vet med."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rdmhjr",
    "title": "Aspiration pneumonia paranoia",
    "body": "I'm new to the industry.\n\nA few months ago, I watched a sweet, older cat deteriorate over the course of a few weeks. He had aspirated some oral medication whilst under the effects of gabapentin, which made him drowsy and sluggish. His owners were absolutely devastated and blamed themselves for the whole thing. It was overall traumatic for everyone involved.\n\nIn the end, he was PTS. My vet said it was possible that he may have had lung cancer or other issues, too, but he was pretty sure aspiration pneumonia was the cause of his illness.\n\nNow, in the aftermath, I am DEATHLY AFRAID to give anything via oral route. And, lucky me, I've been prescribed buprenorphine buccal for my IC/FLUTD kitty. How am I supposed to get past this?? It feels like the little syringes depress instantly and shoot everything out at light speed to the back of her throat. I've been so paranoid\u2014 so afraid that every weird breath sound is proof of aspiration when, logically, her \"noises\" are probably just little snores/snorts because she's high as a kite and snores at the best of times.\n\nIt's literally 4am and I can't sleep because of this bs. Any advice or reassurance would be greatly appreciated :/ tbh, I don't even know what the early signs of aspiration pneumonia look like. I just can't stop thinking about the devastating cries from those poor owners.",
    "flair": "Vent",
    "score": 6,
    "comment_count": 18,
    "created_at": "2026-02-24T17:24:39+00:00",
    "top_comments": [
      {
        "id": "o7691m6",
        "score": 21,
        "body": "With love, have you had other instances in your life where you fixate on something the way you are now? Or is this an isolated experience?"
      },
      {
        "id": "o76a6b7",
        "score": 18,
        "body": "If it was that big of a risk no one would give liquid oral meds and we certainly would never recommend that owners gave them.\n\nI have been in the field for over 20 years and never heard of someone getting aspiration pneumonia from liquid oral meds. Thought I can definitely see how it can happen and I am sure it happens rarely.\n\nFor you, buprenorphine goes on the gums or in the cheek pouch. It is a transmucosal drug orally and should not be swallowed. If it is done right, the syringe should not be pointed at the back of the throat.\n\nFor your peace of mind here is some info about pneumonia [https://www.merckvetmanual.com/cat-owners/lung-and-airway-disorders-of-cats/pneumonia-in-cats](https://www.merckvetmanual.com/cat-owners/lung-and-airway-disorders-of-cats/pneumonia-in-cats)"
      },
      {
        "id": "o76euee",
        "score": 17,
        "body": "As someone who is clinically diagnosed with OCD and panic disorder and medicated, I feel you. I also know I\u2019m not supposed to reassure you. So I\u2019ll say that instead of administering the meds directly into her mouth, stick the syringe between her cheek and gums and break it up into smaller amounts. Like if it\u2019s a .3ml dose give it as .1ml three times in a row. Does that make sense? There are also different ways of holding a syringe that I feel give a little more control. Practice your holds and control using water over the sink. Personally I like to hold I like to hold it like I would if I was going for a stabby stabby motion and depress the plunger with my thumb. I can send you a short video if that doesn\u2019t make sense. Lol"
      },
      {
        "id": "o76foq5",
        "score": 8,
        "body": "If no post mortem exam was done on the elderly cat, there is no way to know if it was truly pneumonia and even then no way to confirm if it was caused by aspiration of meds. IF it was, he could have aspirated on his water dish, wet food or even his own saliva if he was that groggy.\n\nOne of my cats is on daily oral meds, I aim on an angle into his mouth so it hits his palette or cheek instead of straight down his throat to avoid the very slight chance of him inhaling at the exact moment the meds go in. He also snores like a freight train and makes all sorts of fun noises in his sleep, he is just fine."
      },
      {
        "id": "o76yq6l",
        "score": 8,
        "body": "Not sure if it will help you at all, but I like to go to this old study out of UC Davis: [https://avmajournals.avma.org/view/journals/javma/223/8/javma.2003.223.1142.xml](https://avmajournals.avma.org/view/journals/javma/223/8/javma.2003.223.1142.xml)\n\nIn that study, they searched the teaching hospital's necropsy database over a decade (1991-2000) for cats with pneumonia. They found 31,323 cat necropsies with 110 that had a diagnosis of pneumonia. Of those 110 only 6 had aspiration pneumonia. So 6 of 31,323 cats over a 10 year period (that's 0.02% if you're counting). \n\nNow, this is probably an underestimate, because not all cats who get aspiration pneumonia die, and not all cats who die of aspiration pneumonia get a necrospy. But point being aspiration pneumonia in cats is very rare, and even looking only at the 110 cats with confirmed pneumonia at necropsy, about 5.5% of those were from aspiration. I don't know if you've had to intubate a cat yet in your training, but they have a *very* robust laryngeal reflex.\n\nFurthermore, aspiration pneumonia is generally most problematic when it's aspiration of regurgitated gastric contents. Aspirating a tiny amount of buprenorphine almost certainly would do nothing harmful at all (plus, you probably couldn't shoot it straight into your cat's larynx if you tried). "
      },
      {
        "id": "o76birx",
        "score": 7,
        "body": "Haha, this isn't super uncommon for me. I've got diagnoses and meds, but they can only do so much to help."
      },
      {
        "id": "o76dj1c",
        "score": 6,
        "body": "The bup should be going on the gums/mucosa, it is not effective if swallowed."
      },
      {
        "id": "o76h1ez",
        "score": 5,
        "body": "Without a necropsy, no one can be absolutely certain what caused this cat\u2019s decline, and even if it was aspiration pneumonia, if that cat was so groggy on gabapentin, it could\u2019ve just as easily been water or food that it aspirated."
      },
      {
        "id": "o79vkaa",
        "score": 3,
        "body": "Thank you so much for your comment-- I had no idea that aspiration pneumonia was considered such an uncommon cause of death. And your comment about cats' laryngeal reflex makes sense, too. I didn't ever think to connect the dots between the two subjects, possibly because I have yet to intubate a cat and my understanding of the topic is limited to \"use a local anaesthetic to avoid spasms\" at this stage lol."
      },
      {
        "id": "o79tkj6",
        "score": 2,
        "body": ">If it was that big of a risk no one would give liquid oral meds and we certainly would never recommend that owners gave them.\n\nVery true-- thank you for the rational thought!\n\nAnd for the administration, I do struggle a bit because she's a wriggly little cat, but I generally aim it upwards on the side of the mouth, like I'm trying to hit her pre/molars. This is what I was told to do by a tech I spoke to in my local ER, and as my clinic doesn't often prescribe buprenorphine, I haven't been able to watch it/practice administration outside of my personal experience."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rdjnc8",
    "title": "Vet techs of CA-",
    "body": "Hey peeps! \n\nI had a couple questions as a fellow LVT looking to potentially relocate from Vegas. \n\n1- is the field there just as toxic or have you found good clinics with good doctors? \n\n2- Northern California vs LA/San Diego? I\u2019ve seen decent house prices in Fresno, Redding, Stockton. Are these still safe places to live? \n\n3- with your wage, is the state tax superrrrr noticeable? I still don\u2019t understand how that one works\u2026 \n\n4- is living in California actually worth it? \n\nI came from Florida, went straight to the desert and I\u2019ve never been more depressed. Between the \u201cmean \u201c energy from my coworkers, the doctors who only care about the money, and living in a city based mainly on tourism. I miss the beach, I miss the rollercoasters and I miss just being outside in the grass. \n\n. I\u2019m sure these are questions asked all the time, but I appreciate your answers! Thank you!! ",
    "flair": "Work Advice",
    "score": 7,
    "comment_count": 9,
    "created_at": "2026-02-24T15:43:10+00:00",
    "top_comments": [
      {
        "id": "o75nums",
        "score": 5,
        "body": "I've heard of insanely toxic clinics and insanely good clinics and clinics in between.  Housing I wouldn't know much about since I rent. Houses aren't affordable on tech salaries unless you have someone else helping to pay or you move somewhere far away from a city hub. Taxes are taxes like anywhere else they suck. I've heard northern California can be cheaper for the cost of living. Last ones pretty subjective I really like it here there's lots to do and the weather's great , but there are some major trade offs. The biggest one for me personally is the lack of space. I can't have a house with a yard because I can't afford it on a tech salary."
      },
      {
        "id": "o76lwzi",
        "score": 3,
        "body": "Toxicity is real. After running GPs, ERs, and Specialties, the answer is a hard absolute yes. Especially nowadays. Everyone is stressed about high costs out here, political upheavals, tough home lives, and general overall lack of being self actualized in a very spiritually demanding field.  And companies with good values on paper and mission statements like VEG or Modern don't equate that on the floor in practice with the grunts who are in the shit. \n\nMy experience is with the Inland Empire, Orange County, and Los Angeles metropolitan areas. I have met some genuinely good people, but the bad far outweighs the good in terms of meeting genuinely amazing personalities"
      },
      {
        "id": "o7883zs",
        "score": 3,
        "body": "1. Not sure what this even means anymore. Every industry has assholes. I can\u2019t imagine the assholes in CA are any different than assholes elsewhere. \n\n2. Fresno and Stockton suck ass and aren\u2019t anywhere near Northern California or LA/SD. Redding is cool. \n\n3. Hard to say on the state tax thing but I imagine it all comes out in the was considering wages will be slightly higher. \n\n4. Definitely not worth it to move here just to live in Fresno. Also I just don\u2019t want people moving here for selfish reasons. If my aging family wasn\u2019t here, I\u2019d be gone."
      },
      {
        "id": "o75pum0",
        "score": 3,
        "body": "Adding on to what I said. Personally I think California is great for techs who are more active and like to get out there and meet people and do things on their days off. I'm based out of  OC and I moved here from a very rural state so there's a lot of differences I've noticed. California overall is louder , brighter more in your face everything and everyone moves a lot faster. It can be really great , but also it's a lot sometimes."
      },
      {
        "id": "o75quok",
        "score": 2,
        "body": "Sorry for the word salad one more thing I forgot to mention in terms of things I've noticed about California compared to the country. There is a lot less wildlife especially around the cities that was the biggest culture shock for me when I moved from the country. When I first came here the cities felt dead in that regard."
      },
      {
        "id": "o75ilyv",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o77m17q",
        "score": 1,
        "body": "I can\u2019t speak to toxicity of clinics (I work in a non-vet volunteer capacity at a HVHQ spay/neuter clinic for feral cats) , but on your point 2\u2013\n\nI\u2019ll say if you\u2019re looking at Redding, also take a look at Chico. Chico is a nice little place to live \u2014 I moved here from Los Angeles many years ago, and I generally love it. \n\nBoth Chico and Redding are great for wildlife and hiking and have zero traffic. \n\nAll of California sucks for housing prices, whether rental or to own, but the Bay Area is outrageous. \n\nI personally would avoid living in the foothills because of the risk of wildfires, but others may have a different take on that. The Town of Paradise is rebuilding quickly after the Camp Fire and has affordable new homes.\n\nThe Sacramento area and its many outlying communities (Roseville, Folsom and more) are also good. If you\u2019re interested in Sacramento, check out r/Sacramento.  \n\nGood luck to you!\n\nEdit: added info that I am vet-med adjacent"
      },
      {
        "id": "o78xamd",
        "score": 1,
        "body": "1- is the field there just as toxic or have you found good clinics with good doctors? \n\nThis one is so clinic specific as it would be everywhere. Grass is always greener and all that. \n\n2- Northern California vs LA/San Diego? I\u2019ve seen decent house prices in Fresno, Redding, Stockton. Are these still safe places to live? \n\nI would go to Northern California if you have the choice but there is less of everything that way. Less job opportunities, less housing, ect. As for safe areas. Cities around here are not one style. In name sure but that's about it. You'll want to go to those individual subreddit to get a feel or take a vacation and walk around the areas you're interested in living in. \n\n3- with your wage, is the state tax superrrrr noticeable? I still don\u2019t understand how that one works\u2026 \n\nTaxes are high in California. It is difficult here due to cost of living all around. Make sure you factor that in. Many people come here and realize that they can't afford to live here without concessions in life style. \n\n4- is living in California actually worth it? \n\nThis is one that only you can answer. Finding a group of friends and a job you don't hate makes any location livable. Circumstances of all kinds are available here just as anywhere. \n\nI strongly recommend taking a trip out here BEFORE making any sort of decisions."
      },
      {
        "id": "o7a6d4a",
        "score": 1,
        "body": "1- is the field there just as toxic or have you found good clinics with good doctors?\n**This is clinic dependent, but I feel that if you strive, you can find good hospitals. Being in LA or LA-adjacent (Lancaster, Mojave, Ventura, SFV) is  good place to be. Lots of amazing clinics.**\n\n2- Northern California vs LA/San Diego? I\u2019ve seen decent house prices in Fresno, Redding, Stockton. Are these still safe places to live?\n**Depends what you want. LA/SD = 30 to 200% more expensive, Stockton & Redding/Fresno all have good streets & bad streets just like anywhere else.** \n\n3- with your wage, is the state tax superrrrr noticeable? \n**Hard to say. I make $71,000/annually pretax. Post tax it was like $55,000. I have bomb job benefits but I definitely feel like the taxes are ridiculous. Gas prices are bullshit, as is tax in the store, if that\u2019s what you mean.** \n\n\u201cI m from Florida, went straight to the desert and I\u2019ve never been more depressed. Between the \u201cmean \u201c energy from my coworkers, the doctors who only care about the money, and living in a city based mainly on tourism. I miss the beach, I miss the rollercoasters and I miss just being outside in the grass. \n**You moved to the desert from the beach, my friend. As someone who has lived less than 6 miles from the best beaches in California for my entire life, I\u2019d probably wither up and pass away if I had to move to the desert full time. Not even exaggerating. We went to Vegas a couple weeks ago and I felt like i aged 10 years in 3 days, all thanks to the dryness.**"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rdjdbq",
    "title": "On saying \"No\"",
    "body": "More of a \"Vent\", but I wanted to share the good news of finally being able to say \"No\" at work.\n\nI declined a set of additional hours, as well as covering a shift today, when offered yesterday. \n\nIt was a bit jarring at first, but it was a necessary step towards letting go of the need to put the needs of my job, above my own.\n\nSo for anyone in the same position, know that  it does get better.\n\nAuthenticity =/= selfishness, but acknowledging legitimate personal and interpersonal needs that do not turn you into a martyr.\n\nIt's part of a broader set of developments that have surfaced with my current employer, and my personal and professional goals.\n\n",
    "flair": "Positive",
    "score": 33,
    "comment_count": 5,
    "created_at": "2026-02-24T15:33:00+00:00",
    "top_comments": [
      {
        "id": "o75hk9p",
        "score": 20,
        "body": "Congratulations on saying no!\nAlso, remember that you don't have to explain yourself. If you're asked to pick up an extra shift or extend your hours, you don't have to tell anyone about your scheduling conflicts, life events etc. No is enough.\u00a0"
      },
      {
        "id": "o76518a",
        "score": 7,
        "body": "Explaining makes your response weaker, giving someone more points to poke at. Just a simple, \"No, that doesn't work for me / my schedule.\" DO NOT apologize either!\u00a0"
      },
      {
        "id": "o75hvd2",
        "score": 6,
        "body": "It took a while for me to get there, but yes, very true."
      },
      {
        "id": "o75gexx",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o88c04j",
        "score": 1,
        "body": "Well...here's a doozey... I realized in the midst of that conversation that two things came up.\n\nI'm not attributing malice on the part of my employer, but I'm also evaluating my own legitimate personal needs.\n\nI don't call out, unless I absolutely have to do so. I, unfortunately, haven't taken a true vacation since I started in this field.\n\nBut to the meat of the issue!\n\nWhile I am part-time, I am still entitled to PTO, which if memory serves is two weeks of paid vacation.\n\nI could, technically, break it up across several weeks of my scheduled shifts, amounting to at a minimum, a 4-week (2 consecutive shifts) blocks, and sporadically use the remainder as I see fit.\n\nIt places in context, the concern of not knowing who they'd place up there (I do administrative work.) were I unavailable, and the desire not to hire a third.\n\nI'm not doing anything morally objectionable by taking time that I have accrued off. I can't be held responsible for staffing, because I deserve time away."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rdgzhq",
    "title": "Update to moving on from a toxic clinic",
    "body": "hey y'all, I've had a \\*rough\\* couple of weeks. After my last job nearly destroyed my ability to work in vet med, I've been doing interviews and soul searching. I'm happy to say that I am now employed again at another clinic that understands burnout from coworker conflict. It means I also have to be on my best behavior as well, because I don't want to create the environment that I just escaped. I've also had a lot of time to reflect and figure out what I want and need out of my professional life. I've been quiet with my new coworkers about the specific abusive behaviors I experienced at my last clinic because I don't want to give anyone ideas. I will eventually tell them just so I don't accidentally get triggered, but there are very few situations that involve physically blockading me into a space unrelated to animal restraint and treatment. \n\nI'm really excited to learn how Antech lab diagnostics work, and this new clinic stocks feline bravecto (my favorite prevention for cats!) as a regular thing. I'm looking forward to the new opportunity and being able to start fresh.",
    "flair": "Vent",
    "score": 12,
    "comment_count": 2,
    "created_at": "2026-02-24T14:00:18+00:00",
    "top_comments": [
      {
        "id": "o75eu1i",
        "score": 11,
        "body": "I am happy for you, but I don't think you need to share what happened at your last clinic with your new colleagues. \n\nDon't allow the past to remain living rent free in your head. Let go, and move on.\n\nI had to come to terms with that yesterday. I said \"No\" for the first time in my veterinary career, to covering a shift.\n\nBest of luck."
      },
      {
        "id": "o74xuc9",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rdfwup",
    "title": "Washing instruments",
    "body": "Hi all!\n\nQuestions for the assistants and techs who wash surgical instruments\n\nHow do you guys do it? Been at my clinic for three years, only ever worked at this one and don\u2019t have any other friends in vet med so I have no idea what the standard is. We hand wash all our tools with a wire brush and dish soap, put it in the ultrasonic and then lube, lay out to dry, wrap and autoclave. This probably sounds kinda stupid but are there like instrument specific dishwashers? Or is it really all hand washing? I work at a small mom and pop clinic and we\u2019re quite old fashioned on certain things so I don\u2019t know if it\u2019s just us or if this is the way it\u2019s actually done \n\nTools are the absolute bane of my existence so I was wondering if there\u2019s some magical solution to washing tools lmao \n\nThanks!",
    "flair": "Discussion",
    "score": 15,
    "comment_count": 28,
    "created_at": "2026-02-24T13:14:10+00:00",
    "top_comments": [
      {
        "id": "o753kp5",
        "score": 39,
        "body": "The hand-washing is no fun but it\u2019s important. You have to hand wash so you can open and close the hinge of the instrument to make sure you\u2019re scrubbing out any blood or tissue, and you have to be able to inspect from all angles to make sure the instrument is clean (to the naked eye) before going into the ultrasonic. Yes we all hate it, yes this is how it\u2019s done."
      },
      {
        "id": "o74qsws",
        "score": 32,
        "body": "Use chlorohexidine over normal dish soap, honestly gold standard would be to use an instrument specific cleaner and let it soak"
      },
      {
        "id": "o757lb1",
        "score": 20,
        "body": "I actually enjoy cleaning instruments. It felt like a chore when at a poorly staffed/chaotic clinic so I see how others could hate it. But getting a clot noodle out of a suction tip is oddly satisfying! Did i just figure out my retirement plan?"
      },
      {
        "id": "o74v0xx",
        "score": 19,
        "body": "Hand wash with chlorahexadine and then put in the ultrasonic cleaner. Also, you should not be using a wire brush to clean because it will cause abrasions on the instruments"
      },
      {
        "id": "o75bt8g",
        "score": 14,
        "body": "last clinic i was at - i volunteered to be in charge of cleaning instruments and wrapping packs. because that area was tucked back away from the treatment area, and no one could see you working back there. so when i was doing that stuff, i was being left alone for a couple minutes and not pulled in 20 directions. "
      },
      {
        "id": "o75wfn4",
        "score": 10,
        "body": "I left vetmed to pursue sterile processing in the human field! \nThings are very very different between human and vet med, but ideally, you'd want to use some kind of enzymatic cleaner for the instruments and let it soak. Make sure the enzyme is for manual cleaning, most likely a neutral detergent. \nThe use of your ultrasonic is gonna be so important, since veterinary hospitals do not have mechanical washing apparatuses. Make sure they are sitting in the ultrasonic for the full time! The way the ultrasonic cleans is through cavitation, and that's gonna be your saving grace for making sure the instruments are good and clean prior to sterilization!"
      },
      {
        "id": "o75ehiq",
        "score": 6,
        "body": "- 10min soak in organisol instrument cleaner\n- scrub with brush to get rid of stuck on blood + clean jaws/hinges\n- rinse\n- ultrasonic 15 mins\n- surgical milk dip\n- air dry or pat dry with non-fibrous towel\n- wrap and autoclave"
      },
      {
        "id": "o75aeoo",
        "score": 6,
        "body": "I was so happy when I learned this! I despised those wire brushes."
      },
      {
        "id": "o75a78m",
        "score": 5,
        "body": "Same, which is so funny to me because I hate dishes with a passion."
      },
      {
        "id": "o775yg8",
        "score": 3,
        "body": "Sounds fairly standard to me. At my place we hand wash and scrub with soap, soak in enzymatic cleaner, ultrasonic, milk, then dry and autoclave.\n\nEdit: human medicine might have automatic washers, but vet med has a lot of bucket-and-rag type cleaning. Clinics don't usually have the funds for something more high tech, lol"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rdekdi",
    "title": "Wearing two lead aprons at once?",
    "body": "Lol i know this sounds like a shower thought but i sincerely wonder if it will be safer regarding radiation protection wearing two lead aprons one on top of another. If i have to stay in the room while shooting, there are always some extra aprons and thyroid shields. I can have two or even three simultaneously hahaha. \n\nI wonder if anyone have that idea before, or is it just stupid? Wondering what you guys think about it",
    "flair": "Discussion",
    "score": 5,
    "comment_count": 10,
    "created_at": "2026-02-24T12:10:13+00:00",
    "top_comments": [
      {
        "id": "o74r2vu",
        "score": 20,
        "body": "There's just no need. 0.25mm Pb protection is perfectly adequate for scattered radiation, which is all you'll receive during restraint. The link above is for heavy duty Pb to be worn during long fluoroscopic procedures, where their exposure will be a lot higher. Wearing multiple lead gowns is just going to give you back problems."
      },
      {
        "id": "o755k9k",
        "score": 16,
        "body": "Radiologist here. In theory, yes, two layers of lead is better than one. In practice, however, the actual benefit is trivial and the downsides are significant.\n\n0.25mm lead will block 90-99% of x-rays at typical diagnostic kVp. Doubling your lead doesn't double the level of protection, though, because x-ray photon transmission is exponential rather than linear. Furthermore, there are still many parts of your body that are still unprotected (arms, legs, back, head) so there's not much difference in your total body exposure if you double your lead. Meanwhile, especially if you're regularly in the room during x-ray exposure (which you shouldn't be), over time that extra weight will give you back, neck, and shoulder problems that may become debilitating.\n\nThe guiding principle of reducing occupational radiation exposure is ALARA (as low as reasonably achievable). The three main factors to achieving ALARA are time, distance, and shielding. Time means reducing the amount of time you are exposed to radiation. This is the most important one, because limiting your exposure time is much more effective than anything else. This means trying to not be in the room when the x-ray is exposed. Distance means getting as far away from the x-ray beam as possible. Exposure decreases exponentially (second order) with distance, meaning if you're 2x farther away your exposure is 4x lower. And shielding is the last part, basically meaning if you can't reduce your exposure time or distance, you should be wearing appropriate protection (lead apron, thyroid shield, and gloves \u2013 hands inside the gloves!). \n\nRadiation safety is a rampant problem in vet med, mainly I think due to ignorance of those making the policies, overall lack of regulation in veterinary medicine, lack of advocacy for vet tech safety, and the constant drive for profit and efficiency above all other considerations which we in modern capitalist society think is not only normal but morally right and good. So the idea that taking a radiograph may take longer or cost more money because the patient needs to be sedated or the clinic needs more vet techs to able to have multiple people working a case is viewed in the ALARA context as \"unreasonable\" by the policy makers (CEO/owner, Regional Director, Practice Manager, Chief Medical Officer, Vet requesting the study) who unsurprisingly are not the ones being exposed to radiation (vet techs). Which is why in some countries there are laws stating that it's illegal for a human to be in the room when an animal is getting x-rays. Because it's unnecessary, and lower occupational exposure can be achieved reasonably."
      },
      {
        "id": "o75kqan",
        "score": 6,
        "body": "No."
      },
      {
        "id": "o75u3n6",
        "score": 6,
        "body": "No, x-rays are made up of photons just like other forms of light. They just happen to be very high energy photons that can pass through objects. But just like if you had a dark room, turned on a light bulb, then turned it off again there is no \"residual\" light settled on objects or dust. "
      },
      {
        "id": "o74fucf",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o74ly2t",
        "score": 1,
        "body": "https://stemrad.com/bilayer-lead-for-radiation-protection/"
      },
      {
        "id": "o79oblr",
        "score": 1,
        "body": "No."
      },
      {
        "id": "o75j5gg",
        "score": 1,
        "body": "Thank you for the detailed answer. Actually there is one more thing that i wonder since you are a radiologist. Is being in that x-ray room exposes you to radiation when no x-ray is being taken? Like in between poses is there any radiation in the room, on the objects or dust etc? Thanks in advance."
      },
      {
        "id": "o761lnd",
        "score": 1,
        "body": "Thank you again, you've been very informative for me"
      },
      {
        "id": "o74mgo2",
        "score": -2,
        "body": "Wow it's not a terrible idea then"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rd3i20",
    "title": "Arthritic fantail pigeon radiographs",
    "body": "",
    "flair": "Radiograph",
    "score": 13,
    "comment_count": 1,
    "created_at": "2026-02-24T03:20:40+00:00",
    "top_comments": [
      {
        "id": "o72nnlx",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rd2y60",
    "title": "Will I need to buy a stethoscope going into the field?",
    "body": "I was told I might have to buy a stethoscope coming into the field. I'm just wondering if this is standard? Do vet clinics not supply stethoscopes there? Anything else I will have to buy?",
    "flair": "School",
    "score": 9,
    "comment_count": 29,
    "created_at": "2026-02-24T02:55:38+00:00",
    "top_comments": [
      {
        "id": "o72l2c1",
        "score": 39,
        "body": "I've worked at clinics with kinda crappy communal stethoscopes. They're usually not very good and then you have the communal ear gunk situation. I have never been at nor heard of a clinic that supplies a personal stethoscope. It's worth investing in one for yourself because a good one can last you most of your career."
      },
      {
        "id": "o735tbg",
        "score": 19,
        "body": "Unfortunately, this is one of the more affordable ones on the market. There probably are cheaper but it would be worth it to save up and buy the littmann or wait until it goes on sale."
      },
      {
        "id": "o72mfd0",
        "score": 13,
        "body": "We have communal stethoscopes but I bought my own with my own name tag that I use regularly. Doesn\u2019t stop vets from getting ahold of it, but at least I know it\u2019s mine and can steal it back."
      },
      {
        "id": "o72tgcz",
        "score": 12,
        "body": "Your classic littman 3"
      },
      {
        "id": "o73xfs0",
        "score": 9,
        "body": "You can get a cheap one for personal use but saving up for a littman is one of the better investments if you're in the field, it will last you for years and give you better sound than most cheaper stethoscopes. That being said, if all you're doing is checking heart rates, a cheaper one WILL function."
      },
      {
        "id": "o74au91",
        "score": 6,
        "body": "MDF is a great starter brand stethoscope. Litmann is great, but you don't *need* one to start out in the field."
      },
      {
        "id": "o7aqezg",
        "score": 4,
        "body": "Lots of clinics will have a couple old junk stethoscopes laying around. They won't be very good but they'll work in a pinch. If you're unconfident in your auscultation skills, or hard of hearing like me, you'll want a higher quality scope. That you should bring yourself.\n\n(And, not to put too fine a point on it, but if you're in tech school, an appropriate graduation present for you from friends & family should be a nice stethoscope, just like one would get a new grad lawyer their first briefcase.)"
      },
      {
        "id": "o72l853",
        "score": 3,
        "body": "They'll probably have everything, but your own might be better quality. It looks professional too when you pull out your own stethoscope but I think youd be fine if you dont have one"
      },
      {
        "id": "o72nzwg",
        "score": 3,
        "body": "There's communal clinic ones but I just don't like using them. My fiance bought me a Littman Classic 3 as a gift for Christmas a few years ago and I use it daily, and it has a cute scrunchie on it."
      },
      {
        "id": "o733vcj",
        "score": 3,
        "body": "My hospital has communal ones but I prefer to have my own that way I don\u2019t have to go searching for one when I need it."
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rd1jfs",
    "title": "Just a photo dump of my girl about to get spayed",
    "body": "(sorry for the repost, one of my photos had a phone number in the background) ",
    "flair": "Cute",
    "score": 63,
    "comment_count": 3,
    "created_at": "2026-02-24T01:55:02+00:00",
    "top_comments": [
      {
        "id": "o73uc5l",
        "score": 2,
        "body": "A beauty! Everything will be ok!"
      },
      {
        "id": "o7290ih",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o7628ed",
        "score": 1,
        "body": "#10 lmao"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rcwq0f",
    "title": "For those that were in school and worked full time\u2026..",
    "body": "Long story (somewhat) short: I have about six years of experience in the field, four of those in practice management. I\u2019ve realized the PM role just isn\u2019t for me, and I\u2019m happiest working on the floor. I\u2019m looking into attending Penn Foster to get credentialed.\n\nFor those of you who completed Penn Foster while working FT, I\u2019d love to hear the good, the bad, and the ugly. Were you able to finish on time?\n\nFor context, I\u2019m really only responsible for myself, so outside of work and school it\u2019s mostly just normal household responsibilities.",
    "flair": "School",
    "score": 9,
    "comment_count": 7,
    "created_at": "2026-02-23T22:50:19+00:00",
    "top_comments": [
      {
        "id": "o71gx3c",
        "score": 6,
        "body": "You should absolutely be able to finish \u201con time\u201d (technically you have 6 years to finish) but most people finish in 16-36 months. If you work full time and don\u2019t have kids or other things taking up your time you should definitely finish in two years or less. The only snags people tend to run into are waiting to get approved for externships OR finding a location for the final externship which requires large animals. \n\nOther than that, I see people who have experience do really well in the vet med classes like medical terminology, anatomy etc but then they take three months to complete their English class simply because they don\u2019t want to do the work and they didn\u2019t have previous college credits to transfer.\n\nI haven\u2019t finished with PF yet, I had to stop because we had to move before I finished my externship but I plan on hopefully completing it in the next year or so."
      },
      {
        "id": "o71j0y4",
        "score": 3,
        "body": "Finished in 2 years working full-time with two young kiddos, you've got this!"
      },
      {
        "id": "o71hc8q",
        "score": 3,
        "body": "Thank you!! All of this is super helpful - hope the move goes well! Just went through this myself and know how it can slow a lot of things down \ud83d\ude42"
      },
      {
        "id": "o71l5bl",
        "score": 3,
        "body": "This was me lmao\n\nBlew through all of the medical related courses easily. The office management courses made me want to peel my eyes out and it took me a while to complete because of how stupid it was \ud83d\udc80 I had zero motivation to write those damn papers"
      },
      {
        "id": "o71vcm8",
        "score": 2,
        "body": "I was hoping to hear that the beginning courses would be kinda second nature at this point! \ud83d\ude05"
      },
      {
        "id": "o71c8sa",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o71vf8e",
        "score": 1,
        "body": "Thank you!!"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rcodoi",
    "title": "A follow up limerick!",
    "body": "Few weeks ago I posted about my Dr that likes to sent haikus. Well another one of my drs replied to the email with a limerick! Enjoy! ",
    "flair": "Funny/Lighthearted",
    "score": 6,
    "comment_count": 1,
    "created_at": "2026-02-23T17:49:13+00:00",
    "top_comments": [
      {
        "id": "o6zl70w",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rch6o4",
    "title": "Speaking of it being your own pets.",
    "body": "My pug \ud83d\ude29\n\nWaiting on radiology reports but treating him for possible aspiration pneumonia and waiting to see about that heart. Sigh. \n\nSend my goddess boy your good vibes. He is truly the best pug ever. ",
    "flair": "Radiograph",
    "score": 39,
    "comment_count": 7,
    "created_at": "2026-02-23T13:18:13+00:00",
    "top_comments": [
      {
        "id": "o6y6sda",
        "score": 12,
        "body": "I wish I could edit my typo. It\u2019s supposed to say *goodest boy* \ud83e\udd23\ud83e\udd23"
      },
      {
        "id": "o73pryp",
        "score": 6,
        "body": "Sending positive vibes \u2764\ufe0f Honesty doesn't look like a totally horrible chest for a pug. \n\n(You can edit it. If you're using the app click the 3 dots on the top right of your post)"
      },
      {
        "id": "o74ublw",
        "score": 6,
        "body": "https://preview.redd.it/axifd9pn4glg1.jpeg?width=4284&format=pjpg&auto=webp&s=080125a424c20d07f7f3cf276b931c3abb784ece\n\nHe is actually the best. You can trim his nails, draw his blood\u2026he doesn\u2019t turn purple. We rescued him 8 years ago this month. Never thought id be a pug lover, but he\u2019s my guy."
      },
      {
        "id": "o74iuof",
        "score": 4,
        "body": "I like thinking if him as a \u201cgoddess boy\u201d. Sending you and your little dog dude lots of good vibes \u2764\ufe0f"
      },
      {
        "id": "o74fvpx",
        "score": 3,
        "body": "No I definitely caught this early. But scary just to have it happen to my guy. I know *how* it happened but I\u2019m also like \u201chow did this happen?!\u201d\nThank you for your good thoughts\ud83d\udc9c he\u2019s eating and brighter each day. Hoping we are on the upswing"
      },
      {
        "id": "o7b5ud2",
        "score": 2,
        "body": "It can be an unpopular opinion in this field\u2026 but pugs are the best. I\u2019m so glad he has an owner like you taking care of him and making his health a priority.\nI\u2019m sending both of you all of the love/positive vibes! \u2764\ufe0f"
      },
      {
        "id": "o6y37bw",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rch3hl",
    "title": "I'm sorry .. you said WHO is calling?!",
    "body": "Lol they needed an appt for their cat - it wasn't really a hang up LMAO",
    "flair": "Funny/Lighthearted",
    "score": 22,
    "comment_count": 5,
    "created_at": "2026-02-23T13:14:19+00:00",
    "top_comments": [
      {
        "id": "o6zjiqf",
        "score": 5,
        "body": "Icky Thump's cousin"
      },
      {
        "id": "o70z2vy",
        "score": 3,
        "body": "Nah, can't be, they're on a wagon to Mexico."
      },
      {
        "id": "o6z6eyr",
        "score": 3,
        "body": "Even better - that's the owners caller ID name \ud83d\ude02\ud83e\udd23"
      },
      {
        "id": "o6z4si2",
        "score": 2,
        "body": "Is that the cats name??"
      },
      {
        "id": "o6y2kxw",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rc30mc",
    "title": "The same plushie I used 10 years ago, when I was in school, is now being used by my mentee at work.",
    "body": "They are learning how to bandage with the Doctor for their Essential Skills checklist. I was practicing for my midterm which was learning how to sterile drape a surgery patient. My 'surgery table' was my ironing board. ",
    "flair": "Positive",
    "score": 31,
    "comment_count": 1,
    "created_at": "2026-02-23T00:45:12+00:00",
    "top_comments": [
      {
        "id": "o6vdtv3",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rc28yw",
    "title": "Best career route for tue following Wildlife Tech vision ?",
    "body": "Currently Hybrid emergency Clinic Vet-Aide, working on VetTech + Double-majour in Environmental Sustainability (certificate)\n\n\n[Mu](https://www.dovemed.com/health-topics/focused-health-topics/mu-receptors-functions-significance-and-role-opioid-pharmacology) dream is to spend as much time outdoors as possible \n\nRain, Snow, wind, drops landing on my face as it falls in slow globs through pine-needles, walking trails, in situe-GPEs, monitoring anesthesia as we bring back [fauna] to the clinic, assisting on [fauna]'s [surgery], taking care of their rehab, trekking back into the wild to set them free\n\nI initially applied for Environmental and Wildlife Management, but fell in love with the medical aspect when I started working in the clinic \n\nThe Environmental path does not have the medicine, the Vet Tech path does not have the great outdoors\n\nI want to merge both\n\n\nI literally claw at the walls and pace in front of windows when there is a good thunderstorm - let me out!\n\nIn class I look out at the Ravens and Crows and just want to be there with them.\n\n\nAfter I graduate with certification, what would be my best course of action?",
    "flair": "Work Advice",
    "score": 1,
    "comment_count": 10,
    "created_at": "2026-02-23T00:11:56+00:00",
    "top_comments": [
      {
        "id": "o6v8sj7",
        "score": 7,
        "body": "There is very very very few wildlife vet tech jobs most are for vets and vet students. And most wildlife tech jobs you don't get much outdoor time it's 95% indoors. It's basically a regular vet tech job but with wildlife instead of pets so lots of cleaning, paperwork, and administering treatments. Your best bet is actually getting your PhD and working in wildlife health. You can then work in wildlife data survey where you get to go into the field and collect data."
      },
      {
        "id": "o6vx5z9",
        "score": 3,
        "body": "Bit more of a [Hoser](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.sctvguide.ca%2Fprograms%2Fimages%2Fgwn.jpg) I'm afraid."
      },
      {
        "id": "o6vragj",
        "score": 2,
        "body": "You could try a government job if in the US. They have Wildlife Management jobs posted sometimes that require medical knowledge"
      },
      {
        "id": "o6v7ykh",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o6vreud",
        "score": 1,
        "body": "Can you tell me more about wildlife job or give me a link?"
      },
      {
        "id": "o6vw8pa",
        "score": 1,
        "body": "Could the Environmental Biology Majour (left column) with the Wildlife Specialisation do it?\n\nhttps://www.mcgill.ca/nrs/undergrad"
      },
      {
        "id": "o6vrj4k",
        "score": 1,
        "body": "USAjobs.gov"
      },
      {
        "id": "o6wl0xn",
        "score": 1,
        "body": "You can look up NWRA or IWRC they sometimes post jobs or A&M has a job board. I will say you have to be willing to move unless you live in somewhere like Florida or California."
      },
      {
        "id": "o6wlcfk",
        "score": 1,
        "body": "Could you yes will you be first pick for the job no. These jobs are VERY competitive. I took a wildlife chemical immobilization course and the instructor did this kind of work and 99% of the people his company hired were PhD students or had a PHD"
      },
      {
        "id": "o6wkfg4",
        "score": 1,
        "body": "Not a reference I was expecting to see, but it brought such joy to me, I can't even express it!"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rc1xdu",
    "title": "giardia giarding",
    "body": "",
    "flair": "Microscopy",
    "score": 46,
    "comment_count": 2,
    "created_at": "2026-02-22T23:58:31+00:00",
    "top_comments": [
      {
        "id": "o72xd8e",
        "score": 2,
        "body": "Nice!  Not too often do you see the trophs"
      },
      {
        "id": "o6v5l1n",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rc0asz",
    "title": "It really is always vet professionals pets\ud83e\udee0",
    "body": "I brought my girl to work with me cause she needs medication while I'm at work. I decided just for curiosity to just stick an ultrasound probe on her. Turns out she has some free fluid in her abdomen. She just had a full abdominal ultrasound at the end of January where nothing abnormal was noted. We did sedated rads and sent them out. The next day the radiologist apparently called the clinic saying to immediately call me with the results. There's a whole list of possible issues so she's going to see a specialist hopefully next week\ud83d\ude14. She's been acting completely normal aside from urinating a lot but she's on steroids so not surprising ",
    "flair": "Vent",
    "score": 7,
    "comment_count": 2,
    "created_at": "2026-02-22T22:50:45+00:00",
    "top_comments": [
      {
        "id": "o78qvmg",
        "score": 2,
        "body": "My dog recently had a medical anomaly as well. Why is it always ours? I wish your pup the best \ud83d\udc99"
      },
      {
        "id": "o6utkxl",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "VetTech",
    "id": "1rbxrli",
    "title": "Advice/Mentally Healing",
    "body": "Hi, I\u2019m an LVT of 5 years, I\u2019m currently working in ER and in shelter med. I had never been bitten by a dog until Friday and I\u2019m struggling with the idea of going back to work. The thought of handling dogs at this point is bringing me a lot of anxiety. \n\nTo preface:\n\nI was working at the shelter on Friday, we had a male intact husky mix, 80#, that needed a full check in (exam + vaccines) and needed to be neutered. The dog has been at the shelter for a couple weeks and was known to be unpredictable. \n\nMy VA brought the dog into a room to be sedated. We muzzled him, gave him IM dex/torb, and removed his muzzle. The dog was completely fine for all of it, did not react in the slightest. The dog was walking around the room, sniffing everything acting completely fine not showing any indicators that he could attack. \n\nWe decided to try and leave the room so that the dog wouldn\u2019t be stimulated and maybe the dog would fall asleep quicker. While trying to leave the room the dog tried to nudge himself in front of us, the VA pulled his harness and the dog went ballistic. he turned to me while I was back into a corner, grabbed a hold of my shoe and started shaking\u2026He let go and grabbed my arm and started whipping my arm and would not let go. My doctor came running and pushed the door open, which made the dog let go. As you can imagine, there was blood everywhere and I had to be taken to the hospital. \n\nI\u2019ve been thinking about it a lot this weekend and I\u2019m just absolutely terrified to go back to work and to handle dogs right now. I still have a few days at the least as the swelling in my arm and hand are still a lot\u2026but how have you guys managed to go back to work after being mauled?",
    "flair": "Discussion",
    "score": 14,
    "comment_count": 6,
    "created_at": "2026-02-22T21:10:41+00:00",
    "top_comments": [
      {
        "id": "o6ueavw",
        "score": 7,
        "body": "I am well aware that my experience will not be everyone\u2019s. About 9 years ago, I was working kennel in a big shelter. I worked with the behavior dogs and I loved it. One time, about 6 months in, a mistake was made and my entire left arm was used as a chew toy. And what I did personally was quite literally just jump right back into the fray. It honestly gave me newfound compassion and understanding for behavior dogs. When I left for dog/cat GP, I ended up being the one who dealt with all of them. Appointments were scheduled so that I would handle them. My thoughts were always \u2018I survived once, I will survive again\u2019. And I only ever had one close call after, and even then I had no actual damage.        \n\nI have a special place in my heart for bitey dogs, because there\u2019s usually a reason why they\u2019re acting that way. It\u2019s important to have a healthy skepticism of behavior and muzzles are absolutely your friend, but sometimes they just need a little extra help. \n\nI know it\u2019s hard, and everyone heals at different rates. You know your body and mental health best and you are allowed to take as much time off as needed, or limit yourself to something comfortable with."
      },
      {
        "id": "o6wh23p",
        "score": 2,
        "body": "Oh man, I'm so sorry. \n\nIt's really hard to come back from something like that. My experience is not the same, actually it's a bit opposite. I was mauled by a dog before entering the field. I knew I still loved animals but I was often (and still am, though it's getting better) extremely cautious or afraid around aggressive dogs because of my experience. Only now after several years do I feel less scared but I'll always hold that wariness.\n\nAnimals can be unpredictable no matter how well you read body language. I want to tell you what happened won't happen again if you just \"pay attention\" but that would be a lie. There is no 100% confidence in every situation, especially with dogs that can go from 0 to 100 with no warning. The dog I was mauled by was actually quite close to me - a friend's dog that I lived with for years and chose to hurt me simply in a moment it panicked due to a stressor and I was the closest target. That dog ultimately ended up being a behavioral euthanasia.\n\nI don't want to give you advice because I don't think I'm qualified. I think therapy is the best option. I guess, I want to let you know I've been there. And I still struggle, and a lot of the times overreact with fearful dogs which I think frustrates my coworkers. But in my mind it's \"better safe than sorry\", because I've seen what \"sorry\" looks like.\n\nI think time certainly heals most. Not everything and not completely- but most. In time you will feel less scared. But it certainly makes sense there is fear, apprehension, and all else present because frankly you've been traumatized.\n\nAre you able to take any time off? How had management/your coworkers responded to this incident? Are they supportive?\n\nIt might be healthy for you to avoid extremely fearful dogs at least for the next few weeks. But I know you're an LVT and that may not be possible in your position. I hope you work somewhere where they can maybe give you some grace and space to work through this sudden, terrifying ordeal."
      },
      {
        "id": "o7thbiz",
        "score": 2,
        "body": "When you return to work, discuss the incident with trusted coworkers and develop plans to hopefully work together to prevent similar occurrences in the future. \n\nTalk to HR or management about workers compensation paying for you to get access to regular therapy. Your doctor can also write you a referral for this if your workers comp is already paying for that, which would make it harder for them to deny its necessity. You can also have your doctor request reasonable accommodations from your employer in writing before they\u2019ll clear you to return to work; maybe to not have to perform restraint for a certain period of time or no work with animals that are over a certain weight limit or potentially aggressive. This would give you time to recover physically and mentally from the trauma you experienced. \n\nI\u2019m currently out on leave recovering from a bite myself. I\u2019m lucky that my current job has really supportive management and responsive workers comp, and they\u2019ve been great at getting me everything I need throughout this whole situation. I know for a lot of people that\u2019s not the case, and if that\u2019s you, continue to advocate for what you\u2019ll need to get well. \n\nAlso, while it\u2019s important to recognize if mistakes were made that led to your injury, accidents happen. Sometimes, even if everyone does everything right, these things occur and are part of life generally, not just for those who work in veterinary medicine. While we\u2019re exposed to certain risks in our job, and need to be cognizant of those and take measures to be safe, it\u2019s not healthy to constantly be at a heightened state of fear and anxiety. If returning to work with patients becomes that for you, it may be worth looking into other positions within the hospital that are off the floor and won\u2019t be torturous for you. \n\nIf you want to DM with someone also recovering, feel free to reach out."
      },
      {
        "id": "o6ua7ng",
        "score": 1,
        "body": "Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.\n\nPlease thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*"
      },
      {
        "id": "o6wpxor",
        "score": 1,
        "body": "I\u2019m so sorry you\u2019re going through this. 3 years ago I was bitten in the face by my patient. He was muzzled but it left me with some trauma and a scar to boot.\n\nEase your self back into it. Make sure you set clear boundaries and expectations with your co-workers on how you handle restraint and sedation going forward as a team.\n\nI know shelter med can add extra stress to any situation but your safety needs to always be priority. \n\nI have been attacked twice by German Shepherd breeds. I have set rules for that breed specifically when we deal with them in my clinic and my coworkers are aware. We make a plan before any treatments are done and I limit my contact. \n\nGive yourself grace to do what makes you feel comfortable."
      },
      {
        "id": "o7sy37j",
        "score": 1,
        "body": "A pitbull bit me in the face 2 years in for me. I needed stitches and had laser to remove all the permanent, broken blood vessels on my mouth, chin and nose with some success. I\u2019ve been fine but have never touched a pittie since and probably never will. I\u2019m very small and was lucky my face didn\u2019t get crushed or ripped off and I have to be aware of that. I\u2019m more so upset that I have these scars on my face and it\u2019s brought my low self esteem even lower.\u00a0"
      }
    ]
  }
]
```
