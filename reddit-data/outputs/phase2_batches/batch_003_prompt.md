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
    "id": "1rg0tj4",
    "title": "any tips for HSD grip issues?",
    "body": "I have hypermobility spectrum disorder (HSD) and ive been noticing myself struggle with gripping tools and food while cooking, specifically while holding a long food still like carrot or pickles to cut/peel. my fingers really hurt, struggle to keep a good grip or lock in place. as you could imagine, this is really annoying, but it only really happens when i need to hold something super tight or still (cooking, writing under pressure, etc).  \n\nany tips? alternative ways of cutting/peeling/gripping food? or am i just holding everything too tight lmao",
    "flair": "Question",
    "score": 4,
    "comment_count": 12,
    "created_at": "2026-02-27T08:07:32+00:00",
    "top_comments": [
      {
        "id": "o7oxvnw",
        "score": 6,
        "body": "Really sharp knives helped me. You can also get vertical grip knives, and gripping boards that hold the food for you. I also have HSD & specifically struggle with dislocating thumb joints."
      },
      {
        "id": "o7p9vl4",
        "score": 6,
        "body": "I use hockey tape to improve grip on many of my things. Worn out one armed person.\n\nEdit: read whole post. We just quit peeling our veggies. Even after working with the local college capstone to design a peeler that wasn't good, I have tried a few times as well, peeling is tricky to solve. \n\nThis is the link to the accessibility aids I have designed and worked good and use daily myself. Hopefully some can help you.  Hockey tape really is good stuff. \n\nhttps://thangs.com/designer/PlainsPirate?srsltid=AfmBOoopbP_uSS0nw8N82t_3DzNZbH_DjTfI4QnrsRQknZnku1sBkxRZ"
      },
      {
        "id": "o7ohj6a",
        "score": 3,
        "body": "I find taking breaks helps. \n\nAlso worth asking in r/hypermobility"
      },
      {
        "id": "o7oy1ic",
        "score": 2,
        "body": "You mentioned writing too, you can get soft pen grips that are designed to help with this, but you can make your own by poking a hole through a stress ball."
      },
      {
        "id": "o7scm8e",
        "score": 2,
        "body": "i'll definitely look tysm!"
      },
      {
        "id": "o7ox1qt",
        "score": 2,
        "body": "i didnt know there was a separate subreddit, i'll definitely do that thanks!"
      },
      {
        "id": "o7p2ok4",
        "score": 2,
        "body": "that was when i was in school doing hand written exams clutching onto the pen for dear life, and i wanted to present another example, but ty for the suggestion! its not a bad idea as i am an artist :]"
      },
      {
        "id": "o81dat3",
        "score": 1,
        "body": "For peeling something like a carrot, are you holding it vertically in one hand to peel with the other? Instead, maybe you can lay it horizontally on a cutting board and use the heel of your palm to hold down one side while you peel the other (rolling it as you do so that you can access the entire circumference), then turn it around and hold the peeled side down with your palm to peel the rest."
      },
      {
        "id": "o8ggfn8",
        "score": 1,
        "body": "Can you see an occupational therapist? "
      },
      {
        "id": "o7oy5bc",
        "score": 1,
        "body": "those options are really neat i'll definitely look into them!!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rfx72g",
    "title": "anyone here have migraines?",
    "body": "this is basically a question to anyone who has migraines lol but ever since i was a teenager i get what i consider severe headaches. the type of headache where my brain feels like it\u2019s literally pulsating and pushing hard against my skull. no specific triggers every single time but i know of some triggers like long car rides, heat and stress. i\u2019d been complaining about headaches for years and got fobbed off, i got sent to a neuro for the headaches and turns out i have MS (already had thought i did) but the headaches never really got brought up again apart from one time where my current neurologist might as well have said \u201ckinda\u201d to whether they\u2019re migraines or not\n\nthey\u2019re so debilitating and painful and usually i have to lie in a dark room for hours. i get really nauseated and noise etc gets really frustrating, my eyes will hurt, my shoulders can hurt. the pain can last for a day or so or even come and go in intensity for 3-4 days but for the most part painkillers don\u2019t work that well if at all. last week i felt so sick and was in so much pain on a journey home that i kept crying and felt like i was going to throw up every time i spoke even after taking an anti-emetic. only thing is, the pain is often my entire head or focused hugely on my forehead or the back of my head but it\u2019s completely debilitating levels of pain\n\ni have hypothyroidism and POTs too but this predates all of that. because i can\u2019t seem to get a straight answer or diagnosis of migraines/not migraines i feel like a clown repeatedly bringing it up and feel like my doctors don\u2019t take seriously just how agonising these headaches cause. if anyone has migraines i\u2019d love to hear an opinion on whether you think this fits with your experience or something",
    "flair": "Question",
    "score": 28,
    "comment_count": 49,
    "created_at": "2026-02-27T04:45:18+00:00",
    "top_comments": [
      {
        "id": "o7nd9ov",
        "score": 14,
        "body": "That definitely sounds like migraine to me. Everyone's experience is a bit different, of course, but all of those symptoms together scream migraine to me really. I've also come to understand they can have quite a few comorbidities, like POTS, so that feels like another check in the \"probably definitely migraine\" column. \n\nThere's the r/migraine sub that has a lot of helpful resources for things like what you can bring up with your doctor and different relief methods that you could maybe try in the meantime. The community there is great and really supportive and it has helped me immensely on my own migraine journey as well. \n\nI'm sorry you're suffering this pain without doctors really listening, but don't give up on advocating for yourself. I hope you can find relief"
      },
      {
        "id": "o7ndun5",
        "score": 9,
        "body": "Sounds like a migraine to me. I used to tell doctors I had \"bad headaches\" everyday and they didn't take them too seriously. Turns out, they were actually migraines. Doctors just assume you know the difference between a headache and a migraine, but how are you supposed to know if no one explains it to you?\n\n\nNow I take nurtec every other day as a preventive and I get migraine botox done every 10 weeks. Got rid of most of my migraines. I only get a few a month now. I still have a headaches everyday, but least they generally aren't debilitating."
      },
      {
        "id": "o7nfop6",
        "score": 5,
        "body": "One strategy is asking for a referral so repeatedly (politely, friendly, but insistent) that it\u2019s easier for them to say yes. \n\nIt may also help to document your headache symptoms - frequency, severity, etc to show your current docs to get the referral."
      },
      {
        "id": "o7nikkc",
        "score": 3,
        "body": "I get Botox and it helps a ton. I don\u2019t even get them anymore. I have pots as well."
      },
      {
        "id": "o7njjft",
        "score": 3,
        "body": "I get migraines twice a month. The only thing I can\u2019t stand is the auras. I will go blind for about an hour to prepare for the migraine. That\u2019s the time I take my medicine. It usually takes the edge off. I wish all the best in finding a solution to your problem."
      },
      {
        "id": "o7nq4hr",
        "score": 3,
        "body": "They do sound like my migraines, but a headache specialist might want an MRI or other diagnostics, especially if they\u2018re getting worse. And I also have hypothyroidism, so hello friend! Honestly you could just show a headache specialist this post.\n\nSeconding the Botox plus Nurtec recs in here. I went from daily migraines to maybe two a month. A lot of migraine research has happened in the past decades and the treatment options have gotten way better in my experience, if you can get access to them."
      },
      {
        "id": "o7neolp",
        "score": 3,
        "body": "i\u2019d pretty much always been told that migraines are one side of the head, so i was always saying bad headaches too until recently!! but still not entirely confident in using the word migraine because i\u2019m still not 100% sure if it fits and nobody\u2019s ever actually investigated or questioned it enough to even explain the difference\n\ni\u2019ve heard good things about nurtec, i was prescribed amitryptaline and sumatriptan before but i had really bad reactions to serotonergic drugs before so i\u2019ve been too scared to take them honestly. i\u2019m in ireland and the public healthcare system only rarely covers botox and i think it\u2019s when all else fails basically \ud83d\ude43 thank you so much for responding, i\u2019m glad you have some relief"
      },
      {
        "id": "o7oj0fl",
        "score": 3,
        "body": "Migraines take many forms. I had daily ones for years, but never thought they were migraines because I didn\u2019t get the nausea or light sensitivity my mom did with hers. When I eventually got sent to a neurologist she was instantly like those are migraines and prescribed me a CGRP abortive which  worked on the first try (still get them most days even on a couple of preventatives now\u2014but the pain is so much lower than before).\n\nIt also turned out I was having auras for a number of my migraines all along and just kind of thought everyone gets the blurry, wavy vision with sparkly spots shooting by once in a while. Apparently, that\u2019s not normal."
      },
      {
        "id": "o7oqexf",
        "score": 2,
        "body": "I have migraines, but my doctor doesn\u2019t seem to know the cause. When it\u2019s serious, I have terrible nausea and ringing in ears persistently for hours, and I would tear up uncontrollably. The way I\u2019d describe it is like someone is drilling into my head. Things that work for me are using frozen gel caps (bought on amazon), lots of caffeine and weed (legal in canada). Pain medication is obviously another option, but I cant use a lot of those because I\u2019m also on SNRI and the ones I can take are just not strong enough. Regarding doctors, if you have the money or insurance, don\u2019t feel bad over doctor shopping a bit because your current ones seem like they don\u2019t take your problems seriously and it\u2019s their fault (obv in this case)."
      },
      {
        "id": "o7v2qu5",
        "score": 2,
        "body": "Ubrelvy... lol... it's a migraine med and it's beAutiful!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rfx6aa",
    "title": "Canadian disability benefits kept me below the poverty line and punished me for wanting a family \u2014 anyone else navigating this? #fourlittlefeet",
    "body": "I'm a disabled person in Canada and I want to talk about something that I think a lot of people in this community experience but rarely name out loud: our benefit system is designed in a way that makes love and family financially dangerous.\n\n\n\nIf you're on disability supports in Canada and a partner moves in, their income gets counted against your benefits. You lose support. Disabled people are routinely advised by caseworkers to keep relationships off the books, not marry, not cohabit. Families don't get started. #fourlittlefeet is a hashtag I use for the children that never got to exist, the partners warned to stay away, the futures quietly erased by policy.\n\n\n\nThis isn't just a personal frustration \u2014 it's a structural issue. Disability income across Canada is set well below the poverty line. The Canada Disability Benefit, which was supposed to help, maxes out at around $200/month. And the moment anyone tries to build a life \u2014 get a partner, share a home, raise a child \u2014 those already-inadequate benefits shrink further.\n\n\n\nI've been working on a campaign called Jas' Law that asks for two things:\n\n\\- Raise disability income to at least the poverty line, indexed to the real cost of living\n\n\\- End spousal and household clawbacks that penalize disabled people for having relationships\n\n\n\nI'd genuinely love to hear from others here: has this affected your relationships or family decisions? Have you been advised to stay unmarried or live apart to protect your benefits? And if this resonates, the petition is at \n\nhttps://Change.org/endsocialisolation\n\n[End Social Isolation Petition](https://Change.org/endsocialisolation)\n\n\n\n\\#fourlittlefeet",
    "flair": null,
    "score": 169,
    "comment_count": 40,
    "created_at": "2026-02-27T04:44:14+00:00",
    "top_comments": [
      {
        "id": "o7o8wg0",
        "score": 62,
        "body": "It also makes disabled people  financially bound to abusive partners and hard to leave."
      },
      {
        "id": "o7no7lv",
        "score": 61,
        "body": "this is how disability benefits are across Canada its fucking gross. they expect us to either die sad and alone. or become someone else burden and have someone else have to take care of you well your not able to contribute anything because the steal all your benefits."
      },
      {
        "id": "o7oc23m",
        "score": 27,
        "body": "This is how it is in the UK too, it's incredibly cruel. Unfortunately a lot of the public believe a life on benefits is easy and that a lot of people cheat the system, so keeping the rules and keeping payments low is politically popular. I've spoken to couples who know they'll never live together because they simply couldn't afford to live otherwise."
      },
      {
        "id": "o7nokp7",
        "score": 26,
        "body": "This is like in every country though. Are Canadians punished for saving more then 2k like in the us though?"
      },
      {
        "id": "o7nsi2s",
        "score": 15,
        "body": "depends on the region. Ontario lets u have 40k in assists. a couple areas let u have 100k most are much less if u have more then the amount they say u can they just cut off completely.\n\nthere is also a special type of savings account just for disabled people who have the Disability Tax credit. called the RDSP any funds in this account are fully exempt. u can have upto 200k in these accounts. most disabled people will never reach that though with the poverty level funds they give us that basically leave u ever month choosing between paying rent or eating."
      },
      {
        "id": "o7oxana",
        "score": 14,
        "body": "That's crazy. I get around $720 in total (those come from different agencies) a month in my Eastern European s\\*it hole country and I can't lose those benefits under any circumstances. They are independent of everything but the severity of my disability. I've always thought of Canada as a social heaven but I guess I need to educate myself."
      },
      {
        "id": "o7nqjl2",
        "score": 14,
        "body": "\nI was never able to get provincial disability because of the household income policy in my province when I was living with my mom after becoming disabled but at least I got federal disability so I could pay for my perscriptions and not be a total drain. I decided to live with my now husband because either way I would have had no help from my province. I can't get any help from my province like the Disability Support Program or a perscription card. I just go without treatment like mental healthcare, massage therapy and lots of other stuff even cpap supplies. We will never have children or go on vacations because of me. We are unable to save money due to our higher cost of living. I cost us money and I know my husband would be better off financially if I were not in the picture.\n\nI also want to mention household income policies can trap people with disabilities in domestic violence situations!"
      },
      {
        "id": "o7o5mju",
        "score": 14,
        "body": "It\u2019s the exact same in australia :/ on top of that I\u2019m trying to do uni to stay sane and have a purpose within my own limits, using my accessibility resources + health professionals to make it sustainable - but in their eyes if I take more than 2 units (even if it\u2019s the easiest thing on the planet) I\u2019m \u2018fully able to work\u2019\u2026 it\u2019s going to take me over a decade to do anything and my debt will be larger compared to an average person. All I want to do is contribute to research, I don\u2019t have the capacity to be employed."
      },
      {
        "id": "o7r9qz6",
        "score": 13,
        "body": "This is also true in the United States for SSI. Marriage penalty, often a cohabitation penalty, and SSA workers often eager to assume you have support and cut you off prematurely, often presuming, i.e. , that you are married when you are not.\nAnd yes, forced to live below the poverty line.\nSee posts by Imani Barbarin for a very well -said explanation of \"legislated poverty\"\nAlso see John Oliver's episode about disability rules in the USA"
      },
      {
        "id": "o7o2137",
        "score": 12,
        "body": "It's the same in Algeria, I had to provide a certificate I wasn't married and bring two witnesses to get some quite frankly meager benefits, shame since I do sometimes mourn not being able to have a family."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rfvavq",
    "title": "Moratorium on Durable Medical Equipment Suppliers",
    "body": "There will be a pause, essentially, on new suppliers of Durable Medical Equipment (which i understand to mean everything from prosthetics to oxygen tanks and even guaze). Does anyone know how this will affect the cost/availability of these things? It is a 6 month pause. ",
    "flair": "Country-USA",
    "score": 49,
    "comment_count": 23,
    "created_at": "2026-02-27T03:12:50+00:00",
    "top_comments": [
      {
        "id": "o7n3etm",
        "score": 25,
        "body": "From a post I made about this earlier:\n\nThe 6-month freeze applies to initial enrollment applications and changes in majority ownership for specific DMEPOS supplier categories.\n\n\ud83d\udd38 It targets suppliers of equipment like oxygen tanks, wheelchairs, and braces. It does NOT stop patient access to existing, authorized suppliers. \ud83d\udd38\n\nGenerally, this does not apply to existing, properly enrolled providers, but may affect changes in ownership that require a new enrollment.\n\n\ufffc\u2754Why are they doing this:\n\nThe moratorium is being put in place to combat alleged rampant, multibillion-dollar fraud involving fake suppliers and unnecessary billing. \n\n\u2753Should I be concerned?\n\nYes, *but*\u2014 this moratorium doesn\u2019t mean patients won\u2019t have access to durable medical equipment and supplies through existing suppliers. ***As long as your supplier is currently authorized and properly enrolled, and no ownership changes are taking place, you should be okay to continue ordering DME & supplies as usual.***"
      },
      {
        "id": "o7mzav4",
        "score": 15,
        "body": "No idea. They haven't clarified anything yet.\n\n\nSo far they say it's for Medicare, not Medicaid,\u00a0 but that could change."
      },
      {
        "id": "o7mzo5j",
        "score": 12,
        "body": "They also supply and measure for wheelchairs, walkers and other things of that nature. I'm sure they work in hospitals to help patients with new equipment as well as I standalone joints. This is going to be detrimental for lots of people."
      },
      {
        "id": "o7n7pkg",
        "score": 9,
        "body": "\"Massive fraud\" claim the fraudsters. I think they caught sight of themselves in the mirror.\n\nMedicare is one of the biggest payers for DME.  Large amounts of people qualify for it every year. A moratorium of any length, even if just new Medicare enrollees, is bound to have impacts on these suppliers. Worst case scenario companies producing essential DME will close and we won't have replacements for them."
      },
      {
        "id": "o7n2970",
        "score": 8,
        "body": "Evil, evil people."
      },
      {
        "id": "o7n6uxk",
        "score": 8,
        "body": "My apologies for missing that post. Thank you for sharing here."
      },
      {
        "id": "o7n0tbz",
        "score": 6,
        "body": "Thank you."
      },
      {
        "id": "o7n7nvd",
        "score": 5,
        "body": "It was a Facebook post, so no need to apologize at all! Just thought some clarification would be helpful \u263a\ufe0f"
      },
      {
        "id": "o7n7hl3",
        "score": 5,
        "body": "I have used a DME for a wheelchair twice and I have no idea what someone would do if they couldn't. I need the model I have because I can't use a heavier chair and refuse to use an electric one, and it needs to be measured (an electric one would too) and maintained. They repair and deliver batteries for these, deal with wheelchair lifts and much more. Very frustrating to say the least... Not to mention the job losses and downsizing of these companies.\n\nHere is an example of more services they provide *and maintain*.\n\nhttps://www.lincare.com/en/services/dme-and-devices"
      },
      {
        "id": "o7n0r58",
        "score": 4,
        "body": "Thank you for the detailed answer."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rfty18",
    "title": "Voting assistant",
    "body": "My sister is disabled and we tyically do curbside voting for her.  This primary ballot was especially long, and she's been feeling especially weak in her arms, so we decided to do voting assistance this time, with me being her assistant.  \n\nI had to take an oath not to influence her vote, attest that I'm not her employer, etc, then I had to fill out a form.  Then the poll worker asked if I had \"taken 6 or more disabled people to the polls this election.\"  I found that to be an odd question.  My answer was no, but what if it had been yes?  Does anyone know if there are any laws or anything about this.  I'm wondering how that's anyone's business or why it matters.",
    "flair": null,
    "score": 14,
    "comment_count": 2,
    "created_at": "2026-02-27T02:11:25+00:00",
    "top_comments": [
      {
        "id": "o7mw32v",
        "score": 8,
        "body": "If you have, and they later determine all 6 are identical, they'd have essentially an admission of guilt or confirmation. Its a really convoluted way to get evidence."
      },
      {
        "id": "o7zamc0",
        "score": 1,
        "body": "I can't comment anywhere else but here in the UK a person who can't vote themselves can select a \"proxy\" instead.\n\nPR-DIS-E_EnglandProxy_Disability2023_form_2024.pdf https://share.google/9CbTaa7GJInUxwNzG \n\nThey go in your place. One person, one proxy They need a medical professional to sign off in this and the Elections Office  to approve it ( see form )  \n\nI worked in Local Government and have manned Polling Stations; I've also been a Proxy.  The staff are there to ensure all votes are legal made with capacity; without interference and there's no undue influence  So a person presenting as a proxy for several people would be flagged. \n\nThis isn't the same but similar - a couple of days ago we had a crucial by-election in the Manchester area. It's an ethically diverse area but divided into two distinct regions with very particular ethnic makeup. Some sort to discredit the results by alleging \"family voting\" ( didn't happen, it was a ploy ). This is where the male  head of a household instructs the family members who to vote for and makes sure they do. By taking them to the booth one at a time. This isn't allowed either and we had very strict rules to prevent. No matter what. Because  it's election fraud and vote tampering ( not to mention cohesion of an often vulnerable or disadvantaged person ). I imagine it's for similar reasons."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rftxht",
    "title": "Movable sink",
    "body": "Hey guys im designing/developing a sink thats movable on the vertical to have it be accesible for wheelchair users, users with crutches and adaptable for the general public so it can be everywhere and be used by everyone, i wanted to ask anyone finds the idea enticing? Like would this product interest u? Not like im trying to sell it but im looking to cover a necessity and i wanted to get some opinions",
    "flair": null,
    "score": 3,
    "comment_count": 14,
    "created_at": "2026-02-27T02:10:41+00:00",
    "top_comments": [
      {
        "id": "o7p7rxd",
        "score": 3,
        "body": "I like the idea--there's already things like that in use for pet grooming, where the basin of the unit can be raised and lowered, but I've never seen one for human use/in-house use.  I think cost is where things might get hung up, because most non-specialty buildings are constructed to use the cheapest materials with the fewest moving parts/parts that could break.  So, whatever you come up with, you'd need to match or better the cost of a built-in/non-moving sink."
      },
      {
        "id": "o7nm3k8",
        "score": 2,
        "body": "Maybe.  \nDepends on your execution.  \nLike, it should have one lever (control) to maneuver in either direction - twist right for up and left for down.  \nIt *might* have to comply with city\\\\state\\\\etc regulations.  \nControls for the sink (taps or handheld) could be anywhere but the back of the unit - how far can I stretch to reach it?  \nSounds like an idea. Run with it."
      },
      {
        "id": "o7uki8y",
        "score": 2,
        "body": "This already exists\u2026\n\nhttps://wealdenrehab.com/product/aquba-height-adjustable-basin"
      },
      {
        "id": "o7yiv9z",
        "score": 2,
        "body": "thanks for the feedback! And i agree completely, i thought it should be as easy to handle as posible, the point at the end of the day is to have it be completely adaptable with little to no effort to make the user feel the experience is completely individualized to them n their need, found some electric automated table legs with buttons that go up and down, i thought placing on the side of the sink, so it would be around the place one would have to be to generally use the sink :))"
      },
      {
        "id": "o7ym1wn",
        "score": 2,
        "body": "> the reality is it would only be aplicable to countertop sinks\n\nThat\u2019s really not helpful or filling a gap in the market then. \n\nIf I cannot get close enough to the sink (because of a countertop, under sink cupboard or other obstruction), I\u2019m having to lean and strain just to wash my hands. \n\nMany other wheelchair users cannot do that because they don\u2019t have the reach, core function, arm strength and so on."
      },
      {
        "id": "o7yn38s",
        "score": 2,
        "body": "No, I do not think it\u2019s worth it. \n\nPlenty of options already exist on the market. Simply google \u201cheight adjustable bathroom sink\u201d and you will find hundreds of results. \n\nYes, many of them look clinical but they are designed that way *for a reason*."
      },
      {
        "id": "o7yjycr",
        "score": 1,
        "body": "Thanks for the response! Yess cost is something i have to look into a lot to make it realistic instead of some sort of out of wordly futuristic idea, i was thinking of developing the concept as a sink that comes w its furniture included and mirror design, cus i was thinking of just debeloping the structure so it can be adaptable to every sink thats ever existed but the reality is it would only be aplicable to countertop sinks, i thought adding the furniture design and mirror integrated to the system (like the user is still visible on the mirror no matter the height desired for the sink) would create a more complete experience that would solve the idea of \"oh id have to get rid of the sink i already have to place this new piece of design and technology\" like it would make it worth it? I think?"
      },
      {
        "id": "o7ymhvc",
        "score": 1,
        "body": "Hello! Yes i know the concept is already being applied on different sinks, im trying to better it. admittedly i didnt see this one when i was investigating so thank u for the link, im a little confused tho by the fact that all the product pictures are all renders rather than the actual developed product. Anyway my design would be different, and use different materials, i thought creating a different variant would be good, like creating more options? Either way i wanted to know if people thought its was worth it or want it. Also the forms of my design are different, cus i also wanted it to have it be more accesible to users with crutches, and it wouldnt have the white panel but rather a mirror, to create a completely adaptable product without the need of having it look as clinical? More home-ish? I think those reasons make the design worth it, do u think it isnt cus theres one already in the market?"
      },
      {
        "id": "o7ynk9h",
        "score": 1,
        "body": "I see, from my reaserch, counter top sinks can be placed on a \"floating\" surface that would remove the need of the structure that would be in the way of the wheelchair, which is what i was referencing, like this i think.https://originalgranitebracket.com/products/free-floating-bathroom-vanity-kit-with-original-vanity-bracket?srsltid=AfmBOooPDgluNcUHYmToonUpVirNWbOxuhk3DeahCYqEnv5SnXNsmCfh\nI was also looking into creating a curve in the countertop and the sink to make it easier to be closer to the sink and not having to reach over anything to make use of it, what do u think? Have u found those style of sinks usefull"
      },
      {
        "id": "o7yo3xx",
        "score": 1,
        "body": "okay, thanks for the feedback"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rftwbq",
    "title": "I'm tired of having a speech impediment",
    "body": "I have lived my entire life with a speech impediment I can't say my r most people can understand me but my mom say talk better do it again and again she doesn't realize that I try I try it just bugs me how much I try to make improvements in my own life talking better having better grades but people consider me dumb or make fun of me all the time just because of a speech impediment I feel like people look down upon like im a helpless child I just hate talking to people nowadays it always they don't say anything about it or they won't stop talking about like dude im trying my best here like give me a break I have struggle with this more then ever the last couple of years. I just hate the way I talk ",
    "flair": "Rant",
    "score": 15,
    "comment_count": 6,
    "created_at": "2026-02-27T02:09:11+00:00",
    "top_comments": [
      {
        "id": "o7mokj6",
        "score": 4,
        "body": "Ken Venturi had a bad speech impediment, and he ended up winning the U.S. Open, and becoming an award-winning sports broadcaster and host.  Not trying to throw at you inspiration-porn, but people that overcome these kinds of things often go on to achieve notable things later.\n\nAt 10:38, he discusses his speech impediment: [https://www.youtube.com/watch?v=CZPb77ImUB0&t=26s](https://www.youtube.com/watch?v=CZPb77ImUB0&t=26s)"
      },
      {
        "id": "o7mpt5a",
        "score": 3,
        "body": "Honestly this actually did give me hope for the future"
      },
      {
        "id": "o7mopp5",
        "score": 2,
        "body": "I\u2019ve had a lisp for a little over a year now since a tooth pull. I visited my dad when it first started and was really bad he could barely understand me. It gets worse if I\u2019m tired. I try to speak slower and get my tongue right but it finds where the tooth used to be almost every time. I don\u2019t have your experience I just wanted you to know yes it\u2019s frustrating I understand."
      },
      {
        "id": "o7q3oli",
        "score": 2,
        "body": "I got a different battle, but what we share is x-ray vision. We get to see right into the very souls of people by how they treat us. You are awesome just because you care. Take care."
      },
      {
        "id": "o7mrj01",
        "score": 1,
        "body": "cool, I'm glad :)  Thanks"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rft5oc",
    "title": "I made a video on my experience as a former direct support professional. The system is messed up! Intellectually disabled people deserve better. \u2639\ufe0f",
    "body": "",
    "flair": null,
    "score": 4,
    "comment_count": 0,
    "created_at": "2026-02-27T01:36:16+00:00",
    "top_comments": []
  },
  {
    "subreddit": "disability",
    "id": "1rfofxm",
    "title": "Cleaning hacks for little to no leg use",
    "body": "Hello, \n\nI am a disabled man. I\u2019m dealing with chronic pain from an unhealed childhood injury. As-well as cartilage (maltracking issues) wear when I move my legs. \n\nSo, I can walk for short distances with little pain. But severe pain comes after a certain time. \n\nI have access to a walker, and may be moved into a wheelchair if physiotherapy doesn\u2019t end up working out. \n\nWith this struggle. I\u2019ve found it hard to keep my place clean. Brooming the house isn\u2019t really an issue as I can roll around in my walker when it gets bad. \n\nBut it\u2019s more things like oven, bathtub, countertops, walls, etc\u2026 \n\nI\u2019m wondering if you guys have any hacks?\n\nI\u2019m open to any suggestions you may have. Thank you! ",
    "flair": "Question",
    "score": 5,
    "comment_count": 10,
    "created_at": "2026-02-26T22:21:47+00:00",
    "top_comments": [
      {
        "id": "o7llntn",
        "score": 4,
        "body": "Extendable electric scrubbing brush could help for the bath. I have a connective tissue disorder, and I sit on a bath board & use that, then use a shower head to rinse off the cleaner. \n\nThe oven, i sit on the floor to clean. The shelves/racks just go into the dishwasher. \nThe countertops, i wipe off using disposable wipes daily to avoid needing to scrub. Maybe a perching stool could help you with that?"
      },
      {
        "id": "o7plsql",
        "score": 2,
        "body": "Are you getting in the bath? You can give it a clean before you get out. not with cleaning products but a squeeze of soap and cloth and rinse off before you get out. Or just give the sides a rub while your are in there to get rid of any tide marks.\n\nI would be sitting on the floor to give the oven a clean then using silicone sheets to go over the bottom/on the trays that can be pulled out to keep clean. An air fryer is great and not that expensive and solves the bending down to oven issue. \n\nIf you cant reach counter tops face on then have to reverse close up and do everything side ways. Or get a few trays and use them as work surface to make a sandwich or chop veg that can be lifted to the bin/sink and its all contained.\n\nNot sure [I.ve](http://I.ve) ever cleaned my walls but a mop or wipe on a stick would help. "
      },
      {
        "id": "o80r8c7",
        "score": 2,
        "body": "I have a long extended brush to clean the shower/bathtub. I do it sitting in my shower chair right outside the tub, an extendable shower head helps a lot with rinsing\n\nI keep wipes on hand to wipes down the counters after use to keep them clean and avoid how often they need scrubbing. Then once again, I use an extendable scrubber, while sitting in my wheelchair. You can use a squeegee to quickly get soapy water off easily (also come extendable) \n\nThen oven is a little tricky, I take out the wracks and put them in the sink. Then position my chair right in the corner of the oven, from there I can usually reach the whole oven. Once again, extendable tools are your friend \n\nYou can also get one of those swiffer mops, but instead of blowing money on the wipes, just use a normal ol\u2019 microfiber cloth. You can wet it with hot water, hook it on really easy, and you now have a long arm to wipe anything down out of reach"
      },
      {
        "id": "o84ug72",
        "score": 2,
        "body": "I bought a rolling stool...like a laboratory stool, adjusts up and down. I use that around the house for a lot of various chores. I have a similar situation where I'm fortunate to be able to stand and walk but time on my feet is very limited."
      },
      {
        "id": "o7u5v4u",
        "score": 2,
        "body": "I dust my walls with an extendable swiffer duster that lets me set the head at different angles.  If you're at the right angle, this also does inside your light fixtures too.\n\nIf they need cleaning, I use a floor swiffer with microfiber cloths stuck in it.  (mops work too, but the swiffer is really lightweight).  Change the angle and it also does baseboards without you bending.  \n  \nRun your microfiber cloths through the wash to clean, <but not the dryer>.  Dryer wrecks them."
      },
      {
        "id": "o7y775m",
        "score": 2,
        "body": "Will invest in one, thank you!"
      },
      {
        "id": "o7pvb4z",
        "score": 1,
        "body": "Thank you for these suggestions, very much appreciated :)"
      },
      {
        "id": "o7pviso",
        "score": 1,
        "body": "Trays are genius, thank you for all your suggestions!"
      },
      {
        "id": "o85mqej",
        "score": 1,
        "body": "I will invest in some extendable tools, thank you for the detailed suggestion! Will invest in a swiffer as-well seems like they\u2019re much more useful than I could have imagined."
      },
      {
        "id": "o85m72n",
        "score": 1,
        "body": "Thank you for this suggestion, great idea. I\u2019m fortunate to have the use of my arms, we adapt however we can. I think that\u2019s what makes humans amazing :)"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rflzrm",
    "title": "Going from carrying around 20lb + backpack to a not so sturdy wheelchair could use some tips",
    "body": "Pics are of my wheelchair company and is almost identical to what I have and my backpack I am used to carrying around backpacks with extra spare outfits , long heavy duty extension cables, surge protectors,toiletries everything I need to be prepared for unexpected long emergency room visits or to commute from my job/work and  to hospital without stopping at home because wife is chronically ill. \n\nI got hurt at work chasing one of my special needs students so navigating insurance vs workman\u2019s comp.  \n\nTables have turned wife taking care of me now as I broke my tibia and the talus bone in my foot. In a wheelchair and gonna be in a wheelchair for 6-8 weeks after I get surgery whenever that happens.\n\nI already downsized to a laptop bag and got essentials only but still feel naked. \n\nAlso phone screen protector cracked on 3-4 out of 4 corners because pockets are basically nonexistent while sitting in wheelchair.  What phone case are you using? \n\nI am thinking new phone case + tether lanyard ",
    "flair": "Question",
    "score": 13,
    "comment_count": 6,
    "created_at": "2026-02-26T20:50:25+00:00",
    "top_comments": [
      {
        "id": "o7n4y66",
        "score": 5,
        "body": "I use a cross body bag over my chest as my daily bag. I\u2019m permanently wheelchair bound so I like my bag to carry toiletries, power bank, phone, etc. and crossbody allows me to push without getting in the way. Getting one big enough for a laptop is challenging but you can hang your backpack from your back push handles on your chair\u00a0"
      },
      {
        "id": "o7ru1mr",
        "score": 5,
        "body": "you will want a good seat cusion for any long term sitting in this type of chair, as it will wreck your back. "
      },
      {
        "id": "o82yi99",
        "score": 3,
        "body": "The best advice I can give is to find a good occupational therapist. \n\nThese people have experience with assistive devices, home modifications, and so on. \n\nThey can offer a wide range of advice on everything from assistive devices to dealing with mental and/or physical energy drains."
      },
      {
        "id": "o89x1fb",
        "score": 1,
        "body": "That is not the style of wheelchair. I would recommend for anyone who is a day-to-day wheelchair user. That wheelchair design was intended for temporary hospital use. If you're in the United States, I can refer you to an organization that you can reach out to which will walk you through the process of using an any in all available benefits to get a wheelchair that will better suit you reply and let me know if you're in the United States. If not, let me know what country you're in. The Internet is a wonderful thing. I can probably find a resource for you somewhere in the world."
      },
      {
        "id": "o8bn7dk",
        "score": 1,
        "body": "I am in US and workman\u2019s comp is paying for everything. I got hurt chasing a student at elementary school. I am not allowed to use Medicaid to cover anything. I had surgery delayed because of waiting on workman\u2019s comp authorization. \n\nIf you think I would still be eligible I would greatly appreciate any information."
      },
      {
        "id": "o8btdwb",
        "score": 1,
        "body": "Reach out to these guys: [numotion.com](https://numotion.com)\n\nTell them your situation and then let them take over. If it is doable they will make it happen. It's how they get paid."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rfk4qo",
    "title": "Adaptive devices for limited hand functioning",
    "body": "trigger warning: talk of medical needs and anatomical body name parts\n\nI am going to try and keep this very factual. I have Crohn\u2019s disease as well as many other conditions that affect my mobility and the functioning of my hands. I currently have a very severe anal fissure and cannot seem to get anyone to take it seriously or help me adapt my care plan. \n\nAfter weeks of suffering and not hearing back from my GI I gave in and went to the ER and then called the  fissure and hemorrhoid clinic (different than gastro) to get on the cancellation list and happened to get in the next day. The doctor was gentle but brief and by the time his instructions sunk in and I thought \u201cI can\u2019t physically do that\u201c he was already out the door. \n\nCan anyone think of an adaptive device I can buy in Canada to get a vasaline based ointment out of prescription bottle, and at least 5 cm up the bum, without help from another person and without using my own fingers other than perhaps to plunge something?\n\nBecause it even hurts to breathe, I have been trying to do manually, but it is so painful that after 7 days I could no longer hold a fork. 3 pharmacies have told me to basically suck it up, and one said to have the compound pharmacy make me new meds with prefilled compounded single use syringes. I asked about suppositories but they said it wasn\u2019t possible. This tiny container was like $100 and at this rate will last 3 weeks\u2026 and I don\u2019t have compound insurance. \n\nplease help me \ud83d\ude16\ud83e\udd7a",
    "flair": "Question",
    "score": 7,
    "comment_count": 14,
    "created_at": "2026-02-26T19:41:00+00:00",
    "top_comments": [
      {
        "id": "o7kpmlz",
        "score": 9,
        "body": "OP, is this something your primary could get a home health nurse/cna *prescribed for*, to help you get it done?\n\n\nBecause this is the sort of wound care that Home Health *can* be prescribed to help with."
      },
      {
        "id": "o7now5k",
        "score": 6,
        "body": "Such a valid point that I never consider for myself. I have found a solution for now but I have I won\u2019t rule that out and I appreciate you suggesting it!\u00a0"
      },
      {
        "id": "o7li00r",
        "score": 5,
        "body": "I\u2019m not sure if this would work for you but they make [anal lube applicators](https://www.lovehoney.ca/lubes-essentials/lubes/lube-applicators/p/bondage-boutique-extra-large-lubricant-applicator-syringe-0.5-fl-oz/84569.html) and sell them at sex shops. Don\u2019t worry there is nothing graphic at the link. I\u2019m not sure if it would work with limited hand dexterity but it has loops that you could put a finger in to help grip.\n\nI know for people with paralysis there are digital stimulators and suppository inserters for bowel programs. But I don\u2019t know how it could shoot a large amount of petroleum jelly up the rectum as they are mostly for removing material not adding."
      },
      {
        "id": "o7noscv",
        "score": 5,
        "body": "OMG this is exactly what I needed. I sent a friend out to buy one and it\u2019s perfect. Thank you so much!!! Nothing else could get enough medicine up there and this was pretty easy to clean too. You are a life saver.\u00a0"
      },
      {
        "id": "o7meggx",
        "score": 3,
        "body": "Google suppository applicator. Worst comes to worst, you could buy a yeast infection kit that would have something similar included."
      },
      {
        "id": "o7kogcb",
        "score": 3,
        "body": "I apprecaite the suggestions.\u00a0\n\nI\u2019m unfortunately allergic to lidocaine. I was doing lots of sitz baths at home, but I\u2019m staying elsewhere right now because I\u2019ve gotten so sick and I can\u2019t get in or out of this bathtub. I also can\u2019t sit unsupported on the toilet for very long to do one of those types of sitz baths either :(\n\nI suffer from extreme chronic constipation and due to life circumstances and meditation changes I am still struggling to get it under control"
      },
      {
        "id": "o7q8i2m",
        "score": 3,
        "body": "The hilariously funny thing is that I have never personally used one but am a gay male (trans) and have had partners use them but never in front of me. When you mentioned it I had a memory come up of an open package stored away somewhere, but I am not staying in my normal environment. I am autistic and ALWAYS appreciate people's obscure knowledge. Thank you again. :D"
      },
      {
        "id": "o7n6f2a",
        "score": 2,
        "body": "Amazon digital stimulation bowel tool. You can coat the end with the medicine and apply it that way\u00a0"
      },
      {
        "id": "o7np51f",
        "score": 2,
        "body": "I appreciate the suggestion! That was also my first thought (and the pharmacist\u2019s) I did already try both of those but unfortunately because the sphincter is spasming so tightly I can\u2019t insert them. But the lube applicator someone else suggested I was able to get to work great!\u00a0"
      },
      {
        "id": "o7p80uw",
        "score": 2,
        "body": "I\u2019m so glad I could help! I\u2019ve never used one but I saw one before and it looked similar to a medication applicator I had to use once. Never thought recommending lube syringes would improve anyone\u2019s life but I will keep using my obscure knowledge for good! I hope you heal quickly and start feeling better soon!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rfj4kb",
    "title": "has anyone here lives or be to a Occupatonal therapy or aba type facility or assisted living? Whats is it like?",
    "body": "my inpatient is send me too one cause mine support needs are too high for here and they thinks its is not a good fit\n\nim have level 2/3 autism dyspraxia dysgraphia and other disabiltys",
    "flair": "Question",
    "score": 7,
    "comment_count": 5,
    "created_at": "2026-02-26T19:04:08+00:00",
    "top_comments": [
      {
        "id": "o872hin",
        "score": 4,
        "body": "Can you ask for a \"care giver\" and your own apartment instead? You shouldn't have to live at a group home. Those places aren't good enough. They're carceral and degrading. You deserve the space to grow and thrive. If I were you, I wouldn't consent to any kind of ABA or assisted living facility. I've lived at a few. I lived at Connelly House, COMHAR Rita House, various wards/rehabs, etc. It was miserable and I wanted to die. Those environments aren't conducive to pursuing an education anyway. Definitely avoid!"
      },
      {
        "id": "o88bsoz",
        "score": 3,
        "body": "i cannot live independent im am have level 2/3 autism"
      },
      {
        "id": "o88cekb",
        "score": 3,
        "body": "i donot know how to get apartrnent"
      },
      {
        "id": "o88cuym",
        "score": 3,
        "body": "I would ask the facility you're in. I would say, \"I do not consent to ABA or assisted living. I want my own apartment and a supportive room mate type care giver. How do I get that?\" You deserve privacy and as much freedom as possible. I want you to live somewhere good that won't hold back your development. I don't care if I don't know you. I want this for pretty much everyone. :)"
      },
      {
        "id": "o88c1uc",
        "score": 2,
        "body": "I understand that but you deserve to live somewhere nice regardless. You can't get a \"supportive room mate\"? It's like a care giver that's there 24/7."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rfiwq1",
    "title": "Tired of being tired",
    "body": "I'm sure everyone here can relate so this is more of a vent or a rant of emotions I just can't talk to anyone in my life about.\n\n  \nEveryone around me are extremely motivated and active, they all have something going on and something big planned, it seems like they can just keep going and when it comes to taking time off? They run literal marathons to relax! \n\nI've been going through some bad flairs the last few months and have been more or less confined to my room. I've had a friend recently express that I never reach out, but I am also the type that usually only texts or chats when I have positive things to say. I can't really update them on my week when my week has been nothing more than eating and sleeping, and I mean literally, I can't even cook for myself right now. I usually work in a creative industry as well so most of my friends always have something interesting going on or a cool project. I've just felt so burnt out with fatigue and brain fog, even when I start to try I just can't come up with ideas for projects. \n\n  \nI know people are outwardly attracted to people who are very motivated, I worry my friends and family are getting tired of me doing literally nothing and being sad about doing nothing. I'm just hoping this flairs ends soon so I can go back to being more like myself and not fall into a depressed cabin-fevered version Im feeling right now.\n\n  \nJust screaming into the void right now as I doomscroll LinkedIn for remote jobs I can do from bed...",
    "flair": "Rant",
    "score": 17,
    "comment_count": 3,
    "created_at": "2026-02-26T18:56:25+00:00",
    "top_comments": [
      {
        "id": "o8p8us1",
        "score": 1,
        "body": "I\u2019m sorry. I can relate to this. Not sure what you ailments you suffer from but flareups is common word for me. I suffered 2 major flares last year and my body has not been the same since. The fatigue is debilitating and the brain fog just makes me feel inadequate in the work space now as my processing speed has drastically slowed down. I used to be a huge solo traveler. Lived all over the world. Had a job lined up to live in Antarctica for 6 months and then this all happened. Knowing that my disability was an instant disqualification is a hard reality to swallow. Just know you\u2019re not alone. We suffer, but we also persevere. Also, be easy on yourself. Sometimes our own expectations are the heaviest to carry. "
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rfi6a2",
    "title": "Bedding for sweats",
    "body": "Hi all!\n\nSo one of my conditions and two of my meds have sweating as a side effect. I can be cold and still sweating. Two of my conditions have problems with temperature regulation as a symptom. The cold worsens some of my pain, so I sometimes have to wear a blanket even when I'm sweating so I'm not in agony.\n\nMy main sweating issue when I'm lying down is my back & neck. I have a cooling blanket and have tried having that under my back while covering myself in a warm blanket, but the cooling blanket still gets sweaty. I've tried bedding that's meant to be sweat proof but I still drench that. \n\nDoes anyone have any ideas for something that will stay dry/comfortable despite me sweating all the time, please?\n\nMy legs are also sweaty but I have to keep my knees and sometimes shins warm to reduce my pain. I also need a pillow under/between my knees to keep them in a lower pain position. So that pillow gets drenched too. I can't imagine a solution to this but just in case the hive mind has anything available, I thought I'd share. \n\nThank you!",
    "flair": "Question",
    "score": 8,
    "comment_count": 9,
    "created_at": "2026-02-26T18:29:43+00:00",
    "top_comments": [
      {
        "id": "o7klgrv",
        "score": 7,
        "body": "What kind of fabric are you using? You need to use breathable fabrics - and bambo, lyocell, and viscose, tencel types aren't as breathable as \"real\" natural fabrics and are washed with a ton of chemicals. Linen is king when it comes to breathability."
      },
      {
        "id": "o7kchw5",
        "score": 5,
        "body": "We have really enjoyed our PeachSkin Sheets. My partner and I both have temperature intolerance issues and deal with night sweats. These sheets have had zero issues with this\u2014 plus, they\u2019re not too hot and don\u2019t contribute to our existing struggles. Liked them so much we have multiple sets, lol. They wash and dry very well (super quick on the dry) and have held up for 5+ years with weekly washing, animals jumping on the bed, tossing and turning, etc."
      },
      {
        "id": "o7ktees",
        "score": 5,
        "body": "The cooling blanket is a satin feel, it does cool me down if I put it on top of me when I'm hot but it gets wet with sweat. My usual sheets are a soft cotton/polyester blend. \n\n\n\nUnfortunately I have allodynia so I have to have my arms on a soft fabric, but maybe I can have strategically placed linen or just softer fabric pillowcases to rest my arms on. \n\n\n\n\n\nI'm going to need a Frankenstein's bedding situation to handle my competing body tantrums!"
      },
      {
        "id": "o7kuj5y",
        "score": 4,
        "body": "Don't use polyester go with a 200-400 thread count cotton the blends make it worse"
      },
      {
        "id": "o7kh3l9",
        "score": 3,
        "body": " No BUT. I put my dogs chill pad down by my feet and keeping them cool stops me from sweating"
      },
      {
        "id": "o7lz4qj",
        "score": 3,
        "body": "Lambs wool is supposed to be good at cooling and moisture wicking. \n\nSomething like this might be an option to try - https://adaptawear.com/shop/healthcare/lambswool-fleece/."
      },
      {
        "id": "o7maq4p",
        "score": 2,
        "body": "This might sound weird but have you considered sticking reusable incontinence pads under your top sheet? Might help with it being wet through if it's a wicking fabric cos it'll absorb into the pad below.\u00a0\n\n\nNot to draw a rude comparison but I use these pads with a fleece layer sewn on top for my pets. Even though they urinate on them, the urine is wicked down through the fleece and absorbed into the pad, so they don't feel damp to the touch and it controls the smell a bit. Fleece specifically might be a bad call re: not making you sweat more; I think wool is also moisture wicking if you were to try that."
      },
      {
        "id": "o7ktt44",
        "score": 2,
        "body": "Thank you!"
      },
      {
        "id": "o7ktqkz",
        "score": 1,
        "body": "I sweat even when I'm cold, unfortunately. Might be a plan for when I'm hot and one of my cats wants their comfort blanket on my chest for a cuddle nap. Like a temperature lasagna with cool for me and warmth for them!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rfg1r5",
    "title": "Lil vent I need off my chest rn",
    "body": "Why am I getting worse? Now I don't know who I am but I can't even feel what other things are. Like they never felt real enough but now, there's no way to explain. Like wtf is chocolate anymore? What is a flavor again?\n\nI don't wanna reach the point where I can't see and can't feel my limbs anymore again. Make it stop.\n\nToday they had to inject me iron but of course I couldn't go so. Like. It's a closed cycle: I need things I can only get in a hospital but I can't go to a hospital because I need those things. And you don't get an ambulance for just anything and taxis don't take you places that are \"too close\" either IS MY LIFE A JOKE? Lol",
    "flair": "Rant",
    "score": 4,
    "comment_count": 0,
    "created_at": "2026-02-26T17:14:02+00:00",
    "top_comments": []
  },
  {
    "subreddit": "disability",
    "id": "1rffcjo",
    "title": "I've been unable to do as much since my spinal fusion, my parents and their friends think I'm an entitled oversensitive little snowflake.",
    "body": "My post got removed from an advice subreddit because apparently it wasn't acceptable, but I really need some help with this, and I don't have anywhere else to go, so I'll try here instead.\n\nI (23F) am disabled, on state income, and live with my parents because of it. I apologize if this post is all over the place, I'm trying my best to include all the details.\n\nI found out I'm getting underpaid for what I'm supposed to be doing, and for my medical conditions, I might be pushing myself too far, but that doesn't matter. My Step Dad is telling me that I need to get a job, despite the fact that he knows I am legally disabled and get income from the state because of it. I'm on SSI, not SSDI\n\nI've been officially diagnosed with ADHD (attention deficit hyperactivity disorder),  \nAsthma,  \nDepression,  \nAutism,  \nPOTS (postural orthostatic tachycardia syndrome),  \nEhlers-Danlos syndrome,  \nScoliosis,  \nAnxiety,  \nAcid reflux,  \nIrritable bowel syndrome,  \nand Sleep apnea.\n\nMy Mom says ADHD was a misdiagnosis and that I really have ADD. I've had a spinal fusion surgery to treat my scoliosis, and I'm fused from T3 to L3, which is nearly my entire spine. My mom also says that the doctor was wrong about the Sleep Apnea.\n\nI even got in trouble for googling jobs in my area, because apparently that means I wasn't even trying... but I've never even looked for a job before because everyone told me I'd never be able to have one... how am I supposed to know how this works?\n\nI can't afford to live on my own, because I only get $550 a month, and my step dad gets $366 of it for rent and phone. I also have to pay for a third of the food and litter, despite only having one cat to my name, who is my ESA, and she's not even the one in my room. The two cats in my room were dumped in there by my mom, because they didn't get along with the others. There's only two litter pans for the rest to share. There are 11 more cats in the house! And that's not even counting the three newborn kittens! There are a TON of outdoor strays as well. Because of this, the 5 males make messes CONSTANTLY. One of those males is in my room. And one of the others is unfixed. There's an unfixed female in my room, and two more in the rest of the house.\n\nThe rest of my bills are covered by these tasks: sweep all rooms  \nmop all rooms  \nclean stove  \nclean counters  \nclean sink  \nwash/dry/put away dishes  \ndust furniture  \ndust ceiling fans  \nwash/dry/put away laundry  \nclean dining table  \nclean pet messes as needed  \ntake out all trash  \nclean bathroom  \nkeep my AC clean  \ncarry out compost  \nclean litter pan twice daily  \nwalk dog  \nfeed chickens and turkey  \nclean chickens' water  \ngather eggs  \nclean coop  \nfeed dog  \nfeed indoor cats  \nfeed outdoor cats  \nhelp keep pet water clean and full  \nhelp with garden  \nhelp clean porch  \nhelp prepare meals  \nhelp fill and carry in water  \nput up leftovers  \nset up coffee pot  \nroll cigarettes\n\nA normal person doing all of this would receive over $1000 a month, but I only get coverage for $418 in bills, AND I bailed mom and my step dad out of the lawn bill this month, which was another $120!\n\nI'm doing the best I can, but it's never good enough. I don't have a job soon, I'm getting kicked out, because I don't do things good enough. And mom told me this morning that she got kicked out too. She has somewhere she can go, but I don't... I keep asking people if they'll take to a homeless shelter, but they just say I'm exaggerating, and things will calm down... BUT THEY DON'T! I don't know what I can even do...\n\nmom just got mad again because she HAD to give me my money from the state... SHE'S the one that decided to have them deposit it in HER account! I'm scared. I've even thought about doing something to make them \"take me out of the picture\" if you know what I mean...\n\nEveryone thinks I'm just lazy even though I'm working myself past my limit. Maybe I am just a spoiled brat... I don't know how to fix this.\n\nMom said she was fine with me before my surgery, but I got worse after. I, meanwhile, don't even see a difference, other than her adding to the list and me being unable to keep up. A while back, she tried to help me see if I qualified for help to be on my own, but she said it was too much of a headache for such little assistance. I thought that meant I didn't qualify for anything. I'm in Texas, in the USA if that helps. She has my birth certificate and Social Security\u00a0card because she says I can't be trusted with it. I at least have my state ID though, but I don't have a car or a driver's license.\n\nAlso, mom just decided to go behind me on her own accord and sweep, mop, and completely scrub the floors, and said she'd request payment for it... I didn't hire her for the job though... what she did, I normally only get paid almost $14, rounded up to the nearest dollar would be that amount, FOR THE WHOLE MONTH! If I pay her $14 for today, I'm being generous! And I'll only give her a twenty because I need $6 in change so I can pay my step dad the exact amount needed for my phone.\n\nAm I an entitled oversensitive little snowflake like my parents and their friends think I am? If not, is there anything I can do to make them understand?\n\nEdit: I forgot to mention that I'm on Nortriptyline, Hydroxyzine, Oxcarbazepine, Clonidine, and the Depo Shot.",
    "flair": null,
    "score": 50,
    "comment_count": 69,
    "created_at": "2026-02-26T16:48:47+00:00",
    "top_comments": [
      {
        "id": "o7ksyrc",
        "score": 72,
        "body": "This is abuse, they are taking advantage of you and your benefits (not to mention that\u2019s a lot of cats they have you paying for). Could you get in contact with a social worker? Try calling 211, they often can point you in the direction of local resources."
      },
      {
        "id": "o7jxa7p",
        "score": 70,
        "body": "In regards to your mom saying that the ADHD is a misdiagnosis, and that you actually have ADD, they're the same condition, just different presentations. Ever since the DSM-5 got released in 2013, ADD is now \"ADHD inattentive subtype\" and you don't really get an \"ADD\" diagnosis anymore. \n\nTldr: she's wrong, and it's easy to prove"
      },
      {
        "id": "o7k77xn",
        "score": 54,
        "body": "your mom is an idiot. ADHD and ADD are the same thing. The DSM dropped the H for hyperactivity at one point and then brought it back. It\u2019s also not just hyper as in constant energy and movement, but also as in constant thoughts and ruminations. \n\nthey can\u2019t be \u201cwrong\u201d about sleep apnea when you were hooked up to dozens of sensors and monitored overnight. You can misinterpret those findings.\n\nso, bottom line, you are being abused financially. If I were you, I\u2019d be calling Adult Protective Services and asking for their help in getting out of there. There ARE facilities, room rentals in group homes, and section 8 vouchers that you would qualify for (and probably on an emergency basis). APS can help."
      },
      {
        "id": "o7l3mf0",
        "score": 53,
        "body": "Please call adult protective services and also look for resources to get your own bank account and money deposited in your bank account not hers"
      },
      {
        "id": "o7lvcuk",
        "score": 25,
        "body": "If they are withholding your SSI funds from you, that\u2019s illegal and you might consider calling Adult Protective Services. Or perhaps an abuse hotline. There might be nonprofit services in your area that can help you find roomates and affordable housing where you will be free from your parents demands. \n\nAlternatively, you might want to call animal protective service because 11 cats + a bunch of kittens isn\u2019t sustainable. All the cats need to be trapped, neutered, and released to lessen the flow of incoming kittens. \n\nEven if you don\u2019t want to get anyone in trouble, calling an abuse hotline might be therapeutic and they\u2019d be better equipped to offer advice or counsel on what next steps you\u2019d need to take, or could take, if any.\n\nhttps://www.dfps.texas.gov/Contact_Us/hotlines.asp"
      },
      {
        "id": "o7lmy3y",
        "score": 16,
        "body": "Agree with the above.   Your situation with your family is NOT normal and you\u2019re right to want out.   This is exactly the sort of thing APS is for and can help with all the roadblocks you face."
      },
      {
        "id": "o7jlx7e",
        "score": 15,
        "body": "my family thinks im faking it too, despite watching me limp in pain and seeing how many doctors appointments im going to. my stuff is definitely not on par with you but it sounds like financial abuse. if ur able to do all the chores listed i dont think its a bad idea for you to maybe look for a group home with other disabled folks in your area. call your local resource number and see whats around you in terms of resources for you. at least ur money will be towards rent and not people who nag you and belittle you all day. whatevers left over you can use or save for yourself. im sorry youre treated this way OP. get any assistance you can qualify for. thats what its there for"
      },
      {
        "id": "o7mhk70",
        "score": 10,
        "body": "You are being abused. Please get in touch with adult protective services and animal rescue services. Like right now."
      },
      {
        "id": "o7lnf15",
        "score": 9,
        "body": "Hold on\u2026. WHAT? Your parents take your disability aid even thought you\u2019re of legal age?? \n\nYou\u2019re already doing the chores, isn\u2019t that enough for covering the expenses?\n\nHow do you manage to clean everything for a full household with your spinal disabilities? I can\u2019t even wash the floor without crying from pain after a while"
      },
      {
        "id": "o7lidw1",
        "score": 9,
        "body": "Just the situation with the number of cats and limited litter is enough to warrant a call to APS.  I can help if you tell us your location."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rfcwax",
    "title": "Disabled and polyam people\u2019s perspectives needed\u2026 \ud83e\udd72 Am I being fair to feel hurt by my queer platonic partner?",
    "body": "I am sorry the post is very long and my thoughts are all over the place. I am struggling with naming exactly what my feelings are towards my partner Aspen right now, so writing this post is also serving as me trying to comb through my thoughts. I\u2019m sorry if any of these details doesn\u2019t make sense.\n\nFirst, for context, I (32NB they/them) have ASD and ADHD. My queer platonic partner Aspen (32NB he/they) is visibly disabled (wheelchair or other mobility aids needed outside of home), and they have Bipolar, PTSD, ASD, ADHD, Narcolepsy and various learning disabilities. I also have a nesting romantic partner Birch (37M) who has DID and CPTSD. There is also Cedar (31F), who is best friends with Aspen and me, also another AuDHDer. We are all foreigners living in Tokyo, Japan. Birch and I are from Taiwan, while Aspen and Cedar are from the US. Aspen is the only one in school now because he had never gotten a degree due to his disabilities, needing an environment to learn Japanese, as well as just having a legitimate way to stay as a resident.\n\nSo, yesterday, Aspen suddenly informed me, via texting while I\u2019m at work, that they\u2019ve made a decision and would be moving back to the US soon, without ever mentioning this thought to me before it apparently becomes a decision. I did feel happy for them to make an important decision for themself, and there are definitely things that I can see would make them happier and would\u2019ve support their decision regardless. However, I am also having complex feelings towards having this whole thing completely blindsided me and am now doubting our entire relationship and dynamics.\n\nAspen and I are both on the asexual spectrum (me demi, Aspen grey). I first met him at a craft meetup about two years ago when they were in Japan on a tourist visa for 3 months. I started following them on social media immediately because I really like them as a person, and would love to stay connected. They did not remember me at all and they considered our relationship started only when we met again early in 2025 at a queer art event, introduced by a mutual friend from the same craft meetup group. We enjoyed each other\u2019s company very much and were soon spending a lot of time together, often with another nerdy crafty friend Cedar. We spends so much time together and so closely that Aspen jokingly calls us a platonic throuple sometimes. To clarify, we use BFF for Cedar when it\u2019s serious, because she doesn\u2019t like being called a partner as an aroace person, as the word carries a romantic vibe to her (and to be fair, to most people who don\u2019t understand aces).\n\nCedar and I both live more than 1 hour of public transportation away from Aspen, in direct opposite directions. Since Aspen is the most physically disabled of us three, Cedar and I almost always travel to their place to hangout or near it. Aspen also never makes plans. He would tells us he wants to see us, and Cedar and I would make the plans to meet them, sometimes even when Aspen couldn\u2019t give us a firm schedule or confirmation to the plans. I took several paid leaves (and anyone knowing Japan work culture would know how little we have those) to help take Aspen to do city hall and/or medical visits.\n\nCedar and I always check for accessibility even without reminders from Aspen (they still would ask since most ppl need the reminders). We try to be as flexible as we can and make all our plans around the time and places Aspen prefers. Cedar or I also need to make all the small decisions when we go out, together or separately with Aspen, because they struggles the most with making decisions. Noticed I used the word \u201cmost?\u201d That\u2019s because we all struggle with making small everyday decisions, but Cedar and I take on the extra labor in turns if we go out with Aspen.\n\nBeing crafty queer AuDHDers, we have a LOT of overlapped interests and hobbies all over, though I feel like Aspen and I have more in common due to some interesting culture backgrounds. (Idrk, I have started to doubt that maybe it was just me thinking about that one-sidedly.) I went to see a few shows/concerts of his favourite artists with him, though one of those they canceled on me on the night, while I was already halfway to the venue after work, because they were physically in too much pain. I was already excited, so I still enjoyed the show and didn\u2019t mind at the time. Similar situations happened many times throughout our whole 10 months together, whether it was a platonic date with me or other social/queer events with others. I don\u2019t keep a count because I genuinely understand that things happen in life and they already have less mental or physical energy.\n\nI love both Aspen and Cedar but I have a deeper connection with Aspen, which was why I agreed to use the label of queer platonic partners when he asked like 3 months ago, since I did see that we have essentially been dating platonically. Also we started talking about future with each other in the pictures, so it felt natural. We even have similar dreams of opening a specific kind of small business and were started planning our lives together so we can do that.\n\nThis is where Birch comes in. He was the one who kept seeing how much I changed in the past year despite him not being a part of it directly, and he saw how important my connections with them, especially Aspen, are to me. He made time (despite working 6 days a week in the Japanese food industry) to start occasionally hangout with Aspen. He also started to plan his future with Aspen in the picture, as he can easily see where the direction we were heading.\n\nAspen\u2019s parents are wealthy enough and willing to invest in our business, as they do hope Aspen can have a stable and self-sufficient life after all, as ling as we can present a concrete business plan with exit strategies. Scratch that, we can prepare the plan, but Aspen has to be the one to present it or his father aren\u2019t green light anything. Yet Aspen hasn\u2019t been able to deliver it, and without the urgency Birch and I were under the impression for. For you see, Japan has been raising all standards and introducing new costs for future visas applications in the past few months. Also, Aspen having repeatedly stated how he wants to make Japan his forever home and can never go back to the US now as they couldn\u2019t risk their safety as a trans person with a X gender marker. These two details are especially important because Aspen was struggling to keep up with the work load required for a full time student as a disabled person. But without at least a diploma degree, it\u2019s near impossible for them to find a job and stay in Japan as a visibly queer and disabled foreigner.\n\nBirch was especially working hard through the network of local connections of other small business owners in our city, even getting a couple of Japanese friends who would be interested to work for our business in the near future. He also worked really hard everyday after his regular work to just help us make business plans and such, especially with how bad in general as Aspen and I are with making realistic plans. At least I had a business degree and also working in the IT industry now, so I help with the more technical and theoretical aspects while Birch deal with the realistic stuff. What was Aspen doing? School, mostly, and having a hard time catching up. But for our business plan? Just \u201ctalking about\u201d hiring an immigration lawyer for consultation and a friend to do market research, also \u201cemailing\u201d related businesses out of the blue (with no private connections) about the information of the industry we are trying to get in. They didn\u2019t even open up and read any of the updated business plan beyond the first draft.\n\nI know they are talented and creative and capable. We already took on the extra loads of everything Aspen outright said he couldn\u2019t handle. This is why Birch have been getting more frustrated with the progress because they aren\u2019t even doing the parts they believe they could do. I have been trying but communication was becoming very hard when Birch worked till late at night while Aspen is an early sleeper, but Aspen also doesn\u2019t really take the time to read everything Birch writes carefully and I just got blindsided and realized that it hasn\u2019t actually registered in Aspen\u2019s head how much extra unpaid labor Birch and I have already put into our future.\n\nNow they had just decided to up and go without any prior warning, and in contrary to whatever they have been telling me in the past year, I just feel a little lost and sad in a very numb way for what I thought we have, but a lot more angry for Birch, who has avoided mentioning Aspen at all since yesterday and I know is rightfully pissed and feels disrespected by them. We were originally supposed to go out to a one day trip together this weekend, and I don\u2019t think it\u2019s happening anymore.\n\nThe problem I have right now is, I haven\u2019t communicated anything except the initial supportive replies to Aspen because I was at work and wasn\u2019t sure why I was happy for them but \u201cI\u201d also wasn\u2019t feeling happy. Was I (and Birch in relation to me) taken advantage of the whole time, even if unintentionally? How should I proceed from here? We wouldn\u2019t have been working so urgently on this plan if it weren\u2019t to help Aspen staying and avoiding going back to the US, as Birch and I have no trouble maintaining our own work visas to stay as residents\u2026\n\nAm I even an ableist or am I gaslighting myself to believe Aspen capable of doing most things they had assured me to be able to do? Do I have the right to feel hurt and disappointed when I couldn\u2019t see any effort put into what I thought was our future together, not consulted with such major life decision, and anger for Birch to have stayed up so many nights and used what were supposed to be his rest days only to be disrespected like this?\n\nHow do I approach the conversation to address my feelings and without hurting Aspen unnecessarily or evensend them into a depression episode when he is so happy about going back to maybe NYC or Philly\u2026 \ud83e\udd72",
    "flair": "Discussion",
    "score": 0,
    "comment_count": 19,
    "created_at": "2026-02-26T15:19:20+00:00",
    "top_comments": [
      {
        "id": "o7j2nox",
        "score": 52,
        "body": "...ohhhhhhhh kay...\n\nSo much of this is irrelevant.  Like SO much, and I say that as a disabled queer woman who's bi/poly/demi.  Like, almost all of it.\n\nThese two paragraphs, these are what's relevant: \n\n>\"The problem I have right now is, I haven\u2019t communicated anything except the initial supportive replies to Aspen because I was at work and wasn\u2019t sure why I was happy for them but \u201cI\u201d also wasn\u2019t feeling happy. Was I (and Birch in relation to me) taken advantage of the whole time, even if unintentionally? How should I proceed from here? We wouldn\u2019t have been working so urgently on this plan if it weren\u2019t to help Aspen staying and avoiding going back to the US, as Birch and I have no trouble maintaining our own work visas to stay as residents\u2026\n\n>Am I even an ableist or am I gaslighting myself to believe Aspen capable of doing most things they had assured me to be able to do? Do I have the right to feel hurt and disappointed when I couldn\u2019t see any effort put into what I thought was our future together, not consulted with such major life decision, and anger for Birch to have stayed up so many nights and used what were supposed to be his rest days only to be disrespected like this?\"\n\nY'all need to sit down together, all of you, and have an open and honest conversation about recalculating expectations and responsibilities, and what this move is going to mean for all four of you, your relationships, and your financial situations.  You're not wrong to feel hurt and disappointed, and if Aspen feels hurt and depressed over your reaction, that is the logical consequence of their actions--people don't get to unilaterally change things and then not understand that it's going to effect others, which in turn effects them.  That's it, period, take the disability, gender, sexuality, etc., out of it.  Your relationship partner did something that hurt you and drastically changed the relationship, without consulting you, and you need to talk to them about it."
      },
      {
        "id": "o7l91k8",
        "score": 26,
        "body": "I am disabled. I am polyamourous. My honest opinion is that you all sound like you are varying degrees of insufferable."
      },
      {
        "id": "o7mas4t",
        "score": 10,
        "body": "And you know what thats super fair"
      },
      {
        "id": "o7jkx8k",
        "score": 7,
        "body": "You are not responsible for Aspen\u2019s wellbeing legally right?"
      },
      {
        "id": "o7js6w9",
        "score": 7,
        "body": "Sometimes partners make decisions that aren\u2019t well communicated and sometimes expectations weren\u2019t well communicated. You guys are all foreigners living in a big city- the likelihood that one of you would eventually move for work or to be near family or something is very high. Was \u201cwe will live together\u201d or \u201cwe will discuss major life changes\u201d part of the the expectations you set? Those things and ppl being on different pages or making assumptions is hard for traditional couples too. You feel like your trust was violated when they didn\u2019t act as you expected, repairing that will take a lot of open conversation on both sides."
      },
      {
        "id": "o7ocl58",
        "score": 6,
        "body": "This honestly reads like you feel entitled to your partner\u2019s proximity and their parent\u2019s money because you were a supportive and accommodating friend and partner. \n\nIt\u2019s been three months.  That\u2019s not long enough to truly rely on any type of relationship to last forever, no matter your shared/stated goals/intentions, especially when you\u2019re all temporary immigrants from different countries\u2026"
      },
      {
        "id": "o7mxzf3",
        "score": 6,
        "body": "As a queer disabled person, I really wish I could be more helpful, but I\u2019m so fuzzy tonight all I got was, \u201cthey\u2019re all trees, growing together in unique ways, oh aspen decided to leave the trees.\u201d \n\nSo my brain is absolute mush, and I\u2019m sorry the trees (I know you\u2019re all people , but now I\u2019m enjoying the metaphor) are sad. Hopefully the roots can still find a way to communicate, even if they cannot be close together."
      },
      {
        "id": "o7mafen",
        "score": 5,
        "body": "As Aspen run a business before? What's he studying in school? I think he's realizing he's not cut out for the business life and doesn't want to admit it to you all."
      },
      {
        "id": "o7j6ncf",
        "score": 4,
        "body": "Thank you.\n\nI know it\u2019s all over the place. I guess i really should\u2019ve deleted everything else out once i combed through thoughts and wrote down those last few paragraphs. Sorry for the unnecessary long rant of my brain vomit.\n\nThanks for the really helpful advice. Yeah, we really need to find a suitable time to all talk in person."
      },
      {
        "id": "o7m02k0",
        "score": 4,
        "body": "Sometimes so grateful to be ace."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rf4818",
    "title": "Do you name your disability, or do you just say \u201cmy disability?\u201d",
    "body": "If it ever comes up in conversation (like why you can\u2019t do something, or have trouble doing it), do you specify what you have, or do you just keep it to yourself?\n\nThis goes for people with both visible and invisible disabilities.\n\nI used to be very open in the past, but in the past few years I\u2019ve become more private with it outside of friends, people with medical training, or fellow people who have it.  I don\u2019t exactly know why, but I guess it\u2019s starting to feel more like my business instead of the business of others.",
    "flair": "Question",
    "score": 55,
    "comment_count": 75,
    "created_at": "2026-02-26T07:53:55+00:00",
    "top_comments": [
      {
        "id": "o7idt8f",
        "score": 27,
        "body": "I have a long list of conditions that cause various symptoms often from the combination so it\u2019s easier to just say \u201cmy disability\u201d unless it\u2019s a symptom that is clearly linked to one specific medical condition.\nIt also depends on who I\u2019m talking to, if it\u2019s someone I don\u2019t know well then it\u2019s unlikely I\u2019ll give them specifics."
      },
      {
        "id": "o7hajhx",
        "score": 16,
        "body": "I just call it my disability. "
      },
      {
        "id": "o7hck6u",
        "score": 11,
        "body": "Because \"my disability\" is comprised of multiple conditions, I usually just bundle the issue into an umbrella term.\n\n\"sorry, I can't eat that because of my digestive issues. I brought my own food\", or \"can I please be allowed to sit down as an accommodation for my musculoskeletal condition?\"\n\nAmong a few minor common comorbidites, I have ClEDS, CMTD, vascular TOS, carotid FMD, a complex migraine syndrome and I'm autistic. So many of those conditions overlap, and cause similar symptoms, dysfunction and therefore create the same limitations.\n\n\"can we dim the lights? The brightness is bothering me\" could be because of my migraines, the vascular vision loss associated with the FMD, or my autism, so it's hard to add a quick \"because of my [condition]\"\n\n\"The nerves in my legs are playing up so I'm bringing my crutches today\" could be because of the CMTD, the migraine syndrome, or a subluxation from the ClEDS.\n\nSometimes even I don't know which of my various diagnoses are contributing to a symptom.\n\nMost of my disabilities are mild and not in themselves limiting, yes I have to do things a little differently but if it wasn't for the combination of conditions I wouldn't need to say \"sorry I can't do that because I have [*example*] condition\" very often."
      },
      {
        "id": "o7hrcxf",
        "score": 9,
        "body": "I usually don\u2019t name my chronic illness.  If I use one name, people have a preconceived notion of what it is that does not match my experiences, if I say another name it\u2019s just total confusion, even from medical professionals.  I will name my autism if I\u2019m talking about it."
      },
      {
        "id": "o7iyzvw",
        "score": 8,
        "body": "Yeah, this is it for me, too. Whenever I have to list them all off, I probably look [like this.](https://gatherer.wizards.com/JMP/en-us/10/bruvac-the-grandiloquent)"
      },
      {
        "id": "o7i31ci",
        "score": 6,
        "body": "I have a combination of chronic illnesses and issues so bundling it together as \"my disability\" or just saying chronic illness makes it a bit easier and also makes me feel less weird than when I'm revealing my alphabet soup of official diagnoses"
      },
      {
        "id": "o7i43kv",
        "score": 6,
        "body": "I used to say I have a rare neurological condition but I have since developed other issues. Now I say health issues but I think I am finally ready to use disability."
      },
      {
        "id": "o7hcb8q",
        "score": 6,
        "body": "I don't really have a convenient label that encompasses things neatly, at least at this point, so I'll usually name a particular symptom like my fatigue or my chronic pain or sometimes just phrase it as \"my body being uncooperative\" if it's not easy to concisely describe"
      },
      {
        "id": "o7hvlmi",
        "score": 5,
        "body": "This is so real. People whose cousin's friend's aunt's groundskeeper's dog has scoliosis (or whatever else) think they're informed enough on scoliosis to make assumptions."
      },
      {
        "id": "o7kjtj9",
        "score": 5,
        "body": "I really feel this. If I say I have ME/CFS nobody knows what that is, but if I say I have chronic fatigue syndrome everyone assumes I'm just kinda tired and not, yknow, disabled by issues affecting my entire body \ud83e\udee0"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rf1nge",
    "title": "Dude, I got denied AGAIN.",
    "body": "I literally cannot walk, im getting an entire hip replacement in May, my knee dislocates while I sit down (I need a meniscus repair)(a knee surgery will happen after my hip heals), I also have a buldged disc in my back and a shoulder impingement that needs surgery.\n\nIve been denied 3 times and haven't been working since last September. If I didn't have family id be homeless or in a nursing home because im bed bound. \n\nThe fuck. \n\nAlso my doctor reccomend I get on disability.\n\n I expected them to deny me because the Social Security system is extremely unreliable with their decision making. But I'm just extremely suprised, and I hope they give me a thorough explanation. \n\nI really believed the judge was being sympathetic, usually my judgement on people is accurate. But I was wrong :(. Definitely I'll go bankrupt now.\n\n\nThanks everyone's for replying. It reminds me this cruxification has been embodied by all of you. And thank you for your paitence. ",
    "flair": null,
    "score": 93,
    "comment_count": 67,
    "created_at": "2026-02-26T05:26:11+00:00",
    "top_comments": [
      {
        "id": "o7gulvl",
        "score": 25,
        "body": "Yeah. He had 1 question during my hearing for me. Provided no other guidance.\n\nI wonder if there is a way to prove my attorney was not sending over my medical records, or something."
      },
      {
        "id": "o7ivg1i",
        "score": 23,
        "body": "My partner was denied four times before they got it and they still messed up with giving them SSDI vs SSI. They have virtually no work history, or income. They\u2019ve been disabled since 2023, and approved this last December. \n\nThe system isn\u2019t built for people who are disabled. Unfortunately you have to be your biggest advocate even when you\u2019re struggling. \n\nHowever, your lawyer should have records of everything and you should just be able to request them. You hired them, they work for you."
      },
      {
        "id": "o7gu5i7",
        "score": 23,
        "body": "Did you get a lawyer?"
      },
      {
        "id": "o7ldbg1",
        "score": 19,
        "body": "I once knew someone with an amputated arm and multiple other complex injuries they were never going to recover from fully. They got denied twice, as well. It's not just you, it's the way the system is designed, so that we give up and stop fighting for the rights we deserve."
      },
      {
        "id": "o7jqewl",
        "score": 13,
        "body": "I tried my hardest my friend. Tried to get everyone to read Project 2025 before voting. There's still hope that the adults will stand up and stop them but so far nobody seems to be willing. It's not even really Trump that we need to worry about, the real people behind Project 2025 are in JD Vance's billionaire tech world. They are already sitting in cushy administration appointments ready to roll it all out with or without Trump."
      },
      {
        "id": "o7jjcbs",
        "score": 10,
        "body": "Sadly, this is the worst time in the history of America's SS system. Project 2025s ultimate goal is to get rid of it. The government has downsized everything about the department, fired thousands of workers and is slow walking the application process more than ever before. I'm just waiting for the announcement of when payments to current recipients will be stopping so I don't have a lot of hope for us."
      },
      {
        "id": "o7n49tz",
        "score": 9,
        "body": "I hate saying it,\u00a0 but you are probably being denied because your issues can be repaired with surgery and in their mind can be all repaired and have you back in shape to work within a year. All of your issues have to keep you from substantial gainful activity for at least 12 months or they will result in death.\u00a0 Did your attorney tell you that?\u00a0\u00a0"
      },
      {
        "id": "o7nd3s6",
        "score": 8,
        "body": "yeah it is insane. it's been denied since 01/23/2025"
      },
      {
        "id": "o7j4e5w",
        "score": 7,
        "body": "I got denied. I have hemiplegia and I\u2019m enraged. Lawyers haven\u2019t helped my case for shit."
      },
      {
        "id": "o7pz1fx",
        "score": 7,
        "body": "Honestly I'd suggest talking to another lawyer if this is the case. I have a friend who had to switch firms to get approved."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1reyhj2",
    "title": "If you could have any one accommodation from fiction to make your IRL life-better, what would it be?",
    "body": "Hey!\n\nSo I have pretty bad adhd on top of my other disabilities and am very prone to fantasizing about things I can\u2019t have which in turn makes me prone to impulse spending. Lately my hubby and I turned it around into a game where we can fantasize/imagine together about things that are squarely in the realm of fiction so there\u2019s no anxiety about money in any way shape or form.\n\nSo recently our game was \u201cfantasy weapon loadout\u201d and one of my chosen weapons was Mjlonir because when  Jane Foster wields it, she\u2019s impervious to all her cancer symptoms and chemotherapy side-effects, which I figure means I\u2019d be temporarily impervious to my fibromyalgia symptoms, which would be pretty spiffy.\n\nBut when I really think about it, the MCU tech that would help me the most is probably JARVIS. If I had an intelligent, voice activated super-computer that knew me personally, was present everywhere (but not owned by some \\*other\\* creepy billionaire like\u2026 maybe I\u2019d be okay with  Shuri owning it. Definitely not Tony). The way that would help my adhd symptoms is next level. Honestly, I might be as successful as Tony Stark if I had a Jarvis to pester me into doing things on time and never forgetting bills or over spending. Not to mention the brainstorming sessions.\n\n(Also please don\u2019t let this devolve into a convo about current real world AI. It\u2019s not there yet even if it were ethical and that just upsets me more than it helps. )\n\nAnyway, we all have different diagnoses (or lack thereof), different symptoms, different noses, different brains, different needs; what fantasy/ science-if/ fiction thing would make your life so much better and why?\n\nEDIT: that was meant to say \u201cbodies,\u201d not noses, though both are true so I guess autocorrect is not incorrect even though it\u2019s wrong.",
    "flair": null,
    "score": 4,
    "comment_count": 19,
    "created_at": "2026-02-26T02:52:30+00:00",
    "top_comments": [
      {
        "id": "o7lm2s5",
        "score": 4,
        "body": "Uploading my consciousness into the internet so I could still exist and communicate and learn and do whatever I want, go wherever I want, and see anything I want without having to deal with things like body stuff.  I mean, I could act like a ghost and haunt people.  I could leak documents.  I could watch any program ever made.  I could hang out with friends.  I could watch baby animals on security cams at the zoo.  I could keep an eye on those I care about and nag them to do things like take their meds.  Go to all the concerts I wants without having a seizure.  Disseminate hidden patents for things we've all been waiting for or if cures for things exist but are being bought out by Big Pharma to make money off of treatments, make those opensource.  \n\nI'd really miss having a dog and eating chocolate though, but I bet I could get someone to code me VR pets and other creature comforts like that."
      },
      {
        "id": "o7qdix9",
        "score": 3,
        "body": "Found it! Had to dig through my audiobook history on two different apps but it\u2019s called \u201cThe Infinity Courts\u201d by Akemi Dawn Bowman. Here\u2019s a link to it in the Libby app. \n\nhttps://share.libbyapp.com/title/5589557"
      },
      {
        "id": "o7gp6sz",
        "score": 2,
        "body": "Brain implant that eliminates my seizures and can let me download and remember anything/everything I want. Edit to add, definately Shuri tech."
      },
      {
        "id": "o7gy1o1",
        "score": 2,
        "body": "Its from a video game but in Detroit: Become Human, there is a mechanical arm that comes out of the wall attaches to Carl's chair and carries him down the stairs in his house.\u00a0"
      },
      {
        "id": "o7i87lp",
        "score": 2,
        "body": "probably little AI robot helpers. can't have this in the current timeline because the people in charge of these things are more worried about how they can exploit them for monetary gain or use them for military tech than actually concern themselves with making the world a better place"
      },
      {
        "id": "o7o9g5f",
        "score": 2,
        "body": "Exosuits, maybe Titanfall ones? Anything to make my muscular dystrophy a thing of the past"
      },
      {
        "id": "o7p67uq",
        "score": 2,
        "body": "This reminds me of a book I read. If I can remember what it was called I\u2019ll link it here."
      },
      {
        "id": "o7qb7an",
        "score": 2,
        "body": "That\u2019s not it but now you\u2019ve intrigued me\u2026"
      },
      {
        "id": "o7qpepn",
        "score": 2,
        "body": "You definitely should read William Gibson's Neuromancer - I recommend reading the book (and the other novels in the Sprawl trilogy if you can) before the show premiers on Apple TV+ - though the release date is still unknown.  While Gibson didn't invent the Dystopian Cypberpunk Sci-Fi genre he literally coined terms like \"Cyberspace\" and things he wrote about in his books in the 1980s became reality (memory foam mattresses for one example) - which often happens with very good sci-fi, like some of the tech from Star Trek (real-time audio translations, smart home devices, iPads...).    \n  \nEssentially though, if you like Doctor Who and remember when Missy uploaded all the deceased into a server and downloaded them into Cybermen, or if you liked the Black Mirror episode \"San Junipero\", or manga/anime like \"Ghost in the Shell\"... (the list is super long so I will stop here) - these works as well as the one you linked to are all based on William Gibson's books.  Of course Gibson could not have written without his own inspirations as well, so I'm not like a squeeing fangirl or anything.  Just that there would be no Cyberspace to upload consciousness to without the Sprawl trilogy and books like Neuromancer, which isn't even the first book written in the trilogy but it's the one everyone always suggests be read first as it definitely does the better job fleshing out the world so the reader has fewer \"why?\" questions."
      },
      {
        "id": "o7vxzrm",
        "score": 2,
        "body": "I\u2019m not a Doctor Who person tbh \u2014 I tried to get into it a while back but between the limited access in the US and some other factors it just wasn\u2019t for me. \n\nAs part of my dissertation research I studied black womens speculative fiction and I read a LOT of spec fic from women of color \u2014 I don\u2019t get as much time for other authors that fall outside of that so Inhavent read any Gibson but I\u2019ll put it on the list. :) \n\nYou should definitely check out the book I mentioned though because it\u2019s pretty much exactly what you described with a slight twist."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rey4td",
    "title": "For people who were born with their disabilities/impairments/conditions, do you feel that you haven't truly lived?",
    "body": "Around a week ago, I attended a pleasant, fun social event for an organization I'm a part of at my university. One of the activities was to make/build a stuffed animal (it was a baby horse/foal). While making the stuffed horse, one of the students there asked me if I had done a Build-A-Bear workshop before, and I said no. In response, the student said I had never lived before (I don't think he was being mean, as I had met with him before in a positive way). The rest of the social event was good, although I might have messed up one of the later activities there. However, making that stuffed horse made me wonder that as someone who was probably born neurodivergent (e.g., inattentive ADHD), I have probably missed out on important, intangible experiences in life. I am trying my hardest to advance my life, as I'm nearing completion of a bachelor's in a social science degree. I just hate this feeling of living an incomplete life, that's all. ",
    "flair": "Country-USA",
    "score": 4,
    "comment_count": 10,
    "created_at": "2026-02-26T02:36:33+00:00",
    "top_comments": [
      {
        "id": "o7geilk",
        "score": 18,
        "body": "The concept of \"truly living\" or attaining an \"acceptable\" quality of life is often defined by a society that scorns othered people, including disabled people. I was born blind and autistic. My quality of life is not limited by these conditions necessarily, but by the society and individuals therein that put up barriers that prevent me from fully participating. \n\nNot to get dark, but many nondisabled people, especially those in the medical field, think of us as having a lower quality of life than we ourselves do. This becomes a self-fulfilling prophecy; if people treat us as if our lives have no value, there will be fewer ways for us to find that value. \n\nI have never truly lived according to normate standards. That is OK. I know who I am, what I am capable of, and what I would like to achieve. The value of my life cannot be dictated by an ableist framework that would rather have me exterminated or institutionalized than include me like the whole person I am, disability identity and all.\n\nEdit: spelling"
      },
      {
        "id": "o7goqkv",
        "score": 5,
        "body": "yeah there are things that I missed out on or did late, but it's hard for me to really mourn something i never had. maybe it's just cope but I have experiences that other people my age havent, and whether they were positive or negative we still lived the same amount of time. everyone experiences a different life but a life further outside the norm can feel isolating. I dont feel like I havent lived but it is hard to relate to others sometimes. it's why I like hanging out with other disabled people. even if our disabilities are different we have similar experiences of being othered, isolated, and often having a lot of extra crap to keep track of nondisabled people would never even consider. talking about things that are my normal doesnt feel like oversharing, just sharing. idk how coherent my answer was but it's hard for me to think in straight lines lol"
      },
      {
        "id": "o7ggbsq",
        "score": 4,
        "body": "Objectively, I\u2019ve missed key living moments in life as someone born with spina bifida and confined to a wheelchair. Most of that is my own fault, maybe, some of it is due to the inherent ableist society we live in. I regret not living \u2018enough\u2019 even though I\u2019m still very young"
      },
      {
        "id": "o7hipme",
        "score": 4,
        "body": "I was born deaf but I didn\u2019t miss out due to deafness but the fact I was a child rape victim with very few psychologists who saw beyond the overt disability."
      },
      {
        "id": "o7hlibf",
        "score": 2,
        "body": "Yes."
      },
      {
        "id": "o7nwkdv",
        "score": 2,
        "body": "What *exactly* is an \u201cincomplete\u201d life? What *exact* things have you missed out on that now makes your life somehow totally invalid? I\u2019m willing to bet they actually aren\u2019t activities that are universal, and are most likely very narrow things that only a very tiny part of the population would ever touch. \n\nSomeone thinking that one of their socio-economic, cultural experiences is the most important thing there is doesnt make it true."
      },
      {
        "id": "o7pxu5d",
        "score": 2,
        "body": "It's easy to be ableist to yourself. But back up for a sec. what you're asking is does being experiencing life disabled mean that your life is inherently less valuable. The answer to that is no. Disabled people have just as many hobbies, interests, meaningful experiences, emotions and journeys as every abled person does. Comparing disabled lives against abled lives, and then deciding that disabled people must not be 'fully living', is the logic that leads to eugenics. \n\nAlso, many people, abled and disabled alike, have never been to build a bear. That's a rich people thing haha. Is everybody who has never made a build a bear living a less fulfilled life? Nope. Cause they have other hobbies. See how silly it is? \n\nThere are things you might never do because of your disability. But there are a lot of things I do that abled people will never do either. \n\nDon't beat yourself up about it. It's a silly comment."
      },
      {
        "id": "o7r8e4h",
        "score": 2,
        "body": "I don't get all the positivity in the comments honestly, my life fucking sucks because of my disability, I can't do anything, I can't even sit up in the morning, I can't even lift a bottle to drink anymore I need a straw, I can't marry and start a family, I can't take public transit, I can't go hiking, I can't ride my bike or do any of the sports I used to love, it has been over ten years of never-ending grief, it never stops no matter how much I want it to."
      },
      {
        "id": "o7kul44",
        "score": 1,
        "body": "Im 18 and I really feel this. In my first years of highschool some people laughed at me bc of my disability, so I developed some kind of fear on meeting new people outside my usual friends and bc of this, I barely met new people on my highschool years. Right now, im studying CS, trying to fix all the errors that I commited during highschool and although im not the happiest person ever, im happier than I was"
      },
      {
        "id": "o7tx44a",
        "score": 1,
        "body": "Yeah I feel so far behind. Tbh, I think if life were more accessible and livable for me I probably wouldn\u2019t be on mental health meds but, I\u2019ve pretty much accepted I won\u2019t get as much as I thought I would out of this life. I was talking with a friend who brought up \u201creincarnation \u201c I told em I hope it was actually true but, it\u2019s mostly wishful thinking. I want a do over of this life. It\u2019s whatever, I\u2019ve accepted it at this point but, it doesn\u2019t make it suck any less."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rewssj",
    "title": "I'm genuinely starting to wonder if I'm making it all up",
    "body": "I was in the ER on Friday with the worst pain I ever had in my life. I've never once cried over pain before, but I was sobbing and begging the doctors to help me. and they gave me a pain pill and sent me home, because nothing \\*seemed\\* wrong. after years of this shit, no answers not even any signs that there is actually anything wrong with me I'm starting to wonder if there even is. maybe this is just a normal amount of pain to be in on a daily basis. Maybe people are just stronger than me, and my reaction to the pain is just me being childish. I want to scream all the time from the pain I'm in. but maybe everyone does? I feel like giving up. ",
    "flair": null,
    "score": 19,
    "comment_count": 10,
    "created_at": "2026-02-26T01:37:41+00:00",
    "top_comments": [
      {
        "id": "o7fw6ho",
        "score": 9,
        "body": "Usually the er doesn\u2019t help me I have to make appointments wait for them and hopefully be pointed in the right direction. The er Dr surprised me last month I\u2019d passed out a second time that week and my husband called an ambulance while in the er I kept telling the Dr I think it\u2019s just anxiety he said no it\u2019s not it may be pots. So I saw my primary a cardiologist and I\u2019m being tested. Honestly was the first good experience I\u2019d had in the er in a long time. I\u2019ve had pain and illness 15 years the first year with interstitial cystitis I didn\u2019t have a diagnosis but I\u2019d scream and cry id go to the er crying and get no help. The pain was horrible."
      },
      {
        "id": "o7l3nsu",
        "score": 9,
        "body": "You're not making it up- the normal amount of pain a /normal/ (not disabled) person experiences all the time is zero. It takes a long time to find medical professionals that listen and are able to help, unfortunately. I'm so sorry thay happened, I hope you're able to find the help you need soon."
      },
      {
        "id": "o7ftjnq",
        "score": 7,
        "body": "No, believe your experience.  I had horrific pain one time (11/10), and went to the ER, almost unable to move.  They diagnosed me with a panic attack, because they couldn't find anything.\n\nIt was such a cop-out diagnosis; I wasn't even anxious, my mind was peaceful the whole time (had spent the week before meditating with my Buddhist teacher).  I\n\nhonestly didn't know how to react when they handed me the literature saying it was a panic attack - I've just been through hell, and you're telling me it was panic.  Right...\n\nAllopathic medicine has a very myopic scope / purview.  It is arcane compared to medicine that integrates multiple modalities.  Modern medicine is good for strokes and gunshot wounds, but the pharmaceutical model for treating symptoms, not cause, is outmoded (and don't get me started on the limits of modern medical diagnostic testing)."
      },
      {
        "id": "o7fulrg",
        "score": 6,
        "body": "If this is a genuine concern, have you looked into therapy? I started therapy partially for this reason and she helped me dive into why I doubted and being more sure of myself. But I feel like gaslighting yourself into doubting your symptoms is like a cornerstone of being chronically ill/in pain. I also started wearing a smart ring and it helped my \"you're faking it\" anxiety so much because I could actually see my symptoms manifest in heart rate, oxygen, sleep patterns, etc."
      },
      {
        "id": "o7zzyqy",
        "score": 2,
        "body": "I am so sorry, it can be very frustrating and discouraging to feel dismissed by providers. I am still fighting for answers myself. You are strong, they don\u2019t know what it feels like to be in your body. The normal amount of pain is 0."
      },
      {
        "id": "o81u246",
        "score": 2,
        "body": "I had this EXACT same feeling... I went to a therapist. He told me I was most certainly NOT crazy and NOT making it up. He set me up with a PCP who LISTENED to me. I got a bunch of surgeries I needed, and even though I'm still not 100%, I am no longer in the ER all the time (if ever) and I get to sleep for 4 hours at a time."
      },
      {
        "id": "o7wfwi2",
        "score": 2,
        "body": "normal amount of pain is not zero. that is a fantasy.  that being said, a normal amount of pain is certainly not debilitating or severe enough to interfere with basic daily functioning.  "
      },
      {
        "id": "o7wtgfo",
        "score": 1,
        "body": "Where is the pain? Nerve pain is microscopic and can\u2019t be treated with pain killers. Often that\u2019s what\u2019s going on"
      },
      {
        "id": "o7yrdki",
        "score": 1,
        "body": "You havnt talked about specialists. However i will just say. Keep fighting. There will be someone who believes you and someone who will try to help you. This sadly is a very typical part of being chronically ill and in pain. But there will be someone. Do your research on your symptoms and different doctors and providers in your area. It may take a long time, but there is always hope."
      },
      {
        "id": "o813dyc",
        "score": 1,
        "body": "Do you have insurance? I know an ER has to treat you regardless, but I can definitely see them lowering the level of treatment if they thought someone couldn\u2019t pay out of pocket for further testing. My CT scan at the ER recently was $17,000. I feel like they wouldn\u2019t have done it for me if I didn\u2019t have insurance probably.. it\u2019s weird they wouldn\u2019t run any labs or imaging."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1reujd4",
    "title": "Nurul Amin Shah Alam, Blind Rohingya Refugee Dumped by Border Patrol, Dies in Cold",
    "body": "",
    "flair": "Article / News",
    "score": 31,
    "comment_count": 0,
    "created_at": "2026-02-26T00:02:44+00:00",
    "top_comments": []
  },
  {
    "subreddit": "disability",
    "id": "1retwqx",
    "title": "Online exploitation",
    "body": "My adult child (M30) is HFA (Autism Level I), and lives independently, with minimal supports. Because a lot of his activity is online, that comes with some negatives, like buying into online ragebait and some relatively harmless things, but I noticed that he was spending increasing amounts on PayPal. \n\n  \nDigging in a bit more, he said it was for 'commissions' for artwork on DeviantArt (ignore the name, it's an online community for artists/art enthusiasts). People share, discuss, and sell art via creation or commission. \n\nSo, still not an issue, but the amounts kept increasing. $500 in 2024, $3600 in 2025, and $1200 so far in 2026. Pulling the data, it's mostly to 3 or 4 individuals, two of which I know have been sharing their 'misfortune' with him, and telling him that they lost a job, furnace and washer broke down, etc. These two people have gotten roughly $1100 each from him. \n\nSo, because the amounts were increasing, and some months were 3-4X his rent amount, I discussed it with him, and he said he was done with it for now. When it continued and increased, I got the stories about him 'helping out friends'. \n\nThe pattern struck me as exploitative, and while I didn't want to take away his account, I put restrictions on it so that only so much money could go into it each month (as 'entertainment'). That protects him a bit, but I'm still concerned about potential online exploitation. Does anyone else have experience that they can share about how to handle this? ",
    "flair": null,
    "score": 29,
    "comment_count": 17,
    "created_at": "2026-02-25T23:37:57+00:00",
    "top_comments": [
      {
        "id": "o7f7q1a",
        "score": 41,
        "body": "I'm also autistic and I'm out thousands of dollars thanks to people preying on me in a similar way. He is probably lonely and wanting companionship. Is there any way you can help him build some community locally? He might not stop letting people use him for his money until he feels worthwhile enough without their attention. I had really low self esteem when I'd get sucked into beggars' nonsense. I'm sorry you guys are dealing with this. Real friends won't ask him for too many favors! I hope he learns soon."
      },
      {
        "id": "o7f8yql",
        "score": 15,
        "body": "It's been a recurring thing - he once bought a hat for $150 because he 'felt bad' about the shop owner. I want to give him as much freedom as possible, and have worked hard to help him build a local in-person community of friends - and has people that ask if he will join them for things....but he's been resistant to anything that he feels paints him as 'other'.. \n\nSpecifically, he doesn't want to be around people who are lower functioning on the spectrum than he is, and he's spoken pretty badly about people with challenges - and the language he uses comes directly from guy/bro-oriented online stuff, and those people make him feel like he belongs to a community, but it's also filled with people who will prey on him. "
      },
      {
        "id": "o7fbcjp",
        "score": 11,
        "body": "Unfortunately these scammers are really good at preying on vulnerable people. They quickly learn the right way to groom them and once they sink their teeth in it\u2019s very hard to get rid of them, making a new account is easy enough. \n\nYour need to decide how much control you want to put in place but spending more than their rent monthly is concerning."
      },
      {
        "id": "o7f9cig",
        "score": 9,
        "body": "The only way I stopped the money thing was opening up about it in therapy and cultivating more self esteem. I know you can't force him to see a therapist, though. Hmm."
      },
      {
        "id": "o7g1oy1",
        "score": 7,
        "body": "Do you know what exactly he\u2019s commissioning? I think it\u2019s important he understands the difference between purchasing an item and giving money to a friend. Both are acceptable under certain contexts but transactions should belong to one or the other, it\u2019s a little too sticky if a single transaction is mentally compartmentalized as both"
      },
      {
        "id": "o7ffl6s",
        "score": 6,
        "body": "All of my social activities are virtual but my community is really supportive. Sometimes they don't quite understand the WAY I communicate, especially over text, but I remind them that I'm autistic so the way I communicate can be a little different. I'd suggest helping him find a loving, supportive community. Deviant Art is a great place to sell your art if you're an artist. Is he an artist? If not, then I'm not sure why he's on that site. Keep reminding him that with real friends, you don't have to buy them to keep them around. They will like you for who you are."
      },
      {
        "id": "o7gk7og",
        "score": 6,
        "body": "as someone with autism many of us have hyper empathy it can be really hard to not feel \u201c bad\u201d for people over the smallest things. i was financially taken advantage of a lot as a child. i think the only thing that helps is having better friends that don\u2019t take advantage of us"
      },
      {
        "id": "o7m2bze",
        "score": 5,
        "body": "I agree. Tho, I can think of a few reasons why a person might not want to show their art commissions to their parents (NSFW art, etc.)\n\n\nBut, I don't think it's necessary to literally see the artwork to have a conversation about appropriate pricing. The last time I commissioned a piece, it was a digital color drawing of my D&D character. It was only $80, and the artist said it took 4-5 hours.\u00a0\n\n\nSeems like undercharging, actually, now that I'm doing the math. But, regardless, on dA and Instagram commissions between $50 - $200 seem most common.\u00a0\n\n\n$1200, just in the last month and a half? That seems shady.\u00a0"
      },
      {
        "id": "o7f9mfl",
        "score": 5,
        "body": "He sees a therapist on a regular basis. They've known him for 10 years, and we've both struggled to get him to make any change at all in building in-person relationships. It's not easy by any stretch. "
      },
      {
        "id": "o7fa0vz",
        "score": 5,
        "body": "I'm really sorry to hear that. Have you tried bringing any of his special interests into it- if possible? I like friends who will talk about things that are interesting or have similar interests. I hope you get to the bottom of how to promote healthy changes in his social life."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1reteo5",
    "title": "I can't keep doing this. I need help.",
    "body": "I'm a disabled person that is 100% financially supporting themselves out of necessity.\n\nI am in so much pain, mentally and physically. Even just driving to and from work sends me into pre-syncope. Being at work all day is quickly destroying my body even further. My mental health is the worst its ever been. I just want to cry all day, every day. I keep it together very well, and although people know that I am disabled, they do not think it impacts me this greatly.\n\nI live in a right-to-work state, and am in management, so there is almost no way my company will make accommodations. I disclosed my disability upon hire, but that makes no difference. I have been struggling like this for years, but there is no way I can keep going. I have attempted to apply to remote jobs, but none have responded, or they're pyramid scheme \"pay to work\" companies. \n\nI have ten years of customer service experience, over five years of management experience, and have even owned my own business (which I had to let go of when my disability got worse). I also have three years of Vet Clinic experience. Yet nobody in any sector will hire for a remote role. \n\nAm I out of luck? Is there no hope for me? Do I just keep doing this until failure and end up homeless or worse? Do I have any options at this point?",
    "flair": "Discussion",
    "score": 32,
    "comment_count": 13,
    "created_at": "2026-02-25T23:18:16+00:00",
    "top_comments": [
      {
        "id": "o7fl1qg",
        "score": 10,
        "body": "I\u2019m not much of help, but know that you aren\u2019t alone in this. I am not working myself and suffer great deal of shame/anger that I can\u2019t be more functional in this messed up world. I\u2019ll still keep you all in my thoughts, that\u2019s the most I can promise. Please try to be kind to yourself & never give up!"
      },
      {
        "id": "o7jdvxo",
        "score": 5,
        "body": "What do you mean?"
      },
      {
        "id": "o7fwkz9",
        "score": 4,
        "body": "Your job has legal obligations to accommodate you as long as it is not an undue hardship and you can do your essential duties \n\nI highly recommend The Job Accommodation Network, AskJan.org to understand the interactive process your employer is legally required to engage with you in towards getting accommodated.  \n\nAlmost all states are right to work and requesting accommodations is a protected activity and being disabled is a protected class so termination or retaliation for either of those reasons is against the law"
      },
      {
        "id": "o7gauqd",
        "score": 2,
        "body": "I tried to work this system and found the edges, if you're interested."
      },
      {
        "id": "o7kze3r",
        "score": 2,
        "body": "I would give askjan a look, it can be helpful to have a 3rd party that they can look at and make sure to look at all your conditions ( Even the ones that you don't think are contributing that much to the pain you're experiencing, every bit helps and a lot of the accommodations overlap between conditions).\n\nPrioritize asking for the big ones first so it doesn't look like you're trying to see how much you can get away with by asking for small stuff first. For the really small stuff I would just do it on your own if you can (do I know employers should pay for ergonomic keyboards? Yes. am I willing to wait on it? No (but that may also be my, work from home, privilege speaking).) \n\nI would also see if there's any assistive Technologies or home adaptations you can get to see if you can make stuff go a little easier at home. There is a phrase that sometimes disabled people need a higher minimum income to afford to work because they need to pay for things at home like care and adaptations. And although getting a cleaner is really expensive and not always an option, getting a shower chair can also help."
      },
      {
        "id": "o7ognb8",
        "score": 2,
        "body": "As a former professional disability advocate, I echo this gentle push toward reconsidering the reasonable accommodation process. I know that being in a right to work state can feel like balancing on a tight rope, but your state also has a protection and Advocacy agency, one that is there to help you understand your rights in the workplace. Whatever state you\u2019re in, chances are that organization is called Disability Rights Statename. They have resources for you. I used to work at one (in a right to work state, a red state, and we unionized so yeah \ud83e\udd84).\n\nHave you considered taking FMLA? You sound very burned out. You have a set of rights associated with that, too. \n\nI also wonder if you know that you can still work and be on disability\u2014there is a limit to how much you can earn, but it gives you a layer of stability. Sounds like you are feeling pretty precarious right now. I know that feeling. I\u2019m sorry friend. The social safety net is pretty threadbare, but we do still have rights and resources, and people fought pretty hard for that. Let\u2019s use them."
      },
      {
        "id": "o7gq39p",
        "score": 1,
        "body": "Sorry you have to go through this. I'd ask to switch to remote work if they offer it. Other than get find a good psychologist that does telehealth. Best of luck to you."
      },
      {
        "id": "o7hkadz",
        "score": 1,
        "body": "I don\u2019t really know how it works outside the UK but I\u2019m also in a similar situation. I have a mortgage and struggle to manage my health and work full time. I do work from home and that\u2019s as much as my employer is willing to do for me. It\u2019s difficult still but better than it could be. \n\nAre there any guaranteed employers where you are? In the UK a civil servant role is not the best pay wise it\u2019s pretty basic but they are very flexible and accommodating. \n\nI\u2019ve personally had some success with reaching out to related charities for advice and support. In the UK you can also apply for grants for equipment so I don\u2019t know if that\u2019s something that you would be able to do where you\u2019re based."
      },
      {
        "id": "o7plp6w",
        "score": 1,
        "body": "Me too. My old boss didn't hold a ladder when I told him just put your feet there to cut in the top of a foyer stairwell painting. It collapsed I fell 30ft and at 32 years old. Now 40. Stopped working at 38. I have severe spinal stenosis, ruptured L4-L5 disc, torn ACL, torn meniscus, CT joint injury to my shoulder. Im 40, moved back in with my mom , truck got repossessed and been denied disability due to she and education and I don't even have a degree yet. I'm trying. Went back to school for data analytics. Been on temporary disability since May 2024 of 370$ a month. I have nothing. Worked 24 years for nothing basically. I use the analogy of a treadmill, the speed keeps getting faster and faster and you run thousands of miles but when it stops I end in the same spot or even worse"
      },
      {
        "id": "o80en80",
        "score": 1,
        "body": "Never heard of this. Thanks for sharing!"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rert02",
    "title": "How do you maintain housing after disability?",
    "body": "I have invisible disabilities (endometriosis & migraine: frequent intense pelvic pain that can make it difficult to stand & walk during flares, constant severe light sensitivity, dizziness episodes, chronic fatigue, & more rarely occurring temporary stroke-like symptoms (aura): inability to speak, partial vision loss, fainting, etc.), not yet to the point where I can qualify for  government approved disability status, but disabled enough to qualify for WFH accommodations from my workplace with thorough paperwork from my Dr.\n\nLately my company has been doing a lot of layoffs, and in my most recent performance review, they said I do the \u201cbare minimum\u201d even though I\u2019m a critical part of multiple important projects & frequently work early, late, and on weekends with no overtime pay (I\u2019m salaried so this is legal).\n\nI\u2019m scared that soon I\u2019ll be next to be laid off, meanwhile my symptoms have been getting worse with all the overwork & stress. I\u2019m going to appointments every week, I rarely ever leave my apartment except for appointments, & I\u2019m planning a surgery for later this year.\n\nMy question is, for those that have had to stop working due to their condition, how have you kept your housing? I don\u2019t have family who I can lean on; I live with my partner who makes less than I  & would not be able to cover the rent by himself. My savings was mostly used up in my most recent move & the rest is being directed toward my surgery.\n\nI live in a rent stabilized apartment in NYC; it\u2019s a great deal, especially split with my partner. I\u2019m unlikely to find a better deal on housing; we split a 1 bedroom for 1700. I guess I\u2019m looking for advice or suggestions. I\u2019m looking for another job in the meantime but I\u2019m so low energy after my current job that  I barely have the energy, & WFH jobs are a rarity now. I\u2019m scared",
    "flair": "Question",
    "score": 8,
    "comment_count": 3,
    "created_at": "2026-02-25T22:17:34+00:00",
    "top_comments": [
      {
        "id": "o7gand9",
        "score": 4,
        "body": "I\u2019m going to send you a DM. It\u2019s worth reapplying for disability even if you already applied and got denied. I\u2019m from NYC as well."
      },
      {
        "id": "o84f59l",
        "score": 2,
        "body": "Since you mentioned difficulty standing and walking during flares, have you looked into accessible housing options or any modifications that might make your current place more manageable during those times because maybe that could help alongside financial assistance programs too?"
      },
      {
        "id": "o8mcno7",
        "score": 1,
        "body": "Thanks a bunch for your time & advice! Thankfully I\u2019m not having any accessibility issues with my apartment. I live in an elevator building, there\u2019s a ramp at the entrace, my apartment is spacious enough to use a mobility aid if I need, & I can fit a chair in the shower. & I was able to surprisingly find a lot of perfectly good mobility aids at my local thrift store. My concerns are primarily employment related, & being able to keep my housing if I were to become unemployed because this is honestly a great apartment for me."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1reo9qu",
    "title": "Anyone else planning to move away from the U.S as a disabled person?",
    "body": "Does the united states went off the rails for you recently? As a forever pill taker that needs pills to survive and the weirdness in health care here, high prices, high stress, toxins in the food, fast paced lifestyle, it all just makes it all worse for my mental health. You are expected to rely on nothing and nobody and the infrastructure makes it hard to live without a car and live a simple life, they want you to complicate your life and get in debt for nothing, just for basic stuff, i am done, anyone else?",
    "flair": null,
    "score": 161,
    "comment_count": 140,
    "created_at": "2026-02-25T20:07:06+00:00",
    "top_comments": [
      {
        "id": "o7e1y9e",
        "score": 206,
        "body": "I recommend searching this sub as this topic pops up sometimes here. Basically, unless you can work, have a spouse that can work, or have dual citizenship currently, you are unlikely to be successful."
      },
      {
        "id": "o7dz939",
        "score": 118,
        "body": "Pretty sure I see this same post every day in chronic illness and disability subs, so yeah.\n\nBut is this a \"plan\" or is it a wish? Because you need a work visa, green card, or a passport to that country if you wanna be able to actually live there. It's frankly a pretty tone-deaf and privileged look for Americans to casually talk about \"just moving\" to wherever they want in the world as if all borders are open to them. It doesn't work like that."
      },
      {
        "id": "o7e0ccd",
        "score": 117,
        "body": "As a full time wheelchair user, the more I travel internationally the more I appreciate the accessibility in the US"
      },
      {
        "id": "o7e2let",
        "score": 62,
        "body": "Yep! I live in Italy. 2 years ago I dislocated my shoulder dragging my walker up the stairs at the train station because the elevator was out. I'm still waiting for surgery for the tears in my tendon.  The grass is not always greener on the other side.  But somethings are better and somethings are worse."
      },
      {
        "id": "o7e59qu",
        "score": 59,
        "body": "Many countries ( with universal healthcare ) don\u2019t want disabled people unless you can prove you have a lot of money. Like I think I looked into Canada a while ago ( like a decade ago) and I needed at least a hundred grand in bank to go."
      },
      {
        "id": "o7e1gpj",
        "score": 48,
        "body": "Yeah, I\u2019m American and I am working through a several year plan to be able to immigrate somewhere else. The idea that you can just pick up and leave is a little strange."
      },
      {
        "id": "o7gow64",
        "score": 41,
        "body": "Even if you can work and have a strong established career it\u2019s WAY easier said than done. I am an engineer with over 20 years of experience and looked into this and quickly dismissed the idea because it was patently impossible."
      },
      {
        "id": "o7ega4f",
        "score": 39,
        "body": "\nIt does feel tone deaf, especially since a lot of places are directly and negatively influenced by the same things because of american hegemony. And like, I\u2019m not here to judge individuals, and I have a lot of sympathy! \n\nBut all I see these days is people asking about moving to a bunch of places without any deeper research and asking natives from those places to provide to them what basically feels like sale pitches, all with a bunch of criteria a country must fill to be considered\u2026 which are usually impossible because again, american hegemony affecting the world.\n\nNot even gonna get into the consequences of gentrification because that\u2019s a whole other can of worms. Regardless, immigration is harder than ever and americans face the same barriers everybody else does when doing it."
      },
      {
        "id": "o7eg576",
        "score": 34,
        "body": "I looked into this after the election. Unfortunately, countries want citizens that contribute economically, and I, as a disabled person, don't qualify. Midterms can't come soon enough!"
      },
      {
        "id": "o7eoc65",
        "score": 32,
        "body": "I'm an American with several disabilities, including learning disabilities and a TBI. I moved to Germany. I didn't move away because of my disabilities. I married a guy who is German. \n\nThere's stairs EVERYWHERE. I can hardly count on working elevators, if there's one around. Big cities are a little better. Apartments are several stories high with no elevators in them. Even homes tend to be built up not out, so again lots of stairs. My old house has 3 floors,  because it is built up due to space building out isn't possible. \n\nBathrooms are ridiculously small especially in public. They are very clean. Getting a special key for handicap bathrooms  takes a bit of work. Same with parking passes. European cars are tiny, they don't fit into the parking lots, parking garages very well if at all.  The price of gas is basically $7.50 a gallon here,  so bringing a big American car is a bad idea. Just about everything you own you'll have to replace if it plugs in.  The voltage is 110 in the US and 240 here.  Yes, you can get adapters but to waste the little baggage space you get it isn't worth it. \n\nI barely and I mean barely after working hard for over 18 months was able to pass the bare minimum requirements of speaking, reading, writing and communicating in German. This does me ZERO good really at doctors appointments. The doctors may not speak English well enough to properly understand my issues, they tend to not trust American doctors reports. So I had several things that I needed to start over with getting re-diagnosised \ud83d\ude43 again. Trying new medication or trying things that already failed.  Medical in Germany tends to be more find the cure if possible and try herbal medicine first. At the pharmacy I can't buy a huge bottle of Ibuprofen. It is a little box of maybe 20 tablets at a time and 400 MG. It costs more money here, you have to talk to the pharmacist to get it,  so again there's a language barrier for me.  Yes my husband translates, but they want to talk to me,  hear from me what is wrong, not him. \n\nNo one cared that I have diagnosed learning disabilities deal with constant migraines. \n\nGetting medicine like Adderall here is extremely difficult. I haven't found a doctor yet who will prescribe it. There's quite a few medications that you can't bring in from the US, or if you want to go visit to the states bring back.  \nRefrigerators here are very small,  that means several trips to the grocery store every single week. \nMy house doesn't have a freezer. I also don't have a dryer so clothes have to be hung up here. My house relies on a fireplace still. Everything is smaller here.  My microwave isn't big enough to hold my old American dinner plates. The oven is the size of my old microwave. \n\nHonestly if my husband wasn't a sweetheart and wasn't able to do all the laundry, the cleaning and the shopping I couldn't even survive the house. The old outhouse was converted into a \"laundry room\" when it was upgraded 70 years ago. Most have a washer in the kitchen now. The washers here hold about the same amount of clothes as a carry-on suitcase. \n\nA lot of Europe is tiny and is really hard to add handicap friendly to places that have been around longer than the US has been.  My house is older than the US. The food pantry I had back in the US is bigger than my bathroom here. There's rarely AC here. \nI know in the US the costs to see the doctor might be expensive, and but remember that trading the comforts there might be hard to give up, especially if you can't walk far, go up many stairs or have medicine that you can't live without."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1remrgw",
    "title": "Neo-bladder and blue badge",
    "body": "I had my bladder removed recently owing to cancer. I have a neo-bladder, which means I have no 'full bladder' sensation. I sometimes self-catheterise. I have no warning other than sharp kidney pain when my neo-bladder fills up and I drive high mileage in towns and cities where it can be hard to find a parking space before getting to a loo. When I have sharp kidney pain it's very distracting and I don't think my driving is entirely safe. I've noticed high availability of disabled parking spaces from which I could quickly access a loo (I have a radar key). Might I qualify for a blue badge?",
    "flair": null,
    "score": 4,
    "comment_count": 20,
    "created_at": "2026-02-25T19:13:31+00:00",
    "top_comments": [
      {
        "id": "o7ebe4j",
        "score": 6,
        "body": "Not in the UK. You fill in a form explaining your difficulties and provide evidence which for many will include letters from doctors\u00a0"
      },
      {
        "id": "o7eigca",
        "score": 5,
        "body": "Not for incontinence on its own. \n\nhttps://www.gov.uk/government/publications/blue-badge-can-i-get-one/can-i-get-a-blue-badge\n\nAnd if it\u2019s affecting your driving, you need to inform the DVLA because it\u2019s a legal requirement but also because otherwise your car insurance could refuse to cover you if you get into an accident, even if the other driver is at fault."
      },
      {
        "id": "o7dvda5",
        "score": 3,
        "body": "Speak to your doctor they are the ones who can fill out the paperwork"
      },
      {
        "id": "o7vmj4z",
        "score": 3,
        "body": "Incontinence isn\u2019t a mobility issue though?"
      },
      {
        "id": "o81riod",
        "score": 3,
        "body": "So do you think everybody with gallstones or IBS or chronic pancreatitis should get a blue badge? And take up disabled spaces because they need a loo?\n\nI don\u2019t have the luxury of being able to use a regular space because I cannot open the car door wide enough to transfer into my wheelchair without the extra width provided by disabled spaces.\n\nMy friend cannot physically walk from a regular space in the car park to the shop, or the hospital, or whatever the destination is.\n\nThat is what blue badges are for. Hence the criteria not saying anything about toilet needs or temporary pain."
      },
      {
        "id": "o839mf5",
        "score": 2,
        "body": "My sibling is one of the first successful neo-bladder recipients so please don't take this as me trying to belittle your feelings but 35 years of experience you need to schedule bathroom stops no longer then 3 hours if you are driving you need to be mindful of your liquid intake  because waiting till kidney pain is extremely dangerous and can result in life threatening infections and or kidney disease unfortunately this still dose not qualify for a blue badge I'm just pointing this out because of the health risks I saw when reading your post I am sorry you are going through this a neo-bladder is not easy to adapt to no matter what age you receive it and I hope you don't have to deal with to many issues I'm sorry you weren't properly told about how to deal with this issue"
      },
      {
        "id": "o7enn05",
        "score": 2,
        "body": "Ahh my bad. But sounds like you might"
      },
      {
        "id": "o81rnly",
        "score": 2,
        "body": "I\u2019d gladly let you have my blue badge if you take my disability too. And I\u2019ll have yours and park in a regular space and find my own way to the loo using my functional legs \ud83e\udd37\u200d\u2640\ufe0f"
      },
      {
        "id": "o8467sb",
        "score": 1,
        "body": "So, no warning at all, like ever, even after drinking a lot? Figuring out when to go must be a nightmare."
      },
      {
        "id": "o85m1ri",
        "score": 1,
        "body": "Yeah, I saw that link too but it's worded kinda vaguely. I know someone who got one based on \"severe anxiety\" that resulted in a need to always be near a bathroom, so maybe emphasize the urgency aspect?"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rejo0c",
    "title": "Denied after 10 years from beating and recovering from cancer TWICE",
    "body": "Ive been on disability for 10 years, because of my cancer, my arm is weak, my lung and my back are weak as well. I got cancer in my arm at a young age and been recovering till now. And I recently got taken off and denied\u2026\n\nI was in shock cause i literally couldn\u2019t work at all, my physical strength is none existent due to cancer.\n\nBeen through cancer twice, my arm is physically weak and cant lift stuff and i have a bad lung that still has a cancer nodule inside and still looking at it, and im denied as well. Ive been looking for work but no one wants to hire\u2026 especially someone like me with no work history due to this cancer issue\u2026 so i dont understand why disability denied me.. im constantly going to doctors and all of them say i should be on disability but \u201cSTATE doctors\u201d apparently are different\u2026 i have no money to my name due to the denials now and i just need advice at this point.",
    "flair": "Rant",
    "score": 12,
    "comment_count": 13,
    "created_at": "2026-02-25T17:27:56+00:00",
    "top_comments": [
      {
        "id": "o7d4ve8",
        "score": 12,
        "body": "Find an SSDI lawyer."
      },
      {
        "id": "o7dnpk0",
        "score": 12,
        "body": "Most of the disability lawyers work on contingency so they only get paid if they win and they take it from your back pay. So please definitely look into that."
      },
      {
        "id": "o85rwuo",
        "score": 3,
        "body": "It's not just about physical limitations either mental health stuff can be really hard to prove but just as debilitating."
      },
      {
        "id": "o7d3my6",
        "score": 2,
        "body": "What in the world??? I am so sorry you got a denial. Do you have an attorney to work with? I hope you appeal. And I hope you are in the best place possible for your health."
      },
      {
        "id": "o7d4b00",
        "score": 2,
        "body": "I have no money for a lawyer or attorney. Idk how i got it the first time. My mom helped out with all that and it was approved but now since they see me \u201crecovering\u201d technically, they took me off.. its wild i know"
      },
      {
        "id": "o86rb0m",
        "score": 2,
        "body": "Working in it now."
      },
      {
        "id": "o7doc0i",
        "score": 2,
        "body": "I will try"
      },
      {
        "id": "o7w2pg8",
        "score": 2,
        "body": "If you don't have a lawyer yet, at least appeal the decision online within 60 days, and that will give you time to find someone to help you. \n\nIn this situation, there is no \"I'll try\" because this is something that is fairly easy to do, and if you want your disability back, you need someone to help you. Hiring a disability lawyer doesn't cost you a DIME up front, so get going! \n\nYou don't mention your age, but could you have been cut off because you recently turned 18? Sometimes that is the case, but if you are still disabled, there is no reason not to appeal, and try to get your benefits back. \n\nGood luck to you, and praying for your health! \ud83d\ude4f\ud83c\udffe"
      },
      {
        "id": "o84qxzu",
        "score": 1,
        "body": "Dude that\u2019s awful, straight up. For me, and tbh this was years ago, winning my appeal was about getting a doctor to REALLY spell out how I couldn't do even basic jobs."
      },
      {
        "id": "o85u8u6",
        "score": 1,
        "body": "So, when you say \"back pay,\" are we talking about just Social Security, or something else too?"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rej9dh",
    "title": "Restaurant accessibility",
    "body": "I went to a restaurant with my fianc\u00e9 yesterday to celebrate his birthday. During the dinner I had to go to the accessible bathroom and I had to ask my fianc\u00e9 for help with everything. \n\nThe door was so heavy that I couldn\u2019t open it by myself. (There was no door opener either)\n\nThe toilet didn\u2019t have handrails or anything to grab onto so my fianc\u00e9 had to lift me from my chair to the toilet. The toilet paper was too far from the toilet which meant that if I had a bad day I would most likely have fallen of the toilet trying to reach for it. Which could be quite bad since there was no emergency button either. \n\nWhen I was going to wash my hands the sink was way too high (approximately my shoulder height) This caused my shoulders to hurt for the rest of the evening. The soap was too high. (I couldn\u2019t even touch the bottom of the soap dispenser). \n\nThe trash can was a can with a pedal that you step on in order to open it. Probably not the best choice. \n\nNot really sure what they think an accessible bathroom is since nothing was accessible there. ",
    "flair": "Rant",
    "score": 16,
    "comment_count": 7,
    "created_at": "2026-02-25T17:13:57+00:00",
    "top_comments": [
      {
        "id": "o7cy0fn",
        "score": 10,
        "body": "NOt sure about UK laws, but the US has strict definitions about what is accessible. If you're in the States, you can report that place. Go for it."
      },
      {
        "id": "o7cyff7",
        "score": 4,
        "body": "I\u2019m in EU. Not sure if there are any rules about what is accessible."
      },
      {
        "id": "o7f49yh",
        "score": 3,
        "body": "Definitely report it, if I go to a place I haven't been to before these days, I call ahead, and sometimes have still been caught out because they aren't accessible even though they said they were. \n\nSorry this happened. The world just wasn't built for people with disabilities, even though a lot of people will get older and need accessibility and/or anyone can acquire a disability at any time"
      },
      {
        "id": "o7lz0dh",
        "score": 2,
        "body": "Welcome"
      },
      {
        "id": "o7lz2nd",
        "score": 2,
        "body": "I usually just call the number on google"
      },
      {
        "id": "o7i9n36",
        "score": 1,
        "body": "Thank you. \nWill look up how to do that."
      },
      {
        "id": "o81yen4",
        "score": 1,
        "body": "For a private business there wouldn\u2019t really be any place to \u2018report\u2019 it. The best thing to do would be to submit feedback to the business. This could be by phoning them, emailing or filling in a feedback or comments form on their website, or submitting a review of the business on something like Google or Trip Advisor. As far as I know there is no penalty for a private business in not being accessible other than getting the word out to others that it is not accessible."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rehu37",
    "title": "My husband has diabetic neuropathy but can't get disability",
    "body": "My husband has been laid off so many jobs that I have lost count. He physically is unable to work because he has diabetic neuropathy and chronic pancreatitis. He is officially unable to feel one of his legs and can't even leave the house some days, yet he is still being denied disability. I am unable to provide for us both this way, and, while my current job has been extremely lenient on letting me leave to take him to appointments or to the hospital, they are having to let people go soon and I will be one of those people. I don't know what else to do anymore and feel so lost. Has anyone else had to go through something like this? I need so much guidance..",
    "flair": null,
    "score": 5,
    "comment_count": 9,
    "created_at": "2026-02-25T16:24:05+00:00",
    "top_comments": [
      {
        "id": "o7crko5",
        "score": 5,
        "body": "Does he regularly see his doctor(s) and are they documenting in his medical chart that his symptoms prevent him from working and how? This needs to apply not just to the job he has been working but any job enough to earn SGA (Sustainable Gainful Activity, the cut off social security uses to determine if one earns enough to be considered not disabled for employment purposes which is $1690 this year). Has he tried any prescriptions or therapies recommended by his doctor(s)? Has their effectiveness/ineffectiveness/side effects been documented in his medical records?"
      },
      {
        "id": "o7cqm8v",
        "score": 4,
        "body": "Personally neuropathy was never the slightest assume for me while working. And that was 40+ hours a week.  I currently dont have feet and have been denied disability.  So best of luck trying"
      },
      {
        "id": "o7cmklb",
        "score": 4,
        "body": "He was denied SSDI? Have you appealed? Have an attorney?"
      },
      {
        "id": "o7dge26",
        "score": 2,
        "body": "The judge denied him or just the first or second go around?  Did you have lawyer?"
      },
      {
        "id": "o7ndlfp",
        "score": 2,
        "body": "I\u2019m really sorry you\u2019re both going through this. That\u2019s an exhausting place to be.\n\nSadly, a lot of disability claims get denied the first time, even when the person clearly can\u2019t work. Many people only get approved after appealing. If he hasn\u2019t appealed yet, that\u2019s usually the next step.\n\nIf you\u2019re in the U.S., getting a disability lawyer can help a lot. They usually only get paid if you win, and they know how to present things in terms of \u201cfunctional limits\u201d (like how long he can stand, walk, miss work, etc.), which is what they look at.\n\nAlso make sure his doctors are clearly documenting:\n\n* Loss of sensation\n* Falls or instability\n* Hospital visits\n* How often he can\u2019t leave the house\n\nYou\u2019re not failing. The system is just hard. A lot of people in similar situations eventually get approved, it just takes persistence and the right paperwork.\n\nIf you\u2019re comfortable sharing, what country are you in? The process can vary a lot."
      },
      {
        "id": "o7omh66",
        "score": 2,
        "body": "A lawyer is def a good idea, but imo look into vocational rehab services too, they might offer job training that works around his limitations."
      },
      {
        "id": "o7g29jb",
        "score": 1,
        "body": "I\u2019m going to guess DDS said he can do other work. Idk how old your husband is but they might have said he can do sedentary work which wouldn\u2019t require him to be on his feet. Have you looked at his disability claim? You should contact the local office to get a copy to see what rationale they have for his limitations and why."
      },
      {
        "id": "o7omues",
        "score": 1,
        "body": "Appeal and get a disability lawyer, they only get paid if you win so it\u2019s not gonna cost you anything upfront. Seriously, that\u2019s probably your best bet tbh."
      },
      {
        "id": "o813kzi",
        "score": 1,
        "body": "I agree with you that it\u2019s difficult, but my mom\u2019s disability was approved for fibromyalgia and something else (inclusion body myositis?). Her medical records are lengthy though"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1readua",
    "title": "I just got denied disability... Again",
    "body": "I have multiple disabilities and I've been trying to get on disability for about two years. This past time, because of all the stuff going on in the American government they said they would be done doing the paperwork around August last year but here we are. I just got denied yesterday. I'm frustrated. I'm going to be off Medicare because of the stupid government and I don't have snap anymore. I'm so tired. I'm tired of fighting for myself and not having my needs be met by the people who are supposed to help me. I'm fine, I'm just fricken fed up. I hate this government. \n\nIf anyone has any tips to make denials easier or ways to get on health insurance when I can't get a job, that would be wonderful. Thanks for hearing me out. ",
    "flair": "Rant",
    "score": 7,
    "comment_count": 13,
    "created_at": "2026-02-25T11:09:23+00:00",
    "top_comments": [
      {
        "id": "o7b4pzb",
        "score": 6,
        "body": "Did they explain why they denied you? If this was your second denial the next step would be an appeal, are you able to get a lawyer or representative to help you?\n\nAlso you mentioned you would be kicked off Medicare and SNAP, did you mean Medicaid? You can still be on SNAP and receive Medicaid as long as you are able to show proof that you are unable to work. I know different states have different rules but double check and call to speak to someone."
      },
      {
        "id": "o7c6oif",
        "score": 3,
        "body": "Get an attorney for sure they don\u2019t charge you unless you win . My husband fought his for four  years and was approved on the second appeal before a judge. Keep fighting but definitely need an attorney!"
      },
      {
        "id": "o7ej1uf",
        "score": 3,
        "body": "If you want you can DM me. I\u2019ve been working at DDS for 16 years processing claims. I mostly do CDRs/reviews or reconsideration. I reverse a lot of denials. There is such a high turnover rate in my state. A lot of the examiners now haven\u2019t been here that long and either lack the experience and make mistakes or tbh they take shortcuts and do what\u2019s easier for them."
      },
      {
        "id": "o7esntr",
        "score": 3,
        "body": "I'm in a different state but they waved the work requirement because I was under review for SSDI at the time. Might be worth talking to them again if you appeal, they may be able to wave it.\n\nAlso, some disability lawyers offer free services unless you win (they usually take a % backpay)."
      },
      {
        "id": "o7be0zl",
        "score": 2,
        "body": "OP get help from\nServices on the Aged and Disabled Waiver https://share.google/k0hvlKEKKjFVHHLSx"
      },
      {
        "id": "o7flfgz",
        "score": 2,
        "body": "You can get an exemption for the work/ability requirements by getting the proper forms filled out by your doctor.  In MN it's called \"Request for Medical opinion\".  It looks like Nebraska has similar forms but you have to request them."
      },
      {
        "id": "o7b6wtp",
        "score": 2,
        "body": "Yea I meant Medicaid. I'm tired. I'm from Nebraska and sadly I have to be working to be on Medicaid/snap after next month I believe? I don't really want to think about that too hard. \n\nDisability said it doesn't prevent me from working, which is a load of bs so they denied me. That was their whole reason. They said it limits work but doesn't prevent it, which even then I feel I should get partial disability as it, in their words, LIMITS MY WORK ABILITY. This whole thing is stupid. Sadly I don't have a lawyer or representation, I don't know how to. I've done this basically on my own."
      },
      {
        "id": "o7coz7s",
        "score": 2,
        "body": " No such thing as partial disability your either too disabled to make sga or you can make it no in-between"
      },
      {
        "id": "o7f7f3e",
        "score": 2,
        "body": "I'm in Nebraska as well. For the new work requirements, volunteering for a certain number of hours will allow you to keep SNAP - not ideal but if you can't get hired but still need to eat.. I just did snap recertification at the beginning of January and they asked me if I was disabled but didn't require proof or a SSI determination. I just listed my diagnoses and they stopped me when they had enough to approve the work requirements waiver\n\nIf you're in the general omaha area, DM me and I can give a recommendation on a disability lawyer. And if your disability is mental health related, there's another resource. Otherwise, check with Nebraska Legal Aid"
      },
      {
        "id": "o7b3slk",
        "score": 1,
        "body": "Did you get an attorney?"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1re5t3m",
    "title": "Disabled but not enough",
    "body": "Hello! So I am in this weird situation. I have a bad hip. A really bad hip and I need surgery. But I am also over weight to the point they won\u2019t do surgery on me till I loose 200 pounds (I am 380). And I don\u2019t qualify for weight-loss meds on my insurance and I live in the hell hole of the USA and GOP1 is 1k a month because they can charge that because they want to. So I am getting blood drawn and seeing what I can do on my own. Meanwhile my femur is splintering into my body as it\u2019s past bone on bone in there. And my mobility is so shit. I can barely walk. And I am constantly in pain. When I sit I am in pain. When I lay down I am in pain. And the hygiene took me 2 years to figure out (I don\u2019t have help) on my own. And I don\u2019t qualify for disability. I finally got my disability parking! But I can\u2019t apply for disability. The reason is I just don\u2019t have time. It takes years to get approved and I just can\u2019t afford not making money. And I just am so but hurt about it. I have to work so hard just to take care of myself let alone work. It just bites man. ",
    "flair": "Rant",
    "score": 21,
    "comment_count": 29,
    "created_at": "2026-02-25T06:35:44+00:00",
    "top_comments": [
      {
        "id": "o7ab0wb",
        "score": 25,
        "body": "It doesn't necessarily take years to be approved if you're genuinely disabled, but you should hire a disability attorney. They will work on everything for you and only get paid if you're approved. They are only allowed a certain amount of your first check. Best money I ever spent and I was approved on the first attempt. There's no need for you to suffer. You don't get Medicare until you're on it for 24 months though."
      },
      {
        "id": "o7app6i",
        "score": 10,
        "body": "Have the doctors explained why your hip is failing so bad at such a young age? It can\u2019t be just weight. Weight may be a reason though that they put surgery on hold. I had to be under a set weight getting a total knee replacement. \n\nIf you can qualify for disability then you should apply and use an attorney too. They might make you get rejected once before they take your case, so get started on it now."
      },
      {
        "id": "o7d1kzy",
        "score": 6,
        "body": "The lack of work I've had to do is amazing to me. They only reach out to me if they need something. It makes me a smooch anxious to not be apart of the appeal but its still nice not having to worry about any of it."
      },
      {
        "id": "o7cem71",
        "score": 5,
        "body": "A good disability attorney will work on everything for you. A bad one won\u2019t do jack shit. Good luck finding one who isn\u2019t going to do jack shit."
      },
      {
        "id": "o7cwzc3",
        "score": 4,
        "body": "I have been able to do a number of surgeries that were not recommended for my weight by just looking around for a surgeon/anasthesiologist that specializes in overweight people and explaining that I am aware of the risks.  I also agreed to lose as much weight as I could before surgery without committing to a number. Obviously it would help to actually lose that weight but from my experience that is a tall order and difficult if you can\u2019t move much, as not only can you not exercise but it\u2019s harder to prepare healthy food. \nI wish you the best. I would definitely look for anaesthesiologists who can work on overweight people, as often the reason they don\u2019t want to do surgery is because anasthesiologists don\u2019t know how to work on fatter people."
      },
      {
        "id": "o7cmkff",
        "score": 3,
        "body": "I did my research and found an excellent one."
      },
      {
        "id": "o7cb3hr",
        "score": 3,
        "body": "OP states in post history that they are 29. No hallucination needed."
      },
      {
        "id": "o7ekp2v",
        "score": 3,
        "body": "I am very glad you have that! Mine has been almost totally absent from the process to an extent that would shock me if I wasn\u2019t used to being neglected and abandoned by every profession and institutional resource"
      },
      {
        "id": "o7b9bun",
        "score": 2,
        "body": "I'm sorry to hear about your situation. Depending on if you have an FSA, you may be able to use it for a GLP1 from another cheaper resource like another commentor mentioned."
      },
      {
        "id": "o7d53zq",
        "score": 2,
        "body": "I would contact a service that sets you up with a disability lawyer. I used [Atticus](http://www.atticus.com) and they set me up with a lawyer here in the state I am in, which is Texas."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1re31jk",
    "title": "Treated like I\u2019m lazy in the ER",
    "body": "So earlier today I had a therapy appointment where my therapist ultimately had me sent to the er for suicidal ideation and since then I\u2019ve just been treated like I\u2019m lazy. I am in the process of recovering from Guillain-Barr\u00e9 so I can\u2019t stand up or anything and need to use a bedpan. A few hours ago when I had to go the nurse just seemed really annoyed and frustrated and did bare minimum in helping me get onto the bedpan kinda making me reposition myself which takes a shit ton of effort. Afterwards she still just kept treating me like I was lazy and wasting her time. Obviously I can\u2019t just roll over and clean myself or stand up and do it so I needed help but she once again did bare minimum. I don\u2019t even think you could say she tried. My mom came by an hour later and had to finish cleaning me and was livid. It\u2019s already hard enough being in the ER and it\u2019s hard enough needing help with everything but situations like that just make it 100x worse. Next time I\u2019d rather actually follow through with a plan than come here and get treated this horribly. ",
    "flair": "Rant",
    "score": 11,
    "comment_count": 0,
    "created_at": "2026-02-25T04:13:03+00:00",
    "top_comments": []
  },
  {
    "subreddit": "disability",
    "id": "1re2767",
    "title": "Would it be wrong of me to use things like a wheelchair or other aids before I get someone to find out what's going on?",
    "body": "I really wish I could add two flairs to this (both question and concern)\ud83d\ude2d\n\nSo, I usually have a lot of random pain in my lower joints(and sometimes just lower extremities in general) and I've noticed Im feeling more light-headed lately after standing(and it seems that standing and staying standing seems to be the problem). \n\n(More context for above paragraph: no, i dont have any diagnosed disability or reason for it to be happening)\n\nBasically my question is, would it be wrong of me to use an aid like a wheelchair or rollater(I think that's the word?) while waiting to find someone to check me out(and waiting to see what's wrong), even though im fine the majority(maybe 85%) of the time?",
    "flair": "Question",
    "score": 0,
    "comment_count": 10,
    "created_at": "2026-02-25T03:33:35+00:00",
    "top_comments": [
      {
        "id": "o79l4mv",
        "score": 16,
        "body": "There\u2019s two levels of this. It\u2019s not wrong to use the power scooter at the grocery store or ask for a wheelchair at the airport. But regular use of a wheelchair or rollator without training can actually make your disability worse by risking injury.\u00a0"
      },
      {
        "id": "o7a1ibr",
        "score": 9,
        "body": "Second word of caution, if you need it at any given time, use it. But don\u2019t use it consistently 24/7. The reason I say that is because non-use of muscles can create their own problems. If you\u2019re capable of moving around under your own locomotion, do it, but if you\u2019re at risk of hurting yourself, use whatever you need to get through that timeframe. Good luck."
      },
      {
        "id": "o79rl9g",
        "score": 5,
        "body": "If using a wheelchair or any other aid keeps you from being hurt by all means you use it. You do not need a script from a doctor. However in the meantime you need to speak with your doctor and try to find out what is going wrong."
      },
      {
        "id": "o7agie9",
        "score": 3,
        "body": "If using a mobility aid helps reduce your pain symptoms, and does not add any additional symptoms, occasional use should be fine. \n\nIf you are needing to use it daily, I would suggest reaching out to a physical therapist that can help identify your sources of current pain, while also educating you on how to use a mobility aid with minimal harm.\n\nJumping straight into using a standard recovery wheelchair for multiple hours a day, multiple days/weeks/etc. could result in an injury to your back, neck or shoulders. \n\nA mobility aid is a piece of equipment, a tool. \nLearning how to use that tool safely to prevent adding additional harm is ideal. \n\nListen to your body. Pay attention in case you experience new pain elsewhere, such as wrists or shoulders or hips due to using a mobility aid. \n\nI do hope you can afford a physical therapist or some sort of medical assessment to help you identify the best mobility aid for you. \n\nListen to your body. If using the mobility aid helps reduce your pain, without adding a new type of pain, that is ideal."
      },
      {
        "id": "o7ahadc",
        "score": 1,
        "body": "I had to get a rollator before I was diagnosed because I kept falling. Now, I\u2019ve been falling even while using a rollator, so my mom grabs the hospital wheelchairs when I have dr apts.\n\n(Waiting until my CSF leak is healed/fixed before determining in I need a manual wheelchair or not, since some people recover and are able to walk again. Also have POTS though, so idk)\n"
      },
      {
        "id": "o7bmb8j",
        "score": 1,
        "body": "\ud83d\udcaf\ud83d\udcaf"
      },
      {
        "id": "o7bgkdu",
        "score": 1,
        "body": "This is very good advice. I have an ongoing issue with my hands, which prior to physical and occupational therapy, required that I wear a brace at all times to help the pain. Wearing the brace constantly increased the weakness that I was experiencing, to the point where the braces alone stopped helping the pain. A little bit more moderation with the brace time might have helped my recovery, but hey, I'm back to 75% functional now!"
      },
      {
        "id": "o7ah0u2",
        "score": 1,
        "body": "I use different mobility aids for different purposes. \n\nI bring my rollator when I'll need a nice place to sit, and also use it to help carry my luggage -- so I mainly use it at the airport. \n\nI use a wheelchair at conventions where I would be required to stand for more than a few minutes, or end up walking more that 2,000 steps.\n\nI use my \"Seat-Cane\" that unfolds into a small chair when I need to travel light, but need access to seating in locations that do not have seats really available. \n\nI have a wheelchair, and I needed it daily when I worked a job that had me doing 5k-10k steps a day. But now that I work at an office job, sitting, I have not had to use it in months."
      },
      {
        "id": "o79xsiz",
        "score": 0,
        "body": "If you need it, it\u2019s okay to use it.   Do you!"
      },
      {
        "id": "o7c1acn",
        "score": 0,
        "body": "Keep it simple. You do you! You do not need permission from anyone here or anywhere else to use something that will make your life easier. Why would you struggle when you don't have to? You know the answer."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rdzl31",
    "title": "To be, or not to be",
    "body": "Not a \"poor me\" post, I'm genuinely seeking some guidance. M 32. I've recently become disabled, I spent most of my career hot shot driving and in construction, all with Amish and Mennonite. Therefore, I do not have any work credits built up with social security. I've been given less than $1000 a month in assistance between SNAP and SSDI. No kids, no wife, just a dog and my brother and I. I've lost my home, vehicle, and ability to work. I've developed epilepsy and don't know what to do. I don't make enough to save anything after paying people for a place to stay, and I find myself owing money to loved ones at the end of every month. I have no long term plan, nor do I know how to form one with what little I have. What is a guy supposed to do? How do others do it? I wasn't able to get section 8, or HUD, I was not told why, just given a denial in 3 different states over the last few years. Does anyone know how to make this a liveable situation? As it stands, I am becoming a burden on those I love. My inability to drive or save money is leading to isolation from my peers and mental decline. I fear that I will become a stain on the lives of those I've held the closest. There are a lot of days where I contemplate just going out into the woods of a huge national park and just walking until I can't anymore. I don't have the heart to take my own life and hurt my family even more. I don't have any significant partners because I pushed her away in fear of her losing respect and love for me. No, it wasn't an impulsive thing. I watched her slowly lose interest after the accident happened. I've had a good life, I've got a loving family that I was born into. I just don't see any light at the end of this tunnel, and desperately want to stop burdening those around me who have the unfortunate circumstance of helping me stay indoors at the moment. \n\nIf anyone knows of any guidance programs, or has any personal experience in this themselves. Please, do help a brother out. I apologize if this post seems sappy, or dramatic, I genuinely just don't know where else to turn or how to go about asking for help. Before this, I was the one everyone came to for guidance, and help, with bills, a place to stay, work. It's so confusing and frustrating being on this end that I can't see past my own shortcomings.\n\nThanks in advance\n\nSincerely \n\nThe guy that wants to stay",
    "flair": null,
    "score": 6,
    "comment_count": 13,
    "created_at": "2026-02-25T01:35:38+00:00",
    "top_comments": [
      {
        "id": "o7bziyh",
        "score": 4,
        "body": "Honestly, most people that receive SSI are barely maintaining a roof over their head. Some people live with roommates, some have moved back into their parents house. It could take years to get section 8. A lot of people max credit cards out, get personal loans\u2026 life is definitely a struggle for most people on SSI welfare."
      },
      {
        "id": "o792muw",
        "score": 4,
        "body": "While I appreciate that, none of this actually helps me at all. I've reached out to most of these places already and either don't live in a qualifying area, don't meet requirements, or can't get to the place to get the food. Genuinely looking for help, not just lists of gov agencies. I've been on this path for some years, and I can promise you, the assistance programs do not care about single white males with no kids or work history."
      },
      {
        "id": "o7bz7n3",
        "score": 3,
        "body": "If you\u2019re getting less than 1000 a month you are most likely getting SSI welfare and not SSDI. Make sure you know which benefit you are receiving so you know which rules to follow, SSI has some strict rules that must be followed."
      },
      {
        "id": "o796exv",
        "score": 3,
        "body": "I don\u2019t think you understand what we can give you. We are in the same boat you are. What the other person gave you is it. What people have told you to go for help is it. There is no magical place that will save you and make you rich healthy and happy. Becoming disabled leads to poverty. It\u2019s just that simple. The fact you did not work before means what you qualify for is the state minimum and it will barely pay one bill. The government does not care about us. In fact the last year has shown just how much they are cutting back on helping us with any assistance. We are all seeing cut backs and it makes it harder to stay sane. The only thing you can do is keep calling keep advocating for your self because no one else will."
      },
      {
        "id": "o790b2i",
        "score": 2,
        "body": "**United States**\n\n* Call or Text 988\n* [Text HOME to 741741](https://www.crisistextline.org/about-us/where-we-are/)\n* [National Suicide Prevention Hotline](https://suicidepreventionlifeline.org/): 1-800-273-TALK (8255)\n* [Care Crisis Web Chat](https://www.imhurting.org/): 1-800-584-3578\n* [Domestic Violence 24-hr Hotline](https://www.thehotline.org/): 1-800-799-7233\n* [National Sexual Assault Hotline](https://www.rainn.org/): 1-800-656-HOPE (4673)\n* [United Way](https://www.211.org/)\u00a0(Crisis, Food, Health, Housing): Call 211\n* [Adult Protective Services](https://www.napsa-now.org/help-in-your-area/)\n* [Administration for Community Living, Protecting Rights and Preventing Abuse](https://acl.gov/programs/aging-and-disability-networks/state-protection-advocacy-systems)"
      },
      {
        "id": "o796xuu",
        "score": 2,
        "body": "If I were in your shoes I'd call the appropriate agency and figure out what's going on with section 8 because you meet the criteria unless you have some sort of criminal record, there was an administrative error, or the wait list was closed. You can call and request a written denial letter which will have the specific reason for denial (this is required by HUD). \n\nAdditionally, your health insurance should cover therapy, and I would recommend working with a therapist familiar with disability so you can begin working on some of those internal issues and/or taking medication if appropriate. "
      },
      {
        "id": "o79d5rm",
        "score": 2,
        "body": "No criminal record, no shady past. Just a lot of moving around to try and stay housed. As well, I've done the therapy. I don't think it's unrealistic for someone to feel this sort of despair in these kind of circumstances. I don't want to hide from my own reality or dull it out with mind altering substances or aid just do real drugs lol."
      },
      {
        "id": "o79dpp7",
        "score": 2,
        "body": "Then I'd reach out, repeatedly, and ask for a reason and keep advocating for section 8. If you qualify you'll be able to get it as long as you advocate for yourself and really fight for it.\n\nTherapy shouldn't be about telling you not to feel bad, therapy is about learning how to cope in a healthy, non-destructive way.\n\nAnd I hope you're avoiding the \"bad\" drugs lol.\n\nThat said, you keep saying you feel like a burden....are the people in your life telling you you're burdening them?"
      },
      {
        "id": "o79dzfm",
        "score": 1,
        "body": "Real sober\"\" I don't expect some magical answer or secret. I'm just curious as to how anyone is able to do it. As I stated, I meant no offense to the comment or with the hotlines. I've just already exhausted those options with nothing being gained. Not screaming poor me, just asking for help with information to get stable again. Gov apartments won't accept me either, I have a decent credit score, no evictions, no criminal history. I even have letters of recommendation. Just don't know where else to turn, I guess this was just a last attempt to try and find something after years of nothing."
      },
      {
        "id": "o79kyqh",
        "score": 1,
        "body": "Cats\"\" no hard drugs, just MJ and some alcohol. No one is telling me I'm a burden, I'm just not blind. I'm a grown man living off of other people's dime. People who would break themselves for me. It's something I'm beyond grateful for. I think I cope fine, I'm just at a point where I realize this isn't a sustainable situation. I don't mean to come off too dramatic, I would just rather remove myself from the equation than see others struggle because of me just existing. I've done the homeless thing, the tent thing, the couch surfing thing. I'm just not going to keep stressing my family daily about my well being or with their finances being askew because of my presence. I think to believe I could be ok with it, or numb it with psych meds is the crazy approach. I think the only logical thing for a man to do in this situation is to take action to preserve those trying to help me. I'm not their responsibility. Not talking suicide, but more of assisted expedited death by natural causes via means of introduction to life in the wilderness. Who knows, maybe I wouldn't even die out there like that. Maybe I'd end up one with the land and happier than I ever was in society."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rdvwak",
    "title": "22F with muscular dystrophy looking for friends in a similar situation",
    "body": "Hi, I'm 22 years old and I have muscular dystrophy. I've been semi-bedridden for years and I can't eat on my own. It has been very hard lately, and I often feel very isolated.\n\nI'm looking to connect with people who are in a similar situation. I would really appreciate talking to other women around my age, but anyone kind and understanding is welcome.\n\nIf you'd like to chat, please feel free to message me.",
    "flair": null,
    "score": 9,
    "comment_count": 6,
    "created_at": "2026-02-24T23:03:48+00:00",
    "top_comments": [
      {
        "id": "o78sg74",
        "score": 1,
        "body": "Oh that\u2019s too bad. I have a friend of mine who\u2019s in his 60s that  was diagnosed with  muscular dystrophy  in his late 20s and he\u2019s not doing so well mentally I hope you find someone to talk to you that around your age."
      },
      {
        "id": "o797bl2",
        "score": 1,
        "body": "I am 22 almost 23F and I have hEDS that has also left me partially bed ridden (muscular dystrophy is what they thought i had at first so ive read some on it *hugs*)"
      },
      {
        "id": "o7lmzh0",
        "score": 1,
        "body": "I am 21F and have muscle degeneration and loss of feeling/function in my limbs that often impair my mobility/walking due to a neurological condition. I have to spend most of my time in bed as well. I am sorry you are experiencing this. I was actually searching for a disability support group when I came across this message\n\nWhile my situation isn\u2019t identical and I cannot say I know what you are fully experiencing, I can relate to feeling isolated/being isolated from being bedridden off and on. This has been a huge, rapid change for me and I\u2019m sending kind regards your way because it is hell"
      },
      {
        "id": "o8e55bf",
        "score": 1,
        "body": "Hey! I am 33F with a subtype of muscular distrophy (fshd). I use a wheelchair as I cannot walk and would be happy to connect :)"
      },
      {
        "id": "o79rl7i",
        "score": 1,
        "body": "I'm sorry about that. This is the first time I have heard about the disease you mentioned, can you talk a little more about i if it will not be a problem? Is this a progressive disease? Is there a current treatment?\n\nI hope you feel better mentally and physically, if you feel bad, we can talk about it \ud83e\udec2"
      },
      {
        "id": "o79scb7",
        "score": 1,
        "body": "It is also a genetic condition that affects my connective tissues. Its not progressive for everyone, but mine is seeming to be. There is also a chance I get some function/quality of life ive lost, but ive also been symptomatic for as long as I can recall which is unusual normally symptoms dont become super noticeable until puberty. I really struggle with the fact that I was able to walk most places unassisted 5 years ago when I graduated high school and now if im going outside of my apartment I have to use a chair and crutches anywhere in my apartment:( I also live on the second floor which means I dont get out much because I have to plan to get myself back up the stairs or makesure my husband is there to help me."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rdtio8",
    "title": "Charged for applying for disability - California",
    "body": "i\u2019m going to assume this is a pretty unique situation. But I\u2019m really conflicted and I don\u2019t know what to do. I am pregnant and just applied for disability. At the end of my disability application there is a code I am to give to my doctor (or doctors receptionist) after I gave this code she asked me if I was ready for payment. I questioned what she meant by that and she charged me $40 and said someone at the doctors office will complete everything from here on out and I won\u2019t have to deal with EDD. I had never heard of this before so I googled it and I guess it is something common in other states however in California it says it is illegal to charge patients for filling out paperwork for public services such as disability if you have medi-cal insurance which I do. I obviously need them to fulfill their end, disability reaches out to your doctor to go over everything when you apply. That is a requirement, not a luxury.  I\u2019ve checked many reputable websites, and they all say if I have medi-cal insurance, I live in California, and I\u2019m applying for a public service such as disability, if my doctors office is charging me a fee it is against the law and I need to report it but like I said, I don\u2019t want anybody to stop my application process if I do. I\u2019m really conflicted and could use some advice/help. Thank you in advance!",
    "flair": null,
    "score": 16,
    "comment_count": 25,
    "created_at": "2026-02-24T21:34:56+00:00",
    "top_comments": [
      {
        "id": "o78ip3u",
        "score": 9,
        "body": "They may not have realized that you have Medicaid and so you cannot be charged for anything involving your care, including filling out documents. I recently had to educate a physician\u2019s office on the fact that they cannot legally charge a patient with Medicaid a fee for missing an appointment. At first they were adamant that I was incorrect and that such fees were allowed to compensate the medical provider for the time they could have spent seeing another patient as it was not a charge for care provided. I printed out the exact page of the Medicaid policy handbook doctors are given in my state that included this information clearly stated and handed it to them while explaining I would not be signing the form accepting this fee should I have to cancel an appointment on less than 24 hours notice and I had no further issues."
      },
      {
        "id": "o79lx8q",
        "score": 6,
        "body": "Medi-Cal is Medicaid only, not Medicare. Medicaid members can only be charged for services not covered by Medicaid and when there\u2019s an explicit agreement between the provider and member for the charges indicating that it\u2019s not a covered benefit. This is a federal law that states must adhere to and it applies to ALL medical providers, whether they\u2019re enrolled as a Medicaid/Medi-Cal provider or not. If you have concerns about if it is a permitted charge, most state Medicaid departments have a customer service line where you can report provider misconduct. They will tell you if it\u2019s permitted. This is common with balance billing practices or when a provider files a claim incorrectly and it gets denied, so they direct bill the member. State agencies will send the provider a notice that if they do not retract the bill or reimburse the fee they could be sanctioned and disenrolled as a provider or have claim funds withheld or clawed back."
      },
      {
        "id": "o77u9kt",
        "score": 5,
        "body": "Do u have medicaid/medicare?"
      },
      {
        "id": "o782ukr",
        "score": 5,
        "body": "yes i have medi-cal which is the California version of medicaid/medicare. and when i looked this up its specifically illegal in California (whereas other states its not) if you have medi-cal"
      },
      {
        "id": "o7agiyv",
        "score": 4,
        "body": "i am almost positive everyone at this office has medi-cal. as its the only insurance (that i know of) that my doctor accepts. its a very crowded office. i obviously need my disability so im thinking of bringing this up after my application is processed and i get paid. just really disappointing feeling like i may have gotten scammed by my doctors office."
      },
      {
        "id": "o7fiaif",
        "score": 4,
        "body": "Because that\u2019s essentially exactly what their doing, scamming you. Just inform them that they cannot charge you for providing necessary medical information for a disability application. They also wouldn\u2019t typically be allowed to stop your application since your application wouldn\u2019t really be with/through them, disability applications are typically a state/federal thing. \n\nMake sure they refund you too because you didn\u2019t even consent by the way you wrote this, you simply responded \u201cwhat?\u201d To her saying are you ready and they took the payment from your? Saved card? They cannot charge you without authorization that way either"
      },
      {
        "id": "o77uew1",
        "score": 3,
        "body": "This could be the general standard fee doctors offices charge if you don't have medicaid/medicare"
      },
      {
        "id": "o7ah382",
        "score": 3,
        "body": "so do you recommend i call medi-cal\u2019s customer service line and find out if this is a covered benefit?"
      },
      {
        "id": "o7cx4ne",
        "score": 3,
        "body": "If you want your money back, yes."
      },
      {
        "id": "o79kspk",
        "score": 2,
        "body": "I get the frustration and the confusion however if that is what is holding up your application for it it might be worth just paying for it as you\u2019ll receive that and then some once on CASDI through EDD but you can also report it. So it\u2019s really your choice"
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rds4os",
    "title": "How to cope with active & malicious discrimination by neighbours?",
    "body": "I\u2019m in the UK & applied for a disabled parking bay 6 months ago and our local council had to consult with my neighbours as part of the process, which was rejected because of the neighbours who have been hostile and gossipy since. \n\nIt\u2019s taken months to get the clear truth about what the objections were, but I\u2019ve finally learned from a council officer today that some of my neighbours along our street not only cited \u201cnot enough space\u201d (an invalid reason as I wouldn\u2019t have taken any more space than I already do), but also ableist downright discriminatory and incorrect allegations against me to stop my application going ahead. \n\nI\u2019m shocked to have people I thought were friendly be so antagonistic to a reasonable accommodation, though not surprised in this world where hate and misinformation run rife. \n\nCan anyone advise how to deal with these two-faced back-stabbing neighbours( on a personal everyday level, not a legal or process basis)? \n\nI\u2019m not used to my disability being used against me. This feels like grown-up bullying, and being ostracised from the street, but the only silver lining is at least I know the truth about their real feelings.",
    "flair": "Question",
    "score": 11,
    "comment_count": 12,
    "created_at": "2026-02-24T20:45:01+00:00",
    "top_comments": [
      {
        "id": "o77ehe3",
        "score": 16,
        "body": "It sounds like where you live has a complicated ~~dumb~~ legal situation surrounding accessibility. It may be best to engage with a lawyer who works primarily in disability and access law."
      },
      {
        "id": "o77fgfp",
        "score": 8,
        "body": "Thanks. The council has a stupid way of dropping disable parking bay applications if it\u2019s going to cause hassle, but after talking with them today, they apologised and offered to review the application. \n\nThe kicker for me is that my neighbours may likely still object, despite some errors from the Council\u2019s side. \n\nMy lasting dilemma aside of whether I get the bay or not is that I now realise I live amongst awful people who want to make others\u2019 lives difficult.\n\nHence wondering how to deal with the unjustified disability discrimination in a personal level, rather than a legal or procedural level. One objection was \u201cshe\u2019s not disabled enough\u201d \ud83d\ude28. \n\nHow the hell do I counter that level of vileness?"
      },
      {
        "id": "o77hp7p",
        "score": 4,
        "body": "Ime, there isn\u2019t much reasoning to do with bigots."
      },
      {
        "id": "o8m9xci",
        "score": 2,
        "body": "I used to live in a HOA neighborhood where my request for an accommodation for disability was denied because the kindly neighbors didn\u2019t want my household to remain there. They approved another neighbor\u2019s accommodation unanimously. The recommendation that I engage an attorney was tried, and my single consult with the only attorney in the area who would entertain taking on the case got me the information that I couldn\u2019t afford to attempt to prosecute even with plain evidence of discrimination against a household with three disabled people.   \n  \nWe found a place to live without an HOA, which has been financially difficult though not impossible. We were lucky enough to still have savings to make this happen. I\u2019m hoping that we recover financially somehow in the next ten years.   \n  \nI couldn\u2019t cope with these 2-faced neighbors, and I hope that you find a way out as well. "
      },
      {
        "id": "o8ot0tz",
        "score": 2,
        "body": "I\u2019m so sorry you\u2019ve had to go through all of that: A large financial loss to bear as well as all the betrayal of your ex-neighbours. You are strong, you have been through the mill. Adversity breeds strength and resilience. \n\nAt least you\u2019re free of the ghastly neighbours and I wholeheartedly hope your new community is a more friendly, welcoming one. Sometimes we need that storm to help us find a better place to drop anchor in life. \n\nYou don\u2019t deserve all that ostracism; none of us do. Thank you for your kind words & wishing you all the best. \u2728"
      },
      {
        "id": "o8q5d2w",
        "score": 2,
        "body": "I like my new neighbors. The new town is much more diverse and groovy. Nobody snooping around, hunting for violations. "
      },
      {
        "id": "o77ir5b",
        "score": 2,
        "body": "True enough, thanks for replying anyway."
      },
      {
        "id": "o77t2qq",
        "score": 2,
        "body": "Thank you for your thoughtful reply. Must admit, I\u2019m actually in the UK so the law and processes are quite different, unfortunately. Although I note there\u2019s aspects that you have over in the States that we don\u2019t seem to have here. \n\nI love your ideas about the t-shirt or badges \u201cis this disabled enough for you\u201d. I already have a sticker on my car identifying one physical condition I have, but it\u2019s relatively subtle. Maybe it\u2019s time to be more in their face! \n\nYour definition of perfidy is very appropriate. I\u2019ll use that if I get the chance.\n\nThanks for the ideas and practical suggestions, much appreciated."
      },
      {
        "id": "o77w9v5",
        "score": 2,
        "body": "I apologize for my arrogant assumptions that you were in the U.S.\n\nThere are other tactical ways of aggravating one that is not kind but I'll let you decide if it's appropriate.\n\nOne, my brother did while deployed overseas was to throw bird seed on the top of Connex (container) unit. It was used as deployable living spaces for military personnel.\nThe guy was a real piece of work.\n\nIf you haven't,  I would ask whatever search sites you use for info on local disability laws. Specifically, parking and disability byelaws.\n\nI truly wish and Pray for your positive outcome, in all the things you brought up. And good health for you."
      },
      {
        "id": "o77opox",
        "score": 1,
        "body": "I don't know enough about law for us disabled and your disabilities.\n Do you have a disabled placard or tag.\nWhere you live has to obey ADA and local disability laws.\nIf so they have to give you priority for the medical reasons you have.\nThey are gambling being sued if you need preferential needs due to medical disability and not giving it after request.\nI would talk to a lawyer if able.\n\nLook up \n\nThe U.S. Access Board (Access Board (.gov)) is a federal agency that promotes equality for people with disabilities by enforcing accessibility standards under the Americans with Disabilities Act (ADA) and other laws. They provide guidelines, technical assistance, and training on accessibility in design, construction, and transportation.\n\nFederal Agencies: The U.S. Access Board sets accessibility standards, while ADA.gov provides official documents and resources on the Americans with Disabilities Act.\n\nEasterseals (formerly Easter Seals Society): One of the largest organizations serving children and adults with disabilities, often focused on rehabilitation,, and community services.\n\nThe Arc of the United States: While it does not use \"Society\" in its main title, it is the largest national community-based organization for people with intellectual and developmental disabilities.\n\nTASH (formerly The Association for the Severely Handicapped): An international advocate for people with significant disabilities, focusing on inclusion and human rights.\n\nHumanity & Inclusion (formerly Handicap International): An international organization working alongside people with disabilities, particularly in situations of poverty, conflict, and disaster.\nethical\n\n\nThe social part...\nIf u have a device, get a sticker/sign/shirt, saying something like, is this disabled enough 4 u? \n\nOr something of the like\n\nYou could ignore them. If they ask about it, just say your actions speak louder than your:\n\nPerfidy. A more literary term referring to a state of being deceitful and untrustworthy\n\ndisability shaming\n\nMinimizing their condition: Making light of the severity of their disability or suffering.\n\nQuestioning someone's disabilities, challenging, doubting, talking behind their backs; takes a very questionable person or someone who has been exploited. \n\nI think the 1st one might be more prevalent.\nSadly, many people do not like it when someone else gets benefits or help that they don't or can't receive themselves. \nEven thinking why them? I deserve 'whatever' or 'at least', because most are self-serving. And would arguably deny it.\n\nYou could also approach it differently.\nAsk to honestly and maturely, discuss how they perceive your disabilities and how they effect your daily life. \nAnd how you have to do or handle things differently and about flare-ups/bad days.\nThat you would prefer not to be disabled like the rest of the disabled world. And irate, not liking anyone who would be exploitative."
      }
    ]
  },
  {
    "subreddit": "disability",
    "id": "1rdqr4m",
    "title": "Why is the r slur a slur but not other similar terms",
    "body": "Genuine question - why is the r slur considered a slur but not other terms like 'stupid' or 'moron' which have similar origins and meanings?\n\nThe r slur was once a clinical term to diagnose the intellectually disabled - but so also were the terms  'stupid,' 'idiot' , 'imbecile', and 'moron' - all clinical terms once used to describe the degrees of a person's intellectual disability in the early 20th century. 'Hysterical' was a diagnosis used against specifically women - and I see the terms hysteria and hysterical used all the time without anyone seemingly blinking.\n\nSo I guess I'm just confused why the r slur is considered a  slur and not any of these other terms? Like I've heard folks say ' dont call people \\*insert r slur\\*, just call them stupid' and its like... those are both outdated clinical terms once used to described intellectual disability. They aren't fundamentally that different - yet one is clearly considered far worse socially than the other terms. Is there a reasoning for that or is it kind of an arbitrary thing?",
    "flair": "Question",
    "score": 4,
    "comment_count": 20,
    "created_at": "2026-02-24T19:55:20+00:00",
    "top_comments": [
      {
        "id": "o778ery",
        "score": 34,
        "body": "Many disabled people in my circles recognize that all of those are ableist slurs and choose not to use any of them.\n\nI can\u2019t speak for why so many of them have become common parlance without being considered hateful, but language evolution doesn\u2019t need to be logical."
      },
      {
        "id": "o77bbe1",
        "score": 24,
        "body": "This is a good question! My best guess is the amount of time that\u2019s passed since these meanings were associated with these words. \n\nLike \u201cstupid\u201d and \u201cidiot\u201d (I try to avoid the other ones, but I\u2019m not perfect) phased out of medical use a couple decades before MR/ r-word phased out of use. Like the r-word was still a medical term in the early 2000s but stupid and idiot were out decades before that."
      },
      {
        "id": "o77t1u9",
        "score": 18,
        "body": "Hi, I personally avoid using those terms. I think if people really thought about what they were saying, they\u2019d find better language to say what they mean.\n\nSo, calling someone \u201cstupid\u201d or an \u201cidiot\u201d is berating them for their perceived or actual intelligence. Does that really seem okay to people? Is there something morally wrong about being less intelligent that warrants being berated?\n\nIt\u2019s also just really vague. Being an \u201cidiot\u201d means what exactly? The best definition I could come up with is \u201cbad brain\u201d which doesn\u2019t really tell you much. Are they unaware of some information? Are they being foolish? Are they being irrational? All three of those things are better ways to communicate what you mean than just \u201cidiot\u201d. \n\nI\u2019m not even gonna get into how our modern concept of intelligence is rooted in the eugenics movement and white supremacy. Anyways, I hope this helps."
      },
      {
        "id": "o78esum",
        "score": 13,
        "body": "As others have said, yes, many of us\u2014especially those whose values are rooted in Disability Justice\u2014tend to recognize that it is ableist, classist, and eugenicist to insult people\u2019s intelligence, no matter the language we use.\n\nWe can use more precise and descriptive language in the place of these slurs. Rather than just generally bashing someone\u2019s smarts, we can call attention to someone\u2019s incompetence or their recklessness or their callousness.\n\nIt just takes pausing and thinking, and reflecting on whether you\u2019re choosing the most accurate word for what you\u2019re feeling. Because most of the time, there\u2019s something more powerful to say than \u201cidiot\u201d or \u201cdumb\u201d"
      },
      {
        "id": "o7861j5",
        "score": 12,
        "body": "Honestly I don't really have an answer for this other than that the usage of the r slur is very recent and very relevant to modern society. Other terms are extremely old and no longer used to refer to a specific sort of person.\n\nI personally don't care what language people use other than the r-slur (at least, for my family members, I tell them to knock it off). It was the term used to refer to mentally disabled people when I was growing up while terms like stupid, dumb, etc were never used to refer to the disabled. I just don't consider it relevant anymore to avoid dumb and stupid and I think there are more important things to deal with. But that's just me."
      },
      {
        "id": "o7861nm",
        "score": 11,
        "body": "As someone who tries to live this practice, I can relate a lot to feeling like those terms are so common that it wouldn't occur to you that it was something people would/could do. That was my initial reaction and thought. It has helped me be more conscientious about what I say in general, basically if I find that I am going to use a term like that, I ask myself why internally, and that helps shed light on whether there is something I want to say but am just struggling with wording.\n\nPrime example: I've wanted to call right wingers and fascists \"brainless\". That's me wanting to dehumanize them in the way that I feel that they contribute to the dehumanization of vulnerable people, I want to imply that part of \"their sin\" is how \"stupid\" they are. It's also me trying to shame them for that sin of stupidity. So, I don't say that anymore. It has helped me be more precise and authentic in many ways. \n\nMost fascists aren't uninformed people in need of education or lacking the necessary cognitive capacities to understand why fascism is harmful though, most of them are being callous, selfish, myopic, or taking a sadistic delight in cruelty and resentment. Telling them that can feel like it doesn't have the teeth of some quick insult to their intelligence to shame them, but the truth is that it is really valuable to call stuff out as immoral or harmful (even when the person themselves doesn't care, others can and do)."
      },
      {
        "id": "o79qabv",
        "score": 5,
        "body": "Vagueness is exactly why they're used as insults--because they can be used to communicate the speaker's attitude with minimal (counter-)factual information."
      },
      {
        "id": "o77m6wb",
        "score": 3,
        "body": "I havent really heard of anyone avoiding those terms entirely - those terms are just so commonly used in the mainstream I guess it hadnt occured to me that some folks would opt out. \n\nDo they just avoid insulting people's intelligence at all then? Or just use different terms to do so? I'm genuinely curious."
      },
      {
        "id": "o77lwvz",
        "score": 3,
        "body": "Thats probably it at least in part"
      },
      {
        "id": "o7u7est",
        "score": 3,
        "body": "Ignorant, uneducated, misguided, foolish, silly, obtuse, ridiculous, short-sighted\n\nI'll edit if I can think of any other possibilities!"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1l0xjin",
    "title": "17 turning 18, want to do combat arms. Uncle died in Iraq, Dad says no combat",
    "body": "My uncle was a 0311 in Iraq and drove on a ied and died, my dad doesn't want me to join combat arms even with how much I feel called to do it. If y'all had to deal with this I would like to hear y'all's experience and how you handled it.\n\nEdit: my dad is a submariner veteran 2006-2011",
    "flair": "Enlisting",
    "score": 66,
    "comment_count": 55,
    "created_at": "2025-06-01T19:27:30+00:00",
    "top_comments": [
      {
        "id": "mvguxfs",
        "score": 58,
        "body": "Your father lost his brother, so of course he would be hesitant to have his son follow the same foot steps. Due to the trauma, you probably aren\u2019t going to be able to change his mind regardless of what you try to tell him. \n\nIf combat arms is something you truly want to do, then go do it. When you turn 18, you\u2019re a fully grown adult and will be able to make your own choices. He might get angry, but this is your life, not his."
      },
      {
        "id": "mvgvli7",
        "score": 56,
        "body": "I mean technically we\u2019re not at war with anyone but I still understand your father\u2019s concerns. If it\u2019s what you wanna do, the do it."
      },
      {
        "id": "mvgxtan",
        "score": 55,
        "body": "0311 here. My mother\u2019s brother came back ummm different from Vietnam. You could say she lost him there. It took some patience and valid reasons I felt the need to go 03. She wasn\u2019t happy about it, but she understood it was what I felt I needed to do for my life. Today she\u2019s ecstatic and proud of the time I spent there and very glad I\u2019m back safe raising my children. My point is, we all have to choose our own path, and just about any MOS has potential to be dangerous. Especially if shit pops off. Write down your valid reasons and what you hope to accomplish, then share them with him. Patiently. This isn\u2019t a \u201cit\u2019s my life and I\u2019m gonna do this\u201d conversation. You want him on your side, it\u2019ll help you through all the bullshit. Good luck my friend. Infantry ain\u2019t for everyone."
      },
      {
        "id": "mvgzm9q",
        "score": 20,
        "body": "Your dad\u2019s fear makes sense. He\u2019s trying to keep you alive. Losing his brother probably changed him forever. And now he sees his kid wanting to walk into that same fire.\n\nProve to your dad you're informed and research the MOS (Military Occupational Specialty) or AFSC (Air Force Specialty Code) you're interested in. If you want to be close to the action, there are combat support roles that put you in the thick of things but aren\u2019t 0311. You might look at combat engineer, combat medic, JTAC, combat comms or intel roles with special operations units. **If you're not sure you're going to do 20 years then pick a career that can translate easily into a civilian role (firefighting, medic, cyber).**\n\n**The military is not Call of Duty**. It\u2019s not about racking up kills, being a hero. It\u2019s about responsibility. It's not a 9-5 office job that you get to go home and not think about work. It's a 24/7/365 lifestyle that most people can\u2019t even understand.\n\n* **You're responsible all day.** Physically and mentally tested 24/7. Your pack, your weapon, your buddy\u2019s safety, all of your decisions.\n* **You see things that don't leave you.** That might be your friend bleeding out, a kid gets killed, or even just the aftermath of combat.\n* **You train more than you fight.** Endless drills, inspections, range time, rehearsals, cold nights and hot days. It\u2019s 99% boredom, 1% chaos.\n* **You don\u2019t get to pick your war.** You go where you\u2019re told. That might mean a combat deployment, or it might mean classroom training.\n* **You follow orders.** Even when it\u2019s frustrating because you just had a kid or met a girl you like. That\u2019s the job. Your home life and girlfriend are your 3rd priority.\n* **You come home changed.** Some come home to nothing. You'll carry that weight forever.\n\nSource: I'm a 20+ year USAF/USSF vet"
      },
      {
        "id": "mvi1nu6",
        "score": 20,
        "body": "Glad to see not just another redditor basically telling OP to give his dad the bird"
      },
      {
        "id": "mvh1m8t",
        "score": 12,
        "body": "There is no front right now. What war are we in?\nIf you want a chance to see combat you\u2019re going to need to go SF or ranger battalion."
      },
      {
        "id": "mvh04i6",
        "score": 9,
        "body": "Thank you"
      },
      {
        "id": "mvgysrz",
        "score": 7,
        "body": "Why do you feel \u201ccalled for it\u201d? \n\nI can tell you why I wanted/went combat arms. To fight and go to Iraq."
      },
      {
        "id": "mvh0nlc",
        "score": 7,
        "body": "I want to enlist in the army as a 13f and hopefully ranger regiment, thank you sir"
      },
      {
        "id": "mvhk2aq",
        "score": 4,
        "body": "Look man, you\u2019re turning 18. That means you\u2019re becoming a man, and one of the first hard tests of manhood is this: making a decision your family might hate you for\u2014temporarily.\n\nI was in your shoes once. My mother was devastated when I enlisted. Wouldn\u2019t speak to me for months. It stung. But I knew what I was doing was right for me. And when she stood at my AIT graduation in tears, proud as hell? That made it all worth it.\n\nYour dad\u2019s fear is real. He lost his brother. So yeah, he\u2019s terrified of losing you too. But being a man means understanding someone\u2019s fear without letting it steer your decisions. You can love your father and still disagree with him\u2014and still go.\n\nWhat you\u2019re feeling\u2014that \u201ccalled to it\u201d fire inside you\u2014it doesn\u2019t come from nowhere. It comes from the same place that turns boys into leaders. You don\u2019t owe anyone an explanation except the one you give at formation, in uniform.\n\nAnd you\u2019ll earn your dad\u2019s pride back. Maybe not today. Maybe not next year. But one day, when you\u2019re standing tall, he\u2019ll see you didn\u2019t rebel\u2014you just grew into the kind of man your uncle would\u2019ve respected.\n\nWrite your own chapter. Stand tall for your reasons. And when you make that call, don\u2019t look back.\n\n\u2013\nSpecialist \u201cTripod\u201d \ud83c\udf96\ufe0f\nMP/K9 | U.S. Army Veteran | OG E4 Mafia\n100% P&T: Earned it the long way around\n\ud83e\ude96 On the net. You\u2019re not alone out here.\n\n\nTyped it up with a little help from a digital assistant. Final thoughts, experience, and insight are all mine."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1ke8mp4",
    "title": "I\u2019m A confused teenager in the army",
    "body": "I know this probably really stupid of me and probably not the smartest idea but here we go i\u2019ve been in the army since around september 2024. I knew it wasn\u2019t for me as soon as i arrived at reception but i graduated basic and ait and here i am now. I want out so bad, the army is destroying my mental i already had to have mental heath waivers to get in. i went to shpp multiple times in attempt to get chaptered and it never worked and now im thinking about failing a drug test or maybe going awol to get out of the army. any advice?? or any other ways i could get out of the army??? Pls help. Edit: i\u2019m 17 i literally signed my life away a couple days after my birthday im about to be 18 in a few weeks and idk what to do.",
    "flair": "Branch-Specific",
    "score": 65,
    "comment_count": 40,
    "created_at": "2025-05-04T01:42:00+00:00",
    "top_comments": [
      {
        "id": "mqgw7x1",
        "score": 88,
        "body": "Bro. Listen please. Don\u2019t try and force your way out by failing a drug test or going awol trust me these are not ways to get out. If you ever need anyone to talk to please feel free to reach out to me. I care for you and hope the best for you bro but please don\u2019t go awol or fail a drug test on purpose."
      },
      {
        "id": "mqh1vx0",
        "score": 48,
        "body": "Talk to your platoon Sgt about this. Don't fail a drug test or go awol. They can discharge you for failure to adapt, which is a better discharge. If you go awol, they can pull you back and drop your rank. It's a very messy way to leave."
      },
      {
        "id": "mqh2zhv",
        "score": 35,
        "body": "You didn\u2019t sign your life away. Life is just getting started. You only have a couple years for a life time of benefits and a leg up in life. You can still go to college or whatever you wana do."
      },
      {
        "id": "mqgvtbo",
        "score": 30,
        "body": "The fastest and easiest way out of the Army is to just do your time. All you have to do is the bare minimum and you will be fine."
      },
      {
        "id": "mqh6cmk",
        "score": 23,
        "body": "Hey buddy, you can seriously screw up your life if you try to get chaptered on purpose.\n\nFinish your time honorably and it will help your life. You can literally get free healthcare for the rest of your life with the VA and get a a payment every month if you claim a disability after your service. I'm not saying to get hurt on purpose, but almost everyone gets hurt eventually. There also programs to pay for your education and job training and placement programs.\n\nThere are so many good things waiting for you when you finish out your contract."
      },
      {
        "id": "mqha9u8",
        "score": 20,
        "body": "Yes,  this exactly, if life now is affecting your mental health imagine if you were only getting a small portion of your paycheck and were on extra duty as well,  this is what happens if you try to get out by failing a drug test or disappearing,  they will put you out,  eventually,  but your QoL will go down greatly while you hurry up and wait for the discharge. Try to meet people at your unit,  get out of the B's, hunt the good stuff,  go to behavioral health if you have to. you're a year in and you probably only have a few more left, talk to the chappie, try to stick it out."
      },
      {
        "id": "mqgxb3j",
        "score": 16,
        "body": "Time will fly brother. Just think you\u2019ve done a year already. You have 2 years left and you can get down  that to a 1 year and a half if you do a skill bridge and get out 6 months earlier. Easiest way is just do your time. Don\u2019t ruin your life\u2026"
      },
      {
        "id": "mqhkxga",
        "score": 9,
        "body": "Talk to a chaplain"
      },
      {
        "id": "mqkok8i",
        "score": 5,
        "body": "I can speak from personal experience. I was in your shoes at one point. The difference was, I was in the Air Force and I had signed up for 6 years, but I'll share my experience. In 2016 I enlisted into the Air Force and after going through Basic Training and AIt, I knew that I had screwed up too (or at least I thought I did). I got to my new duty station and my mental health was shit, I wanted out. I had no friends or anyone I thought would understand what I was going through. I thought I'd escape going AWOL and honestly, I did attempt it. I went to an airport to attempt to leave, and I was ready to. My leadership reached out to me several times to stop me. What they did was send a supervisor I trusted and I talked to him. He convinced me to come back to base (of course I had to deal with the consequences, but I was lucky and only got a slap on the wrist for it).\n\nMy leadership convinced me to stick it out and try talking to some of my peers who were around my rank/ age. I learned alot of people have similar feelings and thoughts. I eventually gained a very close knit group that I still keep in contact with. I also finished out my contract and now I'm re-enlisting (joining the army now due to some other issues), Sometimes all you need is people you can talk to and bond with. I promise, you are not alone. Instead of finding ways out, find ways to make your experience better, they are out there. Sometimes, they aren't always what you think they are. \n\nIf you need someone to talk to, you can always reach out to me. I promise I'll listen. We're here for you, you just gotta take the first step."
      },
      {
        "id": "mqha5qf",
        "score": 5,
        "body": "Sounds like OP should have just quit in BCT. Depending on how long he's been in, he could try and get a Chapter 11."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1nvq7n2",
    "title": "Is now a bad time to join?",
    "body": "Hello everyone. Joining the military has been a goal of mine for quite some time now as I think it will set my life up well. But, i\u2019m going to be completely honest, trumps pentagon address really discouraged me from joining, especially as a woman. I\u2019m really upset about my time line being affected, and it is still in my heart and in my plans to join, but should I wait for this all to blow over. Should I wait till 2029 when he\u2019s hopefully out of office. Let me know your thoughts, i\u2019m open to hear anything. \n\nEdit: Planning on joining army, hoping for public affairs or intel. Looking at Air Force as well, but leaning towards army. \n\n\nEdit: I am NOT worried about the physical requirements at ALL. I 100% agree with being held to a high standard in the area. I am worried about civil war and ending up fighting my own people. Especially with trump saying to use cities as training grounds. ",
    "flair": "Should I Join?",
    "score": 56,
    "comment_count": 67,
    "created_at": "2025-10-02T01:08:58+00:00",
    "top_comments": [
      {
        "id": "nhag4ty",
        "score": 27,
        "body": "Go Army if you want to go Public Affairs or Intel, you can actually be job locked.\n\nPresidents go, as do SecDef/SecWar. There is no telling what the landscape will be like in 2029."
      },
      {
        "id": "nhbrmp0",
        "score": 21,
        "body": "It won't make much of a difference, I've served under 3 administration and it's been relatively the same. Plus you're not supposed to talk politics in uniform which I highly recommend you stay away from"
      },
      {
        "id": "nhagaba",
        "score": 15,
        "body": "I wouldn\u2019t wait. What\u2019s to say that Trump leaves and then Vance is voted in his place and Pete stays. That\u2019ll be another 7 years before you join if you solely looking at policy change and even then it\u2019s not guaranteed. \n\nIf your goal is to join the military and your heart says take the jump let your mind say how high.\n\nDon\u2019t let something temporary make a permanent impact on your life."
      },
      {
        "id": "nhbwdp2",
        "score": 9,
        "body": "Join. Don't join because of whos in office, join because you want to change your life. As long as you are physically healthy and fit to join then you are good. Also dont talk about politics in uniform if you decide to join."
      },
      {
        "id": "nhbwnub",
        "score": 9,
        "body": "Why? You can be interested in politics and serve, it makes you more aware of the big picture when you are"
      },
      {
        "id": "nhagan8",
        "score": 7,
        "body": "Realistically, you are going to have all kinds of leaders during your time in service, and if it is long enough, all kinds of administrations too. It is better to have people who care about doing the right thing while in uniform, who want to be professionals, and that alone makes a good enough reason to join now if you were planning to join in the first place. I would consider waiting for the beginning of the year, when the recruiting numbers roll over, and making sure your PT numbers are squared away as there is an even greater emphasis that we will probably see being put on PT standards given the recent speech."
      },
      {
        "id": "nhcg7xw",
        "score": 5,
        "body": "First, way to not read the post. Second, what would you know, being NPS and all?"
      },
      {
        "id": "nhdm10g",
        "score": 5,
        "body": "Bullshit. The military is politics. Look at any unit."
      },
      {
        "id": "nhbri22",
        "score": 3,
        "body": "No one said she had a crap life"
      },
      {
        "id": "nhdjvsn",
        "score": 3,
        "body": "She\u2019s looking at the military. That tells you,"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1lgij55",
    "title": "Air Force guys shitting on me for going Army.",
    "body": "I get a lot of shit from Air Force guys for joining Army. I signed a 17C for Army and I ship in less than a month. I initially tried going Navy for a Cyber Warfare Technician rate, but the classifiers at MEPS refused to give it to me. I looked into Air Force, sat down with an Air Force recruiter, and they made it seem like getting the cyber job I wanted with AF was going to be a lottery- I had to list a bunch of different jobs and they would choose one for me to be based on needs of the Air Force. I get that Army isn't as cushy as AF in terms of QOL, but the AF guys I talk to about it make Army seem like it's the worst decision anyone could ever make. But I really wanted a Cyber job and the Army was the only branch willing to work with me to get that job.\n\n  \n\\*\\*EDIT\\*\\*\n\nLots of positive comments in this thread, very encouraging. I appreciate it. ",
    "flair": "Enlisting",
    "score": 57,
    "comment_count": 48,
    "created_at": "2025-06-20T23:40:58+00:00",
    "top_comments": [
      {
        "id": "mywj8bk",
        "score": 42,
        "body": "Go get 'em. Army Cyber is nothing to feel bad about. Congrats!"
      },
      {
        "id": "mywmd7g",
        "score": 26,
        "body": "Think about it this way\u2026\n\nYou\u2019re guaranteed a job as cyber. But it\u2019s the Army, so you might have to do some Army things once in a while, but think about it as the cost of getting slotted.\n\nPray that you head to Ft Meade, Hawaii, Texas, and somehow avoid the 11th, but considering the numbers, you\u2019re probably heading to Ft Gordon (formerly Eisenhower, now back to Gordon)\n\nEdit: San Antonio was also in the lotto, mb"
      },
      {
        "id": "mywi9kx",
        "score": 25,
        "body": "If you wanna do Cyber and have it locked in, Army was probably your best bet. Most of the units are pretty relaxed, except for the 11th."
      },
      {
        "id": "mywumdb",
        "score": 11,
        "body": "Chair Force here, if you got the guaranteed slot for the Army. Send it. If you decide the Army ain't for you in 4/6 years, then get out, use that GI bill and all the other benefits. BUT take advantage of some of those benefits while you're in if you can. Get those certs, CLEP/DANTES a few classes. Set yourself up with a good foundation if possible even if you decide to stay in longer."
      },
      {
        "id": "mywk1e4",
        "score": 10,
        "body": "Lol the chair force should be the last branch to be talking"
      },
      {
        "id": "mywyy1i",
        "score": 8,
        "body": "I mean, you got Cyber and you won\u2019t be pulling Security Forces in North Dakota, so I\u2019d say you come out ahead."
      },
      {
        "id": "mywn3t4",
        "score": 8,
        "body": "From what I've been told by other Cyber guys, I'm most likely to get sent to Ft Mead or Gordon."
      },
      {
        "id": "myxufst",
        "score": 6,
        "body": "Honestly, you *\u201ddodged a bullet\u201d* \u2026 Air Force \u201ccyber\u201d is a huge clusterfuck, continuously trying to *reinvent and rename* its purpose in life. \n\nArmy \u201ccyber\u201d will offer ample tech challenges and diverse opportunities to *be all you can be* in a military cyber environment. \n\n*Don\u2019t look back, press forward with enthusiasm \u2026 excel on your chosen Army path!*"
      },
      {
        "id": "mywsigl",
        "score": 6,
        "body": "Yup. Them\u2019s the breaks.\n\nKeep grinding away and stay on \ud83c\udfaf. Certs, additional training, networking, finding mentors. Don\u2019t stick around after your 5-6 are done. Go get that \ud83d\udcbc.\n\nEdit: unless you really love being in the Army and would like to switch to warrant or commission AND are highly competitive. I think direct cyber commission for AD got shut down. OCS has 5 slots a year for AD cyber.\n\nOn the bright side, when Space Force cyber finally matures, you might get the chance to jump ship to see how it\u2019s like.\n\nBut cyber is looking pretty good rn. TS-SCI, work experience, maybe a college degree, relevant certs, and veteran status will make you employable."
      },
      {
        "id": "myxp73c",
        "score": 6,
        "body": "I'm at ft Meade. Awesome place to be"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1kdhubx",
    "title": "The job market is horrible. Should I enlist?",
    "body": "I just got rejected by Chick-Fil-A despite being the most qualified. I\u2019m pretty sure I lost the position to a high school seniors or college freshman. This was the last straw.\n\nI\u2019m 22 years old. I thought community college would be the answer\u2026but I\u2019d still be in debt, jobless, and broke. I can\u2019t afford to go to a university\n\nMy financial aid stopped coming in about a year ago and no one in my city is hiring. I have no car either, so I can\u2019t reliably go find work.\n\nAll reviews about my city mention seeking work outside of here. It\u2019s that bad. My own dad can\u2019t even find work. Lots of people here have connection with family in and outside the country\u2026which usually means money. We don\u2019t have either. \n\nBetween 18 and 22, I\u2019ve talked to pretty much every branch. I personally really liked the Marines when I was in high school. I think I\u2019m still interested, but my research on the internet has dissuaded me from it. \n\nI want to enlist to be independent, support my parents, have a salary, find a job that isn\u2019t fucking food related, travel, and to have purpose. Life sucks when you feel like you\u2019re doing nothing.\n\nIt would be nice to not have to worry about money or finding work anymore. I dream of going to a nice school, maybe own a car and a place to live. \n\nTo be honest, I don\u2019t really have any passions. I majored in stuff I found interesting, but I\u2019d say I have a lot of hobbies that I do passively. I tend to hang outside or go anywhere that isn\u2019t home to forget about current situation. It\u2019s a great distraction.",
    "flair": "Should I Join?",
    "score": 56,
    "comment_count": 66,
    "created_at": "2025-05-03T01:53:45+00:00",
    "top_comments": [
      {
        "id": "mqaz6br",
        "score": 52,
        "body": "Do it. The opportunity, benefits, experience, & training is worth it"
      },
      {
        "id": "mqb1tdc",
        "score": 15,
        "body": "I am a sergeant in the national guard, the education benefits alone are worth it. Not only do you get state education benefits you get tuition assistance and credentialing assistance, free tsa pre check, meeting people who you will grow to call your brothers and sisters. It\u2019s great. As far as active duty my wife is a e-3 in the space force. Since we are married we get BAH. As an E3 less than a year in service she alone pulls in 2100 in bah (housing allowance) AND roughly 3k a month for base pay. Name a job that pays 5,100 pre tax plus has a 401k that matches with no experience and trains you in (if you choose it) a civilian transferable skill. It\u2019s not for everyone but if you make the military work for you it\u2019s a great option"
      },
      {
        "id": "mqb1ozi",
        "score": 14,
        "body": "AF right, but you should start with the rate/MOS and then work backwards from there.\n\nYour rate/MOS will dictate your experience during and after far more than your branch.\n\n(And, yes, sounds like a great opportunity for you.)\n\nAll else equal, start by looking hard at intel and anything IT."
      },
      {
        "id": "mqb34y5",
        "score": 11,
        "body": "The military is a great resource, especially for some benefits (like educational, training, money, etc.)\n\nI would get in touch with a recruiter from each branch and shop around again. But keep in mind they are trying to sell you something, so they will cover everything with pixie dust to make it seem better.\n\nAlso, make sure you are mentally prepared. And think for the future, especially if you decide to go the military route. Decide which branch will help you in the long run, and then look at some jobs they offer and decide what you might want to aim for (be prepared, you might not get it).  It is also best to not bank on the idea that you can stay in forever because after your first contract you might decide it isn't for you, so like I said preapre for the future. What can help you succeed in the long run.\n\n\nI don't know a lot about other branches, but I do know some information about the Air Force and National Guard.\n\nThe Air Force is more likely going to help you come out of the military with job ready skills. The Air Force corresponds to more \"office\" work, hence the nickname chair force. Don't get me wrong, you can and will do non office work.\nThe Air Force is \"more\" selected than other branches but a better quality of life.\nNational Guard allows you to stay in the same state, and you do not need to move around, but you will be deployable. It is a one weekend a month and like 2 weeks in the summer. So, it's not a full-time job... but they have amazing educational benefits. That is the only reason I would ever do it.\n\n\nHere is so information relating to education:\n\nAll branches give you a GI Bill that can help you further your education once you are out. This can also be passed to a dependent or spouse if not used, I believe.\n\nThe Army National Guard offers scholarships to students who join and do ROTC at a college. This pathway can lead to becoming an officer. https://nationalguard.com/simultaneous-membership-program\n\nAir Force also has a program for enlisted airmen that helps with education, but I haven't done too much research on it: https://www.afrotc.com/scholarships/enlisted/ascp-soar/\n\nThe military is a great resource. I am a child of an Air Force Veteran, and because of his service, I get benefits. For example, I get free tuition at select schools in my area and receive a monthly stipend from the VA that helps for school.\n\nI will also be joining the AFROTC in hopes of becoming an officer. You can receive scholarships this way. Although the AF is very selected with their officers' picks, The Army, I have heard isn't as selected, and you can also get scholarships that way."
      },
      {
        "id": "mqaz73i",
        "score": 10,
        "body": "I\u2019ll keep this tidbit brief, but I wanted to join the Marines because I could relate to the recruiters at 18. They were there for me when I was going through a rough patch in my life. It helped that they were all Mexicans like me LOL. I felt pretty isolated being Hispanic in an Asian city. It takes its toll on you when you have no one to represent you. A lot of the Poolees I met were all Hispanic too, so I felt welcomed there."
      },
      {
        "id": "mqazwu0",
        "score": 9,
        "body": "I\u2019m staring to think so too. Anything than can get me out of here haha. What branch do you recommend?"
      },
      {
        "id": "mqb00bv",
        "score": 7,
        "body": "Air Force"
      },
      {
        "id": "mqcfesv",
        "score": 6,
        "body": "Yes. Go *active duty* (any service branch), total life / career reset, excel at new challenges / responsibilities / locations, and simply live life to the max! \n\n*Empower yourself* \u2026 commit to positive change, creating new opportunities, earning tangible benefits within a military lifestyle, *until the next best thing comes along.*"
      },
      {
        "id": "mqb06ad",
        "score": 6,
        "body": "I\u2019ll look into them, thanks!"
      },
      {
        "id": "mqb5ewt",
        "score": 5,
        "body": "I'm about to retire after almost 22 yrs in the Army. Loved it. Had its ups and downs, but overall, it was a great experience. If you're looking to one and done, you can really come out ahead, too. Just plan and save! I highly recommend active duty in your position and Army if you may be considering it for 2 or more enlisments, AF if considering one and done. Navy and Marine promotions, even in lower ranks, are so slow that you'll make less in 4 years than your Army counterparts. AF and the Army are closer when it comes to promotions. \n\nGood luck!"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1kp1paa",
    "title": "Lied on the military application",
    "body": "I went on the air force website and filled out the application. One of the questions was did you ever take drugs, specifically marijuana use. I filled out no even though I have used. Two days later I got a call from a representative and he asked me the same question and I still said no. He later said I will get a call from a recruiter two to three weeks from now to set up a meeting. When I see him should I come clean and admit I used. Also, they asked if I was ever arrested but the option was for a felony and not a misdemeanor. Should I come clean about that too?",
    "flair": "Enlisting",
    "score": 58,
    "comment_count": 39,
    "created_at": "2025-05-17T19:52:54+00:00",
    "top_comments": [
      {
        "id": "msuehkp",
        "score": 68,
        "body": "Yea be honest, it\u2019s not that deep, last thing we want is you popping into MEPS pissing hot. But you\u2019re clean then you\u2019re clean and no one really cares to be honest."
      },
      {
        "id": "msug0n3",
        "score": 19,
        "body": "Or, getting caught in your lie at any point during the security investigation or during enlistment itself.. then you're fucking yourself.\n\nProps on you being a recruiter and telling them to be honest."
      },
      {
        "id": "msurpjv",
        "score": 15,
        "body": "They almost certainly won\u2019t find out about past marijuana use if it was casual and not on any paperwork. The arrest though, absolutely tell them about. I went in when I was 24 and had a \u2018Minor in Possession of Alcohol\u2019 arrest from when I was 18 that was \u201cdeferred and scrubbed\u201d. I told them about it and it absolutely was not an issue. \n\nBut as others have said, they really don\u2019t care about past marijuana use like they used to so honesty is your best policy. It\u2019ll also set up the right behavior of honesty if you ever want to get a TS clearance."
      },
      {
        "id": "msuexj9",
        "score": 14,
        "body": "yes and yes you should correct both lies at the recruiter."
      },
      {
        "id": "msumgns",
        "score": 13,
        "body": "tell the truth. They just care so you can go to meps and piss"
      },
      {
        "id": "msulxzu",
        "score": 12,
        "body": "Come clean about everything! They will find out eventually, it\u2019s better to get clean now if you haven\u2019t yet. Tell them about your medical and law history. With the law they could maybe get you a waiver but they might send you to another branch I\u2019ve heard that happens to a lot of people."
      },
      {
        "id": "mswc4tv",
        "score": 11,
        "body": "\u201cWe KNOW! You smoked weed 6 years ago, you cant hide it. I was there, behind the elementary schools garbage bin. I\u2019ve been watching you for 20 years, I know more about you than yourself!!! \ud83e\udef5\u201d Sounds like an average recruiter."
      },
      {
        "id": "msvb8yp",
        "score": 5,
        "body": "They are going to show up at your door and At best you spend some time in Ft. Leavenworth making big rocks into small rocks and at worst, well you don\u2019t want to know\u2026\n\nHaha, nothing will happen and honestly your recruiter is probably annoyed you said anything, but they can\u2019t tell you to lie. Back in my day they didn\u2019t know about anything unless you told them and that was basically what you were told by the recruiter. Here\u2019s the thing, once you are in nobody cares unless you start doing that shit while in. There is no office that digs up dirt on people to say they lied when they went to MEPs. But you can also be prosecuted and fined heavily if they want to make an example out of you should you get caught. \n\nThe key point to take away is don\u2019t ever let your parents put you on medication when you are a minor or take you to a shrink because you can be PDQed for things you had no choice in. Don\u2019t do anything against the law from birth until you go to MEPs and don\u2019t think any of the bad thoughts about checking out early no matter what, because again PDQed. If you do all those things you won\u2019t need to worry about answering those questions and the added hoops you need to jump through."
      },
      {
        "id": "mswsvvy",
        "score": 5,
        "body": "Have you used it within the past 60 days? If so, yes. Tell your recruiter because if you pop at meps you're permanently disqualified from joining military service and you make your recruiter look bad. Also if you're 18 and your test comes out dirty- you could likely face legal consequences. Another tip is not to beat your meat within the 2 days before you go to MEPs, why? Because the protein from your sperm can cause the test to show up dirty. \nIf you haven't smoked within the past 60 days then don't self-incriminate.\n\nPs This should go without saying, don't lie to your recruiter."
      },
      {
        "id": "msx3nk1",
        "score": 4,
        "body": "they\u2019re gonna throw you off of a building and if you survive you\u2019ll end up in jail. that\u2019s what happened to me . you should come clean about everything, it\u2019s better for you & your recruiter,  they just want you to be clean before going to MEPS to take the drug test because if you piss hot , it\u2019s 6 months before you can go back :)"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1lqkeqb",
    "title": "Do people really join in their 30s?",
    "body": "I figured the vast majority of people in the military enlist in their teens or early 20s, but the age limits for each force indicate that some people must join much older than that. Army lets people in up to 35. Navy and Air Force are older than that. \n\nDo people really join at the edge of that limit? Do 30 year olds go to basic with a bunch of 18 year olds? How common is that? \n\nI always saw military service as a potential fallback option if I managed to fuck up my life enough, but now I've apparently got another 7 years with that as an option, when I assumed I was basically useless to the military 3 years ago. \n\nWhat is being a new enlistee at 28 years old like? They must exist, if Army doesn't turn down recruits unless they're over 35.",
    "flair": "Should I Join?",
    "score": 57,
    "comment_count": 82,
    "created_at": "2025-07-03T08:32:59+00:00",
    "top_comments": [
      {
        "id": "n13gkeb",
        "score": 36,
        "body": "It's not uncommon to see guys in their late 20s or early 30s newly join a branch to try out for SOF. Buddy of mine joined at 28 and just graduated USAF PJ training"
      },
      {
        "id": "n14103n",
        "score": 29,
        "body": "34 and leaving in August for basic training"
      },
      {
        "id": "n13eis7",
        "score": 22,
        "body": "Yup. I shipped to basic literally 2 days after I turned 33. Probably would\u2019ve been the next day if there wasn\u2019t a holiday. I wasn\u2019t even the oldest in my dorm, but was in my flight which was integrated between 2 dorms I was the oldest because the other oldest were in the other flight. It really isn\u2019t that bad.\u00a0"
      },
      {
        "id": "n13fmbk",
        "score": 14,
        "body": "Honestly no one really gave me stress or anything. Maybe the dorm chief a bit & one other but other than that the other young bucks made it smooth for me. They treated my like an older brother they could vent to & talk to me about life & they helped me with things without me asking twice. Can\u2019t speak the same for others, but my folks were really cool & they still hmu till this day to talk or check up.\u00a0"
      },
      {
        "id": "n13er75",
        "score": 13,
        "body": "I'm heading to basic at fort benning in September at 24. Every one already in uniform I've talked to has said they went to basic with at least one person in their 30's. It's super common, and yeah the traditional way of joining is straight out of high school at 17-18 but you'll see various different ages."
      },
      {
        "id": "n13et7w",
        "score": 12,
        "body": "I expect people gave you shit over it, but probably not much that you couldn't deal with. At the end of the day the whole point of military is that you're all part of a unit and it doesn't matter where you came from just that you have each other's back when the shit gets rough. Correct me if I'm wrong."
      },
      {
        "id": "n13g5do",
        "score": 11,
        "body": "I had two 41 years olds olds in my OSUT cycle"
      },
      {
        "id": "n14sg7p",
        "score": 9,
        "body": "Don\u2019t let your age discourage - everyone has their own unique timeline. I commissioned as a O-3 with 10 years of civilian nursing experience at the age of 30, now I\u2019m an 0-4.\n\nI supervise a mixture of AF and Army fresh enlisted in their late 30s, I actually prefer that more as they are USUALLY more mature and less issues with accountability."
      },
      {
        "id": "n15o9i7",
        "score": 8,
        "body": "32. Just took my asvab. Waiting to piss clean to go to MEPS. Sometimes you get wrapped up in a job you think you\u2019re gonna be at forever and plans change. That itch has never went away. Better late than never"
      },
      {
        "id": "n15f763",
        "score": 8,
        "body": "I shipped at 25 and was the second oldest in boot, im in the fleet and they call me old man. Just roll with it lol they\u2019ll expect more from you and its all kinda easier to handle because you already have life experience"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1qec0ln",
    "title": "What happens if you cheated on the ASVAB at MEPs?",
    "body": "I was at MEPs the other day taking the ASVAB and some idiot sitting across the table from me possibly a high schooler got caught cheating. He had a hoodie and sweat pants on and thought he was slick by sneaking his phone in googling the answers and got caught by one of the lady working. He was then scolded and escorted out. What happens after that? Fraudulent enlistment or just sent home? Is he ban or just suspended? Have y\u2019all seen this happen before?",
    "flair": "ASVAB/PiCAT",
    "score": 54,
    "comment_count": 55,
    "created_at": "2026-01-16T09:59:02+00:00",
    "top_comments": [
      {
        "id": "nzxwtb7",
        "score": 74,
        "body": "Imagine cheating on a 10th grade test as at least a high school graduate."
      },
      {
        "id": "nzxyimo",
        "score": 28,
        "body": "Facts you gotta be as dumb as a rock to fail it. I been out of high school for 3 years and still passed lol. I feel you could literally get a 30 by just guessing lmao."
      },
      {
        "id": "nzw93tk",
        "score": 23,
        "body": "I haven't seen it happen but when I took my test they made us all take our jackets off and hang them send looked at our pant pockets \ud83d\ude02"
      },
      {
        "id": "nzx6cub",
        "score": 20,
        "body": "They stop the test and ban you from coming back to MEPS for whatever amount of time that the MEPS commander determines. Last one I personally seen was 6 months."
      },
      {
        "id": "nzwdobe",
        "score": 16,
        "body": "He will need to most likely wait 30 days pending any disciplinary action ."
      },
      {
        "id": "nzy3e6b",
        "score": 9,
        "body": "Imagine cheating on the world's easiest test"
      },
      {
        "id": "nzw9x8t",
        "score": 8,
        "body": "Yall didn\u2019t go through metal detectors?"
      },
      {
        "id": "o000kh6",
        "score": 8,
        "body": "You'd be surprised, met a guy who has to go to 09m. Great guy but he scored a 21"
      },
      {
        "id": "nzwapiz",
        "score": 7,
        "body": "I went to a METS site for my test, on Ft Hood. They walk around and stare at your soul fr hahaha"
      },
      {
        "id": "nzwaiaz",
        "score": 5,
        "body": "Wtf? Where did you go to MEPs \ud83d\ude2d\ud83d\ude2d\ud83d\ude2d? All they did at where I went was have us put our stuff in the lockers and ask \u201cyou don\u2019t have a phone or your watch with you right?\u201d And straight to testing room. \ud83d\ude02"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1m9b76w",
    "title": "My guest bringing weed on base",
    "body": "So I\u2019m in the military I don\u2019t smoke any weed and pass all my drug test. However, I am in California and I have family visiting and I want to bring them on base and show them around, but I know they will have weed on them. \n\nBecause weed is federally illegal will they get in trouble if they bring it on a military base? Even tho it\u2019s legal in California",
    "flair": null,
    "score": 51,
    "comment_count": 78,
    "created_at": "2025-07-25T21:17:08+00:00",
    "top_comments": [
      {
        "id": "n55qm5p",
        "score": 95,
        "body": "It's a federal installation, not CA State. They can be arrested for it. Just tell them to leave it at home."
      },
      {
        "id": "n55qu1h",
        "score": 70,
        "body": "Yes. Leave the weed elsewhere. Don\u2019t jeopardize your career."
      },
      {
        "id": "n55sxu2",
        "score": 57,
        "body": "Your family is fucking dumb and so are you if you bring them and weed on base. \n\nThey will be arrested. You probably will too. Are you that stupid? When you escort someone on base you are essentially putting your name on the line as their sponsor."
      },
      {
        "id": "n55wvi9",
        "score": 22,
        "body": "That\u2019s fair, and you are right. To be honest, I think I already knew the answer to my question but just wanted a second opinion from my fellow service members. Yeah it was a stupid question, but the military doesn\u2019t pay me to think lmao"
      },
      {
        "id": "n56srix",
        "score": 21,
        "body": "Also, do not trust them. Make them do a supervised self-search prior to entry. If they refuse, do not allow them to go on base."
      },
      {
        "id": "n55qynb",
        "score": 17,
        "body": "Why is it necessary for them to have weed on them? Explain you aren\u2019t gonna smoke it with them and that they\u2019re gonna be putting themselves and you in trouble"
      },
      {
        "id": "n55wcpb",
        "score": 16,
        "body": "You are right"
      },
      {
        "id": "n55ratz",
        "score": 13,
        "body": "If they find it, they are in deep shit. Do with that info what you will. You say you\u2019re in the military? Come on dawg you know better"
      },
      {
        "id": "n569v7h",
        "score": 7,
        "body": "I had a buddy in a similar situation. Long story short even if you are somewhat involved they will fry you for allowing them to bring any drugs on base. Also make sure they don\u2019t stink of weed because PMO will pull you over."
      },
      {
        "id": "n565ihg",
        "score": 7,
        "body": "Respectfully, I\u2019m a sailor. And I got a 75 on my ASVAB, but the ASVAB doesn\u2019t test for common sense I guess\ud83d\ude2d"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1jihout",
    "title": "Brothers Stolen Valor",
    "body": "Just a quick question, my BIL tells everyone about his war stories.  He served at ft Jackson and worked on the range.  He has a Purple Heart metal but as far as we know he was never deployed. Today he told us he received the metal from being a victim of sexual assault by a superior officer while on base in the United States. Is this even remotely true? Please let me know.  Additionally he has told everyone he was an army ranger even know I know he was only a specialist and he only served 3 years and was supposedly medically discharged.  Can you look up someone\u2019s military career info?\n\nThank you for all your help!",
    "flair": "Branch-Specific",
    "score": 46,
    "comment_count": 30,
    "created_at": "2025-03-24T03:30:36+00:00",
    "top_comments": [
      {
        "id": "mjf9zl5",
        "score": 68,
        "body": "He did not receive the Purple Heart medal for being assaulted."
      },
      {
        "id": "mjfauzx",
        "score": 36,
        "body": "You can submit a FOIA request to pull someone's background. It wont have a ton of personal information, but it will usually have training, entry/exit dates, where they were stationed, etc. \n\nPurple Hearts are awarded for injuries in combat. [https://www.hrc.army.mil/content/Purple%20Heart](https://www.hrc.army.mil/content/Purple%20Heart) Being a victim of SA has nothing to do with Purple Hearts.\n\nSounds like he's full of shit. Lots of phonies claim \"Rangers\" and don't really understand what Rangers actually do."
      },
      {
        "id": "mjfdy5p",
        "score": 17,
        "body": "Here\u2019s what probably really happened. He was kicked out for sexually harassing or assaulting someone."
      },
      {
        "id": "mjg1ap3",
        "score": 16,
        "body": "he also has a medal of honor for still coming in to work with a hangover too"
      },
      {
        "id": "mjgrh71",
        "score": 15,
        "body": "Ask him to show you his DD214. That will list all of his career history. Job titles, awards, promotions, etc. \n\nIf he got a purple heart, it would be on there. If he was a Ranger, it would be on there. If he deployed, it'd be on there.\n\nWhen he tells you he doesn't have the form/the army never gave him one/that's not a form they use/his records are classified, then call him out on his bullshit. Everyone gets a DD214, cover assignments or not."
      },
      {
        "id": "mjgpoyt",
        "score": 14,
        "body": "There is a Purple Heart honor roll. Most Purple Heart recipients are on there but it is voluntary to enroll. So we don\u2019t have to put our name on it.  You could ask him about it. If he truly has a Purple Heart then he would have been contacted by the Military Order of the Purple Heart.  I don\u2019t remember how long it took before that packet was Fedex\u2019d to me.  The list is public so you can look up everyone who chose to put their name on the list."
      },
      {
        "id": "mjfb6eb",
        "score": 14,
        "body": "Sounds like he got \"butthurt\" in combat"
      },
      {
        "id": "mjftbsy",
        "score": 11,
        "body": ">He has a Purple Heart metal but as far as we know he was never deployed\n\n>Today he told us he received the metal from being a victim of sexual assault by a superior officer while on base in the United States\n\nImpossible feat. The criteria is available on Wikipedia. It's not a long list. The described is not even nearly eligible. Google for your enjoyment."
      },
      {
        "id": "mjfdqd5",
        "score": 9,
        "body": "sounds like he's fucking with you \ud83d\ude02"
      },
      {
        "id": "mjfcb8n",
        "score": 8,
        "body": "You can request his military record through public means."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1ludmkf",
    "title": "Im thinking about back out tomorrow instead of going to meps",
    "body": "Someone tell me what to do cause im 26 and just not in shape enough. I feel like boot camp is gonna be hell for someone like me. Am I wrong or what should I do? I was set on going but my family got in my head. Any advice would be appreciated.  I just know I can't back out and if my fat ass can't do boot camp then im screwed lol. Joining army btw.",
    "flair": "Should I Join?",
    "score": 43,
    "comment_count": 68,
    "created_at": "2025-07-08T02:48:03+00:00",
    "top_comments": [
      {
        "id": "n1x5w3h",
        "score": 43,
        "body": "Basic training will get you in shape. It'll help if you're already fit, but you don't need to be fast right now to go far."
      },
      {
        "id": "n1x69pp",
        "score": 14,
        "body": "I think you should go!! the biggest reason that I think u shouldn\u2019t back out is because of regret and the feelings of \u201cshoulda coulda woulda\u201d atleast go and TRY!!!! see how far you can get and get out of your head! also many people go and are not necessarily in shape, I heard bmt will help whip you into shape plus if u end up getting recycled that\u2019s really just another chance to succeed! what did ur family say to make u second guess or why do you feel like u want to back out?"
      },
      {
        "id": "n1x7b4y",
        "score": 13,
        "body": "First, I\u2019d say remind yourself of the reasons you\u2019re joining. You don\u2019t have to explain them to me or anyone else, you should already know what they are.\n\nSecond, you should\u2019ve already been preparing yourself both mentally and physically for what\u2019s to come. \n\nI joined at 32 and it really wasn\u2019t that difficult. The experience might vary from person to person but we all generally go through the same things. There are guys who are PT studs and then others on the opposite end. The only people who didn\u2019t graduate from BCT were the people who quit at some point during the cycle. (Just a heads up, if you quit you don\u2019t get to go home right away. We had guys who quit early on and they were still there with us almost until to the end. I went through infantry OSUT)\n\nAre there going to be moments that suck? Absolutely. Are you going to question your decision to join while you\u2019re there? 100%. But I guarantee, if you follow through with the commitment and make it to the end of your training, you\u2019ll realize it wasn\u2019t that bad and a worthwhile experience.\n\nDo with that information what you will. Good luck"
      },
      {
        "id": "n1x796m",
        "score": 10,
        "body": "As someone who has been through Army BCT,I saw many individuals who had medical profiles, were out of shape, or even missed major events like the Hammer and Anvil. Despite those challenges, many of them still graduated. You\u2019ve got this. As long as you give it your best effort, and push yourself, you can make it through."
      },
      {
        "id": "n1xflq6",
        "score": 9,
        "body": "You\u2019re 26. Act like it. You\u2019ll regret not going after about 4 year\u2019s working shit warehouse jobs."
      },
      {
        "id": "n1x7jj6",
        "score": 7,
        "body": "You\u2019ll be fine. Boot camp is made to get people in shape."
      },
      {
        "id": "n1x7svt",
        "score": 7,
        "body": "Idk your life situation or anything else without context. I only joined the national guard and did just fine and am still perusing other things inside of the guard. \n\nIf you don\u2019t have a good stable career on the civilian side then I recommend it. The military is what you make it. You also are not obligated to go even if you go to MEPS. It\u2019s when you actually ship off and set foot at basic. \n\nSo at the end of the day it\u2019s your life, make a decision and run with it. You\u2019ll either regret it and get out at 30 (assuming your contract is 4yrs) or you\u2019ll reenlist because you love it and gained stability. \n\nAgain, there\u2019s a lot of opportunities with the Army. I have a friend who absolutely loves it and one who hates it (Both active duty guys). \n\nUse me as an example, I decided to enlist instead of being an officer. A lot of people told me it was a dumb idea, but the enlisted life suites me better. I don\u2019t regret it at all and I made that decision and went with it. \n\nIf you pass the qualifications to join then basic will get you in shape. Don\u2019t worry about that, you won\u2019t be the only one who\u2019s out of shape. It can be challenging but in the end you\u2019ll be glad you did it."
      },
      {
        "id": "n1x6d4l",
        "score": 5,
        "body": "also if you back out I don\u2019t think u will get a second chance to join the military"
      },
      {
        "id": "n1y24do",
        "score": 5,
        "body": "^ This, it's no good out here. Get good experience, go to college and get a state job when you get out."
      },
      {
        "id": "n1xd45b",
        "score": 4,
        "body": "They will train you into shape. It's part of the program."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1jyytkz",
    "title": "My Son is stuck in MEPS being discharged. Told it will take 2-4 months.",
    "body": "UPDATE: Hey all thanks for the help and info. I think we may have stumbled upon what is actually going on. Greatly appreciate all of the responses.\n\n\n\nApologies as I get names and acronyms wrong here. Hopefully I end up making sense.\n\nSo my son is being discharged shortly after arriving to Basic training, He arrived in MEPS and never left. Originally being held there for an error in his paperwork. Then told he had to select a new MO or Discharge and re-enlist.\n\nDetails aside he is now sitting in MEPS and has been for the past month awaiting his discharge to process.\n\nHe was informed it would take 2-4 months to discharge or he could wait 4-10 months for a new MO?\n\nSo he selected the discharge as this would be faster. So he could re-enlist and come back.\n\nIs there any way to speed up the discharge process? Anyone I can call or he should be reaching out to?\n\nAlso for context. Why does this take so long to discharge him? and why so much longer for the new MO?\n\nThanks in advance. Please let me know if anything does not make sense. I am getting this 2nd hand, through texts. As he is only allowed to text for 5 minutes a week.\n\nEDIT: Branch is Army",
    "flair": "BCT/BMT/Boot camp",
    "score": 48,
    "comment_count": 77,
    "created_at": "2025-04-14T13:25:55+00:00",
    "top_comments": [
      {
        "id": "mn249fy",
        "score": 136,
        "body": "So he isn\u2019t at MEPS, he is at a basic training in processing center. \n\nI\u2019m going to be honest with you, he isn\u2019t giving you the full story. There is something that came up in either his background investigation, his MEPS, or that he admitted and it is causing him to lose whatever job he originally had booked and be discharged. \n\nThere is really nothing you can do to speed this up. He is at the whims of government efficiency. He will be paid, housed, and fed during this time."
      },
      {
        "id": "mn28yny",
        "score": 53,
        "body": "100% \n\nThey wouldn\u2019t discharge just to change MOS. He got in some trouble"
      },
      {
        "id": "mn2l3d3",
        "score": 23,
        "body": "Ahh the ol MOT (Moment of Truth) strikes again! I bet this is whats happening."
      },
      {
        "id": "mn2ky5e",
        "score": 22,
        "body": "It says he was offered an MOS change, wait 4-10 months for school, but is choosing to get out and come back in?? That part doesn't make sense."
      },
      {
        "id": "mn356py",
        "score": 19,
        "body": "I\u2019m guessing that\u2019s the lie. The kid told that to the parents so the parents maybe wouldnt pressure them to take another job.\u00a0\n\nI\u2019m guessing the parents really wanted the kid to join, kid is getting the boot and wants to save face. They don\u2019t make you change MOS unless your security clearance falls through right? And even then you start boot camp prior to finding out that, no?"
      },
      {
        "id": "mn2pm6a",
        "score": 17,
        "body": "Thanks. After all of the other info and responses on here. I think this may be the case."
      },
      {
        "id": "mn286is",
        "score": 16,
        "body": "The recruiter didn\u2019t lie, your son did. \n\nSomething was found out about his background, either medical or criminal (even if he was never arrested, he could have admitted to something). Because of this new information, he was found unable to do that job. He\u2019s being kicked out of the army now."
      },
      {
        "id": "mn3344k",
        "score": 13,
        "body": "That\u2019s it right there he does not qualify for the MOS he shouldn\u2019t have been able to enlist or ship w/o a valid drivers license for that MOS 37F. He should\u2019ve just chose a different MOS it\u2019s going to take him longer to get discharged, rejoin and ship. He\u2019s most likely now going to have at a minimum of 90 days wait once he gets discharged to rejoin."
      },
      {
        "id": "mn2au2o",
        "score": 12,
        "body": "While you\u2019re probably correct, recruiters have been known to tell a prospect to just skip over something or not to mention something. And that something likely came up, as you said."
      },
      {
        "id": "mn2juii",
        "score": 11,
        "body": "Selecting a new MOS means something in his moral background did not come back good and makes him ineligible for that job. Do you know what job he had when he joined?"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1r4vsoh",
    "title": "Lied at MEPS about food allergy and I ship out in less than a month. What do I do?",
    "body": "Gonna cut to the chase,I lied at MEPS. 1, because my recruiter suggested it and 2, my food allergy didnt pop up on record but I DEFINITELY have it. It was a spur of the moment kidna thing so I lied to the doctor. It\u2019s a peanut allergy. I\u2019ve been tested for my allergy recently and it came back positive but for some reason it didnt show at MEPS? My allergy has never affected my life all and any that I\u2019ve had were resolved with benadryl. Never had to use my epipen even though I have prescriptions on my record (MEPS also didnt see this idk how). I have been looking up some pretty informative stuff but I want a solution to MY specific problem. Do I stay silent and just tough it out or do I come clean and try for a waiver? I ship out March 9th. Also I am going to the Navy.\n\nEDIT: I\u2019ve asked my recruiter over and over again if I\u2019ll be fine in basic or if they\u2019d find out anything and he told me since nothing popped up at MEPS that I should be good. Please guys I need help I\u2019m 19 y/o and I\u2019m stressed out. Idk what to do.\n\nANOTHER EDIT: I\u2019ve never had a documented allergic reaction to my knowledge. Don\u2019t know if that\u2019d help my waiver chances or not.\n\nFINAL EDIT: After reading through your guys\u2019 advice I\u2019ll most likely be calling/visiting the other recruiting station in my city. Hopefully they don\u2019t tell me that \u201cyou\u2019ll be fine\u201d as well. Praying I\u2019ll be able to get a waiver.",
    "flair": "Joining w/Med issue",
    "score": 42,
    "comment_count": 85,
    "created_at": "2026-02-14T21:00:42+00:00",
    "top_comments": [
      {
        "id": "o5eicqa",
        "score": 61,
        "body": "They're going to do some medical processing during p days. Tell them you have allergies that you forgot to mention. Not your rdcs, the hm's and officers you're going to be processing with at medical"
      },
      {
        "id": "o5eixd2",
        "score": 30,
        "body": "From my experience, it would just go on your record. The hospital corpsman and the officers at the Red Rover will not yell at you. They are not rdcs. But you'll get a choice of what you get to eat at The galley while you're in boot camp. In the army we had to just eat whatever unless we had a food allergy and it was on our dog tags. So if they tried to feed us something we were allergic to we could just show them our dog tags. But you most likely won't have that problem. They actually allow you to pick what you eat"
      },
      {
        "id": "o5ein7m",
        "score": 19,
        "body": "what\u2019ll most likely happen?"
      },
      {
        "id": "o5evnww",
        "score": 16,
        "body": "Here's the thing. Peanuts and peanut-derived ingredients will be prevalent in the food at basic training. You said it can be solved with Benadryl. Guess what? You won't have access to Benadryl. Not without going to medical and telling them you have a food allergy, at which point the questions will begin. Continuing without telling anyone is stupid and unethical."
      },
      {
        "id": "o5eje33",
        "score": 15,
        "body": "so it\u2019s unlikely that ill be sent home? thats kinda hard to believe for my mental state right now but i really appreciate it. i\u2019ll take what you say to heart and try it. also, did you have a peanut allergy as well?"
      },
      {
        "id": "o5ek3di",
        "score": 13,
        "body": "No you won't get sent home for that. Just make sure you mention it when you guys do your vaccines. I don't know if they do the peanut butter shot anymore but just make sure to mention it"
      },
      {
        "id": "o5fm8zw",
        "score": 8,
        "body": "It\u2019s not a big deal about lying, especially since your not even in the service yet. They\u2019re going to probably be weird and say that you can go to jail for lying about things, but it\u2019s all a farce. It\u2019s not a big deal. Just, like the other guy said, when you get to medical and they evaluate you at reception, just tell them you have a peanut allergy and they\u2019ll update it. That\u2019s from my experience at the 43rd."
      },
      {
        "id": "o5f1e4x",
        "score": 7,
        "body": "That's going to be noticed by your RDCs. That is not going to be the attention that you want on you."
      },
      {
        "id": "o5fhdnk",
        "score": 7,
        "body": "  They take pretty much anyone and everyone and will figure it out. The only risk is how severe your peanut allergy is since you'll be near people who will probably obsess over the peanut butter parts of an MRE.\n\n  Just keep telling people you have it like your provide/medics so they're tracking. At basic don't let the mood sweep you and when it's time to eat and see someone with allergy causing goods next to you just notify your drill that you need to move. The whole DS act aside. Safety is the priority and none of them should beat you over the head for it. If they do. IG complaint"
      },
      {
        "id": "o5if3no",
        "score": 5,
        "body": "Speak up , get that waiver , and do things the right way . Remember doing things the wrong way always come to light no matter what."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1lcx0iw",
    "title": "Is joining the military the most straight forward path to middle class living?",
    "body": "With the robust benefits that service members receive after just a few years, is joining the military the easiest path to middle class living? In what other situation would a person receive free college and the opportunity for $0 down home loan? Those of course being the two most important aspects of upward social mobility.",
    "flair": "Should I Join?",
    "score": 41,
    "comment_count": 53,
    "created_at": "2025-06-16T16:13:49+00:00",
    "top_comments": [
      {
        "id": "my3rt3e",
        "score": 41,
        "body": "No other job is going to give you those benefits, it was extremely helpful but it also comes down to your work ethic AFTER you get out. There are tons of homeless vets because for one reason or another they couldn\u2019t get it together after getting out. Whether that was from drugs/alcohol, laziness, poor financial decisions, etc.  \n\nIt\u2019s entirely up to you to make those benefits work for you. I used the GI bill, got a great paying job, used the VA loan for my first house, sold it, used the loan again for my next house."
      },
      {
        "id": "my5a9to",
        "score": 8,
        "body": "Depends on what rank you retire as really. And even then if you enlist at 18 and retire after 20..\nYour 38 years old and can pick up another job to retire inaddition"
      },
      {
        "id": "my3stmm",
        "score": 5,
        "body": "Right you just have to take what is offered"
      },
      {
        "id": "my44ue2",
        "score": 5,
        "body": "It\u2019s the middle class handed on a silver platter. You just have to accept"
      },
      {
        "id": "my49ary",
        "score": 5,
        "body": "Is that difficult? Not in my experience, unless you\u2019re a dumb piece of shit. The only people I ever saw not get an honorable were criminals and pot smokers.  \n\nWant an honorable? Don\u2019t break the law. Follow your orders. Don\u2019t do drugs. Simple as shit."
      },
      {
        "id": "my3tczh",
        "score": 4,
        "body": "If your starting off with nothing I would say yes, if you pick an MOS that gives you a civilian equivalent (88M can get a CDL very easily, stuff like that) that gives you the pay your looking for. Do a 4 year contracting you're pretty good, may not even need to go to college, and you could still get the health benefits by transitioning to reservist.\u00a0\n\n\nDefinitely depends on your starting situation, and what type of job you want in the future, might just be better to start off civilian, IT for example, you just need a certification, started at an entry level and work your way up."
      },
      {
        "id": "my5xyyn",
        "score": 4,
        "body": "Thank you so much for your reply. I actually just got my paperwork approved for the Navy, but I was looking into the military for experience since it is hard to get hired for any civil service without experience. I mainly want to get into a trade, or a city job with benefits. I am 29 years old so I am at a crossroads in life"
      },
      {
        "id": "my4745x",
        "score": 4,
        "body": "Stop being jaded dude. You\u2019re 21. \n\nbuy a house, sell that house, buy a bigger house or reinvest it into another house, turn it into income. Buy, fix, flip, repeat. \n\nMy current mortgage is like 3000 a month, rent for a similar sized house is like 7,000.  That\u2019s an extra 48k a year I can put back into my home, or another investment. The benefits you get set you up for success. If you choose not to do anything you\u2019re going to fail. \n\nIm solidly upper middle class in southern California because of the benefits I received and used to set up my foundation."
      },
      {
        "id": "my40mpg",
        "score": 3,
        "body": "The military can be a huge level up. Here's some points for you:\n\nTrying to get your first job can be tough - no experience. Maybe you're lucky and get a sweet internship, good luck. On the other hand, a high speed servicemember comes out with military-level training (super valuable in tech fields), EXPERIENCE, and likely a security clearance that opens up wide fields of employment not available to anyone who doesn't qualify for a clearance. That triple combo of training, experience, and clearance, is a huge advantage. \n\nG.I. Bill is huge. Look at the details. You can use it for all kinds of things. You get a stipend if you use it after getting out. \n\nVA home loan - I used it. Made it possible for us to buy a house. \n\nOf course you can succeed in many other ways - good connections, trade school, merchant marine, what have you. Good luck and best wishes."
      },
      {
        "id": "my7dp6y",
        "score": 3,
        "body": "Cyber security is hot though. Huge money to be made if that\u2019s part of your goal."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1lrxaq6",
    "title": "Why are prior service civilians unwanted by recruiters?",
    "body": "Reading posts, it seems recruiters don't like working with prior service civilians who got out and want to get back in, and would rather deal with wholly new people. \n\nWhy is this? I feel like it should be the opposite, where if someone has proven experience with a branch of the military, they should be considered a good investment if they want back in.",
    "flair": "PS",
    "score": 39,
    "comment_count": 38,
    "created_at": "2025-07-05T00:19:46+00:00",
    "top_comments": [
      {
        "id": "n1e9mod",
        "score": 52,
        "body": "Prior service members often have claims with the VA, medical complications or disqualifications since they got out, or need age waivers. It\u2019s more work for the recruiter than a 22 year old who had asthma when he was 8."
      },
      {
        "id": "n1eao8k",
        "score": 32,
        "body": "Former Recruiter back in the day.\n\nSad to say but it was seen as a lot of extra work. More often than not, PS had to take a reduction of rank if E5 or above and they only had certain MOS open based on needs of the Army. The Army viewed it like 'well well well, look who decided to come back'."
      },
      {
        "id": "n1e9zan",
        "score": 30,
        "body": "I knew one guy who came in prior service (army to army), he said he needed waivers bc when he was deployed he got blown up.. has metal plates in his legs.. he got in and is in the army band. Seems like it\u2019s just more of a hassle as opposed to some fresh and healthy 18-22 year old kid out of school"
      },
      {
        "id": "n1eckux",
        "score": 28,
        "body": "You call it \u201cproven experience\u201d but what most experienced recruiters see is \u201cdocumented history of issues\u201d"
      },
      {
        "id": "n1eax6c",
        "score": 11,
        "body": "They likely have baggage whether they like it or not, for some branches like the Air Force Active Duty they want homegrown people not other services folks with a chip on their soldier.\n\nSomebody fresh off the street doesn't really know the in's and out's while you'll have PS people try and rules lawyers their way and cite regs all the time.\n\nBiggest thing is probably the sense of entitlement."
      },
      {
        "id": "n1ed655",
        "score": 10,
        "body": "Is there an element of encouraging soldiers to re-enlist to this? As in, don't give up on the Army or else you'll lose future opportunities with us if you change your mind."
      },
      {
        "id": "n1ee5zx",
        "score": 9,
        "body": "Prior service, require A LOT of paperwork whether they got out honorably or otherwise. Some require waivers. But the biggest issue is job selection. PS are significantly limited on what they are able to choose from compared to non prior service."
      },
      {
        "id": "n1eegvs",
        "score": 8,
        "body": "Yes. They push retention pretty hard and plenty of people reenlist. All branches do that. Part of the mentality."
      },
      {
        "id": "n1eigdb",
        "score": 6,
        "body": "It's more work for them since PS guys often got baggage and thus have to jump through more hoops (they'd much rather prefer \"clean\" guys with no prior connection to the military). Not un-doable to get them in, but recruiters get the same amount of credit for enlisting someone no matter how much work it takes, so why work harder for the same payoff? (I've been trying to reenlist for more than 2 years now and it's been a pain, on my second recruiter; most people would have just given up by now.)"
      },
      {
        "id": "n1epe31",
        "score": 5,
        "body": "Priors expect to come in at a higher rank (get paid more), yet still need to be trained and qualified just like a brand new recruit."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1qow98q",
    "title": "Did anyone join the military straight out of high school with basically no social life?",
    "body": "I\u2019m about to join the military and I\u2019m coming straight from high school.\nI didn\u2019t really have much of a social life no parties, not many friends, mostly stayed in the house all my school years and focused on getting through school. I just wanted to know how its going for others in a similar situation ",
    "flair": "Should I Join?",
    "score": 41,
    "comment_count": 22,
    "created_at": "2026-01-28T00:43:44+00:00",
    "top_comments": [
      {
        "id": "o24lr38",
        "score": 18,
        "body": "I just got two new troops fresh out of HS that were homebodies. They are...adjusting, to say the least."
      },
      {
        "id": "o25b53p",
        "score": 8,
        "body": "A buddy of mine joined the Navy straight out of high school, he was a homebody and was very self persevered, after he came back from his tech school, brother was a whole different person, and I mean it in a good way. Great social attitude too, so you\u2019ll be fine."
      },
      {
        "id": "o258jio",
        "score": 7,
        "body": "In 1965, I graduated from Lakes High School, Lakewood WA, and I wanted to go to college. My family could not financially help me because they had nine children, and I was the oldest. It did not help that I was of Hispanic origin, and there was a large Scandinavian presence in Washington State. There were no minority scholarships, no FAFSA, no outreach for minorities to attend college. During my early school years, I had to work as a \u201cnewspaper boy\u201d delivering the Tacoma News Tribute to earn money to buy school supplies, and to help my family. Money was tight and I could not even afford to go to the Senior Prom in 1965. During my high school years I really did not have the opportunity to establish \u201csocial friends\u201d in after school clubs because I had a newspaper route and from time to time help my father with his second job(s).\n\nI did not want to look for a job in the Tacoma area because I could not afford a used car, no bus service, and I would take up valuable bedroom space if I stayed home and walked to a job. So, in June 1965, I reached out to the Army recruiter who immediately signed me up for the Army Security Agency (ASA). In seven days, June 14, 1965, I was shipped to Fort Ord for boot camp, ASA School at Fort Devens MA, then assigned to the 104th ASA Security Detachment at Torri Station Okinawa. I was finally earning money on my own, had three hot meals a day, and a metal bunk bed in large barrack\u2019s bay (room).\n\nIn the Army, I made friends, visited local tourist traps on Okinawa, and enjoyed our local MWR recreational facilities. I even visited South Vietnam on TDY in early 1966. I finally transferred PCS to South Vietnam in November 1966. I made friends with my Army buddies (note: the Army did not use \u201cBattle Buddies\u201d until 2000).\n\nI was offered a 6-month early discharge because of my extensive in-country assignments. My active-duty service ended in January 1969 when I was sent from Saigon to Fort Lewis WA, via Oakland Processing Station. I have no regrets in serving in the Army or in Vietnam. I personally felt that I matured as a person, learned about life, and I made it out alive."
      },
      {
        "id": "o24mhm3",
        "score": 6,
        "body": "Yea i expected it would be some type of adjusting period appreciate the honesty"
      },
      {
        "id": "o24kkai",
        "score": 5,
        "body": "Well, i had 1 friend in hs.. i always had a tight circle.. went to college. Studying and work non stop.. wore me down even more\u2026 went to military and now im happy with new connections im making having the best time with new friends! Its very great. I was choosing the branches marines or army, and oh well army won my heart."
      },
      {
        "id": "o2648kq",
        "score": 3,
        "body": "Yeah me I got like 4 friends which I rarely see I go to school online which means I basically never leave the house and I play games all day. I graduate early and I did meps a week ago I had to get a waiver but yeah don\u2019t know how it\u2019s going to be in the army."
      },
      {
        "id": "o298n9v",
        "score": 3,
        "body": "My last unit I had a Soldier like that. Very sheltered, quiet, shy. Didn\u2019t even know how to drive. My section taught him driving, social cues, getting comfortable enough to the point he would start roasting us and making us laugh. Sometimes the people you work with can help you grow and develop"
      },
      {
        "id": "o2592z8",
        "score": 2,
        "body": "No regrats"
      },
      {
        "id": "o27awlu",
        "score": 2,
        "body": "Happens all the time, it works well for most because there is a very defined hierarchy so most of the social interactions will be with people of the same standing and experience."
      },
      {
        "id": "o28drzb",
        "score": 2,
        "body": "Air Force is the better option for someone who\u2019s a homebody or more socially introverted. Army needs a battle buddy literally to go everywhere while in training and if you\u2019re in AIT for a long period of time, can be extremely draining. They also have better barracks/dorms for those going active and required to live in base"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1jki784",
    "title": "Is it too late for me to join the army?",
    "body": "Title says it all. I'm a 28-year-old loser who's going to be 29 in a few months and I'm going nowhere fast. I wanted to join the army and pick a Paralegal MOS but I'm over the weight limit by at least 20 pounds, can't even run a mile, and can barely do 20 push-ups. I wanted to join when I was younger but I'm an idiot who went along with what my parents wanted instead of thinking for myself and doing what I wanted. Some people in my life have suggested I just join anyway, but I've heard too many people say I should get in shape first before getting into basic training. I'm afraid that by the time I get in shape I'll be too old to have a long career in the military. Should I still try to join or is it too late for me?",
    "flair": "Should I Join?",
    "score": 38,
    "comment_count": 51,
    "created_at": "2025-03-26T18:00:58+00:00",
    "top_comments": [
      {
        "id": "mjvg6ro",
        "score": 44,
        "body": "I joined in 2004. Had many guys in their 30s.\n\nAs far as being in shape: i couldn't run a mile either and literally could only do ONE pushup. The Army will get you where you need to be."
      },
      {
        "id": "mjvldzb",
        "score": 16,
        "body": "The Army WILL get you there!!! But will you LET the Army get you there. If you put in your all, you will become the absolute best version of yourself. It\u2019s never too late to join."
      },
      {
        "id": "mjvghnf",
        "score": 15,
        "body": "I see. I'm just cautious that I'll fail the PT test but it sounds more and more like it is what you say. The Army will get me there."
      },
      {
        "id": "mjvkotb",
        "score": 11,
        "body": "They'll get you in shape as long as you put effort it, but dont wait to get in shape. Start now."
      },
      {
        "id": "mjvgqrc",
        "score": 9,
        "body": "We had a guy who was 41 in osut"
      },
      {
        "id": "mjvk2zj",
        "score": 7,
        "body": "I did OSUT (One Station Unit Training) so Basic & AIT were combined so to speak. I didn't pass the last PT Test for Basic Training (missed run-time and pushups).  I would finally pass it a few weeks into AIT.\n\nI did 0 preparation for Basic and I had like 8 months to prepare. Don't be like me haha."
      },
      {
        "id": "mjvmlc9",
        "score": 6,
        "body": "Got it, at the very least I've been putting work in but I'll be redoubling my efforts now"
      },
      {
        "id": "mjvhnq4",
        "score": 5,
        "body": "You\u2019ll be fine.  They lowered the ASVABs a while back as well.  If you want in they\u2019ll find a way"
      },
      {
        "id": "mjxafgt",
        "score": 5,
        "body": "Max age to join the Army is 35. If you're overweight the recruiter will go do PT with you until you make weight (a good recruiter will). You've got plenty of time. I couldn't run a mile when I joined. Ended up being as fit as I've ever been and went to a lot of schools I never imagined I'd be doing. If you put your mind to it and don't give up, you can do it. Go for it man."
      },
      {
        "id": "mjxl9b8",
        "score": 5,
        "body": "Take the plunge or regret it 5 years from now tbh."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1khu35l",
    "title": "Is it too late to join the military?",
    "body": "I'm a 38 year old male. I have thought about joining millions of times over the years. Is it too late for me? Is there any branch that would take me? How hard will it be for someone at my age. ",
    "flair": "Should I Join?",
    "score": 37,
    "comment_count": 54,
    "created_at": "2025-05-08T16:15:30+00:00",
    "top_comments": [
      {
        "id": "mr9olxg",
        "score": 26,
        "body": "Talk to a Recruiter. Army is most likely to take you. \n\nIn fact, I know a nationwide Recruiter who might be good for you to work with."
      },
      {
        "id": "mr9rlxa",
        "score": 15,
        "body": "Just got waiver for age I\u2019ll be 42 when I ship. Can ship in army up to 43rd bday"
      },
      {
        "id": "mr9pm1l",
        "score": 11,
        "body": "[deleted]"
      },
      {
        "id": "mrbx9aq",
        "score": 8,
        "body": "I heard a story from my recruiter of how a guy trying to enlist already started the process in Air Force yet 7 months later he still didn\u2019t hear back from the Air Force recruiter. From the sounds of it their quotas are so low they don\u2019t really prioritize recruiting \ud83d\ude2d"
      },
      {
        "id": "mrapu4a",
        "score": 7,
        "body": "Joining shouldn't be a big issue. You're dqd from being a pilot in the air force because of your age, but that's pretty much it."
      },
      {
        "id": "mrbnb1m",
        "score": 6,
        "body": "That was also a Direct Commission as a JAG. DC has its own rules."
      },
      {
        "id": "mrdwkzs",
        "score": 6,
        "body": "No"
      },
      {
        "id": "mrememd",
        "score": 5,
        "body": "[removed]"
      },
      {
        "id": "mrcpkha",
        "score": 4,
        "body": "Husband is an Army recruiter and the cutoff is 42 which would mean youd probably be able to join the Army if you meet all the other qualifications-not too late! Not sure about other branches though. Reach out to a recruiter."
      },
      {
        "id": "mr9yk3v",
        "score": 4,
        "body": "Hunter Biden joined the Navy at like 40 although who knows if his pops had to pull any strings."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1qy2myo",
    "title": "Fired after informing employer I was joining the Air Force \u2014 they called it a \u201cresignation\u201d",
    "body": "I work as a project supervisor for a roofing company. I have worked here for 9 months, I disclosed that I was in the process of joining the U.S. Air Force in October. They acknowledged it and just asked that I give them notice once I had a ship date. I told them I didn\u2019t know when that would be yet, but I would inform them as soon as I received it , whether that was a week, two weeks, or longer.\n\nI have not received a ship date yet.\n\nToday I went to work like normal, completed my job for the day, and around 3 PM I received a text from my Manager asking me to come to the office after I finished. Around 5 PM I went to the office and my manager got with me and explained that they were essentially letting me go because of me joining the Air Force and saying that they had to cut down on budget costs. \n\nThey said I was being \u201clet go,\u201d but then had paperwork stating it was a resignation.\n\nThere was no prior warning, discipline, performance issues, or notice, I showed up for a normal workday and was terminated the same day. After speaking with the Owners they said that I had resigned as soon as I gave them notice that I would be leaving for the Air Force but previously we came to an agreement that I can work here until I get a date to leave and then give them my notice. Now once it came down to them no longer needing me anymore through a new hire they decided to say I was resigning, basically a forced resignation but I had no heads up on any of it and it was dropped on me on a Friday right before going home. \n\nThe only notable circumstance is that they were aware I am entering the Air Force and would eventually be leaving once I receive a ship date.\n\nSo I\u2019m trying to understand:\n\nIs any of this legal? \n\nIs there any laws out there protecting me because of this?",
    "flair": null,
    "score": 38,
    "comment_count": 29,
    "created_at": "2026-02-07T03:14:22+00:00",
    "top_comments": [
      {
        "id": "o40qvpr",
        "score": 42,
        "body": "No, none of that is legal. I hope you didn\u2019t sign any of that nonsense.\n\nYou are protected by a federal law called USERRA. Even if/when you do ship, they are required to reemploy you if you are gone for less than 5 years.\n\nhttps://www.dol.gov/agencies/vets/programs/userra"
      },
      {
        "id": "o42dxzi",
        "score": 17,
        "body": "They pushed the resignation paperwork on you so the paper trail shows you quit instead of them letting you go. It's to cover their ass so you can't say they illegally fired you."
      },
      {
        "id": "o40wxsv",
        "score": 12,
        "body": "Had the same thing happen to me. Informed my employer that I would be leaving to the coast guard but instead of firing me I was just treated horribly. \n\nI decided to just quit the job to not have to deal with all the BS . \n\nMy advice to you is don\u2019t let them know until you have a ship date already. \n\nAlso I\u2019m pretty sure you\u2019re protected by law. DONT sign any resignation papers!!!"
      },
      {
        "id": "o43k3ck",
        "score": 12,
        "body": "ESGR Ombudsman Director/ESGR National Trainer here.\n\nNo. It is not legal. Even though you have not actually joined the military yet, the Uniformed Services Employment and Reemployment Rights Act (USERRA) protects you even now. First, the employer cannot discriminate or retaliate against you where your uniformed service (or protected activity) was \"a motivating factor\" in the adverse employment action. 38 USC 4311. \"the person\u2019s activities or status need be only one of the factors that \u2018\u2018a truthful employer would list if asked for the reasons for its decision.\u2019\u2019 \u2018\u2018Military status is a motivating factor if the defendant relied on, took into account, considered, or conditioned its decision on that consideration.\" Significantly, it does not have to be a \"but for\" cause, merely one factor out of many. In your case, there is *direct* evidence that your plans to enlist was \"a  motivating factor\" in their decision since they told you it was.\n\nAs a prospective recruit, USERRA gives you additional protections. For instance, any examinations to determine eligibility for military service, such as MEPS, is considered uniformed service, 38 USC 4303(13), and the employer must allow you to take time off for such examinations and reemploy you after wards. 38 USC 4312; 38 USC 4313. Also, if you go into the delayed enlistment program (DEP), any required musters for a military purpose are considered uniformed service (outings to the ball park are not). Finally, you can work up until you have to report for basic training, or you can take some time off *before* your service to get your affairs in order pursuant to 20 CFR 1002.74.\n\nFinally, you should become familiar with ESGR. It's a DoW program to assist service members with civilian employment issues. You should contact them at [ESGR.mil](http://ESGR.mil) (800.336.4590) to request assistance. A trained Ombudsman will contact you and mediate to get your job back. If unsuccessful, they will refer you to DOL-VETS, which has the power to investigate possible violations. Eventually, you can have it referred to the Dept of Justice. Or, if you wish, you can retain your own attorney. However, if you do, ESGR and DOL-VETS will not assist you.\n\nI post regularly regarding USERRA issues at r/ESGR_USERRA_Answers \n\nEDIT: Some other points. As noted elsewhere, you are protected for up to 5 years cumulative non-exempt service. An initial enlistment for active duty is all non-exempt, but as long as you don't exceed 5 years by reenlistment or extension, you should be good. Also, even if you signed a \"resignation,\" that is unenforceable, and you maintain your reemployment rights regardless. 38 USC 4302(b); 20 CFR 1002.88."
      },
      {
        "id": "o42pglq",
        "score": 8,
        "body": "Oof sorry man. You shouldn\u2019t have signed that paperwork. Still reach out to an employment lawyer they might know something I don\u2019t"
      },
      {
        "id": "o45zx0n",
        "score": 4,
        "body": "You have been the most helpful comment I have had yet. Thank you, this really means a lot to me."
      },
      {
        "id": "o4538ug",
        "score": 4,
        "body": "What you don't know is that an employee cannot waive their reemployment rights under USERRA. 38 USC 4302(b); 20 CFR 1002.88. It can be explicit, signed under oath, notarized, etc., but it will still be unenforceable. "
      },
      {
        "id": "o42pr26",
        "score": 3,
        "body": "They got you with the paperwork, but you are protected by a federal law under USERRA"
      },
      {
        "id": "o4488yi",
        "score": 3,
        "body": "Yea, the real lesson here is never letting a job know your plans until you absolutely have to. They\u2019ve been doing the same thing if ppl put in their two week notice."
      },
      {
        "id": "o47bos4",
        "score": 2,
        "body": "No it\u2019s not legal. If they cut you loose that\u2019s a layoff not a resignation. First thing apply for unemployment. Then get legal advice."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1nn8zrs",
    "title": "Why Do Soldiers Marry Strippers?",
    "body": "I\u2019m enlisting soon, but I have to ask. Why do soldiers marry strippers? It\u2019s one thing to go to the club, get a lap dance and maybe hookup with a dancer, but why marry said dancer? A vet I talked to not long ago put it this way when it comes to being successful in the Army.\n\nLesson 1: Don\u2019t ever have kids while in the Army.\n\nLesson 2: If you do want kids, do not meet the mother of your children in a skin joint.\n\nLesson 3: If you do get married to a stripper for either the kids or benefits, don\u2019t ever expect her to change her ways.\n\nI don\u2019t know if this is true overall or if there are exceptions, but what was your experience and how did it turn out for you?",
    "flair": "Enlisting",
    "score": 36,
    "comment_count": 27,
    "created_at": "2025-09-22T01:04:10+00:00",
    "top_comments": [
      {
        "id": "nfituil",
        "score": 56,
        "body": "Lonely dudes first time with a woman. She knows she\u2019s going to get benefits so she agrees."
      },
      {
        "id": "nfiuetb",
        "score": 13,
        "body": "What this guy said"
      },
      {
        "id": "nfj2kdb",
        "score": 12,
        "body": "I personally know one guy who married a stripper after a 2 week relationship after we came back from Iraq, another guy married the barracks bunny lol. She cheated on him while we were in Iraq the entire time. We came back and he refused to divorce her because he thought they could make it work, make it work while her new boyfriend lived in their trailer and he slept in my closet in his sleeping bag and puss pad."
      },
      {
        "id": "nfjwone",
        "score": 8,
        "body": "Lol this shit has been going on since the beginning of time.\n\n It's easy to explain lessons 1,2, and 3 to soldiers but give them a bunch of cash and some alcohol and logic goes completely out the window."
      },
      {
        "id": "nfj0g9f",
        "score": 8,
        "body": "That\u2019s depressing"
      },
      {
        "id": "nfjn72y",
        "score": 7,
        "body": "Boobies. Duh."
      },
      {
        "id": "nfiymg0",
        "score": 7,
        "body": "Ah a question as old as time itself"
      },
      {
        "id": "nfjo2bs",
        "score": 5,
        "body": "Young, lonely and a pocket full of cash. Chasing that sweet BAH."
      },
      {
        "id": "nfjdtjw",
        "score": 4,
        "body": "\u2026I have no words, honestly."
      },
      {
        "id": "nfkqxte",
        "score": 3,
        "body": "I married a stripper when I was in the Air Force. We met in 94, got married in 96, and are still together to this day."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1m5td1q",
    "title": "Discharged from the Air Force Due to Alcohol Abuse \u2014 Now Seeking Guidance on RE-4 Upgrade",
    "body": "I joined the Air Force right after high school at 18 years old. In order to enlist, I had to stop smoking marijuana to pass the drug screening \u2014 my recruiter was aware. After I quit smoking, I picked up drinking instead, mostly hard alcohol. At the time, I didn\u2019t think much of it since there were no real consequences beyond hangovers and the occasional humiliation.\n\nEventually, I received my AFSC (2W1) and ship date: February 2018. Going into BMT, I was in top shape and qualified for Warhawk right away (not that it\u2019s hard or matters much). I graduated BMT with my flight and was assigned to Sheppard AFB for tech school.\n\nWhen I arrived at Sheppard, I felt a sense of freedom \u2014 understandable after coming out of BMT. During the first week, around 8 PM, we all had to line up in the dorms for a random breathalyzer check. I hadn\u2019t been drinking, so I blew zeroes. The Technical Sergeant said, \u201cThis will be the easiest test you ever pass.\u201d At the time, I believed him.\n\nEventually, I got access to alcohol through another Airman, and that led to drinking on the weekends \u2014 sometimes even during the week as graduation approached. I kept it hidden and never wanted anyone to know I was drinking. I managed to finish tech school without getting caught.\n\nAfter graduation, I took two weeks of leave. On my very first night home, I got blackout drunk. My mom told me she thought I might have a problem, but I denied it. I drank the entire two weeks and then reported to my first duty station: Ellsworth AFB.\n\nIt didn\u2019t take long before I received my first LOC \u2014 for skipping PT. I thought it wouldn\u2019t be a big deal, but I was wrong. I never skipped PT again, but I still racked up a few more LOCs. My drinking habits from leave continued, and I spent most of my off-time drinking. Eventually, I started drinking before shift. That obviously escalated things quickly.\n\nLOCs turned into LORs. LORs turned into an Article 15. The drinking was snowballing. It all came to an end when I showed up drunk to a class after lunch break. I was pulled aside and sent to the base hospital, where my blood alcohol level came back over 0.2. That was the final straw.\n\nMy command had gathered enough evidence. I received notice to pack my bags \u2014 the Air Force no longer wanted me.\n\nIt\u2019s now been over five years since I got out. I\u2019ve been through multiple rehab programs, and I can honestly say that my drinking was a serious problem that hurt not only me but those around me. I\u2019m 26 now, and I\u2019ve built up a decent amount of sobriety. Looking back, I didn\u2019t fully grasp what a blessing the military was. It still pains me to think about, but life is full of mistakes \u2014 some bigger than others.\n\nNow, I have a strong desire to try and reenlist. I know that upgrading an RE-4 code isn\u2019t easy or guaranteed. But I\u2019d rather give it everything I\u2019ve got and be denied than live with the regret of never trying. I\u2019m putting this out into the universe with no expectations. Maybe someone out there can help. Maybe this helps someone else. Maybe it matters, maybe it doesn\u2019t. \n\n\u2e3b\n\nTL;DR:\nI developed a serious drinking problem that got me discharged from the Air Force. I\u2019ve been sober for a while now and want to upgrade my RE-4 code so I can try to reenlist.\n",
    "flair": "PS",
    "score": 36,
    "comment_count": 106,
    "created_at": "2025-07-21T20:03:17+00:00",
    "top_comments": [
      {
        "id": "n4fncop",
        "score": 8,
        "body": "The military isn't for you man. Congrats on getting sober - stay that way, but it's time to move on to something else."
      },
      {
        "id": "n4i38k0",
        "score": 7,
        "body": "Congrats on being sober, it\u2019s a huge accomplishment. \n\nHowever, this chapter in your life is over- time to move on homie."
      },
      {
        "id": "n4f1iai",
        "score": 7,
        "body": "Even with an upgrade, you'll require a waiver. The Army has requested 2 years sobriety post rehab from an applicant I had before."
      },
      {
        "id": "n4pzmv7",
        "score": 6,
        "body": "to be honest man\u2026. As a Navy Veteran who got Admin-Seperated due to Marijuana and also received a RE-4 back in 2021 . I would say shoot for your VA Disability and benefits instead of tryna further damage your brain and body or possibly relapse on the Alcohol.\n\n I know it\u2019s some traditions and parts of the military that is unforgettable and hard to let go off but , Ask yourself why did you start drinking so much after you got in ? , what things happened in the military that persuaded you to drink so much? What things happened AFTER you were separated due to the drinking the military has caused. \n\nThat\u2019s just my two cents . or maybe 5"
      },
      {
        "id": "n4fgk97",
        "score": 4,
        "body": "RE-4 separation code basically tells the entire US military you are dead to them. You will never be able to rejoin, and you can try to get it upgraded but you have like a 2% chance of that happening. You fucked up and now it\u2019s time to live with it bro"
      },
      {
        "id": "n4f71n9",
        "score": 4,
        "body": "AD air force is gonna be out of your hands. But if you upgrade your code, maybe guard or reserve. Huge maybe"
      },
      {
        "id": "n4xjtsk",
        "score": 3,
        "body": "Don\u2019t get Sober because you want to get back in the military. Get sober because you want to impact your own life and others."
      },
      {
        "id": "n567fe0",
        "score": 3,
        "body": "Sounds like you\u2019re trying to relive something you lost, like trying to get an old girlfriend back. Never a great idea. \n\nMaybe think smaller. ANG?"
      },
      {
        "id": "n53ct3e",
        "score": 3,
        "body": "just to be sure, you are not going at the OP, correct?  he already said he most likely wont try for disability.\n\nalso, there are other reasons than combat that someone may turn to the bottle and you shouldn't discount those.  i know of several people on my boat that became alcoholics because life on the fast attack was complete dogshit.  it was harsh.  a lot of divorces and just completely low morale caused by a captain that didnt give a shit about his crew.  for example, we had a stores loadout issue caused by the captain.  did he take the blame?  hell no.  our supply officer and the mess cooks were blamed and got letters of reprimand for something the captain failed to do.  it's not like they could just quit and find another job.  you dont have that option in the military.  also, good luck being sexually assaulted or mentally tormented and getting any relief from that, at least thats how it was 10 years ago or so."
      },
      {
        "id": "n4egqbo",
        "score": 2,
        "body": "**DQ standard(s) (requires waiver(s))**:\n\nAny history of substance-related and addictive disorders (except using caffeine or tobacco).\n***\nThis sub cannot definitively tell you whether you're eligible. Waivers are decided on a case-by-case basis. Contact your local recruiter.\n***\n***\n**Jobs mentioned in your post**\n\nAir Force AFSC: [2W1X1 (Aircraft Armament Systems)](https://www.airforce.com/careers/science-and-technology/aircraft-armament-systems)\n\n^(I'm a bot and can't reply.) [^(Message the mods)](https://www.reddit.com/message/compose?to=/r/Militaryfaq&subject=MilFAQBot) ^(with questions/suggestions.)"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1qb1dyi",
    "title": "Recruiter said I can\u2019t join for the MOS i signed for.",
    "body": "Basically what the title says. On the last day of the government shutdown I signed a contract for 15C and was set to leave to Fort Jackson on the 26th. Now my recruiter called me today and says there\u2019s something about the flight physical that makes joining under my MOS a no go. I never took a flight physical. I told him this and he started saying something about a new policy that he wanted to get me grandfathered into. I asked him what it was that got my application flagged and he responded that he didn\u2019t know but was working on it. Does anyone know anything about this? I was literally supposed to go in two weeks man:(.",
    "flair": "Enlisting",
    "score": 36,
    "comment_count": 21,
    "created_at": "2026-01-12T17:35:59+00:00",
    "top_comments": [
      {
        "id": "nz799m4",
        "score": 15,
        "body": "Did you get call about security clearance?\nDid you say something that may have disqualified you?"
      },
      {
        "id": "nz7dpkq",
        "score": 14,
        "body": "Basically last Friday an email was sent out stating for MOS 15C and 15Q that medical history will be reviewed to determine if they can pass  a class IV flight physical.\n\nIt seems they have determined you  are not qualified and will have to renegotiate your contract. It may be because you disclosed drug use after you were (I\u2019m assuming) 18 YO."
      },
      {
        "id": "nz7g4eu",
        "score": 10,
        "body": "Yeah your recruiter is probably as confused as you, it\u2019s a decision from MEPs command."
      },
      {
        "id": "nz7fccu",
        "score": 7,
        "body": "I was a sophomore high school when this happened, and on the civilian side i hold a Class 1 FAA flight physical. so this is weird that i got flagged."
      },
      {
        "id": "nz7akrh",
        "score": 6,
        "body": "I disclosed prior drug use to the MEPS doctor during my physical, but they told me the same day i didn\u2019t need a waiver for anything. My recruiter said the same thing, and unless this call i just got was about security clearance (which wasn\u2019t mentioned) I haven\u2019t heard anything about it."
      },
      {
        "id": "nz81rch",
        "score": 2,
        "body": "We received new guidance last week stating that \u201ceffective immediately: Regular Army and Army Reserve enlistments into MOS 15C and 15Q, will have their medical history reviewed after enlistment to determine if they meet the requirements of passing a Class IV Flight Physical\u201d\n\nMy guess is you had a medical waiver that they didn\u2019t like. \n\nDid you have any medical waivers?"
      },
      {
        "id": "nz9h1gi",
        "score": 2,
        "body": "Honestly the new policy is looking out for the applicants more now. Before you would get to fort Jackson then decided if you meet qualifications for the flight physical and if you didn\u2019t you would go needs of the Army. At least now you get the choice of Reno or don\u2019t ship lol"
      },
      {
        "id": "nz83q7x",
        "score": 2,
        "body": "No, I didn\u2019t need to process a waiver for anything"
      },
      {
        "id": "nz83yg0",
        "score": 2,
        "body": "I read through the comments and the history of drug use might have been the issue."
      },
      {
        "id": "nz9hw1g",
        "score": 2,
        "body": "[removed]"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1onguuf",
    "title": "2 failed drug test at meps",
    "body": "I failed 2 drug tests at MEPs (Marijuana) a few years apart when trying to join the marines. Its been about a year and half since I failed the second test. I was told in a letter when I failed I was permanently disqualified from joining the military. Recently I had a recruiter contact me out of the blue and ask me if I still had any interest in joining. I explained my situation to him and he told me it is still possible to join, im just wanting to know if I'm being told the truth and should go back to MEPs for a 3rd drug test, or if it's even possible to get a waiver for 2 failed drug tests.",
    "flair": "Enlisting",
    "score": 36,
    "comment_count": 135,
    "created_at": "2025-11-03T16:46:25+00:00",
    "top_comments": [
      {
        "id": "nmwnb7a",
        "score": 30,
        "body": "Have you\u2019ve smoked recently, if you haven\u2019t you should be in the clear at least like a month or 2 of not smoking, if you have let your recruiter know that you need time to clear your system and give him the day you last smoked. And don\u2019t smoke when you are in the Military!!!"
      },
      {
        "id": "nmxp8xx",
        "score": 21,
        "body": "Unless Russian or Chinese paratroopers are falling from the sky, you\u2019re barred from the military"
      },
      {
        "id": "nmwrbb9",
        "score": 14,
        "body": "That recruiter is lying \u2026. After the second fail you\u2019re done"
      },
      {
        "id": "nmwo6b5",
        "score": 14,
        "body": "I haven't smoked since I failed about 1 1/2 years ago. I just want to know if a waiver for 2 fails is possible. I was previously told it wasn't. But a new recruiter at the Marines office I went to is telling me it is."
      },
      {
        "id": "nmwojz5",
        "score": 13,
        "body": "Believe in your recruiter, and listen to what he tells you and I don\u2019t know much other than recruiters will do their best to get you in."
      },
      {
        "id": "nmx2kq9",
        "score": 6,
        "body": "I know this comment is not helpful but why go to MEPS if you\u2019re gonna piss hot dude lol! I hope it works out for you."
      },
      {
        "id": "nmxcymm",
        "score": 6,
        "body": "Failed 2 drug tests back to back\u2026you\u2019re gonna need an ASVAB waiver too."
      },
      {
        "id": "nmzjotn",
        "score": 6,
        "body": "Lol, as much as it suck this was kinda funny"
      },
      {
        "id": "nmwqhoc",
        "score": 6,
        "body": "Permanently disqualified doesn\u2019t mean you are, it just means it\u2019ll be more of a hassle to get in, if a recruiter says they can get you in they can fight for your wavers, plus wouldn\u2019t it be still possible to join a different branch?"
      },
      {
        "id": "nmwqtn5",
        "score": 6,
        "body": ">Permanently disqualified doesn\u2019t mean you are\n\nYou're thinking of medical waivers, meaning the medical condition is permanent.\n\n>plus wouldn\u2019t it be still possible to join a different branch?\n\nNo. This is a DoD DQ. OP got two chances and screwed up twice."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1n0fkqn",
    "title": "Husband admitted to mental hospital during Army boot camp",
    "body": "Hello, I\u2019m not sure if this is the right place to post but I hope y\u2019all can help me. My husband started BCT this past month, and on our Sunday calls he\u2019s said it\u2019s been very mentally difficult for him. A few days ago, I received a call from a nurse at a nearby ER, and she informed me that my husband was admitted the previous night for a suicide attempt. \n\nHe told me that the isolation and psychological stress he experienced led to severe psychosis (auditory and visual hallucinations as well as delusions), which led to a suicide attempt. He was kept in the (civilian) medical hospital over the weekend for an unrelated medical issue, which has since been treated. Last night he was taken to the local psychiatric hospital, where they say he will stay for 5-10 days before returning to base.\n\nBefore this he dealt with some anxiety, but nothing anywhere near this serious. I am very worried about my husband, especially since he has stated that he \u201cend up back in the hospital\u201d if he has to continue the level of isolation that he experienced during BCT.\n\nI have a few questions. I know the answers are mostly \u201cit\u2019s up to command\u201d, but I\u2019ll take any information you can give me. What happens from here? Will he be given a medically discharge? Is there anything I can do so he\u2019s not stuck in reception for months?\n\nI know the answer to this one is probably no, but is there any possible way he could be sent home for treatment?",
    "flair": "BCT/BMT/Boot camp",
    "score": 34,
    "comment_count": 36,
    "created_at": "2025-08-26T07:42:24+00:00",
    "top_comments": [
      {
        "id": "naqnt2v",
        "score": 33,
        "body": "May I ask how he is severely isolated in bootcamp? I know they are yelled at and aren't supposed to talk, but you do have your platoon mates to talk to and most do when the DI/DS aren't looking or after \"lights\", where they go b to bed in the evening.\n\nAnyway, to answer your question, he will likely be entry level separated/medically separated. One he returns to base he will see some doctors there as well, then go to a separation platoon. They won't be yelled at much and just hang out till paperwork and travel plans are finalized.."
      },
      {
        "id": "naqgclm",
        "score": 31,
        "body": "Hi, sorry to hear about your husband.  How did he enlist with these conditions? Most likely they will let him go after treatment. I know people that came home early because they started having anxiety attacks during bct which led to seizures. Hope he gets treatments and be home safe."
      },
      {
        "id": "nar8ux1",
        "score": 31,
        "body": "FYI it wasn't a lie if he was never diagnosed."
      },
      {
        "id": "nar5y0h",
        "score": 28,
        "body": "He\u2019s going to get kicked out. Entry level separation. He couldn\u2019t hack it. He\u2019s not isolated, he just can\u2019t deal with military life."
      },
      {
        "id": "nard4jg",
        "score": 18,
        "body": "This was the mistake that was made, not them telling him to lie about it, so much as him thinking, already suffering with PTSD, that joining anything besides the Air Force, was a good idea. Only because the AF has the easiest basic training."
      },
      {
        "id": "nar8y38",
        "score": 17,
        "body": "He doesn't need to. He has a documented attempt. He's coming home."
      },
      {
        "id": "nar4wi9",
        "score": 13,
        "body": "I know what kind of comments are coming.  Let's just not for once.  Truth is, no one knows exactly what it feels like to be in.  \n\nOP, I think they'll eventually cut him loose,  but it won't be pretty.  May be in a hold-over unit for a few months.  Sadly, people in my platoon, who had gone to psych, were still there when we were all graduating. \n\nEventually he'll be home and life will go on."
      },
      {
        "id": "nare8y9",
        "score": 13,
        "body": "I feel bad because you never want anyone to go through stuff like this however he was not isolated \u2026. You have a bunch of soldiers in your platoon unless he was just keeping to himself which still sounds strange"
      },
      {
        "id": "naqhsir",
        "score": 12,
        "body": "Before enlisting, he dealt with some anxiety and PTSD (from time as a firefighter). Never saw a doctor, never got diagnosed. Recruiter told him to lie at MEPS. However, it was never anywhere near this severe and he has never attempted before."
      },
      {
        "id": "natc1l5",
        "score": 9,
        "body": "100% \n\nOpposite of isolated. More like constantly grouped with 50+ people"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1qsvnk4",
    "title": "How do you deal with waking up early in the morning for boot camp?",
    "body": "One of my biggest hesitancies for joining the military is the early morning wake-up times.  I tend to be a night owl, and if I don't get my full 8 hours of sleep, I'm not able to function as well.  Will I be so exhausted during boot camp that I'll basically fall asleep on the dot?  How will wake-up times be like after I get out?  Would I still be able to stay out late and do stuff on the weekends late at night?",
    "flair": "BCT/BMT/Boot camp",
    "score": 32,
    "comment_count": 36,
    "created_at": "2026-02-01T11:04:33+00:00",
    "top_comments": [
      {
        "id": "o2z5itv",
        "score": 76,
        "body": "You don\u2019t deal with it. You just do it."
      },
      {
        "id": "o2yctnu",
        "score": 26,
        "body": "You will sleep like the dead because you are a level of tired you are not familiar with. In fact staying awake does become a problem later on during the FTX part of basic; I remember we used to take the coffee out of MREs and wrap it in napkins for \u201cRanger Chews\u201d. The idea being the caffeine in the coffee grounds would help. When that wasn\u2019t enough, one time I rubbed hand sanitizer under my eyes because I was literally falling asleep standing up in an MG pit. Wasn\u2019t the only person doing that. \n\nYou will not have a problem waking up in any basic of any branch. In fact you will be waking up on the dot before the drills come because it is kinda traumatic the way they wake you up in the first weeks. Those big squad bay lights come screaming on and they come screaming in banging trash cans and yelling. Then you get into the routine. In Army basic, by the end, I remember big drill would come in, flip the lights on, yell \u201cwake the fuck up privates\u201d and we would auto pilot into uniform and downstairs for first formation. In Coast Guard basic they never fucking let up lol. Coast Guard basic was the same as the Army in that you could fall asleep standing up, though I actually feel there was a lot less leeway. More eyes on you constantly, and you weren\u2019t out in the field where you could arguably kinda escape attention. \n\nOutside of boot, it\u2019s a job, you wake yourself up with an alarm clock lol. Army it depended on commute and when your leadership wanted you to show up for FF and PT, but you could be waking ip pretty fucking early. Some dudes woke up at like 4 if they had to drive. CG we don\u2019t do that. We don\u2019t have formations like that. You could wake up 30 minutes before work time and as long as you\u2019re there in uniform on the dot nobody will blink. Weekend duty at stations we even sleep in until 8 usually. Flag detail not withstanding."
      },
      {
        "id": "o30dzzm",
        "score": 10,
        "body": "Facts"
      },
      {
        "id": "o303nd2",
        "score": 7,
        "body": "Army guy checking in. Also a night owl. They\u2019ll exhaust you to the point where you\u2019ll be laughing about asking this question. We didnt sleep for the first couple days once we arrived to basic. You\u2019ll learn to wake up before they come kicking in the doors."
      },
      {
        "id": "o31vcbj",
        "score": 7,
        "body": "You PT on your own while operational in the air force"
      },
      {
        "id": "o30cawz",
        "score": 5,
        "body": "You do it or else you\u2019ll get the whole plt smoked and then they\u2019ll sock party your ass."
      },
      {
        "id": "o31bq18",
        "score": 4,
        "body": "In Air Force basic training you do PT as a unit. Who told you that you do it on your own?"
      },
      {
        "id": "o32z1ol",
        "score": 3,
        "body": "Read your post wrong, but I\u2019d go Air Force instead of navy if you\u2019re worrying about sleep, wake up time is gonna depend on the time you have to wake up for work. Avoid mechanical, infantry and military police. I doubt you\u2019d want to sleep in a cubicle in a submarine. \n\nBootcamp you\u2019ll be on a schedule and exhausted,\n\nNETC I can\u2019t speak for, but in Tech School you\u2019ll be on your own schedule with a curfew though you\u2019ll still have a wake up time designated by your leadership.\n\nOperational through any branch you\u2019re on your own, with the wake up time being on work days like a regular job whenever you have to be in to work."
      },
      {
        "id": "o2ysea4",
        "score": 2,
        "body": "After the first couple mornings of your drills kicking in the door with airhorn in hand screaming \"wake up! wake up! wake up!\", you'll have no issue waking up in the mornings, especially when you only get 10 minutes to shave, brush your teeth, get dressed, and get to formation lmao."
      },
      {
        "id": "o31xp8w",
        "score": 2,
        "body": "trust you\u2019re gonna get 8 hours they\u2019ll make sure of it. wdym stay out late you\u2019ll be consistently training on a schedule that schedule includes bed time and wake up."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1mkvwk0",
    "title": "Recruiter wants me to lie on my sf86",
    "body": "Update: I appreciate every single one of you for your time and responses, I let my recruiter know that I will not be signing until we get the waiver and I am waiting to hear back. Thank you guys for the push I shouldn\u2019t have needed \n\nI have definitely been arrested before but nothing is coming back on the checks that my recruiter does. I am on a severe time crunch and need to leave asap and my recruiter says if I insist on including my juvenile record I won\u2019t be able to leave by the time I need to. He says since my finger prints come back clean and I\u2019m not going for TS that there is no reason to list it. I can\u2019t afford to make this process take longer but I also can\u2019t afford to not be able to serve due to a lie I never wanted to tell in the first place \n\n\nEdit: my recruiter has been pretty firm on telling me not to list the arrest and that it will dq me from the mos I picked and that if I make him list this the waiver process will take months or even longer. I am facing homelessness and need to be shipping out asap. I am in a different state than my arrest, misdemeanor as a minor almost a decade ago. How screwed am I?",
    "flair": "Enlisting",
    "score": 32,
    "comment_count": 62,
    "created_at": "2025-08-08T13:56:24+00:00",
    "top_comments": [
      {
        "id": "n7lp3bv",
        "score": 42,
        "body": "Do not lie on your SF86. Your recruiter is a POS for telling you this"
      },
      {
        "id": "n7lue8b",
        "score": 24,
        "body": "they find out everything.  that recruiter shouldnt be saying that."
      },
      {
        "id": "n7ltq8t",
        "score": 13,
        "body": "I doubt it's a test, they're just tossing OP at the wall and seeing if he/she sticks. The only one who has anything to lose is OP."
      },
      {
        "id": "n7m6agf",
        "score": 10,
        "body": "I\u2019ve quite literally met someone a couple years back at 30th (reception) who had been there for a while specifically because they didn\u2019t list an arrest on their enlistment forms. They had been there for several weeks, and at that point, they were waiting to go home and get discharged. Would definitely recommend disclosing it"
      },
      {
        "id": "n7ohfk9",
        "score": 8,
        "body": "Clean prints doesn\u2019t mean you can lie on a SF86. That\u2019s falsifying a federal form\u2014they check more than fingerprints. Get caught later, you\u2019re out, benefits gone, maybe more charges. \n\nAnd if you\u2019re about to be homeless, the military isn\u2019t a magic fix\u2014lying just sets you up for a harder fall. Go in clean or don\u2019t go in at all. Also your recruiter\u2019s an idiot for saying otherwise"
      },
      {
        "id": "n7npn8x",
        "score": 8,
        "body": "First hand experience. My recruiter also told me to do that. I did it, I ended up getting held up for my TS clearance for 3 months and I had to get a shitload of character references from a bunch of people that I was lucky to have. \n\nDo not lie on your Sf86."
      },
      {
        "id": "n7lxrea",
        "score": 7,
        "body": "Brother. The guilt will eat you alive. Don\u2019t do it lol."
      },
      {
        "id": "n7m4qoo",
        "score": 7,
        "body": "It\u2019s not a test. It\u2019s a shitty recruiter."
      },
      {
        "id": "n7lup65",
        "score": 7,
        "body": "yep.  the recruiter hits his/her numbers and the OP suffers.  recruiters really do not care.  i really wish there was a self-service process where you didnt have to go through these liars.  they are disgusting and dont give a crap, kind of like car dealers in states that make you buy through car dealers."
      },
      {
        "id": "n7od8pb",
        "score": 6,
        "body": "If you get found out later on there's no way in hell your recruiter is going to say yeah \"I told him not to list it.\" I guarantee standing in front of you. Your recruiter will tell his command. I told him to disclose everything. \n\nSorry you're in a bad spot."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1l2w2x3",
    "title": "Is the military a good way to escape family?",
    "body": "I'm an 18 year old female, and a recent high school graduate. My relationship with my mom has never been the best, but has gone significantly downhill in recent months.\n\nMy mom is against the fact that I am a lesbian, and is threatening to cut me off from insurances, use of our family vehicles, and cell service. I have a job, but I do not have enough saved to even buy a car to drive to work.\n\nThe military has always been in the back of my mind, specifically the Air Force. Would this be a good way to distance myself from my family, while also having a place to live and a stable job?",
    "flair": "Should I Join?",
    "score": 30,
    "comment_count": 25,
    "created_at": "2025-06-04T03:59:18+00:00",
    "top_comments": [
      {
        "id": "mvw9crg",
        "score": 19,
        "body": "Absolutely, no time like the present. While military life isn\u2019t for everyone, it gives you job training, housing, pay, health coverage, etc. Choosing the military for a contract at least gets you out of the living situation you\u2019re in and on to a better path. Being LGBTQia+ in the military is no big deal, especially for women (personal experience)\n\nEdit : definitely should have just put LGBQ (not so much the T anymore)"
      },
      {
        "id": "mvwfieu",
        "score": 9,
        "body": "I mean I did, I wanted to leave California but the irony is  the Army brought me back for Recruiting duty. Jokes on me but is not bad as I\u2019m making 4.5x more than I did when I left."
      },
      {
        "id": "mvxfyl7",
        "score": 9,
        "body": "You'd be in good company. A lot of us did."
      },
      {
        "id": "mvwj1mh",
        "score": 5,
        "body": "You\u2019re not wrong for thinking about it. A lot of us didn\u2019t join the military because everything was perfect\u2014we joined because we needed out. Out of a bad town, a broken home, no money, no options. And yeah, for plenty of folks, it worked. You get a roof over your head, structure, a steady check, and a shot at doing something bigger than your current chaos.\n\nYou sound like you\u2019re already tough. That kind of pressure at 18? And you\u2019re still thinking clearly about your next move? That\u2019s strength. If you do go the Air Force route, just know: it\u2019s not an escape. It\u2019s a launch. You\u2019re still going to face pressure\u2014but now it\u2019ll be from pushups, time hacks, and figuring out who you are on your own terms.\n\nYou\u2019re not alone in that decision, and you\u2019re not broken for needing a way out. Just make sure you\u2019re doing it for the version of you that you want to become\u2014not just the version you\u2019re trying to outrun.\n\nAnd if you end up in uniform? Hell yeah. Make \u2018em regret underestimating you."
      },
      {
        "id": "mvwsfn7",
        "score": 5,
        "body": "If you\u2019re considering AF, make sure you talk to a Coast Guard recruiter too. Great branch."
      },
      {
        "id": "mvy1ozx",
        "score": 4,
        "body": "When I felt stuck and not going anywhere in life I joined. It was the best decision I made as a young adult.\n\nIt got me away from the house and I got to experience so many things I wouldn\u2019t have been able to if I stayed home."
      },
      {
        "id": "mvyt470",
        "score": 2,
        "body": "Yes, go reach out to a recruiter, take the ASVAB, pick a good job, go through MEPS (make sure you\u2019re clean from drugs and not pregnant), and ship."
      },
      {
        "id": "mw0ku7p",
        "score": 2,
        "body": "\\> Being LGBTQia+ in the military is no big deal, especially for women (personal experience)\n\nSeparating sexual preference (LGB) from the rest of the bunch, gender dysphoria is a disqualifying factor for the U.S. military without a waiver of sorts."
      },
      {
        "id": "mw2sk71",
        "score": 2,
        "body": "What\u2019s the QIA+?"
      },
      {
        "id": "mvx9d0l",
        "score": 1,
        "body": "If you want, it's a good place to go."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1ksbrmd",
    "title": "What is my recruiter not telling me?",
    "body": "I (30f) already have a bachelor's and I'm not interested in being an officer but still thinking of enlisting. I met with a recruiter today and it all just seems too good to be true. Picking my job, what base I'm stationed at, the benefits, etc. Is the army actually just awesome? Or is there something he's not telling me?",
    "flair": "Enlisting",
    "score": 32,
    "comment_count": 57,
    "created_at": "2025-05-21T23:00:12+00:00",
    "top_comments": [
      {
        "id": "mtk9hhq",
        "score": 33,
        "body": "The military is just packed to the brim with absolute bullshit you have to deal with constantly. Far too much to describe in a single response. My advice is just go check out the branches Reddit pages and read the stuff people talk about. \n\nThat being said I\u2019m at 17 years Army and if I could go back and do it again, I 100% would. There\u2019s a lot of good things too."
      },
      {
        "id": "mtk9zen",
        "score": 11,
        "body": "You can definitely choose your job in the Army, assuming it is available and you are qualified.\n\nThere is also a contract option to choose your duty station, but you may be limited on available job/base combos. The recruiter would know best what's available. \n\nWhat about the benefits seemed too good to be true?"
      },
      {
        "id": "mtkc4se",
        "score": 9,
        "body": "As an officer, not everyone is cut out to be commissioned.\n\nI personally applaud her self-awareness and agency here. Usually, it's the other way around where people are like \"I have a degree, make me an officer, I'm too good/special to be enlisted.\"\n\nAs a non-prior enlisted officer, I feel immensely grateful to work with so many professional NCO's who have so graciously opted to help out an LT, especially right now in my career. \n\nI'll also say... I spend a lot of time at my unit's CSS, and am probably the *least* educated person in there."
      },
      {
        "id": "mtkgfvw",
        "score": 8,
        "body": "Def a great option I just signed for 31b I decided not to choose where I go as I love excitement. I\u2019m 41 and will be 42 when I ship and chose enlisted over officer as well."
      },
      {
        "id": "mtkrz82",
        "score": 8,
        "body": "Basic dental/healthcare is free, elective surgeries are on a case by case basis and based more on patient needs vs. wants as I understand it."
      },
      {
        "id": "mtkoj1j",
        "score": 7,
        "body": "I don't want the responsibility or paperwork. The jobs where you're not in charge of things seem more enjoyable/fun and the possible pay increase isn't really a motivating factor for me. I may eventually be open to it, but I would rather learn the ropes of the army as enlisted. \ud83e\udd37\ud83c\udffc\u200d\u2640\ufe0f"
      },
      {
        "id": "mtk84bt",
        "score": 6,
        "body": "Jobs are limited right now"
      },
      {
        "id": "mtkm8tb",
        "score": 4,
        "body": "The Army is the Army, so there\u2019s that. Assholes exist everywhere but the Army can host a special breed. \nDid the recruiter mention the Army is willing to pay off your student debt (if it\u2019s the right kind)? \n\nIf you can find the MOS you want, go for it. Look for any options you can add on (overseas duty, etc). Good luck"
      },
      {
        "id": "mtkc46h",
        "score": 4,
        "body": "Essentially this. \n\nhttps://m.youtube.com/watch?v=Yv8gxbMERq0&pp=ygUaZmFtaWx5IGd1eSBhcm15IHJlY3J1aXRpbmc%3D"
      },
      {
        "id": "mtltdmg",
        "score": 4,
        "body": "I mean it\u2019s not rocket science, you\u2019re in your 30\u2019s and already have a degree. You will have responsibilities either way. Why take less pay at this stage in life?"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1nqmdyy",
    "title": "Should I join the military to escape my living situation?",
    "body": "I\u2019m 26F Brooklyn NY\n\nI live with my mom who is mentally ill and is in denial and doesn\u2019t want to get help. She paranoid and doesn\u2019t want to help my 84 year old grandpa to pay the rent and bills because she\u2019s paranoid and doesn\u2019t see him as her real father and think he\u2019s out to kill her.\n\nWe both live with my 84 year old grandpa who is the main person who pays the bills and rent at the apartment. \n\nI graduated college in 2021 but have been job hopping and haven\u2019t kept a stable job because confused what to do in life (indecisive) which caused depression and anxiety issues. \n\nI\u2019ve recently thought about about joining the military (army, air forces, marines, navy , etc) to escape my living situation for my own mental sanity. I\u2019m not familiar with the Military to be honest. But I feel like this is my only option really \n\nBut I have questions though \u2026do I need to be \u201cphysically fit\u201d? Or \u201cis it required to go to war\u201d? \n\nPlease give me advice and just be honest with me on if I\u2019m making right decision to potentially join the military? ",
    "flair": "Should I Join?",
    "score": 27,
    "comment_count": 28,
    "created_at": "2025-09-25T23:46:37+00:00",
    "top_comments": [
      {
        "id": "ng7x002",
        "score": 27,
        "body": "If you need to ask, be required to go to war, you probably shouldn't join the military. \n\nThere may not be a war for us to be fighting right now. But, I was in almost 8 years. \n\nI deployed to Afghanistan and Liberia. I also deployed to Africa after being home less than a year after arriving at my next duty station."
      },
      {
        "id": "ng7xb3n",
        "score": 25,
        "body": "I joined to escape my living conditions and it was the best decision I ever made. The military is easy as hell: show up at the right place, at the right time, and in the right uniform, stay in shape, listen to your superiors, don\u2019t talk back, bring solutions and not excuses any time you fail, and look better than the dude or chick next to you. It\u2019s fucking easy.  If you hate it after the first enlistment, just get out, so easy a caveman can do it. \n\nJust understand that every initial entry contract is for EIGHT years.  Eight, not three, not four, EIGHT. This translates to however many years active you do plus the remaining years on inactive reserve. So when the recruiter says to you, \u201cjust sign the line and you only have to do three years\u201d or whatever they say, they are only talking about the ACTIVE portion of the contract.  It\u2019s an eight year commitment no matter what.  If you\u2019re nervous about that, you can always do the guard and try going active later but from my experience, that\u2019s always a pain in the ass. Plus, guard or reserves aren\u2019t going to get you out of your environment. \n\nAnyway, I did 20, I was a drill, I did infantry and special operations. I retired as a first sergeant. I still have may friends in as well so if you ever have any questions, my DMs are open.  Good luck troop!!"
      },
      {
        "id": "ng7vmbh",
        "score": 9,
        "body": "Yes, you have to be in shape. And if you have orders to go deploy to go to war, yes you have to go (to keep it simple, I just gave you a basic answer.)"
      },
      {
        "id": "ng91moh",
        "score": 6,
        "body": "I know someone who did that at 19.  Same reason.  Love them.  Don\u2019t be them.  Person was a lifer.  32 years.  28 active duty.  No other considerable options at the time.  Straightened them out.  Gave them focus, purpose, training and a plan.  Got in the slot and kept moving up.  Now retired- no regrets.  Happier than a pig in shit- and nothing changed at the address they left."
      },
      {
        "id": "ng8d822",
        "score": 4,
        "body": "Being in the military, you cannot completely shut down the chances of you being deployed somewhere. It\u2019s the military for a reason. Any recruiter who says they can guarantee you no deployments is lying to your face.\nHowever, with that being said, there are plenty of non-infantry jobs that limit the chances of you deploying.\n\nIf you are not a fit person I would rule out the Marines, they are tough and in order to become one you must be willing to whip yourself into shape. Plus, you mentioned battling through anxiety and depression over the years, if you were prescribed meds then you are going to be a medical waiver. All of the branches offer waivers but the Army is easiest to get those approved. The most difficult is the Marines by far.\n\nI suggest speaking to a recruiter from all the branches and deciding on which one you think suits you best. Choose non-infantry and don\u2019t do reserves because that will place you right back in your hometown once you\u2019re done with your training."
      },
      {
        "id": "ng7w6g6",
        "score": 3,
        "body": "Need to be fit enough to meet standards, and prepared to go to war if it kicks off."
      },
      {
        "id": "ng8inck",
        "score": 3,
        "body": "This is what I did back in 2003 and I retired in 2024."
      },
      {
        "id": "ng7v8x2",
        "score": 2,
        "body": "**DQ standard(s) (requires waiver(s))**:\n\nAnxiety/Depressive disorder if:\n\n(1) Outpatient care including counseling required for longer than 12 cumulative months;\n\n(2) Symptoms or treatment within the last 36 months;\n\n(3) The applicant required any inpatient treatment in a hospital or residential facility;\n\n(4) Any recurrence; or\n\n(5) Any suicidality\n***\nThis sub cannot definitively tell you whether you're eligible. Waivers are decided on a case-by-case basis. Contact your local recruiter.\n\n^(I'm a bot and can't reply.) [^(Message the mods)](https://www.reddit.com/message/compose?to=/r/Militaryfaq&subject=MilFAQBot) ^(with questions/suggestions.)"
      },
      {
        "id": "ng7yn17",
        "score": 2,
        "body": "One big factor to ponder:\n\n* if you have been *medically diagnosed* with depression or anxiety, those can be impediments to enlisting. How seriously so would depend on the diagnosis, medication status, etc.\n\n* If you have not been formally diagnosed with mental health conditions (for the love of Pete, don't put self-diagnoses on military paperwork, you're not a doctor), it's worth pondering if you have inherent personal mental health issues that would be *exacerbated* by military service, or if you are sincerely convinced that your current issues are situational and would be resolved by having a stable job away from family.\n\nA *lot* of folks have used the military to escape a shitty life situation and been very successful. But there are also people struggling with innate mental health issues who assume the military will \"fix\" them, sign up and either mentally collapse and/or threaten suicide to get kicked out, sometimes even in Basic training.\n\nYou need to do some serious soul-searching about whether you'd thrive or collapse when under pressure. Frankly just for a start I'd suggest you watch a bunch of videos of various branches' basic training on YouTube and ask yourself if you'd find it an exciting challenge, or traumatic.\n\nYour whole career isn't going to be people shouting at you like it's Basic, but the point of Basic is to artificially induce stress to see how you'll cope with stress in real life emergencies or combat."
      },
      {
        "id": "ng8ea7e",
        "score": 2,
        "body": "Look into the Coast Guard"
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1ouvn5m",
    "title": "Should I join at the age of 35?",
    "body": "Hello,\n\nI\u2019ve been debating this for a long time. I\u2019m 35 years old, with a good job, a wife, and a child. Despite being successful in my current career, I can\u2019t shake the feeling of being unfulfilled. It\u2019s not that I need a new hobby, t\u2019s something deeper.\n\nI have always thought about joining the Air Force. \n\nAs a man, I feel a pull to break away from the generational career path in my family and serve in the military. But I struggle with doubts, that I might not be good enough, or that I\u2019d just end up doing the same kind of work I do now (management and AC-related work). The truth is, I\u2019m not even sure what role I\u2019d pursue if I did join.\n\nMore than anything, I want to do something I can truly be proud of, something my son can be proud of too.\n\nYour thoughts and insights would be truly appreciated. Thank you to all those that served and that are serving currently. ",
    "flair": "Should I Join?",
    "score": 27,
    "comment_count": 27,
    "created_at": "2025-11-12T04:26:04+00:00",
    "top_comments": [
      {
        "id": "noel0af",
        "score": 12,
        "body": "[deleted]"
      },
      {
        "id": "nogrur3",
        "score": 10,
        "body": "I was mostly in the same boat as you. I was 26, I was married, had a kid on the way and a decently paying job. I was unfulfilled. I intended on joining after high school but got a job instead. After 8 years of working in stuffy offices with passive aggressive people, I couldn't keep doing it.\n\nI've been in a good few years now and I won't lie, I love it. Don't get me wrong, I hate a lot about the military. I could write 10 pages on the stupidest shit I've ever seen, but there is magic to this job for me. I love my MOS, I love my coworkers, I love training soldiers. I love going to new places, I like going to the field (sometimes), etc. \n\nMy point is, it was the right decision for me, so it's possible it could be for you as well. I'd talk extensively about it with your wife and make sure she fully understands the sacrifices it takes to be in this career field. Make sure you understand them as well. I missed my daughter's birth because I was deployed. I missed her first birthday because I was in the field. I missed her first steps because I was in the field. I hate that that's true. You will pay a toll to be in this career.\n\nSome people mention shit pay. It's really not terrible in my experience. Your base pay will probably go down but you'll have better benefits. If you're enlisting, I wouldn't recommend your wife SAH, I see guys do it but they always struggle financially."
      },
      {
        "id": "noepxvh",
        "score": 8,
        "body": "Are you looking to enlist or commission? Do you have a bachelors degree?\n\nHow does your spouse feel about being a solo parent for months at a time, probably moving to somewhere they didn\u2019t choose and know no one, and likely being underemployed or unemployed?\u00a0\n\nWhat\u2019s your current household income? Have you compared that to E-1 (or E-2 or O-1 if applicable) pay and benefits? Is your spouse\u2019s job portable?"
      },
      {
        "id": "noezys8",
        "score": 7,
        "body": "That fulfillment is not going to be fulfilled by the military. Many guys get out and struggle because they have that same very lack of fulfillment. I don\u2019t have the answer for you, but personally I don\u2019t think the military will answer it. However if it\u2019s something you\u2019re really wanting, go for it, just know people are typically retiring at your age. You\u2019re gonna have to move your family more than likely. And it\u2019s going to be shitty pay\u2026"
      },
      {
        "id": "noffbge",
        "score": 5,
        "body": "Maybe. Continue to explore *part-time* military Reserve or Guard options to proudly serve without giving up your current lifestyle or career. Identify the *\u201dright fit\u201d* opportunity and challenge for you and get *prequalified* to join to confirm it\u2019s a viable option. \n\nA Reserve or Guard military position doesn\u2019t have to be aligned or related to your civilian career \u2026 research well, choose wisely, and  excel at whatever military role *\u201dcalls\u201d* to you as something you want to pursue."
      },
      {
        "id": "noik1ed",
        "score": 5,
        "body": "I joined at 34 (national guard) it\u2019s honestly fine. You just have to deal with all the immature disrespectful kid\u2019s during basic and tech school."
      },
      {
        "id": "noezmu4",
        "score": 5,
        "body": "Army is also 42."
      },
      {
        "id": "noezsi0",
        "score": 4,
        "body": "At least since the recruiting crisis started."
      },
      {
        "id": "nof124h",
        "score": 4,
        "body": "The data is correct, but it's waived to 42. It used to be case by case, but now is de facto."
      },
      {
        "id": "nof1d8o",
        "score": 3,
        "body": "Honestly no. If you lack purpose then get involved with a charity or something. Im jaded but fuck this shit, especially if you\u2019re older and don\u2019t need it."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1jusgfi",
    "title": "Separated wife says army needs my SSN",
    "body": "My soon to be ex told me that she's going tp join the army and that they need my SSN and DL. Something doesn't feel right about them need my info since we're separated.\nIs this identity theft or is it legit?",
    "flair": "Enlisting",
    "score": 29,
    "comment_count": 26,
    "created_at": "2025-04-09T00:02:07+00:00",
    "top_comments": [
      {
        "id": "mm4mats",
        "score": 65,
        "body": "Until you are legally divorced, as in the judge signed paperwork, you are your wife's dependent once she joins."
      },
      {
        "id": "mm4nffc",
        "score": 38,
        "body": "You don\u2019t have to give it to her, you may provide it to the recruiter. As her legal (yet estranged) spouse you are entitled to benefit\u2019s upon her \u201cshipping out\u201d for Basic Combat Training (TriCare, dental and vision coverage etc). The Army/DOD is just verifying who you are. You may be eligible for spousal support. See an attorney."
      },
      {
        "id": "mm4mcrh",
        "score": 36,
        "body": "Legit. \nYou're legally married. The marriage ties you to her. \nWhen they enter her in the system, and if she's married, your information is required. Legally, separation means nothing."
      },
      {
        "id": "mm4u91x",
        "score": 11,
        "body": "As long as you\u2019re still married she will need a copy of your ID, Social, and Birth Certificate.\n\nIf you\u2019re not comfortable sending it to her ask her for her recruiters email and send it directly to them. \n\nThey are obligated to enroll you in DEERS as long as your married, you will at least have good insurance until your divorced.\n\nEDIT- A legit recruits email will end with army.mil/ navy.mil etc. \n\nIf it doesn\u2019t end in .mil it\u2019s not real."
      },
      {
        "id": "mm4mirv",
        "score": 8,
        "body": "It is legit and she will need marriage/divorce certs too if you have those. But consider going to the office with her if they need them copied. When she ships she only needs COPIES of those items but the recruiter may need to make copies of the originals. And she should only need that info if you are still legally married."
      },
      {
        "id": "mm5e1ja",
        "score": 3,
        "body": "It\u2019s normal. You are married."
      },
      {
        "id": "mm4ob07",
        "score": 3,
        "body": "I was worried more about her intentions or a fake recruiter than the actual government I already know they have all my secrets in their grasp"
      },
      {
        "id": "mm4mu0u",
        "score": 2,
        "body": "Thanks everyone for the answers. Helped alot"
      },
      {
        "id": "mma3yhf",
        "score": 2,
        "body": "You can actually meet up with the recruiter too if you dont want to see her. Just another option."
      },
      {
        "id": "mm4oj28",
        "score": 2,
        "body": "Then verify who is asking for the information. Call the recruiter."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1jk05nr",
    "title": "bro, where tf are the airforce recruiters?",
    "body": "I have never seen an airforce recruiter in my life and they never pull up to my school. I'm joining the army but I was just curious on why the air force doesn't recruit that hard.",
    "flair": "Enlisting",
    "score": 27,
    "comment_count": 26,
    "created_at": "2025-03-26T01:22:25+00:00",
    "top_comments": [
      {
        "id": "mjrfixx",
        "score": 28,
        "body": "Former Army Recruiter (2004-2011)\n\nSmallest branch which means they have less shoes to fill and can be more selective, and they don't need to prospect that hard; the applicants/prospects come to them.\n\nI'm assuming you see the Marine Recruiters at your school. They own the Senior HS Marketshare. That's their cream of the crop."
      },
      {
        "id": "mjrg9j5",
        "score": 24,
        "body": "Because they don\u2019t need to. Generally speaking they have more applicants coming to them than they need or want."
      },
      {
        "id": "mjry1u1",
        "score": 9,
        "body": "They're ghosts. When I was trying to join I reached out to 5 offices near me and finally got a call back after a month. Few months later I finally shipped off. Took until I was almost done with tech school that I got my second call back saying he could set up an appointment to talk with me. Never heard from the other 3 and I'm out now."
      },
      {
        "id": "mjsl6er",
        "score": 9,
        "body": "Joined the Air Force out of Glendale, AZ in 2008. My recruiters exact words when I walked in to the office the first time after telling him I wanted to join \u201ctake this packet and fill it out if you want to join. Bring it back if you do. If you don\u2019t that\u2019s fine, there\u2019s 100 more of you coming in the door this week\u201d lol"
      },
      {
        "id": "mjrxd52",
        "score": 7,
        "body": "Bro, I\u2019m right here. You hardly see me because my AOR covers an entire state. There\u2019s like 15-20 army recruiters for every one of me."
      },
      {
        "id": "mjrf9em",
        "score": 5,
        "body": "[deleted]"
      },
      {
        "id": "mjum33n",
        "score": 5,
        "body": "You need to call or show up to their office. \n\nI cannot imagine how many emails an Air Force recruiter has to sift through."
      },
      {
        "id": "mjry93s",
        "score": 4,
        "body": "yeah same man, my original goal was to go air force and I emailed like five recruiters and never heard back -the only time i got an interaction with an air force recruiter was when the academy scout showed up at my school"
      },
      {
        "id": "mjs30n4",
        "score": 3,
        "body": "Smaller recruiting mission and horribly outmatched manning wise. The army in my station has 8 recruiters that split 6 schools i have 20 by myself just to put how far stretched we are into perspective. Also we have assigned school frequencies for schools between monthly and quarterly. If you never see them at yours they're either lazy, in classrooms because cafeteria visits/jrotc is a waste of fucking time or not going at all because your school has an established reputation for dumb kids. Pick your poison."
      },
      {
        "id": "mjrppes",
        "score": 3,
        "body": "Their only standard that is different is the ASVAB and it's 4 points different. \n\n\nMy brother in law was an Airforce Recruiter, he said he comes in, checks his voicemail on his phone, call those people back to prequel them and set appointments and leaves for the day.\n\n\n\nArmy and Marine Recruiters aren't even sure their answer machine works. \n\n\n\nWhen your branch offers the same benefits as the others, a better quality of life, no field time, and much less danger (relatively) you don't really have to try and recruit."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1nl8mwn",
    "title": "Can I face legal repercussions for not telling my job I was joining the military?",
    "body": "Hello! As the title states, I signed up for the army a few months ago and go to basic in a few days. I got a job because a needed to sustain myself in the months leading up to basic. Here's the thing though: I didn't tell them I was joining the army as they were hiring me. I have yet to put in my two weeks notice because im worried they'll dunk on me legally if I tell them the reason for my quitting is because I'm going to basic. Any advice would be nice, thanks! ",
    "flair": "Enlisting",
    "score": 27,
    "comment_count": 34,
    "created_at": "2025-09-19T16:42:22+00:00",
    "top_comments": [
      {
        "id": "nf3lpf7",
        "score": 54,
        "body": " Tell them you\u2019re leaving for basic training. Shake their hand and say thank you. Then go start your new life. Not giving them any heads up if you\u2019re leaving in a few days is kind of lousy but life goes on."
      },
      {
        "id": "nf3m07u",
        "score": 38,
        "body": "1. \"Two weeks notice\" is a courtesy. There's no legal requirement to give any kind of notice.\n2. You are protected by USERRA. [https://www.dol.gov/agencies/vets/programs/userra](https://www.dol.gov/agencies/vets/programs/userra)"
      },
      {
        "id": "nf3nvsb",
        "score": 17,
        "body": "Don't quit. Request military leave."
      },
      {
        "id": "nf3kejx",
        "score": 14,
        "body": "No, you can\u2019t get in any type of trouble. That said, don\u2019t apply over there in the future. They have nothing to \u201cdunk on you\u201d for since people walk out of their jobs every day. That\u2019s freedom, baby."
      },
      {
        "id": "nf5sfxq",
        "score": 14,
        "body": "And always remember kids, they don\u2019t have to give you a two weeks notice they are firing you so don\u2019t waste your time doing the same. If you like your supervisor tell him/her so they can prep for your departure and then peace out."
      },
      {
        "id": "nf3klp0",
        "score": 10,
        "body": "Did you sign some contract to work there? Most americans are not obligated to show up to work legally"
      },
      {
        "id": "nf41lsm",
        "score": 7,
        "body": "You are protected from any adverse action based upon your uniformed service by USERRA. You do want to give them written or verbal notice that the reason you are leaving is for uniformed service. That way if something goes wrong and you don't complete basic you will still have reemployment rights. Indeed, you have up to five years of active duty before you would no longer be eligible for reemployment."
      },
      {
        "id": "nf3oobr",
        "score": 6,
        "body": "Legally they can't do any of that. The absolute worst thing they can do is decline to give a reference if you apply for another job in the future."
      },
      {
        "id": "nfbi50b",
        "score": 5,
        "body": "Tell them you\u2019re taking military leave*\n\nI know what you meant but wanted anyone reading to know - you don\u2019t have to ask for it. Legally they have to give you 5 cumulative years (some portions of your service are exempt)."
      },
      {
        "id": "nf4iglb",
        "score": 5,
        "body": "Even if you did the worst that could happen is they request a bonus back or something, most contracts are something along the lines of \u201cwork with us for two years and we will give you a 10k bonus\u201d, with the rule that if you quit you pay it back or something like that. Even then you just return it and its done."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1prvnjv",
    "title": "do all infantry soldiers get pistols (army)",
    "body": "Hey everyone, I\u2019m a civilian trying to understand how gear is issued. I\u2019ve heard that most 11Bs don\u2019t get a handgun, and that pistol training only happens if you\u2019re issued one. Is that true? And if so, why not train everyone with pistols just in case they need one? Thanks for any help.",
    "flair": "MOS/AFSC/Rate Specific",
    "score": 25,
    "comment_count": 32,
    "created_at": "2025-12-21T02:42:08+00:00",
    "top_comments": [
      {
        "id": "nv4xu0v",
        "score": 42,
        "body": "Correct, the Army only issues pistols out to certain people. If they followed through on their plan when they fielded the M17, the lowest ranking infantryman to be issued a pistol would be a team leader (usually a sergeant).\n\nWhy doesn't everyone get trained on pistols? Time and money, that's basically it."
      },
      {
        "id": "nv5a52u",
        "score": 31,
        "body": "Infantrymen aren\u2019t operators, and don\u2019t act alone. There\u2019s very rarely a scenario where one needs to \u201cswitch to secondary.\u201d \n\nIn the real army, that moment you communicate that you\u2019re loading, and other men cover. \n\nAgain, not a singular fighter kind of thing, more like bees in the hive."
      },
      {
        "id": "nv4ydzw",
        "score": 20,
        "body": "I had a M9 pistol when I carried a 240B belt-fed machine gun. Because no one else used the same rounds, it was a backup for me if the gun went down or I ran out of rounds. \n\nAs an officer, I had a M9 and an M4. I usually gave my pistol to our mine sweeper so his rifle wouldn't interfere with the read out. I've also given my pistol to interpreters after some range time and getting to know them well enough that I didn't think they'd shoot me or anyone but the TB."
      },
      {
        "id": "nv4wukw",
        "score": 16,
        "body": "Officers and higher enlisted usually"
      },
      {
        "id": "nv51ztd",
        "score": 11,
        "body": "Join as a tanker or direct commission as a CPT in law, divinity, doctor, nurse or veterinarian then lol, I believe at least some of those dudes get issued M9s. \n11Bs/19Ds can\u2019t do one field problem without some guy losing an M4/NODs. I can only imagine the shitshow that would take place if every swinging dick from PV2-SPC got issued a pistol on top of all the other shit."
      },
      {
        "id": "nv52blt",
        "score": 11,
        "body": "My unit had everyone qual on the M17 but this isn\u2019t call of duty where everyone gets a secondary. Fire superiority and maneuvering is the name of the game. Infantrymen are already carrying a lot of shit as is and weight is everything. The M17 has a max firing range of 50m according to the TM. I\u2019d rather have my rifleman carrying extra M4 mags and be able to touch people out to 500m. If I\u2019m in a situation that requires a pistol of last resort I\u2019m already fucked"
      },
      {
        "id": "nv5dlfe",
        "score": 10,
        "body": "It\u2019s a waste of space for most soldiers. \n\nPrioritizing more rifle magazines is a much better use of weight and space on your kit. \n\nIf there isn\u2019t a direct need for a handgun, which is limited already, then more magazines for your rifle will be more beneficial. \n\nPistols normally go to a handful of people, machine gunners, PL, PSG, SL, medic sometimes, and vehicle crews are the norm. Normally in that order. \n\nSometimes TLs or special teams might get one such as EPW teams but for the most part handguns are issued on a mission specific basis."
      },
      {
        "id": "nv5en3l",
        "score": 8,
        "body": "Yes when I was in the Infantry we trained with pistols seldomly. We got opportunities to qualify a hand full of times but most of the hands on was for EIB, other than that it was reserved up PSG and up. \n\nAs an Enabler as in 35 series in USASOC, I trained more with a pistols than I did in the Infantry, actually I traveled with an Sig and my rifle all throughout Afghanistan and always had access to our weapon for training, When I got to INSCOM, I qualified both Pistol and M4 ironside as a PSG. But only once every two years and only with bare amount of ammo, which sucks since Intel guy don\u2019t get much gun time and even less when you hit PSG."
      },
      {
        "id": "nv546al",
        "score": 8,
        "body": "Chaplains can\u2019t be armed. Their assistants act as their bodyguards for that reason"
      },
      {
        "id": "nv5j1yl",
        "score": 6,
        "body": "Rarely would use it if ever. Pistols are more of a status item for rank or job. \n\nSome positions call for it at times. At one point if you were a driver you were issued a pistol as well. Didn\u2019t make sense but it\u2019s was someone\u2019s bright idea so we did it for a while. \n\nWe never want to be in a situation where pistols would be useful. Always engage at distance or with overwhelming numbers even in CQB environments. \n\nThe major upside to having a pistol was being armed on base. You could leave your rifle locked up and carry your pistol. Had to be armed but most bases it wouldn\u2019t matter."
      }
    ]
  },
  {
    "subreddit": "Militaryfaq",
    "id": "1kp7xka",
    "title": "Am I dumb to choose the Army over the Air Force?",
    "body": "I am 26 and a husband and am planning on joining the Army over the Air Force. The reason for this is so that I can pick my job. I want to provide a good life for my family. I plan on entering the intelligence field. Is that a bad idea?",
    "flair": "Which Branch?",
    "score": 25,
    "comment_count": 72,
    "created_at": "2025-05-18T00:54:59+00:00",
    "top_comments": [
      {
        "id": "msvtzv9",
        "score": 29,
        "body": "Nope. Since you are married, you are avoiding 2 things that a lot of people hate about the Army(barracks and DFAC)."
      },
      {
        "id": "msvtfxl",
        "score": 15,
        "body": "I chose army over the air force for the same reason and air force processing time will take longer. I just notice quality of life is better in air force than army but i dont regret anything at all cos i got to pick my MOS."
      },
      {
        "id": "mswajf2",
        "score": 11,
        "body": "If you want AF quality of life *and* getting to pick your job. We'd be happy to have you in the Space Force. We only have 3 career fields(Space/Intel/Cyber), and we don't really deploy, so you won't be away from your family. Downside is you will 90% be stationed in Colorado, Northern California, Northern Florida, or the DMV area, but if that sounds good, go for it."
      },
      {
        "id": "msvuso7",
        "score": 10,
        "body": "That being said, the Army tends to deploy/rotate a lot more often than the Air Force, so you could end up in Europe or Korea for 9 months without your family. Something to think about."
      },
      {
        "id": "mt3lrvl",
        "score": 5,
        "body": "Coast guard let you pick up your job, and has better quality than all branches, even the Air Force."
      },
      {
        "id": "msvwfoj",
        "score": 4,
        "body": "Not dumb, but you will find that the grass is greener on the Air Force side. Do your time, and switch over GOOD LUCK!"
      },
      {
        "id": "msvub0g",
        "score": 4,
        "body": "Thank you for the answer!"
      },
      {
        "id": "msvuwkk",
        "score": 4,
        "body": "Definitely. Just want to provide a good life for my family while not doing maintenance or security forces"
      },
      {
        "id": "mt06zlr",
        "score": 3,
        "body": "No. Choosing your job can be very important... Especially since some army jobs have a far better quality of life than some air force jobs. Sure most airmen will experience better conditions than most soldiers.... But some soldiers are absolutely living the dream while some airmen are out at 4am in 20 degree rain saluting officers in their cars thankful even for the few seconds of heat that blows out of their windows as they pass."
      },
      {
        "id": "msy3aid",
        "score": 3,
        "body": "Yes. You can \"pick your job\" in any Branch w/ the recruiter lol you just need to qualify for it & a slot needs to be open. The AF from what I've gathered, treats the enlisted MUCH better than the Army. I was in the Army and I would choose the AF if I did it again."
      }
    ]
  }
]
```
