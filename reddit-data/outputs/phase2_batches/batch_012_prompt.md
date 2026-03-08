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
    "id": "1rih1hr",
    "title": "Dress uniform form 15+ years ago",
    "body": "So I was going through all my stuff and my kids saw my dress uniform form my military days. Daughter is 13 and I was out before she was born, so naturally she wants to see what it looked like. Tried it on, as best I could, and it has officially shrank in my closet. Asked my father in law, his shrank too. Same as my father. At this point, I am convinced the military makes it clothes out of fabric that shrinks after sitting in closets for years.",
    "flair": "Discussion",
    "score": 99,
    "comment_count": 26,
    "created_at": "2026-03-02T02:44:31+00:00",
    "top_comments": [
      {
        "id": "o85ypvf",
        "score": 26,
        "body": "I have my grandpa's from WWII and it looks like a 12 year old could wear it."
      },
      {
        "id": "o85xsk9",
        "score": 25,
        "body": "It's like a cruel joke, isn't it, the Incredible Shrinking Closet."
      },
      {
        "id": "o87wxl7",
        "score": 21,
        "body": "They 100% got the joke and responded in kind."
      },
      {
        "id": "o88369a",
        "score": 20,
        "body": "I thought for years the dryer was shrinking all my clothes. Turns out it was the refrigerator."
      },
      {
        "id": "o86honv",
        "score": 17,
        "body": "If clothes are not worn regularly then the threads of the weave tighten up resulting in shrinkage. \n\nScience."
      },
      {
        "id": "o85yljd",
        "score": 10,
        "body": "My 13 button trowsers didn't fit 4 years after I got out. They made cracker jacks to fit for 1 moment in your life, zero forgiveness!"
      },
      {
        "id": "o869jug",
        "score": 10,
        "body": "my dad's greens were the same way, i was 13 when i could last fit into them and i still to this day can't understand how this man could fit into it"
      },
      {
        "id": "o886uvj",
        "score": 9,
        "body": "My dude - joined at 18 myself and def heavier. Sorry for trying to play along"
      },
      {
        "id": "o864w9n",
        "score": 5,
        "body": "At a Veterans Day event a few years back, we saw an Army WWII Veteran in his dress uniform. Impressive AF."
      },
      {
        "id": "o86t8z9",
        "score": 4,
        "body": "Mine shrank while serving. But 13 years later they reversed and grew back."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rifzfw",
    "title": "Can I rejoin with a re4 code",
    "body": "to put things in basic terms my ex wife accused me of rape to get a divorce from me I was very hurt at the time my commander demanded I pay her 1700 a month thas all my bah we had an apartment together and I could not afford it I was barred from reenlistment unless I paid her in full than when the investigation was over it was left up to my commander on the decision to have me removed from the army he and my ex-wife were talking more than I was talking to him so he motion forward with my lieutenant colonel to go ahead and push for me to get put out I was given a general discharge with honorable conditions and I was found innocent of rape in both civilian court and military uniform code of justice so I want to know if I can rejoin with all this information",
    "flair": "Question/Advice",
    "score": 0,
    "comment_count": 43,
    "created_at": "2026-03-02T01:54:59+00:00",
    "top_comments": [
      {
        "id": "o85pl5n",
        "score": 25,
        "body": "That\u2019s a hard battle to fight. Move on."
      },
      {
        "id": "o85ptry",
        "score": 23,
        "body": "Bro what!?"
      },
      {
        "id": "o85ppuk",
        "score": 21,
        "body": "damn dude, that's a rough situation. You should definitely talk to a recruiter about your specific circumstances since a General discharge can sometimes be waivered depending on the branch and their current needs \ud83d\udc80 \n\n  \nThe fact that you were cleared of all charges should work in your favor, but each case is different so you'll need someone who can actually pull up your records and see what's possible."
      },
      {
        "id": "o85qro7",
        "score": 16,
        "body": "That\u2019s wild this even happened, good reminder for me to never get married and die alone"
      },
      {
        "id": "o85qo8s",
        "score": 16,
        "body": "Not worth it dude. Not at all."
      },
      {
        "id": "o85xax5",
        "score": 9,
        "body": "Its an even tougher fight that he let on. He did not get denied re-enlistment for the accusations. OP said in another comment \n\n\"I stopped showing up to work because of it but my psg said all I had to do was call in and check in my jag lawyer wanted to fight it and I had to go to fap for like 6 months but I decided not to go ahead with fighting for it I didn't see a reason I just wanted to leave but I want back in now\". \n\n\n\nSo they had accusations; he was ordered to pay all his BAH, but he should have lawyered up. Instead, he didn't fight because it was a crap situation, took the L and got out. Thats a fight hes not going to win. He didn't get kicked out because of the accusations he got kicked out because he stopped going to work. Sounds like his psg tried to do him a solid by telling him to just check in with his lawyer, which makes me wonder if his wife was mil or civ, but at the end of the day he checked out. They did not push him to not re-enlist, he said he wanted out. The story was all over the place, makes me wonder if he was found innocent, or was the case dismissed due to lack of evidence. Depending on when it happened it would have been a he-said-she-said. "
      },
      {
        "id": "o85pylu",
        "score": 8,
        "body": "Not gonna happen."
      },
      {
        "id": "o85tyt8",
        "score": 8,
        "body": "Best of luck OP. I deservingly got a RE-4. Im tempted to rejoin, but that also feels like running back into a burning building...."
      },
      {
        "id": "o85qkrk",
        "score": 7,
        "body": "He can also look into getting it bump up.   Of course there other side to the story.   If he wasn\u2019t found guilty what was the reason for the general discharge then?"
      },
      {
        "id": "o85s02t",
        "score": 7,
        "body": "Sounds like you checked out before you checked out.   I know things were rough and it can\u2019t change, but if you really want to go back in look at getting your discharge or R rating upgraded/waived."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1ri8mwu",
    "title": "New Mexico, it looks like a 30% disabled vet would get 30% reduction of property taxation.",
    "body": "In New Mexico, it looks like a 30% disabled vet would get 30% reduction of property taxation.  \n...and a 50% disabled vet would get 50% reduction.  Most sites disagree but the State's own Veteran's Exemption form says this:\n\n\"Veteran Tax Exemption: Up to Ten thousand dollars ($10,000) of the taxable value of property, including the community or joint property of husband and wife, subject to the tax is exempt from the imposition of the tax if the property is owned by a veteran or the veteran\u2019s un-remarried surviving spouse if the veteran or surviving spouse is a New Mexico resident.  \n\n\nDisabled Veteran Tax Exemption: The property of a disabled veteran, including joint or community property of the veteran and the veteran\u2019s spouse, receives an exemption from the taxable value of property **equivalent to the veterans VA Service Connected Disability rating**. The Property must be occupied by the disabled veteran as the veteran\u2019s principal place of residence.\n\nIs there any 10-50% veteran living there that can confirm this?",
    "flair": "Question/Advice",
    "score": 19,
    "comment_count": 7,
    "created_at": "2026-03-01T20:48:35+00:00",
    "top_comments": [
      {
        "id": "o85vqqt",
        "score": 4,
        "body": "I voted on this a couple years ago for NM. Super glad it passed because before bets under a percentage were essentially not able to get anything. Now it's a scale so seems more fair to me."
      },
      {
        "id": "o85nmym",
        "score": 4,
        "body": "At 70%, Illinois gives you a 100% exemption for property taxes."
      },
      {
        "id": "o85iaoi",
        "score": 3,
        "body": "I did some additional digging and can confirm that this is the case, and it's a new Disabled Vet benefit for the state, which is why most benefit breakdowns don't account for it.\n\nThis government site/page is what confirms this to be just as the application says, giving an example with a 70% disabled vet.\n\n[https://www.bernco.gov/blog/2025/10/31/exemption-formula-for-veterans-with-service-connected-disability-is-now-set/](https://www.bernco.gov/blog/2025/10/31/exemption-formula-for-veterans-with-service-connected-disability-is-now-set/)  \n\n\nGreat seeing a state extend a financial break to disabled vets like this.  I'm not aware of any other state going quite this far for those rated between 10-90%, regarding reductions on property tax.  \n\nBravo New Mexico!  (we don't live there)"
      },
      {
        "id": "o85thvo",
        "score": 3,
        "body": "Yep, that's also a rare break, but below 70%, no break on property tax.  I'm not saying that's bad either.  States have to cover the bills and tax is how it's done.\n\nThat said, bravo to Illinois for going farther than nearly all other states have."
      },
      {
        "id": "o886cdv",
        "score": 2,
        "body": "That\u2019s true but the amount paid by veterans has to be pretty small"
      },
      {
        "id": "o8nwpl9",
        "score": 1,
        "body": "You're reading it correctly, but there's some confusion in how it's worded. New Mexico's veteran property tax exemption is a flat amount, not a percentage based on your rating. The law allows up to $10,000 of taxable value to be exempt if you're a disabled veteran with a service-connected disability rating. The percentage part doesn't mean your rating equals your exemption percentage.\n\nWhat you get is the full $10,000 exemption if you meet the eligibility criteria, which typically requires at least a 10% service-connected disability rating. Some counties or municipalities may have additional local exemptions or benefits that scale with your rating, but the state-level exemption under New Mexico law is that $10,000 regardless of whether you're 30%, 50%, or 100%.\n\nIf you're seeing conflicting information, it might be because some sites are confusing New Mexico's rules with other states that do use a sliding scale based on rating percentage. Your best bet is to contact your county assessor's office with your VA disability letter and ask them to walk you through exactly what exemption you qualify for. They'll have the definitive answer for your specific property and situation."
      },
      {
        "id": "o8ce4n4",
        "score": 1,
        "body": "Congratulations on it passing, and being put into action!"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1ri8gwb",
    "title": "GI Bill Not Paying?",
    "body": "Hi, \n\nI have used the GI Bill for years without issue - in fact I am finally running out and I am halfway done with my doctorate. That said since the shut down in October the payouts have been so delayed - is anyone else experiencing this?\n\nHere is my most recent schedule and payout: \n\n  \nDates: 10/20/25 \u2013 12/12/25  \nLast Payment: 12/31/25 - Partial month for Dec\n\n  \nDates: 01/19/26 \u2013 03/13/26  \nNo Payment in Jan but a $250 book stipend  \nNo Payment in Feb at all\n\nI called the hotline and they just said its \"processing\" and that I can keep checking back but they didn't give me any clarification. \n\nIs anyone else not getting their payment?\n\n  \n",
    "flair": "Question/Advice",
    "score": 11,
    "comment_count": 15,
    "created_at": "2026-03-01T20:42:12+00:00",
    "top_comments": [
      {
        "id": "o86vpox",
        "score": 3,
        "body": "Got my payment for January (partial of course due to class starting the 12th) but nothing for February as of yet."
      },
      {
        "id": "o8b68l6",
        "score": 2,
        "body": "Im still waiting for mine too. They always pay on time it\u2019s wierd. They haven\u2019t even sent me a confirmation text for attendance"
      },
      {
        "id": "o8euzi2",
        "score": 2,
        "body": "I haven\u2019t gotten mine yet either. When I talked to them they said it was processing but on my va.gov page it didn\u2019t show up under payments. Idk"
      },
      {
        "id": "o8jhri0",
        "score": 2,
        "body": "Mine doesn\u2019t even say that it\u2019s pending on the VA website itself; that\u2019s odd"
      },
      {
        "id": "o8e616j",
        "score": 1,
        "body": "Due to ongoing IT system issues and a new, delayed digital GI Bill rollout, many payments are facing processing backlogs, with some being handled manually. \n\nSystem Delays: A new, $2.3 billion digital GI Bill system is experiencing bugs, causing delays in tuition and housing stipends."
      },
      {
        "id": "o8fkwjz",
        "score": 1,
        "body": "**Same, my class started a month ago, I don't even think my school sent the enrollment certification yet.** No Payment in Jan, and No Payment in Feb, No book stipend, and No school tuition."
      },
      {
        "id": "o8ha3q8",
        "score": 1,
        "body": "Nothing yet for February for me either and I don\u2019t even see it in my pending payments"
      },
      {
        "id": "o8i56w8",
        "score": 1,
        "body": "I\u2019m seeing mine on the website it\u2019s pending but says n/a. Hopefully it\u2019ll pay in the next couple of days. Not showing on the app tho. Good thing I had enough in my account to cover rent "
      },
      {
        "id": "o8n8p2b",
        "score": 1,
        "body": "Got a payment today but need to calculate if it was everything. Should have been part of Jan and all of February. Hoping that March is not delayed again too. "
      },
      {
        "id": "o8ha9a1",
        "score": 1,
        "body": "Same"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1ri7yvp",
    "title": "VA ch 33 payments",
    "body": "Has anyone not gotten their BAH yet for the GI Bill? It\u2019s alr Mar 1st and ik usually we would have gotten paid earlier. They asked me to confirm enrollment yesterday, so i was wondering if anyone was also let unpaid for now. Hoping they pay tomorrow, rent is due yk haha ",
    "flair": "GI Bill/Education",
    "score": 11,
    "comment_count": 41,
    "created_at": "2026-03-01T20:23:12+00:00",
    "top_comments": [
      {
        "id": "o8489a7",
        "score": 2,
        "body": "Still waiting on mines"
      },
      {
        "id": "o86nd2v",
        "score": 2,
        "body": "Still waiting"
      },
      {
        "id": "o88h3rp",
        "score": 2,
        "body": "Received confirmation text yesterday , still waiting with USAA."
      },
      {
        "id": "o8auooe",
        "score": 2,
        "body": "still haven\u2019t gotten paid, this sucks lol"
      },
      {
        "id": "o8dy3sm",
        "score": 2,
        "body": "Still waiting on ch 33 as well"
      },
      {
        "id": "o8ekxiz",
        "score": 2,
        "body": "Did anyone receive it yet? \ud83d\ude2d I got the verification text that they usually send before it drops but it hasn\u2019t deposited"
      },
      {
        "id": "o8el4i2",
        "score": 2,
        "body": "Yup.. same here. Odd."
      },
      {
        "id": "o8jhc3p",
        "score": 2,
        "body": "Hasn\u2019t hit yet boys, feel like the green weenie is an ex that i can\u2019t block."
      },
      {
        "id": "o8ljgfr",
        "score": 2,
        "body": "Been checking and waiting, still nothing here."
      },
      {
        "id": "o8byrks",
        "score": 2,
        "body": "Bro me too, I'm glad it's not just me, I need that rn\ud83d\ude02"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1ri2118",
    "title": "TriCare 20/20/20 question",
    "body": "Hello, I'm writing on behalf of my mom, who was married to my dad, who is a veteran and now are seperated and preparing for divorce. \n\nshe was married to him for 22 years, but as an active duty wife, he's only served 19 years and 3 months as active duty while they were married. \n\nFrom what I'm aware, to qualify, 20 years of military service and 20 years of marriage must overlap for 20 years, but she's 9 months short. However, my dad did serve 2 years as part of the army reserve in their marriage and if those 2 years were fully counted, then the overlap between his military service and the marriage would exceed 20 years.\n\nBut the army reserve does not work every day like active duty; they typically work about twice a month. So if that time were calculated by actual days worked, my mom would still not reach 20 years. If the 2 years in the National Guard were counted as a full 2 years, then she would qualify for TRICARE 20 20 20.\n\nSo I am wondering how TRICARE calculates this when granting lifetime TRICARE benefits to a former spouse after a divorce judgment. What method do they use to calculate the time? Thank you. ",
    "flair": "Question/Advice",
    "score": 9,
    "comment_count": 6,
    "created_at": "2026-03-01T16:44:04+00:00",
    "top_comments": [
      {
        "id": "o84ubpp",
        "score": 5,
        "body": "Hello OP, I am really sorry you and your mom are going through this. I am a retired first sergeant and I walked a few airmen and their spouses through divorce. It\u2019s not easy. \n\nOn TriCare, the rule most people are thinking about is the 20/20/20 rule. That means three things must all be true. He must have at least 20 years of creditable service toward military retirement. The marriage must have lasted at least 20 years. And at least 20 of those years must overlap, meaning 20 years of marriage during 20 years of creditable service.\n\nThere is also the 20/20/15 rule. If there are at least 15 years of overlap between the marriage and his creditable service, but less than 20, your mom may qualify for one year of TriCare coverage after the divorce. This sounds more like what your mother will qualify for. But what she needs to confirm is your dad\u2019s official total creditable service for retirement. That number, not a calculation of drill weekends, is what TriCare will rely on. That can come from his S1, IPPS A  or Army Human Resource Command website. Your dad would need to get that information, I don\u2019t believe they would release it to the spouse. DD Form 214 may have it as well under Blocks 12c, 12d or 12e. \n\nOne last thing, if she\u2019s going to lose TriCare, she should ask about CHCBP. It is a premium based bridge plan that can provide temporary coverage, often up to 36 months if she qualifies and enrolls on time. It is not free, but it can prevent a sudden gap.\n\n[CHCBP](https://tricare.mil/Plans/SpecialPrograms/CHCBP/PurchaseCHCBP)\n\nIf I messed up here please be kind, at pool watching my daughter swim for team practice. Plus I\u2019m on my phone. Best of luck OP."
      },
      {
        "id": "o82uklu",
        "score": 2,
        "body": "If the beneficiary qualifies for Tricare, then so does she. As long as she doesn\u2019t remarry"
      },
      {
        "id": "o82ww6r",
        "score": 1,
        "body": "She probably qualifies under the 20-20-15 rule - https://tricare.mil/Plans/Eligibility/FormerSpouses"
      },
      {
        "id": "o8fgkfy",
        "score": 1,
        "body": "It's going to be based on whether the servicemembers reserve time was creditable towards retirement. If it wasn't, it doesn't count. \n\nFor retirement eligibility, the servicemember must have accrued at least 50 points during a given year for it to be creditable. \n\n\n- 1 point per day of active service\n\n- 1 point for each attendance at a drill period\n\n- 1 point for each day performing funeral honors duty\n\n- 15 points for each year of membership in the reserves. \n\n\nBest thing for her to do is contact the appropriate service personnel component. Army Reserve can be reached at 888.276.9472."
      },
      {
        "id": "o8aw4up",
        "score": 1,
        "body": "That is not true. Not at all. It ends at divorce unless they are eligible for the 20/20/20 or 20/20/15 rules stated elsewhere in this thread."
      },
      {
        "id": "o82vw6s",
        "score": 0,
        "body": "may I ask what you mean? do you mean that if I still have tricare she does as well?"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rhqrr8",
    "title": "Behind on everything and can\u2019t catch up. Just listen or advice",
    "body": "Hey veterans world 100% P&T who\u2019s GF broke up with him and was a two income household but went down to a single I have a decent job but missed an entire week of work when one of my disabilities flared up. And just struggling to catch up and always seem behind. Just renewed this lease and I live in Connecticut and of course the rent is ridiculous at 3400 a month and I don\u2019t know what to do I do contact the Va homeless or at risk and was forwarded to that and will be waiting on a call next week I\u2019m assuming. I just wanted to write it here as idk what to do so wanted to more or less vent. ",
    "flair": "Question/Advice",
    "score": 20,
    "comment_count": 42,
    "created_at": "2026-03-01T07:11:29+00:00",
    "top_comments": [
      {
        "id": "o81jrbv",
        "score": 9,
        "body": "Have you considered getting a roommate?"
      },
      {
        "id": "o80ohx8",
        "score": 8,
        "body": "Hey man i was living the American dream and my ex left me and I spiraled nearly lost everything and became behind in everything.\n\nAll I can tell you is everything will be okay.\n\nKeep going forward one foot in front of the other.\n\n\n\nMaybe move dude cuz wdf is that rent."
      },
      {
        "id": "o82ogjb",
        "score": 5,
        "body": "Do you have an extra room to rent out? Start making plans to leave the state. There\u2019s plenty of states that you can live off the 100% alone. \n\nHow is your budget? What other monthly expenses do you have? Since you have a FT job as well, there\u2019s no reason you should be behind. You really need to tighten the budget until you can get out of your living situation and into something more reasonable."
      },
      {
        "id": "o82jrwb",
        "score": 5,
        "body": "I always hate these post about not being able to afford things then you have single dude renting paying $3400. That\u2019s insane. Lifestyle creep is real. We moved back to Kentucky and our mortgage dropped in half from what we were paying in California. Same size house."
      },
      {
        "id": "o82pn4z",
        "score": 5,
        "body": "This is stupidity. Get a roommate."
      },
      {
        "id": "o81rm4a",
        "score": 4,
        "body": "You were paying way too much for rent"
      },
      {
        "id": "o81uge7",
        "score": 4,
        "body": "Good time to get out of Connecticut if you ask me."
      },
      {
        "id": "o82para",
        "score": 4,
        "body": "Seriously. It\u2019s so easy. There are entire groups on Facebook where people are looking for roommates. That\u2019s how I found mine."
      },
      {
        "id": "o82p1p0",
        "score": 4,
        "body": "So break it and move into a cheaper spot. I seriously doubt that 3400 is the least you could get a 1br apartment for. Look for a studio while you regroup."
      },
      {
        "id": "o80nnpw",
        "score": 4,
        "body": "Reach out to your local VFW or American Legion and see if they have an emergency fund to help veterans in need. Otherwise reach out to your local Vet Center and see if they have any resources locally that can help out."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rhofut",
    "title": "Do you ever dream that you've reenlisted?",
    "body": "I have a recurring dream, bordering nightmare, that I've reenlisted in the Army. But it isn't my in-shape self of 20 years ago, it's me, now, and I'm already late for my first formation. Hell, sometimes I'm just wandering the company AO, trying to figure out where I'm supposed to go.\n\nAnyone else have similar recurring dreams? Does this essentially replace the \"back in high school\" dream so many others have? Because I've never had that one.",
    "flair": "Discussion",
    "score": 92,
    "comment_count": 91,
    "created_at": "2026-03-01T05:01:39+00:00",
    "top_comments": [
      {
        "id": "o806btu",
        "score": 26,
        "body": "I've had dreams where I'm on the ship again, reliving stressful events or variations similar to them. Maybe get them once a month or so."
      },
      {
        "id": "o806fhh",
        "score": 21,
        "body": "I still have dreams that I\u2019ve misplaced my rifle after almost 20 years of being out, and it\u2019s still panic inducing every single time."
      },
      {
        "id": "o807kaw",
        "score": 18,
        "body": "I've reenlisted. I'm missing half my uniform. I'm lost. Muster is in twenty minutes and an Army Sergeant Major is in charge. I've forgotten all of my military bearing. And I'm going to be late."
      },
      {
        "id": "o807fxk",
        "score": 12,
        "body": "Yes! I have recurring dreams where I'm back in the Navy Reserves. I retired back in 2008. I'm missing half my uniform, and I have to be ready to do my PFA at the ripe old age of 61. Yikes! "
      },
      {
        "id": "o80bee3",
        "score": 11,
        "body": "All the time brother, totally normal"
      },
      {
        "id": "o80ktt8",
        "score": 11,
        "body": "Same! And to top it off forgot to pack some of my uniforms! This very dream haunts me all the time, pull into port and realize I forgot my whites."
      },
      {
        "id": "o806yrp",
        "score": 10,
        "body": "That would be a nightmare. For me at least.\u00a0"
      },
      {
        "id": "o806r60",
        "score": 7,
        "body": "Frequently. I never belong.\u00a0 It's the very much the \"I miss the clowns, not the circus\" situation.\u00a0"
      },
      {
        "id": "o8074ok",
        "score": 7,
        "body": "Yes, and I've been out for 20 years."
      },
      {
        "id": "o809rg2",
        "score": 7,
        "body": "Reenlisted? No. Ended up back in the Army against my fucking will? Yes."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rhn5zk",
    "title": "My K9 best friend",
    "body": "Anyone have any helpful suggestions to deal with shit when your K9 best friend is the one going through it? My Karma, a 9 year old dutchie just had GDV surgery, which was successful, but then an additional complication due to pain. Back to back emergency vet visits and she\u2019s spending the night in their care. I\u2019m at a total loss without her and at a total loss trying to be there for her. Never expected anything to be so emotionally draining. This dog has always been my rock, but it never hit me so fully until this whole mess. PTSD, anxiety, etc and she\u2019s gotten me through everything and I feel like I\u2019m in the wind without her. What\u2019s the best way to get through it when your K9 best friend is going through it, I\u2019m drained giving everything I can to support her back.",
    "flair": "Question/Advice",
    "score": 139,
    "comment_count": 4,
    "created_at": "2026-03-01T03:56:04+00:00",
    "top_comments": [
      {
        "id": "o8008ub",
        "score": 3,
        "body": "I'm not sure i have anything helpful to add, just solidarity. My late service dog managed to keep my dumb ass alive for 15 years, and even a night without her was a shitty reality check. I'll be around if you wanna talk about Karma, and I'm rooting for you both"
      },
      {
        "id": "o81whmz",
        "score": 3,
        "body": "Nows the time to get a puppy and have your best friend train the puppy."
      },
      {
        "id": "o8oorr4",
        "score": 1,
        "body": "My Karma aka Karmageddon wishes her a speedy recovery"
      },
      {
        "id": "o80600r",
        "score": 1,
        "body": "Thanks brother, it\u2019s rough not having her home. But worse having her in my lap in pain. I know she is under great care, but so rough being away from me. Constantly worried I\u2019m not doing enough for her. No way to put a tangible amount of how much you really owe them for everything."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rhm6cp",
    "title": "Employer disability",
    "body": "Hi Reddit!\n\nUnfortunately I have to undergo some lengthy medical treatments at the VA that require\n\nMe to take FMLA. If the treatments don\u2019t work, I\u2019ll end up getting brain surgery. I\u2019m 100% and haven been struggling to keep working with all of this going on.\n\nSeveral of the doctors recommended I stop working soon, I have been so scared to tell work.. because I\u2019m worried about unpaid FMLA.\n\nI do have short and long term disability benefits through my employer.  I have been hearing that since my disability is from my service in Iraq.. that the employers insurance might deny paying the full benefits. I heard they can approve it but pay 0% and sometimes they do approve it for veterans health issues.\n\nHas anyone successfully been paid for STD or LTD through their employer benefits for issues directly from war time service? What was the process like?",
    "flair": "Employment",
    "score": 10,
    "comment_count": 19,
    "created_at": "2026-03-01T03:06:47+00:00",
    "top_comments": [
      {
        "id": "o7zvhg2",
        "score": 8,
        "body": "Why would your work know what it\u2019s is linked to? FMLA is protected status.\u00a0"
      },
      {
        "id": "o801qnt",
        "score": 4,
        "body": "I've used FMLA and STD for my SCD. My employer did give me ton of shit but not that kind. It may be something your might try. I would just remind you management team before you go out that you are a disabled vet and that is a protected class. That may in and of itself ward off some trouble or not. If they do give you shit. Fight back hard. Do not let HR try to screw you over threaten with getting a lawyer and calling the labor board. "
      },
      {
        "id": "o8bf6b3",
        "score": 1,
        "body": "Yes. They approved the STD with no problem and eventually I got on LTD. \n\nIt doesn't really matter when you got sick. You were able to work and now you can't. You will be fine and covered just like any other illness. \n\nI worked for 5 years after the military, but eventually I couldn't anymore due to service connected autoimmune disease. I got STD and eventually LTD and will receive LTD until im 62."
      },
      {
        "id": "o8c4vkk",
        "score": 1,
        "body": "Dealing with health issues while trying to keep your job is a lot to handle, especially when you're facing something as serious as brain surgery. It's completely understandable to feel scared about how your employer will react, especially with the added stress of unpaid FMLA.  \n  \nNavigating the intersection of service-related disabilities and employer benefits can be tricky. Many veterans have faced similar situations, and it can be helpful to connect with others who understand what you're going through. Sharing experiences and advice can sometimes lighten the load a bit. Just remember, you're not alone in this."
      },
      {
        "id": "o8ppoi6",
        "score": 1,
        "body": "First off, VA disability compensation is separate from your employer's short-term and long-term disability insurance. Your VA benefits won't be affected by whether you work or not since you're already rated at 100%, and employer disability payments typically don't reduce your VA compensation. They're considered different income streams.\n\nThat said, some employer disability policies do have clauses about offsetting benefits if you're receiving other disability income, like Social Security Disability. You need to read your policy carefully or talk to HR to confirm whether your VA benefits are considered in any offset calculation. Most private policies don't count VA compensation, but every plan is different.\n\nIf your doctors are recommending you stop working and you're worried about income, you might also consider applying for Social Security Disability Insurance if you haven't already. Being 100% P&T with the VA doesn't automatically qualify you for SSDI, but it can help your case. SSDI does offset some state and employer disability benefits, so again, check your policy. Also, if you end up needing to stop working long-term, look into Total Disability based on Individual Unemployability if you're not already receiving it. That might bump your compensation or solidify your status. Take care of yourself first\u2014money is important, but your health comes before the paycheck."
      },
      {
        "id": "o7zw6ep",
        "score": 1,
        "body": "I meant more so the short/long term disability provider, they will need info from the VA and I\u2019m afraid they might deny the claim because it all stems from my military service."
      },
      {
        "id": "o82rx2l",
        "score": 1,
        "body": "[removed]"
      },
      {
        "id": "o82xrh9",
        "score": 1,
        "body": "[removed]"
      },
      {
        "id": "o82y5jt",
        "score": 1,
        "body": "[removed]"
      },
      {
        "id": "o82z6kg",
        "score": 1,
        "body": "[removed]"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rhh3rj",
    "title": "used parachute",
    "body": "What does the Army do with un-serviceable parachutes? I look on ebay/marketplace and they are stupid expensive.\n\nI remember the pathfinder's office in Germany and they hung one from the ceiling and it was a cool looking office.\n\n  \n",
    "flair": "Question/Advice",
    "score": 17,
    "comment_count": 13,
    "created_at": "2026-02-28T23:14:53+00:00",
    "top_comments": [
      {
        "id": "o7zjju0",
        "score": 19,
        "body": "We had to sleep in a tank pit for a month in North Iraq so we took the cargo parachutes and tossed one on the ground around the tank pit, and one we put over that one and lifted it up with cargo net spreaders and it was the greatest tent ever. While all the rest of the squads we sleeping with scorpions, we had the motel 8 of fighting positions. I don't know what anyone else does with their parachutes."
      },
      {
        "id": "o7yncj5",
        "score": 12,
        "body": "If you're in the US, contact an FAA-certified rigger before you buy one for jumping yourself. Skydiving Drop Zones usually have one. Make sure he or she can service and inspect it.  If it's a round parachute, I wouldn't jump a round though. Squares are much better to steer."
      },
      {
        "id": "o7zixo8",
        "score": 6,
        "body": "I was on jump status and chute detail way back in the 1980's.  They get DXed to some mystical magical army place (3rd shop I think) that reviews the rigger's inspection and if agreed, they trash them after they cut the risers and the steering so dumb asses won't try to paraglide out the back of a deuce with them.  I was able to secure a T-10B during my travels.  It's still sitting up in my attic 40 years later."
      },
      {
        "id": "o7yt38e",
        "score": 6,
        "body": "I dont know any riggers still in or id ask. I remember the riggers would pull them out of their ass for awards and shit. "
      },
      {
        "id": "o7zio49",
        "score": 4,
        "body": "They are sold at auction in surplus bulk, like old tents, uniforms, and Humvees. I would recommend finding a military surplus store around you and talking to them. If they deal in actual surplus, they would be the ones I would talk to."
      },
      {
        "id": "o7ztsyy",
        "score": 3,
        "body": "I should have saved mine instead of throwing it away. I could have used it to make blankets or something warm lol"
      },
      {
        "id": "o818vde",
        "score": 3,
        "body": "https://go-armynavy.com/genuine-military-surplus/parachutes/"
      },
      {
        "id": "o7zseya",
        "score": 3,
        "body": "Id love a t 10 or the t11 from my day. That would be amazing on the wall. "
      },
      {
        "id": "o7yta39",
        "score": 3,
        "body": "I'm referring to civilian riggers at civilian skydiving drop zones. They can inspect, repair, and service used parachutes. Doesn't have to be a military rigger."
      },
      {
        "id": "o86wb9t",
        "score": 2,
        "body": "yum knee pad flavored blankets"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rhavkl",
    "title": "My family is about to be homeless and I don\u2019t know what to do",
    "body": "The landlord of the apartment we have been renting since I medically retired last October just ended our month to month lease because their business is failing. We have to be out by April 1 and \n\nwe don\u2019t know what to do.  ",
    "flair": "Question/Advice",
    "score": 45,
    "comment_count": 52,
    "created_at": "2026-02-28T19:01:08+00:00",
    "top_comments": [
      {
        "id": "o7xc5fz",
        "score": 58,
        "body": "Contact the HUD/VASH office at your local VA Medical Center. Their social workers are like magicians."
      },
      {
        "id": "o7xcr1q",
        "score": 33,
        "body": "Let the training kick it bro. Assess your financial situation and figure out how much money you have at the present moment. Explore housing rates in your area and areas nearby. Identify the best options based on which are closest to your current financial capabilities. Then go from there. You are already past the first step by having identified the problem. One foot in front of the other, just a little nature walk. You got this."
      },
      {
        "id": "o7xdkif",
        "score": 28,
        "body": "HUD/VASH is your lifeline. Call now."
      },
      {
        "id": "o7ya01c",
        "score": 25,
        "body": "Make sure to be VERY clear that you are at imminent  risk of homelessness. This is a key phrase that elevates your case based on need."
      },
      {
        "id": "o7ydzkg",
        "score": 19,
        "body": "VA SW are force multipliers, nothing short of amazing."
      },
      {
        "id": "o7xcuyr",
        "score": 14,
        "body": "Don't panic. \n\nYou have an entire month to find a place, pack, and move. \n\nWhat area are you in? What's your budget? How many people in your family? \n\nAssuming you're 100% rated, which is a pretty good starting point."
      },
      {
        "id": "o7xl1j5",
        "score": 12,
        "body": "Will do Monday"
      },
      {
        "id": "o7xzz6o",
        "score": 11,
        "body": "Call 1-800-MICH-VET (1-800-642-4838): The primary Michigan line for veterans experiencing housing instability. \n\nSupportive Services for Veteran Families (SSVF): Provided by organizations like VOA Michigan, offering rapid re-housing, rent assistance, and security deposit help for low-income veterans.\n\nVA Homeless Programs\nHUD-VASH\nMichigan Veterans Trust Fund:  Offers emergency grants to veterans for temporary, unforeseen financial hardships.\nFair Housing Center of West Michigan:  provides assistance with landlord-tenant disputes and evictions, especially if disabilities are involved.\n\nOr the VA medical center, such as the Grand Rapids Home for Veterans (as suggested before).\n\nGood luck!"
      },
      {
        "id": "o7xywr5",
        "score": 11,
        "body": "[deleted]"
      },
      {
        "id": "o7xn86g",
        "score": 9,
        "body": "Ok so you have a permanent semi decent income, rental history, and time to find a place and move. What specific issues are you running into?\n\nLook for rentals in your area through normal sources. Zillow, Redfin, etc."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rh2ty6",
    "title": "Saw this today, and I feel, while it's trite, it's TRUE",
    "body": "\"Beating the competition is relatively easy, \n\nBut beating yourself is a never-ending commitment.\"      (Nike)\n\nI feel like this is what we need to do, every day as Veterans. \n\nCheers.",
    "flair": "Discussion",
    "score": 9,
    "comment_count": 4,
    "created_at": "2026-02-28T13:36:48+00:00",
    "top_comments": [
      {
        "id": "o7wb4i6",
        "score": 4,
        "body": "I beat myself first thing every morning"
      },
      {
        "id": "o7whah7",
        "score": 2,
        "body": "LMAO. Well, that probably helps your mental health, so go you! "
      },
      {
        "id": "o85erpz",
        "score": 1,
        "body": "The last time I took advice from Nike I almost got done at a sewer plant.  Well, guess I'd better just do it again."
      },
      {
        "id": "o8fxkch",
        "score": 1,
        "body": "I\u2019m dead \ud83d\ude02\ud83d\ude02\ud83d\ude02. On a side note, I\u2019m glad I\u2019m not the only one."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgvhur",
    "title": "Got this petition in the mail from the American legion. Is this legit or a scam?",
    "body": "Today I just got an envelope in the mail thay said \"do you believe veterans need access to Healthcare \" and inside was a letter from the American legion asking me to sign a petition for the ACCESS Act. Will this actually make a difference? \n\nThis is the first time i have gotten a petition from the American legion ",
    "flair": "Question/Advice",
    "score": 8,
    "comment_count": 5,
    "created_at": "2026-02-28T06:39:32+00:00",
    "top_comments": [
      {
        "id": "o7ufat0",
        "score": 3,
        "body": "No idea. Posting here to follow the post, and answers.\u00a0"
      },
      {
        "id": "o83bz9w",
        "score": 3,
        "body": "Probably not.  But if you do respond you can be assured you will be receiving more mail, email, and texts (if you included email and telephone number) from various organizations soliciting donations.\n\nAll of these veterans organizations do have pull with Congress, but they don't need individuals to sign anything.  There whole purpose is to represent the needs of veterans and advocate for them.\n\nYour better choice would be to contact your Congressman and request they support the act, at least that way you'll stop the annoying emails, texts, phone calls, and mailings."
      },
      {
        "id": "o7xdnrh",
        "score": 2,
        "body": "Not just veterans, How about all Americans?"
      },
      {
        "id": "o83db1v",
        "score": 2,
        "body": "It's one way the Legion generates community involvement and the info helps them direct the mission."
      },
      {
        "id": "o83d2m3",
        "score": 0,
        "body": "Yes, all Americans.. but the Legion represents Veterans so that is their mission.  Other organizations are (or should be) running the all Americans missions.. AMAC, AARP, the two that pop to mind.."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgug3u",
    "title": "PSA for any of ya'll who rely on annual physicals",
    "body": "Apparently we're winning so much, the VA no longer auto schedules an annual physical. At least for me. Discharged just over 11 years ago, and since then almost like perfection, received a notification no later than the end of January of an upcoming appointment in February. Hump it to the local clinic, get a blood work up, return in a week, get my ears, nose, and heart checked, out in an hour. This year, crickets. About 2 weeks ago the radio silence hit me, so I sent a secure Healthevet message asking what's up. Got a call 2 days ago - \"sorry we don't have a doc, take 2 aspirin and check back in September.\"\n\nLOL!",
    "flair": "Discussion",
    "score": 50,
    "comment_count": 37,
    "created_at": "2026-02-28T05:40:37+00:00",
    "top_comments": [
      {
        "id": "o7uu1w6",
        "score": 61,
        "body": "They have us schedule our next one as we check out of the current one\u2026"
      },
      {
        "id": "o7vuau5",
        "score": 28,
        "body": "That's what my VA has always done."
      },
      {
        "id": "o7uavhh",
        "score": 18,
        "body": "It sounds like your facility.\u00a0 You should be able to ask for community care due to their staffing.\u00a0"
      },
      {
        "id": "o7vn4n1",
        "score": 15,
        "body": "It\u2019s bs. He made up that quote."
      },
      {
        "id": "o7vyo4w",
        "score": 14,
        "body": "Isn't that how all appointments work?"
      },
      {
        "id": "o7voigh",
        "score": 13,
        "body": "Yeah, I don't think they're Auto scheduled, except for the idea that your doctor should have scheduled it for you when you were at your last appointment. \n\nMaybe it just slipped their mind."
      },
      {
        "id": "o7uzogu",
        "score": 11,
        "body": "I\u2019ve been out since 08 and never had an apt auto scheduled. That would piss me off. I work and schedule when I have time. Also every time I need a follow up it\u2019s scheduled when I check out that day."
      },
      {
        "id": "o7u43bq",
        "score": 10,
        "body": "Had my annual a few weeks ago.  I hadn't been gone 15 min when they scheduled me for 2027."
      },
      {
        "id": "o7vrcto",
        "score": 10,
        "body": "Never been auto scheduled\u2026"
      },
      {
        "id": "o7v1mf2",
        "score": 8,
        "body": "This is facility dependent.  They always schedule me when I go to my appointment.\n\nAlso, you can send a secure message and have them put in an order for labs anyways."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgtk0b",
    "title": "Housing (bah)",
    "body": "Do you get bah for doing online school? If yes how much? And how soon do you get it? ",
    "flair": "GI Bill/Education",
    "score": 1,
    "comment_count": 18,
    "created_at": "2026-02-28T04:53:00+00:00",
    "top_comments": [
      {
        "id": "o7u53q0",
        "score": 2,
        "body": "No you don\u2019t get BAH, that\u2019s specifically for the military. Using the Post 9/11 GI bill you receive MHA, monthly housing allowance. The online only is 1169 for a full month which is half of the national average."
      },
      {
        "id": "o7u5s5h",
        "score": 2,
        "body": "you have to sign up/apply for either chapter 31 or chapter 33 benefits. Its not automatic."
      },
      {
        "id": "o7x90nb",
        "score": 2,
        "body": "Veterans should use the correct terminology. The mod that is most active on this sub will correct comments that say BAH instead of MHA. \n\nYeah, we know that OP meant MHA, but what\u2019s the harm in correcting them on the proper terminology?"
      },
      {
        "id": "o7tvjq8",
        "score": 1,
        "body": "'Have you looked in the **[Wiki]( https://www.reddit.com/r/Veterans/wiki/education)** for an answer? We have a lot of information posted there. \n\nTo contact VA Education, 1-888-442-4551, for ~~Voc Rehab~~ VR&E (Veteran Readiness and Employment Program) assistance with appointments or problems with your Case Manager (not for missing payments): 1-202-461-9600. \n\n**Payments for certain education benefits (DEA, VEAP) are paid at the end of the month you attend school - Department of Treasury issues these payments **using a 10 business day window** - these payments are not locked into a specific day of the month like VA disability/military pay is**. For Voc Rehab missing payments, contact your Case Manager or your local **[VA Regional Office](https://www.knowva.ebenefits.va.gov/system/templates/selfservice/va_ssnew/help/customer/locale/en-US/portal/554400000001018/content/554400000260849/VRE-Officers-and-Contact-Information)\n\nFor Post 9/11 GI Bill only, If you signed up for direct deposit when you applied for education benefits, **we\u2019ll deposit your payment into your bank account 7 to 10 business days after you verify your school enrollment.** This is the fastest way to receive your payment. [Text Verification FAQ](https://benefits.va.gov/GIBILL/docs/IsaksonRoe/EnrollmentVerificationFAQs.pdf)\n\nMGIB and MGIB-SR and DEA CH 35 have to do [monthly verification](https://www.va.gov/education/verify-school-enrollment/) and you should receive the payment within 3 to 5 business days.\n\nFor Online Only training, the Post 9/11 GI Bill is currently **(1 August 2025) paying $1169.00** for those who started using their Post 9/11 GI Bill on/after 1 January 2018 - this is based on 1/2 of the National Average BAH paid to an E5 with dependents. Post 9/11 GI Bill MHA rates are adjusted 1 August of each year and are based on the 1 January DoD BAH rates for that year - **so VA can't use 1 January 2025 BAH rates until 1 August 2025** - for those who started training on/after 1 January 2018, the MHA rates are 95% of the DoD BAH rates. First possible payment for the 1 August 2025 increase is 1 September.\n\nFor VR&E, there are two different Subsistence Allowance programs - https://www.benefits.va.gov/vocrehab/subsistence_allowance_rates.asp The P9/11 Subsistence Allowance is based on the BAH paid to an E5 with dependents. Those who started using VR&E on/after 1 January 2018 receive 95% of the BAH paid to an E5 with dependents. **As of 1 January 2026 Online only students using VR&E are being paid $1198.00** if they started using VR&E on/after 1 January 2018. The CH31 Subsistence Allowance rates are adjusted 1 October each year by Congress.\n\nVA Education is going paperless - make sure VA has a current email address for you. Please make sure you add Veteransbenefits@messages.va.gov to your contacts list so that you don't miss important updates from VA.\n\n[VA Award Letter explanation](https://benefits.va.gov/gibill/understandingyourawardletter.asp)\n\n[Contact a VR&E Supervisor](https://www.knowva.ebenefits.va.gov/system/templates/selfservice/va_ssnew/help/customer/locale/en-US/portal/554400000001018/content/554400000260849/VRE-Officers-and-Contact-Information)\n\n [VA Rudisill Decision](https://benefits.va.gov/gibill/rudisill.asp) - some veterans may qualify for an additional 12 months of a second GI Bill based on serving two or more different periods of active duty service.\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Veterans) if you have any questions or concerns.*"
      },
      {
        "id": "o7ukj2l",
        "score": 1,
        "body": "get a hybrid program. I only have to go the first day of each semester. Full BAH (MHA) at e5 rate.\n\n  \nYou talk to the veteran office at your school to get it certified."
      },
      {
        "id": "o7x9y2g",
        "score": 1,
        "body": "Yes you can get MHA for online classes. However, depending on what the VA considers full time, 1-2 of those classes must be in person. If the school has it, a HyFlex class can meet the in person requirement. Currently, that\u2019s what I\u2019m doing."
      },
      {
        "id": "o85l8yu",
        "score": 1,
        "body": "dont say 'bah' about houzing! its important!\n\n\ud83d\ude06"
      },
      {
        "id": "o7u591s",
        "score": 1,
        "body": "Do I have to do anything? Or\nDoes it automatically get deposited? And how long does it take? After I start school?"
      },
      {
        "id": "o7uphua",
        "score": 1,
        "body": "I think you\u2019re getting stuck in semantics (BAH vs MHA).  Also, to answer his original question there are different requirements and amounts for this allowance when you\u2019re going to online school vs a physical campus, which is what I think he was getting at in his original post."
      },
      {
        "id": "o7yiwoj",
        "score": 1,
        "body": "What school do you attend is it local and is mha high?"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgszce",
    "title": "Retroactive Induction of GI Bill if you have already completed VR&E program?",
    "body": "So I just found out about this retroactive induction aspect of the VR&E program. \n\nI don't know if my situation would be particularly unique, but I graduated in 2020 under Voc Rehab with my engineering degree. I would have been completely eligible under VR&E or Voc Rehab at the time, the entire duration of my schooling.\n\nBefore using Voc Rehab I was using the PGIB. Getting my time back would allow me to pursue a masters in my engineering field as it would get me back at least another 18 months.\n\nI am not currently under VR&E as I graduated obviously and am an employed engineer but I am still technically eligible and I went through the whole song and dance so I think it counts as successfully completed the Voc Rehab/VR&E program. \n\nHow would I go about trying to get this ball rolling? Anyone have any experience? ",
    "flair": "Question/Advice",
    "score": 6,
    "comment_count": 3,
    "created_at": "2026-02-28T04:22:54+00:00",
    "top_comments": [
      {
        "id": "o7trdnu",
        "score": 1,
        "body": "'Have you looked in the **[Wiki]( https://www.reddit.com/r/Veterans/wiki/education)** for an answer? We have a lot of information posted there. \n\nTo contact VA Education, 1-888-442-4551, for ~~Voc Rehab~~ VR&E (Veteran Readiness and Employment Program) assistance with appointments or problems with your Case Manager (not for missing payments): 1-202-461-9600. \n\n**Payments for certain education benefits (DEA, VEAP) are paid at the end of the month you attend school - Department of Treasury issues these payments **using a 10 business day window** - these payments are not locked into a specific day of the month like VA disability/military pay is**. For Voc Rehab missing payments, contact your Case Manager or your local **[VA Regional Office](https://www.knowva.ebenefits.va.gov/system/templates/selfservice/va_ssnew/help/customer/locale/en-US/portal/554400000001018/content/554400000260849/VRE-Officers-and-Contact-Information)\n\nFor Post 9/11 GI Bill only, If you signed up for direct deposit when you applied for education benefits, **we\u2019ll deposit your payment into your bank account 7 to 10 business days after you verify your school enrollment.** This is the fastest way to receive your payment. [Text Verification FAQ](https://benefits.va.gov/GIBILL/docs/IsaksonRoe/EnrollmentVerificationFAQs.pdf)\n\nMGIB and MGIB-SR and DEA CH 35 have to do [monthly verification](https://www.va.gov/education/verify-school-enrollment/) and you should receive the payment within 3 to 5 business days.\n\nFor Online Only training, the Post 9/11 GI Bill is currently **(1 August 2025) paying $1169.00** for those who started using their Post 9/11 GI Bill on/after 1 January 2018 - this is based on 1/2 of the National Average BAH paid to an E5 with dependents. Post 9/11 GI Bill MHA rates are adjusted 1 August of each year and are based on the 1 January DoD BAH rates for that year - **so VA can't use 1 January 2025 BAH rates until 1 August 2025** - for those who started training on/after 1 January 2018, the MHA rates are 95% of the DoD BAH rates. First possible payment for the 1 August 2025 increase is 1 September.\n\nFor VR&E, there are two different Subsistence Allowance programs - https://www.benefits.va.gov/vocrehab/subsistence_allowance_rates.asp The P9/11 Subsistence Allowance is based on the BAH paid to an E5 with dependents. Those who started using VR&E on/after 1 January 2018 receive 95% of the BAH paid to an E5 with dependents. **As of 1 January 2026 Online only students using VR&E are being paid $1198.00** if they started using VR&E on/after 1 January 2018. The CH31 Subsistence Allowance rates are adjusted 1 October each year by Congress.\n\nVA Education is going paperless - make sure VA has a current email address for you. Please make sure you add Veteransbenefits@messages.va.gov to your contacts list so that you don't miss important updates from VA.\n\n[VA Award Letter explanation](https://benefits.va.gov/gibill/understandingyourawardletter.asp)\n\n[Contact a VR&E Supervisor](https://www.knowva.ebenefits.va.gov/system/templates/selfservice/va_ssnew/help/customer/locale/en-US/portal/554400000001018/content/554400000260849/VRE-Officers-and-Contact-Information)\n\n [VA Rudisill Decision](https://benefits.va.gov/gibill/rudisill.asp) - some veterans may qualify for an additional 12 months of a second GI Bill based on serving two or more different periods of active duty service.\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Veterans) if you have any questions or concerns.*"
      },
      {
        "id": "o7trzz4",
        "score": 1,
        "body": "https://www.va.gov/education/check-remaining-post-9-11-gi-bill-benefits/\n\nJust check online. I requested a certificate of eligibility and found out I had like 30 months restored after graduating with Voc rehab years ago."
      },
      {
        "id": "o7tteuj",
        "score": 0,
        "body": "I did do the initial check online as I was applying to grad schools and I had as much time as I thought I had. As I was googling I found out about the retroactive induction was I believe implemented after I graduated hence my conundrum as trying to figure how to get the ball rolling after having completed the program to get back some of my PGIB time is something nebulous. "
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgrdfb",
    "title": "How do yall keep going?",
    "body": "When i was leaving the miltary i always told myself i would never be the guy who has a hard time transitioning into civilian life. I had a job at 16 all the way till i joined the army at 18. I got out at 21 years old and ever since then my body has been stuck in fight or flight like i am constantly waiting for the next stressor to happen. \n\nI used to be such an easy going very talkatove social person, but now my body takes the fight or flight i used to get in the military from its stressors and has put them alongside my eceryday stressors. I claw and scratch in my head to do the littlest tasks like laundry or dishes. Every time i go to school or work its always the same feeling of absolute fear and dread but when im in the moment i know i am okay but its so hard to act like a normal person infront of people at times. \n\nJody got my wife 2 weeks after i got out of the army. I grew up in a broken home and moved to live with my ex wifes family and i immidiately was on my own as soon as i left the army in a new area ive never lived in. Every friend ive made since then are low quality, i cannot share deep interpersonal thoughts with them. I dont have a mom or a dad to talk to, and my biological family who i met at 18 are not that close with me even after attempts. I am only 23 and i feel like im in a midlife crisis. \n\nThe only thing keeping me going is playing semi pro football. Those dudes are my brothers but I feel like I cannot relate or connect with anyone my age. I live alone, I have had no sucess with women since then and not to toot my own horn but i am more attractive then the vast majority of dudes my age but what i lack is a calm spirit. \n\nEvery word i say, action i do, movement i take, idea i share, its all contradicted in my head. I question myself, my own beliefs, direction and goals in life even though i am very sucessful for my age. I am very greatful for the foundation i have built for myself but i feel i have no skills to break down my walls. Every person who i have ever called my best friend has wronged me in some way and we no linger communicate. I always have my generosity taken advantage of. I dont know wether i am too much of a people pleaser or if i dont give enoigh of myself to other people.\n\nI constantly stumble on my words when im sharing personal thoughts, i truly dont even know if my own emotions are real or fiction made up in my head. I feel like aeverything in my life is stacked togther aimlessly with toothpicks. I feel like an imposter. I am constantly in fear of what would happen to me if an unexpected emergency were to happen in my life. I have no support even from those who say they would support me. \n\nI genuinely do have alot. I drive a really nice car, i have a super nice apartment, i have an amazing job with amazing coworkers, i am in college at my dream school, i have a dog and a cat at home, but i feel like a fraud or an outsider in some way. I cant stop the feeling of being on edge. I feel like at any time someone is going to tell me im wrong or something. Ive tried medications, supplements and the whole kitchen sink and i am seeing mental health at the VA. Tackle football is my only outlet and I know one day it will no longer become an option. \n\nI feel like my own problem are so miniscule but on the inside i know something isnt right and i thought it would go away after the military but my body is still at the same protective and anxious homeostasis it did when i was still in. I dont enjoy most things i used to or thoight i would enjoy after the army. I feel like i had high expectations of my civilian life and two years later i am living fine but i dont feel fine. I dont know if its because i am alone and camnot connect with others anymore or what. I was homeless right before the Army at 17 or 18, and the military significantly amplified the syress i underwent for my entire childhood growing up with foster parents who neglected me. I dont even know the direction of what help im asking for here but i just need some advice. ",
    "flair": "Question/Advice",
    "score": 24,
    "comment_count": 22,
    "created_at": "2026-02-28T03:04:23+00:00",
    "top_comments": [
      {
        "id": "o7tuog4",
        "score": 9,
        "body": "I'm much older, and female, so I suppose I don't really have advice that would probably be helpful. Just wanted you to know I read your story, and I'm here if you want to talk."
      },
      {
        "id": "o7tsf6b",
        "score": 5,
        "body": "Talk to someone. I recommend the program below.  They've helped me tremendously.\n\nhttps://www.uclahealth.org/programs/operationmend"
      },
      {
        "id": "o7xxon2",
        "score": 5,
        "body": "Dude, if you\u2019re 100% and got no kids, I would bounce out of America and go enjoy life for a couple of years"
      },
      {
        "id": "o7u1j6r",
        "score": 4,
        "body": "I went fulltime back to school at 28, three years later I\u2019m currently in research/grad prep and planning a 3 month solo backpacking thing across Europe. \n\nYou gotta live for the small goals and make it to the larger goals every once in awhile. And the goals that you set for yourself should be for you only. Right now, my small goals are just maintaining straight A\u2019s; working towards the summer, and hopefully everything works out."
      },
      {
        "id": "o7u0a8a",
        "score": 3,
        "body": "Faith in myself, faith in a higher power and I have  some good people who remind me to look for the good in life."
      },
      {
        "id": "o7u7rdl",
        "score": 2,
        "body": "I resonate with you on having no one to talk to. Seems like the world moved on without us when we were in. Finding a good therapist will help. You are very young. I have hope you\u2019ll do amazing things and I\u2019m not just saying it.. I\u2019m 33, and would love to go back in time."
      },
      {
        "id": "o7vy8sy",
        "score": 2,
        "body": "Philosophy, specifically stoicism has taught me how to take control of my life.\n\nI recommend checking out How To Be Free, which was a life changing book for my perspective on life and helped me deal with my anxiety etc."
      },
      {
        "id": "o7u8zit",
        "score": 1,
        "body": "Op...what keeps me going is traveling, along with going to church and getting involved with my American legion.  \n\nHave you talked to a chaplain? That's what helps me. That and a 4 week trip to japan."
      },
      {
        "id": "o7une0t",
        "score": 1,
        "body": "1. I believe that things well get better, even in the worst days I know that the day will pass. \n2. And this is the big part for me i learned how to be a kid again. I relearn how to let my self be truly excited over the simple and random things. I basically treated my self like I was a 5 year old and rebuild form there. \n3. Thearpy and lot of it. \n\nI been out longer then I was in and I was in for 10 years lots of deployment time, got blown up got med borded. It wasnt easy and it wasnt fast, but every week I made an effort to be better. I wasn't strong enough to make the effort every day, but direction is more important than speed. And if you just got out you still need to rest and decompress, you dont have to have it all figured out right away."
      },
      {
        "id": "o7v6h7p",
        "score": 1,
        "body": "It sounds like you're lacking humility or you have a skewed image of who you really are either way it sounds like you could greatly benefit from a social worker/therapist who could give you a more accurate assessment of what you really are"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgq8sw",
    "title": "Help me understand how are the MWR tickets discounted.",
    "body": "We are trying to get discounted ticket for universal in Orlando but maybe I missing something but you will pay more using the military discounted ticket than buying it from universal website.",
    "flair": "Discussion",
    "score": 38,
    "comment_count": 34,
    "created_at": "2026-02-28T02:12:04+00:00",
    "top_comments": [
      {
        "id": "o7tw2om",
        "score": 85,
        "body": "I got really curious about this, so I looked it up. The key thing to notice in the price at universal is \"price and availability may vary by date\" They do flex pricing, so the price changes to be cheaper in the off / slow season to crazy expensive in high / busy seasons. \n\nThe MWR discount / agreement is to sell them for a fixed price. So that price you see is what they will always be.\n\nSo MWR is of more value in high season when Universal tickets can be as much as $235 ,but if youre going in low season would be better to buy directly from Universal cause it can get as low as $120."
      },
      {
        "id": "o7u4eun",
        "score": 66,
        "body": "I dont know what to tell you... you asked for help understanding, I tried to gave you info for how it works to clarify whats going on here. How you feel it should work instead isn't really anything I can speak on."
      },
      {
        "id": "o7v2yl2",
        "score": 34,
        "body": "There\u2019s no pleasing people like you. Be grateful there\u2019s any discount at all"
      },
      {
        "id": "o7ufofv",
        "score": 32,
        "body": "When you buy the Universal studios tickets through MWR it is a season ticket ! Wife and I did not know this. We bought them and went in March of last year and then went back down to Florida in September to go to Disney. We then learned that our Universal tickets were good for the whole year as a season pass ! So we went over to Universal again for free for 2 days. Now some dates they can\u2019t be used like major holidays but still a season pass for 200 bucks can not be beat. When I retire in 10 years and move to Florida we will be there at least 1-2 a month lol."
      },
      {
        "id": "o7v1b4c",
        "score": 22,
        "body": "Dude, that pass is good for a whole year\u2026 and for that price, that\u2019s awesome. \n\nSource: look at the date on the bottom of your second picture."
      },
      {
        "id": "o7u7qj1",
        "score": 15,
        "body": "NFL, NBA, MLB, MLS, NHL, Disney, Ticketmaster, Everyone is doing it. Flex Pricing. Dynamic Pricing. It\u2019s all Bullshit."
      },
      {
        "id": "o7uin5b",
        "score": 11,
        "body": "\ud83d\udc46 100%"
      },
      {
        "id": "o7ujupr",
        "score": 9,
        "body": "Clearly you\u2019re saving $3."
      },
      {
        "id": "o7ujh78",
        "score": 8,
        "body": "We went through shades of green and it was actually a season pass!\n\nNotice on the bottom it says expires DEC 2026. Its good for the whole year."
      },
      {
        "id": "o7vrnw6",
        "score": 7,
        "body": "Eligible veterans. So usually if you're 100%"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgowar",
    "title": "Did yall get this email too",
    "body": "",
    "flair": "Question/Advice",
    "score": 133,
    "comment_count": 116,
    "created_at": "2026-02-28T01:09:55+00:00",
    "top_comments": [
      {
        "id": "o7tgh9r",
        "score": 27,
        "body": "[removed]"
      },
      {
        "id": "o7t1lcd",
        "score": 12,
        "body": "https://benefits.va.gov/GIBILL/rudisill.asp"
      },
      {
        "id": "o7t85zc",
        "score": 10,
        "body": "Knowledge leaks outward, I see a comment about expired benefits. There\u2019s sometimes a solution"
      },
      {
        "id": "o7u80ug",
        "score": 9,
        "body": "It's determined by periods of service. If you qualified for post 9/11 *and* MGIB, *and* have two or more qualifying periods of service (i.e. reenlisted) you get twelve months of education benefits tacked on to your 36 months\n\n\nThe new decision sounds like they're removing the requirement for re-enlisting to get both actually, and now it's based on some other factors. That being said, if you did reenlist you are very likely eligible depending on service period."
      },
      {
        "id": "o7t5792",
        "score": 9,
        "body": "Anyone who is on the mass mailing list received this email, whether eligible or not. My Post 9/11 GI Bill expired in 2019."
      },
      {
        "id": "o7u0wuu",
        "score": 9,
        "body": "personally I had never heard this, so sharing it helps regardless. I'm sure I'm not the only one."
      },
      {
        "id": "o7tb140",
        "score": 8,
        "body": "Yep. I was originally told 100% requalified me, then that it didn\u2019t. I assume this has something to do with that"
      },
      {
        "id": "o7tx598",
        "score": 8,
        "body": "What if you used all of your post 9/11 and got the $1200 MGIB refund?"
      },
      {
        "id": "o7wf49t",
        "score": 8,
        "body": "I Haven\u2019t figured out all new rules on this yet."
      },
      {
        "id": "o7t5mfo",
        "score": 8,
        "body": "Just an fyi, you can have it extended if something service connected or Health prevented you from using them. Had mine extended 6 years"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgmgww",
    "title": "Therapist just canceled appointment for 2 weeks in a row. No new appointment for a month.",
    "body": "Feeling defeated beyond belief right now. I started working with this therapist about a month ago because I was really struggling. I gave up my community care availability because the VA said they could expedite getting a therapist for me. Now I\u2019m basically going a month+ without seeing anyone when I really need it. What should I do? If I ask for community care again I feel I\u2019m going to have to start the waiting process all over again? Can\u2019t exactly afford just going off and finding civilian therapists on my own either. Any thoughts or advice? ",
    "flair": "Question/Advice",
    "score": 9,
    "comment_count": 11,
    "created_at": "2026-02-27T23:26:07+00:00",
    "top_comments": [
      {
        "id": "o7sph5u",
        "score": 8,
        "body": "Try your nearest Vet Center."
      },
      {
        "id": "o7shz66",
        "score": 3,
        "body": "You can ask for a different provider within the VA. It may be faster. You may be able to secure message the provider and ask them if you asked for a CC referral will it be a new one or can you use the old referral. I find that secure messaging is a great tool to communicate with. You usually get answers pretty quickly from providers or their nurses."
      },
      {
        "id": "o7vnbai",
        "score": 3,
        "body": "Can\u2019t recommend this enough. Vet Centers are the VAs best kept secret. I credit their therapists with saving my life."
      },
      {
        "id": "o7srhg8",
        "score": 2,
        "body": "Send your provider a message and let them know you'd like a replacement appointment. You might have to be seen outside your normal day/time and shift your other work/life stuff around. But it would be worth it."
      },
      {
        "id": "o7tugpu",
        "score": 2,
        "body": "I feel for you! I am struggling with something similar. Following along for useful suggestions."
      },
      {
        "id": "o7sk6ma",
        "score": 2,
        "body": "The whole reason I was going community care was because all the other therapists at my VA were scheduled out till May. So I could get another one but then it won\u2019t be for even longer at this point because they said they booked out till May at the beginning of January."
      },
      {
        "id": "o7slgry",
        "score": 2,
        "body": "I would still message them and tell them you need to be seen and soon. If they give you any issues go to the patient advocate, they can get things done in a pretty quick manner usually."
      },
      {
        "id": "o7slomv",
        "score": 2,
        "body": "Gotcha thank you for the information I will do that then and follow up with PA if I need to thanks."
      },
      {
        "id": "o7sgnma",
        "score": 1,
        "body": "I use this platform be get therapeutic advice. I also have a VA therapist. Please, don't take everything on this platform literally - use it as a place to vent or even listen. I highly doubt everyone on this platform has good intentions."
      },
      {
        "id": "o82jfgx",
        "score": 1,
        "body": "Veteran's white house hotline \ud83e\udd37"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rglvlk",
    "title": "How do I get my VA to send me for dual diagnosis rehab",
    "body": "TLDR;\n\nI have asked my local VA for help to send me to a specific rehab that I have attended before when a seperate VA facility sent me there. I provided my new VA all the information they needed to create the consult, and to contact admissions, with the rehab. I told everyone that the rehab wants me asap and all I need is that consult, but my local VA is stonewalling me. After much argument and begging the VA said still denied me. I need help knowing who to contact to create the consult I want. My local VA is in VISN 17 the South Texas Veterans Healthcare System, San Antonio\n\nMore context -\n\nDesperate on my own to get help, I gave up trying for what I knew is the best choice for me, and accepted their demand to get 72 hour detox so they can place me. They only offered one local option which is a substance use domicillary. After I declined they said they had one other offer that is also a domicillary but dual diagnosis. I felt forced to say yes, so day 1 of my detox they told me they had a bed for me, a consult was placed, and travel will be arranged. I never got anymore answers to my requests for more information, and desperately was trying cement the plans before they discharged me. Today they discharged me back home with all the hope of \"someone will call you\" and \"expect the day you were told you were leaving to change\". I need help knowing who to contact to create the consult I want and not be forced to accept the kind of \"help\" this VA says is the \"only help available\"",
    "flair": "Question/Advice",
    "score": 1,
    "comment_count": 10,
    "created_at": "2026-02-27T23:02:01+00:00",
    "top_comments": [
      {
        "id": "o7sege8",
        "score": 1,
        "body": "this is rough \ud83d\udc80\n\n  \ncontact patient advocate asap"
      },
      {
        "id": "o7sehgh",
        "score": 1,
        "body": "Try r/VeteransBenefits"
      },
      {
        "id": "o7si94a",
        "score": 1,
        "body": "I just wanted to add for context I'm 100% P&T for PTSD with major depression and substance use (alcohol) disorder as secondary to the PTSD. I promise I'm not just some disgruntled veteran complaining as a victim of every situation that angers me. I have more often than not sang the praises of the VA for the last 8 years, because despite all the red tape and appointment time waits, I truly have been helped in the past. That's why I am so upset at experiencing the complete opposite at this VA. I just moved here under 2 years ago and it's blown my mind that such a gap of difference of care exists.\n\n*post edited to fix my grammar*"
      },
      {
        "id": "o7syfkf",
        "score": 1,
        "body": "Talk to social workers."
      },
      {
        "id": "o7sh2ul",
        "score": 1,
        "body": "I can't contact them asap. Nobody answers the phone, and no voicemail is setup. Instead they refer you to the \"ask va\" section on the va.gov main website. Then you have to wait for somebody to reach out to you. I've tried to contact patient advocate back in december for a different reason 2 months ago. After a few days I got a VA secure message back from a local patient advocate asking me to explain the situation, so I did. After a few more days I received another secure message from the same patient advocate saying they had forwarded all of the details to \"Primary Care Administration\", that I'd be contacted at least 3 times if I don't answer their call, and at least 1 voicemail with contact info will be provided. I never was contacted, no voicemails provided. With my own personal mental health and substance issues going on, I never followed up on them never contacting me back.\n\n*post edited to add a little better clarification*"
      },
      {
        "id": "o7sfh1s",
        "score": 1,
        "body": "dang just tried to crosspost this to that veteransbenefits and got a notice that the type of message/message content isn't allowed. It blocked my ability to post it"
      },
      {
        "id": "o7u2nvh",
        "score": 1,
        "body": "I'm not knocking you for such a simple answer so forgive my tone of text here, but I absolutely have talked to them and I wouldn't be posting to reddit if they had provided any sort of help in the least."
      },
      {
        "id": "o7skion",
        "score": 1,
        "body": "Don't cross post"
      },
      {
        "id": "o7u7jmc",
        "score": 1,
        "body": "Ya my reply was a bit lazy. I\u2019ve been to several rehabs via the VA. I\u2019ve done several stints Palo Alto VA which is an onsite rehab on the VA campus. Access to all the doctors and from Stanford. I\u2019m sober now for almost 7 months and my life is better than it has been in a long, long time. I met a Ranger in rehab why\u2019s was strongly advocating to be moved to a specific place that apparently focused on PTSD. I get the sense that the VA doesn\u2019t like \u201cshopping\u201d for certain rehabs or dual diagnosis places. They are slowing getting more strict and want to prevent vets from just making a life long habit of staying at rehabs. But you and I are the real deal and deserve to get the best help available. Maybe try to get sent to VA Palo Alto in California. Tons of doctors. PTSD treatment. \nHope this was a better answer."
      },
      {
        "id": "o7uarl9",
        "score": 1,
        "body": "Wonderful answer and I appreciate you taking the time to clarify. In my old VA I was offered palo alto as an option but I declined because doing PTSD work with a majority of vets whose PTSD is understandby from their experiences in war. I deployed twice and what little I experienced I already knew wasn't part of my PTSD amd I have never ever claimed it as such. My PTSD is diagnosed from grooming by an SNCO leading to sexual assault leading to rape as a junior enlisted who would have made NCO, but I broke down all around before that became a reality. Things kept getting worse until I received my discharge, honorably. Male Sexual Trauma subsect of PTSD much harder for males to talk about, and much, MUCH harder to find professional help for. I declined palo alto because \"comparatively\" it isn't the same. The symptoms of the PTSD are all the same nonetheless, but ask your average bystander whats worse - I experienced war or I experienced sexual assault. I'm no fool - male on male rape is as looked down upon as the average soldier assuming sexual assault claims are just regrets, and pregnancy is to get out of deployments \ud83d\ude44 Either way I feel too \"less than\" to my fellow veterans experiencing their own war to share a group room with them and say my deployments were okay but holy shit did this SA fuck me up. I'm not saykng it's fair I'm just not naive enough to disregard the culture"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgkp8w",
    "title": "Alabama military veterans eligible for special teaching certificates under newly passed bill",
    "body": "\nIf you know a veteran who wants to get into teaching, please share.\n\nhttps://www.al.com/news/2026/02/alabama-military-veterans-eligible-for-special-teaching-certificates-under-newly-passed-bill.html",
    "flair": "Article/News",
    "score": 54,
    "comment_count": 28,
    "created_at": "2026-02-27T22:15:11+00:00",
    "top_comments": [
      {
        "id": "o7tjoj0",
        "score": 55,
        "body": "Being a veteran is not an across-the-board license to do everything."
      },
      {
        "id": "o7szdu1",
        "score": 45,
        "body": "Thats one sentence with a lot of dumb ideas. "
      },
      {
        "id": "o7w5ssw",
        "score": 37,
        "body": "As a veteran, most of the other veterans I know shouldn\u2019t be allowed to teach their own kids, let alone someone else\u2019s."
      },
      {
        "id": "o7u23gd",
        "score": 21,
        "body": "So an Associate's degree, or round abouts at least depending on the specific credits. That still ain't much learnin' to then be going out and edumacatin' the yungins."
      },
      {
        "id": "o7tqfk9",
        "score": 17,
        "body": "To qualify, veterans would have to serve four years on active duty and have at least 60 hours of college credit with a GPA of at least 2.5 on a 4.0 scale.\n\nThey would have to clear a criminal history background check, be recommended for certification by a local superintendent or private school administrator, and have other credentials.\n\nThe superintendent would assign a mentor for the veteran for at least two years.\n\nThe certificate would be valid for five years.\n\nThey are not just saying, Oh, you served, here is your classroom.  "
      },
      {
        "id": "o7yeqnb",
        "score": 10,
        "body": "[removed]"
      },
      {
        "id": "o7ujkmm",
        "score": 10,
        "body": "Saying an imperfect system needs fixing is different from saying an imperfect system should include very specific changes. Any action is not always better than inaction, and no one is arguing for inaction."
      },
      {
        "id": "o7vrokz",
        "score": 8,
        "body": "No. 60 hours is an associate degree. 120 hours is a bachelor degree."
      },
      {
        "id": "o7v3e05",
        "score": 8,
        "body": "Where do you think these mentors will be coming from? The same state that is traditionally ranked at or near the bottom? \n\nThe blind leading the blind is what you will get. We want our students to have better education, but this ain't it chief."
      },
      {
        "id": "o7w252v",
        "score": 8,
        "body": "In this case, \u201ctrying something new\u201d is lowering the standards for teacher certification. If the status quo is unacceptable, lowering standards seems counterproductive."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgjtm4",
    "title": "Question on Military Honors at a funeral",
    "body": "My dad (retired 23 year Navy veteran) just recently passed and our family decided to get the beautiful commemorative Urn from the VA, as my dad was cremated and wished for his ashes to eventually be scattered. The funeral home we are using told us because we got the urn from the VA he can no longer have military honors at the small funeral we are doing at our local church. Online it said he should still be eligible but I really couldn\u2019t find direction on how to move forward and was hoping if anyone had any insight or information. Thank you! ",
    "flair": "Question/Advice",
    "score": 31,
    "comment_count": 17,
    "created_at": "2026-02-27T21:41:12+00:00",
    "top_comments": [
      {
        "id": "o7s3tb6",
        "score": 19,
        "body": "Every honorable discharge is obligated to military hours.  If you don\u2019t do grace side, then you might not get the 21 salute.  But which ever branch he was part of will come and do taps and flag folding."
      },
      {
        "id": "o7sbtb8",
        "score": 19,
        "body": "I'm KY's VFW State Senior Vice Commander, and literally just came from a funeral for one of our past state commanders. He was cremated and still received not only VFW honors, but military honors as well. The funeral is just being lazy and not wanting to do the leg work. Contact your local Veteran Service Organization (VFW, DAV, AMVETS, or American Legion). If that doesn't produce the right answer, holler at me and I'll see what I can do about getting your dad his well deserved honors."
      },
      {
        "id": "o7s4x5e",
        "score": 12,
        "body": "I think the Funeral home is confused. \n\n\n\nMy Uncle was a longtime Navy veteran. He was cremated and buried in the family's church. He was given full honors. \n\n# Urns and Plaques\n\nThe urn and plaque are two memorial items that commemorate a Veteran whose cremated remains have not been interred. A commemorative urn is used to hold the remains of a cremated Veteran and a commemorative plaque is designed to hang on a wall. Claimants may request either the urn or the plaque to honor the Veteran's service according to their preference.\n\nIt's important to note that if a family chooses an urn or a plaque to commemorate a Veteran, VA is prohibited by law from interring that Veteran's remains in a VA national cemetery or from providing a headstone, marker or medallion for placement in any cemetery. Families should be certain of their choice. If the family chooses to receive an urn or a plaque to commemorate their Veteran, their decision cannot be undone. The law does not provide a method to restore these benefits."
      },
      {
        "id": "o7s6cyb",
        "score": 12,
        "body": "Is the funeral home upset because they couldn't cash in? Not sure ho the two are even connected."
      },
      {
        "id": "o7s30l0",
        "score": 8,
        "body": "[EDITED to add info]\nI never heard of this before. Sounds like BS to me. Contact your local reserve unit or military base to request a military honors detail. If they don't have a real bugler, you can request  1 from 1 of many nonprofits.\n\nIF the military detail does  NOT have a real bugler, please have a real volunteer bugler with a real bugle perform Taps at his burial.  Contact Buglers Across America. They'll need a copy of his DD214."
      },
      {
        "id": "o7u5kko",
        "score": 7,
        "body": "Probably *very* upset. Know that funeral sales-weasels lie at the drop of a hat. *Any* hat. I could drop my hat right now, and a funeral home would have to call someone.\n\nOffer to use another funeral home, see how fast that changes."
      },
      {
        "id": "o7s64bv",
        "score": 6,
        "body": "contact or go to a local vfw or american legion to get some info.\n\nmy dad was in the VFW in his area and I spoke with them to give a gun salute and flag.\u00a0\n\nthe fellows from the VFW came but was one guy short for the gun salute, since I was a veteran they allowed me to fill in. It was a nice way to send my dad off."
      },
      {
        "id": "o7s543a",
        "score": 5,
        "body": "My husband died 7 years ago and retired from the army after 32 years and he was also cremated the Army sent a full honor guard complete with 21 gun salute to honor his service there was no graveside service so I would think your father would qualify for military honors at any funeral home/church"
      },
      {
        "id": "o7tfk6x",
        "score": 4,
        "body": "Three-volley salute, not 21 gun salute."
      },
      {
        "id": "o7s328o",
        "score": 3,
        "body": "I don't know the definitive answer, someone will respond that does. \n\nI really don't see what one has to do with the other though."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgjn29",
    "title": "Save your money if you can",
    "body": "Hey guys uh just save your money this year. Enjoy life ",
    "flair": "Discussion",
    "score": 129,
    "comment_count": 80,
    "created_at": "2026-02-27T21:34:12+00:00",
    "top_comments": [
      {
        "id": "o7rxy5z",
        "score": 132,
        "body": "Jokes on you im already broke."
      },
      {
        "id": "o7s3hk4",
        "score": 46,
        "body": "Tell me you haven\u2019t been obliterated in a child custody battle without telling me you\u2019ve haven\u2019t been obliterated in a child custody battle."
      },
      {
        "id": "o7s0l34",
        "score": 44,
        "body": "I wish you would have told me before I bought enough booze to put down a bull elephant, a high-interest auto loan for a car I cannot afford, and a bunch of jewelry for the girl I just met and got pregnant."
      },
      {
        "id": "o7rxd01",
        "score": 29,
        "body": "I'm buying ammo"
      },
      {
        "id": "o7scks6",
        "score": 29,
        "body": "No kids, I\u2019ll never be trapped in the depths of hell"
      },
      {
        "id": "o7td0e9",
        "score": 28,
        "body": "Remember, free fish are all you can eat at Petco if you can outrun the employees \ud83e\uddd0"
      },
      {
        "id": "o7sclgl",
        "score": 16,
        "body": "Like save more than usual or was there another catastrophe?"
      },
      {
        "id": "o7s2o62",
        "score": 15,
        "body": "Atleast we are in the same boat"
      },
      {
        "id": "o7s2rld",
        "score": 14,
        "body": "Sir, you're looking for the r/bootenant sub"
      },
      {
        "id": "o7syf47",
        "score": 12,
        "body": "Kinda hard to save money when you have 4 ~~little snots~~ beautiful kids ~~sucking the life out of me~~ that constantly need something.  I love them though.  I do try to put something away though, it's always smart to try to save something."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgj9jm",
    "title": "Hard to hold a job any advice",
    "body": "I\u2019m 27 years old, I was an infantryman in the army. Ever since I got out of the military in 2024 for my disabilities. I\u2019m 70% veteran. I haven\u2019t been able to hold on to a job for long. I get bored so freaking easily it sucks. I was in car sales and left after the adrenaline from that wore off. Now I\u2019m in life insurance sales and I want to literally rip my skin off I\u2019m so freaking bored. I literally work a job for a couple months then I end up quitting either do to boredom, bad management, or just falling into a depression then never showing up again.I just don\u2019t know what to do for work or what to do. What field should I look into or what should I do?",
    "flair": "Question/Advice",
    "score": 26,
    "comment_count": 61,
    "created_at": "2026-02-27T21:19:42+00:00",
    "top_comments": [
      {
        "id": "o7rxnva",
        "score": 33,
        "body": "EMT here, highly recommend this career field for veterans. Driving through the city with lights and sirens at 2 am with an energy drink, just to push some narcan to a hobo never gets old\u00a0"
      },
      {
        "id": "o7rx4hq",
        "score": 14,
        "body": "Public safety dispatcher?\n\nInvestigator of some kind, like insurance/fraud? Or even a federal background investigator?\n\nOr a trade job, if your disabilities will allow that. I'm looking at that for the variety, which I suspect is part of what you're looking for. Think like HVAC repair."
      },
      {
        "id": "o7ruzre",
        "score": 11,
        "body": "EMT? EMS dispatcher?"
      },
      {
        "id": "o7sdhhj",
        "score": 7,
        "body": "Not sure how broken you are but if money isn't an issue try your hands at being a barista.\n\nIf it actually paid a meaningful salary I'd still be a barista. Highly rewarding, high paced, and I genuinely enjoyed my time doing it. Was very healing for my soul.\n\nIt was weird being the only heterosexual, male, conservative there but I got used to it pretty quick."
      },
      {
        "id": "o7rsgvx",
        "score": 6,
        "body": "Well can\u2019t do LEO (depend on what disabilities you have) and can\u2019t go back to military (not worth it). Seems like you want some action."
      },
      {
        "id": "o7ryqae",
        "score": 6,
        "body": "Government contracts! I did anti terrorism force protection"
      },
      {
        "id": "o7si6ub",
        "score": 6,
        "body": "Veteran here, was a firefighter/paramedic civilian side for about 6 years. It\u2019s a great career, every day is different. If you have a great crew it\u2019s like getting paid to workout, hang out with your best friends, do some really cool training, and you get to do things you\u2019d never think of. Just find a solid department that is part of the IAFF for better pay, schedules (many are trying to go 24/72 which is amazing.!) \n\nSome departments academies are even certified so if you have your GI Bill they\u2019ll pay you BAH while you\u2019re most likely getting paid for the FD as well. Fire academies can go from 3-6 months so you can definitely pocket some savings if you find one that is certified by the VA. (But not required by no means.)\n\nIf you want an adrenaline rush and to find camaraderie you had in the military, I\u2019d highly recommend it. I started volunteering at a FD while I did EMT school using my post 9/11 and absolutely loved it."
      },
      {
        "id": "o7to7c4",
        "score": 6,
        "body": "I ended up becoming a male nurse. It\u2019s definitely interesting both from the patients and coworkers who are 95% female and that has both pluses and minuses to it. A big plus is you can work directly with fellow veterans if you want and a bunch of different areas and age ranges of people. You can also move most places and have a good paying job and if you work 12 hour shifts you can get a nice work life balance"
      },
      {
        "id": "o7s81vx",
        "score": 6,
        "body": "You can have all of that and do LEO. Don\u2019t let these idiots tell you what you can\u2019t do"
      },
      {
        "id": "o7suvvl",
        "score": 5,
        "body": "I get bored easily too. Started working with elementary school kids recently and rarely get bored. Especially if I\u2019m filling a spot in a special ed class. Kids with severe hyperactivity and/or autism will keep you on your toes. Another positive is that there isn\u2019t much in schools to trigger ptsd or anxiety. \n\nWorked in telecom for about 15 years and rarely got bored doing that, but it really breaks your body down. Unfortunately, I spent much of that time triggered from having to go into people\u2019s homes, or just entering their property. \n\nSomething to think about though\u2026 maybe some of your boredom is due to depression and not necessarily the job? I sometimes get \u201cbored\u201d when it\u2019s really my depression causing lack of motivation and desire to do anything. \n\nGood luck."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rggku1",
    "title": "Camp Lejeune Army basic training 1981",
    "body": "We have sent for paperwork but it\u2019s taking forever. Has anyone in this group had experience with completing Basic at Camp Lejeune in 1981?",
    "flair": "Question/Advice",
    "score": 0,
    "comment_count": 17,
    "created_at": "2026-02-27T19:37:12+00:00",
    "top_comments": [
      {
        "id": "o7r8z1z",
        "score": 29,
        "body": "Lejeune is Marines and Marines do boot at Parris Island or San Diego, unless I'm wildly mistaken."
      },
      {
        "id": "o7rij86",
        "score": 27,
        "body": "The Army doesn't do basic training at camp lejune, so I bet thats the first reason its taking so long"
      },
      {
        "id": "o7rpz1g",
        "score": 10,
        "body": "Not sure if you've heard, but staffing is a bit wonky in the federal government atm.\n\nAlso, you requested this during Ramadont (period between USMC birthday and the end of January where no one does shit because of the back to back holidays and block leave periods), so I'd give it another month or so before I start making phone calls to ask what the hold up is. \n\n\nThat being said, the only boot camp that I'm aware of ever happening at Camp LejeuRne is Camp Johnson for the first Black Marines prior to integration. Fun fact, those barracks are still in use, and I'm pretty sure they've done no modernization to them since first constructed. Ask me how I know"
      },
      {
        "id": "o7rjmio",
        "score": 9,
        "body": "The closest I can think of for Army would be Fort Jackson, SC.   Just a thought."
      },
      {
        "id": "o7rj4vf",
        "score": 7,
        "body": "Does he have or can you locate his DD-214 form? \n  May I ask how are where you requesting this information? \n  Research form\nSF-180 to obtain a DD-214. It took about 3 weeks and mine was mailed to me."
      },
      {
        "id": "o7rewux",
        "score": 5,
        "body": "What type of paperwork are you requesting ?"
      },
      {
        "id": "o7sgjtq",
        "score": 5,
        "body": "It\u2019s more likely that as Army he may have participated in some unit level training event at Lejeune after he completed Army basic training elsewhere.  For instance, his Army unit may have used Marine ranges or like resources, or participated in a joint training event/exercise.  If that\u2019s the case Lejeune will not have any info on your husband.  \n\nIf he attended a formal USMC TECOM school or training at Lejeune, TECOM may have the records but not Camp Lejeune.  Army TRADOC recognizes TECOM credit so look for such evidence through Army channels."
      },
      {
        "id": "o7sqgej",
        "score": 5,
        "body": "He could have trained there for some reason. But that is not gonna show on a 214."
      },
      {
        "id": "o7s7ic2",
        "score": 3,
        "body": "Was he in the Army or a Marine?"
      },
      {
        "id": "o7tk4r7",
        "score": 3,
        "body": "Camp Lejeune is Marines. It\u2019s never been with the Army."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rgd7cp",
    "title": "I need advice on picking a career",
    "body": "I was med retired in 2024 from the army. I joined the military at 18 to get away from home and travel so I didn\u2019t care about my job (wasn\u2019t thinking about the future). I ended up choosing 92F which is a fueler, but I don\u2019t want to drive trucks or work with fuel. I retired as an E5 at 22 and am now 24, anything manual labor is off the table. \n\nI have a business management bachelors but that hasn\u2019t really helped in either supply chain jobs or logistics. Everything that will hire me is warehouse work. I have a few tech certs and am in interested in the field but entry level tech is like wiping your ass with a brick right now. \n\nI want to hear opinions or ideas on what anyone here would do or have done in this situation. Luckily I\u2019m young enough to start over but I have no specific career interest I just want to make money so it makes me open to all career paths except sales which is good and bad. \n\nAlmost forgot should I get a second bachelors in whatever field I choose?",
    "flair": "Question/Advice",
    "score": 7,
    "comment_count": 40,
    "created_at": "2026-02-27T17:33:23+00:00",
    "top_comments": [
      {
        "id": "o7qwmt2",
        "score": 10,
        "body": "Accounting. You can work from home or for any size firm. IMO cybersecurity is over saturated and some of the core business functions are being overlooked, plus the pay is pretty nice the higher you get."
      },
      {
        "id": "o7rhhxl",
        "score": 4,
        "body": "You need to seriously look into Vocational Rehabilitation (Chapter 31) [https://www.va.gov/careers-employment/vocational-rehabilitation/](https://www.va.gov/careers-employment/vocational-rehabilitation/)"
      },
      {
        "id": "o7qr877",
        "score": 4,
        "body": "Use your VA benefits to the max, aim for a cleared role if you can, and look at non warehouse ops like procurement, contract specialist, project coordinator, compliance, or QA, lean on USAJOBS, SkillBridge style internships even post service via DOD SkillBridge like programs with vets groups, network with alumni and LinkedIn recruiters, consider a short targeted program like cybersecurity GRC or SecOps over a second bachelors, and if you want remote admin type work while you figure it out, I\u2019ve seen some decent leads trickle in from wfh\u200bal\u200bert."
      },
      {
        "id": "o7qs3ml",
        "score": 4,
        "body": "starting over in any job role with no work history is gonna be wiping your ass with a brick.\u00a0\nif you\u2019re wanting to find a job thats not labor intensive, there are some entry level supply chain analyst, warehouse auditors, or buyer jobs.\nsupply chain is super broad and as broad as your degree is you could stay gainfully employed. the one good thing is you can hop job roles in the industry, just dont let that brick drag ya down.\n"
      },
      {
        "id": "o7r86yc",
        "score": 4,
        "body": "A CPA is not a requirement to be an accountant.\n\nI am a CPA and I worked a long time in the private sector. I left private for the stability of the government.  I make a good living and there are people here making 6 figures without their CPA license\n\nHOWEVER, AI is here and is removing the need for lower level accountants."
      },
      {
        "id": "o7r6uqs",
        "score": 3,
        "body": "I can\u2019t find the thread but there is a website that only hires remote accountants and it\u2019s a legit company.  \n\nIf anybody remembers the website, please post it. They are a third party company that companies use to outsource basic shit"
      },
      {
        "id": "o7sl71b",
        "score": 3,
        "body": "lol thank you. Here\u2019s your tea \ud83e\uddcb"
      },
      {
        "id": "o7rdi34",
        "score": 3,
        "body": "You don\u2019t have to be a CPA. I do book keeping (I did it through quickbooks and it took 2 weeks for the quickbooks certification and that pays $22-30/hr) then got bookkeeping at my local community college and I\u2019m working on my tax preparation certification at the college now too. Building a small business and I networked with CPAs and I feed them clients and get a finders fee there too. \n\nAccounting is broad. I have a classmate who only does payroll accounting, she doesn\u2019t have an associates and makes $38/hr. It\u2019s steady and follows banking hours and because no one understands it, they leave us alone."
      },
      {
        "id": "o7quoxu",
        "score": 2,
        "body": "I am in somewhat of a similar situation. I have been looking at entry level jobs for the airlines simply for the flight benefits, but have not really had any luck in my area. Then again, I'm not sure if the flight benefits are worth it or not but have not figured that one out yet"
      },
      {
        "id": "o7r4wqc",
        "score": 2,
        "body": "Have you looked at project management? I\u2019ve found my need to complete the mission often without enough time or resources aligns with my time in the Navy"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rg8sqi",
    "title": "GI Bill not covering tuition",
    "body": "Has anyone experienced the gi bill not covering their full tuition or consistently owing money at the end of the semesters because it wasn't fully paid. I got to a very affordable school that isn't expensive in the slightest and some how i consistently owe money at the end of the semester. This sometimes effects my registration status. I'm wondering if anyone has experienced the same, and if you have potential solutions Please and Thank you. -Semper Fi",
    "flair": "Question/Advice",
    "score": 9,
    "comment_count": 10,
    "created_at": "2026-02-27T14:53:38+00:00",
    "top_comments": [
      {
        "id": "o7poeex",
        "score": 14,
        "body": "Step one - talk to the school\u2019s veterans office about this - that\u2019s who reports how much VA has to pay the school."
      },
      {
        "id": "o7q80ca",
        "score": 5,
        "body": "GIBILL has yearly tuition caps. What school do you go to?"
      },
      {
        "id": "o7qi05r",
        "score": 5,
        "body": "Only at private schools. There are no caps at public schools."
      },
      {
        "id": "o7qi6t0",
        "score": 4,
        "body": "Post 9/11 GI Bill pays all authorized tuition and fees at public schools. Only private schools have a Cap on the annual amount of tuition/fees VA can pay."
      },
      {
        "id": "o7q9l9v",
        "score": 2,
        "body": "If they aren't a Yellow Ribbon school, then the GI Bill only covers up to a certain amount."
      },
      {
        "id": "o7pozlr",
        "score": 2,
        "body": "So in my case I went to a state associated school instead of a state school so I always had like 2k remaining balance after each semester. Talk to the veterans office at your school about this and see if you\u2019re leaving any money on the table elsewhere maybe from fasfa grants or anything!"
      },
      {
        "id": "o7pjxg6",
        "score": 1,
        "body": "'Have you looked in the **[Wiki]( https://www.reddit.com/r/Veterans/wiki/education)** for an answer? We have a lot of information posted there. \n\nTo contact VA Education, 1-888-442-4551, for ~~Voc Rehab~~ VR&E (Veteran Readiness and Employment Program) assistance with appointments or problems with your Case Manager (not for missing payments): 1-202-461-9600. \n\n**Payments for certain education benefits (DEA, VEAP) are paid at the end of the month you attend school - Department of Treasury issues these payments **using a 10 business day window** - these payments are not locked into a specific day of the month like VA disability/military pay is**. For Voc Rehab missing payments, contact your Case Manager or your local **[VA Regional Office](https://www.knowva.ebenefits.va.gov/system/templates/selfservice/va_ssnew/help/customer/locale/en-US/portal/554400000001018/content/554400000260849/VRE-Officers-and-Contact-Information)\n\nFor Post 9/11 GI Bill only, If you signed up for direct deposit when you applied for education benefits, **we\u2019ll deposit your payment into your bank account 7 to 10 business days after you verify your school enrollment.** This is the fastest way to receive your payment. [Text Verification FAQ](https://benefits.va.gov/GIBILL/docs/IsaksonRoe/EnrollmentVerificationFAQs.pdf)\n\nMGIB and MGIB-SR and DEA CH 35 have to do [monthly verification](https://www.va.gov/education/verify-school-enrollment/) and you should receive the payment within 3 to 5 business days.\n\nFor Online Only training, the Post 9/11 GI Bill is currently **(1 August 2025) paying $1169.00** for those who started using their Post 9/11 GI Bill on/after 1 January 2018 - this is based on 1/2 of the National Average BAH paid to an E5 with dependents. Post 9/11 GI Bill MHA rates are adjusted 1 August of each year and are based on the 1 January DoD BAH rates for that year - **so VA can't use 1 January 2025 BAH rates until 1 August 2025** - for those who started training on/after 1 January 2018, the MHA rates are 95% of the DoD BAH rates. First possible payment for the 1 August 2025 increase is 1 September.\n\nFor VR&E, there are two different Subsistence Allowance programs - https://www.benefits.va.gov/vocrehab/subsistence_allowance_rates.asp The P9/11 Subsistence Allowance is based on the BAH paid to an E5 with dependents. Those who started using VR&E on/after 1 January 2018 receive 95% of the BAH paid to an E5 with dependents. **As of 1 January 2026 Online only students using VR&E are being paid $1198.00** if they started using VR&E on/after 1 January 2018. The CH31 Subsistence Allowance rates are adjusted 1 October each year by Congress.\n\nVA Education is going paperless - make sure VA has a current email address for you. Please make sure you add Veteransbenefits@messages.va.gov to your contacts list so that you don't miss important updates from VA.\n\n[VA Award Letter explanation](https://benefits.va.gov/gibill/understandingyourawardletter.asp)\n\n[Contact a VR&E Supervisor](https://www.knowva.ebenefits.va.gov/system/templates/selfservice/va_ssnew/help/customer/locale/en-US/portal/554400000001018/content/554400000260849/VRE-Officers-and-Contact-Information)\n\n [VA Rudisill Decision](https://benefits.va.gov/gibill/rudisill.asp) - some veterans may qualify for an additional 12 months of a second GI Bill based on serving two or more different periods of active duty service.\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Veterans) if you have any questions or concerns.*"
      },
      {
        "id": "o825p70",
        "score": 1,
        "body": "What state are you in? Did you work with the student veterans office in financial aid? Have you checked for scholarships or yellow ribbon? Pell grants?"
      },
      {
        "id": "o7rg6dk",
        "score": 0,
        "body": "Apply for pel grant (if you are eligible) to cover the gap"
      },
      {
        "id": "o7tcalc",
        "score": 0,
        "body": "How many credit hours you taking"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rg28fm",
    "title": "I Can\u2019t Sleep, Advice?",
    "body": "It\u2019s been a few months since I got out. First 1-2 months I slept okay but since then my sleep schedule has become non existent. Currently going to college at around 10. Get home workout (trying to not let my body go). But ever since then I CANT SLEEP. I\u2019ve gone days were I stare at the ceiling in the dark waiting hours to go to sleep. On a few occasions I\u2019ve been up since the day prior. (Just want to clarify I don\u2019t have PTSD, I\u2019ve never gone to combat). I feel like I\u2019m losing my mind. I\u2019ve tried everything. Over the counter medications, putting my phone on Do not Disturb far away from me. Running/Being active to tire myself out before going to bed. Nothing. I use to be able to sleep with Artillery going off but now I can\u2019t even sleep in a quiet room.",
    "flair": "Question/Advice",
    "score": 10,
    "comment_count": 18,
    "created_at": "2026-02-27T09:34:25+00:00",
    "top_comments": [
      {
        "id": "o7obv07",
        "score": 6,
        "body": "If you're service connected in any way, talk to the VA sleep center. \n\nThe gist is - get off screens at least 30min prior to bedtime. Try to set a strict sleep schedule. If you find yourself in bed unable to sleep, get up and go into a different room and do something boring, but no screens and nothing mentally stimulating, like go read the driest textbook you have, and let your eyes glazer over and then go back to bed when you're tired. No matter what, get up at your designated time."
      },
      {
        "id": "o7og0tn",
        "score": 5,
        "body": "I like mag glycinate every night. It's a nutrient your body actually needs bound to an amino acid that helps cool the body ever so slightly to prepare you for sleep. It improves sleep quality by relaxing muscles, calming the brain via GABA receptors."
      },
      {
        "id": "o7p2qw3",
        "score": 2,
        "body": "I\u2019ve found that routine works for me. I put on blue blocking glasses at 7, start getting ready for bed at 9 by drinking 8 ounces of tart cherry juice. At 9:30 I take CBD and get in bed by 10. If/when I wake up, I play a game of solitaire, read, try to figure out what ever it was that woke me up and after about an hour I can usually go back to sleep. Works for me, your mileage may vary."
      },
      {
        "id": "o7pntjr",
        "score": 2,
        "body": "Maybe stop working out at night. Being that you are older now your body could be responding to it differently. Try bio feed back and meditation. There\u2019s a few good channels on YT that have guided meditation. I\u2019ve been out for 20 years and had the same problem in the past. I would stay up for days sometimes. Now my sleep is better. If your drinking alcohol stop, that messes with your sleep cycle. I used to drink and pass out. Now that I\u2019m older when I drink I wake up around 1-3 am and stay up. So I stopped drinking. Hope this helps good luck. It will pass. Might take a lot of time but it will."
      },
      {
        "id": "o7ocs4b",
        "score": 1,
        "body": "Some days it\u2019ll be easier others not so much. Lol I know what you mean about the artillery bit. I was a 13M and it was like raindrop noise putting me to sleep."
      },
      {
        "id": "o7oq58u",
        "score": 1,
        "body": "I can't sleep in a quiet room! I use white noise to help. I soldi had to stop working out late. If when you ate going to the gym you take a pre workout the caffeine can long lasting residual effects. I won't take a pre after like 2pm."
      },
      {
        "id": "o7pawd3",
        "score": 1,
        "body": "I recently (and temporarily) had to make an adjustment to my work hours, and have been working from 3am to 1pm.  While occasional sleep issues are normal for me, they became constant so I had to make a few changes.\n\n\\-you may want to adjust your workouts...  I find that my HR is too high and messes with my sleep if I work out too close to bedtime.\n\n\\-I skip dinner altogether now since I go to bed around 5 or 6.  I found eating an hour or less before bed was also messing with my sleep.\n\n\\-I'm not sure if it's a placebo effect, but I read that some blue light blocking glasses would help.  I do have a habit of scrolling on my phone a little before I fall asleep, and I think the glasses definitely help (and they were cheap, off amazon).  Placebo or not, if it works it works.  \n\n\\-Sometimes I'll also drink \"Neurosleep\" which is supposed to help.  Never a full bottle, just a few sips.  This could also be placebo, but I think it helps.\n\nI'm 46 and find that the older I get the more picky my body is, especially with my sleep.  I hate it!"
      },
      {
        "id": "o7prkji",
        "score": 1,
        "body": "Could you give me your average day schedule with hours?"
      },
      {
        "id": "o7q39qk",
        "score": 1,
        "body": "Me to, it\u2019s like I\u2019m taking naps instead of getting a good sleep not to add the problem of falling asleep. Try gummy melitonin"
      },
      {
        "id": "o7qa5nu",
        "score": 1,
        "body": "I recently tried a sambucus gummy sleep aid by nature's way. I was amazed at how effective it worked. Your results may vary. Good luck. Sleep routines are good also"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rfzwlk",
    "title": "Need To Rant, I'm Having Some Struggles (Long, Sorry!)",
    "body": "Just went past my 6 year mark being out. I tried to get into the corporate job that I worked, but it was super hard. For the most part, people that I worked with pretty much disliked military or veterans, they made that known. Even though my first boss was a veteran, I know he hired me just to do me a veteran favor and because we got along and saw eye to eye on job related things that aligned with a position they were opening up (I did an informational meetup as I was transitioning out).\n\nIt was kind of evident that I was the outlier since I was never trained and had no mentoring, and people that came in after me had weeks and months of training and mentoring. Found out later from a close co-worker that my boss had asked one of the employees who had been there 20 years to train me, but they refused since they weren't the one that hired me.\u00a0\n\nEven though he was friendly, I eventually asked to work under somebody that was going to give me more challenging work because I was excelling and needed more challenges (and I knew he wasn't supportive). The new boss ended up being super toxic and was a terrible supervisor. It definitely made me miss the military a whole lot more.\u00a0\n\nIn the end, after 6 years, I got laid off due to budget during the government shutdown. No severance (they don't do that), just a 2-week notice. So, now I've been out of work for 4 1/2 months. I've applied for over 70 jobs for which I'm fully qualified and have tailored my resume and everything. I have a real distaste for the corporate world now, even though I'm trying to get back in it so I can earn a paycheck. Honestly, I'm trying to find anything.\u00a0And, I applied even to Home Depot and others. \n\nIn the end, I just need a job for money, I'm not even going to get into what it's all about. And, I'm definitely going to keep looking for new opportunities at the expense of my next employer and no longer try to be a faithful hard-working employee. Just check the blocks, collect the paycheck.\u00a0Still give 100% but F them. I think the worst part is the people that know I don't have a job and I'm looking keep asking me do you have a job yet, did you find something? No, MF, I haven't. \n\nMy service stretched over 32 years because I had a 7-year break (living in Europe, it was a great time). So, I'm not young. I also got out right before COVID so it kind of severed those military ties immediately. Now, I live over an hour away from where I moved 2 years ago, so I have zero connection with anyone. My old Army buddies are doing their thing, you know the drill. I'm beginning to go through a pretty dark time, and I'm having problems sleeping and starting to get rid of things. The ONLY thing keeping me afloat is my kids, I can't stop supporting them. \n\nAnd, yes, I've talked with the Crisis Hotline and all of that. It's barely slightly helpful. They did further provide an advocate (from the VA?) who called and left a message. I ended up calling her three times and leaving messages, and never heard anything so I just gave up.\n\nI'm definitely without a network, and it's festering. \u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200bI need some kind of mental/spiritual/physical fulfillment. I did go to a veterans meetup in town and everyone was Vietnam era so it was awkward, they clearly had their cliques. Many organizations are drinking-oriented, not my thing. Before anyone asks, no, I don't have the GI bill as I gave it to my kids. \n\nI did apply for VR&E the first week of October when I got laid off, and I haven't heard anything other than to replies when I reached out saying that they're answering everything in the order \u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200bit was received. After 4 months we're burning a significant hole in our savings, and I've got about one more month before we're probably facing homelessness unless I start burning through my retirement savings (which I will). \u200b\u200b\u200b\n\nI did go back to a lot of the organizations that I used when I was transitioning out which is helpful with doing some webinars and getting a little bit of assistance. I even have an account with Coursera, but I can barely get motivated with itand I feel like I just want to sleep all the time and lack ambition. \u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200bMentally, I want to change, but I'm running through quicksand and not applying effort. \n\nSorry you had to read this, I really just had to put it out there somewhere, I don't even talk to my wife about a lot of this. I don't want my family to realize where I'm at with this. \u200b\u200b\u200b\u200b\u200bI was hoping to have a counselor to talk with about this. To no avail. ",
    "flair": "Discussion",
    "score": 23,
    "comment_count": 8,
    "created_at": "2026-02-27T07:12:30+00:00",
    "top_comments": [
      {
        "id": "o7ohcce",
        "score": 5,
        "body": "See if you qualify for a State CDL program through your local department of labor or any local bus companies looking for drivers. They'll usually train you for a CDL through them and you'll be required to work there for a year or two but it just gives you something to fall back on in rough times."
      },
      {
        "id": "o7nzt6p",
        "score": 4,
        "body": "Maybe, you should talk to your wife about this. Being vulnerable to your partner would probably lighten some load off of your shoulders. If anything, she should support you while you are struggling. Atleast, my wife does. \n\nMaybe, get into a trade? Go to community college? Or go to church if you feel like it. I don\u2019t want to impose faith on you, but the guy upstairs got me through heavy times especially when my wife and I were homeless living in our car. We made it through, but I cannot give myself full credit for it. \n\nJust do anything at this point that will pay the bills man. You don\u2019t really got a choice."
      },
      {
        "id": "o7opejh",
        "score": 2,
        "body": "Idk where you\u2019re located but I got my CDL training paid for by a work force development grant. Ended up only having to pay ($50.00). I put 7 years into trying to get my small business going after getting out. It didn\u2019t work out the way I planned so I decided to do something else. I submitted hundreds of resumes and didn\u2019t hear anything back. Finished CDL training in August of 25. Three days after I started my first job. I locked down a local job working for a farm after that. Monday I start with Nutrien Ag hauling fertilizer locally. 21 days paid vacation prorated for the first year and 9% 401k matching."
      },
      {
        "id": "o7qba9q",
        "score": 2,
        "body": "Hang in there! Similar boat as you.  Keep pushing. Consider a field change as a bridge job? \" It's easier to get a job when you have a job\". Corny. I know but seems true.\n\nHave you tried for VA jobs for cultural alignment? I found the transition from military to corporate extremely hard. Ultimately, the kinder, gentler world of corporate life won. I hope you're able to transition easily.\nI wish you the best. Have hope. It will happen. \n\nMy story for comparison and conviction of Hope...\n2017 Moved across country for a company that laid me off 3 years later. Been on the layoff wagon since (3 more layoffs). As an older employer, starting over doesn't match the life I've built with a wife, kids and bills. Savings is depleted.\n \nAfter 95 resumes, 20 interviews, and four months, I did land a job and it's my second field of choice so I have doubts of success but a job is a job."
      },
      {
        "id": "o7q1be9",
        "score": 2,
        "body": "The city bus driver start off at $32/hr with a hiring bonus incentive in my city with a pension, and annual increases. No experience and will train to get you your CDL."
      },
      {
        "id": "o8dd47v",
        "score": 1,
        "body": "8 year Navy vet here, and I rate VA claims for vets. \u00a0Maybe you should not be physically working and mentally work on yourself. Yes, it is an adjustment, but there is life after the military. If you have your 100%, like I think you should as a Vietnam Vet, then that should sustain yall for a bit, depending on the state you live in. \u00a0You can always volunteer at children\u2019s hospitals, homeless shelters, libraries\u2026so many people need help too. Dont just give up on life, you were a person before that uniform and you\u2019re a person after. The uniform does not define you.\u00a0"
      },
      {
        "id": "o8dd9yi",
        "score": 1,
        "body": "It\u2019s sad that corporate America dont wanna hire us. No one tells you that part."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rfxz2h",
    "title": "Chronic pain",
    "body": "I have had a hip replaced, waiting on my second one. Had my c6/7 vertebrae fused(7 months post op). I\u2019m having severe nerve pain shoot down my right arm. The pain in my right back and arm has left my chronic hip pain feeling like a field of daisy\u2019s. I woke up feeling like this is the end. I have fought endlessly for years through surgery\u2019s to find a sense of normalcy, it doesn\u2019t seem like that\u2019s a thing I\u2019ll be graced to find. I yell in my sleep from discomfort, I have medical \u201cprofessionals\u201d at the VA telling me I\u2019m normal, while I can\u2019t breathe, laugh or cough without debilitating pain that lasts for hours. I have reached out to the VA again. The best they could tell me is that they\u2019d get me in to see a professional in 3 weeks. WTF!?\n\nWhat are we supposed to do here? I know I\u2019m not the only one. ",
    "flair": "Question/Advice",
    "score": 5,
    "comment_count": 6,
    "created_at": "2026-02-27T05:24:51+00:00",
    "top_comments": [
      {
        "id": "o7nhyem",
        "score": 2,
        "body": "Im angry, im tired and my pains ceases to quit."
      },
      {
        "id": "o7o7a3a",
        "score": 1,
        "body": "ask for a referral to a pain clinic in the community if you want pain killers. VA just won\u2019t prescribe them these days. Thats what I had to do."
      },
      {
        "id": "o7peplf",
        "score": 1,
        "body": "The VA offers Telehealth Pain Management seminars and \u201cpain teams.\u201d These are often affiliated with major VA medical centers.\nI am on my fourth type of chronic pain seminars.\nI find these extremely helpful."
      },
      {
        "id": "o7p7xfx",
        "score": 1,
        "body": "The VA does prescribes them. They don\u2019t prescribe them to those with \u201cseeking\u201d behavior though from my understanding. They don\u2019t want someone to become addicted to them. The VA doctors have to fill out some sort of pain medicine approval system to assess you before they can prescribe. I\u2019ve seen it and my doctors have talked about it. I have chronic pain and have been given numerous pain medication for chronic pain."
      },
      {
        "id": "o7qgs38",
        "score": 1,
        "body": "Ive been going to the pain clinic for the last month. It\u2019s been alright, but its cognitive therapy. My doc there hasnt(or maybe can\u2019t) prescribe medicine."
      },
      {
        "id": "o7qgckj",
        "score": 1,
        "body": "I\u2019ll look into that. I\u2019m currently going to the pain clinic, but it\u2019s all cognitive therapy. It\u2019s good, but it\u2019s more of learning how to deal with it unfortunately."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rfsc75",
    "title": "Anyone else financially stable after retirement but still feel unfulfilled in civilian work?",
    "body": "Retired after 20 years. Financially stable between pension and current job. Fully remote, flexible schedule, good compensation.\n\nOn paper, everything looks good.\n\nBut I\u2019m struggling with fulfillment in my civilian role. I don\u2019t feel ownership of anything. A lot of relationship management and reactive work. I also find high-level corporate meetings stressful in a way that surprises me.\n\nHas anyone else experienced this disconnect after transition? What helped you define purpose or ownership in civilian life?",
    "flair": "Question/Advice",
    "score": 16,
    "comment_count": 13,
    "created_at": "2026-02-27T00:59:52+00:00",
    "top_comments": [
      {
        "id": "o7nof63",
        "score": 7,
        "body": "I'm retirement and doing okay financially but I feel like I don't fit in"
      },
      {
        "id": "o7ohcd5",
        "score": 5,
        "body": "The same thing happened to me too, I went into a role and had a NCO mindset trying to fix everything make things more efficient. Oh boy that does not work there is no structure in the civilian world. I decided to stop caring, because if I kept caring I would just go crazy."
      },
      {
        "id": "o7mx8q2",
        "score": 3,
        "body": "Dude, it sounds like you\u2019ve made your job your identity. This is common in our veteran demographic. Once the carpet is pulled from under you (prior service),you lose your purpose. A job or a career in itself is not a sense of purpose, the come and go. You\u2019re gonna have to do some introspection and figure out who you are, what you value and what you want to get of life. Separate yourself from your career and slowly you\u2019ll learn to live a happy existence. A job is just a means to exist, and if you\u2019re lucky you still have your family and friends, who I will remind you do not give a shit what your career is, they only care that you\u2019re in their lives! Good luck and good journey"
      },
      {
        "id": "o7qqz4m",
        "score": 2,
        "body": "Literally everyone feels this...except the financially stable part."
      },
      {
        "id": "o7oubgd",
        "score": 2,
        "body": "Wow this sounds all too familiar. I just wish there was a better solution than \"stop caring\"."
      },
      {
        "id": "o7masaf",
        "score": 1,
        "body": "[DoD Information Book on Benefits - 2025] (https://warriorcare.dodlive.mil/Portals/113/DoD%20Wounded%20Ill%20and%20Injured%20Compensation%20and%20Benefits%20Handbook%20(Published%20March%202025).pdf?ver=XxCAfhqHnDFULID0dQ6gHw%3d%3d)\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Veterans) if you have any questions or concerns.*"
      },
      {
        "id": "o7mbnbm",
        "score": 1,
        "body": "No. Completely enjoy what I do. It\u2019s like in service leading sailors but with less of the personal bullshit AND I\u2019m learning new skills in the realm of finance/CAM working and managing a budget. my boss is there to catch me/listen to my input and implement my numbers when they make sense and adjust when they don\u2019t leveraging his experience. Hell yeah"
      },
      {
        "id": "o7u2j9m",
        "score": 1,
        "body": "This sounds wierd, but ive been \"semi retired\" from the military for the past 3 years. Ive done consulting for ice cream companies, ive been a program manager for a tech company (inperson and remote) , ive taught at a school, and ive worked with the homeless and Ill soon have an MBA.  After being in all of those roles, ive realized that what fills my cup is helping others and seeing the fruits of my labor happen in real-time, and every role I do after this will involve helping people\n\nSecond thing I've learned, is that for the past 19 years, my identity was the military and aviation, where when I started this retirement process, my identity was stripped away and I had to find a new thing for myself, so I started volunteering in my free time in order to not make my new jobs my identity, and dude... what a relief, it helped the mental fatigue for me quiet a bit"
      },
      {
        "id": "o7vwi3e",
        "score": 1,
        "body": "This is exactly how I feel. Retired, Financially stable with remote job. My old-military mindset was in full gear during my first 2 months as I was on teams call about 15 minutes early, then one day one of the younger engineers politely said \u201cstop dialing in too early, everyone dials in about 2 minutes before the meeting\u201d. That\u2019s the day I told myself I\u2019m not wearing the uniform anymore, and let it go.  \n\nI have this itch to switch to civil service and be around the fed environment, but I love my remote job with great pay, and filling my family\u2019s cup.  I\u2019ve been able to financially see family more and help financially, and that feels so good than when I was active duty. I guess I\u2019ll just keep this job for now for those reasons."
      },
      {
        "id": "o7vzw8b",
        "score": 1,
        "body": "I found purpose in helping people and volunteering."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rfmih0",
    "title": "I have a question",
    "body": "I was just wondering if anyone is kinda insecure about their service. My parents Me feel that way my mom specially and have some bad mental health. I was a corpsman at naval hospital camp lejeune in the emergency room I was there from 2018-2022 Covid really fucked me up mentally and my mom says I wasn\u2019t over seas and I should be fine I\u2019ve told her some of the things I\u2019ve seen specifically babies but she just either forgets or doesn\u2019t care and my dad as well he says he understands it but doesn\u2019t empathize with me. Neither of them were in the military. ",
    "flair": "Question/Advice",
    "score": 7,
    "comment_count": 28,
    "created_at": "2026-02-26T21:09:12+00:00",
    "top_comments": [
      {
        "id": "o7l5qms",
        "score": 12,
        "body": "Respectfully...your mom is wrong and needs to stop. You have every right to be proud of your service, especially as a corpsman. I have a special place in my heart for corpsman and medics in general, they saved my son's life in Afghanistan. You served during COVID and while it may not have been overseas, it was still a tough time and I'm sorry you had to go through that. Mom needs to back off. I would stop talking about your service with her, she has no idea what it's like being in the military and never will. Her comments and little remarks don't mean anything."
      },
      {
        "id": "o7l70bt",
        "score": 12,
        "body": "Their opinions are background noise. I did 10-20 in the Army with a few tours and my mom still complains about how I didn\u2019t become a doctor and she would die happy if I did; while my dad says \u201canyone can walk with weight and a gun for miles\u201d but he won\u2019t go hiking and can barely lift 40lbs himself.\n\nFamily isn\u2019t the best form of support, they never walked a step in your boots. When people don\u2019t understand they downplay it especially when it\u2019s intimidating like the military. \n\nJust remember you did serve, you answered the call war or not, you did your time honorably and no one can take that from you. Ever."
      },
      {
        "id": "o7nzazq",
        "score": 7,
        "body": "I left the military with 6 weeks of memory I cannot access, and have flashbacks of burnt bodies, and such after 9/11.  My PTSD is rather...frustrating. It has SHAPED my life, the way I am, how I work (remote for the last 20 years), how I make friends (barely have any, but only a few very close ones), and how I raised my children.  My entire world has shaped around my coping capabilities, and how I interact with the world is shaped by these...issues.  The VA has been wonderful helping me through it, working with the anxeity and working with the depression that comes with it, but it's something that's static in life - The triggers may be manageable, but will never ever fully go away. \n\nBut, do I regret my service? NEVER  \nI had such a great time during service, and while 9/11 happend during it, I still had a wonderful time, even though i was tasked to do things.....that...........well, not really worth talking about here. \n\nI still dont' regret it, and I still belive it's worth while.  Heck, just 3 years ago, a veteran friend of mine who went back to work at the base still said they use documentation written by me 20 years ago lol  that gives me such great comfort that I left a good mark. \n\nService is what you make of it, what mark you can leave on it, and what marks it leaves on you.  I cannot...regret....what is me.  Who I am today, for better or worse, is because of the military; and how I run my business, how my children are (one becoming a lawyer and the other a phenominal programmer), is all affected by how my service shaped me. \n\nI can't....ever....regret it :)  And, as to being insecure about it? Insecurities are usually bred out of regret, or failed mindsets - the military taught me to not accept either :) So, not insecure about it either. I earned my benefits. I served my time. And, I helped contribute to various missions. I'm fine with that :)"
      },
      {
        "id": "o7lgjqu",
        "score": 6,
        "body": "Listen. You chose to say that oath. You served. Doesnt matter if it was boots on ground or not. Be proud you stepped up when so many didnt. And to serve during covid, thats a real kind of stepping up, whether you intended for that or not, you still did it. \n\nAs for what your parents have to say, stop listening. Haters gonna hate. They dont, wont or cant understand what you did, and thats not your fault, or frankly, your problem. Id recommend stop trying to get praise from them, and stop letting them make you feel bad for what many would consider honorable service.\n\nYou went in and became a corpsman because you wanted to help people, and it sounds like you did. Good on you for that. I hope thing turn around for you."
      },
      {
        "id": "o7ldq1o",
        "score": 3,
        "body": "From someone that was deployed overseas during COVID, I think we all lived through a shared experience. \n\nYour service isn't lesser than mine, and mine no more meaningful than yours, because we all signed on the dotted line to do the job, and the Navy told us where they needed us. You were responding to legit medical needs in someone's time of need. Don't ever tell yourself that the line of work you were in didn't make a difference in someone's life. \n\nA lot of people that never served or weren't a first responder don't know what the real world is like, or care not to think about the tragedy in day to day life, they live in their bubble and hide from anything that makes them uncomfortable. We didn't get that luxury, but we can turn the good and bad things we witnessed into something positive. I would say depending on where you live, there are peer support groups that meet at VET Centers or through WWP online and in person. Talking with other vets, even though all of our experiences are our own, has helped me a great deal. Something to consider if you need a group that will understand. \n\n  \n"
      },
      {
        "id": "o7l8srl",
        "score": 3,
        "body": "Serving during covid would have really fucked me up! I'm a combat vet - a corpsman who served with Marines on the front lines. \nMy best friend died, then a business partner, then 4 people I went to high school with - ALL in much better shape than I.\nI have PTSD but I really believe that it mostly came from the time I worked the ER at NavHospGLakes.\nMake sure you apply for VA benefits. You deserve them!"
      },
      {
        "id": "o7lbxyf",
        "score": 3,
        "body": "[removed]"
      },
      {
        "id": "o7mo87p",
        "score": 3,
        "body": "Hey man Im proud of you.\n\nWhat matters now is staying in the present.\n\nWhat will you do now."
      },
      {
        "id": "o7uox1c",
        "score": 3,
        "body": "dad- \u201canyone can walk with weight and a gun for miles\u201d\n\nyou- \u201dbet, here is a rubber duck and a 80lbs rucksack, let\u2019s go\u201d"
      },
      {
        "id": "o7mhd1t",
        "score": 3,
        "body": "I am so glad that building was destroyed, horrible memories when I was an HM there\u00a0"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rflo4d",
    "title": "MBA worth it through VR&E?",
    "body": "Did 8 years in, and have been working for the gov the last 7 years. Getting let go because of cutbacks and qualified for the VR&E. Thinking about doing an MBA but I\u2019m almost 40, have a family, and want to be in the Chicago area. \n\nQuestion: if I\u2019m not paying for it, is an MBA worth it if not from a T25 program? \n\n(Prob going to post this in r/MBA as well because I have my VR&E meeting soon)",
    "flair": "VR&E - Voc Rehab Veteran Readiness",
    "score": 13,
    "comment_count": 44,
    "created_at": "2026-02-26T20:38:44+00:00",
    "top_comments": [
      {
        "id": "o7kxbqc",
        "score": 11,
        "body": "It is rewarding but it is up to your counselor to decide if that is the path for vocational rehab. VRE is not an education benefit."
      },
      {
        "id": "o7l0aup",
        "score": 9,
        "body": "MBA is all about networking and connections (and internships). It is what you make it."
      },
      {
        "id": "o7l6nxn",
        "score": 6,
        "body": "That really depends on where you get an MBA. I was able to use VRE to get an MBA at a private AACSB and although the connections are great, the coursework has enabled me more than any connections. So while true at some schools, in others the coursework is truly transformational. "
      },
      {
        "id": "o7kzngd",
        "score": 4,
        "body": "If you get into Booth, 100%. You\u2019ll be pivoting out of gov most likely. I went to a T25 EMBA program and it\u2019s helped tremendously in my space. VR&E if at 100% you\u2019ll be able to get school covered, and also get your school loans forgiven. So you can take out the $128k in student loans and then forgive them and pay I believe only taxes on it once completed, some folks do that to keep themselves paid in the mean time during school. If enlisted, check out enlisted exfil as they are an amazing source for folks aiming for top MBA programs and answer all these kind of questions, from resume screening to prepping. It\u2019s a community on discord and LinkedIn totally free"
      },
      {
        "id": "o7l5psu",
        "score": 4,
        "body": "Yeah you need to accentuate how your service connected  disabilities impede you from certain work and that the job you\u2019d want to pursue, which is easier on your mental/physical health, requires an MBA. That\u2019ll pretty much get you into the honey."
      },
      {
        "id": "o7lbbhn",
        "score": 3,
        "body": "I'd say an MBA can be very useful, especially when applied correctly. I got mine using VR&E and it has helped land a number of jobs making good money over the years. Combined with my military and civlian experiences it has played a role in getting position that I am about to land making over 170k a year.\n\nSome people may say it is too broad of a degree but I haven't found that to be the case in my situation. I still recall the VR&E counselor telling me during our initial meeting that people with an MBA \"don't make a lot of money\". I wish that I had stayed in contact  so that i could share my experiences with her and maybe change her beliefs."
      },
      {
        "id": "o7mh400",
        "score": 3,
        "body": "Man I wish the government loans equaled the total cost of tuition, but they have some weird math that makes it less for me. VRE covers it all but the loans aren\u2019t equal. They must have learned math from the VA \ud83e\udd23"
      },
      {
        "id": "o7lhhn6",
        "score": 2,
        "body": "Try to get in Chicago or Northwestern man. Definitely worth it!"
      },
      {
        "id": "o7lo39f",
        "score": 2,
        "body": "Personal growth is always worth it. That it\u2019s free is but icing on the cake."
      },
      {
        "id": "o7mhmxi",
        "score": 2,
        "body": "I\u2019m just north of 40, not in a T25 program, and ran a business for a decade prior to this. Not learning much from the program that\u2019s useful, but having an MBA still opens doors into corporate roles I\u2019d be passed over for otherwise. And that the MBA is paid for by VRE made it a deal too good for me to pass up."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rfilci",
    "title": "[HIRING] Electrical Engineering Technician \u2013 Eden GeoPower | Somerville, MA",
    "body": "Hey r/Veterans, posting this job offer on behalf of [Eden](https://www.edengeopower.com/), a clean energy startup pioneering high-voltage electrical reservoir stimulation technology. \n\nThey're looking for an Electrical Engineering Technician to join their team in Somerville, MA. It's a hands-on, field-deployed role that's a strong match for veterans with backgrounds in:\n\n* Electrical systems, power generation, or high-voltage equipment\n* Military occupational specialties like electrical/electronics repair\n* NETA certification or NFPA 70E/79 experience (a plus, not a must)\n\nWhy this could be a great fit for you? If you're used to field deployment and working with complex electrical systems under real-world conditions, you'll definitely thrive here!\n\nLocation: Somerville, MA Apply here: [https://apply.workable.com/eden-geopower/j/094844E39D/](https://apply.workable.com/eden-geopower/j/094844E39D/)\n\nFeel free to DM me with any questions before applying.",
    "flair": "Employment",
    "score": 5,
    "comment_count": 0,
    "created_at": "2026-02-26T18:45:02+00:00",
    "top_comments": []
  },
  {
    "subreddit": "Veterans",
    "id": "1rfikts",
    "title": "Embarrassed to say it, but I'm struggling after retirement.",
    "body": "I\u2019m struggling right now. I served in both the Army and Air Force and have been retired from the Air Force two years now. I have experienced plenty of challenges before but what I'm going through now is kicking my a$$ and because of it I am more lost today than I have ever been in my life!\n\nThis has nothing to do with experiences in Combat. I never saw combat while I was in Iraq or any of my other deployments. The closest I ever got was on October 27, 1995, during an Active Shooter incident on Fort Bragg. While that experience definitely sucked and affects  \nmy ability to handle large crowds to this day, I am struggling with something  \nelse thats destroying mentally. \n\nI thought that I was going to love retirement, but found that as the years roll by, I really miss the military structure and camaraderie. I thought that I would find meaning in my life right away or at least by now, but I am still looking everywhere and struggling with thoughts of giving up.\n\nA huge kick in the nuts is that old military friends and colleagues that once promised to keep in touch or help me out (if I ever needed it), have all but disappeared. The ones that I still talk to are great friends and I enjoy hanging out with them. They are positive and have expressed interest in helping especially in finding jobs, but I feel all my pleas for support have become a burden on them.\n\nI started looking, networking and applying almost a year before I got out. I was feeling positive I was going to land a job not long after I retired. It\u2019s been two years and I have not had a steady or meaningful job. Two years of applying, getting some interviews and receiving lots of rejection letters or no letters. Two years of job fairs and networking that lead to nothing. \n\nI got back into school last year and earned a PM certificate but not the one that matters. I've been struggling to make myself study for the PMI PMP exam. Most days I sit in my office looking for jobs, applying for jobs, and beating myself up over not being able to figure it all out!\n\nI started therapy sessions a few months ago when I thought I had hit rock bottom. I wish I could say it was helping, but my mental health sucks right now. I'm too embarrassed to talk to any friends or family about it. I've talked to my wife about it a few times, but I can tell it stresses her out, I stay out of sight and avoid the conversation as much as possible. \n\nIt kills me that I went from being a Senior Enlisted Leader taking care of people and the mission a few years ago to just another guy with no job that can't get his shit together. \u00a0\n\nI don't know who to turn to at this point. ",
    "flair": "Question/Advice",
    "score": 105,
    "comment_count": 64,
    "created_at": "2026-02-26T18:44:34+00:00",
    "top_comments": [
      {
        "id": "o7kita6",
        "score": 34,
        "body": "assuming 20+ year retirement + VA rating you probably dont really \"need\" to find employment that way. consider starting a small business or serious hobby project?"
      },
      {
        "id": "o7kmxj9",
        "score": 33,
        "body": "Find some volunteer work to give meaning. Animal shelters, food pantries, habitat for humanity, sports coach, etc."
      },
      {
        "id": "o7kiylp",
        "score": 13,
        "body": "My heart goes out to you comrade. Because, it sucks what you're going through. And frankly I don't have a magical answer. \n\nI'll say this that you made it good decision to get therapy. And I would encourage you to continue with that idea. Now if the therapy sort that you're getting isn't being helpful there are other modalities for therapy. So the thing about therapy is you may need a different variety. \n\nYou've got the right idea about tying into veterans. Frankly the issue I find is we understand each other. And not to sound critical of civilians but the truth is they don't have a clue. And this doesn't have to do with combat or anything. I wasn't a combat veteran. I however was explosive ordinance disposal so I had my own interesting events that scared the crap out of me. Fortunately I was good at my job. \n\nIf that sort of thing helps you feel better about what's going on then do more of it. Not a hard choice to make there. Just feeling better over time is going to help you. \n\nOf course the whole employment thing is also related to wherever you are in the world. But I'd encourage you to believe in yourself. And not beat yourself up over what you cannot fix. You cannot make jobs appear by magic. No matter how much you want to. Believe me I've been there done that. And I've had those feelings where you want to put the burden to blame on yourself. Don't. If you're doing the things you need to do and it's not having success then the obvious one of course is to do something different. If there's no jobs to be had then stop making them the focus. That doesn't mean you stop looking but don't let it be the focus of your life. \n\nOf course my service was back in the Vietnam days. I've gone through many of the things you're talking about but that's not my circumstance today. So you can take that as an assertion and proof that you can get through this and that things will get better. It just may take some damn time. So try to find ways to take care of yourself and the people you love so you can maintain. \n\nStop blaming yourself. Stop buying into the idea that somehow it's your inadequacy. Keep on doing what you know you need to do. Keep on talking to people. Keep on with some sort of therapy and just keep maintain it. Good luck."
      },
      {
        "id": "o7khtly",
        "score": 12,
        "body": "Well I did my 4 and gtfo, fairly young dude and I\u2019m still pacing in my head on WTF I\u2019m supposed to do with my life. The truth is, some of the homies vanish. It just happens. Also it doesn\u2019t help to reach out to them too yk. I was an MP and I still can\u2019t get hired for shit! \nAlla I gotta say is, keep busy. Have goals. Gym gym gym even though I\u2019m being a fat body right now, I can\u2019t lie. Need to get back in there because it really helps. Try to find new hobbies. Keep your wife entertained because at the end of the day, she\u2019s all you got. Check out federal jobs as well."
      },
      {
        "id": "o7ll2as",
        "score": 11,
        "body": "I was too. I started drinking hard before I retired, then it got real bad.  Stay plugged in with other veterans. I didn't do that, I isolated myself.  You got this friend. By the way. I've been clean and sober for over 4yrs. You got this friend. \ud83d\udc4d\ud83d\ude0e\ud83e\ude96"
      },
      {
        "id": "o7mmvyq",
        "score": 8,
        "body": "What I'd add to my comment is think broadly. And ultimately think about what would please you. It's time brother to put away the demands from other folks. And focus on what's going to fulfill you. Because no matter that you have people like your life and you have people that you love if you don't take care of you you can't do good for them."
      },
      {
        "id": "o7l9g85",
        "score": 8,
        "body": "I basically just typed out the same thing, I gained like 30 lbs in a few years after I got out. Not really a fat ass, just bulkier lol but getting back into a good gym routine has made me feel something again"
      },
      {
        "id": "o7kmcz9",
        "score": 7,
        "body": "A couple things brother; \n\nThe job market for lack of better terms, sucks right now. Some things I\u2019ve read claim it to be worse than 08/09. It\u2019s cyclical, it should get better but there are so many things playing a part in the redistribution of the work force and taskings that what better looks is variable. \n\nI am glad to read that you are receiving treatment, it\u2019s good to have a professional listener in your corner. \n\nLast, set goals man. Goals that you have the control to complete. A hobby, fitness, just something with small attainable goals. In the military we accomplish things every day, and then there\u2019s always another goal to attain. Find a way to replicate that in some form. Lift an extra amount of weight, learn a new song on an instrument, catch a fish. Something you have fun with and also can get a feeling of accomplishment and/or frustrated with helps tremendously."
      },
      {
        "id": "o7ki6gq",
        "score": 6,
        "body": "I don't know where you live, I felt the same.  My state had a state guard (state defense force)  it gave me what I needed, the comradarie, plus I helped in a few natural disasters.  See if your state has one and if it looks interesting."
      },
      {
        "id": "o7moava",
        "score": 6,
        "body": "The lack of dignity with this job market is appalling. I'm in the same boat, with countless others. I went to a Wells Fargo VET program info session and they told me 600-1000 people apply for the handful of roles they have. Others spoke in the Zoom call and one thing came up more than not: What are we doing wrong? And the answer we got was skirting around it. There is an employment crisis within this country. Hundred's of thousands of fully capable and fully qualified people getting rejected day after day. We've all tried networking. We've all tried LinkedIn. We've all tried job fairs. We've all tried tailoring our resume. It's time to admit that it's all bullshit. Sitting in that meeting and hearing guys with 20+ years of serving in the military, to having 20+ years of relevant job experience sitting there asking \"why are we not getting any interviews?\" is humbling, and to me, disappointing. If someone *that* experienced can't get the job, how the hell can I? \n\nI understand the advice of getting some bullshit job or doing some passion project, but the reality is a lot of us don't care to do that or have bigger ambitions. It's a shame that the first thing most of us wake up to each morning is another email rejection letter. Great way to start a day. \n\nI'm sorry you're going through this. Good luck. The lack of purpose and dignity is hurtful."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rfi31o",
    "title": "I\u2019m in college for almost a year and this is the first time this has happened.",
    "body": "Is this normal for the VR&E to pay in bits usually they pay it all at once, is anyone else have this problem?",
    "flair": "VR&E - Voc Rehab Veteran Readiness",
    "score": 8,
    "comment_count": 4,
    "created_at": "2026-02-26T18:26:19+00:00",
    "top_comments": [
      {
        "id": "o7k6cvu",
        "score": 5,
        "body": "Depends on how your school submitted the invoice"
      },
      {
        "id": "o7mk8n5",
        "score": 1,
        "body": "Yes my pending payment is only 3500 and its usually 4500. never had this happen before and i really need it.\n\n  \nedit: mine is post 9/11 gi bill payment."
      },
      {
        "id": "o7o9qbb",
        "score": 1,
        "body": "I get paid monthly. I've never seen a statement like this though."
      },
      {
        "id": "o7orvgq",
        "score": 1,
        "body": "That\u2019s for paying the school not the monthly payment"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rfg7vh",
    "title": "March 3 Missouri House Veterans Committee Hearing \u2013 Disabled Veteran Tax Relief",
    "body": "The Missouri House Veterans Committee is holding a hearing on multiple Disabled Veteran Property Tax bills.\u00a0*Missouri is one of the few states left without meaningful property tax relief for disabled veterans. Every state that borders Missouri offers some form of veteran tax benefit.*\n\n\ud83d\uddd3 Tuesday, March 3, 2026  \n\u23f0 12:00 PM  \n\ud83d\udccd House Hearing Room 7  \nYou do NOT need to attend in person to participate.\n\n**Live video feed:**  \n[https://house.mo.gov/CommitteeDetail.aspx?category=all&year=2026&code=R&cluster=true&committee=4346&nid=11308](https://house.mo.gov/CommitteeDetail.aspx?category=all&year=2026&code=R&cluster=true&committee=4346&nid=11308)\n\n**Bills being heard include:**\n\n\u2022 4 statewide homestead exemption bills (tiered relief based on VA disability rating)  \n\u2022 2 county-option real property tax credit bills  \n\u2022 1 county-option personal property tax bill (up to two vehicles)\n\n(This is the committee stage. This determines which bills move forward. We are hoping at least one bill moves forward this session.)\n\n**Submit testimony here:**  \n[https://witness.house.mo.gov/Default.aspx?bill=HB2276&noticeid=11308](https://witness.house.mo.gov/Default.aspx?bill=HB2276&noticeid=11308)\n\nWhen submitting:  \n\u2022 Select ALL disabled veteran property tax bills listed for the hearing  \n\u2022 You can copy and paste the same statement for each bill\n\nEven short testimony matters. Committee members look at how many veterans speak up.\n\n**Simple template you can use:**\n\nChairman and Members of the Committee,  \nI am a Missouri veteran and I support legislation that provides property tax relief for disabled veterans. Rising property taxes affect veterans and their families across our state. Please move these bills forward. Thank you.",
    "flair": "Article/News",
    "score": 9,
    "comment_count": 0,
    "created_at": "2026-02-26T17:20:02+00:00",
    "top_comments": []
  },
  {
    "subreddit": "Veterans",
    "id": "1rffm4k",
    "title": "VA VRNE CASE TRANSFER",
    "body": "After 7 months of waiting, I finally did my VRC VR&E initial intrview and was found entitled for the program. I requested that my case be transferred to the Washington State regional office because I'll be relocating in May. Ideally I want to be enrolled on Fall semester. I'm just wondering how fast they can transfer my case. I also was told that I won't do orientation and initial interviw again there. I just hope its true. Anybody experience this?",
    "flair": "Question/Advice",
    "score": 3,
    "comment_count": 11,
    "created_at": "2026-02-26T16:58:43+00:00",
    "top_comments": [
      {
        "id": "o7jl2sh",
        "score": 1,
        "body": "'Have you looked in the **[Wiki]( https://www.reddit.com/r/Veterans/wiki/education)** for an answer? We have a lot of information posted there. \n\nTo contact VA Education, 1-888-442-4551, for ~~Voc Rehab~~ VR&E (Veteran Readiness and Employment Program) assistance with appointments or problems with your Case Manager (not for missing payments): 1-202-461-9600. \n\n**Payments for certain education benefits (DEA, VEAP) are paid at the end of the month you attend school - Department of Treasury issues these payments **using a 10 business day window** - these payments are not locked into a specific day of the month like VA disability/military pay is**. For Voc Rehab missing payments, contact your Case Manager or your local **[VA Regional Office](https://www.knowva.ebenefits.va.gov/system/templates/selfservice/va_ssnew/help/customer/locale/en-US/portal/554400000001018/content/554400000260849/VRE-Officers-and-Contact-Information)\n\nFor Post 9/11 GI Bill only, If you signed up for direct deposit when you applied for education benefits, **we\u2019ll deposit your payment into your bank account 7 to 10 business days after you verify your school enrollment.** This is the fastest way to receive your payment. [Text Verification FAQ](https://benefits.va.gov/GIBILL/docs/IsaksonRoe/EnrollmentVerificationFAQs.pdf)\n\nMGIB and MGIB-SR and DEA CH 35 have to do [monthly verification](https://www.va.gov/education/verify-school-enrollment/) and you should receive the payment within 3 to 5 business days.\n\nFor Online Only training, the Post 9/11 GI Bill is currently **(1 August 2025) paying $1169.00** for those who started using their Post 9/11 GI Bill on/after 1 January 2018 - this is based on 1/2 of the National Average BAH paid to an E5 with dependents. Post 9/11 GI Bill MHA rates are adjusted 1 August of each year and are based on the 1 January DoD BAH rates for that year - **so VA can't use 1 January 2025 BAH rates until 1 August 2025** - for those who started training on/after 1 January 2018, the MHA rates are 95% of the DoD BAH rates. First possible payment for the 1 August 2025 increase is 1 September.\n\nFor VR&E, there are two different Subsistence Allowance programs - https://www.benefits.va.gov/vocrehab/subsistence_allowance_rates.asp The P9/11 Subsistence Allowance is based on the BAH paid to an E5 with dependents. Those who started using VR&E on/after 1 January 2018 receive 95% of the BAH paid to an E5 with dependents. **As of 1 January 2026 Online only students using VR&E are being paid $1198.00** if they started using VR&E on/after 1 January 2018. The CH31 Subsistence Allowance rates are adjusted 1 October each year by Congress.\n\nVA Education is going paperless - make sure VA has a current email address for you. Please make sure you add Veteransbenefits@messages.va.gov to your contacts list so that you don't miss important updates from VA.\n\n[VA Award Letter explanation](https://benefits.va.gov/gibill/understandingyourawardletter.asp)\n\n[Contact a VR&E Supervisor](https://www.knowva.ebenefits.va.gov/system/templates/selfservice/va_ssnew/help/customer/locale/en-US/portal/554400000001018/content/554400000260849/VRE-Officers-and-Contact-Information)\n\n [VA Rudisill Decision](https://benefits.va.gov/gibill/rudisill.asp) - some veterans may qualify for an additional 12 months of a second GI Bill based on serving two or more different periods of active duty service.\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Veterans) if you have any questions or concerns.*"
      },
      {
        "id": "o7kfkil",
        "score": 1,
        "body": "I had to do interview, orientation all over again IN the same state because I took a semester off due to a move."
      },
      {
        "id": "o7kh98q",
        "score": 1,
        "body": "I dont think it will apply to my case since i just got approved and they are transfferint my case to new vrc right?"
      },
      {
        "id": "o7koy18",
        "score": 1,
        "body": "I'm in Oregon and my case manager is in Alaska now since the local guy retired."
      },
      {
        "id": "o7kp773",
        "score": 1,
        "body": "Did you have to repeat orientation and initial vrc again?"
      },
      {
        "id": "o7kpdxo",
        "score": 1,
        "body": "No, but I'm already taking classes."
      },
      {
        "id": "o7kpi8z",
        "score": 1,
        "body": "Im going to washington state. I hope the vrc are cool there"
      },
      {
        "id": "o7kqgao",
        "score": 1,
        "body": "You'll probably have the same counselor as me. If you want I can dm you their contact info."
      },
      {
        "id": "o7kqome",
        "score": 1,
        "body": "Is yours in seattle regional office?"
      },
      {
        "id": "o7kr1gh",
        "score": 1,
        "body": "My counselor was Portland based, not sure."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rffgyv",
    "title": "3M DPP result",
    "body": "Context, younger, multiple deployments, So, back in 19, I signed up, I went deferred, and have waited, in total my settlement will be about $800k. It\u2019s interesting how they rate the scoring system, if you\u2019re under 30 you get a multiplier that increases your points and older folks get a divider that reduces it because of their more advanced age. Points are expected to have a final value of 8-10k each.\n\nI only am posting this, because a majority made jokes about $5 and a ham sandwich. And how it was a scam. And because of those guys, who made the jokes and didn\u2019t sign up, the payout was bigger. TYFYS",
    "flair": "Discussion",
    "score": 25,
    "comment_count": 27,
    "created_at": "2026-02-26T16:53:19+00:00",
    "top_comments": [
      {
        "id": "o7jqbvl",
        "score": 11,
        "body": "I didn't even hear about it lol\n\nNo pun intended"
      },
      {
        "id": "o7kal3l",
        "score": 8,
        "body": "Dang they only gave me 10k and took half"
      },
      {
        "id": "o7jwku2",
        "score": 7,
        "body": "All I saw were spam ads in Facebook. I assumed it was some BS ambulance chasing scheme. Turns out it was legit. Dang."
      },
      {
        "id": "o7jkceh",
        "score": 7,
        "body": "Damn that's actually solid money, congrats on sticking with it when everyone was clowning around about ham sandwiches. The age multiplier thing is wild tho - makes sense they'd weight it heavier for younger vets who got more life ahead of them to deal with the effects"
      },
      {
        "id": "o7nxjle",
        "score": 5,
        "body": "It\u2019s not that it was turned down, they just had an alternate option,  EPP do expedited single payments, or wait it out for essentially a structured settlement with a single payment every October 2025-2029"
      },
      {
        "id": "o7kh5eb",
        "score": 4,
        "body": "I got $24k, thought that was a good payout. Sorry about your hearing bro."
      },
      {
        "id": "o7kiji6",
        "score": 4,
        "body": "Former arty guy here. Did year tour during Afghan surge in 2010. Cant hear shit. I only got 7k. \n\nNot sure how you swung 800k, I feel hosed lol. Congrats nonetheless."
      },
      {
        "id": "o7jqf8y",
        "score": 3,
        "body": "You got $800k in payout? That\u2019s crazy"
      },
      {
        "id": "o7ml3ex",
        "score": 3,
        "body": "I thought the lawsuit settlement was over years ago? And you couldn't pursuit this anymore ?"
      },
      {
        "id": "o7kw9wz",
        "score": 3,
        "body": "Deafness in the 20s isn\u2019t all that bad. More focus \ud83d\ude05"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rffdti",
    "title": "Update on Arizona Veterans getting property taxes exemptions",
    "body": "early this year, the house passed a bill to remove the income cap for 100% disabled veterans for property taxes exemptions for bill 2792.\n\n  \nthe bill was signed feb 2026. The final bill can be seen here: [https://legiscan.com/AZ/text/HB2792/2026](https://legiscan.com/AZ/text/HB2792/2026)\n\n  \nif you scroll down to section H, you\u2019ll see that they voted to keep the income cap restriction. so what unanimously passed in the house to remove the income cap ended up keeping it, effectively changing jack shit for veterans in AZ. ",
    "flair": "Article/News",
    "score": 22,
    "comment_count": 18,
    "created_at": "2026-02-26T16:50:04+00:00",
    "top_comments": [
      {
        "id": "o7k42e3",
        "score": 10,
        "body": "Here is the latest Bill 1365 to remedy this, its past the house and on to the AZ senate.\n\n[https://www.azleg.gov/videoplayer/?eventID=2026021089&startStreamAt=6844](https://www.azleg.gov/videoplayer/?eventID=2026021089&startStreamAt=6844)\n\nThe bill 1365 starts at the 1:54:14 mark."
      },
      {
        "id": "o7l2cfc",
        "score": 9,
        "body": "She\u2019s implying that if a veteran is a \u201cmillionaire\u201d or well off they shouldn\u2019t benefit from this tax break. Shes not understanding the principles to that. If that\u2019s the case then wealthy veterans shouldn\u2019t get disability income or benefits. Little does she know a majority of veterans who made something out of them selves because THEY COULD would trade away their net worth to go back to health they were prior service. I understand what she\u2019s trying to get at\u2026. But really how many 100% disabled veterans are in the state of Arizona are multi millionaires\u2026 and if they are good for them. They more than likely earned it the hard way. I don\u2019t know a single millionaire who made money off their disability only. \n\nSorry I had to rant that pissed me off."
      },
      {
        "id": "o7k7m78",
        "score": 6,
        "body": "Holy SHIT this is clutch. Let\u2019s see if they fake us out again. The gentleman explaining it to that dumbass crooked witch in the green was everything here.\u00a0"
      },
      {
        "id": "o7ka76y",
        "score": 6,
        "body": "Facts... She complains on any thing good for Veterans it seems!\n\nEVERYONE Needs to call, email, and keep pinging our Representatives !"
      },
      {
        "id": "o7juli7",
        "score": 5,
        "body": "It\u2019s around 34k a year w/o dependents and 42k a year with dependents.\u00a0"
      },
      {
        "id": "o7q0wds",
        "score": 4,
        "body": "Bill 1365 is in process to remove it. Fingers crossed"
      },
      {
        "id": "o7ofoxo",
        "score": 3,
        "body": "Well hopefully something passes to remove the income cap"
      },
      {
        "id": "o7jzi8r",
        "score": 2,
        "body": "I'm sure with a good accountant a millionaire can get that declarable income low enough.\u00a0"
      },
      {
        "id": "o7kr47p",
        "score": 1,
        "body": "The bill we need is AZ HB2973 2nd session, since AZ reuaea bill numbers.  https://apps.azleg.gov/BillStatus/BillOverview/85197"
      },
      {
        "id": "o7zxt5h",
        "score": 1,
        "body": "We took the same oath. Don\u2019t be a hater."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rfd31u",
    "title": "Looking for veteran friends in Arkansas",
    "body": "I live in central AR and am looking for other veterans that are 100% or tdiu that also gets tired of being alone all day. I always felt a better connection to other veterans than others.",
    "flair": "Discussion",
    "score": 13,
    "comment_count": 7,
    "created_at": "2026-02-26T15:26:20+00:00",
    "top_comments": [
      {
        "id": "o7k17rd",
        "score": 5,
        "body": "100% here. Central Arkansas. What are you into?"
      },
      {
        "id": "o7knwvp",
        "score": 3,
        "body": "Not in Arkansas but this post is sweet. I\u2019m in Indianapolis, Indiana and I feel what you\u2019re saying!"
      },
      {
        "id": "o7kou1y",
        "score": 2,
        "body": "Volunteering at your local CBOC or VAMC is a good way to get out of the house and interact with other veterans."
      },
      {
        "id": "o7ms4dw",
        "score": 2,
        "body": "I'm east of Little Rock so probably not central"
      },
      {
        "id": "o7msi3t",
        "score": 2,
        "body": "I need to do something!!!"
      },
      {
        "id": "o8khhiv",
        "score": 1,
        "body": "Dude sorry for the late response. I haven't been on here much but insomnia is a mf which ultimately lead me back lol. I sometimes game (sports usually) but honestly I enjoy watching sports and exploring the outdoors. I'm a big food enthusiast! I like older country and rock music. Rap is alright ig kinda screws w my mind though. I like to hit the AGFC gun range every once in a while. Fishing, hunting are both hobbies I like. Unpopular opinion but I like gardening, building new things. Sometimes when I get just super bored I'll find some random blueprint and build it. Im in my 20s"
      },
      {
        "id": "o8leyfn",
        "score": 1,
        "body": "No problem at all! We all have lives! \n\nI'm not allowed to touch firearms anymore, but there's a lot to do. We have some veteran's that play hockey at the Skatium in Little Rock. I just started a book club as well, we're on our third months, and I think there's at least 3 veterans in that group. Feel free to shoot a message if you want. "
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1reyngg",
    "title": "VR&E Ch 31",
    "body": "Hello all! \n\nI\u2019d like to know everyone\u2019s experience with trying to get education through them. I\u2019m honestly struggling with figuring out how to prove my disability hinders any job i can get? if i prove my disability hurts working then how can i prove education will help me work. i don\u2019t get it. ",
    "flair": "VR&E - Voc Rehab Veteran Readiness",
    "score": 3,
    "comment_count": 13,
    "created_at": "2026-02-26T03:00:06+00:00",
    "top_comments": [
      {
        "id": "o7gsz29",
        "score": 3,
        "body": "I would apply to use VR&E first rather than GI bill. Don\u2019t expect much from the program because 97% of counselors are useless"
      },
      {
        "id": "o7kuau9",
        "score": 2,
        "body": "i have my second appointment in 2 weeks! i\u2019ve heard the same thing :)"
      },
      {
        "id": "o7mq3k8",
        "score": 2,
        "body": "that\u2019s what i\u2019m going for!"
      },
      {
        "id": "o7wp7g2",
        "score": 2,
        "body": "thank you so much for both of your help :) my appointment is next week and i\u2019m glad to hear your guys\u2019 experience with it"
      },
      {
        "id": "o7kn917",
        "score": 1,
        "body": "Navigating the VR&E process can feel like a maze sometimes. When I went through it, I found that focusing on how my disability impacted my daily life and work capabilities really helped clarify things for the counselors. They want to see a clear connection between your limitations and how education can bridge that gap.\u00a0  \n  \nIt\u2019s all about showing that the skills you gain from education can help you overcome the barriers your disability presents. Just keep pushing through and don\u2019t hesitate to lean on your fellow veterans for support. You\u2019re not alone in this."
      },
      {
        "id": "o7lmk4q",
        "score": 1,
        "body": "My experience was great. Just graduated with a BS in biz mgt."
      },
      {
        "id": "o7rte3o",
        "score": 1,
        "body": "Here's my history.\n-Machine gunner in a line platoon\n\n-Used some of my GI bill to go through a carpenters apprenticeship\n\n- applied to VR&E\n\n- my previous back, knee, ankle, shoulder injuries made it so I could no long stay gainfully employed as a carpenter. \n\n-applied for VR&E for essentially a desk job that required a degree, currently halfway to said degree."
      },
      {
        "id": "o843klv",
        "score": 1,
        "body": "Easy. You work construction, which makes your conditions worse.  VRE helps you get an accounting degree so you can work without hurting yourself more"
      },
      {
        "id": "o7kudll",
        "score": 1,
        "body": "thank you so much"
      },
      {
        "id": "o7rx5lk",
        "score": 1,
        "body": "congrats dude! thank you also for your help. that makes a lot more sense"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1reyet4",
    "title": "How do I get my father in law involved in his local non-alcohol-centric veterans community?",
    "body": "Active duty asshole Navy SWO asking on behalf of a fellow former Navy SWO father in law. \n\nHe\u2019s a 65 year old ass and has taken a big turn recently, working out plus stopped drinking. I\u2019m hoping to find places for him to be productive and social. Where do we start? He qualifies for the VFW and other veterans groups, but they tend to basically be glorified drinking clubs. Just looking for any leads.",
    "flair": "Question/Advice",
    "score": 11,
    "comment_count": 10,
    "created_at": "2026-02-26T02:49:02+00:00",
    "top_comments": [
      {
        "id": "o7g635l",
        "score": 8,
        "body": "We love having veterans volunteer at the USO!\n\nwww.uso.org/volunteers"
      },
      {
        "id": "o7g7owt",
        "score": 8,
        "body": "I quit drinking 10 years ago. I used to have buddies stopping by all the time. Now, no one shows up or asks me to do anything. I haven't found any local social clubs, but I have found a new hobby that keeps me pretty busy. At 52, I decided to have another kid. Now I visit with doctors, the daycare lady, and all the ladies at the local Walmart think she's adorable. USO volunteer should have been my first choice \ud83d\ude06"
      },
      {
        "id": "o7g6mra",
        "score": 7,
        "body": "He\u2019d actually love this. I don\u2019t know why I didn\u2019t think about this lol. He gets to give people snacks + bitch to people who have nowhere else to be about the state of the military. He might be your best volunteer\u2026"
      },
      {
        "id": "o7jopvb",
        "score": 5,
        "body": "At the VA im at there is a program thats called healing waters where you get taught how to make flies and rods for fly fishing. Its mostly vets with a few spouses mixed in."
      },
      {
        "id": "o7ircnj",
        "score": 5,
        "body": "Lmfao I love the animosity. It pleases me."
      },
      {
        "id": "o7ikmwr",
        "score": 3,
        "body": "Many of the VFW / AmLegions are drinking clubs. A few do a service side. You could try going to a few with him to navigate around the drinking parts and help steer him into the self service side of the organizations. Some posts do it better than others. \n\nActive-peace\u2019s recommendation for the USO is a really good idea that I hadn\u2019t considered."
      },
      {
        "id": "o7iy5u5",
        "score": 2,
        "body": "Is he in AA? Not military-related, of course, but I've met people who spend much of their time in AA-related stuff. Many vets too."
      },
      {
        "id": "o7l6kps",
        "score": 2,
        "body": "If he lives close enough, he can volunteer at the local VA hospital or clinic. I've been doing it for over 15 years and it keeps me off the streets."
      },
      {
        "id": "o7gupuo",
        "score": 2,
        "body": "You crazy than I.  I wish you all the luck. I  had my last one at 29.  Happy for the empty nest now."
      },
      {
        "id": "o7nwci8",
        "score": 1,
        "body": "Wounded Warrior Project is a good place to look at. They put on events all the time. They aren\u2019t in every area but they are in a lot of places."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rey7aw",
    "title": "Did anyone attend the Marines reenlistment meeting today? Any notes to share?",
    "body": "I missed the meeting, I lost track of time driving my kid home from practice. \n\nIf anyone has any slides or points they made that\u2019d be great. \n\nYes I know it\u2019s a trap but the economy sucks sue me. ",
    "flair": "Question/Advice",
    "score": 39,
    "comment_count": 75,
    "created_at": "2026-02-26T02:39:45+00:00",
    "top_comments": [
      {
        "id": "o7h1l03",
        "score": 98,
        "body": "Yeah, be on the grinder with glow belts at 0630 for PT. RAHHHHH. \n\nAlso, you have duty this weekend."
      },
      {
        "id": "o7hta7c",
        "score": 81,
        "body": "You spelled Grindr wrong"
      },
      {
        "id": "o7gpq0j",
        "score": 67,
        "body": "Fool me once shame on you.\n\nFool me twice for a cushy shore duty command close to where I was originally going to go to college anyways, shame on me."
      },
      {
        "id": "o7hty0j",
        "score": 60,
        "body": "Would have been funny if a bunch of vets joined just to crash it and bust their balls with dumb questions \ud83e\udd23"
      },
      {
        "id": "o7hcov6",
        "score": 46,
        "body": "Hahahaha. ^no"
      },
      {
        "id": "o7gq4qc",
        "score": 37,
        "body": "The beatings will continue until morale improves. \n\nOh, and no more free crayons, so the beatings will probably continue indefinitely."
      },
      {
        "id": "o7i4lpd",
        "score": 32,
        "body": "You don't miss is. It's called Stockholm Syndrome lol"
      },
      {
        "id": "o7ie9ky",
        "score": 31,
        "body": "Fuuuuuuck no. I wouldn't serve these assholes who are hellbent on gutting our benefits and eroding any goodwill we've had with longstanding allies."
      },
      {
        "id": "o7h340f",
        "score": 26,
        "body": "I miss it sometimes. Not quite THAT bad tho \ud83d\ude02"
      },
      {
        "id": "o7gxhu2",
        "score": 23,
        "body": "When I was getting out I saw a retention poster with a close up of a uniform and it said \u201cBefore you take it off, think about how well it fits.\u201d\n\nYou do what you have to do - the green weenie provides. However, before you put it back on, think about why you took it off. Be sure to check out USA jobs.gov too. Your prior service will give you an edge.\n\n\u00a0And just for fun, here is [The EAS Song](https://m.youtube.com/watch?v=RoxdT2xhra8&pp=0gcJCY4Bo7VqN5tD).\n\n"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1remk3e",
    "title": "Finally going to use college benefits, but idk what degree/career track. Why does planning my life stress me out?",
    "body": "Hi, I've been out 4.5 years and I REALLY need to take advantage of my VR&E (I'm 100% P&T) and Post 9/11. But I loathe the idea of going back to school. I did a semester of community college pre-Army and then I did some college with AMU between 2016-2018. At one point, I had enough credits from Army (JST and MOS schools/courses) and college that I was maxed on electives and like 80% done with GenEd for a Bachelors. If I applied these credits to Cochise College, I'd be a few classes shy of an AA. I know, I know, just finish it! I'm just unmotivated to go back to school. I've been contracting in SIGINT with the Army since I ETSed with just my clearance and experience and make 6 figures.  \nDon't get me wrong, I love still being part of the Army and Intel community, but I can't decide if this is a lifelong path for me. On one hand, I'd be dumb to part ways as it's clearly worked out for me and an easy paycheck. On the other hand, I'm also tempted to branch out and do something I guess \"easier/simpler\" and with more flexibility (as far as vacation time because I love to travel when I can), like becoming a teacher.  \nMy husband is still active duty and has 6 years left until retirement. I don't know, I kind of selfishly want to move on from government work just so I can enjoy more of life with him. He has so much use or lose and clearly I don't get that same PTO time. But I do also selfishly enjoy an extra paycheck (on top of VA).  \nAnyways, I'm considering using my VR&E to finish my bachelors in Intel Operations at UofA and maybe using my Post 9/11 for a teaching degree. Does an intel degree even matter at this point? I have to consider too what happens if we PCS to a place that I can't find a SIGINT job?\n\nSide note: people are going to ask things like \"well what are your hobbies or what do you like to do?\" I'm sorry, I honestly couldn't tell you a variety of things I'm interested in. My hobby is traveling and I actually genuinely enjoy researching travel deals, locations, etc. (I've considered travel agent, it's a very competitive industry.)\n\n\\~\\~\\~\\~\\~\\~\\~\\~\\~\\~\\~\n\n**TL;DR:** Need to use VR&E and Post 9/11 GI Bill. Should I consider sticking in current career field (based on familiarity and current economy) or should I branch out into different paths?\n\n\\*\\*High key wish they'd just give me even half the money they'd spend to send me to college. Then I'd just stay in intel.",
    "flair": "Question/Advice",
    "score": 7,
    "comment_count": 14,
    "created_at": "2026-02-25T19:06:26+00:00",
    "top_comments": [
      {
        "id": "o7dsc2k",
        "score": 5,
        "body": "Just go travel.\n\nCollege can wait u r literally 100% p&t.\n\nYou will only break down ever further as time goes. \n\nGo \ud83d\udc4f and \ud83d\udc4f travel \ud83d\udc4f"
      },
      {
        "id": "o7ecsiz",
        "score": 5,
        "body": "Imo keep your job and save your benefits until you\u2019re sure you know what you want. Try traveling with your current schedule."
      },
      {
        "id": "o7e73dq",
        "score": 5,
        "body": "oh yikes. then i need to use it asap if that's the case. i'll research it now.\n\nUpdate: straight from va. gov\n\n**If your service ended before January 1, 2013,**\u00a0your Post-9/11 GI Bill (Chapter 33) benefits will expire 15 years after your last separation date from active service. You must use all of your benefits by that time or you\u2019ll lose whatever\u2019s left.\n\n**If your service ended on or after January 1, 2013,**\u00a0your benefits won\u2019t expire thanks to a law called the Forever GI Bill - Harry W. Colmery Veterans Educational Assistance Act.\u00a0\n\n  \nLooks like I'm good."
      },
      {
        "id": "o7egfuj",
        "score": 2,
        "body": "As a fellow siginter in a similar VA situation that has separated from the army and is also married to a spouse that is still active duty, it\u2019s nice to meet you \ud83d\udc4b\n\nI can attest that I also loathe school, always have, always will, yet I\u2019m currently working on my masters in cybersecurity technology because benefits and because it aligns with my experience in SIGINT with a broader application outside of just government work. I have a bachelors in business administration and some cyber certs and this degree is what I am adding to my resume to prepare for future opportunities in a leadership or analytic role at some point in the future. Rn I enjoy being a stay at home student/veteran/husband/dad.\n\nAs far as being a travel agent, that sounds fulfilling. Sounds like you\u2019d enjoy it. The boots 2 business program may be able to help point you in the right direction. It could look like pursuing a bachelors in entrepreneurship to learn and prepare for your travel agent business and get paid to learn as you go.\n\nI\u2019m happy to be a sounding board if you want to continue the thought train."
      },
      {
        "id": "o7ek26k",
        "score": 2,
        "body": "I used my VR&E for my 2nd degree and just kinda took my time.\nI rushed right into my 1st degree after getting out and I super struggled. I got on academic probation twice. Had a to take a couple semesters off to get my shit together. It got to the point I was paying kids to do my homework.\n\nFast forward 15yrs later\u2026I had a deeper appreciation for school. It was a breeze for me. I took my time. Dove in deep with doing the course work, granted this degree was way easier, but it just felt more satisfying.\n\nNow ive 2 pretty pieces of paper saying i went to school, while my current job wouldnt of happened if it werent what i learned in the military but life is just odd that way.\n\nif you have an established career, maybe just do as everyone says and travel.\nbut if you want to pursue another career or career expand on what youre at, go to school while you have to time to earn that salary potential."
      },
      {
        "id": "o7f5uq0",
        "score": 2,
        "body": "SIGINT is only really in the handful of locations with those buildings. \n\nIf you're unsure if you want to leave, I'd recommend keeping the job and going to school part time until you either discover what you want your new career to be or finish the necessary degree to move up in the IC. \n\nWhen I got out, I never wanted to see a SCIF again, but plenty of friends still in the biz. Just gotta figure out what makes sense! \n\nOh, and whatever career you think you want to do, find people who actually do it and speak to them. Understand which companies in that field you'd like to work for, where they are, and if they have any preferred university programs."
      },
      {
        "id": "o7lcszl",
        "score": 2,
        "body": "So let's me ask this. Why are you working? And that's a serious question. It's not a suggestion that you shouldn't be? It's a question that I want you to seriously answer for yourself. What is it that keeps you working.? \n\nYou could be doing it just because you think you should be. Okay. That's a reason. I don't think it's a good one but it is a reason. \n\nFinding your right path isn't magic. And the first part I suggest is discussing with yourself why you're doing what you're doing now. If you had that genie in a bottle pop up and they gave you the magic wish that said what would you do differently to be happier more satisfied with your life. It's important that the answer you find for yourself is important to you. Not to anyone else. If your answer is I'm doing this because fill in the blank thinks I should then you need to question if that's not the source of your problem. \n\nYou've had service time and you've reached a point in your life that perhaps you just need to try and focus on what you want to do. What will make you satisfied. What if you were doing it would make you feel accomplished, what would make you feel like you were doing things that suited you? \n\nYes these are annoying questions. So the idea that you have to use your education benefits and you really admittedly not motivated to do so should be telling you something. There's a conflict. You need to look closely at that. \n\nI always found when doing this exercise and I used to do it quite frequently is pencil and paper. You need something physical, ask yourself why am I doing what I'm doing? And if you're not doing something because that's what you want to be doing you really need to ask yourself why? And then of course when you find out you're doing everything because everyone else expects you to be doing it comes the hard part of disappointing people's expectations. But fulfilling your own."
      },
      {
        "id": "o7dw5if",
        "score": 2,
        "body": "I totally agree with you. I'm 34 and we don't have kids, so we have the ability to travel. But then let's say we do a couple big trips a year. Then what? I mean I guess I just go to school for something outside of intel?  \n  \nAlso, Isn't there a time limit on the VR&E and GI bill? "
      },
      {
        "id": "o7ioq3s",
        "score": 2,
        "body": "I honestly didn't intend to come back into this realm. I just got bored on terminal leave and it was easy to jump back into lol. My first contracting job was a DCGS trainer and I didn't have a lick of DCGS experience, I got hired because of my clearance. And now I'm in a position that is basically what my MOS was, so it's worked out. "
      },
      {
        "id": "o7ipovs",
        "score": 2,
        "body": "Right on, there are also lots of defense/ aerospace/ cyber companies that value an active clearance. So if there's something in that vein you'd be interested in that's another option. But I'd still recommend working whatever minimum amount is necessary at your current job to maintain the clearance and go to school part time if possible. \n\nI interned at a company a few years after I got out while in school but my clearance had gone inactive because I'd been read out for two years, even though my poly was still valid."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1remg7t",
    "title": "Service dog",
    "body": "How do I get my dog registered as a service dog? Does the VA cover this? ",
    "flair": "Question/Advice",
    "score": 5,
    "comment_count": 21,
    "created_at": "2026-02-25T19:02:39+00:00",
    "top_comments": [
      {
        "id": "o7dnids",
        "score": 13,
        "body": "To get a dog certified for VA service dog benefits, you must have a service dog trained by an organization accredited by\u00a0[Assistance Dogs International (ADI)](https://assistancedogsinternational.org/)\u00a0or the International Guide Dog Federation (IGDF). The VA does not train or certify dogs directly, but covers veterinary care for dogs that assist with mobility, hearing, or mental health conditions (like PTSD).\n\n"
      },
      {
        "id": "o7do1uk",
        "score": 10,
        "body": "No such thing as a service dog registry. You can train your dog to provide a service. According to ADA, they have to provide a service (i.e. sight, epilepsy warning, touch/pressure for PTSD flairs) and be well-behaved in public. PTSD is so iffy because it can skirt the line of requiring a service dog or an ESA. And most people actually just have an ESA that they want to hug and slap a vest on it and call it an SD, but a service dog should actually be working, as in if you start having a PTSD episode, your dog should be able to provide pressure point therapy or like sit on you to calm you down.   \nAll that to say, there's no registration, but if you do need it to be able to live places or like go to Disney for instance, then you do typically need a doctors letter. Which I've found impossible to get through a VA provider. "
      },
      {
        "id": "o7dq32q",
        "score": 5,
        "body": "Then you need the ESA letter"
      },
      {
        "id": "o7dna29",
        "score": 3,
        "body": "What training has your dog gone through to be certified as a service dog?"
      },
      {
        "id": "o7fgb0a",
        "score": 3,
        "body": "\"Is your dog trained to perform a specific task to assist you?\"\n\n\"What specific task is your dog trained to perform?\"\n\nGeneral emotional support doesn't count. They would have to be trained to sense an oncoming panic attack or scout the room ahead of you to alleviate your PTSD or something like that. If your dog is not trained to perform a specific task, they are not a service dog, and you shouldn't refer to them as such. At that point, they are an emotional support animal and do not have the same general legal protections that a service dog does."
      },
      {
        "id": "o7dqpcb",
        "score": 3,
        "body": "VA doesn\u2019t pay for training of service dogs. VA does give grant money to nonprofits who train service dogs. Your PCM can only recommend you get a service dog. https://www.prosthetics.va.gov/ServiceAndGuideDogs.asp"
      },
      {
        "id": "o7dsv37",
        "score": 3,
        "body": "I'm not saying you're wrong, I just find that crazy you're having a hard time finding an apartment that won't allow a 12lb dog. Unfortunately, I think in this case, you're going to have to find a community care doc that can help you. I've been told that the VA won't do letters for SDs or ESAs because they don't want to be held liable if your animal is actually a demon. "
      },
      {
        "id": "o7f3vvv",
        "score": 2,
        "body": "Since you haven\u2019t mentioned anything abut a disability, you are probably  looking for help on getting documentation for an emotional support animal"
      },
      {
        "id": "o7kc7ia",
        "score": 2,
        "body": "There's no service dog process to pass. Unless a dog is bred and highly trained by an organization who provides services dogs and passes that organizations process. Other than that, there is not an actual service dog registry or certification. You can quite literally train your own dog to be a service dog. I have two dogs that actually provide me pressure therapy for PTSD panic attacks and I didn't even train them on it. However, one of them is not the best on the leash, she pulls a lot and is very curious and excited in public and the other is a 120lb Saint Bernard and like good luck getting a VA doctors letter stating she provides a service (I've always been told the VA won't do this because of liability). So I don't bother with it because I didn't train them to work for me. They're just ESAs at this point."
      },
      {
        "id": "o7hfxjw",
        "score": 2,
        "body": "In California, they can't even deny an Emotional Support animal, which is not a Service Animal, which does require training and certification. All I had to do was to get my VA doctor to write a letter stating that I need an emotional support animal, and that covers the California legal requirements. "
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1remeai",
    "title": "Children\u2019s education benefits",
    "body": "I am 100% T&P under unemployability, I have one child almost through his freshman year in college and another about to start college. I was deployed but my Gi bill lapsed. What benefits are available for my children to use for college? ",
    "flair": "Question/Advice",
    "score": 4,
    "comment_count": 15,
    "created_at": "2026-02-25T19:00:56+00:00",
    "top_comments": [
      {
        "id": "o7dmq8t",
        "score": 7,
        "body": "Each of your dependents is eligible for their own 36 months of DEA CH 35. Your disability award letter should have informed you of this program. \n\nEach dependent who is 18 or older must submit their own application at va.gov. The veteran doesn\u2019t apply.\n\nThe child who is in their freshman year should be eligible for backpay for this and the previous semester."
      },
      {
        "id": "o7dmiuj",
        "score": 4,
        "body": "Look at chapter 35 benefits"
      },
      {
        "id": "o7dvz8d",
        "score": 4,
        "body": "They\u2019re both registered as my dependents through the VA so can they just go on VA.gov and make accounts using their SSN ?"
      },
      {
        "id": "o7ewx7k",
        "score": 3,
        "body": "Chapter 35 benefits. SOME STATES HAVE TUITION WAIVERS AS WELL. They usually only apply if your child is going to college in the same state that you are a resident of. (In state schools)"
      },
      {
        "id": "o7dt3ss",
        "score": 3,
        "body": "Some colleges in california and elsewhere give free education to your kids as well\n\n as long as u r rated even 0%"
      },
      {
        "id": "o7dxc2p",
        "score": 3,
        "body": "Yup"
      },
      {
        "id": "o7g8077",
        "score": 2,
        "body": "Here is a list i compiled of states that offer free tuition to dependents and vets.\n\nNot updated to include any 2025 changes yet though.\n\nhttps://www.veteransbenefitskb.com/free_tuition"
      },
      {
        "id": "o7dkdyu",
        "score": 1,
        "body": "'Have you looked in the **[Wiki]( https://www.reddit.com/r/Veterans/wiki/education)** for an answer? We have a lot of information posted there. \n\nTo contact VA Education, 1-888-442-4551, for ~~Voc Rehab~~ VR&E (Veteran Readiness and Employment Program) assistance with appointments or problems with your Case Manager (not for missing payments): 1-202-461-9600. \n\n**Payments for certain education benefits (DEA, VEAP) are paid at the end of the month you attend school - Department of Treasury issues these payments **using a 10 business day window** - these payments are not locked into a specific day of the month like VA disability/military pay is**. For Voc Rehab missing payments, contact your Case Manager or your local **[VA Regional Office](https://www.knowva.ebenefits.va.gov/system/templates/selfservice/va_ssnew/help/customer/locale/en-US/portal/554400000001018/content/554400000260849/VRE-Officers-and-Contact-Information)\n\nFor Post 9/11 GI Bill only, If you signed up for direct deposit when you applied for education benefits, **we\u2019ll deposit your payment into your bank account 7 to 10 business days after you verify your school enrollment.** This is the fastest way to receive your payment. [Text Verification FAQ](https://benefits.va.gov/GIBILL/docs/IsaksonRoe/EnrollmentVerificationFAQs.pdf)\n\nMGIB and MGIB-SR and DEA CH 35 have to do [monthly verification](https://www.va.gov/education/verify-school-enrollment/) and you should receive the payment within 3 to 5 business days.\n\nFor Online Only training, the Post 9/11 GI Bill is currently **(1 August 2025) paying $1169.00** for those who started using their Post 9/11 GI Bill on/after 1 January 2018 - this is based on 1/2 of the National Average BAH paid to an E5 with dependents. Post 9/11 GI Bill MHA rates are adjusted 1 August of each year and are based on the 1 January DoD BAH rates for that year - **so VA can't use 1 January 2025 BAH rates until 1 August 2025** - for those who started training on/after 1 January 2018, the MHA rates are 95% of the DoD BAH rates. First possible payment for the 1 August 2025 increase is 1 September.\n\nFor VR&E, there are two different Subsistence Allowance programs - https://www.benefits.va.gov/vocrehab/subsistence_allowance_rates.asp The P9/11 Subsistence Allowance is based on the BAH paid to an E5 with dependents. Those who started using VR&E on/after 1 January 2018 receive 95% of the BAH paid to an E5 with dependents. **As of 1 January 2026 Online only students using VR&E are being paid $1198.00** if they started using VR&E on/after 1 January 2018. The CH31 Subsistence Allowance rates are adjusted 1 October each year by Congress.\n\nVA Education is going paperless - make sure VA has a current email address for you. Please make sure you add Veteransbenefits@messages.va.gov to your contacts list so that you don't miss important updates from VA.\n\n[VA Award Letter explanation](https://benefits.va.gov/gibill/understandingyourawardletter.asp)\n\n[Contact a VR&E Supervisor](https://www.knowva.ebenefits.va.gov/system/templates/selfservice/va_ssnew/help/customer/locale/en-US/portal/554400000001018/content/554400000260849/VRE-Officers-and-Contact-Information)\n\n [VA Rudisill Decision](https://benefits.va.gov/gibill/rudisill.asp) - some veterans may qualify for an additional 12 months of a second GI Bill based on serving two or more different periods of active duty service.\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Veterans) if you have any questions or concerns.*"
      },
      {
        "id": "o7dkwrg",
        "score": 1,
        "body": "[removed]"
      },
      {
        "id": "o7h6vzi",
        "score": 1,
        "body": "This op see what state benefits your kids can get. California dependents can get tuition waived for state schools."
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rejf9e",
    "title": "Weird call from the VA",
    "body": "I live in Alaska I\u2019ve lived in Alaska for the last 20+ years. This morning my wife got a call, asking for me, from the Poplar Bluff VA in Missouri wanting to schedule me an appointment. Other than basic training, I\u2019ve never been to, or lived in MO. \n\nAnyone else get a weird call like this? Is this some kind of phishing scam? ",
    "flair": "Question/Advice",
    "score": 22,
    "comment_count": 11,
    "created_at": "2026-02-25T17:19:34+00:00",
    "top_comments": [
      {
        "id": "o7dajcd",
        "score": 31,
        "body": "I work for VA @ Poplar Bluff MO.  Never underestimate the ignorance of their consolidated call center staff"
      },
      {
        "id": "o7czie4",
        "score": 11,
        "body": "In Michigan I've had calls from Cleveland because they were responsible for scheduling radiology at my local VA. \n\nIn Arizona I'd get notices from New Mexico because they were remote reading the eye scans taken at the Tucson AZ hospital."
      },
      {
        "id": "o7isfeg",
        "score": 8,
        "body": "Your mileage claim is gonna kick ass!"
      },
      {
        "id": "o7d05xz",
        "score": 3,
        "body": "Dude to double check just check your appointments in the app or website\n\nIf you have nothing don\u2019t pick up of talk to them"
      },
      {
        "id": "o7m34bc",
        "score": 3,
        "body": "\ud83d\udc80"
      },
      {
        "id": "o7era2x",
        "score": 2,
        "body": "This has happened to me as well. It was legit. They were taking the overloads and scheduled me for a visit at my local office,"
      },
      {
        "id": "o7g5mlk",
        "score": 1,
        "body": "You get calls from the VA?  The closest VAMC(not local) doesn't even answer the phone.  Just transfers to the Crisis Line."
      },
      {
        "id": "o7ie4zl",
        "score": 1,
        "body": "Closest I\u2019ve come is Colorado Springs calling me for an appointment. I live in Denver less than two miles from the regional VA."
      },
      {
        "id": "o7zhvfl",
        "score": 1,
        "body": "I had something similar, calling me from Charleston SC, even though I live almost at the NC border and my local clinics are assigned to the Columbia SC hospital system, AND I already had an appointment with a specialist that does the same thing they were trying to schedule me for."
      },
      {
        "id": "o7yg4f7",
        "score": 1,
        "body": "Its like the military....for people that hate their lives even more"
      }
    ]
  },
  {
    "subreddit": "Veterans",
    "id": "1rehtjj",
    "title": "DOD removed Burn Pit and Airborne Hazard webpages from Military Health website.",
    "body": "This link, that's still listed on the VA Burn Pit and Airborne Hazards page, just goes to a dead page now.  You would think the DOD would be smart enough to at least just change the page to a link that sends back to the VA if they don't intend to provide any sort of info for the veterans dealing with exposure related health issues anymore.  Makes me wonder if this is just a whoops or someone intentionally trying to make it harder for someone to get in to the registry and look for info about issues they are dealing with that may also want to do a future PACT Act claim of some sort.\n\n[https://health.mil/Error?item=%2fmilitary-health-topics%2fhealth-readiness%2fenvironmental-exposures%2fva-airborne-hazards-and-open-burn-pit-registry&user=Undefined&site=website](https://health.mil/Error?item=%2fmilitary-health-topics%2fhealth-readiness%2fenvironmental-exposures%2fva-airborne-hazards-and-open-burn-pit-registry&user=Undefined&site=website)\n\nEdit: appears in the last few years enrollment became automatic so its possible with that change the original DOD Health page was no longer needed. Thanks u/4RTKBA for that info. ",
    "flair": "Discussion",
    "score": 192,
    "comment_count": 19,
    "created_at": "2026-02-25T16:23:35+00:00",
    "top_comments": [
      {
        "id": "o7edx7u",
        "score": 19,
        "body": "Supposedly it is now automatic registration based on deployment records, and veterans no longer need to register on their own. No clue how that works out in reality, but I think that's the reason the registration page/info no longer exists."
      },
      {
        "id": "o7cudrr",
        "score": 13,
        "body": "No the other page had ways to get in to the registry and way more info but if thats new then I guess its better than nothing."
      },
      {
        "id": "o7cs7u9",
        "score": 11,
        "body": "[deleted]"
      },
      {
        "id": "o7cvaz0",
        "score": 9,
        "body": "Shocking."
      },
      {
        "id": "o7dzbqs",
        "score": 7,
        "body": "Given leadership's recent actions...\u00a0\u00a0"
      },
      {
        "id": "o7cvg3v",
        "score": 5,
        "body": "So strange that a location I deployed to is listed on this link even though at the time it was classified even deployment orders were to a different continent. We weren\u2019t even allowed to tell family where we were and now it\u2019s listed on that link.  Even two years ago when I was checking into burn pit info- I couldn\u2019t list the country I just had to point to a column and say yes or no when I asked if my actual location was in either of the columns."
      },
      {
        "id": "o7ek2cw",
        "score": 4,
        "body": "Interesting.  Hadn't heard that and we regularly have to send folks to the local VA coordinator to verify if they are in or not. Thanks for the heads up, going to be good going forward when we have folks come in to the office.\n\nJust looked for more info on auto-enrollment and found this.\n\n[https://newsroom.tricare.mil/News/Defense-Health-Agency-News/Article/3865888/burn-pit-registry-redesign-auto-enrolls-participants-and-simplifies-requirements#:\\~:text=Veterans%20and%20service%20members%20who,can%20opt%20out%20of%20participation](https://newsroom.tricare.mil/News/Defense-Health-Agency-News/Article/3865888/burn-pit-registry-redesign-auto-enrolls-participants-and-simplifies-requirements#:~:text=Veterans%20and%20service%20members%20who,can%20opt%20out%20of%20participation)."
      },
      {
        "id": "o7gbotq",
        "score": 3,
        "body": "Intentional , they have to add MRE's to the exposures lists \ud83e\udd23\ud83e\udd23\ud83e\udd23"
      },
      {
        "id": "o7eyghq",
        "score": 3,
        "body": "Yeah it was automatic for me"
      },
      {
        "id": "o7i84as",
        "score": 3,
        "body": "Last week I went to the VA for a checkup for the first time in several years.  On making the appointment they asked about burn pit exposure.  My Dr. also discussed it with me during the appointment asking where I was deployed.  A few days later I got a follow up call about scheduling a consultation for burn pit exposure.\n\nSo, from my experience, they seem to be more proactive about it."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1nttssi",
    "title": "A man of the people",
    "body": "Thank you for your service",
    "flair": "Headlines & News :rsz_21601:",
    "score": 9790,
    "comment_count": 945,
    "created_at": "2025-09-29T20:55:40+00:00",
    "top_comments": [
      {
        "id": "ngwbx7l",
        "score": 1570,
        "body": "If someone is out there blindly approving claims someone is also out there blindly denying them."
      },
      {
        "id": "ngwak1x",
        "score": 1020,
        "body": "Well, I know this staffer didn't get my claim..."
      },
      {
        "id": "ngwdku9",
        "score": 782,
        "body": "The guy denying them is employee of the month"
      },
      {
        "id": "ngwha41",
        "score": 370,
        "body": "Right, where's the article about the staffers who routinely deny good claims in the tens of thousands?"
      },
      {
        "id": "ngwbb7d",
        "score": 263,
        "body": "[deleted]"
      },
      {
        "id": "ngwffvi",
        "score": 234,
        "body": "If they\u2019re a senior VSR, that typically means they\u2019re the authorizer. He was the one who authorized the funds to be released. What he was supposed to be checking was that the funds were correct, the effective dates were correct, and that the claim was valid, among other things. Senior VSRs are not raters, so he likely had nothing to do with rating the claims. It would be near impossible for a rater to average four minutes a claim, even if they didn\u2019t do anything they were supposed to except for blind approving it. That means people are not likely to lose their rating. However, they may be required to pay back improperly authorized money, or have money withheld from their monthly benefits payments until the erroneously paid money is recouped."
      },
      {
        "id": "ngwgs2e",
        "score": 157,
        "body": "The guy that denied my other knee as secondary to my first knee"
      },
      {
        "id": "ngwa9iv",
        "score": 134,
        "body": "Better 100 undeserving people get benefits than one deserving person get denied"
      },
      {
        "id": "ngwmvia",
        "score": 115,
        "body": "Probably somewhere with the article about how some VA staffers were caught having an orgy on the clock"
      },
      {
        "id": "ngwdwtl",
        "score": 104,
        "body": "fade fine employ money airport subsequent offer memorize jar scale\n\n *This post was mass deleted and anonymized with [Redact](https://redact.dev/home)*"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1nbhzga",
    "title": "I feel seen",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 3225,
    "comment_count": 100,
    "created_at": "2025-09-08T08:14:28+00:00",
    "top_comments": [
      {
        "id": "nd2vut6",
        "score": 245,
        "body": "He is actually 21 and just finished their infantry contract."
      },
      {
        "id": "nd2cbrq",
        "score": 214,
        "body": "I love seeing older people have the courage to go back to school and accomplish things they previously thought would not happen because of age. \n\nI am in my 50's, and I take college classes all the time. Some of the younger people make fun of me, but that's ok. I probably would have done the same when I was 20. It took me 30 years to realize that it doesn't matter what other people think of my goals. They are my goals, not theirs."
      },
      {
        "id": "nd22vmu",
        "score": 211,
        "body": "![gif](giphy|1Qdp4trljSkY8)"
      },
      {
        "id": "nd38mpd",
        "score": 66,
        "body": "When I was in Uni back in 2016 there was a woman in her 60s in one of my classes. She was pretty u cool - very helpful too since she actually paid attention and took notes lol.\n\nShe said she retired and decided she wanted to be a lawyer, lol. Good for her \ud83d\udc4d"
      },
      {
        "id": "nd2nn4d",
        "score": 60,
        "body": "I\u2019d just ask for their mom or dad\u2019s (whichever way you swing) number and take them on a nice date, fuck them, and never call them back. The kid/young adult won\u2019t bother you after that."
      },
      {
        "id": "nd2v94u",
        "score": 54,
        "body": "Just graduated about 4 months ago. I am 52. I relate."
      },
      {
        "id": "nd2e73u",
        "score": 37,
        "body": "Wasn\u2019t as old, but definitely can relate."
      },
      {
        "id": "nd3nk4x",
        "score": 28,
        "body": "You\u2019re not alone. Same deal here. VR&E has given me an opportunity I never thought I\u2019d see again. \ud83d\ude4f\ud83c\udffe"
      },
      {
        "id": "nd250dh",
        "score": 27,
        "body": "![gif](giphy|l4HoeVtb6LMTRfJII)"
      },
      {
        "id": "nd2z3r0",
        "score": 23,
        "body": "In college again at nearly 40. I feel this."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1n5ozsi",
    "title": "For that special Veteran",
    "body": "I finally bought this for my best friend\u2026 cause he won\u2019t ever let me forget it\u2026 \u201cI know bro! You almost did what I did, got it.\u201d ",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 2872,
    "comment_count": 311,
    "created_at": "2025-09-01T13:40:22+00:00",
    "top_comments": [
      {
        "id": "nbu4kvy",
        "score": 462,
        "body": "Dude. My neighbor straight said, \"I would've joined the Marines too but I hate being yelled and I would have probably ended up in prison for kicking those drill sergeants asses.\"\n\n\ud83d\ude44... drill sergeants"
      },
      {
        "id": "nbu9hxx",
        "score": 260,
        "body": "I lost count of how many times I\u2019ve heard this."
      },
      {
        "id": "nbux12k",
        "score": 144,
        "body": "If I had a nickel for every time someone has told me this I wouldn't bother with the VA claim I'd be a rich man"
      },
      {
        "id": "nbu519a",
        "score": 117,
        "body": "Thank you for your almost service"
      },
      {
        "id": "nbvbq3b",
        "score": 115,
        "body": "I\u2019d still be poor, fuck talking to people \ud83d\ude02"
      },
      {
        "id": "nbuz8t7",
        "score": 93,
        "body": "Civilians think that boot camp is the hardest part of the military \ud83d\ude02"
      },
      {
        "id": "nbu8bnx",
        "score": 91,
        "body": "I almost got out, but then I stayed for 20. That\u2019s my response to an \u201calmost-joined veteran\u201c."
      },
      {
        "id": "nbu65iz",
        "score": 82,
        "body": "[removed]"
      },
      {
        "id": "nbu5pib",
        "score": 70,
        "body": "They could sell these at every dive bar in America"
      },
      {
        "id": "nbuenwj",
        "score": 65,
        "body": "My cousin talked shit about me because I went into the army as behavioral health with hopes of pursuing more school and working with veterans and their mental health. \n\n\u201cBro\u2026 just go special forces. Getting an msw sounds lame.\u201d\n\nHe didn\u2019t have shit to say when my aunt put a picture of me in uniform up and his own wife said \u201cyou look so handsome\u201d and his father in law (who is a vet who struggles with PTSD) said \u201cI\u2019m so proud of you and the work you do.\u201d"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1m604ts",
    "title": "Ever get the feeling?",
    "body": "Every time!",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 2737,
    "comment_count": 117,
    "created_at": "2025-07-22T00:42:37+00:00",
    "top_comments": [
      {
        "id": "n4fzlh0",
        "score": 302,
        "body": "Thank you for paying your taxes!"
      },
      {
        "id": "n4g0hml",
        "score": 149,
        "body": "My God, I hate it so much. I get it, Viet Nam veterans got fucked over but I don\u2019t need to be thanked. Hell my Army service was being an unsupervised teenager with access to explosives and alcohol in a foreign country. At no time did I think I was doing it for anyone other than myself."
      },
      {
        "id": "n4g5o0u",
        "score": 115,
        "body": "I tell my husband this after sex or when he's mowed the lawn. I always get a glare. Good thing we are dual military so he started doing it back to me."
      },
      {
        "id": "n4g077s",
        "score": 85,
        "body": "i feel the ick saying thank you for your support \ud83d\ude42\ud83e\udee0\ud83d\ude35\u200d\ud83d\udcab"
      },
      {
        "id": "n4g3w3r",
        "score": 81,
        "body": "THATS WHAT I ALWAYS SAY!!!!!"
      },
      {
        "id": "n4g8p6z",
        "score": 53,
        "body": "I\u2019m extremely uncomfortable with it.  I avoid Veteran\u2019s Day and really the whole week.  I usually take the week off if I can, and hide in my garage.  No Applebees, no parades, nothing.  I\u2019d rather be left alone."
      },
      {
        "id": "n4g9kkc",
        "score": 50,
        "body": "If it's a cashier at a Lowes or Home Depot, I will respond with \"thank you for service too!\"  If the start to mention that my military sacrifice is greater than theirs', I say, \"I spent all my enlistment in Hawai'i.  I probably shouldn't do that, but it feels very undeserved honor that I did not earn."
      },
      {
        "id": "n4g6ppo",
        "score": 32,
        "body": "I would feel weird saying this to veterans that didn\u2019t deploy"
      },
      {
        "id": "n4g6jt9",
        "score": 31,
        "body": "I've started saying \"Welcome Home.\" When I meet another vet.\n\nI like it a lot better, and wish everybody would do it, civilians and other vets.\n\nIt was the standard greeting for Vets before Vietnam.  WW1, WW2, Korea, the standard greeting was Welcome Home.\n\nIt feels odd for two people who served to thank each other for their service.\n\nWelcome Home has no ick factor.\n\nIt has special meaning to us Vietnam era Vets who were definitely not welcomed home."
      },
      {
        "id": "n4g80bi",
        "score": 27,
        "body": "I just say, \"It was my pleasure, thank you.\" Because that's what I heard my Dad and Grandpa tell people when I was young."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1ona48l",
    "title": "For those vets asking if they should re-enlist.",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 2674,
    "comment_count": 105,
    "created_at": "2025-11-03T12:13:49+00:00",
    "top_comments": [
      {
        "id": "nmv8als",
        "score": 210,
        "body": "Smarter than a lot of us"
      },
      {
        "id": "nmvdgu9",
        "score": 101,
        "body": "I guess that\u2019s all he has to say about that."
      },
      {
        "id": "nmv9fgz",
        "score": 76,
        "body": "Definitely his IQ is higher than mine."
      },
      {
        "id": "nmvfyhv",
        "score": 66,
        "body": "[deleted]"
      },
      {
        "id": "nmvkbqs",
        "score": 65,
        "body": "Shot in rhe buttocks.\n\nSorry, not service connected."
      },
      {
        "id": "nmvhc5r",
        "score": 61,
        "body": "Had a degree from the University of Alabama, he could\u2019ve applied for OCS\u2026 \ud83e\udd37\u200d\u2642\ufe0f"
      },
      {
        "id": "nmvj95w",
        "score": 43,
        "body": "But that would\u2019ve been a waste of a damn fine rifleman\u00a0"
      },
      {
        "id": "nmva3wo",
        "score": 41,
        "body": "![gif](giphy|xUPJPFuMO1wOik4Bxe)"
      },
      {
        "id": "nmvhy06",
        "score": 38,
        "body": "my question was always, why did he enlist after graduating college? Like, the Army fucked him worse than Jenny."
      },
      {
        "id": "nmvi3en",
        "score": 28,
        "body": "So sad. He was gonna be a goddamn General one day"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1kvy3wq",
    "title": "Definitely trying to hit his quota",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 2299,
    "comment_count": 175,
    "created_at": "2025-05-26T16:04:53+00:00",
    "top_comments": [
      {
        "id": "mud3xxg",
        "score": 210,
        "body": "**Me:** Wait\u2014what do you mean you\u2019ll put zero?\n\n**Recruiter:** I mean exactly what I said. *Zero.* Nada. Zilch. You\u2019re clean as a whistle, Private Saint.\n\n**Me:** But I literally just admitted to smoking it... twice.\n\n**Recruiter:** *[leans in]* And I\u2019m telling you that what I heard was \u201cyou once stood near someone who smoked oregano at a Blink-182 concert.\u201d That\u2019s not illegal, that\u2019s just bad judgment.\n\n**Me:** So... you\u2019re just gonna ignore it?\n\n**Recruiter:** Son, if I wrote down everything a future soldier told me during this part, we wouldn\u2019t have a military. You want to serve or you want to confess?\n\n**Me:** I mean... serve, I guess?\n\n**Recruiter:** Then congratulations. You\u2019ve just passed the \u201chow bad do you want this\u201d test. Next question\u2014do you faint at the sight of needles?\n\n**Me:** Only if they\u2019re pointed at me.\n\n**Recruiter:** Perfect. That\u2019s a \u201cno.\u201d"
      },
      {
        "id": "mud65yi",
        "score": 192,
        "body": "For me it was \"have you smoked in the past 30 days?\"\n\n \"No.\"\n\n\"Good, you never smoked. Don't admit you ever did or you're fucked.\""
      },
      {
        "id": "mud76cb",
        "score": 169,
        "body": "Recruiter - \"So have you ever done drugs before?\"\n\nRecruit - \"Well, I've dabbled in a bit of coke at a party a year and a half ago\"\n\nRecruiter - \"Oh? You like coke? I'm a Pepsi guy myself\"\n\nRecruit - \"No, I said I've dabbled in coke, as in the white stuff.\"\n\nRecruiter - \"**AND I SAID** I'm a bit of a Pepsi guy myself. Great, we both love soda.  Anyway, I'll just put no, you haven't done any drugs and uhh, we'll get you started with some paperwork.\""
      },
      {
        "id": "mud6eoa",
        "score": 118,
        "body": "My recruiter told me \u201cN-O\u201d stood for Navy Opportunities."
      },
      {
        "id": "mud8vol",
        "score": 107,
        "body": "When I answered NO to all the drug, alcohol, and criminal background questions the recruiter stopped and said, \"you grew up in this town and want me to believe you didn't do any of this stuff?\"\nI said, \"that's my story unless you have evidence otherwise\" \nHe just shrugged and said \"fair enough\""
      },
      {
        "id": "mud9sny",
        "score": 106,
        "body": "https://preview.redd.it/byzs04j6o53f1.jpeg?width=500&format=pjpg&auto=webp&s=1c965d1726fb06e3f57892944557711f456f1501"
      },
      {
        "id": "mudemtb",
        "score": 84,
        "body": "On the way to MEPs\u2026..\n\nRecruiter: smoke weed? \nMe: Yeah, this morning before you picked me up! \nRecruiter: let\u2019s try this again in 30 days\u2026.\n\nlol \ud83d\udca8"
      },
      {
        "id": "mue1fs0",
        "score": 66,
        "body": "My uncle after being in the air force for 10 years told his command he smoked marijuana prior to his enlistment. He got busted down and dealt with than shit until his retirement. Luckily they didn\u2019t kick him out. He only smoked once and the guilt about lying is why he said anything all. I think he might be retarded. \ud83d\ude02"
      },
      {
        "id": "mudhtr4",
        "score": 61,
        "body": "And Y.E.S. stood for Your Enlistment Stops."
      },
      {
        "id": "mudb1m9",
        "score": 52,
        "body": "I dead serious have never smoked. When I said 0 to my recruiter he said, \u201cit\u2019s okay if you have. I\u2019ve smoked before.\u201d I was like interesting but I never have. He said, \u201cnot even once?\u201d"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1otwd2d",
    "title": "In preparation for tomorrow",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 2040,
    "comment_count": 175,
    "created_at": "2025-11-11T01:27:40+00:00",
    "top_comments": [
      {
        "id": "no7l7s4",
        "score": 301,
        "body": "Not even free food will get me out of the house"
      },
      {
        "id": "no7s5r9",
        "score": 189,
        "body": "The plan for Veterans Day. Denny\u2019s for breakfast, free coffee at Starbucks, lunch at Duffy\u2019s, get the free voucher at Texas Roadhouse, a blizzard at Dairy Queen, and dinner at Red Robin. Then off to the VA hospital for a free bypass surgery!"
      },
      {
        "id": "no7lhdz",
        "score": 77,
        "body": "My family was so broke one year, that went to 4 different restaurants and asked for the meal to go. It was the first time we had restaurant food in a long time."
      },
      {
        "id": "no7psgs",
        "score": 66,
        "body": "Bro, same."
      },
      {
        "id": "no7jjd3",
        "score": 59,
        "body": "Ill leave these potential LZ's for anyone looking.  \n[https://www.wearethemighty.com/entertainment/our-huge-list-of-veterans-day-2025-freebies-discounts-and-deals/](https://www.wearethemighty.com/entertainment/our-huge-list-of-veterans-day-2025-freebies-discounts-and-deals/)"
      },
      {
        "id": "no7kt1j",
        "score": 52,
        "body": "Here's to all the people that didn't even make it through their enlistment going to Applebee's to tell all of their chow hall war stories."
      },
      {
        "id": "no7jyal",
        "score": 47,
        "body": "Please tip your waiter/waitress/bartenders accordingly."
      },
      {
        "id": "no99xck",
        "score": 40,
        "body": "Im gonna try tho, I need to get out, get some sunshine. I will beat this.\n\n\n\nEdit: unexpected update! Id been feeling pretty down the whole day despite it going mostly well. Omw home my  found out my uber driver was also a veteran (after i asked about his cauliflower ears lol)\nHe and I have very similar disabilities. It felt so good to talk to someone who understood what I went through! We connected and ill see him in church Sunday. \nSo message is guys keep fighting, go out there and take care of your self. You might meet someone who could uplift you and maybe you could do the same for them."
      },
      {
        "id": "no7l2j4",
        "score": 38,
        "body": "Don\u2019t forget about Texas roadhouse"
      },
      {
        "id": "no7pxw8",
        "score": 34,
        "body": "The best one cause they give a voucher instead. Pocket it for another day."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1qbaw7j",
    "title": "I just feel awkward when it happens",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 1926,
    "comment_count": 323,
    "created_at": "2026-01-12T23:25:19+00:00",
    "top_comments": [
      {
        "id": "nz978ah",
        "score": 458,
        "body": "Say \u201cThank you for your support\u201d and move along."
      },
      {
        "id": "nz9lqmh",
        "score": 151,
        "body": "I give them a free lap dance, no matter where we are (i am not an exotic dancer)"
      },
      {
        "id": "nz9e8gy",
        "score": 144,
        "body": "Just tell them that you love them and give them a long hug, followed by some serious eye contact."
      },
      {
        "id": "nz98gyl",
        "score": 131,
        "body": "I hit them with the \u201cyou got it.\u201d\u00a0"
      },
      {
        "id": "nz98eud",
        "score": 107,
        "body": "I say \u201cyou\u2019re worth it\u201d and give them a thumbs up and a smile and keep moving"
      },
      {
        "id": "nz9bpxi",
        "score": 96,
        "body": "![gif](giphy|13EtQIwmTqNDji)\n\n\u201cNo problem my guy\u201d"
      },
      {
        "id": "nz99utv",
        "score": 86,
        "body": "In the same tone delivered. They give a scripted statement, you can return the same."
      },
      {
        "id": "nz98r1a",
        "score": 77,
        "body": "Can I do finger guns? \ud83d\udc49"
      },
      {
        "id": "nz9etdd",
        "score": 61,
        "body": "Personally, i think people are legit trying to be nice about us being in service.  I've had kids come up to me and say it... and people who generally support the military say it.     I just say thank you and move on.   Also parents with kids say it, etc.\n\nIt doesn't bother me because it's better than them hating us.  I'll take the annoying love and move on.   All the support we can get"
      },
      {
        "id": "nz9gcuc",
        "score": 54,
        "body": "Add a quick squeeze of their glutes. Just so they know you\u2019re really sincere."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1qj8xwu",
    "title": "I am absolutely floored by the VA",
    "body": "I don\u2019t even know where to start. I have been kicked to the curb like a used condom by the civilian world. \n\nUntil last weekend I never knew I was even eligible for VA healthcare. I applied anyway with zero confidence of any help. \n\nTuesday I got an intake call. Again no expectations of help because I didn\u2019t feel like I deserved it. I begged for mh help. Completed intake still with little hope for help. \n\nI just got off the phone with a mental health intake. It\u2019s Wednesday. Two business days after applying. The really wonderful lady on the other end has plugged me into far more help than I ever thought possible or that I deserved. \n\nFor the first time in over a decade I actually have hope. For the first time I feel valued enough to not want to just crawl into my wife\u2019s urn to be with my wife. I\u2019m crying because she made me feel seen. \n\nIt\u2019s good to be back with my brethren. ",
    "flair": "Health Care :caduceus:",
    "score": 1762,
    "comment_count": 95,
    "created_at": "2026-01-21T20:17:26+00:00",
    "top_comments": [
      {
        "id": "o0x7knp",
        "score": 374,
        "body": "Its not perfect but its what we have. I have mostly had good experiences with VA healthcare. I hope you get all the help you need friend."
      },
      {
        "id": "o0xdnfq",
        "score": 160,
        "body": "[removed]"
      },
      {
        "id": "o0x4x73",
        "score": 123,
        "body": "Welcome back and stay with us a long long time!"
      },
      {
        "id": "o0xh1y0",
        "score": 87,
        "body": "The VA has its flaws but I'm grateful to have it every day. Watching my friends and family slog through standard health care and insurance reminds me every day how good it actually is. \n\nIf I could give you any advice, it's to get the app and use Secure Messaging as much as you can. The messages stay with your record and it really helps having that 'paper' trail"
      },
      {
        "id": "o0x8hlj",
        "score": 84,
        "body": "That is such an amazing story, hopefully it is what you need"
      },
      {
        "id": "o0xh996",
        "score": 51,
        "body": "Already in progress. I\u2019m on appeals. There are few doctors that have sufficient knowledge to understand my cancer. I lucked out and got two SMEs. One was my oncologist\u2019s professor. \n\nThank you seems so insufficient. \n\nThis is LLHR on full glorious display."
      },
      {
        "id": "o0xk28r",
        "score": 51,
        "body": "The VA lady got me into the app. She was so kind. Walked me through everything"
      },
      {
        "id": "o0xfoab",
        "score": 45,
        "body": "Everyone cries that the VA health system is bad, but it's just underfunded. If I didn't know any better, I'd say private Healthcare lobbyists have a hand in that. If socialized healthcare works in America, they'll lose all their money when civilians see it's working and demand it for themselves."
      },
      {
        "id": "o0x94yg",
        "score": 38,
        "body": "I\u2019m glad you have had such a good experience! There are a lot of horror stories about the VA and those are certainly valid. However, I\u2019ve also had overwhelmingly positive experiences with them. Glad you decided to seek out care and support!"
      },
      {
        "id": "o0xdvs2",
        "score": 31,
        "body": "If its health related my very first stop is the VA. I have been in about every health care scene you can name and nobody even comes close to the va. I know it can be very regional but I stare in amazement when someone complains about va health care.  In fact I got a call from them just checking in on me today, who in the hell does that."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1oeynu8",
    "title": "New VA Disability Pay Rates / Chart",
    "body": "",
    "flair": "Headlines & News :rsz_21601:",
    "score": 1586,
    "comment_count": 344,
    "created_at": "2025-10-24T14:05:48+00:00",
    "top_comments": [
      {
        "id": "nl5554q",
        "score": 744,
        "body": "30 percenters with children be like\n\n![gif](giphy|Lopx9eUi34rbq)"
      },
      {
        "id": "nl55lna",
        "score": 278,
        "body": "The jump from 90 to 100 is insane I see why people are fighting for it"
      },
      {
        "id": "nl59sw4",
        "score": 213,
        "body": "I'm at 90% and scared to poke the bear, but I'm also grateful at 90%."
      },
      {
        "id": "nl5oe3r",
        "score": 87,
        "body": "Kids being out of the house is worth the pay reduction \ud83d\ude02"
      },
      {
        "id": "nl5fnxt",
        "score": 84,
        "body": "Haham wish I had kids with 100% to increase but also so damn glad they are grown and gone on their own. Wife and I prefer the solitude and peace. \ud83e\udd23\ud83e\udd23"
      },
      {
        "id": "nl5taed",
        "score": 79,
        "body": "I\u2019m reading this while watching my 1 year old go on a rampage"
      },
      {
        "id": "nl5cc7w",
        "score": 74,
        "body": "This is me as well.  87% actual and grateful."
      },
      {
        "id": "nl5724r",
        "score": 70,
        "body": "And here is the SMC chart for those interested:\n\nhttps://preview.redd.it/v0l1zty4n2xf1.jpeg?width=5333&format=pjpg&auto=webp&s=a519fc2432929c6cb10585ae2b962c3ad4fc3a13"
      },
      {
        "id": "nl5ap7r",
        "score": 68,
        "body": "Thanks for the laugh."
      },
      {
        "id": "nl5f6lh",
        "score": 68,
        "body": "Yeah, those in that 85-88% range it's a tough spot because that 95% is so damned far away even another 50% rating doesn't get you there."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1kkqmpq",
    "title": "It\u2019s only a matter of time",
    "body": "No favorable findings found. ",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 1553,
    "comment_count": 104,
    "created_at": "2025-05-12T11:56:19+00:00",
    "top_comments": [
      {
        "id": "mrwdptj",
        "score": 117,
        "body": "[deleted]"
      },
      {
        "id": "mrwe1xh",
        "score": 45,
        "body": "\u2018Best we can do is 10% for gastrointestinal problems\u2019"
      },
      {
        "id": "mrwfh0o",
        "score": 35,
        "body": "\"Veteran worked days from 0700-1530, therefore service connection cannot be granted, due to non-exposure.  No evidence of working at night, when exposure is at a maximum.  \u270d\ud83c\udffe\""
      },
      {
        "id": "mrwhqk5",
        "score": 30,
        "body": "Yo, that chest burster is technically a dependent, so make sure you add that."
      },
      {
        "id": "mrwj8u7",
        "score": 29,
        "body": "IBS until it leaves your body."
      },
      {
        "id": "mrwdsa5",
        "score": 28,
        "body": "Fair point lol"
      },
      {
        "id": "mrwe9e3",
        "score": 26,
        "body": "They mostly come out at night\u2026 Mostly\u2026"
      },
      {
        "id": "mrwiha9",
        "score": 20,
        "body": "GERD, Sinusitis, Cervical Strain at a minimum."
      },
      {
        "id": "mrwf5j8",
        "score": 18,
        "body": "I see your face got blasted, we did find favorable findings for your feet though!"
      },
      {
        "id": "mrwpgmy",
        "score": 17,
        "body": "At least he's getting the With Dependents rate eventually ^posthumously."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1jjkpil",
    "title": "I never thought I\u2019d be able to buy a home, never knew how easy it would be using the VA loan.",
    "body": "I have mid credit at best(680 ish), but a decent income thanks to skills learned while active and the GI Bill. My wife is a SAHM to our three kids. We were looking for another rental when my wife saw a builder offering great incentives so we figured why not try and see what sticks. I had to pay a $500 earnest deposit but I\u2019m getting it back after we close next week. Went under contact March 6th and we\u2019ll get the keys on the 31st, signing everything this Thursday. \n\nI never thought it\u2019d be so easy to navigate this process. It has always intimidated me and frankly I\u2019m kicking myself in the ass for not doing this back when homes were cheap. So thanks to all the dudes in the past who posted questions about using this benefit, they\u2019ve all helped in some way. \n\n",
    "flair": "Housing :house:",
    "score": 1548,
    "comment_count": 487,
    "created_at": "2025-03-25T14:30:27+00:00",
    "top_comments": [
      {
        "id": "mjnrseu",
        "score": 383,
        "body": "Where did you find that interest rate? NFCU is still at 5.75%"
      },
      {
        "id": "mjntfkb",
        "score": 298,
        "body": "Make sure you do your due diligence on inspections. I have read that a lot of the new builds aren't great quality, I would get 2-3 different inspections personally.\n\nEdit: I seen your comment you are in arizona, definitely have multiple inspections."
      },
      {
        "id": "mjnt3d0",
        "score": 199,
        "body": "It is a new build."
      },
      {
        "id": "mjnvqkm",
        "score": 199,
        "body": "In arizona there is a really good inspector, who has been sued by home inspectors and home builders over and over for being \"too much.\"\n\n\"Sai Porter, known for his home inspection videos, is a home inspector in Arizona who has gained attention for exposing flaws in homes, particularly those built by Taylor Morrison Homes, which prompted the company to file a complaint\"\n\nu/cantuseasingleone\n\n\nEdit: I dont live in Arizona, but follow Sai on facebook as his videos went viral because the other inspectors and home builders streissanded themselves."
      },
      {
        "id": "mjnsl9q",
        "score": 137,
        "body": "All things considered, that is a decent rate for the times we live. Congrats! \n\nDon't forget to refinance if the rates go down. Going from 4.75% to 3.75% saves you $100,000 in interest."
      },
      {
        "id": "mjns9kx",
        "score": 123,
        "body": "I'm wondering the same thing. Only place I seen rates that low are on new builds."
      },
      {
        "id": "mjnvymy",
        "score": 66,
        "body": "He\u2019s booked months out so we found another one to inspect recently and then again before the warranty expires."
      },
      {
        "id": "mjnwxhb",
        "score": 66,
        "body": "I had to book a year out with Cy. As soon as I closed on my new build, I booked my one year inspection with him. He found so many things than my first inspector I hired before closing"
      },
      {
        "id": "mjnvxhc",
        "score": 44,
        "body": "There's a guy that pops up on my YouTube shorts named Cy Porter. He only does new build in AZ. It's insane the things he finds. He is so hated by builders that one tried to get his license revoked. I think he is 100% on broken welds on windows. Stuff that will be signed off by the city that doesn't even come close to meeting code."
      },
      {
        "id": "mjp4qc2",
        "score": 41,
        "body": "When they do."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1ntfjkv",
    "title": "For those who know...",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 1492,
    "comment_count": 124,
    "created_at": "2025-09-29T11:32:57+00:00",
    "top_comments": [
      {
        "id": "ngt7spv",
        "score": 76,
        "body": "Never had a problem with that.  But I also did a bunch of cocaine with the guys in supply on the weekends in Austin and the bunny club."
      },
      {
        "id": "ngt8o3x",
        "score": 63,
        "body": "![gif](giphy|9OXijlbEBxy5fQbfaM|downsized)"
      },
      {
        "id": "ngtc9yk",
        "score": 56,
        "body": "[deleted]"
      },
      {
        "id": "ngtfe78",
        "score": 40,
        "body": "POV you're the armorer who just declined my weapon on a Friday for the 3rd time\n\nhttps://preview.redd.it/69s1w4bal3sf1.jpeg?width=236&format=pjpg&auto=webp&s=4ff8f1c2e7f7c8dc33706362cbd0a589a85276aa"
      },
      {
        "id": "ngtlkcs",
        "score": 36,
        "body": "I learned to wait until they really wanted to get out of there to turn mine in.  Like 15 mins before formation."
      },
      {
        "id": "ngta4rb",
        "score": 34,
        "body": "As a former armorer, don't come to my arms room 30 minutes after we've come from the range to turn in your weapon. 100% turn around. If you wanted to pay me to clean your weapon, then let's talk \ud83d\ude00"
      },
      {
        "id": "ngtdzmb",
        "score": 27,
        "body": "God I use to hate working a 14 hour day and trying to go home but my M4 was dirty and had to clean.  This brought me back."
      },
      {
        "id": "ngts03f",
        "score": 23,
        "body": "I was the unit armorer and took everyone\u2019s shit. Except for our SFC. He was a dick. It was also funny watching him get pissed off and couldn\u2019t pull rank then. I was just a dumb SPC at the time."
      },
      {
        "id": "ngteyam",
        "score": 19,
        "body": "![gif](giphy|GXKK71oMMtBPu8ffUW)"
      },
      {
        "id": "ngva0dl",
        "score": 15,
        "body": "I was the Armorer in my last unit, and it 100% depended on how I felt about you. If you were super annoying, you were definitely getting denied a couple times."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1l1eio6",
    "title": "He's P&T EVERYONE!!!!!",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 1420,
    "comment_count": 165,
    "created_at": "2025-06-02T10:27:02+00:00",
    "top_comments": [
      {
        "id": "mvl42cd",
        "score": 413,
        "body": "https://preview.redd.it/nb392atioi4f1.jpeg?width=602&format=pjpg&auto=webp&s=5df24d09505ed93c951df026aaba80008cc8b832"
      },
      {
        "id": "mvldct4",
        "score": 206,
        "body": "Random people on the Internet don\u2019t need to know your rating. Apart from the VA, very few people need to know.\n\nThat said, if you\u2019re rocking a disabled plate, it\u2019s no secret that you\u2019re rated for something.\n\nAnd to anyone that tries to talk about how they wish they could get \u201cfree money\u201d from the government, direct them to the nearest military recruitment office where they can sign up for that *free money*."
      },
      {
        "id": "mvkd1m0",
        "score": 204,
        "body": "Broke the rule. Never tell anyone your rating. Especially your own family."
      },
      {
        "id": "mvld18p",
        "score": 62,
        "body": "Is it mostly in the lower back and knees? Because the VA sure doesn't think so."
      },
      {
        "id": "mvla0pj",
        "score": 61,
        "body": "I feel your pain \ud83d\ude2d\ud83e\udd23"
      },
      {
        "id": "mvkfg17",
        "score": 57,
        "body": "Never tell Newman the building gossiper. The notorious Blue Falcon!"
      },
      {
        "id": "mvmkz82",
        "score": 56,
        "body": "I got rid of my plate. I\u2019d rather pay the registration fee each year than have anyone know that info about me."
      },
      {
        "id": "mvl8zyx",
        "score": 55,
        "body": "I told a total of 5 people. two stopped talking to me. lol"
      },
      {
        "id": "mvknr1c",
        "score": 48,
        "body": "Oh plenty of people care \n\nWe still lived together for a bit after we broke up.\n\nOne day while I was at work she went through my shit  and say that I was recently made p&t. \n\nShe announced it on Facebook and tells anyone that will listen."
      },
      {
        "id": "mvnlwlj",
        "score": 45,
        "body": "[deleted]"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1k4f9n4",
    "title": "Some of y'all are ASVAB wavers and we don't have to ask cuz we can tell",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 1414,
    "comment_count": 152,
    "created_at": "2025-04-21T14:44:17+00:00",
    "top_comments": [
      {
        "id": "mo9kvlc",
        "score": 526,
        "body": "Waivers*"
      },
      {
        "id": "mo9mnym",
        "score": 307,
        "body": "Is this an ASVAB waver?\n\nhttps://i.redd.it/6sik4o1vd7we1.gif"
      },
      {
        "id": "mo9lsst",
        "score": 157,
        "body": "OP clearly needed a \u201cWAVER\u201d"
      },
      {
        "id": "moa25zn",
        "score": 141,
        "body": "Obviously OP is an ASVAB Waiver"
      },
      {
        "id": "mo9viw7",
        "score": 90,
        "body": "\ud83e\udd23\ud83e\udd23"
      },
      {
        "id": "mo9l03w",
        "score": 89,
        "body": "Waiver*"
      },
      {
        "id": "mo9l1sn",
        "score": 70,
        "body": "\u201cI got rated 100% but they did it for the wrong reasons. lemme fix it. That\u2019ll show em\u201d\n\nLike bro stfu and take the money."
      },
      {
        "id": "mo9rr00",
        "score": 55,
        "body": "Leave OP alone... Marines rarely were trusted with computers to make memes (which is why they were left with crayons).  Spelling isn't high in priority."
      },
      {
        "id": "moabx2n",
        "score": 55,
        "body": "Who failed \u201cSpelling for Marines\u201d"
      },
      {
        "id": "mo9mjlx",
        "score": 51,
        "body": "Ironic."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1ou27l8",
    "title": "Who is ready to hear it??",
    "body": "I saw this and thought it was hilarious \ud83d\ude02",
    "flair": "VA Disability Claims :claim:",
    "score": 1366,
    "comment_count": 233,
    "created_at": "2025-11-11T06:24:33+00:00",
    "top_comments": [
      {
        "id": "no8vece",
        "score": 205,
        "body": "These guys will always tell you long stories about their security guard adventures."
      },
      {
        "id": "no9dehu",
        "score": 137,
        "body": "As a veteran with flat feet, I like hearing how they would have joined if it wasn\u2019t for their flat feet."
      },
      {
        "id": "no8zjwq",
        "score": 135,
        "body": "\"I would have joined but I would have gotten in too much trouble when I would have punched out a drill sergeant for telling me what to do.\""
      },
      {
        "id": "no9nyq1",
        "score": 120,
        "body": "\"You know, I almost joined. You're better than me though, cuz I couldn't stand there while some drill sergeant screamed at me. I would have punched him right in the face and broke his jaw. No, but really, I could have joined but I like my freedom. I couldn't have somebody telling me what to do all the time and I like being able to do what I want whenever the fuck I want, you know? But yeah man, thank you for your service, you want a beer?  No? Ok, so anyway, my pops kept trying to get me to join because he was in the Army. He's all, \"Son, you gotta do something with your life. You can't play video games and drink all day.\" And I'm all, \"Bullshit, I'm not going anywhere just to get screamed at, you know how I am when people scream at me pops.\" He backed off after that. *sips beer* But you did good man, you did real good. I see you're married, you got a nice house, nice car and that's nice but me? I don't need a house. Pops lets me stay with him for free so I don't pay any rent or anything. I'm living the dream. You know, my dream was always to be like Pops and be this big time Army guy, but meh, what can you do? Once a summbitch tried to even attempt to yell at me, it woulda been LIGHTS OUT!!!!!\"\n\n![gif](giphy|jnhXd7KT8UTk5WIgiV)"
      },
      {
        "id": "no8yqcb",
        "score": 88,
        "body": "Or some magical condition about their left pinky toe nail how it disqualified them"
      },
      {
        "id": "no9lksz",
        "score": 75,
        "body": "The military *gave* me flat feet!!!"
      },
      {
        "id": "no9tjee",
        "score": 46,
        "body": "Thank you for your intent to serve."
      },
      {
        "id": "no9jkm1",
        "score": 41,
        "body": "I\u2019ll never forget an acquaintance I had on FB who gave her job description on her profile like this: \u201cProtecting those who build vehicles for our nation\u2019s military.\u201d She was a security guard at a defense contractor."
      },
      {
        "id": "no9lmht",
        "score": 38,
        "body": "Almost Veteran day is April 1st!"
      },
      {
        "id": "noaaucr",
        "score": 38,
        "body": "That 'might' have been me when i failed the ranger/sf physical because of my eyesight. So.... i had a then experimental eye surgery (radial keratotamy) to fix my vision and passed on the second try. Geez, that was a long time ago."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1kfaa8w",
    "title": "Go ahead\u2026. Fire me.",
    "body": "Although not ideal, it definitely lessens the stress. ",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 1349,
    "comment_count": 141,
    "created_at": "2025-05-05T12:23:30+00:00",
    "top_comments": [
      {
        "id": "mqp4sw3",
        "score": 380,
        "body": "Nah fr tho. I was at work this weekend and it was busy and one of the managers made some comment about writing me up, and I responded with \u201cI\u2019ll quit right now\u201d it felt so freeing just being able to say that and mean it.  Ftr I didn\u2019t quit or get written up but having the ability to do so with zero effect on my day to day life is soooooo freeing"
      },
      {
        "id": "mqpnlas",
        "score": 299,
        "body": "https://preview.redd.it/s3ru48q84zye1.jpeg?width=1170&format=pjpg&auto=webp&s=9457c5ce07093eeec2053d7e24c6c61ddd7fd26a"
      },
      {
        "id": "mqp3c0t",
        "score": 193,
        "body": "What pisses me off is when people find out you have a disability rating and they get mad about it. I'm the one that had the balls to join after 9/11 and as a result, got injured in iraq. If they didn't step up to the plate, they can't really complain. It's not like I chose to get injured."
      },
      {
        "id": "mqp5lex",
        "score": 135,
        "body": "Right! Like is it ideal? No. BUT could I survive with some small adjustments to my spending? YES. Easy"
      },
      {
        "id": "mqp3fuf",
        "score": 113,
        "body": "Or when they find out you\u2019re 100% and tell you lunch is on you\u2026.. kiss my ass \ud83e\udd23."
      },
      {
        "id": "mqp6wlf",
        "score": 91,
        "body": "Every time this gets shared, it loses another pixel.  \ud83e\udd23"
      },
      {
        "id": "mqpnnpx",
        "score": 70,
        "body": "Hey you made that on a gameboy color too! Lmao"
      },
      {
        "id": "mqq2dta",
        "score": 65,
        "body": "No. Freedom is on me"
      },
      {
        "id": "mqpsx46",
        "score": 60,
        "body": "Could you imagine if there was a country where all the people could feel this level of freedom, especially at work?"
      },
      {
        "id": "mqp90pn",
        "score": 59,
        "body": "For a short period of time I was a Federal Corrections Officer in TX after I got out of the army. There were 2 parking lots, a really huge one, but then you had to walk up a massive hill that was literally like a football field worth of steps at a steady incline, and then there was a smaller one at the top of those stairs that only had like 6 spots, and 5 of them were handicap spots.\n\nIn TX (at the time, the law has since changed) if you had a DV plate, you could park in the handicap spots. I have degenerative arthritis in both knees, walking up those stairs not only caused my knees to ache for a couple hours, but you could literally hear my bones grinding and crackling... so if there was a spot open at the top of the hill, I would park in one versus walking all those stairs.\n\nOne morning at like 5 am I was walking in, and putting my stuff through the X-ray machine, when one of the prison nurses walked in behind me, and just right in front of everyone asks, \"Are you actually handicapped and allowed to park in those spots??\" in such a degrading ass tone. It immediately made my blood boil, and my face turned a little red from it, and I said in a snotty tone back to her, \"Not that it's any of your business, but yes.\" And she just kind of scoffed and said, \"Must be nice.\" To which I immediately shot back, \"What would be nice is to not be 30 years old with the joints of an 80 year old and in pain every day of my life from it.\" I couldn't believe someone actually had the audacity, not only to question me, but to tell me it \"must be nice\" to have destroyed joints just because they had to do a little bit of exercise to walk in to work."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1kqea1x",
    "title": "\u201cIs it though?\u201d",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 1343,
    "comment_count": 67,
    "created_at": "2025-05-19T15:16:43+00:00",
    "top_comments": [
      {
        "id": "mt4zxnk",
        "score": 85,
        "body": "Better yet, VA: \"Yes, your back is jacked up, but it's not connected to your 24 years of abusing it during military service.\"  \ud83d\ude44"
      },
      {
        "id": "mt645xy",
        "score": 34,
        "body": "\"Your back is really bad! Here's a lil 10% for your suffering\""
      },
      {
        "id": "mt5py2k",
        "score": 25,
        "body": "I had surgery for colon cancer a few months ago. I recently filed under the PACT Act. During my recent C and P exam, the nurse practitioner told me that she is not sure that it was really cancer. I wanted to say what I was thinking, but I held my tongue and pointed to the statements on the medical diagnosis that stated that it was cancer. She still seemed skeptical."
      },
      {
        "id": "mt5dmby",
        "score": 25,
        "body": "VA: Oh your spine is messed up?\n\n\nVet: Yeah that thing that unites my entire skeletal structure.\n\n\nVA: Ah yes, well unless you are literally paralyzed and can\u2019t move at all which we know is not true because you arrived here for your exam, best we can do is 40% if the protractor reads right.\n\n\nVet: But it hurts to do anything let alone exist.\n\n\nVA: Fuck you."
      },
      {
        "id": "mt6g6oq",
        "score": 19,
        "body": "The problem is that the things we did when we were 21 and bullet proof usually don't show as chronic problems until we are much older.\n\nFor example, we (2 of us) were routinely told to pick up a 500lb buoy and hold it so another person could put lifting straps under it, so the crane could lift it onto the ship.  When we complained about backaches, we were told to drink more water and walk it off.  If we tried to go to medical, we were told we were malingering and trying to get out of work, so we didn't go.\n\nNow, years later I have a backache and sciatica that won't go away so I get Xrays and finally after it's been hurting for more than 6 months, they send me for an MRI.  The MRI finds I have 2 crushed discs even though I have worked a desk job ever since I got out.\n\nI file a claim with the VA, because I'm having constant pain and I am told \"Not Service Connected\" because there are no complaints about back problems during service...\n\nEDIT 1: Before you say it;  I'm not over weight, I stay in shape, and I don't ride a motorcycle.  The doctor said me staying in shape is probably what allowed me to go this long before it became an issue, but bone density changes and cartilage hardening as you age caused an existing injury to worsen.\n\nEdit 2: I know people lie on their VA claims and I hope they get what's coming to them for it.  My experience thus far is that everyone of us who submits a claim is treated as if we're lying and that's not right."
      },
      {
        "id": "mt4uz8r",
        "score": 13,
        "body": "![gif](giphy|fX8H6GACvaiatkqexi|downsized)"
      },
      {
        "id": "mt51klh",
        "score": 13,
        "body": "VA: you refused to admit it was messed up in every single annual physical you had, claimed it didn\u2019t hurt at all while doing retirement paperwork, but your Facebook feed talks non stop about that motorcycle accident you had a year ago when you\u2019ve been out for five years.\n\nteam, just be honest during your annual exams and there\u2019s never a question if it\u2019s service connected. But if you give them no solid reason to guarantee it is, they\u2019ll look for any reason they can to say it\u2019s not."
      },
      {
        "id": "mt6lcsg",
        "score": 13,
        "body": "I hate to break it to the NP, but she is not an Oncologist nor an MD."
      },
      {
        "id": "mt5ri9z",
        "score": 13,
        "body": "And there\u2019s no way it\u2019s coming from being hellaciously overweight and inactive for the 30 years after the military or anything. No way at all."
      },
      {
        "id": "mt5vtoq",
        "score": 12,
        "body": "[deleted]"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1nhpmys",
    "title": "Sleep study",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 1329,
    "comment_count": 52,
    "created_at": "2025-09-15T15:52:30+00:00",
    "top_comments": [
      {
        "id": "ned8qiy",
        "score": 196,
        "body": "Notable Events during Study:\n\nAt approximately 02:37 AM, the patient demonstrated sudden elevations in heart rate, irregular respiratory effort, and rapid EEG arousals. Initially concerning for seizure or sympathetic storm, video monitoring clarified that the patient was, in fact, vigorously engaging in manual respiratory physiotherapy\u00a0(masturbation).\n\n  \nDuring this event:\n\n\t\u2022\tHeart rate spiked from 64 bpm baseline to 132 bpm.\n\n\t\u2022\tRespiratory belts showed erratic thoracoabdominal movement resembling severe paradoxical breathing.\n\n\t\u2022\tPulse oximetry briefly read \u201cError,\u201d likely due to excessive hand motion.\n\n\t\u2022\tTechnician note: \u201cPatient appears to be enjoying himself. No intervention required (except maybe a\u00a0cold\u00a0shower).\u201d"
      },
      {
        "id": "ned6517",
        "score": 105,
        "body": "It's sleep fapnea Darlene, get in there and cure it."
      },
      {
        "id": "nedf770",
        "score": 105,
        "body": "It\u2019s all fun and games until they start questioning your ED claim that was granted many years ago. LoL."
      },
      {
        "id": "nedemlh",
        "score": 45,
        "body": "I went in for a sleep study at the VA. They told me to stick to my normal bedtime routine\u2026 so now some poor intern had to watch me jerk off, pass out, and start yelling classified coordinates in my sleep. At least now they finally know where all the missing MRE heaters ended up."
      },
      {
        "id": "neddt51",
        "score": 43,
        "body": "Paranormal Whacktivity"
      },
      {
        "id": "ned5to7",
        "score": 31,
        "body": "![gif](giphy|anYBNhqT2BYcg)"
      },
      {
        "id": "ned7wts",
        "score": 27,
        "body": "Francis, we got *another one*! Get the spray bottle."
      },
      {
        "id": "nedcmph",
        "score": 25,
        "body": "Take my upvote. Love this one"
      },
      {
        "id": "nedyhst",
        "score": 25,
        "body": "https://preview.redd.it/etxdsskpddpf1.png?width=946&format=png&auto=webp&s=e811f0e34e267febf85940d9484c99f62a1f6e7f\n\nFigured you would enjoy this"
      },
      {
        "id": "nee3ys8",
        "score": 20,
        "body": "I was gonna toss in a lame comment about not service connected, but yours is much better."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1qnryoe",
    "title": "I'll Just leave this Right Here",
    "body": "Stole..... Borrowed? From Army Meme Facebook",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 1324,
    "comment_count": 110,
    "created_at": "2026-01-26T20:30:53+00:00",
    "top_comments": [
      {
        "id": "o1w0h37",
        "score": 146,
        "body": "I get the argument but gas masks don\u2019t have a pump that creates air pressure pushing the mask against your face either."
      },
      {
        "id": "o1w16nl",
        "score": 83,
        "body": "They do now. The army has started issuing PAPR. Also masks seal with a beard."
      },
      {
        "id": "o1w0a73",
        "score": 63,
        "body": "If only there was a difference in the purpose/ function of a gas mask and a CPAP."
      },
      {
        "id": "o1w4zhm",
        "score": 40,
        "body": "Beard home station, shave when down range. Problem solved."
      },
      {
        "id": "o1w237i",
        "score": 37,
        "body": "I guess tech has changed since 12 years ago, learned something new"
      },
      {
        "id": "o1w7rkh",
        "score": 30,
        "body": "Even greater than 12 years ago. The Avon M50 was first issued in \u201806 and you can still get a good seal with facial hair with that mask. HOWEVER, there\u2019s a gradient to that and why the manufacturer says that facial hair MAY break the seal.\n\nWith proper form fit, you can get a seal with almost any negative pressure mask/respirator up to something like 30 mm of thickness. The problem is that facial hair, along with people not getting proper fit increases the chances of a seal breaking. So now they\u2019re working on masks that don\u2019t leave room for that chance even with facial hair."
      },
      {
        "id": "o1w3kha",
        "score": 17,
        "body": "Beards can definitely break the seal"
      },
      {
        "id": "o1wo2ke",
        "score": 15,
        "body": "PAPRs are not for regular field Soldiers.  Some CBRN and firefighter MOSs use PAPRs but most use the M50 series negative-pressure protective masks."
      },
      {
        "id": "o1x3ugq",
        "score": 14,
        "body": "We do? I\u2019m still active and we still use regular pro masks. I have no idea what PAPR is"
      },
      {
        "id": "o1xo95y",
        "score": 13,
        "body": "This isn't the only argument, either.\n\nHow many of ya'll have been stationed at a command that doesn't even issue you a gas mask?  I had been to several.  So you can't have a beard, because the gas mask we don't issue you won't seal properly.\n\nI'm retired now, but that shit is still dumb AF."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1kfe75x",
    "title": "The accuracy \ud83d\udc4c",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 1284,
    "comment_count": 235,
    "created_at": "2025-05-05T15:18:21+00:00",
    "top_comments": [
      {
        "id": "mqq0qed",
        "score": 179,
        "body": "I tried to go Air Force because I wanted to do TACP. \n\nFucking recruiter was out to lunch so the Navy dudes snagged me.\n\nCan confirm, shoulda went Air Force."
      },
      {
        "id": "mqq33w7",
        "score": 55,
        "body": "Can confirm, should of went Air Force \ud83d\ude02"
      },
      {
        "id": "mqq3qhg",
        "score": 48,
        "body": "The \"shoulda went Air Force\" is so true...I went to the AF recruiter, but was a few pounds overweight.  The Army wasn't accepting women at that moment, or there weren't enough to make a full unit (what the recruiter said).  the Navy recruiter was ear hustling in the hall and asked if I was ready to go NOW, measured me, and we got the process started. I'm glad I did it, I went into aviation anyway, but who knows what life would have been like if I'd gone AF."
      },
      {
        "id": "mqq0cat",
        "score": 46,
        "body": "Hey now, Marines are a department of the Navy for that football game day only."
      },
      {
        "id": "mqq58v7",
        "score": 41,
        "body": "[removed]"
      },
      {
        "id": "mqq566g",
        "score": 36,
        "body": "Same scenario except marine came out and said they were buddies with Air Force and to chat with him. \n2 weeks later I shipped off to MCRDSD and should\u2019ve gone air force"
      },
      {
        "id": "mqq6zao",
        "score": 32,
        "body": "![gif](giphy|CeqX0rEkF1AsBlEWc5|downsized)\n\nYou would\u2019ve gone pro\u2026 \ud83d\ude0e\ud83e\udd18"
      },
      {
        "id": "mqq3vkv",
        "score": 31,
        "body": "I went Air Force. \ud83d\ude01"
      },
      {
        "id": "mqslg1p",
        "score": 29,
        "body": ">of\n\nThey wouldn\u2019t HAVE taken you."
      },
      {
        "id": "mqqwmoo",
        "score": 28,
        "body": "Only problem with the Air Force is you get stationed in shitty places like Minot, or bumfuck Texas.\n\nmost of us squids either ended up in San Diego or Norfolk, which at least had beach near by."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1jo10ec",
    "title": "This is why the VA is important",
    "body": "",
    "flair": "VA Disability Claims :claim:",
    "score": 1265,
    "comment_count": 46,
    "created_at": "2025-03-31T11:32:35+00:00",
    "top_comments": [
      {
        "id": "mkoty1t",
        "score": 146,
        "body": "I don't think Ira Hayes ever sought any VA help but he did get some help .\n\n\"Ira Hayes, the Pima Native American Marine known for raising the flag on Iwo Jima, struggled with alcoholism after World War II. There\u2019s no definitive evidence that he formally sought help through structured programs like rehabilitation or therapy, as such options were limited in the 1940s and 1950s, especially for Native Americans in rural areas like the Gila River Indian Community. However, there are indications that others attempted to assist him, and he expressed some desire to address his drinking.\n\n\"After the war, Hayes faced significant challenges reintegrating into civilian life, compounded by PTSD and public scrutiny. His drinking led to frequent arrests\u2014over 50 by some accounts\u2014often for public intoxication. In 1953, after one such arrest in Chicago, the Chicago Sun-Times intervened, raising funds for his rehabilitation and helping him secure a job in Los Angeles. Hayes reportedly expressed gratitude and optimism, saying, \"I know I'm cured of drinking now.\" Yet, within a week, he was arrested again, suggesting either a lack of sustained support or an inability to maintain sobriety without ongoing help.His family and community didn\u2019t abandon him, despite his struggles. His celebrity brought attention, but not always aid\u2014some argue he was targeted due to racist stereotypes rather than supported. \n\n\"Author Tom Holm, in Ira Hayes: The Akimel O'odham Warrior, World War II, and the Price of Heroism, suggests Hayes was more a binge drinker than a chronic alcoholic, using alcohol to cope with trauma, and that formal help for PTSD wasn\u2019t available until decades later (recognized in 1980). His brother Kenneth and others believed his death in 1955\u2014officially from exposure and alcohol poisoning\u2014might have been influenced by an altercation, not just drinking, though no investigation followed.Hayes\u2019s own words and actions don\u2019t explicitly show him seeking help, but his moves to cities like Chicago and Los Angeles, facilitated by the Bureau of Indian Affairs relocation program, might reflect attempts to escape environments that fueled his drinking. \n\n\"Unfortunately, these efforts didn\u2019t stick, and he returned to Arizona, where he died. The lack of mental health resources, cultural stigma, and systemic neglect likely limited any chance he had to get effective support. So, while he didn\u2019t clearly pursue help himself, others tried to intervene\u2014with little lasting success.\""
      },
      {
        "id": "mko4ma7",
        "score": 105,
        "body": "He was 23 when he raised the second flag on Iwo Jima."
      },
      {
        "id": "mko434l",
        "score": 81,
        "body": "For some reason I was always associating the majority of our troops at the time being kids around 18-22 that I never thought about those serving at an older age like this one. 61% of those serving during WW2 were drafted. Still thank those for fighting against fascism. Thanks for the reminder and sharing OP"
      },
      {
        "id": "mkok1uh",
        "score": 54,
        "body": "First Native American in the marine corps to be recognized for something so significant! Asked my FMF corpsman husband who it was and he got it right thanks to all that corps knowledge lol"
      },
      {
        "id": "mkpcdfg",
        "score": 53,
        "body": "https://preview.redd.it/efnonlcrr1se1.jpeg?width=262&format=pjpg&auto=webp&s=4debe670b6653c042ed216c38d98c280c9322187\n\nTo put a face on those who lost their lives in the attack on Pearl Harbor, this is my great-great uncle Vernon Matney, whose remains rest under the water, in the USS Arizona. His brother also perished, but was on shore having breakfast."
      },
      {
        "id": "mko576f",
        "score": 43,
        "body": "I\u2019ll be honest I didn\u2019t recognize the name off first glance, but I\u2019m glad you told me this because now I\u2019ll remember that. Thanks man"
      },
      {
        "id": "mko6mm1",
        "score": 41,
        "body": "Without a doubt\u2026 But at the end of the day, the one thing it is apparent is the VA did not serve minority communities as well."
      },
      {
        "id": "mko5b6s",
        "score": 38,
        "body": "The average age of troops in WWII was 26. Now Vietnam the average age was 19, so maybe that\u2019s where the thought came from."
      },
      {
        "id": "mko58s0",
        "score": 37,
        "body": "I frequently think about Ira, I always wonder if the story we get about him is the truth, I know he was a tortured person (who wouldn\u2019t be?) but I wish we knew more about who he actually was and not the Clint Eastwood / Johnny Cash / James Bradley version of him."
      },
      {
        "id": "mkp13j5",
        "score": 37,
        "body": "I repectfully disagree.  This is not DEI.  \n\nSemper Fi\ud83c\uddfa\ud83c\uddf8"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1mhermi",
    "title": "Accurate representation of the chain of command",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 1265,
    "comment_count": 98,
    "created_at": "2025-08-04T14:20:23+00:00",
    "top_comments": [
      {
        "id": "n6vlql5",
        "score": 226,
        "body": "The fact that there isnt an officer standing in front of the truck like a roadblock tells you its wrong ;)"
      },
      {
        "id": "n6vkjmd",
        "score": 130,
        "body": "Do not lump the E4 mafia into that nonsense."
      },
      {
        "id": "n6vl77m",
        "score": 84,
        "body": "E4-5s do all the work on submarines"
      },
      {
        "id": "n6vufea",
        "score": 61,
        "body": "My first thought. There aren\u2019t three Lts and a captain pushing it to the other direction"
      },
      {
        "id": "n6w0nsh",
        "score": 45,
        "body": "Yep. I came here to say \u201cthis must be army shit\u201d"
      },
      {
        "id": "n6vyhko",
        "score": 43,
        "body": "Who do you think took the photo?"
      },
      {
        "id": "n6wmjzv",
        "score": 41,
        "body": "We are smart enough to be doing \u201c some other work\u201d instead of being in the picture."
      },
      {
        "id": "n6vvdpc",
        "score": 39,
        "body": "They are lost on a different street, give em' some slack.\u00a0"
      },
      {
        "id": "n6vqlmo",
        "score": 27,
        "body": "Navy it's definitely E1-5"
      },
      {
        "id": "n6vq6s8",
        "score": 27,
        "body": "\u201cI need 5 bodies for a detail\u201d\n\n\n\u201cWhat\u2019s the detail?\u201d\n\n\n\u201cI need 4 bodies for a detail\u201d"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1k2udvi",
    "title": "The $83,000 solution.",
    "body": "at the end of February, I experienced stroke like symptoms and was transport to the Mayo Clinic in Jacksonville. used my VA health card on everything. ambulance, ER, and hospital stay.\n\nstayed at the Mayo for five days, and called the VA 800 number telling them (day two). the VA told me not to worry about the bill. I took the advice.\n\nwife and i focused on recovery and while a set back for myself, remained optimistic. \n\n  \nthen the bills came. team, my hospital bill due to tests, meds, et al, came to $83,000 before the agreed pricing kicked in. in the end \u201cthe veteran\u2019s responsibility is $0.00\u201d.  \n\n  \nwhile my follow on with the Mayo is on me, the initial care was paid for. 100-percent grateful.  100-percent on track for recovery. thank you for reading. ",
    "flair": "VA Disability Claims :claim:",
    "score": 1249,
    "comment_count": 141,
    "created_at": "2025-04-19T11:43:53+00:00",
    "top_comments": [
      {
        "id": "mnwvhsm",
        "score": 229,
        "body": "Are you sure the follow up is on you? I broke my leg a few weeks ago and the VA is covering everything, including follow ups and physical therapy. You might double check."
      },
      {
        "id": "mnwxeln",
        "score": 127,
        "body": "It's likely on him if he'd like to continue to go to the Mayo. If he'd be willing to go through the VA, you're right, likely 100% covered."
      },
      {
        "id": "mnwyz9l",
        "score": 52,
        "body": "Yeah. I guess my situation could be because the closest hospital is 200 miles away. They just refer everything out  locally and I haven\u2019t paid a dime. This is my 3rd surgery in 5 years."
      },
      {
        "id": "mnwylq5",
        "score": 41,
        "body": "VA healthcare and coverage is a blessing. I have always been grateful for that aspect of the VA"
      },
      {
        "id": "mnxfza0",
        "score": 31,
        "body": "I had covid pneumonia and was on ecmo life support for 45 days my bill was1000000 + va covered it all"
      },
      {
        "id": "mnwx8gp",
        "score": 16,
        "body": "Hope all is well and that you have a speedy recovery. Mayo Clinic is the best hospital I can think of. Glad things went well. Duvalll."
      },
      {
        "id": "mnx8j60",
        "score": 14,
        "body": "Northern Michigan. I actually mapped it, it\u2019s 167 miles, but still."
      },
      {
        "id": "mnxqre0",
        "score": 13,
        "body": "Have you thought about setting up community care instead that\u2019s what I have and any time I go to my primary physician it\u2019s fully covered no matter what"
      },
      {
        "id": "mnwxrv6",
        "score": 12,
        "body": "I had a stroke some years ago. They covered the ER visit, but didn\u2019t want to cover the follow up with the non-VA hospital. I asked my primary care doctor to refer me to the  VA clinics for the same follow up stuff, gave him the rundown and where I was treated so he could verify and/or get the treatment record stuff, and just did it at the VA (I had lingering speech issues and some motor issues).  \n\nYour mileage may vary, but as much as I\u2019ve had very bad experiences at most VA clinics, their specialty clinics for that recovery were top notch. May be worth exploring as an option as that recovery treatment can get very expensive but also make a lot of difference."
      },
      {
        "id": "mnx7n4c",
        "score": 12,
        "body": "Concur on this. I can use the VA. In Jacksonville, most likely VA \u201ccommunity care\u201d. While community care is good, I am using my Medicare. VA hospital is in Gainesville\u2014a three hour drive. My vision is impaired due to a \u201cthunderclap\u201d headache. Despite this, I am in a group with 97-percent recovery. \n\nAmbulance paid for by transportation at VA. Thank you for the reply."
      }
    ]
  }
]
```
