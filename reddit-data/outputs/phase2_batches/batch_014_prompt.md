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
    "subreddit": "VeteransBenefits",
    "id": "1ogomz4",
    "title": "Judges reject VA secretary\u2019s request to pause veterans\u2019 claims appeals",
    "body": "Well the current administration is trying yet again to screw Veterans but at least they lost this attempt. \n",
    "flair": "Headlines & News :rsz_21601:",
    "score": 636,
    "comment_count": 57,
    "created_at": "2025-10-26T16:15:04+00:00",
    "top_comments": [
      {
        "id": "nli3u1b",
        "score": 288,
        "body": "Nobody hates veterans more than a Republican politician"
      },
      {
        "id": "nli4laz",
        "score": 227,
        "body": " Not gonna lie I low key regret who I voted for\u2026"
      },
      {
        "id": "nli9chw",
        "score": 217,
        "body": "We can start with the firing of VA workers. \n\nIt shouldn't take 3 months for me to see a Dr for a simple check up.\n\nIt use to be under a week last year"
      },
      {
        "id": "nlia8rr",
        "score": 215,
        "body": "It matters that you can admit it. Please talk to you friends and family still drinking the koolaid."
      },
      {
        "id": "nli4fi0",
        "score": 198,
        "body": "What\u2019s up with the account that keeps posting stuff defending the va secretary\u2019s push for this within minutes of every post"
      },
      {
        "id": "nli5q18",
        "score": 193,
        "body": "Theyre going to shut down this post soon but yeah this administration continues to gut veteran benefits and a judge just got in their way but for how long"
      },
      {
        "id": "nli7wg6",
        "score": 160,
        "body": "At least you can admit it. We all make mistakes just gotta learn from them."
      },
      {
        "id": "nliblwm",
        "score": 147,
        "body": "Regret is the first step towards redemption"
      },
      {
        "id": "nli4t6g",
        "score": 122,
        "body": "Giving people weapons, training them in their use, saying 'thank you for your service', and then ripping them off in broad daylight....  \n\nVery high risk strategy. Requires a lot of chutzpah and/or willful ignorance of history."
      },
      {
        "id": "nlhwsqq",
        "score": 61,
        "body": "[removed]"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1lok7s2",
    "title": "*Internal Giggles*",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 627,
    "comment_count": 17,
    "created_at": "2025-06-30T21:44:44+00:00",
    "top_comments": [
      {
        "id": "n0od2yf",
        "score": 357,
        "body": "Reminds me of talking to this guy long ago. He was talking about being stationed or TDY in Panama. He said for a chicken dinner you could have any girl you wanted. Then he mentioned his wife was from Panama. I just blurted out without thinking \u201cso that was like two chicken dinners\u201d. He was not pleased with me, but he didn\u2019t correct me either."
      },
      {
        "id": "n0olmox",
        "score": 316,
        "body": "Im guessing he bagged his own groceries"
      },
      {
        "id": "n0o8u0o",
        "score": 273,
        "body": "True story: we had a guy in our company who married a Korean. He gets orders to go back to the states. They fly back, he wakes up on the plane and she is gone. Can\u2019t find her anywhere on the plane. Didn\u2019t know what happened to her. A few months later he goes to target and she is there working as a cashier."
      },
      {
        "id": "n0o44a8",
        "score": 171,
        "body": "You\u2019re proving his point loll"
      },
      {
        "id": "n0olbgk",
        "score": 111,
        "body": "Okay what the actual fuck. How did that end?"
      },
      {
        "id": "n0olfyv",
        "score": 110,
        "body": "I read it like the Filipinas had been military members stationed at Misawa and their husbands were Japanese. lol"
      },
      {
        "id": "n0onf8u",
        "score": 104,
        "body": "And a 40 something year age gap"
      },
      {
        "id": "n0oj2ng",
        "score": 83,
        "body": "A tale as old as time."
      },
      {
        "id": "n0o5cy8",
        "score": 68,
        "body": "People marry the people they're around \n\nNot exactly a startling development"
      },
      {
        "id": "n0nsj24",
        "score": 50,
        "body": "you mean like juicies? they have contracts to pay off. so it's never them."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1kd1v00",
    "title": "USAA Deals on Tires",
    "body": "Hey, I realized a lot of people didn\u2019t know this existed. If you\u2019re looking for new tires USAA paired up with Goodyear and you get 25% off your total at checkout. If you want to take it even further send that price over to discount tire they\u2019ll beat the price ( only about 10 bucks) and then you can apply an additional 5% military discount during checkout with them. I saved about $400 today doing this. Hope this helps someone.\n\nEDIT: if y\u2019all want a more step by step check out my comments down below. If you still have questions feel free to comment or fire me a pm \ud83d\ude0a I\u2019ll do my best to monitor the post the next couple days \n\nEDIT 2: USAA perks has way more than just this discount too it\u2019s worth going through the entire site. They have great deals on rental cars and can sometimes wave the age fee if you\u2019re under 25 for them. Sometimes there\u2019s also cheap tickets for theme parks and things as well. Definitely a resource more people should know about.",
    "flair": "Vet Discounts/Freebies :moneybags:",
    "score": 616,
    "comment_count": 97,
    "created_at": "2025-05-02T14:08:16+00:00",
    "top_comments": [
      {
        "id": "mq77nej",
        "score": 123,
        "body": "I've been getting tires through the Veteran's Canteen Service. The VCS gives fleet pricing on the tires for which you don't pay sales tax for the tires. You do have to pay for installation at the authorized tire outlet."
      },
      {
        "id": "mq7cqc2",
        "score": 32,
        "body": "I actually do need new tires, so this is timely."
      },
      {
        "id": "mq77ujy",
        "score": 30,
        "body": "Checked them out too, got a better deal going the other route though. Off road tires tend to be more expensive with canteen in my experience though."
      },
      {
        "id": "mq77jjz",
        "score": 21,
        "body": "I prefer Michelin but in a pinch saving money on any tire is great. Thanks for this!!"
      },
      {
        "id": "mq7eqns",
        "score": 20,
        "body": "What the fuck man, I just bought some tires for like 700 bucks \ud83d\ude2d"
      },
      {
        "id": "mq7epbe",
        "score": 19,
        "body": "I was debating about 5 different A/Ts and I saw a comment about USAA deep in an off-road forum. The timing was perfect for me so I shared it here hoping it would hit the right people \ud83c\udfaf"
      },
      {
        "id": "mq7fzb6",
        "score": 15,
        "body": "I\u2019m actually stationed down at Moody in Valdosta right now. I went through to USAA app to shop deals and typed in Goodyear tires. It takes you to their online storefront and automatically applies the 25% discount when you go through the app. You then have the option to have them delivered to you or to a participating tire shop near you and can calculate the install fees and everything at check out. Or like I said you can price match it to the nearest discount tire to you and grab that extra 5% off."
      },
      {
        "id": "mq7f1ju",
        "score": 8,
        "body": "At least you\u2019ll know for next time! After all the discounts I\u2019m still paying a lot tires are just expensive \ud83d\ude2d"
      },
      {
        "id": "mq7mc45",
        "score": 8,
        "body": "I went through to USAA app to their \u201cshop deals\u201dsection and typed in Goodyear tires. It takes you to their online storefront and automatically applies the 25% discount when you go through the app. You then have the option to have them delivered to you or to a participating tire shop near you and can calculate the install fees and everything at check out. Then you can screenshot that quote reach out to discount tire I used their chat feature sent them the photos of the quote and some info so they could find my store. 10 minutes later they sent me a quote beating the discounted quote from Goodyear an additional $10 and then I used ID me to apply an additional 5% discount tire military discount at checkout for another $61 off and had them sent to discount tire. When they mount it you get free tire maintenance and tire repair for the entire life of the tire as well. I bought a full set of 5 to have my spare done as well."
      },
      {
        "id": "mq85nib",
        "score": 7,
        "body": "Not exactly. You choose from [the listed options](https://www.vacanteen.va.gov/VACANTEEN/PatriotStoreDirect_Automotive.asp) and then call an 800 number to place your order. At that time they will tell you which tire place in your area is authorized to install them."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1ojcqof",
    "title": "Reminder to get your shoes",
    "body": "Went to my doctor about my plantar fascia issues and Achilles tendonitis. Got sent to the custom shoe store for orthotics and 2 new pairs of shoes. So glad they had athletic shoes and not all the old man looking deals",
    "flair": "Health Care :caduceus:",
    "score": 619,
    "comment_count": 173,
    "created_at": "2025-10-29T18:38:33+00:00",
    "top_comments": [
      {
        "id": "nm2024s",
        "score": 277,
        "body": "Flat feet and plantar fascitis and all my VA gives is 1 pair of off the shelf shoe inserts."
      },
      {
        "id": "nm23r0s",
        "score": 65,
        "body": "Follow up with foot appointments and communicate if the generic inserts dont work, they'll recommend custom inserts. Typically these are fitted at a larger facility like a VA hospital, and they are shipped directly to you from the manufacturer. whole process takes weeks and they're a tad bulky and may impact what footwear you pick. The foot support will be greatly improved.\u00a0"
      },
      {
        "id": "nm22c3v",
        "score": 44,
        "body": "Huh, this is actually a thing (new shoes I mean)??? I've only ever been given orthotics"
      },
      {
        "id": "nm268we",
        "score": 36,
        "body": "Ummm... he is an old man lol"
      },
      {
        "id": "nm30fm9",
        "score": 29,
        "body": " Bulky is an understatement. The only shoes I found that work for my VA issued inserts were my combat boots and chucks."
      },
      {
        "id": "nm25vhn",
        "score": 27,
        "body": "my husband is 81 and gets the old man ones, lol"
      },
      {
        "id": "nm20yq6",
        "score": 23,
        "body": "West LA VA gives you old shitty shoessssss. wtf what VA is this?"
      },
      {
        "id": "nm33vai",
        "score": 22,
        "body": "My VA podiatrists acts as if they will take the cost of the shoes out of his pay."
      },
      {
        "id": "nm24o46",
        "score": 17,
        "body": "I was issued only orthotic inserts from 2004 to 2022 then a podiatrist authorized two pairs of shoes with the new inserts. On my second pair of shoes/inserts."
      },
      {
        "id": "nm225nw",
        "score": 15,
        "body": "I don\u2019t have flat feet but I do have 2 knee replacements. My surgeon recommended getting these brooks ."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1o2il8j",
    "title": "Other?",
    "body": "Just wondering why there\u2019s a lack of information on my dav id card",
    "flair": "DoD/Federal Benefits :US_flag:",
    "score": 608,
    "comment_count": 201,
    "created_at": "2025-10-09T21:33:17+00:00",
    "top_comments": [
      {
        "id": "nioci1r",
        "score": 422,
        "body": "You don't have the clearance to know what service you were in!\n\nhttps://i.redd.it/wmg6rsuey5uf1.gif"
      },
      {
        "id": "nio3uoy",
        "score": 197,
        "body": "Must have been a government spook. Good on you! /s"
      },
      {
        "id": "nio27rg",
        "score": 154,
        "body": "They should have updated the system before printing the card."
      },
      {
        "id": "nio3i79",
        "score": 118,
        "body": "G7 classified"
      },
      {
        "id": "niqqegm",
        "score": 112,
        "body": "E4 Mafia is FO EVER"
      },
      {
        "id": "nipstf1",
        "score": 103,
        "body": "As long as that paycheck hit i\u2019ll be anything they want \ud83d\ude06"
      },
      {
        "id": "niobgbo",
        "score": 99,
        "body": "I believe you mean G14 classified\n\n![gif](giphy|xoHntNXFYkfzGAftEv|downsized)"
      },
      {
        "id": "nipoa5b",
        "score": 90,
        "body": "[deleted]"
      },
      {
        "id": "nio5x5w",
        "score": 76,
        "body": "Mine has Pay Grade, Rank, and Agency/Department"
      },
      {
        "id": "nipyoly",
        "score": 74,
        "body": "You will get better room rate now if you stay at shades of green at Walt Disney World."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1nzio0k",
    "title": "Getting your first decision letter be like ...",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 612,
    "comment_count": 40,
    "created_at": "2025-10-06T13:11:42+00:00",
    "top_comments": [
      {
        "id": "ni2jy0y",
        "score": 127,
        "body": "We acknowledge your disability, and that it has worsened over time, but there is no evidence of disability."
      },
      {
        "id": "ni2xzjx",
        "score": 61,
        "body": "At least it\u2019s service connected I\u2019ll take a 0 any day over an outright denial"
      },
      {
        "id": "ni2pss5",
        "score": 53,
        "body": "At least you got your shit granted. I literally had to appeal all of my shit just to get it service connected."
      },
      {
        "id": "ni36zdv",
        "score": 24,
        "body": "exactly! it is service connected and can increase at a later time. this is especially important if you are sitting at 90%."
      },
      {
        "id": "ni2juf7",
        "score": 17,
        "body": "Damn, not just me eh?"
      },
      {
        "id": "ni33iiw",
        "score": 11,
        "body": "Yeah, but 0% means it\u2019s service connected. I had struck up a conversation with a retired Senior Chief during one of my TAPs intermissions about his experience with VA claims. He said not to worry about a low score. Most issues get worse instead of better so he said to file for an increase. I took his advice and both of my claims at 0% were increased to their maximum value. It also means to VA will provide treatment for it should something happen down the road"
      },
      {
        "id": "ni44jwi",
        "score": 10,
        "body": "Absolutely! I was happy to rack up several 0%\u2019s. I wish they woulda rated my mental health claims at 0 instead of outright denial. I\u2019ve had favorable findings overall but got boned on my MH claims."
      },
      {
        "id": "ni450kr",
        "score": 9,
        "body": "That makes sense since it wasn\u2019t caused by military service, and cannabis use is illegal federally"
      },
      {
        "id": "ni2ncmf",
        "score": 6,
        "body": "It's a start!"
      },
      {
        "id": "ni3ehxt",
        "score": 5,
        "body": "And not just that u can still claim something secondary to it although it\u2019s 0"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1lq5o8p",
    "title": "Bragging online",
    "body": "Veterans need to stop bragging about how they are getting disability and still working a physically demanding job, or working out. These young kids I think they can just post everything online with no consequences and then argue how they have the freedom to just post everything they want.\n\nWe have enough going on with the VA trying to cut benefits without people posting online how they\u2019re getting 100% and then working the toughest physical demanding job what is wrong with people?",
    "flair": "VA Disability Claims :claim:",
    "score": 608,
    "comment_count": 208,
    "created_at": "2025-07-02T19:57:48+00:00",
    "top_comments": [
      {
        "id": "n103tjv",
        "score": 516,
        "body": "People need to stop worrying about other people\u2019s benefits.  You don\u2019t know why they are 100%.  You don\u2019t what they can and can\u2019t do.  You are not a doctor or rater.\n\nMost importantly it\u2019s none of your business."
      },
      {
        "id": "n10f5le",
        "score": 334,
        "body": "Compensation.\n\nStop calling it disability."
      },
      {
        "id": "n10nn60",
        "score": 172,
        "body": "[removed]"
      },
      {
        "id": "n109xpi",
        "score": 156,
        "body": "I work a mentally demanding job in a supervisor role. I go out regularly, I even am trying to get back into working out.\n\nWhat people don\u2019t see is last year when I didn\u2019t leave my house for weeks at a time or stopped answering calls and text for nearly all of 2024 because my depression spiked and it was exhausting to just deal with society. Or the medication I take on a daily basis. Or the fact that I struggle with binge drinking.\n\nIt\u2019s not bragging but I kinda have to do these things in order to not slip back into the symptoms of why I got my rating"
      },
      {
        "id": "n121z0o",
        "score": 72,
        "body": "Thank you.  I work out.  I work a physically demanding job.  My shit hurts.  I have social prosthetics to help me and if I didn\u2019t I couldn\u2019t even walk 100 yards. If anything it\u2019s a testament to how productive I can be BECAUSE of the VA."
      },
      {
        "id": "n104yox",
        "score": 70,
        "body": ">Most importantly it\u2019s none of your business\n\n\nDamn, shut the fuck up Friday came early."
      },
      {
        "id": "n10a6ds",
        "score": 65,
        "body": "The perception matters.\n\n\u201cPeople need to stop worrying about x\u201d has never stopped rubbernecking people from worrying about x even though it\u2019s none of their business.\n\nPeople need to stop posting about their disability in this political climate. Civilians hear \u201cdisabled veterans\u201d and they think of the people who lost limbs from IEDs, not the people who were in training accidents who have PTSD and migraines that don\u2019t *look* disabled. I got out in 2013 and I didn\u2019t even know that VA disability extended beyond things like the former, civilians are not going to educate themselves on this stuff."
      },
      {
        "id": "n10hsqz",
        "score": 49,
        "body": "Loser influencers like Caleb Hammer keep posting about VA benefits with the insinuation that vets are scamming the system. Wish vets would stop going on his show, or at least set him straight with his ignorant attitude."
      },
      {
        "id": "n109vov",
        "score": 42,
        "body": "Why can't a disabled veteran work out to the level they feel comfortable and safe doing?\n\nSuch a dumb take."
      },
      {
        "id": "n10jcv2",
        "score": 39,
        "body": "No, it's called VA disability compensation. I'm not disabled but I get compensation for disabilities caused to me. \n\nThe 21-526EZ is called Application for Disability Compensation and Related Compensation Benefits. \n\nDidn't realize the VA printed plates though."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1l7kjm0",
    "title": "The more times goes on the more I agree with the philosophy of tell NO ONE your disability rating!",
    "body": "It seems like anyone that becomes aware of your disability rating especially 100%, people even close friends begin to treat you differently. \n\nI watched this unfold very recently with a an acquaintance of mine who was granted 100% P&T! He being very happy that this had happened and told multiple people. All of a sudden it seems people think he\u2019s suddenly loaded\u2026 \ud83d\ude33 interestingly through all this as I was advising to do this and that for his claim process he never asked me what mine is and I think I\u2019m not going to tell him. \n\nAlso, something else I noticed , it seems like wives of friends get very nosy about how much disability you get, which was completely shocking to me. \n\nI don\u2019t know I\u2019ve seen lots of these posts on here and now I think I agree keep your trap shut.",
    "flair": ":Spanish_question_mark: Other :VA_logo: Stuff :Question_mark:",
    "score": 598,
    "comment_count": 161,
    "created_at": "2025-06-09T23:59:13+00:00",
    "top_comments": [
      {
        "id": "mwxkn7l",
        "score": 257,
        "body": "I had someone at work ask about my hearing aids. I told them they are for tinnitus and some\nhearing loss due to too many loud booms without hearing protection. They said \u201cwell I hope the VA is paying you for that!\u201d  I told them \u201cjust the hearing aids which is fine with me\u201d. The less they know the better."
      },
      {
        "id": "mwxkram",
        "score": 122,
        "body": "The way I look at it. I don\u2019t remember the recruiting office being closed after I visited and enlisted. Carry on, enjoy your life. Everything you have you earned"
      },
      {
        "id": "mwxfs2q",
        "score": 91,
        "body": "I always disagreed with this notion. Yes, horror stories are commonly told again and again, but if the people you surround yourself with change dramatically when your income changes dramatically, you're surrounding yourself with the wrong people.\n\nNeed to know always makes sense, you generally shouldn't be sharing information that's highly personal with everyone and anyone. However, you should absolutely have a close circle of friends and family you're able to share things with.\n\nIf friends or family start to abuse financial knowledge about you, you should cut ties with them."
      },
      {
        "id": "mwxkrmg",
        "score": 80,
        "body": "Personally, me, I don't give a shit. Everything that I have was granted to me, is medically and legally documented, so if they want to, they are more than welcome to follow a report with the VA. And it will be dismissed, expeditiously.\n\nAlso I don't participate in marathons or powerlifting on my free time and upload videos send photos to my social media."
      },
      {
        "id": "mwxm6os",
        "score": 49,
        "body": "I know several people who are at 100%, and every one of them completely deserves every cent of it!"
      },
      {
        "id": "mwxzuud",
        "score": 49,
        "body": "Good way to put it."
      },
      {
        "id": "mx0nxu0",
        "score": 43,
        "body": "I used to be one of those civilian friends that said \u201cmust be nice\u201d when my enlisted friend talked about benefits\u2026a few months later I enlisted myself because I realized there was nothing stopping me from earning free education but myself lol"
      },
      {
        "id": "mwxrdcn",
        "score": 39,
        "body": "My momma and my partner. Those are the only two I\u2019m telling. Why? Because they were there for me when I had nothing. I don\u2019t care if they want things from me later on. If I got, they can have it. They kept me from drinking my life away or doing drugs and eventually losing hope in humanity. \n\nThose two and God."
      },
      {
        "id": "mwxssea",
        "score": 37,
        "body": "Those are the people that make it look suspicious. Got 100% for bad knees and back, but check out my 650lb deadlift and the two Marathons I ran over the weekend. \ud83e\udd23"
      },
      {
        "id": "mwxjaox",
        "score": 35,
        "body": "[deleted]"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1k0l8r4",
    "title": "Having VA healthcare is honestly a godsend.",
    "body": "This is mostly just an appreciation post for VA healthcare, since I see a lot of negative sentiment towards the VA. \n\nBack in January, I tore my ACL and immediately went to the VA ER, they took X ray's and scheduled me for an MRI exam that coming week. Met with my surgeon and had to get a secondary MRI and a nerve test done. Yesterday, I had my ACL surgery done and everything went smoothly. I was in and out relatively quickly. All the people I interacted with were friendly and only interested in helping me. Keeping everything within the VA made life so much easier and the process less stressful. The VA gave me a custom knee brace alongside an Ice machine. \n\nKnowing that I have free healthcare for the rest of my life for anything I need, is honestly such a godsend. If I didn't use the VA, I would imagine my medical bill would probably be over 20k ( my nerve test alone was about 10k alone but covered by community care). The VA has its issues for sure, but the free healthcare definitely makes up for any short term issues I encounter. \n",
    "flair": "Health Care :caduceus:",
    "score": 604,
    "comment_count": 139,
    "created_at": "2025-04-16T14:05:00+00:00",
    "top_comments": [
      {
        "id": "mnetjtv",
        "score": 56,
        "body": "It really is. Had to come in this morning to get a toradol shot for pain. They are unfortunately a regular part of life. Thankful to have it covered"
      },
      {
        "id": "mnevobc",
        "score": 37,
        "body": "Stupid question here, but did you just go to the ER without needing anything else? If I broke a bone, can I just walk into a VA hospital and they\u2019ll take care of everything, free of charge? I\u2019m 100% P&T"
      },
      {
        "id": "mnexkok",
        "score": 34,
        "body": "Also if not near VA hospital at least they will cover it if they are notified within 72 hours if seen at civilian ER."
      },
      {
        "id": "mnf14yf",
        "score": 34,
        "body": "Lord have mercy you need to get up to speed in the AMAZING federal benefits unlocked to you via being P&T. \n\nDo you have dependents? \n\nYou also can walk into urgent care. \n\nYou also get paid travel for any / all of your medical appointments community care or VHA care. \n\nChapter 35?!\n\nChampVA?!"
      },
      {
        "id": "mneuksi",
        "score": 15,
        "body": "Agree, put off cataract surgery for years cause it was too expensive.  Got it done at the VA and no complications,  man I didn't know I was that blind lol"
      },
      {
        "id": "mnexoxb",
        "score": 11,
        "body": "No, I never saw combat. If you are service connected of atleast 10% all healthcare is covered except dental\u00a0"
      },
      {
        "id": "mnfyuxh",
        "score": 10,
        "body": "At 50% I\u2019m now in priority group 1!  Healthcare for life no copays. Va takes care of all my health issues SC or not!  Definitely a godsend for me!!!"
      },
      {
        "id": "mnf3snl",
        "score": 9,
        "body": "One of the best benefits of having full VA health coverage is being able to decline workplace health insurance, and save a butt-load per paycheck."
      },
      {
        "id": "mnew4pb",
        "score": 9,
        "body": "Yes that\u2019s exactly what I did. They just ask for your social. When I went to the ER, they passed the info along to my primary care doc who put in a referral for orthopedic and MRI.\u00a0"
      },
      {
        "id": "mnevonj",
        "score": 8,
        "body": "I am employed and have insurance through my employer, but I like having VA as a backstop.  I do use VA healthcare for my PTSD therapy and medication and I'm grateful for that.  I have talked to therapists in the community - my private insurance would pay for my therapy, but the therapists have zero experience with PTSD when I have asked.\n\nThis is actually why I fear the drive to privatize VA healthcare.  I don't want 'community care' for my MH therapy.  If my 'community care' therapist was not equipped to deal with military PTSD, I would not attend."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1riyrwu",
    "title": "Good work team!",
    "body": "Keep being loud and angry for the right reasons.",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 592,
    "comment_count": 28,
    "created_at": "2026-03-02T17:14:44+00:00",
    "top_comments": [
      {
        "id": "o89et2t",
        "score": 96,
        "body": "20k? Pump those numbers up big dawg."
      },
      {
        "id": "o89fd36",
        "score": 63,
        "body": "20.5k angry comments, 60 lawmakers, every veteran service organization, and multiple military newspaper articles.... Good work team"
      },
      {
        "id": "o8aze7l",
        "score": 24,
        "body": "Let's get more louder, angrier! They are really trying to cut out disability compensation!"
      },
      {
        "id": "o8anwrt",
        "score": 16,
        "body": "My bad. I meant that as there was a lot more than 20k people. You are correct, good work team."
      },
      {
        "id": "o8ab6m8",
        "score": 15,
        "body": "Yeah there are 200k vets in this sub alone, way too many people not commenting imo. Only takes a couple minutes"
      },
      {
        "id": "o8c0682",
        "score": 9,
        "body": "And MY axe! \ud83e\ude93 \ud83d\udcaa\ud83d\ude0e\ud83d\udd95"
      },
      {
        "id": "o8dvqa2",
        "score": 9,
        "body": "Oddly, there were posts by veterans telling other veterans to get involved, comment in the rule site, contact legislators, etc., who were down voted into oblivion by, I assume, other veterans on this sub. I don't understand that."
      },
      {
        "id": "o8cjmg3",
        "score": 8,
        "body": "That will disable me even more! \ud83e\udd23"
      },
      {
        "id": "o8aq9ho",
        "score": 8,
        "body": "Don't forget the dependants."
      },
      {
        "id": "o8cyh1u",
        "score": 7,
        "body": "Idk why they want to fuck with guys who have literally been trained to kill, and they're targeting the mentally unstable ones at that."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1o2pl87",
    "title": "Hey WaPo, I found a Veterans Benefits story for you. This is far more common than the fraud you're hyper focused on, BTW.",
    "body": "",
    "flair": "Headlines & News :rsz_21601:",
    "score": 597,
    "comment_count": 7,
    "created_at": "2025-10-10T02:54:58+00:00",
    "top_comments": [
      {
        "id": "nipm20v",
        "score": 309,
        "body": "https://www.wsbtv.com/news/local/navy-vet-says-va-cut-her-disability-check-half-over-job-she-never-had/A72RKJKN7NFQ3LDNKWUVJJSJLI/\n\nFound the story.\n\nLooks like TDIU.\n\nUnfortunately, this is why you never skip mail from the VA. For TDIU, I believe they send you at least 3 letters about your earnings and then 2 more when they propose to reduce you."
      },
      {
        "id": "nipq3yf",
        "score": 55,
        "body": "Please make this the top comment."
      },
      {
        "id": "nipm1oz",
        "score": 49,
        "body": "[removed]"
      },
      {
        "id": "nipqltk",
        "score": 27,
        "body": "Why would they reduce you?"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1qgkg4l",
    "title": "ChampVA - Hoping to clear up widespread confusion",
    "body": "I see many people struggling to find a Dr that accepts ChampVA. I have a cheat code for you.\n\nOK, not a cheat code perhaps, but it works just like one. I live in a very non-military area. I'm 30 miles from a small Great Lakes Coast Guard station and ninety miles from an Air National Guard base. 180 miles away is an Army post with all of 200 active duty soldiers.\n\nNobody has ever heard of ChampVA. Sound familiar?\n\nOn the ChampVA card in red is a billing code: 84146\n\nWhen they look at you blankly when you say ChampVA, ask them to see if that billing code is in their system. Nearly always it will be and all of your problems are solved.\n\nEdit: it may not be on your card (it is on my wife's new card) but the number is good. Write it down and ask.\n\nEdit 2:\nBecause I'm getting tired of replying to the MANY people commenting \"almost\" correctly:\nNo, doctors aren't forced to accept CHAMPVA just because they take Medicare, but hospitals and hospital-based providers that accept Medicare must also accept CHAMPVA. But, MOST doctors that accept Medicare will also accept ChampVA - even if they don't know it. So, give them the billing code.\n\n \n",
    "flair": "Health Care :caduceus:",
    "score": 592,
    "comment_count": 105,
    "created_at": "2026-01-18T21:12:49+00:00",
    "top_comments": [
      {
        "id": "o0cy3uj",
        "score": 128,
        "body": "This is actually genius, thanks for posting this. I've been dealing with the blank stare thing for months and had no idea about the billing code trick"
      },
      {
        "id": "o0d5d8r",
        "score": 51,
        "body": "Holy shit, ive been fighting with my pharmacy about this champva stuff for the last 6 months. I was actually beginning to think it was worthless. Im definitely gonna give them this number. Thanks, bro!!"
      },
      {
        "id": "o0cyjb0",
        "score": 50,
        "body": "I\u2019ve heard mentioned here if they accept Medicare or tricare then they\u2019ll accept the Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA)"
      },
      {
        "id": "o0dm1i0",
        "score": 31,
        "body": "In case you didn't know, there are two different pharmacy aspects to CHAMPVA.  There is a mail order one that is handled by Meds by Mail and a bricks and mortar one that is covered by OPTUMRx.  You need to present your OPTUMRx card at the participating bricks and mortar pharmacies.  If you get meds filled at a bricks and mortar pharmacy you have a 25% copay.  Meds by Mail is free."
      },
      {
        "id": "o0d01g6",
        "score": 23,
        "body": "Yes it is filed on a Medicare from. My wife has had Champva for 16 years never a problem and now that she is on Medicare it acts as secondary she has not been out one penny."
      },
      {
        "id": "o0epuob",
        "score": 23,
        "body": "What's \"facebook?\""
      },
      {
        "id": "o0d4jo8",
        "score": 21,
        "body": "I just qualified for my wife to get ChampVa last year and she is going on Medicare next month. Very much looking forward to zero deductibles and co-pays! Because she is self-employed, we've been paying $1000 a month for a plan with an $8000 deductible!\n\nDecided to stick to \"original\" plan B for now to maintain maximum flexibility. $2,500 a year isn't nothing but it sure beats the $20,000 we paid two years ago (and $12-18k a year when she was healthy)!"
      },
      {
        "id": "o0e7mg9",
        "score": 20,
        "body": "Check them voicemails when you get time \ud83d\ude02"
      },
      {
        "id": "o0dnczd",
        "score": 13,
        "body": "https://preview.redd.it/p6gwtf2dy6eg1.jpeg?width=1290&format=pjpg&auto=webp&s=a5b449db10799d6379f8dcc1094946a2f0eb004f\n\nThanks!"
      },
      {
        "id": "o0dk7rk",
        "score": 12,
        "body": "Yeah its not on the cards which is confusing to a lot of people and doc offices."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1kkz0it",
    "title": "It\u2019s called The Deployment Diet.",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 585,
    "comment_count": 46,
    "created_at": "2025-05-12T17:49:51+00:00",
    "top_comments": [
      {
        "id": "mryapq2",
        "score": 29,
        "body": "Literally everyone in the infantry."
      },
      {
        "id": "mrybmhv",
        "score": 19,
        "body": "PFAS and mold adds to the flavour"
      },
      {
        "id": "mrycnyw",
        "score": 17,
        "body": "You\u2019re forgetting nicotine and broken dreams."
      },
      {
        "id": "mryinvq",
        "score": 17,
        "body": "I think my time on convoys, being given a *literal case* of Rip-Its, every night for fourteen months may have caused some long-term damage. My daily Green Bean MoAC before heading to the staging lanes probably didn\u2019t help.\n\nBut the alternative was to fall asleep at the wheel or miss something and get blown up.\n\nAnd the citrus ones were fucking delicious, especially when mixed in a Gatorade."
      },
      {
        "id": "mrycu3q",
        "score": 10,
        "body": "You forgot the 3200mg of motrin everyday.  \n\nDrink a quart of coffee with 800 mG 4 times a day to fix those knees that have been pounded to rubble."
      },
      {
        "id": "mrydlo0",
        "score": 7,
        "body": "The foundation of that pyramid is nicotine"
      },
      {
        "id": "mry9qfx",
        "score": 6,
        "body": "Don\u2019t forget the mystery meat from the chow hall...adds that essential layer of \u201cI might be immortal now but at what cost.\u201d"
      },
      {
        "id": "mryj70c",
        "score": 5,
        "body": "Plus smoking jp- 8 all day"
      },
      {
        "id": "mrybsbm",
        "score": 5,
        "body": "Spicy blue cheese. Mmmm."
      },
      {
        "id": "mrz19rb",
        "score": 5,
        "body": "I find it interesting and hilarious that for many, we don't even find out about the things we are exposed to until after we are already out."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1kv1li5",
    "title": "Ignoring my VSO - best decision I've made - Tinnitus claim",
    "body": "Ok.  First and probably last post here...but I thought I owed it to you all to share my brief story since this subReddit gave me the background and experience of those who have gone it alone with better success.\n\nFirst - I'm old.  I left the service 30+ years ago.  Like many, I came out with T but never complained.  Fast forward to present, my wife talked me into making a claim if only for the hearing support.  I found a local VSO since I had no clue what I was doing - I just didn't know they didn't know what they were doing either.  The initial claim got denied (surprise, surprise).  Trying to get hold of them for next steps....crickets.  Finally get through and they don't want to waste their time with me.  VSO literally says my claim is DOA anyway, and he would advise against wasting time on an HLR.  Why?  Because he says he can see that my entry and exit audiograms showed no changed in my hearing and that tinnitus needs measurable difference at the exit exam to support a strong C&P rationale. I offer up the 'Well, I could lawyer up!' in a pique of irritation and he responds, 'You do that.'  And then he wishes me good luck and ends the call.\n\nNow I'm pissed.  I start researching and trying to figure out what to do to breathe life back into my 10% claim.  I finally realize I'm stumped.  Screw it...I file an HLR after 7 months of hemming and hawing.  Get my conference, and the Sr. Reviewer is cool and copacetic.  Listens to my story, he looks at the docs and says, 'You could get a nexus statement from an ENT and file a supplemental claim.'  I responded, I have that in the records I've submitted.  He looks and says, 'By gum...you're right.  They did not reference that in your denial letter'. Taaadaaa.  A Duty to Assist Error was born.\n\nFast forward again and I've completed a follow up C&P (I think that like 4 or 5 audio exams I've had at my VHCC), and the wait begins.  I check on the app a couple weeks ago, and it says I'm service connected for Tinnitus, 10%.  Just got my letter.\n\nOut of curiosity, I looked in my VA health records to see what the C&P exam said.  Wouldn't you know it, I never had an exit physical.  My VSO lied straight to my face.  My VSO never looked at the documents that were reviewed as part of the denial.  My VSO did not want to waste his time with an old fart who can't stop the ringing which started in 1990.\n\nIn other words, I have had the same experience as many on this subReddit.  There may be some good VSOs out there who will work and advocate for you...but I did not get lucky and pick that one.\n\nSo the take home messages:\n\n1. Old vets CAN get rated for tinnitus - don't listen to anyone else.  File your claim.\n2. VSOs are only as good as your gut says they are...if they are uncommunicative and not actively advocating for you and helping you FIGHT, FIGHT, FIGHT!!  Then dust them off quick...because they already don't care.\n3. After you do some research and read some of the experience on this subReddit, you'll probably have more knowledge and eagerness to Fight than your VSO ever did.\n4. Lastly - you are worth the time and effort it takes to do what is in your best interest.  Don't expect anyone to fight for you.  You are a warrior - you are fully capable of fighting your own battle!\n\nPeace...",
    "flair": "C&P Exams :stethoscope:",
    "score": 587,
    "comment_count": 221,
    "created_at": "2025-05-25T12:41:01+00:00",
    "top_comments": [
      {
        "id": "mu5w4tz",
        "score": 84,
        "body": "Not surprised.  My Local VSO never returned my calls. In my opinion they're a complete waste of time.  Did everything on my own with the help of this sub and youtube"
      },
      {
        "id": "mu5w9hk",
        "score": 69,
        "body": "I went to a VSO once and he filed the wrong paperwork. I have done all my claims by myself with help from this sub and the r/veterans sub."
      },
      {
        "id": "mu5xs11",
        "score": 67,
        "body": "My personal experience: VSO's suck and you can get far better free advice here and from YouTube."
      },
      {
        "id": "mu5xawe",
        "score": 46,
        "body": "I used DAV VSO and a lawyer. Lawyer ghosted me for months with the occasional we are still working on your claim stuff. This went for over a year with no actual substance in any update. Reported them to state bar and they had an admonishment placed in their file or something.\n\nSwitched to DAV and they told me I couldn't file.\n\nIgnored them files all my conditions anyway, at 100% p&t now and both DAV and that lawyer can smd."
      },
      {
        "id": "mu5xk7u",
        "score": 41,
        "body": "Great advice.  After my initial denials I began educating myself.  The webpage associated with this sub is outstanding.  I went through all that.  I watched about 200 hours of content online.  I went to the doctors and got medical records online to support my claim.  I got medical opinions.  I then filed supplementals, and one HLR, all were approved.  You are your own best advocate.  And I waited 24 years after separating before my first file."
      },
      {
        "id": "mu5w3lx",
        "score": 34,
        "body": "Good for you! Nicely done for being persistent. This proves that no one cares about your claim more than you do."
      },
      {
        "id": "mu5wk4r",
        "score": 19,
        "body": "When I got my tinnitus rating, although they did a new hearing test on me, to my understanding, hearing loss was not a requirement. It certainly is not the consensus in the Tinnitus/Neurological/Audiological community.  You can have hearing loss and NO tinnitus, and NO hearing loss AND tinnitus. Also, Tinnitus is associated with high frequency hearing loss that may not be picked up on an audiogram.\n\nTinnitus is due to a malady within the audio/brain pathway, which is why some people experience it (just like migraines), and some people don't. \n\nLook up Tinnitus Labs (guy named Anthony) on Youtube.  He is actually making strides while everyone waits for the Susan Shore Device to be approved by the FDA."
      },
      {
        "id": "mu8blq2",
        "score": 19,
        "body": "I avoided them after reading the horror stories. This sub gave me what I needed to get to 70% MH on my own and on the first go around. \n\nI applied a year ago after being out since 2011 btw."
      },
      {
        "id": "mu8i8bg",
        "score": 19,
        "body": "Facts! Literally learned everything I could from Reddit/YT/FB and only went to the VSO to submit everything."
      },
      {
        "id": "mu5xtr6",
        "score": 17,
        "body": "Kind of the same thing here, a friend recommended that I contact the County VSO to get help filing my claim (been out 30 years). I scheduled an appointment and spoke with two of them, they didn\u2019t seem all that interested but told me to call them back when I completed my intent to file. I called multiple times, never could reach anyone, left multiple voicemail messages. They never called back. Well about a month before my intent to file expired I said screw it, found this page and started reading. Filed my claim on my own about a week before my ITF expired and got %70 first time.  This page is amazing with all of the information available."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1jilptp",
    "title": "Me Thinking Tinnitus Would Get Me From 90%-100%",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 582,
    "comment_count": 68,
    "created_at": "2025-03-24T08:11:23+00:00",
    "top_comments": [
      {
        "id": "mjg7o9w",
        "score": 91,
        "body": "[deleted]"
      },
      {
        "id": "mjg8uwi",
        "score": 54,
        "body": "Anyone find a god damn cure for this yet? I swear either I\u2019m progressively going deaf or the tinnitus is getting louder."
      },
      {
        "id": "mjhiasj",
        "score": 31,
        "body": "Every time I hear the \u201ctinnitus ring\u201d on a movie I tell my SO that\u2019s what I hear\u2026 she still doesn\u2019t believe me \ud83d\ude02"
      },
      {
        "id": "mjh0yct",
        "score": 25,
        "body": "I hit 95%, WITH Tinnitus.  So yea, every little bit helps.  Sure the larger ratings carry the major lifting, but any way you slice it, without my 10% Tinnitus I would be 94%, rounded DOWN.  Thank God I found the internet and lots of good information via Youtube videos and Reddit on what counts, what doesn't, and how to file a fully developed case.  I would include facebook, but they keep disabling my account for absolutely no reason so I abandoned farcebook."
      },
      {
        "id": "mjil3eq",
        "score": 23,
        "body": "Only if you were at 94%. Got to love VA math."
      },
      {
        "id": "mjjb9ik",
        "score": 21,
        "body": "I have my wife by my side. I am not in the need for any extra babbling."
      },
      {
        "id": "mjgydnd",
        "score": 19,
        "body": "VA math is the hardest math (unless you\u2019re a rater; I can confidently rate ALS with higher level SMC but I\u2019m going to call at least 3 people if I have to rate multiple eye conditions, and none of us will feel super great about it)."
      },
      {
        "id": "mjgmgif",
        "score": 13,
        "body": "They have hearing aids noise machines now where you can constantly hear a babbling brook"
      },
      {
        "id": "mjh1lbn",
        "score": 13,
        "body": "Agreed.  10% using VA math seems useless until you are poised on a 94% and that 10% of your remaining 10% gives you that 1% that pushes you to 95% and it rolls up to 100%.\n\nI'm not turning down anything.  I'm 10% Tinnitus, 0% hearing, and 50% PTSD.  Got an HLR and two new claims in since then."
      },
      {
        "id": "mji1cbt",
        "score": 12,
        "body": "Mawp"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1pz1em9",
    "title": "Payment schedule for 2026",
    "body": "Hope this helps someone. \ud83e\udee1",
    "flair": "VA Disability Claims :claim:",
    "score": 577,
    "comment_count": 108,
    "created_at": "2025-12-29T23:14:26+00:00",
    "top_comments": [
      {
        "id": "nwmsoea",
        "score": 155,
        "body": "Wishing the best for all who haven\u2019t been helped for 2025, will get the help they need in 2026."
      },
      {
        "id": "nwn3k42",
        "score": 106,
        "body": "What\u2019s the point\u2026we\u2019ll still be the monthly \u201cdid ya\u2019ll get paid\u201d posts?"
      },
      {
        "id": "nwofke2",
        "score": 71,
        "body": "Because some of the vets in here live pay check to pay check on 100% disability because they're too fucked up from their deployments to hold a job down and cant live and support a family off 40 grand a year... Whether they can barley walk because of pain without assistance, are an amputee or are out of it mentally.\u00a0\n\n\nSome of them would literally be homeless without that monthly payment and when it shows up early one month then late the next, their bills bounce because unlike our disability, monthly bills come out at the same time every month regardless if you got your disability late or early.\u00a0\n\n\nThe real question is if it bother you so much what are you doing on a thread about when we are getting our disability? Its like yall come to these specific threads strictly to dog on those disabled vets that rely on these checks to live...\n\n\n\"GOD, im sick of going to threads that talk about this specific thing that I have to go out of my way to find and comment on. If only there was something I could do to not see these posts that irritate me so much!\"\n\n\nThats yalls logic here..."
      },
      {
        "id": "nwmvb1l",
        "score": 64,
        "body": "[deleted]"
      },
      {
        "id": "nwnnc0f",
        "score": 58,
        "body": "I'll never understand why people are obsessed with needing it to be earlier. You get one each month. Whether it's two days earlier than Bob doesn't change that it's only one time.\n\nIt's only a problem if it doesn't come at all."
      },
      {
        "id": "nwn0t11",
        "score": 52,
        "body": "I am 100 P&T 1 wife and my daughter I think my pay is going to go up to 4340 this coming new year. God bless all of you brothers and sisters. Army strong RLTW <3>"
      },
      {
        "id": "nwo1hnd",
        "score": 46,
        "body": "I think it is a simple matter of budgeting."
      },
      {
        "id": "nwn30o3",
        "score": 20,
        "body": "[deleted]"
      },
      {
        "id": "nwom0dc",
        "score": 20,
        "body": "I moved all my bills to the first three days of the month. Ever since doing that, my compensation check pays for it all. Ever since doing that I\u2019ve been okay. I recommend it for anyone who can do that to do it. I can\u2019t work like many of us but it helps. Do you budget too?"
      },
      {
        "id": "nwn2f9b",
        "score": 16,
        "body": "Give em one"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1otkvz6",
    "title": "Im doing it",
    "body": "",
    "flair": ":snoo_tongue:Meme Monday:snoo_joy:",
    "score": 573,
    "comment_count": 93,
    "created_at": "2025-11-10T17:59:43+00:00",
    "top_comments": [
      {
        "id": "no58ayb",
        "score": 377,
        "body": "Make sure you come back in 2028 and let us know how it went."
      },
      {
        "id": "no5bp17",
        "score": 285,
        "body": "The only people who are dumb for poking the bear are those with 100%."
      },
      {
        "id": "no58f8z",
        "score": 141,
        "body": "Unless you\u2019re severely lying or you walk in to your exam doing jumping jacks I don\u2019t think it\u2019s a problem, the people who are 100% and go for more money are the dumb ones"
      },
      {
        "id": "no59bz0",
        "score": 74,
        "body": "![gif](giphy|kC8N6DPOkbqWTxkNTe)"
      },
      {
        "id": "no5upc4",
        "score": 47,
        "body": "Well. Yes, and no. If your married and you wan't your spous to have benefits after you die, then it's smart to keep getting rated for those ailments that are service-related because if you die from something service connected, your spouse would be entitled to continue receiving a portion of your VA benefits."
      },
      {
        "id": "no5e186",
        "score": 46,
        "body": "I will never understand risking your 100% like that."
      },
      {
        "id": "no58tm0",
        "score": 45,
        "body": "It's NOT poking the bear when you're 80% and looking to increase."
      },
      {
        "id": "no5c476",
        "score": 38,
        "body": "Poke me, daddy."
      },
      {
        "id": "no5l0ae",
        "score": 35,
        "body": "Because housebound is another $500.\n\n![gif](giphy|0NAxDmdrb9t8aA2yh2|downsized)"
      },
      {
        "id": "no6hurs",
        "score": 30,
        "body": "If your 100% P&T for over 10 years you can die of anything"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rlnh7z",
    "title": "New VA app feature",
    "body": "The VA app now allows veterans to see there Certificate of Eligibility - Home Loan Letter.",
    "flair": "VA.gov/VA App :VA_logo:",
    "score": 6,
    "comment_count": 3,
    "created_at": "2026-03-05T17:20:54+00:00",
    "top_comments": [
      {
        "id": "o8t9rsk",
        "score": 1,
        "body": "I am enjoying this new dedication to making the VA efficient and ready for new technology.  This is completely different from the VA of the 2000s and early 2010s."
      },
      {
        "id": "o8ta92i",
        "score": 1,
        "body": "Saw it this morning.  Great new feature!"
      },
      {
        "id": "o8tbhue",
        "score": 1,
        "body": "https://preview.redd.it/e24sqc4ei9ng1.jpeg?width=1179&format=pjpg&auto=webp&s=9949acbbb9591a4bf885bacc1e42d3fd5259d78c\n\nlol. I was excited and wanted to see."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rlm5e6",
    "title": "Checking your disabilities static status",
    "body": "https://api.va.gov/v0/rated_disabilities\n\nFound this on a FB page. Basically log into the VA, open a new tab and click the icon in the upper left hand. This will list all your current disabilities and state of services connected, % and if they are static.",
    "flair": "VA Disability Claims :claim:",
    "score": 6,
    "comment_count": 6,
    "created_at": "2026-03-05T16:31:24+00:00",
    "top_comments": [
      {
        "id": "o8t42cy",
        "score": 9,
        "body": "It is also in the Knowledge Base.\n\n[https://www.veteransbenefitskb.com/static-check](https://www.veteransbenefitskb.com/static-check)"
      },
      {
        "id": "o8sy7oj",
        "score": 3,
        "body": "holy shit this is actually useful, just checked mine and had no idea half my stuff was marked static already. been wondering about that for months but never knew where to look\n\n  \nthanks for posting this, way easier than calling and sitting on hold forever"
      },
      {
        "id": "o8t6bom",
        "score": 1,
        "body": "Here is also an excellent tool that is a plugin extension for your Chrome Browser.  I used it extensively tracking my claims:  [https://www.reddit.com/r/VeteransBenefits/comments/17qr058/va\\_claim\\_tracker\\_chrome\\_extension/](https://www.reddit.com/r/VeteransBenefits/comments/17qr058/va_claim_tracker_chrome_extension/)\n\n"
      },
      {
        "id": "o8ten7k",
        "score": 1,
        "body": "Holy Crap!  I just did this although the [VA.gov](http://VA.gov) link is bad now so just open a new tab and type it in yourself then follow the instructions given on the one below on the link for the knowledge base. I just finished one of my rating appeals to increase my ptsd which I just got granted last year and also did an increase which again just got granted this month and its listed as static now!  Thank you!  I do learn a lot from here and now if I can just get that last 10!!  They of course denied a slew of things already and that was my like 3rd round on some of my stuff a lot they kept using TERA but if I get it this round will not poke the damn bear at all but its been a long journey for me and I appreciate much to my fellow vets here! Wish me luck, finished the feet cp exam yesterday and its my last one, they deferred my tinnitus and the feet so that is what is left.  Been fighting for a long time my PTSD and thankful to finally have it and feel vindicated that someone beliefs me what happened in the Army for me!!!"
      },
      {
        "id": "o8tgmhs",
        "score": 1,
        "body": "This is largely moot as almost all claims are rated static by default for the past 5 years. "
      },
      {
        "id": "o8tbr1u",
        "score": 1,
        "body": "You know people don\u2019t read the about section here cmon"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rlktpq",
    "title": "DIC question",
    "body": "So I am 100% P&T and have been so since January 2019.  I was at 90% effective 2015.  The only things that changed to get to the 100% were tension headache increase that pushed me over.   for DIC, if a service connected doesnt take me out, then  it says 10 plus years.  Does that have to be 10+ years from the effective date of 100% or do they factor in any other dates from previous percentages?\n\nThe reason I am asking is in the last 12 months, I have been diagnosed with 2 rare tumors and 1 not so rare tumor ( 3 total) as well as having a workup for ALS that thankfully turned out to be BFS instead ( at least for now).   I don't want to poke the bear and don't really intend to, but I am also nervous that these can cause issues down the road.  2029 is 3 years away and there is no telling if anything can progress or change between now and then.\n\nSo is it really 10 years for DIC for 100% P&T or does it factor anything else in.  Thanks!\n\n  \nEdit to add: Tumors are benign ( they think)",
    "flair": "VA Disability Claims :claim:",
    "score": 0,
    "comment_count": 12,
    "created_at": "2026-03-05T15:40:44+00:00",
    "top_comments": [
      {
        "id": "o8sov71",
        "score": 3,
        "body": "10 years or longer from the effective date of 100% if death is due to a non service connected disability.  If it is a service connected issue or complication of a service connected issue, time does not matter."
      },
      {
        "id": "o8soqim",
        "score": 2,
        "body": "The 10 year clock starts from your 100% P&T effective date, so January 2019 in your case. Your earlier 90% rating doesn't count toward that timeline unfortunately\n\n  \nReally sorry to hear about all the health scares you've been dealing with - that's a lot to process in one year. The benign tumor news is at least some relief, and dodging the ALS bullet has to feel huge"
      },
      {
        "id": "o8ssk73",
        "score": 2,
        "body": "Im not sorried about the treatment, I already have that. I was just looking at info since those arent service connected, how does it work if any of that took me out before I reach 10 years 100% in 2029.  I would have to poke the bear to get them service connected, which i DO NOT plan to do."
      },
      {
        "id": "o8t5ukh",
        "score": 1,
        "body": "Look...if you have a apouse...make sure you set up to take of them. I'm 100% P&T  July 2024, I'm 63 with two claims that needs sc for DIC. I'm not listenimg to that *poking the bear crap* , I'm making sure my wife is good to  if it's needed. I must say that I feel safe with 18 to 19 rated items  and the VA have reviewed my file with SSDI.(Inside Tip). I had one items adjusted not reduced because 10% vertigo was added with 10% tinnitus which is now 10% tinnitus w/vertigo. Keep your documents and treatments updated !!!\n,"
      },
      {
        "id": "o8spvo6",
        "score": 1,
        "body": "Thank you"
      },
      {
        "id": "o8splqo",
        "score": 1,
        "body": "Yea it is a huge relief. But then again ALS is also just a waiting game, So yea it is BFS now, but that can change. But I take huge relief knowing I don't have to have it on my mind for now. Its just annoying that these are all popping up, None of them are service connected.  Deployed to Iraq twice at the beginning. IDK if it has anything to do with it. Def annoying for sure. "
      },
      {
        "id": "o8spudm",
        "score": 1,
        "body": "No, Im worried that my new diagnoses from the past 12 months have a chance to cause further issues.  But I dont want to poke the bear and will just ride it out I for now I rekon.  Just planning for the future. "
      },
      {
        "id": "o8stnze",
        "score": 1,
        "body": "Oh ok. You are asking about dependent benefits after you are gone?  That sucks you are having to think about that\nFor some reason I was thinking those kicked in after 8 years, but it looks like several other commenters are saying 10 years"
      },
      {
        "id": "o8spx65",
        "score": 0,
        "body": "Don't poke!!!!"
      },
      {
        "id": "o8sq3bl",
        "score": 0,
        "body": "I dont plan on it.  Just looking in to things to plan ahead. "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rlkjpv",
    "title": "Richard star act",
    "body": "[ https://www.veterans.senate.gov/2026/3/senate-republicans-block-benefits-for-combat-injured-veterans-amid-ongoing-military-conflict-in-iran ](https://www.veterans.senate.gov/2026/3/senate-republicans-block-benefits-for-combat-injured-veterans-amid-ongoing-military-conflict-in-iran)\n\nBlocked again",
    "flair": "Headlines & News :rsz_21601:",
    "score": 12,
    "comment_count": 6,
    "created_at": "2026-03-05T15:29:46+00:00",
    "top_comments": [
      {
        "id": "o8svu99",
        "score": 8,
        "body": "This sucks but I have never understood why this bill is limited to combat injured veterans instead of all injured veterans. It would likely get more support if it would just include all injured veterans"
      },
      {
        "id": "o8sy56d",
        "score": 6,
        "body": "It got blocked by 1 Republican not the whole party. \n\nThey tried to do a uniamous consent option on this bill and Ron Johnson voted No. So now it has to go to a full Senate vote on the bill"
      },
      {
        "id": "o8t3j5t",
        "score": 2,
        "body": "I don't have any idea if or when it will go to the full Senate vote"
      },
      {
        "id": "o8tgdzz",
        "score": 1,
        "body": "Now that\u2019s some bs "
      },
      {
        "id": "o8thley",
        "score": 1,
        "body": "MOTHER FUCKER. Ughhhh. \n\nI\u2019m one of the 80,000 that this would apply to. I get 100% VA and a nice chunk for CRSC but not like if I got my Maj pay and 100%. "
      },
      {
        "id": "o8t2jb9",
        "score": 1,
        "body": "Thanks for the explanation. Do you have any idea when it will go before the full Senate, or what happens overall from here?"
      },
      {
        "id": "o8t7cdk",
        "score": 1,
        "body": "Okay. You know more about how it works than I do I am guessing so I thought I would ask lol"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rljc17",
    "title": "VA Rating?",
    "body": "I completed my first contract from 2014-18, no sick call visits honorable DC. Then I turn around and rejoined in 2022 and then I got kicked out in 2023. I got a general under honorable. Because something happened...\n\nI remember it was so bad that I came to reddit and posted under the Army subreddit and I said I was looking to get a pew pew and off myself. Then my unit found my post. They called me and told me to come see them. I stood by and the medical captain of my unit asked me if I was sad. I said no and kept saying no because I wanted them to believe me. \n\nThen they took me to the base hospital to speak with a medical captain there. I of course kept lying but I could tell they didn't believe me.\n\nFast forward to 2025, I went to MEPS to try and join again because I had to wait a year. And the medical personnel that was checking me out said they had a screenshot of that reddit post on my medical record confirming that I wanted to get a pew pew and off myself and on top of that. My records also said I had Borderline Personality Disorder. So I was told I was DQ'd from ever joining the military again.\n\nSo with that information on my record could I make a claim with the VA to get a disability? I know BPD isn't ratable I'm talking about the other stuff.\n\nThanks\n",
    "flair": "VA Disability Claims :claim:",
    "score": 1,
    "comment_count": 13,
    "created_at": "2026-03-05T14:41:01+00:00",
    "top_comments": [
      {
        "id": "o8sq4fj",
        "score": 4,
        "body": "How\u2019d they even know it was you on Reddit?"
      },
      {
        "id": "o8svn1e",
        "score": 3,
        "body": "\"because something happened...\"\n"
      },
      {
        "id": "o8sqhuy",
        "score": 2,
        "body": "I put my unit name in the post, but idk how they found out. "
      },
      {
        "id": "o8seugi",
        "score": 1,
        "body": "You can claim anything you feel worthy. It just so happens you have a strong case that your mental issues are service connected. "
      },
      {
        "id": "o8sqe2o",
        "score": 1,
        "body": "Yea what he said. Good luck "
      },
      {
        "id": "o8t7y25",
        "score": 1,
        "body": "Yeah interesting how they found your post on here that\u2019s why I semi watch what I say here just so they don\u2019t use it against me just in case they peruse these sites"
      },
      {
        "id": "o8t9fh3",
        "score": 1,
        "body": "lol"
      },
      {
        "id": "o8suzjw",
        "score": 1,
        "body": "think my case would be strong with that reddit post being on file?\n"
      },
      {
        "id": "o8t918z",
        "score": 1,
        "body": "they also sent me to Behavior Health, and the guy had a screenshot of my reddit post in his email he clicked it up and showed me. I went str8 to lying lol"
      },
      {
        "id": "o8t9odj",
        "score": 1,
        "body": "what"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rli72f",
    "title": "Advice - Stroke (from non military spouse)",
    "body": "Husband is 100% P&T, still in AF Reserves, and has full time civilian job with ok insurance.\n\nHe had a stroke last Saturday, 2/28, went via ambulance to closest hospital with stroke care. Was in ICU for almost 5 days, has now been moved to a lower unit.\n\nI am not military and was not aware of the possible VA help/assistance and just wanted a direction to go. As soon as I found out about it, I was given the 72 hour line to call and make a claim. I think my math puts that call at 75 hours. The gentleman that entered the emergency claim was so helpful and kind, trying to let me know next steps, but not mush he could really say. Also, I spoke to the rehab campus he will be transferred to next and she has worked with the VA and said has approval.\n\nI have seen people on here say the VA isn't 'Insurance', which I understand, but should I keep waiting to hear if the VA will work with my husband's other insurance to help get it all worked out and covered for the emergency part? Or did I miss my 72 hour window and just go with his civilian insurance, which would cover maybe 80% of this if we're lucky, and is probably hundreds of thousands at this point.\n\nJust looking for viewpoints to try to make sure I'm doing to best decision I can. Thank you all.",
    "flair": "Health Care :caduceus:",
    "score": 7,
    "comment_count": 4,
    "created_at": "2026-03-05T13:53:47+00:00",
    "top_comments": [
      {
        "id": "o8s3c7i",
        "score": 4,
        "body": "really sorry your family is going through this, strokes are terrifying. the 72 hour thing isn't a hard cutoff for emergency claims - you're close enough that it shouldn't matter, especially since you called as soon as you knew about it\n\n  \nthe va will coordinate with his other insurance since he's 100% p&t, they should handle most if not all of it. keep pushing with both the va case worker and the rehab facility's va coordinator, they deal with this stuff all the time and know how to navigate it. don't panic about the civilian insurance timeline yet, let the va people work their magic first"
      },
      {
        "id": "o8s65h6",
        "score": 3,
        "body": "The 72 hour rule is a guideline, not a hard cut off.  Circumstances are taken into account.\n\nFocus on health.  The financial part will solve itself."
      },
      {
        "id": "o8sgeg9",
        "score": 1,
        "body": "Sometimes the hospital billing department makes that call on your behalf to make sure they are paid so check with them too."
      },
      {
        "id": "o8s64m8",
        "score": 1,
        "body": "Thank you for your words and advice. Very reassuring right now.\u00a0"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rlhp1t",
    "title": "DBQ results - thoughts on outcome?",
    "body": "I\u2019m not seeing anyone post similar results so I\u2019m curious what anyone may think will be the outcome of this",
    "flair": "Predict My Rating :Crystal:",
    "score": 2,
    "comment_count": 14,
    "created_at": "2026-03-05T13:31:23+00:00",
    "top_comments": [
      {
        "id": "o8s24q2",
        "score": 2,
        "body": "Friendly reminder from your r/VeteransBenefits mod team to **never** provide (Personally Identifiable Information) on reddit.  \n\nAnyone asking for it in a PM is likely trying to steal your identity.\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VeteransBenefits) if you have any questions or concerns.*"
      },
      {
        "id": "o8tafba",
        "score": 1,
        "body": "How did you get that dbq ?"
      },
      {
        "id": "o8s06pr",
        "score": 1,
        "body": "Did you file for TDIU?"
      },
      {
        "id": "o8ss8fp",
        "score": 1,
        "body": "70"
      },
      {
        "id": "o8s0et4",
        "score": 1,
        "body": "I ask because this strongly meets the criteria for 70% but also 100% pay if you filed for TDIU. "
      },
      {
        "id": "o8s0gya",
        "score": 1,
        "body": "No. I work in a specific accommodative environment making about 30k currently where I may be able to file for tdiu if this fails. "
      },
      {
        "id": "o8s0shz",
        "score": 1,
        "body": "Once I read these docs I wasn\u2019t sure I would even get 30-50 I\u2019m feeling very insecure right now "
      },
      {
        "id": "o8sjtd7",
        "score": 1,
        "body": "Would it be prudent to file for TDIU while the rating is still under review or wait until after?"
      },
      {
        "id": "o8s1syr",
        "score": 1,
        "body": "Oh no this is extremely strong. If you want, I can break it down for you. But it definitely supports 70%. Not 100% because they didn\u2019t say total occupational and social impairment. But you need to apply for TDIU. If you can get documentation stating that your employment is accommodated and protected due to your disability, that\u2019s TDIU gold and your income won\u2019t interfere because it\u2019s not considered competitive, substantially gainful employment if it\u2019s accommodated. "
      },
      {
        "id": "o8smvj8",
        "score": 1,
        "body": "If it\u2019s still in evidence gathering, I\u2019d do it now. The evidence is there and it\u2019ll be considered with the evidence already submitted. Also, the back pay will be considered with the file date for when the claim was initially filed, if not earlier. "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rlgtv8",
    "title": "Back to Step 3\u2026",
    "body": "After my initial claim got denied, it went back to step 3. I already got diagnosed by my examiner with PTSD but have to \u201cprove\u201d I was there at the event. Im going to submit buddy letters and a written statement. Do I just post it under \u201cSUBMIT EVIDENCE\u201d option and that will restart the process once I upload it or do I have to submit a form to kickstart the process again?  Sorry first time doing this. ",
    "flair": "VA Disability Claims :claim:",
    "score": 5,
    "comment_count": 9,
    "created_at": "2026-03-05T12:51:49+00:00",
    "top_comments": [
      {
        "id": "o8rtopd",
        "score": 1,
        "body": "Yes just put it under submit evidence it'll move you back to step 3"
      },
      {
        "id": "o8rtwh0",
        "score": 1,
        "body": "How do they know when I\u2019m done submitting evidence? I guess I\u2019ll just submit it all at once and not touch it. "
      },
      {
        "id": "o8ru1kr",
        "score": 1,
        "body": "My claim went in before yours and I've been at step 1 the whole time so....\ud83d\udd95\n\nI've never seen a situation like yours. When I was denied I got a letter in the mail telling me to appeal it. No more steps. Did you have other things in for rating or is it just this one issue..? "
      },
      {
        "id": "o8rtsun",
        "score": 1,
        "body": "I\u2019m at step 3. So it\u2019ll move forward from there? "
      },
      {
        "id": "o8ruexp",
        "score": 1,
        "body": "I had one deferred maybe that\u2019s why it\u2019s still \u201copen\u201d"
      },
      {
        "id": "o8ruso6",
        "score": 1,
        "body": "So what\u2019s the process of submitting evidence for a denied claim? "
      },
      {
        "id": "o8rtywl",
        "score": 1,
        "body": "Anytime you upload info when it's past step 3 it goes back to step three. It will progress more but it may take some time, especially if they have to schedule you for another exam"
      },
      {
        "id": "o8rwsgj",
        "score": 1,
        "body": "That's the answer. "
      },
      {
        "id": "o8rwr7y",
        "score": 1,
        "body": "You sir will get a letter in the mail giving you a VERY CLEAR path to appeal.\n\nThey will explain it like you're 5. Just wait for the letter. "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rlcwz5",
    "title": "VA denies limiting veterans\u2019 mental health care; Vets, VA psychologists say it\u2019s happening",
    "body": "",
    "flair": "Headlines & News :rsz_21601:",
    "score": 365,
    "comment_count": 99,
    "created_at": "2026-03-05T09:10:55+00:00",
    "top_comments": [
      {
        "id": "o8rlu02",
        "score": 68,
        "body": "I left the VA last year as a mental health provider (vet also), it absofuckinglutely is happening. \n\nMy role involved going into the community with GOVs, during the whole DOGE fraud, many of the credit cards for gas tied to each GOV were deactivated (it got unfucked eventually, but not fully).\n\nHow the fuck do you provide service if you dont have the gas to get to the client?\n\nDuring the pandemic, there was a surge of new eligible vets with the PACT act. \n\nMakes absolute sense they started laying off people right...?\n\nMore vets added to an already stressed system while further stripping that system of providers! 5D chess move! Who would've guessed it created a shit load of issues!\n\nOne of our new hires got the boot a few months after being hired... but she did confide in my coworker she supported and voted for this. \ud83e\udd37\u200d\u2642\ufe0f"
      },
      {
        "id": "o8rmaf8",
        "score": 63,
        "body": "I keep getting passed around from interns who always leave at the end of their internships which does wonders for my abandonment issues and is always fun to restart with someone new."
      },
      {
        "id": "o8rkufk",
        "score": 61,
        "body": "Geee fire people, make it so miserable that people leave for the private sector\u2026.. and wonder why care is rationed? "
      },
      {
        "id": "o8rdf8l",
        "score": 43,
        "body": "Yea, and I am struggling because my provider can't see me with my mental health crumbling."
      },
      {
        "id": "o8rp27x",
        "score": 24,
        "body": "All I got offered was group therapy because I'm not \u201cactively suicidal\u201d and like hell I'm talking about all this shit on some Zoom group chat."
      },
      {
        "id": "o8ronpi",
        "score": 24,
        "body": "Worked at the VA from 2021-2024 and it really was impossible getting vets in at the first VA I worked. I then transferred to BHIP for a remote position at another VA and they put anyone and everyone in my schedule and I had a client list of over 150 with only 24 weekly spots\u2026 when I asked how I could maintain treatment plans they talked about seasons of care\u2026 12-20 sessions then move to the next\u2026 I fought it until I couldn\u2019t anymore "
      },
      {
        "id": "o8ros58",
        "score": 23,
        "body": "I currently go to to the Vet Center, honestly it\u2019s the one system that can actually maintain the treatment plans as they should be "
      },
      {
        "id": "o8roans",
        "score": 22,
        "body": "Absolutely happening!! Want to rebrand it as \u201cSeasons of Care\u201d worked and left the unethical practices and gaslighting drove me out of the field. "
      },
      {
        "id": "o8rwphz",
        "score": 20,
        "body": "Of course its happening. It happens every session for me. MH provider tells me every time, \u201cok, schedule to see me again in two weeks.\u201d But I have to wait for the scheduler to call me, which takes around 3 weeks, then it\u2019s always at least 5 weeks later until I can get on the schedule. Ends up being less than ever other month when I\u2019m supposed to see them every other week. It\u2019s been like this for at least 3 years now. "
      },
      {
        "id": "o8rmxj4",
        "score": 15,
        "body": "I know quite a few psychologists who have worked at the VA. Most of them leave because they are given an unmanageable case load that is so large that there is zero chance of getting people in frequently enough for appointments that treatment can be effective. \n\nThe reality is that the VA had been deliberately underfunded by the GOP for years and is short tens of thousands of medical providers. The solution for this is supposed to be CCN - but getting a referral through is close to impossible and requires finding a provider who participates in CCN. "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rlb9eu",
    "title": "Hill and Ponton Withdrew",
    "body": "Hello to all fellow veterans,\n\nI am currently at a very serious juncture and would like some advice. I filed for a TDIU supplemental claim in October 2025. I was approved for MDD at 70% in December 2024. I was denied PTSD in May 2020, but the VA had a favorable finding for MDD in that same month. I have been living below the poverty line in terms of income for the past five years.\n\nAfter Hill and Ponton had been representing me for the past year, they recently withdrew and waived all fees. I am essentially lost because I live overseas, and a DBQ is currently processing on Step 3 of 8. I am asking today: should I be worried? Does this mean my claim is unlikely to be successful?\n\nUpdate:\n\nAs noted in the letter we sent on March 4, 2026, our office made the decision to withdraw from representation due to ongoing difficulties that made it impractical for our firm to continue handling your appeal. These issues primarily related to communication challenges and difficulties obtaining the timely cooperation necessary to effectively move your claim forward. In addition, there were delays in the progress of the appeal, including missed VA examinations and timing issues related to notifying VA of your relocation outside of the United States.\n\nBecause these factors significantly impacted our ability to effectively manage the case, we determined it was appropriate to withdraw from representation.",
    "flair": "VA Disability Claims :claim:",
    "score": 0,
    "comment_count": 29,
    "created_at": "2026-03-05T07:28:33+00:00",
    "top_comments": [
      {
        "id": "o8roxqk",
        "score": 4,
        "body": "There is a silver lining, they don\u2019t think it\u2019s worth the work for the money. For you this mean more work and you will keep 1000s of dollars for yourself "
      },
      {
        "id": "o8rb1jd",
        "score": 3,
        "body": "Why did they withdraw?"
      },
      {
        "id": "o8rs80r",
        "score": 3,
        "body": "thanks for sharing, while your situation is stressful, the events you are describing do not necessarily mean your claim will be unsuccessful. in many cases, these moving parts are standard parts of the VA claim process! \n\npraying for a great outcome! "
      },
      {
        "id": "o8qxnp2",
        "score": 3,
        "body": "It\u2019s a real mental health crisis on my end. I ultimately feel like I am defeated in a sense. They have a 96% win rate so that says a lot."
      },
      {
        "id": "o8rcazo",
        "score": 3,
        "body": "They told you they would no longer represent you and they were waiving their fees but they didn't tell you why? "
      },
      {
        "id": "o8rxylp",
        "score": 3,
        "body": "This might be a hot take but what I was getting at is you don\u2019t need an attorney for most claims and as accredited attorneys they only get paid in specific circumstances mainly out of back pay from appeals. If they see you have good case that is unlikely to result in a lengthy appeal (or one they could make lengthy) they may have decided continuing to help you would generate negative profit for them. What you do have to do is then leg work yourself the benefit is you keep the money and you don\u2019t jerk yourself around or leave yourself hanging."
      },
      {
        "id": "o8rp50c",
        "score": 2,
        "body": "It says they cherry pick cases. "
      },
      {
        "id": "o8stgrz",
        "score": 2,
        "body": "I ask myself the same question sometime. I have a fianc\u00e9 and a daughter in the country so that keeps me sane. Ultimately I will have to eventually figure it out \u2026"
      },
      {
        "id": "o8rspyw",
        "score": 1,
        "body": "You get to keep your back pay!!!!"
      },
      {
        "id": "o8t4d6e",
        "score": 1,
        "body": "At 70%, you shouldn't be living below the poverty level in Liberia.  I wouldn't worry about it; you are at step 3 just let the claim go forward and hope for the best.  As other's have said, if approved, you won't have to give up any of your back pay."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rlate0",
    "title": "OSA secondary to PTSD denied despite nexus letter. Filing HLR. Anyone succeed?",
    "body": "Looking for some advice or experiences from anyone who has gone through something similar.\n\nI filed a supplemental claim for obstructive sleep apnea secondary to my service connected PTSD. My sleep study diagnosed severe OSA with an AHI of 75 and I was prescribed a CPAP.\n\nFor evidence I submitted:\n\n\u2022 A private nexus letter from a PA who reviewed my records and cited medical literature linking PTSD and OSA\n\n\u2022 The nexus explained weight gain as an intermediate step (PTSD \u2192 weight gain \u2192 OSA)\n\n\u2022 Buddy statements describing my sleep symptoms and fatigue\n\nTimeline:\n\n\u2022 Supplemental claim filed Jan 27, 2026\n\n\u2022 C&P exam Feb 25, 2026\n\n\u2022 Decision Mar 4, 2026\n\nThe VA denied the claim and relied heavily on the C&P examiner\u2019s opinion. The examiner basically stated that OSA is caused by mechanical airway obstruction and PTSD is a psychiatric condition that does not affect the airway, so they concluded there is no nexus.\n\nThe VA also discounted my nexus letter and said it relied on my reported history, and they gave more probative weight to the VA exam.\n\nWhat I found interesting is that the decision still listed several favorable findings:\n\n\u2022 Confirmed diagnosis of severe obstructive sleep apnea (AHI 75)\n\n\u2022 I am service connected for PTSD\n\n\u2022 My service treatment records show sleep disturbances during service\n\n\u2022 Southwest Asia deployment and toxic exposure were conceded\n\nSo the only real issue seems to be the nexus.\n\nMy nexus letter argues that PTSD contributed to sleep disruption and weight gain which then contributed to OSA, which the VA examiner didn\u2019t really address. The examiner mainly focused on the idea that PTSD does not directly cause airway obstruction.\n\nBecause of that I\u2019m planning to file a Higher Level Review with an informal conference.\n\nOne thing I\u2019m wondering is whether the VA exam really addressed the intermediate step theory (PTSD \u2192 weight gain \u2192 OSA) that was explained in the nexus letter, or if it only answered the question of whether PTSD directly causes airway obstruction.\n\nFor anyone who has gone through something similar:\n\n\u2022 Has anyone had OSA secondary to PTSD approved at HLR after a denial like this?\n\n\u2022 Did the reviewer order a new medical opinion or grant it outright?\n\n\u2022 What kind of HLR timelines are people seeing lately?",
    "flair": "VA Disability Claims :claim:",
    "score": 3,
    "comment_count": 22,
    "created_at": "2026-03-05T07:01:46+00:00",
    "top_comments": [
      {
        "id": "o8qq316",
        "score": 6,
        "body": "the c&p examiner completely missed your intermediate step argument and just focused on direct causation which isnt what your nexus letter was claiming"
      },
      {
        "id": "o8rpsf4",
        "score": 3,
        "body": "First, get a copy of the c&p results by filing a FOIA request. See if your private examiner will strengthen their nexus letter by making it more specific to you and rebut the VA examiners opinion. You can then file a supplemental with the new nexus as your new evidence. Make sure your nexus letter addresses that the PTSD caused the weight gain. The weight gain caused the OSA, whether the weight gain was a significant factor in the development of OSA and whether absence of the weight gain caused by PTSD, would you still have developed OSA. They require the examiner to answer those 3 questions in their medical opinion for service connection. \n\nIf you can't get the nexus letter strengthened, you need to do an HLR and specifically state that the VA examiners opinion did not address obesity as an intermediate step due to your PTSD. That will likely get them to order a new medical opinion. As soon as you complete the HLR informal conference, submit any new evidence you have. Once the conference is done, the DRO will hopefully find a duty to assist and order a new medical opinion. The claim then goes back to a VSR to order any required exams. You want any new evidence to be on the record before the exam / medical opinion is ordered so they can include it with the exam request. The claim then turns into a defacto supplemental and new evidence can be considered."
      },
      {
        "id": "o8qo9oh",
        "score": 2,
        "body": "https://preview.redd.it/z6gobu73e6ng1.jpeg?width=1170&format=pjpg&auto=webp&s=ecc26afe02f9cb2484d49c2a88b597c3e87e979a"
      },
      {
        "id": "o8qsn9z",
        "score": 2,
        "body": "Just curious, are you on Sertraline. A noted side affect of Sertraline is weight gain, that could sway the odds in your favor.\u00a0"
      },
      {
        "id": "o8rm4hu",
        "score": 2,
        "body": " Point out in your HLR hearing that they did not address aggravation beyond natural progression , which should trigger another C&P or approval "
      },
      {
        "id": "o8rq1dx",
        "score": 2,
        "body": "I got a medical opinion from a psychologist. Because of their credentials and experience their medical opinions should carry more weight than a nurse practitioner or even a MD. It worked for me. Their opinions should have more probative value"
      },
      {
        "id": "o8rqavp",
        "score": 2,
        "body": "I was not able to use my CPAP due to claustrophobia, and I\u2019m allergic to latex. The dental device didn\u2019t work at all, and I\u2019m not too excited about the inspire sleep apnea device, don\u2019t want to have to be cut open in order to possibly sleep.   Luckily I didn\u2019t need OSA, but with all stuff I\u2019ve tried the only thing that\u2019s works is these cheap soft plastic nasal dilators you can buy on Amazon for like 10 bucks.  "
      },
      {
        "id": "o8ruefs",
        "score": 2,
        "body": "FYI FOIA can take some time 6+ months to over year. Would recommend going to your VA regional office, they can print your C&P results as long as the claim isn\u2019t open. "
      },
      {
        "id": "o8qoajp",
        "score": 2,
        "body": "https://preview.redd.it/034t6hp5e6ng1.jpeg?width=1170&format=pjpg&auto=webp&s=fc541375100a75210a8c8771d46382674b44af06"
      },
      {
        "id": "o8rkkm4",
        "score": 2,
        "body": "But what if you were prescribed it after your OSA diagnosis?"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rl91bx",
    "title": "Do VHA providers actively avoid providing diagnoses?",
    "body": "Idk if it's just my experience, or the VAMC that I go to, but it feels like any one at the VA capable of diagnosing a vet with a condition actively avoids doing so. They'll acknowledge said issue, but not label it in medical charts and medicate it. It's gotten to the point where I'll go to private care for a second opinion, and they don't even second guess it. Hell, I'll even get more details in clinical notes that establishes evidence more concretely. But even with conditions that I had treatment for, tested and diagnosed while on AD/orders, and have been SC'd for I still get VA providers that I see for further treatment question it. It seems like they neglect to read my chart and see that it's an issue that's been mentioned for more than a dozen years. Is it just protocol to not directly diagnose vets to aid them in building a case with the VBA?",
    "flair": "Health Care :caduceus:",
    "score": 22,
    "comment_count": 45,
    "created_at": "2026-03-05T05:22:56+00:00",
    "top_comments": [
      {
        "id": "o8qd7ez",
        "score": 15,
        "body": "I think you could fairly say that yes that is exactly what they do. I was trying to get help for GERD due to my penchant for taking Tylenol and ibuprofen to make my days tolerable, and when I mentioned the idea to my primary, she said, \u201cI\u2019m not diagnosing you with that you\u2019re diagnosing you with that.\u201d because obviously there are no objective tests that can be done to confirm or reject that diagnosis. Oh wait there are and that\u2019s exactly what my doctor did once I got health insurance and saw a real honest to God no shit true story doctor with a license and a practice. "
      },
      {
        "id": "o8qmuqj",
        "score": 9,
        "body": "I haven\u2019t experienced this issue. My doctor has been more than happy to order whatever seems appropriate when I have an issue. All of my medical issues have been diagnosed through the VA. This just seems like what the baseline of care should be."
      },
      {
        "id": "o8qhisb",
        "score": 9,
        "body": "had the exact same thing happen with my knee issues - va kept saying \"well it could be this or that\" while private doc took one look and immediately ordered an mri"
      },
      {
        "id": "o8qjcjm",
        "score": 7,
        "body": "I scheduled an appointment and when I got there I said, \u201cI have been having a lot of heartburn for the last couple of months and I have read that that is a potential side effect for the amount of ibuprofen and Tylenol I\u2019ve been taking over that time. I think that I have Gerd.\u201c Then she ignored me. I mean, what is even the point of talking to a doctor about your health concerns if they are just going to assume that you don\u2019t know what you\u2019re talking about or that you\u2019re actually there just recreationally because you\u2019re looking to kill an afternoon? My private doctor didn\u2019t assume that I was lying for some nefarious reason, and she also didn\u2019t assume that I had a clue what I was talking about. She ordered the test. Same thing with my orthopedic surgeon. He didn\u2019t just go hacking away on my knee because he was bored and I was willing to pay; he ordered a test and then he performed a procedure that was indicated by the results of the test. \n\nIt\u2019s frustrating that I couldn\u2019t get just\u2026 a baseline of consideration. "
      },
      {
        "id": "o8qfb7k",
        "score": 5,
        "body": "I'm guessing you had an EGD done and that private doc confirmed it?"
      },
      {
        "id": "o8qie4l",
        "score": 4,
        "body": "Dealing with something similar I have a issue they say is idiopathic (unexplained), but they keep bringing up things they have completely ruled out.\u00a0 Then they have other possible causes they speculate on, but won't order tests that would prove it one way or another.\u00a0 The record keeping is crazy too, really poor attention to detail and things that I never even said."
      },
      {
        "id": "o8qiqnm",
        "score": 4,
        "body": "What???\u00a0 Did she bother to order an endoscopy or anything.\u00a0 I wasn't aware we could self diagnosis and the doctor just says 'oh yeah, I like that one!'"
      },
      {
        "id": "o8qhzo5",
        "score": 4,
        "body": "One of the things I fought the VA for was treatment on my knee. It took six months to get an MRI to show that I had a meniscal tear. A private doctor was able to get me into an MRI in two weeks and he only made me wait that long to make sure that his office staff could get it approved with my health insurance.  Legitimately I waited longer for my primary to order an X-ray than I waited for an orthopedic surgeon to schedule my actual surgery. When my son needed an MRI on his leg, it took one calendar week and three of those days were on me because I didn\u2019t realize that his doctor expected me to make the phone calls to get an MRI scheduled with a local facility. "
      },
      {
        "id": "o8rkf8n",
        "score": 3,
        "body": "I kept being ignored on my health evet of issues I went to theER for and was recommended a specialist by the ER.  My care team kept blowing me off on my request. Everytime I asked they never acknowledged it. This went on for 3 weeks until I finally called them out that they were blowing me off and not giving me the recommended care I needed. I wrote that and sent it in my ehalthevet. As soon as it was read, I got a phone call apologizing and boom had the referal I needed.  I said thank you but it didn\u2019t need to come to this, you should have done it based on the case notes and recommendation by the er doctor. "
      },
      {
        "id": "o8rb7mj",
        "score": 3,
        "body": "When it specialty as Something like gerds ask to be referred to whatever specialty diagnoses and treats it. For Gerds I'd ask to see an ENT. Pro tip - when doing care in the community I pick a practice that's part of the hospitals clinic system. That way if something comes say like my ENT Dr removes a growth on my vocal cords and I need voice therapy they can use the ENT authorization to refer to voice therapy. VA will approve. Like wise if you need a endoscopy it uses the same ENT authorization. When I broke my neck the authorization for the Neurosurgeon allowed him to refer me to the hospital Physical Therapy after healing. As well as X-rays, CT Scans or MRI's way faster than the VA takes. Heck if I need an MRI for a claim the VA would never do it or take forever. At the hospital I can ask my pain mgmt Dr to get one and I'm getting it in a few days. Hospitals are all about making money so they will get it for you "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rl7s24",
    "title": "PSA - Colon Cancer Screening",
    "body": "Few weeks ago I posted about having lots of blood on my toilet paper and asked if it's an emergency because I didn't want the VA to deny my visit. I took pictures of it and been keeping a journal. I will be seeing the GI doc in June. My dad had polyops at 45 and grandma had colon cancer. \n\nI got the monthly VA email and they cover an entire series on it and symptoms to look out for. Just passing along the message. I'm 39 so I'm right on the border given my dad's history and my grandmother.\n\n https://links-1.govdelivery.com/CL0/https:%2F%2Fwww.youtube.com%2Fplaylist%3Flist=PL2quV7hnnZ3maBXBbmzUSx712JuaFXhY0/2/0100019cbc17bc0f-5dffb304-024e-4aa5-a158-4b84fd220653-000000/uh16DLNZXBwe2Ma1xAIrha8cLETyy8tEfpNWLEfo_68=447  ",
    "flair": "Health Care :caduceus:",
    "score": 3,
    "comment_count": 10,
    "created_at": "2026-03-05T04:19:55+00:00",
    "top_comments": [
      {
        "id": "o8qb6dy",
        "score": 7,
        "body": "Same boat as you. Since 45yo have had to have polyps removed every 2/3 years during a colonoscopy. So far so good. Blood in your rectum near the entrance can also be a minor hemorrhoid bleeding, which I have. Ask Dr about the bleeding and what might be the cause. 65 now will need to do a colonoscopy every 2/3 years for the rest of my life, time interval determined by a gastroenterologist."
      },
      {
        "id": "o8qav5q",
        "score": 3,
        "body": "I am in almost the exact same boat. My blood turned out to be a hemorrhoid from crapping so much from IBS. If it\u2019s bright red blood, it\u2019s generally something different than cancer. It\u2019s the dark, tarry, stool that you need to look out for. Best of luck yo yah."
      },
      {
        "id": "o8s5hw7",
        "score": 3,
        "body": "Just had a colonoscopy done through the VA yesterday. Dad passed away at 49 due to colon cancer so I started getting checked at 35. I would highly recommend that everyone get checked as it is not that bad of a process and a good peace of mind."
      },
      {
        "id": "o8rawb1",
        "score": 2,
        "body": "Please talk to your doc about your family history. There are genetic predispositions to colon/digestive cancers. I have a PMS2 mutation of my genes that predisposes me to colon and ovarian/uterine cancer (very strong family history so I got tested). Now I go in every two years for a colonoscopy/endoscopy (took care of the female part shortly after diagnosis). It\u2019s called Lynch Syndrome. Yes, the scope tests are invasive, but if caught early they are treatable cancers. \n\nGood luck in June. \n\nAnd folks, the prep and the tests are no big deal. More of an inconvenience compared to the alternative. "
      },
      {
        "id": "o8qhuuk",
        "score": 2,
        "body": "good catch on documenting everything - that's smart especially dealing with va claims. with your family history definitely worth getting checked out sooner rather than later, glad you're already scheduled with gi in june"
      },
      {
        "id": "o8rq8be",
        "score": 2,
        "body": "Exactly. I'd just rather be safe. Given my track record of being told my brain tumor was potentially just an STD although everything lined up which even I had no idea about until one ENT doctor was like wow everyone else is a dumbass. \n\nSecond worst was in 2020 when I lost feelings on my right side of my body which my neurologist said was a TIA event but the doctor kicked me out of the ER and told me to stop doing drugs. Soooo yeah."
      },
      {
        "id": "o8ru4p9",
        "score": 2,
        "body": "That sucks. I was lucky before my dad died, he compiled a list of family members going back to my great grandparents and how they died. I was fortunate to get an appointment with a renown researcher (now retired) and got tested. That info was \u201cgold\u201d to her. Was also part of a research study. That\u2019s how I came about knowing the risks I had. "
      },
      {
        "id": "o8rp1z1",
        "score": 1,
        "body": "Funny enough I did a genetic test through a cancer center and somehow they lost the records \ud83e\udd37\u200d\u2642\ufe0f. "
      },
      {
        "id": "o8rk61r",
        "score": 0,
        "body": "Well, the problem is its an exit, not an entrance."
      },
      {
        "id": "o8roue9",
        "score": 0,
        "body": "Given my track record for being in service with a brain tumor and being told by medical that it's just an STD when I was constantly having dizziness, passing out randomly, losing my hearing yes I need to be careful. "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rl7d69",
    "title": "Gi bill",
    "body": "anybody experienced this?? I\u2019ve never claim my GI Bill and it\u2019s saying someone is using my number and email for education benefits that\u2019s not me. I put in a help ticket to ask VA but they haven\u2019t responded to it.",
    "flair": "Education Benefits :mortarboard:",
    "score": 5,
    "comment_count": 0,
    "created_at": "2026-03-05T03:59:34+00:00",
    "top_comments": []
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rl71q1",
    "title": "Sleep apnea secondary to rhinitis denied",
    "body": "",
    "flair": "Denied :Not_Happy:",
    "score": 7,
    "comment_count": 12,
    "created_at": "2026-03-05T03:44:28+00:00",
    "top_comments": [
      {
        "id": "o8qdwi0",
        "score": 5,
        "body": "It does not need to cause it. aggravation by an incremental increase in severity due to a service connected disability.  spicer v mcdonough.  \n\nThere is substantial literature that sinus issues exacerbate osa.  The opinion should speak of the extent, if possible, the sc condition aggravates OSA.  The medical opinion may have fell short because the va examiner cited medical reference, and yours did not.  \n\n  \nmight try to focus on aggravation and cite some things.  Maybe like this stuff that ai whipped up   \n1. Allergic Rhinitis and Sleep Disturbance (Craig et al., 2004)\n\n**Study:**  \n[https://pubmed.ncbi.nlm.nih.gov/15536445/](https://pubmed.ncbi.nlm.nih.gov/15536445/)\n\n**Findings**\n\n* Allergic rhinitis causes **nasal congestion and inflammatory mediator release** that disrupt sleep.\n* Nasal obstruction leads to **sleep disturbance and daytime somnolence**.\n\n**Takeaway:**  \nRhinitis-related nasal obstruction contributes to sleep-disordered breathing and worsens sleep quality.\n\n\n\n# 2. The Linkage of Allergic Rhinitis and Obstructive Sleep Apnea (Chirakalwasan & Ruxrungtham, 2014)\n\n**Study:**  \n[https://pubmed.ncbi.nlm.nih.gov/25543037/](https://pubmed.ncbi.nlm.nih.gov/25543037/)\n\n**Findings**\n\n* Allergic rhinitis increases OSA risk through:\n   * **increased nasal airway resistance**\n   * **mouth breathing that narrows the airway**.\n\n**Takeaway:**  \nInflammation and nasal blockage from rhinitis can **worsen OSA physiology**.\n\n\n\n# 3. Chronic Rhinosinusitis and Sleep (Alt & Smith, 2013)\n\n**Study:**  \n[https://pubmed.ncbi.nlm.nih.gov/24039230/](https://pubmed.ncbi.nlm.nih.gov/24039230/)\n\n**Findings**\n\n* Chronic rhinosinusitis is strongly associated with **sleep dysfunction and impaired sleep quality**.\n* Inflammatory disease processes in the sinuses contribute to disturbed sleep physiology.\n\n**Takeaway:**  \nSinus inflammation can significantly affect sleep and contribute to sleep-disordered breathing.\n\n\n\n# 4. Chronic Rhinosinusitis and OSA Prevalence (Jiang et al.)\n\n**Study:**  \n[https://www.rhinologyjournal.com/Rhinology\\_issues/manuscript\\_1425.pdf](https://www.rhinologyjournal.com/Rhinology_issues/manuscript_1425.pdf)\n\n**Findings**\n\n* Patients with chronic rhinosinusitis had a **higher prevalence of obstructive sleep apnea**.\n* Nasal obstruction and airway inflammation are possible mechanisms.\n\n**Takeaway:**  \nCRS patients frequently have OSA due to **nasal obstruction and airway inflammation**.\n\n\n\n# 5. Allergic Rhinitis and OSA Severity (Literature Review)\n\n**Study:**  \n[https://www.researchgate.net/publication/270163342\\_The\\_linkage\\_of\\_allergic\\_rhinitis\\_and\\_obstructive\\_sleep\\_apnea](https://www.researchgate.net/publication/270163342_The_linkage_of_allergic_rhinitis_and_obstructive_sleep_apnea)\n\n**Findings**\n\n* Inflammatory mediators in rhinitis (histamine, leukotrienes, cytokines) **worsen sleep quality and OSA symptoms**.\n\n**Takeaway:**  \nUpper airway inflammation from rhinitis can **aggravate OSA severity**."
      },
      {
        "id": "o8qbn2y",
        "score": 2,
        "body": "I would say first things first, request your DBQs from the VA so you can see the response the VA opinion gave  that was more convincing.\n\nWith that said, your nexus is decent, but not great. It mentions reviewing your records but doesn\u2019t dive deep into detail on what they entail. \n\nThe Drs credentials aren\u2019t questionable but the nexus reads off as generic. It mentions studies but doesn\u2019t link them or say how YOUR records tie into that. It doesn\u2019t mention how bad your rhinitis is, how long you\u2019ve had it etc. Doesn\u2019t even say what years or how long you\u2019ve served. \n\nBasically long story short, the nexus doesn\u2019t go into deep detail that the VA wants to see. The VA is looking for your nexus to show that the doctor reviewed every single detail about your evidence and that they considered multiple factors such as weight/bmi or if it\u2019s possible your rhinitis actually doesn\u2019t aggravate your osa. "
      },
      {
        "id": "o8qq0q2",
        "score": 2,
        "body": "This is the way. You have to claim aggravation. And if you\u2019re considered overweight it will be a tough challenge unless you are service connected for disabilities that prevent you from regularly exercising and prescribe medication that inhibits weight gain. If that\u2019s the case you\u2019d be better off obtaining a new nexus because obesity is considered the number one risk factor for OSA.and still you\u2019d have a greater chance by claiming aggregation and filing OSA as secondary to multiple conditions and weight gaining prescriptions using weight gain as an intermediate step. "
      },
      {
        "id": "o8rx4mo",
        "score": 2,
        "body": "You are better than AI. Thanks for sharing this. You ROCK!"
      },
      {
        "id": "o8r4f7i",
        "score": 2,
        "body": "I didn't pay for it, my doctor wrote it. "
      },
      {
        "id": "o8rrp67",
        "score": 2,
        "body": "Aggravation is not the best way to claim OSA unless you have nothing else left to try. Aggravation is rated by looking at what your rating would be without the aggravation and what it is now. They rate you the difference. In most cases OSA will end up getting rated 0 under aggravation as the logic goes;\n\nWithout the aggravation would the veteran still have OSA and require a CPAP. If yes 50% would be the rating. CPAPs are prescribed for even mild OSA. If you wouldn't have mild OSA then the secondary issue would be the cause and not aggravation.\n\nWith the aggravation what is the veterans rating, 50%\n\n50% - 50% = 0%"
      },
      {
        "id": "o8s16qa",
        "score": 2,
        "body": "First, Thanks.  Just share experiences, since it seems more and more difficult these days.\n\nYeah, not sure why I am getting downvoted for sharing caselaw, medical studies and arguments accepted by the Board of Veterans Appeals (via CAVC).  The law is clear that any measurable aggravation, despite how little, is service connected.  A lot of vets or VSO get hung up on secondary alone, which is medically complicated and debatable.   Making it a little worse, not complicated or a high standard.\n\nAlso FWIW, almost any board certified sleep dr would agree that sinus congestion contributed to intolerance of a CPAP, or so I heard....  Pretty sure having trouble using a cpap objectively worsens symptoms...."
      },
      {
        "id": "o8q0ltq",
        "score": 1,
        "body": "Well you're trying to convince them with 50% certainty that rhinnutus caused your OSA. Although you have a good letter etc. They felt other factors more likely contributed to OSA and not service condition. So, my question would be are you overweight as if you are you'd have a hard time convincing them rhinnutus was the cause. In addition you'd need to build a good case to show that the rhinnutus caused your osa which would also be difficult depending on how far after the military you applied as your have to show rhinnutus with a direct link to OSA based on your hx not just the likelyhood that OSA can be caused by rhinnutus without showing your disease progression that caused OSA."
      },
      {
        "id": "o8qiebp",
        "score": 1,
        "body": "That's not a very good Nexus letter.  I hope you didn't pay much for it."
      },
      {
        "id": "o8rtkoi",
        "score": 1,
        "body": "Start with a FOIA request for the c&p exam results including the medical opinion. Read that opinion well. Wait a few days, go back and read it again. Now list out what you find incorrect on it. Did it just list a bunch of possible causes such as obesity? Ask your doctor to do redo the letter rebutting the examiners opinion. For example, the fact that you do not have the typical causes of OSA. Your BMI is only 23.2 and does meet the criteria for obesity. Your examiner needs to point out why the typical causes of OSA do not apply to you and why the rhinitis is the more likely cause. Is your rhinitis rated for blockages or polyps that would contribute to the airway collapse?\n\nIt would be best if they could say it is \"at least as likely\" the cause and leave out the aggravation. Then file a supplemental claim. You have 12 months to file, gather your evidence and don't just jump into an appeal."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rl5zh3",
    "title": "TBI Va claim",
    "body": "Hello, \n\nPlease, I would like to know if you wear a lot helmet or if your head can just hit something slightly? ",
    "flair": "VA Disability Claims :claim:",
    "score": 1,
    "comment_count": 13,
    "created_at": "2026-03-05T02:54:50+00:00",
    "top_comments": [
      {
        "id": "o8pqu2f",
        "score": 12,
        "body": "I think you qualify don't worry about it. "
      },
      {
        "id": "o8q04zh",
        "score": 4,
        "body": "I tried very hard to not laugh after reading your comment. "
      },
      {
        "id": "o8pqtu2",
        "score": 3,
        "body": "I\u2019m so confused by your post can you elaborate I have tbi would like to help"
      },
      {
        "id": "o8pqywf",
        "score": 3,
        "body": "TBIs can happen regardless of helmets. Yes, they can reduce direct injuries, but the claim is usually made with the medical report you\u2019d get from the doctor\u2019s exam; concussions are also considered in TBI claims, they happen regardless of if you\u2019re wearing a helmet or not.\n\nThe important thing for TBI claims is having the medical report with medical evidence for a TBI. Being hit slightly might probably not warrant you to get checked unless your leadership sends you to sickcall later or if your injury is not improving or gets worse."
      },
      {
        "id": "o8pscas",
        "score": 3,
        "body": "facts"
      },
      {
        "id": "o8prtvk",
        "score": 2,
        "body": "Lol \nThank you "
      },
      {
        "id": "o8q5cyp",
        "score": 1,
        "body": "I got 50% tbi from a head injury from a motorcycle accident that happened back in 07"
      },
      {
        "id": "o8qpekn",
        "score": 1,
        "body": "They lumped my TBI in with my psych shit. The only reason I'm not complaining is I am 100% P&T"
      },
      {
        "id": "o8ps89n",
        "score": 1,
        "body": "Get some treatment brother, hope things go well for you"
      },
      {
        "id": "o8qjhqh",
        "score": 1,
        "body": "Being deployed to TX won't cut it for a reason. What injury event happened to cause your TBI. That is what they'll want to know, plus any in service medical records if they exist. If none, that injury/event will be important with a private Dr's medical diagnosis/treatment in your records."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rl3q1z",
    "title": "VA Home loan 100% P&T",
    "body": "I am looking to buy, but not sure how much I would even get approved for or even try to get approved. I\u2019m 100 p/t, I have a little part time that brings in about 1,000 a month. My credit score is about 750 and just a car loan that I owe about 10k on. I do have debt which is about 2k. I am also in school and just tried of living in an apartment with my kids. Any advice ? ",
    "flair": "Housing :house:",
    "score": 3,
    "comment_count": 15,
    "created_at": "2026-03-05T01:12:25+00:00",
    "top_comments": [
      {
        "id": "o8p8bb3",
        "score": 9,
        "body": "Fuckin go get a home loan dude just dont make yourself housepoor. Better to be paying a mortgage vs paying rent. You know if the hard times hit youll atleast be working toward not paying a mortgage anymore. "
      },
      {
        "id": "o8rjhff",
        "score": 3,
        "body": "Do house hacking. Get yourself a duplex or something in that realm. I got a 4 plex a couple years ago and it has been amazing so far. Tenants pay my mortgage, and I have a little extra every month. Once these interest rates go down and I can refinance it'll be even better. I highly recommend it. I keep myself separated from the tenants... my property manager deals with everything and its only 6% of the monthly rents."
      },
      {
        "id": "o8pam7p",
        "score": 3,
        "body": "real talk \ud83d\udd25"
      },
      {
        "id": "o8r3hj9",
        "score": 3,
        "body": "It\u2019s like leasing a car\u2026 if you have the money to throw away, cool, but if you want to own something eventually, stop giving money away to use something\u2026 \n\nI think of it this way. Do you lease your clothes? Couch? TV? Phone? \n\nI sure hope not!! "
      },
      {
        "id": "o8pb7ik",
        "score": 2,
        "body": "You can use calculators online to see how much you can afford. Look into your state benefits, like no property tax, etc. Then see what\u2019s available for the same amount monthly that you pay in rent. Will give you a good starting point. \n\nMake sure that you keep in mind having some extra for home repairs, and other home things. For easy math: if you pay $100 in rent, see what\u2019s available for $80/ month mortgage payment. Then save that extra $20 for home maintenance."
      },
      {
        "id": "o8pef55",
        "score": 2,
        "body": "I just bought a home using a VA loan just make sure your debt to income ratio is good. I owe way more and already have a mortgage in another state.  As long as you have good credit and can prove you pay debt on time and have a decent cash reserve you should be fine"
      },
      {
        "id": "o8pe7ar",
        "score": 1,
        "body": "You can talk to a lender and see this fairly easily. Just know that they'll approve you for more than you can realistically afford. It's up to you to determine what's inside your means and stick to it. Like someone else said, dont become house poor. People hold up home ownership as a driver of wealth and that's not false but home maintenance/big repairs can eat you alive if you arent prepared for it."
      },
      {
        "id": "o8pnf1y",
        "score": 1,
        "body": "Where in the country do you live at?  How much in savings do you have?  What is your budget?"
      },
      {
        "id": "o8sm0q4",
        "score": 1,
        "body": "Bro as long as your credit score is above like a 680 or something you're good "
      },
      {
        "id": "o8snwcn",
        "score": 1,
        "body": "How long until you finish school? If you buy now and end up needing to repair/replace something in your home will you have that extra money? Might consider just waiting it out until you finish school and work where you can make a little more and/or dont have the added stress of school in case you would need to work extra hours to make that repair/replacement. "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rl3mju",
    "title": "Freedom of Info Act still waiting",
    "body": "I requested my military records for a specific C&P exam back in 2024 after I didn't feel comfortable with  a C&P I had a few months prior. Im still waiting on them. Since then I am at a 100%. Was wondering if I should contact VA and have them cancel this request or just let it be. Thank you",
    "flair": "C&P Exams :stethoscope:",
    "score": 14,
    "comment_count": 12,
    "created_at": "2026-03-05T01:08:12+00:00",
    "top_comments": [
      {
        "id": "o8p7nmm",
        "score": 7,
        "body": "Let it ride. "
      },
      {
        "id": "o8p7yik",
        "score": 7,
        "body": "FOIA requests are not done by raters so it cant hurt anything. You may find the records interesting at least, even if you dont make additional claims in the future."
      },
      {
        "id": "o8p96e1",
        "score": 4,
        "body": "At 366 days I contacted my congressman. His office had the electronic version of records in 8 hours.  I mever got the disc but got the electronic download which was done many months before. "
      },
      {
        "id": "o8phmh1",
        "score": 3,
        "body": "That is how they appear -- as claims, even when entered via FOIA workflow."
      },
      {
        "id": "o8panpb",
        "score": 2,
        "body": "I just posted a similar question lol. Guess it\u2019s gonna be a while. "
      },
      {
        "id": "o8pb7xn",
        "score": 2,
        "body": "Thank you"
      },
      {
        "id": "o8pbbs2",
        "score": 2,
        "body": "Thank you"
      },
      {
        "id": "o8pr98h",
        "score": 2,
        "body": "I had no idea, I suppose it makes it a lot easier to keep track of things. I like that \ud83d\udc4c "
      },
      {
        "id": "o8pat2h",
        "score": 1,
        "body": "Wait... you put in a claim for a foia request instead of doing a foia request? Thats new to me. "
      },
      {
        "id": "o8q93lg",
        "score": 1,
        "body": "Mike took about 7 months to get my disc in the mail."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rl2pg6",
    "title": "Can someone explain if I\u2019ll get back pay, VA math is confusing \ud83e\udee8",
    "body": "Hello all \ud83d\udc4b! I\u2019m confused about how to explain to my husband the VA math when it comes to backpay. Backstory: I submitted a supplemental for an increase in mental health and it was granted from 30% to 70%, I am now 100% permanently and totally disabled by the VA standards. Now the effective date was backdated to January 22, this was confirmed via my decision letter. Now while I was waiting for the actual decision  letter, I was paid January 30 and February 27 but for my 90% service connected. Fast forward. I received my new decision letter for the 100% on March 2 again with the effective date being backdated to January 22. Will this warrant some form of backpay? I\u2019m just a little confused as to how the payment system works and how the VA sees it. Thank you everyone for taking the time to explain\u2764\ufe0f",
    "flair": "VA Math :math:",
    "score": 2,
    "comment_count": 12,
    "created_at": "2026-03-05T00:28:12+00:00",
    "top_comments": [
      {
        "id": "o8p4z4n",
        "score": 6,
        "body": "The only backpay you\u2019re owed is the difference between 90% and 100% for February. "
      },
      {
        "id": "o8p0km9",
        "score": 4,
        "body": "No backpay for January because partial months are not paid. You will get back pay for February only. You will be paid 100% for March at the end of March as VA pays in arrears."
      },
      {
        "id": "o8p119b",
        "score": 4,
        "body": "Yes, there should be some back pay. Even though the effective date is January 22, the VA does not pay partial months, so compensation begins February 1 and is paid March 1 because the VA pays one month behind. Since you were paid at the 90% rate for February while waiting on the decision, the VA should issue a retroactive payment covering the difference between the 90% and 100% rate for that month (and any other months paid at the lower rate). That difference normally shows up as a separate lump-sum deposit once the award processes.\n\nBackpay often hits around a week later (3-10 business days) after the decision is finalized."
      },
      {
        "id": "o8p4jxe",
        "score": 4,
        "body": "\n> so when you got paid feb 27th that was for january's benefits, and when you got paid jan 30th that was for december. \n\nThis part is wrong, the VA pays for the previous month, not a month behind.  Feb 27 (Mar 1) pay was for February, January 30th (Feb 1) was for January."
      },
      {
        "id": "o8p1zpm",
        "score": 3,
        "body": "The February 27 payment is for February, not January. The January payment would have been at the end of January. OP is owed the increase for February only, since March has not been paid yet and January is a partial month."
      },
      {
        "id": "o8p9h8a",
        "score": 2,
        "body": "If I\u2019m reading right you should get a back pay check/deposit in the next few days to a week for the difference in pay of 90 and 100 percent for February. Your next regular check/deposit April 1 will be at the 100% rate. Many others pointed out no backpay for January. "
      },
      {
        "id": "o8p3uts",
        "score": 2,
        "body": "January 30 was for January not December. VA pays at the end of each month not two months behind. "
      },
      {
        "id": "o8p2497",
        "score": 1,
        "body": "Being that February just paid out for all vets  a few days ago it was probably included in your backpay. So no pay for a January as that is your partial month.  You would be due the month of February. No one has been paid for March yet, that won\u2019t happen til April 1st"
      },
      {
        "id": "o8p8wbd",
        "score": 1,
        "body": "This"
      },
      {
        "id": "o8pdjja",
        "score": 1,
        "body": "Okay that makes sense ! I was confused since it was backdated to Jan 22, thank you for the explanation!"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rl1chx",
    "title": "Went to NON VA Emergency Room- I have Tricare and 100% P&T do I need to notify the VA?",
    "body": "As the title states, I am a 100% disabled veteran P&T and I also have Tricare prime because I am retired from the Air Force. I went to the NON VA emergency room on Sunday morning and was treated and discharged. I did not take an ambulance. When the hospital asked me what my insurance was I put down that I had Tricare and VA- I\u2019ve seen posts on this sub Reddit before about people getting bills so I\u2019m wondering\u2013 does Tricare get billed before VA?do I need to tell the Va? Will tricare cover this visit? Thanks",
    "flair": "Health Care :caduceus:",
    "score": 1,
    "comment_count": 21,
    "created_at": "2026-03-04T23:31:20+00:00",
    "top_comments": [
      {
        "id": "o8ovhk5",
        "score": 7,
        "body": "Ok, no worries.  Here's the link to the VA website that explains getting care at non-VA emergency rooms.  Give the number listed a call within 72 hrs of being treated.  They're going to ask where you were treated, the day, and the time you were admitted.\n\n[https://www.va.gov/resources/getting-emergency-care-at-non-va-facilities/](https://www.va.gov/resources/getting-emergency-care-at-non-va-facilities/)"
      },
      {
        "id": "o8ov8cc",
        "score": 5,
        "body": "ChampVA is healthcare coverage for the dependents of 100PT Veterans. You are covered under Veterans Healthcare Admin, for VHA to cover bill, you need to notify VHA within 72 of being admitted to ER. Since you listed Tricare as your healthcare provider they will likely bill them and you will probably have a copay. As ma1butters mentioned above fill out the form and see if VA will cover bill if you are within the 72 hr timeline."
      },
      {
        "id": "o8ou17s",
        "score": 4,
        "body": "If you're the retired veteran, then you don't have ChampVA.  ChampVA is only for dependents.  Have you enrolled into VA Healthcare?  Receiving disability compensation doesn't automatically enroll you into the VA Healthcare system."
      },
      {
        "id": "o8ozljj",
        "score": 4,
        "body": "I am retired Marine with Tricare Prime and 100% P&T VA i have used the emergency room a couple of times I NEVER tell them I have any VA care the VA will fuck it up every time i just give them Tricare\u2026 and if there is a small co pay i pay it "
      },
      {
        "id": "o8oq29a",
        "score": 4,
        "body": "Fill this out.\n\nhttps://emergencycarereporting.communitycare.va.gov/compliance"
      },
      {
        "id": "o8p38el",
        "score": 3,
        "body": "I would recommend notifying the va. They make my bills $0 every time I notify them."
      },
      {
        "id": "o8p0eoz",
        "score": 3,
        "body": "Must also call within 72 hours plus fill out that form\n\n844-72HRVHA (844-724-7842)"
      },
      {
        "id": "o8owja8",
        "score": 2,
        "body": "Thanks I edited my post and filled out the form! "
      },
      {
        "id": "o8oufh4",
        "score": 2,
        "body": "Done. Thank you!! "
      },
      {
        "id": "o8ozsnr",
        "score": 2,
        "body": "Call them after you fill it out because you need to do both"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rl0u44",
    "title": "Asked for HLR and got a CUE and Reduction to Benefits Notice. Help!",
    "body": "Long story so here are the cliff notes:\n\n1 - Filed for flat left collapsed arch after separation in May 2023. Approved as SC and awarded 30%\n\n2 - Noticed that I had a podiatrist note that I had an acquired foot deformity when I did my OCS indoc in 2011 so I filed for right foot collapsed arch. OCS was 5 years after my initial enlistment. I served an enlisted term and completed two deployments prior to OCS.\n\n3 - After my C&P, the VA came back and said I had asymptomatic flat feet when I joined in 2006 so it was denied.\n\n4 - Asked for HLR. Explained how the podiatrist noted my foot as an acquired deformity and it isn't just asymptomatic flat feet. They agreed and reopened the case.\n\n5 - Today I receive a decision letter stating that the VA agrees that I should have bilateral pes planus that isn't fixed by orthotics. However, they made a **clear and unmistakable error** when I filed for my left foot in 2023. They should have noticed both my feet were deformed (even thought I only put left foot on the claim) and also should have noticed that I had asymptomatic flat feet from my MEPS physical.\n\n6 - Somehow, the VA decided that before I joined the service that I should have had a 30% rating already applied to my feet. Therefore, while they acknowledge I am 50% for flat feet, they are subtracting 30% from this based on what symptoms they believe I had when I joined despite there being no proof. So now this reduction from my original rating of 30% to 20% **reduces** my overall benefits from 70% to 60%.\n\nWhat do I do? I plan to fight it but I honestly have no clue where to start or how this is even legal? The only medical thing related to my feet is my MEPS Dr. stating I have normal feet with asymptomatic moderate flat feet. How can they apply a 30% rating to this to subtract from the 50%? Please help!\n\nEdit: Added pictures of my claim letter.\n\n[https://imgur.com/a/GHlcyU](https://imgur.com/a/GHlcyU)\n\nEdit: the reasoning they are using to say I had these problems prior to service are literally a cut and paste from my active duty Dr's comments. Literally word for word.   \n",
    "flair": "C&P Exams :stethoscope:",
    "score": 10,
    "comment_count": 43,
    "created_at": "2026-03-04T23:10:46+00:00",
    "top_comments": [
      {
        "id": "o8oz379",
        "score": 22,
        "body": "The first thing you need to do is call and tell the VA you are requesting a \"predetermination hearing\" in regards to the proposed reduction. If you do this within 30 days of the proposal, the reduction gets put on hold and your payments stay the same until a hearing and a final decision. Follow this up with a personal statement (21-4138) stating the same thing. Do not file a supplemental, do not file an HLR. You need to request a predetermination hearing. It is not the same thing as an HLR with an informal conference. \n\n[Proposed Rating Reduction, Incompetence, or Entitlement Severance | Act quickly to save yourself \u2014 Veterans Benefits Knowledge Base](https://www.veteransbenefitskb.com/reduction)\n\n  \n[Predetermination (RVSR) Hearing and Proposed Reduction. Have you been to one? : r/VeteransBenefits](https://www.reddit.com/r/VeteransBenefits/comments/1qrl09y/predetermination_rvsr_hearing_and_proposed/)\n\n"
      },
      {
        "id": "o8ox15l",
        "score": 12,
        "body": "I think there's alot more to this story. My first guess is you have a break in service between enlisted and officer and theres a good chance you are reserve or guard.  "
      },
      {
        "id": "o8ox875",
        "score": 10,
        "body": "Acquired foot deformity just means it happened after birth.  They are saying he was already at an equivalent 30% when he joined and they are granting him an additional 20%.  If he was deformed when he entered and it got worse in service they cover the worse in service.  That\u2019s literally how that works."
      },
      {
        "id": "o8oyiux",
        "score": 8,
        "body": "I don't understand.\n\n\nAll I was trying to do was get a SC for my right foot just like my left foot.\u00a0\n\n\nI literally have a note from a military podiatrist saying I have deformed feet from military service. I also have trouble walking because of how bad my feet are now. I didn't think trying to connect my other foot would get me a decrease"
      },
      {
        "id": "o8ot5ee",
        "score": 8,
        "body": "People like you are the issue as instead of offering OP legit help you instead just make useless comments like this.  This has nothing to do with the VA not helping vets but the VA following the law which is what\u2019s happening here.\n\nI agree the situation stinks for OP but this in no way shows the Va doesn\u2019t help vets but them doing there jobs and following the rules which require these types of actions"
      },
      {
        "id": "o8ovzxu",
        "score": 8,
        "body": "It\u2019s also in their file they were deformed prior to enlistment.  That\u2019s what they are referring to."
      },
      {
        "id": "o8p063u",
        "score": 8,
        "body": "Same time as you?  I\u2019m going off what you told us.  If you want to post actually letters that would be more helpful.  You say you were born with flat feet but you didn\u2019t have a deformity but are now claiming your flat feet are a deformity?  Which is it?"
      },
      {
        "id": "o8pguqw",
        "score": 7,
        "body": "All depends the exact dates. You also are leaving out tons of crucial information like you should have TWO enlistment exams. 1 for enlisted and 1 before you commision.  You say at meps you noted asymptomatic flat feet but youre not telling us which time you were at meps ..was it for enlisted or commissioning? These are fine details vets leave out when you get on this sub.\n\n There are tons more of fine details involved in an aggravation claim, especially for those reservists, guardsman and people with breaks in service.  \n\nThe advice to request a hearing is the right step for you. Just say you dont understand where they got the pre service percent of 30 percent and want them to double check that.  The main law here is 38 cfr 3.6 and 3.306.  There also alot of m21 manual references regarding these 2 laws. Good luck"
      },
      {
        "id": "o8pm7dg",
        "score": 4,
        "body": "This post is about Op and his experiences and needed help not your personal issues with the VA.  Don\u2019t highjack someone else\u2019s post to vent your own issues as that\u2019s not fair to OP."
      },
      {
        "id": "o8q06m0",
        "score": 4,
        "body": "It says why they rated 30 pre active duty. That is pretty specific and sounds like it was pulled directly from a medical record that must be dated between your enlisted active duty and your officer active duty.  In which case the rating looks correct.  Please note that critical error ratings are reviewed by senior regional office leaders prior to be sent to you, so high level eyes have already reviewed and approved this rating. "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rl0hrs",
    "title": "What to select during job application?",
    "body": "What do you select here?  My example, I\u2019m a 100% P/T and retired military member that retired on 1Jan 2025.",
    "flair": "VA Disability Claims :claim:",
    "score": 130,
    "comment_count": 70,
    "created_at": "2026-03-04T22:57:10+00:00",
    "top_comments": [
      {
        "id": "o8ok0y6",
        "score": 126,
        "body": "Here is flyer about a protected veteran:\n\n[https://www.dol.gov/sites/dolgov/files/ofccp/posters/Infographics/files/ProtectedVet-2016-11x17\\_ENGESQA508c.pdf](https://www.dol.gov/sites/dolgov/files/ofccp/posters/Infographics/files/ProtectedVet-2016-11x17_ENGESQA508c.pdf)\n\nhttps://preview.redd.it/dflhx4lqz3ng1.jpeg?width=1320&format=pjpg&auto=webp&s=1589571e3f1b537e239d50ba93f4ff7b509a53aa"
      },
      {
        "id": "o8okm4n",
        "score": 117,
        "body": "Just letting you know that companies receive tax incentives for hiring a disabled veteran\u2026 "
      },
      {
        "id": "o8oldzk",
        "score": 61,
        "body": "Disabled veteran or protected veteran declining to disclose what group "
      },
      {
        "id": "o8okhi1",
        "score": 50,
        "body": "This is awesome great reference but I still don\u2019t know which to pick.  I was also in Iraq and have a campaign medal."
      },
      {
        "id": "o8on9t1",
        "score": 38,
        "body": "Pick campaign badge veteran."
      },
      {
        "id": "o8om5ew",
        "score": 33,
        "body": "I guess I am the odd man out in that I do disclose that I am a disabled veteran.\n\nI do this because I look at it from the company's perspective. In that they are required by law to report how many disabled veterans they have on staff. They are required to do this to prevent any sort of discrimination against us. It also boosts their stats, where they advertise, \"we're a veteran friendly organization, we have hired ## of vets, and ##% vets make up our work force.\"\n\nLastly, we are a protected class which does indeed provide us with accommodations. (I know, this part may be a negative in being hired. But it has worked out for me up to this point over the years.)"
      },
      {
        "id": "o8ok36z",
        "score": 32,
        "body": "I always just pick campaign badge, but would never mention my disability. "
      },
      {
        "id": "o8ouidu",
        "score": 27,
        "body": "Thank you for the reminder. Sometimes people forget that they were new at one point as well. Don\u2019t get why people are the way they are on here. "
      },
      {
        "id": "o8om9vz",
        "score": 16,
        "body": "\u2026\u2026who meet other criteria such as discharge date or unemployment status.  They don\u2019t get a tax break for hiring disabled vets just because they are disabled."
      },
      {
        "id": "o8p02lt",
        "score": 16,
        "body": "Not the commenter you were responding to, but I'm guessing it's to alleviate the stigma of choosing \"disabled veteran\" since lots of people are afraid that selecting that option will make employers *less likely* to hire them (out of accommodation concerns or something)"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rkz9wy",
    "title": "19k tankers back claims",
    "body": "what's up everyone I was just talking to my lawyer and they're filing a claim for my back because I had sciatica really bad. I was getting shots and then I had to go to a chiropractor for a long time so I was just wondering how back claims go and how they do the percentages for something like that.",
    "flair": "VA Disability Claims :claim:",
    "score": 0,
    "comment_count": 12,
    "created_at": "2026-03-04T22:10:19+00:00",
    "top_comments": [
      {
        "id": "o8om15p",
        "score": 5,
        "body": "https://www.veteransbenefitskb.com/spine"
      },
      {
        "id": "o8ok0gd",
        "score": 3,
        "body": "19k tankers back claims -I'm not sure what this means...."
      },
      {
        "id": "o8of53m",
        "score": 2,
        "body": "VA back ratings are all over the place but sciatica with documented treatment history usually gets you somewhere between 10-40% depending on range of motion and how bad your flare-ups are"
      },
      {
        "id": "o8pd279",
        "score": 2,
        "body": "No such thing as automatically based on MOS. Youd need to articulate how your MOS/duties caused your back issues and the VA would get a medical opinion."
      },
      {
        "id": "o8pucbe",
        "score": 2,
        "body": "I was saying link it to your time in service but I\u2019ll def give this a look "
      },
      {
        "id": "o8q2cfx",
        "score": 1,
        "body": "Ask your lawyer about this."
      },
      {
        "id": "o8oxa3y",
        "score": 1,
        "body": "I just watched some YouTube video where some guy was talking about IVDS and how if you had a certain MOS like 19k you could get your back injury pretty much automatically. I thought it was bs so I came here asking questions."
      },
      {
        "id": "o8q53sv",
        "score": 1,
        "body": "This is an MOS in the Army."
      },
      {
        "id": "o8ptbr2",
        "score": 1,
        "body": "As a 19k myself I\u2019ve never heard this. Not saying you can\u2019t find what you need on youtube every claim is different so def gonna have to still link it "
      },
      {
        "id": "o8pu49m",
        "score": 1,
        "body": "https://youtu.be/7H9k2GkYpPU?si=piyezWfwDQyoNFZm\n\nThis is the guy I heard it from"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rkxwh5",
    "title": "ChampVA questions",
    "body": "Hi, so I enrolled my wife into ChampVa and she recently went to the cardiologist and I understand that we have to pay part of the bill until 3000$ is hit for the year. However I got my explanation of benefits to find out everything was \u201cnot covered\u201d and none of it went towards the deductible. \n\nI am currently on 2 hour hold with them so hoping maybe someone here can help explain better. \n\nChampVA is our primary \u201cinsurance\u201d so I\u2019m not sure. \n\nThanks for any explanation! ",
    "flair": "Health Care :caduceus:",
    "score": 0,
    "comment_count": 10,
    "created_at": "2026-03-04T21:18:22+00:00",
    "top_comments": [
      {
        "id": "o8o1ih7",
        "score": 3,
        "body": "Looks like wherever she went, they dont accept Medicare. They have to accept Medicaid for champva to work.\n\nEdit: it's Medicare"
      },
      {
        "id": "o8o703r",
        "score": 3,
        "body": "You can't trust what these places put online as what they accept for insurance.\n\nLooking for a place recently. Providers website says they accept ChampVA. Called to verify. Thryey do not.\n\nOther places say they work with ChampVA coverage. By this they mean they will provide a \"superbill\" which can be presented to ChampVA so they will consider reimbursing up to the billable amount, which may be a fraction of the billed amount, if they reimburse at all.\n\nOur healthcare system is so fucked.\n"
      },
      {
        "id": "o8o2a3k",
        "score": 2,
        "body": "Medicade or Medicade? It was Kelsey Seybold clinic in Houston which online shows they take it. "
      },
      {
        "id": "o8o1q6b",
        "score": 1,
        "body": "Are you sure the system shows her as not having another insurance?\n\nI don't work for the VA, but all the notes at the bottom hint to them thinking there is another insurance and that it needs to be billed first"
      },
      {
        "id": "o8o4lxd",
        "score": 1,
        "body": "Here are some more specifics on co-pay/deductibles.  (https://www.va.gov/resources/getting-care-through-champva/#care-and-services-we-cover-thr) \n\nhttps://preview.redd.it/tznx1ky4m3ng1.png?width=1244&format=png&auto=webp&s=f960559f7ab6ef47b906e2f848dffddc3b62307a\n\n"
      },
      {
        "id": "o8o2cvk",
        "score": 1,
        "body": "I changed jobs a month ago and no longer have insurance for her as we switched to champVA"
      },
      {
        "id": "o8o6t2x",
        "score": 1,
        "body": "I'm sorry I didnt realize I typed both. My understanding is CHAMPVA is accepted anywhere that MEDICARE is accepted. Looks like a billing error if they accept Medicare. "
      },
      {
        "id": "o8ojnv8",
        "score": 1,
        "body": "Gotcha, well the explanation of benefits (EOB) is leading me to believe that they think otherwise.\n\nDid you have that insurance still at the time of the appointment?  Remember that usually your coverage tends to be til the end of the month."
      },
      {
        "id": "o8oyzes",
        "score": 1,
        "body": "Did you notify champva? "
      },
      {
        "id": "o8oyqv3",
        "score": 1,
        "body": "This is not true, any hospital and hospital affiliated doctor that takes Medicare must take champva. Any other doctor or office is not required to take it even if they take Medicare. "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rkuqio",
    "title": "C-File access",
    "body": "I have seen many complaints here about the time it takes to get a copy of our C-File. I am looking to change that by starting a grass roots lobbying effort to our representatives (both House and Senate). Our C-file should be as easy to access as our medical files.\n\nSince that information is readily available via VBMS, adding the access to the [VA.gov](http://VA.gov) website should be a fairly easy process. It\u2019s not like they would have to create it from scratch. We should have as easy access as the VSOs and accredited representatives that we grant that access to. Once it is set up, it would save time that the RVSRs have to spend on the FOIA requests\n\nI am not seeking full access to VBMS. I only want to have access to the information about myself. Each veteran should have the same access. It is as much our information as our medical records.\n\nIn the letter that I would to write to the representatives, I would like to share the possible reasons that the information is not available. Does anyone know if there is a written directive to not share the information, or is it just a Culture of Nondisclosure? If anyone has helpful knowledge, please share it.\u00a0 We are all in this together!\n\nWhen I have the letter composed, I will share it here as well as a list of who is on both of the Veterans\u2019 Affairs Committees and where to send it. Everyone will be invited to participate and maybe, together, we can get the attention of someone that can make the change we need.",
    "flair": "VA Disability Claims :claim:",
    "score": 41,
    "comment_count": 15,
    "created_at": "2026-03-04T19:19:20+00:00",
    "top_comments": [
      {
        "id": "o8nauk8",
        "score": 12,
        "body": "been dealing with this exact frustration for months now, waiting on my c-file through foia and it's been radio silence. the fact that vsos can pull up everything instantly while we're stuck waiting weeks or months for our own information is ridiculous\n\n  \nyou're spot on about the infrastructure already being there - they're not building anything new, just opening access to what already exists. from what i've gathered talking to other vets and doing some digging, there's no specific written policy blocking this access, it's more like institutional inertia and the whole \"that's how we've always done it\" mentality\n\n  \nthe culture piece is huge though. talked to a vso buddy who mentioned that internally there's this weird protective stance around c-files, like they're worried about veterans \"misinterpreting\" their own records or causing more work for rvsr staff with questions. but that's exactly backwards - giving us direct access would reduce the workload since we wouldn't need to file foia requests for basic stuff\n\n  \nwhen you get that letter together, definitely emphasize the cost savings angle too. every foia request costs them time and money to process, and most of us just want to see what's in there before filing claims or appeals"
      },
      {
        "id": "o8nu4fg",
        "score": 7,
        "body": " The amount of work to scan old files. I previously worked the VA Seattle Regional Office in 1970 and we had stuffed file cabinets holding C-Files. It was so bad that we had to place the files on top of the cabinets. Some veterans had two or more file folders. \n\nThe VA should start with electronic files. "
      },
      {
        "id": "o8ng87e",
        "score": 4,
        "body": "100% agree. Have you guys gone the evetrecs route? I know several waiting on them with no response. Is FOIA typically faster?"
      },
      {
        "id": "o8nxpzl",
        "score": 4,
        "body": "If the files are only on paper, they have to scan the old files anyway when a claim is made. They could start with the files that are already electronic and work on scanning the paper files as needed or as time permits. Perhaps they could use the time saved by giving us access to scan paper files."
      },
      {
        "id": "o8nvoyw",
        "score": 3,
        "body": "I am not sure a c-file exists as a stand alone file in the system. Given the length of time for these to be created, I feel like the information is kept in many different systems/compartments and compiled upon request somehow. I can get exam DBQs in 2-3 weeks, I feel like if a \u201cc-file\u201d existed, it wouldn\u2019t take that long to send us a copy. Having access to our own records through VBMS should absolutely be granted. Thoughts?"
      },
      {
        "id": "o8oletx",
        "score": 3,
        "body": "https://preview.redd.it/ebyyh6m214ng1.png?width=1079&format=png&auto=webp&s=313151db55b937e210e742458d34edd8a7dfdcfd"
      },
      {
        "id": "o8nu61j",
        "score": 3,
        "body": "From a coding perspective I don\u2019t think this would be all that difficult to do. We can already see the names of the files in our C-Files, so they already have the access controls in place to ensure we can only see our own files. They just need to make them clickable. "
      },
      {
        "id": "o8or6fv",
        "score": 3,
        "body": "https://preview.redd.it/bepoujir64ng1.jpeg?width=1284&format=pjpg&auto=webp&s=bc919d431233c1df87334279f2e232a58ff7ee37"
      },
      {
        "id": "o8o387j",
        "score": 2,
        "body": "I just had 2 diagnostic exams as part of a claim. The testing is complete, and everyone can see it but me. The only way I can see the results of my own health testing data is a FOIA request. Bonkers"
      },
      {
        "id": "o8oexxz",
        "score": 1,
        "body": "This may be an easy ask. Then again, probably not. The c-file is only used for compensation and pension/fiduciary claims. There is a lot of the VA benefits that don\u2019t use VBMS. I am not certain all of them use an electronic system to be honest. \nThe guidance comes from Freedom of Information Act and the Privacy Act (5 USC 552a). \n\nThinking like an administrator, if I give you access I will have to give anyone who asks access as well. So, maybe limiting the access is good. \n\nI would love to see the ability to download your files quickly. I know veterans can access their military records through DPRIS. \n\nhttps://milconnect.dmdc.osd.mil/milconnect/public/search/dpris\n\n\nSorry - personal records is privacy act, not FOIA."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rktyyd",
    "title": "Denied because only had electronic records",
    "body": "Had this go to a HLR. 2.5 months later got nothing . Had the one on one meeting and VA said they did find errors.. but since then I had not received any responses until this. Any advise appreciated ",
    "flair": "VA Disability Claims :claim:",
    "score": 2,
    "comment_count": 15,
    "created_at": "2026-03-04T18:51:25+00:00",
    "top_comments": [
      {
        "id": "o8naest",
        "score": 2,
        "body": "That is the first time I heard that was an issue. Good luck in obtaining a proper adjudication. "
      },
      {
        "id": "o8nc57x",
        "score": 2,
        "body": "I had gone to the military doctor for neck pain in 2019 and 2025. I also currently go to Physical Therapy for neck pain. But that missing records statement was in every single one of my 4 other medical issues, all status did not change still denied. Frustrating, wish they would explain if that is why it is denied or because I\u2019m not receiving treatment, etc. "
      },
      {
        "id": "o8ngqy7",
        "score": 2,
        "body": "Both of these claims are for secondary service connection not primary so in service records won\u2019t do anything here as you aren\u2019t claiming the military caused the issues but your primary service connected condition did"
      },
      {
        "id": "o8nh049",
        "score": 2,
        "body": "I did provide evidence of these claim issues during service, but marked them as secondary. would that change anything? Thanks"
      },
      {
        "id": "o8nhmm7",
        "score": 2,
        "body": "If you have inservice records for these issues they need to be claimed as primary not secondary especially since you have inservice records supporting the military caused them then yes change them to primary"
      },
      {
        "id": "o8nhvgk",
        "score": 2,
        "body": "Interesting ok. Thank you. Any advice on the chronic neck pain, a couple of others had the same statements but were primary claims "
      },
      {
        "id": "o8ni7uh",
        "score": 2,
        "body": "For neck pain your going to need a nexus letter to connect your complaints to military service "
      },
      {
        "id": "o8nanir",
        "score": 1,
        "body": "I should say I have no idea why this is denied, has anyone been in this paper and electronic form issue??"
      },
      {
        "id": "o8nbm55",
        "score": 1,
        "body": "What other favorable findings were there if any?\n\nI can bet you weren\u2019t denied due to missing records as I would bet your missing one of the key elements for a successful claim ie nexus, current diagnosis\u2019s etc"
      },
      {
        "id": "o8nr8t4",
        "score": 1,
        "body": "Was the DTA error that they did not have all your records and only had electronic records. You mentioned about missing records, were those paper documents? If so they tried and concluded they have all records that are available."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rkstl0",
    "title": "Backpay",
    "body": "2 things\u2026.i thought intent to file only goes back one year? Secondly\u2026if someone was denied a claim and filed again 10 years later is there backpay in this case?",
    "flair": "VA Disability Claims :claim:",
    "score": 5,
    "comment_count": 13,
    "created_at": "2026-03-04T18:10:35+00:00",
    "top_comments": [
      {
        "id": "o8mw4p6",
        "score": 3,
        "body": "Intent to File does generally preserve the effective date for up to one year, as long as the actual claim is submitted within that one-year window.\n\nAs for a claim that was previously denied and then filed again years later, it usually depends on the situation. In most cases, if someone files a new claim 10 years after a final denial, the effective date would normally be the date of the new claim, not the original one. Back pay to the earlier date typically only happens if the earlier decision is successfully challenged, such as through an appeal that remained open or a clear and unmistakable error.\n\nEvery case can have different facts, though, so the details of the claim history really matter."
      },
      {
        "id": "o8n00po",
        "score": 2,
        "body": "thanks for sharing, the VA intent to file holds your effective date for up to one year to submit a claim, securing back pay to the intent to file date. for a claim filed 10 years after a denial, you generally cannot get back pay for the period unless you can prove a clear and unmistakable error or file within 1 year of the old decision. \n\ni hope this helps! "
      },
      {
        "id": "o8myfw5",
        "score": 1,
        "body": "They also can give you an extra year before you filed in some cases if they think your conditions existed in that period of time . "
      },
      {
        "id": "o8qfp1v",
        "score": 1,
        "body": "Intent to file only holds the date for a year, but... If filing happens within that year, and then the claim gets denied, and then appealed and then denied and then appealed and then granted.... Backpay would go back to intent to file claim date."
      },
      {
        "id": "o8reooi",
        "score": 1,
        "body": "You can file a \"CUE CLAIM \"which is a \"Clear and unmistakable error\"\u00a0\nIf put is ruled that the VA errored by law,\u00a0 by evidence at the time etc then yes you can get back pay all the way back\n\n\nI have a 12.5 year back pay CUE claim in process myself.\u00a0\n\n\nThe va refused to produce my records then denied everything\n\n\nI'm now rated 100% P&T for the same thing they said never happened\n\n\nFought on my own for akbar 13 years before getting a lawyer.\u00a0 \u00a0The va turned over my records to my lawyer with in a week.\u00a0 \u00a0I did FOIA and every other official request for 12.5 years using to get them\n\n\nMy lawyer used my official requests that were never produced to file suit on the va immediately and 1 week boom there the are and everything was in my records\n\n\nThe chances of winning are low especially of you don't have a lawyer\nAnd\nYou only get 1 shot at the CUE claim\nIf you lose you can't try again\n\n\nThat's why I strongly recommend to everyone to get a lawyer for it\n\n\nGood luck\n\n\nGood luck"
      },
      {
        "id": "o8svelq",
        "score": 1,
        "body": "It was deemed service connected and was within the one- year window. It was a mistake on the initial rater. I didn't have to do another sleep study, nor did I have to submit new evidence."
      },
      {
        "id": "o8qiysy",
        "score": 1,
        "body": "Sometimes if new evidence found increase will be based off of that date not intent to file date, happened to me\u00a0"
      },
      {
        "id": "o8n9omb",
        "score": 1,
        "body": "yessir!!! A lot of those claim tied to huge backpay are granted at the BVA level after waiting years to get a favorable decision. "
      },
      {
        "id": "o8pq17k",
        "score": 1,
        "body": "Well said\u00a0\n\n\nTo add to that, those that have received those huge backpays never let the claim died. The must have kept arguing their case/s, thru all the available channels including the board"
      },
      {
        "id": "o8r934q",
        "score": 1,
        "body": "100% facts!!!"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rksgbd",
    "title": "VRE and School",
    "body": "So I'm curious has anyone else used VRE and been recommended school? I'm going through the VRE system and we're currently trying to figure out certifications or School, and I was told doing 1 class online would not qualify me for it then, but the school specifically the VA office of the school said that they can and should since they actively have people doing it that way, and that the credits are the same as full time- I have no clue what either of that means since its not very well for me, but I've looked at the recommended certifications and I'm out of ideas. The only other recommendation I received was to go to the VA and submit ADHD paperwork so I could get accommodations but I feel like that's a bit extreme. I already have 70/120 or so credits to graduation, or else I'd of gone full time just to a local college. Anyone got experience or resources for this to direct me? Feeling a bit overwhelmed \ud83d\ude13 ",
    "flair": "Veterans Readiness and Employment (VR&E) :mortarboard:",
    "score": 3,
    "comment_count": 11,
    "created_at": "2026-03-04T17:57:47+00:00",
    "top_comments": [
      {
        "id": "o8mvdly",
        "score": 4,
        "body": "VR&E is an Employment program not an education program.  I used it."
      },
      {
        "id": "o8n4vwa",
        "score": 3,
        "body": "I got approved for VRE and am taking MBA courses via VRE benefits. "
      },
      {
        "id": "o8mt7ua",
        "score": 1,
        "body": "dude the whole VRE system can be confusing as hell but your school VA office is probably right on this one. If the credits count the same as full time then it should qualify - I've seen people make that work before\n\n  \nThe ADHD accommodation thing isn't as extreme as it sounds if you actually need it. Military life can mess with focus and if you're struggling academically it might be worth looking into. But don't feel pressured to do something your not comfortable with\n\n  \nWith 70 credits already you're in a decent spot. Maybe try calling the main VRE office directly and getting a second opinion? Sometimes the local counselors have different interpretations of the rules and it helps to go up the chain"
      },
      {
        "id": "o8mx2ht",
        "score": 1,
        "body": "I had a lot of issues with this when I used VR&E for grad school.\n\nIt really comes down to your school's certifying official. He logs into a VA system and enters how many credits you're taking, how making credits count as full time, the start/end dates for the semester, and if it's in-person or remote.\n\nWhat counts as full time is different for each program and each school. My SCO put down the correct amount of credits I was taking, but incorrectly put down the full time credit load (he was using the undergrad full time credit load). So my stipend was 50% of what it should've been. I had my program head email the SCO saying that for my program, I was actually taking a full time credit load. After the SCO corrected the info, I received 100% of my allowed stipend. However, I had to do this every single semester because the SCO sucked."
      },
      {
        "id": "o8nkmd2",
        "score": 1,
        "body": "I got approved recently for school.  Told my counselor that I needed to get into a more managerial position so I\u2019m not stuck on a cubicle for 8 hours a day.  So I told her that there are MBA programs that are a year long. She said if I can find one she will approve it.  So I did, and got accepted and she approved it.  Pretty simple.  Although I\u2019m sure my experience is not universal.  "
      },
      {
        "id": "o8mxlrb",
        "score": 1,
        "body": "Yeah this sorta sounds like what the VA from the school for enrollment was talking about but wasn't sure. Because she said I DID count as full time for GCU and even if I did 1 the credits should be applicable. So now I'm waiting for the paperwork to see if it passed. "
      },
      {
        "id": "o8pdldn",
        "score": 1,
        "body": "I got my BS, so what?  It is still an employment program.  If you are smart enough, you can figure out how to make it work to get to school."
      },
      {
        "id": "o8pdran",
        "score": 1,
        "body": "Doesn't depend on the path if what you are implying is that it is not an employment program.  Now, if your three career choices all require skills that need a degree to get, then you are golden."
      },
      {
        "id": "o8mya7t",
        "score": 1,
        "body": "wait--are you taking only 1 class this semester? Is it 100% online? How many credits is that class?\n\nIf your school's SCO says that number of credits is full time, then they put that into the VA's system and they'll see that you're a full time student"
      },
      {
        "id": "o8mxc3v",
        "score": 0,
        "body": "Depends on the path. :') I thought that too\n But it depends on what the justifications are. I'd the career requires degrees or certifications they will pay for it. But that's all I know \ud83d\ude2d because I did not wanna go to college again lmao "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rkrqk6",
    "title": "Static ratings",
    "body": "Are static ratings safe? I\u2019ve read a lot\u2026. So much\u2026. And I\u2019m still confused. All of my current conditions are listed as static. That much I know. A few have definitely worsened over time (2017) was my last increase) and I\u2019m stuck going back and forth thinking do I want to risk it for an increase? I\u2019ve read that static conditions are conditions that won\u2019t get better, only worse. How nervous should I be? ",
    "flair": "VA Disability Claims :claim:",
    "score": 16,
    "comment_count": 17,
    "created_at": "2026-03-04T17:32:18+00:00",
    "top_comments": [
      {
        "id": "o8mpi4r",
        "score": 8,
        "body": "Static conditions are safe as long as you don't mess with them.  You could submit for an increase and end up with a decrease.  I had a rating that was rated over 20 years ago.  I submitted for an increase and went from 10% to 40%, then I foolishly submitted for something else secondary and because I only had the increased percentage for 3 years it wasn't protected and I was reduced back down to 10% based on fabricated ROM."
      },
      {
        "id": "o8ne4dc",
        "score": 7,
        "body": "If you\u2019re going to put in for an increase, or a new claim, I highly recommend getting seen and treated for all currently rated conditions first. Take a few months to see the doctors, get your prescriptions refilled, and send secure messages on VA.gov to your medical team related to everything you\u2019re rated for. \n\nMany of us just suck it up and never get check-ups or treatment for anything we were rate for. Then we put in for an increase or a new claim, the raters look and see we haven\u2019t been to the Dr or complained about anything for years. So they schedule a C&P exam. \n\nI always see the Dr at least once a year and go over how all my rated conditions are impacting me. Important to have that medical evidence! Then you won\u2019t need to worry as much about new claims affecting old claims. "
      },
      {
        "id": "o8mutye",
        "score": 5,
        "body": "So static conditions are conditions the VA won't have you reevaluated for randomly. So you won't get an RFE to check your back in 4-5 years to see if it got better or not.\n\nHowever, if you put in for an increase, the VA will look at your back again. If they determine that your back condition improved, they may recommend a decrease in your rating.\n\nThe best thing to do is to look up the rating schedule for your issues. Then compare how they worsened to the rating schedule.\n\nIt is possible for a condition to get worse, but not in a way that increases the rating. Or you may already be at the highest rating."
      },
      {
        "id": "o8nxm5x",
        "score": 4,
        "body": "How do you check if each condition is static or not?"
      },
      {
        "id": "o8o3zyu",
        "score": 4,
        "body": "https://www.veteransbenefitskb.com/static-check"
      },
      {
        "id": "o8o7ys3",
        "score": 2,
        "body": "What are the codes or where are the codes they talk about"
      },
      {
        "id": "o8r6o5i",
        "score": 2,
        "body": "https://www.ecfr.gov/current/title-38/chapter-I/part-4"
      },
      {
        "id": "o8mxtyz",
        "score": 2,
        "body": "Interesting! Ok, thank you. This is why I\u2019m so nervous! Having VA healthcare has been a lifesaver for me so the fear of losing it weighs on me. I know none of my conditions have got any better but who\u2019s to say they feel the same. It all seems so subjective. "
      },
      {
        "id": "o8npm9y",
        "score": 2,
        "body": "Thank you! Absolutely makes sense! Fortunately for me (or maybe unfortunately \ud83e\udd74) my care team is probably sick of seeing my face because I\u2019m there quite often complaining \ud83d\ude05 I was as you described for a very long time and I just couldn\u2019t take it anymore so for the past 2 years or so, I\u2019ve tried to be really good about making my appointments, getting the imaging done, etc. Hoping it\u2019s pretty well documented at this point. Great advice. "
      },
      {
        "id": "o8my0th",
        "score": 2,
        "body": "Thank you! I\u2019ll look into the rating schedules! I know how my body feels but whose to say they agree \ud83d\ude05 "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rkrdnf",
    "title": "Diagnosed with PTSD but claim denied",
    "body": "Who do I need to get with for help and what documentation do I need to provide typically? First claim and everything got denied\u2026",
    "flair": "VA Disability Claims :claim:",
    "score": 9,
    "comment_count": 31,
    "created_at": "2026-03-04T17:19:23+00:00",
    "top_comments": [
      {
        "id": "o8mlapb",
        "score": 20,
        "body": "You need a qualifying service event "
      },
      {
        "id": "o8mmrdx",
        "score": 16,
        "body": "A well written personal statement could be enough. Buddy letters absolutely would help as well. If you have several buddy letters that say \"I was there on X date with scottgsteph90 and he witnessed the death of X person.\""
      },
      {
        "id": "o8mnori",
        "score": 8,
        "body": "You have others that were there with you write a letter confirming you were there and witnessed the death. Not just that you were in the same general location, but there and witnessed the death with your own eyes."
      },
      {
        "id": "o8n23gi",
        "score": 6,
        "body": "They need more than a doctor saying he has XYZ.\n\nFor PTSD you have to have a verifiable stressor.  They will need documentation and evidence of said stressor unless you have verified combat service, then the stressor is conceded.\n"
      },
      {
        "id": "o8mstd5",
        "score": 6,
        "body": "Here is the link for the form for buddy statement: \n\nhttps://www.va.gov/forms/21-10210/\n\nUse this for people in your squad/unit that were at the event.  I have found having a squad leader or officer that was in charge of you pulls more weight. \n\nHere is the link for personal statement:\n\nThis is YOU statement of the event.\n\nhttps://www.va.gov/forms/21-4138/\n\nMake sure the dates of the event(s) line up.  I know after a few years, the exact date of the event can get foggy.\n\n"
      },
      {
        "id": "o8mqi0s",
        "score": 6,
        "body": "Got it. Thanks. Your best bet is to get buddy letters, preferably from someone higher ranking than you that can state you witness the event. "
      },
      {
        "id": "o8mqscn",
        "score": 5,
        "body": ">We did not find a link between your claimed condition and military service\n\nYou essentially need a Dr to say you have PTSD from XYZ in the military"
      },
      {
        "id": "o8mlm65",
        "score": 5,
        "body": "The event that happened was seeing someone die. I mentioned this in my C&P exam. Do I need to have other documentation? Like a written testimony, a buddy letter to prove I was there? Any other evaluations? "
      },
      {
        "id": "o8niz1l",
        "score": 3,
        "body": "Unless he was seen kn service for anxiety, he will need a stressor event to link anxiety to service. "
      },
      {
        "id": "o8mmspo",
        "score": 3,
        "body": "They seem to be saying they need more evidence to believe you witnessed the event. Buddy statements would help did you fill out anything with mental health after the event while in service?  "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rkqmq3",
    "title": "Does this mean I won? I already receive DIC this is an appeal for back pay",
    "body": "",
    "flair": "VA Disability Claims :claim:",
    "score": 7,
    "comment_count": 6,
    "created_at": "2026-03-04T16:52:05+00:00",
    "top_comments": [
      {
        "id": "o8n4ig0",
        "score": 2,
        "body": "My concern is that the granted might refer to my previous approval for DIC on this appeal. Maybe it\u2019s my current status and not \u201cgranted\u201d "
      },
      {
        "id": "o8nkmoa",
        "score": 2,
        "body": "No worries. Just trying waiting for the ball to drop and see if I get my back pay "
      },
      {
        "id": "o8n68wx",
        "score": 1,
        "body": "Please tell me if the stays on this appeal is referring to my previous claim. To clarify I already receive DIC so maybe the status on this appeal is just showing that I already receive DIC and not pertaining to this appeal for back pay "
      },
      {
        "id": "o8nha98",
        "score": 1,
        "body": "[deleted]"
      },
      {
        "id": "o8otpgh",
        "score": 1,
        "body": "You can check the VA website or app to see if the letter is already there.  This just says they made a decision and are preparing to send you the letter.  "
      },
      {
        "id": "o8ni5wk",
        "score": 1,
        "body": "Ok but it says granted? So is that just my current status? On my DIC currently ? "
      },
      {
        "id": "o8nkfzu",
        "score": 1,
        "body": "Oh so sorry,  I didn't see the 2nd page ,  and sorry for your loss.  "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rkq525",
    "title": "100% PT Florida Property Tax Exemption",
    "body": "Looking for anyone with experience in moving to Florida and filing for property tax exemption. \n\nIm looking at moving later this year and establishing residency in the state after buying a house, will I still be responsible for all property taxes for the rest of 2026? \n\nThanks for any help. ",
    "flair": "VA Disability Claims :claim:",
    "score": 3,
    "comment_count": 10,
    "created_at": "2026-03-04T16:33:43+00:00",
    "top_comments": [
      {
        "id": "o8rmm4d",
        "score": 2,
        "body": "This is because all exemptions start the following January when filed from the previous year.  A lot of people assume it starts immediately upon filing, unfortunately this isn't how they process exemptions.  I also live in Brevard."
      },
      {
        "id": "o8mbwjd",
        "score": 1,
        "body": "You'll still owe prorated taxes for 2026 based on when you establish residency and get the exemption filed - Florida doesn't backdate it to the beginning of the tax year."
      },
      {
        "id": "o8nb5bk",
        "score": 1,
        "body": "Yes, the deadline is March 1st, or 2nd if the first is one a Sunday. You will be responsible for what the current deed holder owed though based on their taxes, not what yours would be for 2027.\u00a0 100 % in Florida is where it is at though. Your children/spouse can get free schooling (I don't know what the residency stipulations are for people that move here after the fact), free License tag, free hunting and fishing license (because you can't come to florida without fishing) among other things.\n\n\n\u00a0Where do you plan on moving? Any cities jump out to you?\u00a0"
      },
      {
        "id": "o8rl0zb",
        "score": 1,
        "body": "You will owe for 2026 since exemptions in FL don't take effect until Jan of the following year.  You won't owe for 2027, but more than likely will still be making payments for it that year.  This is due to how escrow calculates the following year based on what was payed for the previous year.  Your mortgage company should cut you a check for escrow over payment at the beginning of 2028 for what was payed in 2027.  Since your tax bill in 2027 (tax bill gets released around Aug every year and usually payed by your escrow in Nov) should be reduce to close to nothing, this will reflected on your mortgage payments for 2028.  In summary, be expect to still pay taxes for 2027 (you'll be refunded that amount by your mortgage company) and everything should settle down to where it needs to be in 2028.\n\nHopefully this makes sense."
      },
      {
        "id": "o8sllat",
        "score": 1,
        "body": "Yes"
      },
      {
        "id": "o8mcgg7",
        "score": 1,
        "body": "Thanks! I saw some info saying you may be granted a refund for those taxes paid when filing for 2027 but I\u2019m guessing not since I\u2019m not currently a resident. "
      },
      {
        "id": "o8ndnco",
        "score": 1,
        "body": "I got this from the Orange County Property Appraiser. Looks like if you purchase May-November you pay the prorated taxes for the rest of the year but then request a refund for the next tax year when you get the exemption. Basically not getting taxed then, that\u2019s awesome for being a first year resident of the state.\n\nDo you know if Florida makes you have to wait to have a full year of residency before applying for the fishing/hunting license? Arkansas does."
      },
      {
        "id": "o8nhyvp",
        "score": 1,
        "body": "That's crazy if you get a refund, Brevard County didn't do that. I got 100 March 25th of last year, so I had to pay last year in full, but nothing now this year (I have to pay a couple hundred, but not the 4800 I paid last year). I already owned my home before that so that may be the difference. Either way, it's a huge perk. As long as you have a Fl DL, you can get the permit. Florida is pretty easy to get residency, that's why everyone left the big cities up north and came here during COVID.\u00a0"
      },
      {
        "id": "o8soer7",
        "score": 1,
        "body": "I live in Orange County.  They won't refund 2026.  What you are going to hear back from them is that you weren't a resident or did not own a home in Orange County or have an exemption on file prior to the March deadline.  They're going to go to a \"supervisor\" for verification and clarification and come back and apologize for the misunderstanding and let you know that effective 01/01/2027 you'll pay no taxes.  Just wen through this with 2024/2025. Paid 2024, paid 2026, 2025 was refunded in 2026 and won't have to pay from 2026 on..  In your case, you'll probably end up paying 2026 and 2027 and they will refund 2027 in Jan or Feb 2028 as it is already past March 1st."
      },
      {
        "id": "o8sr3up",
        "score": 1,
        "body": "Appreciate the info. I asked about residency status and they said as long as it\u2019s before 1/1/2027. Wonder if it\u2019s worth going to a tax attorney about, seems very misleading. "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rkpum2",
    "title": "Happy Birthday FOIA Request!",
    "body": "I submitted my FOIA request to obtain my C-file on March 4, 2025. As of today, I'm still on step 2 of 5. Is it more appropriate to wish my request happy birthday or happy anniversary?",
    "flair": "VA Disability Claims :claim:",
    "score": 14,
    "comment_count": 7,
    "created_at": "2026-03-04T16:23:00+00:00",
    "top_comments": [
      {
        "id": "o8mfw2x",
        "score": 2,
        "body": "I think they are interchangeable.  Mine was submitted 2/1/25 and is still on step 2 as well."
      },
      {
        "id": "o8mgcm9",
        "score": 2,
        "body": "Crazy. I submitted mine in October 2025 and got it February 2026. "
      },
      {
        "id": "o8mh880",
        "score": 2,
        "body": "Celebrate both!"
      },
      {
        "id": "o8mpbyv",
        "score": 2,
        "body": "Congratulations!\u00a0 It really needs a\u00a0commemorative plaque to mark the occasion.\u00a0 My request is just 10 months old, but I'm really looking forward to celebrating milestones like this."
      },
      {
        "id": "o8n8c6r",
        "score": 2,
        "body": "Submitted mine November 2024 and it has disappeared from the VA website for at least a month now. I\u2019m toast. "
      },
      {
        "id": "o8n90y8",
        "score": 2,
        "body": "Happy birthday! Congratulations on another lap around the sun. I hope it will be a special day for you. What a sad situation! I hope you get it soonest."
      },
      {
        "id": "o8nkfkv",
        "score": 2,
        "body": "I hope to have a relationship with my FOIA request as strong as yours. We\u2019ve been going steady almost 10 months, I look forward to many, many more"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rkozmf",
    "title": "Just got 90%, should I shoot for 100% for anxiety",
    "body": "Currently at 90% a month ago:\n\n30% Allergic Rhinitis \n\n50% Sinusitis\n\n10% Loss of Smell\n\n10% Loss of Taste\n\n30% Migraines\n\n50% Sleep Apnea and Asthma combined (Claims were done at the same time)\n\nI'm not trying to poke the bear but I legit have multiple diagnoses with documented evidence from my ENT, Allergy and Asthma Specialist, Pulmonary, and Therapist in 2020 that I have Anxiety. \n\nMy therapist said that my Anxiety is caused by my AR(allergic rhinitis) and Asthma. I just had my sleep study done and was informed I have sleep apnea and I will be getting my CPAP in 2 weeks. I've just learned that Sleep Apnea can cause anxiety. \n\nI deal with panic attacks multiple times a week, barely or don't socialize at all, constantly tired, lose train of thought, lose interest in conversations, and slur my words a bunch. Also, I wake up still feeling tired and in a terrible mood.\n\nI'm not trying to poke the bear but if I have a legit condition that's medically documented at and outside VA facilities I should fight for it right?......right?",
    "flair": "VA Disability Claims :claim:",
    "score": 0,
    "comment_count": 12,
    "created_at": "2026-03-04T15:51:12+00:00",
    "top_comments": [
      {
        "id": "o8m33sg",
        "score": 4,
        "body": "File for what occurred during service, from service or aggravated by. It's not poking the bear"
      },
      {
        "id": "o8m2xq0",
        "score": 2,
        "body": "Yeah..if you're truly at 90% (I didn't do the math) a 50% anxiety rate will bump you to 100. Also, I don't see any other mental health ratings, and you only get one. So yeah, shoot your shot homie. "
      },
      {
        "id": "o8m3f4i",
        "score": 2,
        "body": "Anxiety secondary to Sleep Apnea is going to be a tough battle. "
      },
      {
        "id": "o8m7jvp",
        "score": 2,
        "body": "![gif](giphy|IDGNYvFLkJKLK)\n\n"
      },
      {
        "id": "o8mors5",
        "score": 1,
        "body": "You should file a claim for whatever is connected to your service. Whether that gets you to 100% or not isn\u2019t as relevant as making sure you are properly rated. "
      },
      {
        "id": "o8nbl8f",
        "score": 1,
        "body": "If you feel it is from service, file. I have 50% sleep apnea secondary to PTSD. The jump from 90-100 is huge.\u00a0"
      },
      {
        "id": "o8m3og8",
        "score": 1,
        "body": "Yeah, but a lot of people are scared to actually claim because they think there will be some type of  retaliation"
      },
      {
        "id": "o8m78m5",
        "score": 1,
        "body": "Well said and says it all. "
      },
      {
        "id": "o8m91hq",
        "score": 1,
        "body": "Your comment was removed because it didn't contribute to the discussion and just wasn't helpful.\n\nCivil disagreements are fine. Insults, personal attacks, slurs, bigotry, etc., are not permissible."
      },
      {
        "id": "o8m4w2x",
        "score": 0,
        "body": "sigh\n\nIf you\u2019re not using a claim shark or paid service (besides a lawyer) then just file"
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rkoqh3",
    "title": "Don\u2019t think you can\u2019t fill for migraines secondary to tinnitus!",
    "body": "After years my fight for what I deserve is over! With back pay! Once I saw I was going to LHI for my exam I was already chalking up another L\u2026 But to my surprise these people actually cared and asked me to discuss either then what was going on daily and had a genuine compassion which blew me away! Again don\u2019t lose hope! Keep fighting for what you deserve!!",
    "flair": "VA Disability Claims :claim:",
    "score": 9,
    "comment_count": 1,
    "created_at": "2026-03-04T15:41:29+00:00",
    "top_comments": [
      {
        "id": "o8mbmzq",
        "score": 1,
        "body": "Well done!  "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rko538",
    "title": "filing for VA claims almost 2 years out of service",
    "body": "Hello,\n\nI am debating filing for VA claims and I know most would say it would be stupid of me not to at all as I was at medical quite often while I was in. I separated 2 years ago and I\u2019m curious on if it would be more difficult for me to get any type of ratings after waiting so long. I had never filed to begin with because I didn\u2019t think I would get much or anything at all (serious case of imposter syndrome) and just overall anxiety about dealing with it all (something I\u2019m ironically trying to file for.) I haven\u2019t seen any doctors since I\u2019ve been out and I heard that can be hard to prove that it\u2019s still ongoing or serious issues but I\u2019m a full time college student now and I don\u2019t really have the money to see a doctor so I\u2019ve just been dealing with my issues. I guess any advice or tips about this possible upcoming process would be greatly appreciated. ",
    "flair": "VA Disability Claims :claim:",
    "score": 13,
    "comment_count": 20,
    "created_at": "2026-03-04T15:19:07+00:00",
    "top_comments": [
      {
        "id": "o8lxjpk",
        "score": 16,
        "body": "Bro, there are still WWII veterans filing claims.  Two years is nothing.  It won't be hard at all to get rated if you have the medical evidence for it."
      },
      {
        "id": "o8m1wl8",
        "score": 6,
        "body": "Nope, not too late at all. First, register for a VA.gov account. Once you\u2019re registered, submit an Intent to File form which you can find on the website. This bookmarks your backpay date to the day it\u2019s received by the VA. Good for 1 year while you get your claims and evidence together. Second, submit a FOIA request for your service records. This form is also available on the VA website and once it\u2019s submitted, this is probably the longest wait for you to receive. I\u2019ve heard they email them now, but a few years ago, they were mailing out CDs and it was taking anywhere from 6 to 9 months to receive. Plus some people didn\u2019t have anything to read the CD with, so keep that in mind. Third, sign up for VA healthcare. You should qualify for it and it\u2019s mostly free for Vets with some co-payments, depending. But better than paying full price for anything medical. This includes medication. Once you have a VA PCP, bring any and all medical info you have, including any private physicians you\u2019ve established care with already and check to see if you can continue seeing them and have the VA pay. These are called Community Care providers and they have to be enrolled in the VA system. This could help you continue your treatment with a Physician you\u2019ve already established a rapport with, while having the VA pay for most of it. \n\nOnce you\u2019re registered for VA Healthcare, the VHA should contact you for your first appointment. Have them schedule it for you or call them if you don\u2019t hear from them within a couple of weeks. This is how you start creating a paper trail to use for your VBA claims. \n\nNow, make a list of the conditions you\u2019re wanting to claim and be able to explain how you got each while Active Duty. Example: you\u2019re claiming Tinnitus because of your exposure to loud noises such as gunfire, explosions, near proximity to aircraft engines, etc. Tinnitus is subjective, so there\u2019s no test which proves you have it. If you have a constant ringing in your ears which began during your service and it\u2019s constant, including now, that\u2019s probably tinnitus. A lot of Vets make the\nmistake of saying it comes and goes, which some examiners will use to disqualify you. It\u2019s probable the buzzing becomes less pronounced at times so there\u2019s a big difference between the lessening of the sound opposed to the sound coming and going. Tinnitus is an easy way to get service\nconnected and even without treatment records from the\nmilitary, can be easily proven. This is based on the loud noises you may have been exposed to. Keep in mind it only takes one incident to cause it, as opposed to multiple exposures like some examiners or raters feel. \n\nOnce you have your list of possible conditions, do research ti prove the link between that condition to your service. If you have service medical records showing a broken leg, for example, and your leg is still causing problems after service, you would need to establish health care to get a current diagnosis, which is a requirement to prove a claim. Make sure you explain to your current Physicians how it was caused during your service, if it was, so they can make notes in your medical file. This helps build up your credibility. You have to prove the link between the service-caused condition to your symptoms and condition after discharge, until today. This can be done through a personal statement as well as your medical records. If your Physician is willing to write a nexus letter for you, which is an opinion from a medical professional linking your current condition to something you had while serving, all the better. \n\nIf you\u2019re familiar with civilian Workers Comp or a car insurance claim for treatment of injuries in an accident, for example, it\u2019s very similar. Think of disability claims as workers comp or auto insurance claims for the Military. You have to prove you got it then, how it affected you, how it continued, even without follow-up treatment, and have a current medical diagnosis from an actual medical professional for it. Don\u2019t feed the info into AI and think the VBA is going to accept that as a medical opinion. Once you submit everything (hopefully before the 1 year Intent to file deadline so you get the backpay), if the VBA feels you have enough credible evidence, they\u2019ll schedule a Compensation and Pension exam for you. This is where a \u201cmedical professional\u201d\u2019hired by and paid for by the VA, will look at your records; speak to you and possibly conduct tests, depending on what you claim, then render a medical opinion which will probably supersede the opinion of your own doctor. Don\u2019t be frustrated if your Physician who\u2019s been treating you for months or years will have their opinion scrutinized, agreed with, or disputed by someone you see for 15 minutes. This is common in the VBA system. \n\nSorry for rambling but the point I\u2019m trying to make is it\u2019s never too late to file. Just work on getting the evidence to prove your conditions. This includes open source info from credible websites. \n\nAnd search through this forum for information and questions you may have. The Knowledge Base created by the senior members here will help answer any questions you may have. This is very important info for you to review so your VBA journey is as smooth as it can be. Good luck!"
      },
      {
        "id": "o8mbfw8",
        "score": 2,
        "body": "I asked for an increase 20 years later. I was medically discharged with cluster headaches 10%. I just dealth with it, because that's what i thought i had to do. A few years ago, someone said I should file a claim because it's been chronic , worsening, and since it was a surgery in the service, i could ask for a raise in rating. \n\nAs i approach 50, i can't handle and power through like i used to. I have sleep apnea (closely tied to cluster headaches), panic attacks because they're so debilitating now, neurological issues that have come on as a result of it. \n\nI went from 10 to 50%. I'll be filing a secondary for panic/anxiet and sleep apnea this year. Get a vso, register with the va and go through the motions."
      },
      {
        "id": "o8nnrfl",
        "score": 2,
        "body": "Im 8 years out and have had a few successful claims so far. Get your records and go through them. \n\nIm using gemini to help me write claims. Its been super useful."
      },
      {
        "id": "o8lyftq",
        "score": 1,
        "body": "I waited almost a lot longer before filing. I guess I wasn\u2019t paying close enough attention during my separation lectures. \ud83e\udd37\u200d\u2642\ufe0f You can definitely make it work. "
      },
      {
        "id": "o8m32yg",
        "score": 1,
        "body": "I ETS'd in 1994 and filed in 2016. 100% several months later!!! Just make sure you have good documentation of medical events, injuries etc!!!!"
      },
      {
        "id": "o8mczw8",
        "score": 1,
        "body": "Don't wait any longer. I waited almost 20 years before I filed. I should have filed right when I got out, it would have been soo much easier\n\n"
      },
      {
        "id": "o8mh676",
        "score": 1,
        "body": "Check dm "
      },
      {
        "id": "o8ms149",
        "score": 1,
        "body": "35 years just got it done"
      },
      {
        "id": "o8n2bvp",
        "score": 1,
        "body": "2 is better than 35."
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rknob1",
    "title": "Va app",
    "body": "Am I just a moron or can you not use the app to create an appointment?",
    "flair": "Health Care :caduceus:",
    "score": 5,
    "comment_count": 13,
    "created_at": "2026-03-04T15:01:05+00:00",
    "top_comments": [
      {
        "id": "o8lufvr",
        "score": 6,
        "body": "I can't comment on whether you are a moron or not.... but use the app to send a message to your PCP and then someone calls. Very efficient!"
      },
      {
        "id": "o8m0p0w",
        "score": 5,
        "body": "Ive been on for an hour waiting. Someone mentioned using the app for appointments. Guess they just send messages"
      },
      {
        "id": "o8lvdm0",
        "score": 3,
        "body": "thanks for sharing, sometimes is easy just to call and speak with someone to schedule based on your availability. "
      },
      {
        "id": "o8mga75",
        "score": 3,
        "body": "Calling sucks with the wait times, but it's usually the best.\u00a0 I have orders/ referrals sitting for 2 months ..... Scheduling hasn't even called me yet.\u00a0\u00a0"
      },
      {
        "id": "o8m163y",
        "score": 3,
        "body": "At this point it seems like my fastest option is just go to the clinic and make an appointment in person. "
      },
      {
        "id": "o8m9c15",
        "score": 2,
        "body": "Wow"
      },
      {
        "id": "o8mf3x9",
        "score": 2,
        "body": "It really isn\u2019t. Use the website, there\u2019s very simple instructions you can find anywhere on the web. \n\nThat being said, for some reason some can be online and some of them have to be phoned. Depends on the department I guess "
      },
      {
        "id": "o8mgq4s",
        "score": 2,
        "body": "Yeah I can\u2019t make any online till after my first appointment typically. The issue is making those first appointments "
      },
      {
        "id": "o8ltlh6",
        "score": 1,
        "body": "You can request one on the web portal and even select a few potential dates/times if they are available.  I can never see dates at my assigned clinic so I just pick the VAMC (Audie Murphy in San Antonio) and I get a call in a few days from a scheduler.    No on hold and no extra trip.   Going in person would probably be faster/"
      },
      {
        "id": "o8m0vlp",
        "score": 1,
        "body": "I might have to do that. "
      }
    ]
  },
  {
    "subreddit": "VeteransBenefits",
    "id": "1rknjxa",
    "title": "Would I be a candidate for TDIU even though I have worked part time jobs?",
    "body": "**BACKGROUND:** \n\nMedically retired in 2020 for PTSD. Had many other physical injuries while in service. Currently 90% overall, 70% for PTSD and the rest is for random stuff like wrist injury, TBI, back, shoulder. \n\nEver since being medboarded out in 2020, I have never worked a full time job. I am 32, and I always had so much ambition so I have tried to work many times. \n\nSince 2020, I have attempted to work 5 different jobs (ALL PART TIME except for one). The longest I managed to stay at any of these was for 7 months. I always quit due to symptoms of my disability. Usually it was due to PTSD or my lower back. I do have emails between me and my bosses where I tell them I am quitting due to my disabilities. \n\n\\-\n\nI just started another part time job and immediately my back is killing me. I am on day two and in a lot of pain. \n\n**QUESTION: Could I apply for TDIU even though I have been technically \"working\" ?** \n\nAgain, its always been part time and I usually have to quit after a couple of months. I have a therapist I see 2x weekly since 2020 for PTSD. I dont have a ton of treatment records for attempting treatment for my back or other injuries simply because my PTSD makes it hard to prioritize other areas of my health. The most I have done for my back is getting pain meds and sometimes getting a steroid shot. \n\nLastly: I do still want to keep trying to work, but in the meantime I'm barely surviving in a HCOL area with my 90% benefits. I need to work to survive at this point. \n\n",
    "flair": "TDIU Unemployability :no-job:",
    "score": 4,
    "comment_count": 21,
    "created_at": "2026-03-04T14:56:20+00:00",
    "top_comments": [
      {
        "id": "o8luu9b",
        "score": 4,
        "body": "Yes"
      },
      {
        "id": "o8m31rk",
        "score": 3,
        "body": "I advise against applying for TDIU if you\u2019re still able to work. You\u2019re rated at 90%, which is generally considered a good position to be in. With TDIU, you cannot earn above the poverty threshold currently $15,960 per year regardless of how many dependents you have. That comes out to about $1,330 per month before taxes.\n\nIn a high cost-of-living area, you could earn at least $3,200 per month working full time in an entry-level job, which is a significant financial difference.\n\nAnother important consideration is that filing for TDIU can reopen your file. That could potentially lead to a reduction or even severance of a disability condition, particularly if you do not yet have the 10- or 20-year protections in place."
      },
      {
        "id": "o8mokh7",
        "score": 2,
        "body": "I would like to pursue a higher rating, but honestly i feel \u201ctoo disabled\u201d to do the labor you are describing. It\u2019s difficult for me to do the bare minimum of functioning everyday, so doing all of the labor to pursue the new claims seems out of reach. I\u2019ve been telling myself to do it for years but i\u2019m never able to make progress. At this point it feels like i wish i had just tried for TDIU years ago since ive never been able to get through the claims process. "
      },
      {
        "id": "o8mh9ig",
        "score": 2,
        "body": "Go to your local vso. They\u2019re there to help you. Open a search engine and use your computer keyboard to type (I like to use Google it\u2019s easy) and then use your mouse to scroll past the sponsored ad and a map should pop up showing different local VSOs to you. Select one and there should be some info, like address or phone number.\n\nUse your cellphone to dial the numbers and a human agent should guide you for the rest of the process. Good luck!"
      },
      {
        "id": "o8n5eav",
        "score": 2,
        "body": "Lol, asshole.\ud83d\ude04"
      },
      {
        "id": "o8qhxfr",
        "score": 2,
        "body": "Okay I see, thanks for sharing this. I dont know what I assumed it would be easier. Also not sure why im being downvoted, any insight? I will definitely check out a VSO and try to push forward. Thanks for the advice. "
      },
      {
        "id": "o8qp9qy",
        "score": 2,
        "body": "Do your intent to file ASAP if you haven't already.  I hooked you up with some upvotes, bud. \ud83e\udd19 Good luck"
      },
      {
        "id": "o8m1ozi",
        "score": 1,
        "body": "Yes you can, you would have to provide the VA with your employment history and how the SC conditions are the reason you cannot work. Even on TDUI, you can work but your annual income has to be really low (can\u2019t think of the amount off the top of my head). Def seek a VSO tho! But your current rating qualifies you. "
      },
      {
        "id": "o8mdgm2",
        "score": 1,
        "body": "TDIU claims are super invasive.  They contact all your previous employers and if you win, you have work restrictions.  I would look for secondaries to your other conditions.  I just hit 100 p&t with ibs secondary to NSAID use for spinal conditions.  Look through the side effect lists of the medications you take for your service connected disabilities.  Make sure your side effects are documented.  You can create the evidence paper trail with direct messaging your VA healthcare team through myhealthyvet. "
      },
      {
        "id": "o8lw2qh",
        "score": 1,
        "body": "Thanks. Any tips for getting started or can you point me in the direction of resources. I have never had to do claims myself because when I was medboarded out all the work was done for me while I was active duty. So i dont have any experience getting it done myself or where to begin."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1k66e36",
    "title": "VA scheduler thought he was on mute",
    "body": "I just had my annual visit last week and my provider put in quite a few consults. For two of them she just said to call the speciality office and schedule an appointment. \n\nI get transferred to the scheduling office for one of the specialities I need to see and they had asked if I had ever been seen by that office before, I was like \u201cmaybe.. I don\u2019t think so\u201d and they were like okay well let me check real quick. \n\nI think they believed they muted me or put me on hold. First I hear him say \u201cwhat the F are you talking about -my name-\u201c and I\u2019m shocked like..does he want me to answer that? So I just sit silent. Then he\u2019s munching on chips. I heard him mocking me by repeating things I said in a high pitched girl-like voice like \u201cI don\u2019t thiiink sooo\u201d. and I hear him talking to a coworker in the background.\n \nThen this man said \u201cI swear if they\u2019re not old and stupid, they\u2019re young and stupid\u201d. Implying that I\u2019m stupid for not remembering that I had been to this office before. Which btw was in 2023. I\u2019ve had brain surgery since then sorry if I\u2019ve forgotten.\n\nFirst of all you have no idea what a veteran has been through. In service, in their life, that week, that day. If you\u2019re going to talk sh*t on a patient you sure as h*ll should double check that you\u2019re muted. I\u2019m so shocked. I was already super anxious and didn\u2019t want confrontation so I just hung up\u2026 I called patient advocate immediately and had to leave a voice mail. But I\u2019m going to ask them to pull the call.",
    "flair": "Healthcare",
    "score": 139,
    "comment_count": 17,
    "created_at": "2025-04-23T18:23:10+00:00",
    "top_comments": [
      {
        "id": "monj87j",
        "score": 112,
        "body": "Not ok. Contact the patient advocate for that location and report what happened.\u00a0\n\nhttps://www.va.gov/HEALTH/patientadvocate/"
      },
      {
        "id": "monpg2b",
        "score": 50,
        "body": "I would've asked what kind of chips he was eating, and then said some things. Glad you called the patient advocate and hopefully this guy will get some much-needed training."
      },
      {
        "id": "monkd4f",
        "score": 46,
        "body": "Sorry, I rage responded before I got to the end. Good on you for contacting the advocate. I\u2019m really sorry this happened to you.\u00a0"
      },
      {
        "id": "montbht",
        "score": 27,
        "body": "Lately I\u2019ve been good at standing up for myself, but I think I was just so shocked I didn\u2019t know how to respond and just hung up. I wish I gave him a piece of my mind"
      },
      {
        "id": "moomgnu",
        "score": 23,
        "body": "With so many good people being laid off or fired by Elon musk, why did they have to leave this a-hole behind"
      },
      {
        "id": "monvanc",
        "score": 16,
        "body": "Im so sorry this happened to you. \ud83d\ude22 Its not okay for you to be treated this way no matter the circumstances. This person does NOT need to be a scheduler. Schedulers are called AMSAs or MSAs. They are on the front lines and can make or break a veteran's experience at the VA so when they do this crap it brings the whole VA down and makes the veteran less likely to call for services or help. I would advise you to request to speak with a supervisor over the AMSA for that department. You can speak with any other scheduler and they should be able to get you into contact with the supervisor. The supervisor will be able to discpline the AMSA and will also require them to do customer service training again. \n\nYou are valued as a patient by many. I hope your experience next time reflects that."
      },
      {
        "id": "monjbbf",
        "score": 13,
        "body": "Good for you! That is inexcusable.\u00a0"
      },
      {
        "id": "mony9s9",
        "score": 9,
        "body": "I\u2019m so sorry this happened to you. Definitely file a complaint with HIPAA (whoever he was talking to had no need to know the details of your medical history) and file a complaint with patient advocate"
      },
      {
        "id": "monw8lw",
        "score": 9,
        "body": "That\u2019s exactly how I feel. I\u2019ve been going to this VA for a few years and have had my ups and downs, but it makes me hesitant to call back and I have a lot of other appointments to schedule. I\u2019m worried to call back that I will get that guy again. I think I\u2019m going to try again later this week, and do it when my husband can sit down next to me.\n\nThank you for the advise, since I had to leave a message the voicemail said it could take up to 3 days to get a call back, I\u2019ll be sure to consider what you said about asking for a supervisor!"
      },
      {
        "id": "moppwb1",
        "score": 9,
        "body": "Ask him if he is young and stupid, or old and stupid. I mean, it sounds like an idiot who doesn't know how to use his phone."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1jc19oz",
    "title": "Arlington is now erasing us",
    "body": "Another example of women being considered part of DEI. Good luck, DOD, with recruiting an all-white, all male military. Sigh\u2026",
    "flair": null,
    "score": 70,
    "comment_count": 10,
    "created_at": "2025-03-15T18:10:30+00:00",
    "top_comments": [
      {
        "id": "mhz4pd5",
        "score": 30,
        "body": "I feel sorry for anyone serving under the bone spur."
      },
      {
        "id": "mhz4j12",
        "score": 26,
        "body": "I hope the women veterans memorial will take a stand."
      },
      {
        "id": "mi1t7hz",
        "score": 11,
        "body": "Racist tyrant and his psychotic ideas"
      },
      {
        "id": "mi0zk8j",
        "score": 10,
        "body": "He is not for us."
      },
      {
        "id": "mi503ph",
        "score": 10,
        "body": "I did a presentation a few months ago on women in the military and how, despite all the barriers to allowing us to serve, wars would be lost without our contributions. From the women who gave up their identities and pretended to be men, the women who traveled with the armies to help feed them, wash and repair their uniforms and assist in providing medical support, the women who stepped up and did factory jobs during the world wars, women have always been key participants in any conflict."
      },
      {
        "id": "mi2va6z",
        "score": 7,
        "body": "They can\u2019t erase us. \n\nThey can try. But they will fail.\n\nTry taking my plot away, motherfuckers. It\u2019s not at Arlington but another beautiful, STATE-FUNDED veterans cemetery."
      },
      {
        "id": "mi4mw8k",
        "score": 4,
        "body": "Waiting for him to try to dig up bodies so he and his buddies can take the spaces."
      },
      {
        "id": "mhz5lbn",
        "score": 3,
        "body": "That direct link still works, but exploring the website itself, there's nothing directing one to find it or anything regarding women or minority figures."
      },
      {
        "id": "mhys8dp",
        "score": 2,
        "body": "[deleted]"
      },
      {
        "id": "miru8t3",
        "score": 1,
        "body": "A draft dodger rich white male is more important than any veteran female under current dictatorship"
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1jukkvq",
    "title": "U.S. Navy Vice Adm. Shoshana Chatfield, the only woman on NATO\u2019s military committee, was fired over the weekend",
    "body": "",
    "flair": "General Chit Chat",
    "score": 69,
    "comment_count": 10,
    "created_at": "2025-04-08T18:19:56+00:00",
    "top_comments": [
      {
        "id": "mm33zek",
        "score": 58,
        "body": "These attacks against DEI in the military hit hard. It\u2019s exhausting to see our service and sacrifices reduced to political talking points.\n\n**We belong**. We\u2019ve led, endured, and served with honor in a system that hasn\u2019t always made space for us. DEI isn\u2019t a threat to readiness or lethality - it\u2019s the reason many of us were finally seen and heard and given space to protect and defend our great country to the absolute best of our abilities.\n\nIf you're feeling frustrated or dismissed, you're not alone. I believe in our collective strength more than ever.\n\nLet\u2019s keep showing up, for ourselves and for those who will follow."
      },
      {
        "id": "mm2s6k9",
        "score": 35,
        "body": "Reasons she was fired:\n\n> The letter said Chatfield posted supportive comments on LinkedIn about a diversity summit and gave a speech in 2015 at Women\u2019s Equality Day. The group quoted her as saying that *investing in empowering women can unlock human potential*.\n> \n> And they also said she was quoted as saying, \u201c*our diversity is our strength*\u201d \u2014 a phrase that Hegseth has repeatedly condemned."
      },
      {
        "id": "mm3ol35",
        "score": 30,
        "body": "Just another effing \u201cexcuse\u201d to fire a  woman and replace with another unqualified man."
      },
      {
        "id": "mm3pjzq",
        "score": 18,
        "body": "Is it not discrimination?"
      },
      {
        "id": "mm44kuk",
        "score": 16,
        "body": "An executive order got rid of the Civil Rights act that covered equal opportunity employment. The office that would have handled discrimination lawsuits has been dismantled.\n\nhttps://www.whitehouse.gov/presidential-actions/2025/01/ending-illegal-discrimination-and-restoring-merit-based-opportunity/\n\nhttps://www.congress.gov/crs-product/LSB11268"
      },
      {
        "id": "mm4nokf",
        "score": 7,
        "body": "Thank you for the encouraging words. Every day, I am made to feel less than\u2026 In so many ways, even after I did my best to serve with honor and integrity."
      },
      {
        "id": "mm45ubh",
        "score": 7,
        "body": "There\u2019s no longer any such policy."
      },
      {
        "id": "mm46u66",
        "score": 7,
        "body": "Wow I\u2019m just reading up on it now\u2026 truly a dangerous time.."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1jcm1gi",
    "title": "Get your weight loss meds ;)",
    "body": "Turning 40 and it has been an uphill battle trying to loose a little weight like I did back in the day. Well I enrolled into the move program and will begin my zepbound journey. For free !!! :) if you\u2019re not sure about enrolling into the MOVE program maybe this might convince you to try it out. In Two weeks my dosage will increase and I won\u2019t get released from the program until I reach my goal weight. ",
    "flair": "Healthcare",
    "score": 61,
    "comment_count": 67,
    "created_at": "2025-03-16T13:59:25+00:00",
    "top_comments": [
      {
        "id": "mi3ium5",
        "score": 9,
        "body": "I get my meds just fine and I\u2019ve been on Wegovy since May 2024. I am going to see if my community care provider will be game to switch to Zepbound when I see them next week, but I haven\u2019t been to a move class since early 2024? There is no requirement (that I\u2019m aware of) to continuously be in a move class/program to continue receiving the meds. That might be an issue with your PCP in not wanting to continue to prescribe meds."
      },
      {
        "id": "mi3c6up",
        "score": 7,
        "body": "They usually release you after one cycle of MOVE. Good luck getting those meds after that."
      },
      {
        "id": "mi43dwz",
        "score": 7,
        "body": "Congrats! Please be careful, as those weight loss meds usually speeds up the process of osteoporosis, and us ladies can develop osteoporosis very easily already :c"
      },
      {
        "id": "mi3t9ip",
        "score": 7,
        "body": "this is amazing, happy for you. I spoke to my pharmacist this past week and have been asking about these meds and have been denied. I knew there was a shortage issue prior, but still not able to get injectables. I probably don\u2019t fall on the top of the list of necessity, but the medication I\u2019m currently on hasn\u2019t proven to be successful. Been on it for 4 months and currently scheduled to titrate to highest dosage. What did you say to your PCP? Thank you and good luck \ud83c\udf40"
      },
      {
        "id": "mi6aonz",
        "score": 6,
        "body": "I had to fight for mine. I started on Mounjaro's compounded version last March. In fact, tomorrow on the 17th it will be exactly a year. Anyway, I paid out of pocket until this past October when I showed them how much weight I had lost, how my cholesterol had gone down, my A1C was all better (!!!), and my blood pressure wasn't high anymore. The pharmacist jumped through hoops and finally it was determined to be easier to get me on the Zepbound for weight loss instead of the Mounjaro for diabetes. They usually put you on Ozempic or Wegovy but since I had been on Mounjaro for so long already, they didn't want to switch me. So we went that route even though she was unfamiliar with it and I was the first. (She was used to the Wegovy/Ozempic.)\n\nThere were a few hiccups (like two months of the wrong dose - 10mg instead of 12.5) and she was reluctant to increase my dose to 15 mg even though I had been on the 12.5/10 for 6 months. I still had some of the compounded left so I added that to my 12.5 mg to make 15. (Don't tell on me!) As of today, I have lost 93 pounds. I was hoping for 100 in a year, but it didn't happen because of the holidays and my reaction to the election. But I should be there by my birthday! I hope. This is the BEST THING I have ever done for myself and I just wish I had started sooner! The only thing I have to do is take virtual health classes which I need anyway. I'm taking one for healthy cooking, one for managing chronic pain, and the one on Mondays where we check in and keep each other accountable and offer suggestions and basically just chat. \n\nIMPORTANT!!! For any of you still at the beginning, I wish I had known about the free app \"MeThreeSixty\" when I started last March. I didn't find out about it until I had already lost 30 pounds. YOU NEED THIS APP - IT IS COOL AS HELL!!! It generates a 360 degree view of your body and compares all the important parts to show how much you have lost and what has changed. You can't post a photo here so I can't show you. If you want to see, send me a message."
      },
      {
        "id": "miaslsb",
        "score": 6,
        "body": "I was put on Ozempic. The side effects were so bad I had to get off it.\n\nI had zero energy. I stopped eating anything but water because whatever I eat immediately triggered explosive diarrhea and flatulence that sprayed fecal mater all over my underwear. I lost zero weight. But I did not put any back on after getting off the med.\n\nI hope this drug works better for you than it did for me."
      },
      {
        "id": "mi54vgy",
        "score": 5,
        "body": "PSA: if you happen to be fortunate (lol) enough to have Diabetes, you can bypass the Move program and get Ozempic."
      },
      {
        "id": "mi3vmcb",
        "score": 4,
        "body": "I was able to get on Contrave after some Move program participation. I\u2019m on my 4th month and down about 15 lbs. pretty slow, but it\u2019s been steady. And it\u2019s a pill, side effects have not been bad. It just makes me less hungry and the cravings have subsided."
      },
      {
        "id": "mi6lrpe",
        "score": 4,
        "body": "This stuff is so easy to get on the gray market."
      },
      {
        "id": "mi6nxw7",
        "score": 4,
        "body": "I start the move program in April of this year\u2026 \nI have so many questions\u2026 I read above that after just one class you can start getting the meds.. so who can we have prescribe them? The provider that did the referral? Also is there any certain criteria that has to be met in order to get them? \nI am just ready to get moving with this weight loss journey.."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1jrexz3",
    "title": "Disabled Veteran with service dog turned away from emergency shelter",
    "body": "During the recent storms and tornadoes across Missouri, a disabled veteran went to a local FEMA shelter and was denied entrance with her service dog and was directed to wait outside. \n\nMissouri Patriot Paws made a post and the people responding said that she doesn\u2019t pay the city taxes and anything else is irrelevant. Except, she did pay city and county taxes and had only recently moved several miles away but in the same county. \n\nI don\u2019t understand people and how they could value taxes above human life. Ironically the posters bio said \u201cBe a kind human.\u201d\n\n",
    "flair": null,
    "score": 59,
    "comment_count": 9,
    "created_at": "2025-04-04T15:39:49+00:00",
    "top_comments": [
      {
        "id": "mlg9oze",
        "score": 19,
        "body": "Not surprised. Lots of vets don\u2019t even consider women vets peers. Toxic af culture."
      },
      {
        "id": "mlhdc22",
        "score": 14,
        "body": "Exactly! They probably thought she was a) lying about being a Veteran, b) lying that it was a service dog, and/or c) all of the above. It annoys me how female Veterans only matter when it helps their agenda."
      },
      {
        "id": "mlkwyom",
        "score": 10,
        "body": "I\u2019m happy for *you* that your anecdotal experience has led to you believe otherwise, but others have experienced enough misogyny to know you\u2019re incorrect."
      },
      {
        "id": "mlmdkq7",
        "score": 3,
        "body": "Shelters aren\u2019t for taxpayers, that\u2019s a troll comment."
      },
      {
        "id": "mlq9omn",
        "score": 3,
        "body": "But I'm sure they \"thanked\" her for her service...\ud83d\ude0f\n\nThese are the kind of people who make me feel angry. \nThose who directly benefit from our military service and then when we need service don't give us any.\n\nThere is NO honor in this emergency shelter turning her and her service dogs away...\n\nFucking shameful \ud83d\ude24"
      },
      {
        "id": "mllvcs0",
        "score": 2,
        "body": "Trump roll back. \n\n  \nAnyone know if she is okay now?"
      },
      {
        "id": "mls2von",
        "score": 2,
        "body": "It\u2019s the lack of human decency. A life is a life. And the people talking about whether or not she had paid her taxes..wth does that matter for? Whether she was a veteran or not. There was a tornado on the ground and someone was killed in another nearby community from a tornado from the same storm."
      },
      {
        "id": "mllvos6",
        "score": 2,
        "body": "She\u2019s fine!"
      },
      {
        "id": "mlig4o9",
        "score": -5,
        "body": "That\u2019s not true at all. What they did was wrong, but why are you blaming other veterans?"
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1jvgq1t",
    "title": "How have the VA cuts affected YOU?",
    "body": "Because I can't post on other socials without getting harassed by the cult, how have the cuts to the VA hurt/affected you? This shouldn't be partisan, but I cannot even say a fucking thing on there without some dumbass attacking me so simply saying \"hey this was my experience today at my VA.\"\n\nMy nurse was telling me all about it, there was a damn table set up INSIDE the VA with a ton of info. I tried to get into pain management and heard it has been gutted by the lady who did scheduling. I have limits on the number of appointments I can have per year, and max referrals is x2 per year. My Dr and nurses are stressed because THEY said that for every 4 workers that gets cut, they are allowed to hire 1, no this doesn't make sense but I guess that's how they are dealing with the freeze (or \"unfreeze\" for federal ppl). No it doesn't make sense, no it isn't helping anyone, no things wont somehow magically get better. Goddamn I am so fucking sick of people ignoring this. \n\nMy congressmen and reps (R's) are MIA, phone disconnected. They don't give a shit.\n\nPeople say they care about the 22 a day, say TYFYS, act like they give a shit, but now that it is time to stand up for us, NOTHING. They are not saying shit. I am the last person who wants to have to get in front of a camera and say \"hey this is happening\" but I'm getting there. ",
    "flair": null,
    "score": 56,
    "comment_count": 37,
    "created_at": "2025-04-09T21:02:48+00:00",
    "top_comments": [
      {
        "id": "mmag2ul",
        "score": 28,
        "body": "I haven\u2019t had a direct impact\u2026 yet. I setup a slew of community care and other appointments in early January that so far have continued without a hitch. Crossing my pregnant fingers it stays that way \ud83e\udd7a\n\nBut I have noticed all the DEI related stuff missing at my VA. We used to have a lovely \u201call are welcome\u201d display with various flags and LGTBQ related benefits. Now it\u2019s just\u2026 bare."
      },
      {
        "id": "mmaej9m",
        "score": 23,
        "body": "I feel the same. Seems all the politicians desire the same thing: a FACIST society and we are the cattle."
      },
      {
        "id": "mmawvsz",
        "score": 19,
        "body": "I miss my VA's \"we serve ALL who served\" displays. I live in Seattle which is like the second largest queer city (maybe on just the West coast? Idk Seattle gay feel different) and they really did what they could to be actively, vocally, supremely loud about their support for the LGBTQ+ community as well as centering POCs and especially women of all races and it's just all gone and it hurts my heart. \n\nI know in the grand scheme of things it's a small change but as a queer but straight-presenting woman it makes me feel like I have to be a little less \"out\" for fear of retaliation."
      },
      {
        "id": "mmah47b",
        "score": 13,
        "body": "I live in a rural area so it\u2019s hard to tell. I\u2019m used to not have access to robust services as well as needing to drive 2 hours to the nearest VA medical center. That being said my county veteran service commission is supposedly facing budget cuts and they provide the service of driving veterans to their appointments. I\u2019m worried about losing access to that since my partner and I share one car."
      },
      {
        "id": "mman32z",
        "score": 12,
        "body": "I have a small clinic 20 min away, but have to drive 2.5 hours for womens healthcare in Fayetteville. Fayetteville has refused to take down inclusive posters and is fighting back (or at least a few weeks ago that was the case) and had an awareness to the cuts table in the lobby."
      },
      {
        "id": "mmaopzm",
        "score": 11,
        "body": "I've already lost a few options that were deemed as gender affirming care. I used to feel mostly safe at the VA facilities, but now my anxiety levels jump when I have to go to an in-person appointment."
      },
      {
        "id": "mmb0f0r",
        "score": 11,
        "body": "I can only imagine how it feels being in that minority! Inclusive spaces benefit literally everyone, so knowing those are being taken down hurts my heart. Those anti-harassment posters made me feel safer as though IF something happens at that VA, I could tell someone and they would do something about it. I just feel so helpless against all this crap"
      },
      {
        "id": "mmaj1sl",
        "score": 9,
        "body": "\"I have limits on the number of appointments I can have per year, and max referrals is x2 per year.\"\n\nwell this is definitely worrisome as me and my husband use VA as our source of healthcare...since it has always had everything we needed! I just had brain surgery last year and all of my treatment has been through VA or referrals...\n\nI see my PCP next week, I will ask her, but as of currently we have heard nothing about any changes."
      },
      {
        "id": "mmcr35u",
        "score": 9,
        "body": "This will be a huge impact. I got very lucky with my amazing surgeon that got me in for a radical breast reduction on February 4th. Literally right under the wire. Mine was medically indicated as I have plates in my neck and am in pain management but it\u2019s still gender affirming care. She is worried, not just about LGBT people(I\u2019m a lesbian) but about Veterans women\u2019s care outright. We make up a small portion of VA healthcare and she has seen the cuts. \n\nAs a plastic surgeon that only does 15 hrs a week at the VA(practices at a very large civilian facility otherwise) she is trying to help as many women as possible at our VA while she still can. I\u2019m afraid she won\u2019t be there at my 6 month follow up. She\u2019s holding the line but in her words \u201cThe spread sheet they sent me could have been done better by my 3rd grader. I\u2019m angry. I DONT HAVE to be here, I CHOOSE to be here. And I love helping vets, especially women veterans. I will fight as long as I can.\u201d It\u2019s insane."
      },
      {
        "id": "mmaht85",
        "score": 8,
        "body": "No direct impacts yet, but I anticipate it-directly and indirectly."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1kappna",
    "title": "Committee Members of the Defense Advisory Committee on Women in Services Have Been Dismissed",
    "body": "FYSA:\n\n\n\nCommittee members of the Defense Advisory Committee on Women in the Services (DACOWITS) have all been dismissed. DACOWITS has existed since 1950 developing guidance to improve the quality of life for women service members. DOD & Congress have implemented nearly 95% of the committee's recommendations. \n\n\n\nI expect the same to happen with some of the advisory committees for the VA.\n\n\n\n[https://thewarhorse.org/military-standards-women-in-combat/](https://thewarhorse.org/military-standards-women-in-combat/)",
    "flair": null,
    "score": 55,
    "comment_count": 13,
    "created_at": "2025-04-29T14:46:17+00:00",
    "top_comments": [
      {
        "id": "mpo6gxk",
        "score": 25,
        "body": "Oh what the fuck"
      },
      {
        "id": "mppu17j",
        "score": 15,
        "body": "This coming Veterans Day needs to be one they'll NEVER forget...we are being treated like the most foul enemy this nation has ever fought."
      },
      {
        "id": "mpp6irg",
        "score": 12,
        "body": "This is total bullshit. Next thing you know they\u2019ll try to bring back k the WACs"
      },
      {
        "id": "mpqb1pe",
        "score": 9,
        "body": "More like they\u2019ll insist the WACs and the other womens services never existed in the first place."
      },
      {
        "id": "mpp6ohx",
        "score": 8,
        "body": "wtf"
      },
      {
        "id": "mpqsau4",
        "score": 7,
        "body": "Like systematically eliminating every memorial regarding women service members. It\u2019s very scary, and oh, the many rights that female veterans had to fight for, like not getting automatically kicked out of active duty (active or reserve) for being pregnant. This is beyond unacceptable"
      },
      {
        "id": "mprqjt4",
        "score": 3,
        "body": "I can\u2019t find any info on this?"
      },
      {
        "id": "mpu9bol",
        "score": 3,
        "body": "I shared the news article. It seems to be the only outlet that has shared this information."
      },
      {
        "id": "mpuscaj",
        "score": 3,
        "body": "The first time I clicked on it I got an error page but I can read it now. Thanks!"
      },
      {
        "id": "n8nvkel",
        "score": 2,
        "body": "One way to stick it back to the man is to make sure that your military service is written in history:\nhttps://womensmemorial.org/make-herstory/\nI recently had my military retirement at this amazing, non-profit memorial in Arlington (ie, not federally funded thus not cancellable!).\nYou can register your service at the above link by just making an account and entering some details about your service and dates. All your personal info is private.\nThis way when we\u2019re old ladies at the VFW wearing our hats, telling our stories, we can look up long lost buddies who we deployed with even if we can only remember their callsign.\nThe Military women\u2019s memorial operates only off of donations and event fees like the one I paid to have my ceremony there. Once you fill in all your registration details and story, I think you can pay a donation to have it printed on nice paper as a keepsake. I haven\u2019t done that part yet, I am still working on my story.\nDoing this tiny thing to counter the current administration\u2019s efforts to erase female military contributions made me feel a little bit better about the future. I hope it helps you too!"
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1rgqnz6",
    "title": "Best IUD insertion process at VA women\u2019s clinic",
    "body": "I have to hand it to the women\u2019s VA clinic in my state- they went all out to make sure that I had the best experience one possibly could in getting an IUD inserted. I actually sobbed at the kindness.\n\nI was quite astonished. I had been mailed a pain pill by my provider a week before to take an hour before the procedure. When I arrived, the nurse went over the basics. She offered me aromatherapy which consisted of this lavender smelling patch on my shirt that I could peel off once I left the clinic. The stirrups were heated. My doctor (woman) asked me if I wanted music playing during the insertion. I declined, and she asked if I was sure because they had a varied and large playlist with almost every genre.\n\nMy nurse talked to me during the procedure and she even held my hand during the insertion. She told me I could squeeze it as hard as I wanted to manage the pain.\n\nI actually cried because it was such a nice experience and they were both so compassionate. The pain pill also relaxed me, so that likely contributed as to why I was so weepy lol.\n\nIt\u2019s the care we absolutely deserve. I\u2019m bragging because this is the gold standard and I want women to know about it.",
    "flair": "Healthcare",
    "score": 52,
    "comment_count": 10,
    "created_at": "2026-02-28T02:31:37+00:00",
    "top_comments": [
      {
        "id": "o7tbpnk",
        "score": 16,
        "body": "This is so nice to hear! I recently got a colposcope done at a VA women\u2019s clinic and they were so compassionate. They put me under at my request due to my history of PTSD and MST. They didn\u2019t want to re traumatize me and they understood that I was putting my trust in them during a vulnerable time. I was treated with such care. I\u2019m happy that other women are experiencing this level of care."
      },
      {
        "id": "o7tcoga",
        "score": 10,
        "body": "It\u2019s truly beautiful. I don\u2019t believe non- VA affiliated doctors would do this for us. I\u2019ve read so many horror stories regarding women\u2019s experiences and they seemed traumatic. \n\nThis is another one of those moments where I am so deeply grateful for the care the VA gives me."
      },
      {
        "id": "o7tgu84",
        "score": 7,
        "body": "What VA do you go to? I\u2019ve never had an experience that nice.  I\u2019ve been trying to make appointments for a while and get redirected to the er"
      },
      {
        "id": "o7v5wvo",
        "score": 6,
        "body": "I am so happy you had a great experience! I would call the patient advocate and ask about nominating the nurse for a Daisy award (not all facilities participate in Daisy awards, but it's worth a try) and ask how to report having great experience to your provider's management. The more we reinforce good care and shine a light on exceptional people, the more it becomes the standard. \ud83d\udc9c"
      },
      {
        "id": "o7x163a",
        "score": 3,
        "body": "I have a great OB/Gyn in Nashville. Dr. Taylor is an angel on earth, like the matron saint of perimenopause. Was super supportive of pain meds for IUD insertion!"
      },
      {
        "id": "o7yxxwy",
        "score": 3,
        "body": "I love my VA women\u2019s clinic, I\u2019m so glad others do too"
      },
      {
        "id": "o7yygag",
        "score": 3,
        "body": "I love this! Which woman\u2019s Va clinic was it?\n\nI also love my local Va woman\u2019s clinic"
      },
      {
        "id": "o85s0g2",
        "score": 3,
        "body": "Hey! I love Dr. Taylor! She\u2019s helped me a ton over the past year! Such a great provider and listener."
      },
      {
        "id": "o7vx1ys",
        "score": 2,
        "body": "I\u2019m so happy for you! Im still active duty but Ive never had a good experience like that \ud83d\ude22 im glad you\u2019ve found good providers!!"
      },
      {
        "id": "o864724",
        "score": 2,
        "body": "I need to move to your VA \ud83d\ude2d"
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1juj3ba",
    "title": "VA Video - Powerful Reminder that you've Earned Your Benefits and Belong",
    "body": "Wanted to share this video that the VA just put out on YouTube. With the title/captioning, don't think it'll get much views, but the actual video is very well done, about a Woman Veteran and her journey/hesitations about going to the VA. It definitely got me in my feels and could relate to in many ways.\n\n[https://www.youtube.com/watch?v=-k84Juai7aU](https://www.youtube.com/watch?v=-k84Juai7aU)\n\nThis video applies to all Veterans. It's also a great reminder about the power of outreach and supporting one another.",
    "flair": null,
    "score": 43,
    "comment_count": 6,
    "created_at": "2025-04-08T17:21:16+00:00",
    "top_comments": [
      {
        "id": "mm4sx8v",
        "score": 6,
        "body": "I got about halfway through it and had to close it. It just makes me feel even more like a fraud because I did none of those things. I'm not that person. I worked my ass off to wear that uniform and all I did was sit in an office and slowly fall apart until they sent me home for being too broken to go to a field exercise.\n\nMy entire TIS feels like a fever dream."
      },
      {
        "id": "mm7p3ei",
        "score": 5,
        "body": "I haven't watched the video yet, but I want to pass on to you that an active duty soldier home on leave told me when I said much the same as you did in your comment. \"Don't ever say that. All the jobs in the military are important. Just because you never went into combat means nothing. You may never know how your work supported the overall missions that the military did while you were in but you joined which the military when so many others did not. You deserve credit just like me.\"\n\nI took that to heart and ever since, I just say \"you're welcome\" when someone thanks me for my service. We ALL deserve to get benefits, no matter what our MOS was."
      },
      {
        "id": "mm4ulf2",
        "score": 3,
        "body": "Damn onion cutting ninjas"
      },
      {
        "id": "mmhtout",
        "score": 3,
        "body": "We all went where we were told and did what we were told. No job is insignificant or even less significant. We all had to work together to get the mission done."
      },
      {
        "id": "mm2iw2s",
        "score": 2,
        "body": "Well done! Very, well done!"
      },
      {
        "id": "mm2xfq0",
        "score": 2,
        "body": "Thank you for sharing, and kudos to the production team. This is very, very well done."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1kd4ajs",
    "title": "Feel like screaming",
    "body": "I had an appointment with the MOVE dr since November that was scheduled to be on June 2nd. Yesterday I got a call from the clinic that it was canceled. No explanation as to why and that it would be rescheduled. Apparently the next soonest appointment is JANUARY 29th. I will have waited for over a year for this appointment and I just feel like screaming. This is ridiculous especially since I\u2019m not the one who canceled my appointment! Is there any I can do like community care or SOMETHING!!!!??? I just feel like crying from frustration and don\u2019t know what to do at this point. My primary won\u2019t prescribe me any injectables even though I\u2019m diabetic because \u201conly the MOVE dr can\u201d but now I\u2019ll literally have waited a year and a half to even see him. ",
    "flair": "Healthcare",
    "score": 42,
    "comment_count": 35,
    "created_at": "2025-05-02T15:48:31+00:00",
    "top_comments": [
      {
        "id": "mq7ubpd",
        "score": 24,
        "body": "This is really infuriating. Can you take this information back to your pcm to try to force it? Or file a complaint and ask for community care?"
      },
      {
        "id": "mq7xlcg",
        "score": 17,
        "body": "I\u2019d definitely speak to someone about community care. \n\nThe VA system is a mess, they are critically short in areas of the VA hospital I used to work at. It\u2019s a shame."
      },
      {
        "id": "mq7vx1s",
        "score": 14,
        "body": "I feel your pain, sis! It was a nightmare just to get my old PCP to acknowledge that I'm eligible for GLP-1s after taking multiple MOVE classes.\n\nThat's when I started to use my private insurance because clearly I was not getting anywhere. I've been on Wegovy for almost a year and have lost 40+ pounds with diet and exercise. I recently told my new PCP about my success, and she told me to send in my current prescription to show that I've been on it. Once they received the information, they promptly sent the drugs to me.\n\nI know it's not possible for everyone to use private insurance, but this was the only way they would acknowledge my request. There are coupons for certain GLPs that could help mitigate some costs.\n\nI'm rooting for you. Always happy to answer any questions you may have.\n\nDon't give up! \u2665\ufe0f"
      },
      {
        "id": "mq8nt8n",
        "score": 11,
        "body": "patient advocate - go see em , call em or msg them thru secure mail. Sometimes they can do stuff faster."
      },
      {
        "id": "mq7ubpi",
        "score": 9,
        "body": "I am also having difficulties with the VA, but mine is with getting HRT. I finally went to MIDI, she was able to access my records and tests and she thinks she can send prescriptions to the VA pharmacy. We will see."
      },
      {
        "id": "mq82muz",
        "score": 8,
        "body": "I had the exact same problem and went with MIDI. I didn\u2019t ask to have my scripts sent to the VA because I didn\u2019t think the VA would accept them from an outside doctor. I know you can get scripts filled from outside doctors through community care but they have an agreement with the VA and it\u2019s authorized. Anyways, went to the VA for a gyno visit and saw a new doctor, mentioned I\u2019m on HRT, and she said I can totally prescribe that for you! She even gave me three months worth of pills at a time and it cost me nothing! \n\nI was paying almost $300 a month through MIDI for visits and scripts but it was worth it because HRT has made me feel amazing. Getting it through the VA has been a life saver on my budget. If your VA doctor refuses HRT go and ask to switch to a new doctor and keep doing it until you get one that will listen. My first doctor that refused was a straight up bitch and told me the VA doesn\u2019t do hormones and HRT causes cancer \ud83d\ude44\ud83d\ude44\ud83d\ude44\ud83d\ude44 Funny how they don\u2019t do hormones but male veterans have no problem getting testosterone through the VA."
      },
      {
        "id": "mq87jn2",
        "score": 7,
        "body": "You have every right to be upset. This isn\u2019t just a scheduling issue \u2014 it\u2019s your health. Push for Community Care under the MISSION Act \u2014 you do qualify since the VA can\u2019t meet your needs in time. And don\u2019t let them gaslight you into thinking you have to just wait it out."
      },
      {
        "id": "mq8yibm",
        "score": 5,
        "body": "Go to your patient advocate. Ask why your facility is limiting prescribing of weight loss medications to MOVE!  Endocrinologists when there are no national restrictions by provider. I suspect your facility doesn\u2019t actually have any restrictions; that\u2019s just what your PCP told you. Then ask why your PCP is either misrepresenting or doesn\u2019t understand facility policy. Then ask what your healthcare team is going to do to get you appropriate care scheduled sooner."
      },
      {
        "id": "mq7wi0f",
        "score": 4,
        "body": "Where are you if you don\u2019t mind answering? I\u2019ve been out of the system for a while since we\u2019ve been overseas. All these posts are scaring me about coming back. I can usually rely on pretty good treatment near Seattle."
      },
      {
        "id": "mqb6obd",
        "score": 4,
        "body": "Yeah it took me 9 months of paying for it myself (no insurance) before they tried to help me."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1j92olh",
    "title": "Feeling disconnected",
    "body": "I got out of the service a year ago but feel frustrated that I can\u2019t fit in the civilian world. I am currently 25 years old and did 7 years in the army. I feel like I didn\u2019t serve long enough to experience a rough transition on the mental part. I have been in therapy for PTSD from which contributes to my fibromyalgia. I don\u2019t like letting other people know about my military background or the things I internally deal with besides therapists. I can\u2019t relate to people around my age. It\u2019s tough. I don\u2019t have any friends where I live, but I have four long-distance friends I can call if needed.\nI feel like I connect with older folks more easily. I have had more genuine conversations with them at random places. I don\u2019t know if I still need to work through the PTSD more or if this is what people meant when they told me it feels lonely out there. I\u2019m currently in college and don\u2019t fit in well. I get irritated in some of my classes due to the disrespect given to professors, yelling, or obnoxious behavior. I want to snap. Next semester, I plan to take only one in-person class and do the rest online. My college has a veteran center, but the times I\u2019ve shown up for events, I don\u2019t get included. There have been times when they thought I was a spouse. If you were to look at me, you\u2019d think I\u2019m some nice 20-something-year-old girly girl. I have lots of internal frustrations. BJJ internally helped me, but my fibromyalgia has interfered with physical activities. ",
    "flair": null,
    "score": 37,
    "comment_count": 11,
    "created_at": "2025-03-11T21:49:39+00:00",
    "top_comments": [
      {
        "id": "mha5pz4",
        "score": 11,
        "body": "I just want to say you\u2019re not alone in feeling disconnected. I feel the same way, down to not having any real-life friends nearby. What are you doing in school? What are you working towards? Have you looked into yoga or anything through the VA? I just started with a \u201cwhole health coach\u201d at my VA and I noticed they have a VVC for chair yoga and tai-chi and a few other things. Might be worth looking into\u2026 I\u2019ve been out wayyyy longer than you and still trying to figure this life out. Hang in there and be kind to yourself! And my chat is always open if you want a new internet friend \ud83d\ude02\ud83d\udc9c"
      },
      {
        "id": "mhahyii",
        "score": 5,
        "body": "I'm 28 have fibro too, AF. \n\nYou 100% can have PTSD, the military really does change you physiologically. \n\nTrauma can be small things too its not all IEDs and bullet wounds. We also don't get to pick what our brain views as trauma. \n\nI felt this way for a couple of years. What helped me get out of it and what I wish I would have done sooner. \n\nI started going to an all womans gym they have yoga and kow impact stuff I can do. I spoke to my doctor got put on a good antidepressant. I have a dog ans we walk every morning. Even if thats the only thing I have spoons for.\n\n Here's my list:\nGotta remember to talk nicely to yourself. \n\nFibro is a real bitch, and you are living life on hard mode right now. Even if others can't see it. \n\nWanting to snap at people for rude behaviors that's a trauma response because you don't feel physiologically safe. Also your feelings are valid  civilians (muggles) can be insensitive, and plain dumb. \n\nSee a thearpist, I started at every week for 3 months, twice a month for a year, I'm now going once a month.\n\nVeteran stuff can feel really weird because alot of the time it's a bunch of dude bros, who have not intrest on actually working on issues. \n\nTry to do what you can physically BJJ is bad ass. Talk with your instructors and see if you are having high pain low mobility day you can just sit in and watch. \n\nIm linking things that help me. The 10 day life support is free and sometimes I just need something to tell me what to do to take care of myself. \n\nBe kind to yourself, it's okay to not being okay. \ud83d\udc99 \n\nCalmstrips help me when I'm really to snap at a muggle. [Calm Strips](https://calmstrips.com/collections/all-products)\n\n\n[10 day life support](https://www.jenniferlatch.com/shop/p/10-day-life-support-checklist)"
      },
      {
        "id": "mhfv1in",
        "score": 5,
        "body": "I\u2019ve been out for decades and still don\u2019t feel like I belong anywhere. I wish I had some female veteran friends but they\u2019re hard to find. I don\u2019t like veterans groups because of the vet bros. So I\u2019m just a lonely weirdo."
      },
      {
        "id": "mhc75tb",
        "score": 4,
        "body": "They\u2019re called college KIDS for a reason. They\u2019re young, immature and obnoxious. Do yourself a favor and do online courses. Find a veteran group or a women veteran group. I dunno about other guys but I\u2019d love to have veteran women friends. Well, I\u2019d just like to have friends. It\u2019s lonely out here."
      },
      {
        "id": "mhbyyuk",
        "score": 2,
        "body": "It took me a while to readjust. I\u2019m working on a way to help women vets do that. Honestly it took me going through a dental hygiene program to feel normal again- and it\u2019s because I was with the same humans every day for 2 years. What part of the country are you in? What are you going to school for?"
      },
      {
        "id": "mhfhaxn",
        "score": 2,
        "body": "Girl, it took me a solid decade to understand these civ lol \n\nI got kicked out of a mommy and me group once cause my humor was wayyyy off. \n\nAs time progresses you\u2019ll get better, stay positive"
      },
      {
        "id": "mhgasxn",
        "score": 2,
        "body": "I understand. At 27, this was exactly how I was feeling. I found other women's veteran groups but I felt I couldn't fit in with them because they had the Vet Bro mentality and kept trying to one-up stories. It was at VetCenters where I had a great therapist who allowed me to speak and she listened that I started to feel some acceptance of myself. Once I accepted that I had changed and I was no longer the same due to service, I realized that I may never feel like I \"fit in\" or feel \"accepted\" because of how I used to be vs who I am post-service. The Vet Bro mentality also affects us because people have a certain image of what a Vet is and how they're supposed to act. It's all about readjusting to who you are now versus who you were before or who you wanted to be post-service. \n\nAs for college, I'll echo what another person said, they're called college KIDS for a reason. I did online college because of that. It irritated me how entitled some kids felt towards professors who have knowledge and are trying to teach.\n\nI'm in my 30s now and I have moments where I have to remind myself that it's not my job to feel like I need to fit in or feel accepted by others, but to feel accepted by myself and my new way of life."
      },
      {
        "id": "mhox3z7",
        "score": 2,
        "body": "Oh yeah, it was ROUGH when I got out. I basically started over at Step 1, and felt so completely lost and alone. I moved cross country with my new-ish boyfriend, married now, and he was all that I had. His family was the first time I ever had someone's family not like me (his father is awkward and his mother is the evil stereotype). We both left the military for school. His program full of great people with a variety of backgrounds. My program full of barely out of high school,  still living at home, mommy and daddy pay for everything little girls. At one point during the program one of said girls even pointed out it was as if I had a target on my back, because I got in \"trouble\" over anything that displeased the staff. See, I didn't keep quiet when people were behaving inappropriately... I didn't fit the mold. It was a small college, and a smaller medical program. Then, my grandpa died. I went from being depressed into a pit of despair with no light.  Let's just say I say on my bed with what I thought in that moment was the way out... I knew that's not what I truly wanted. I told my spouse and went straight to therapy for the first time in my life. It made a world of difference, as well as officially being diagnosed with ADHD. Therapy helped me in that moment, but I have sought out therapy again to work through other things. Every few months I reflect back on changes and honestly it gets better and better. Idk if sharing my story helped, but I hope it helps you not feel so alone in this crappy transition.\n\nThere are a few only women's veteran groups on socials who gather for evenings out, camping, and what not! \n\nYou are not alone! Feel free to message if you would like to chat."
      },
      {
        "id": "mhe9o54",
        "score": 1,
        "body": "Hi! We totally get your frustrations!\n\nWhat you are feeling is not unusual for women who served to feel. What state are you in? Perhaps there are women veteran groups you can take part in whenever you want to help close that connection gap."
      },
      {
        "id": "mi83w4y",
        "score": 1,
        "body": "I hope you\u2019ve applied for some benefits due to the PTSD and fibromyalgia. I went in the military at 17 and got out at 23. I looked like I was still in high school, so really no respect from anyone around me. I moved back to where family was. I started college at 23 and family treated me like I was still 17 even though I had been through a lot including having lived overseas and having gone through a marriage and divorce plus I had migraines and PTSD. I remember a few students asking me to buy them alcohol, and I was that super uncool person saying no thinking: \u201cI\u2019m not getting in trouble for you.\u201d I hope things start to align for you."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1jdbvy2",
    "title": "HRT for my peri/meno ladies",
    "body": "Hi ladies! I went to my well woman appointment this last week, and much to my delight, the PA was well versed in perimenopausal/menopausal hormone replacement therapy (HRT). I know there used to be a lot of hesitation about HRT, but it can be a great option for a lot of us. The VA has a lot of things on formulary that can be prescribed for all the symptoms. Don't be afraid to ask!! \u2764\ufe0f ",
    "flair": "Healthcare",
    "score": 35,
    "comment_count": 11,
    "created_at": "2025-03-17T12:51:43+00:00",
    "top_comments": [
      {
        "id": "mi9t0rk",
        "score": 12,
        "body": "I\u2019m SO glad you got help from the VA with this. I\u2019m 47 and went to Women\u2019s Health at the VA to get help with perimenopause last summer because my life was being destroyed by all of the fun symptoms. My doctor was a complete bitch and I left in tears. I\u2019m one of those people that would rather die than have someone see me cry so I was really embarrassed. I tried hiding out in a corner until I got my emotions under control and a really nice woman came and asked if I was okay. I finally just paid out of pocket and see an online provider. Two months of HRT and I feel fantastic and have my life back. It\u2019s expensive, I have to budget and cut corners on other things, but it\u2019s worth it. The doctor at the VA said they don\u2019t cover any type of HRT."
      },
      {
        "id": "mi9zzul",
        "score": 7,
        "body": "What were they able to do for you?"
      },
      {
        "id": "micvria",
        "score": 6,
        "body": "What a crap provider. If you want to pursue this with the VA, I recommend calling the patient advocate and switching providers. I am so sorry that happened to you! \ud83d\ude22"
      },
      {
        "id": "mjglgse",
        "score": 2,
        "body": "I did a quick search and it doesn't look like it's on the formulary at first glance. You'd have to ask."
      },
      {
        "id": "mid2ndt",
        "score": 2,
        "body": "I\u2019ve thought about calling patient advocate. I did switch providers and asked again about HRT but she told me I was too young \ud83d\ude02 At least she was willing to try and help me with the hair loss but after seeing her one time I was told she\u2019s retiring and my follow up would be with a new provider. At this point I give up. I\u2019m really happy to see other women getting the care they deserve tho! HRT has really been a lifesaver for me."
      },
      {
        "id": "mj1czlk",
        "score": 2,
        "body": "Hey I just want to say a big thank you to you! I went back to the VA again today and requested another doctor, a gynecologist, and she was awesome! She said HRT is covered by the VA and filled my estradiol and progesterone at no cost to me. I was paying $158 a month prescription copay through my online doctor plus $120 a month copay for the visit. The GYN also is treating me for the heavy bleeding I\u2019ve been dealing with for two years. She actually listened and i left feeling really hopeful for the first time."
      },
      {
        "id": "mj1dx87",
        "score": 2,
        "body": "Omg!!! I have happy tears! \ud83e\udd70\ud83c\udf1f YAY!! \ud83c\udf89"
      },
      {
        "id": "n0ifjfz",
        "score": 2,
        "body": "OMG i am SO HAPPY for you! \n\nWe shouldn't have to beg and pull teeth and wait til you see a THIRD provider to get it!"
      },
      {
        "id": "mj8xjec",
        "score": 1,
        "body": "[deleted]"
      },
      {
        "id": "nufltez",
        "score": 1,
        "body": "Does HRT/HT make you non deployable? Can your unit find out about it thru PHA?"
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1jfzexm",
    "title": "You're invited to attend the U.S. Department of Veterans Affairs Center for Women Veterans Social Security Administration (SSA) webinar.",
    "body": "You're invited to attend the U.S. Department of Veterans Affairs Center for Women Veterans Social Security Administration (SSA) webinar.\n\n\n\nThursday, March 27, 2025 at Noon EST.\u00a0\n\n\n\nRegister at [https://events.gcc.teams.microsoft.com/event/8a928197-8f1e-47d3-955f-b86b5a6597a7@e95f1b23-abaf-45ee-821d-b7ab251ab3bf](https://events.gcc.teams.microsoft.com/event/8a928197-8f1e-47d3-955f-b86b5a6597a7@e95f1b23-abaf-45ee-821d-b7ab251ab3bf)",
    "flair": null,
    "score": 31,
    "comment_count": 12,
    "created_at": "2025-03-20T20:56:26+00:00",
    "top_comments": [
      {
        "id": "mivmp77",
        "score": 16,
        "body": "Anyone can read or watch the news. We all know they're going to eliminate thousands of positions at social security and close local offices. They want us all to go into a a central office and identify ourselves. They're hoping that poor disabled people don't have the means to travel 2 hours to one of their central office locations. I don't trust these people as far as I can throw them."
      },
      {
        "id": "mivjshu",
        "score": 10,
        "body": "Why is my first thought that they are trying to remove responsibility for veteran benefits to regular social security doctors, therapists, and process? \n\nAll in the name of privatizing our healthcare, or possibility just women vets on disability??"
      },
      {
        "id": "miv3flg",
        "score": 6,
        "body": "What are they talking about? What's it for?"
      },
      {
        "id": "miv9hr1",
        "score": 6,
        "body": "Per the link: \n\n\"The webinar will cover how to start a social security account online and will provide an overview on Social Security disability benefits and services that meet the changing needs of the public. \u00a0We look forward to seeing you there.\u00a0\""
      },
      {
        "id": "mj09o45",
        "score": 4,
        "body": "Yeah, no. They are disappearing us online and in person."
      },
      {
        "id": "mizrcwi",
        "score": 3,
        "body": "Will he be dressed as this? [https://imgur.com/a/4DtEuqY](https://imgur.com/a/4DtEuqY)"
      },
      {
        "id": "mjicmft",
        "score": 2,
        "body": "I hear you. \n\nI'm just sharing the event for awareness."
      },
      {
        "id": "mjicn80",
        "score": 2,
        "body": "I hear you. \n\nI'm just sharing the event for awareness."
      },
      {
        "id": "miv2gqt",
        "score": 1,
        "body": "View in your timezone:  \n[Thursday, March 27, 2025 at Noon EDT][0]  \n\n[0]: https://timee.io/20250327T1600?tl=You're%20invited%20to%20attend%20the%20U.S.%20Department%20of%20Veterans%20Affairs%20Center%20for%20Women%20Veterans%20Social%20Security%20Administration%20(SSA)%20webinar.\n\n\n^(_*Assumed EDT instead of EST because DST is observed_)"
      },
      {
        "id": "mjicjj2",
        "score": 1,
        "body": "I hear you.\n\nI'm just sharing for awareness."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1q1ho7m",
    "title": "Hurting",
    "body": "I\u2019m at my wits end with my knees today. I hope we\u2019re cannabis friendly in this community. I\u2019m a 22 year retired Army soldier and damn, today my knees ache. Tylenol and mortin haven\u2019t touched the pain. I\u2019ve made elevated 151 and mixed a shot with some raspberry lemonade. So some alcohol and THC, hopefully it helps.  Any advice please ",
    "flair": "Healthcare",
    "score": 26,
    "comment_count": 25,
    "created_at": "2026-01-01T22:51:42+00:00",
    "top_comments": [
      {
        "id": "nx5rarw",
        "score": 14,
        "body": "i think she means 22 year in and retired"
      },
      {
        "id": "nx5pms9",
        "score": 11,
        "body": "I support cannabis as medicine but having been sober 30 years, I would not use alcohol as pain management. I'm 66 years old and I stay away from most pharmaceuticals because they don't really help. I do have my aches and pains and I soak in the bath with Epsom salts, I use magnesium malate for sleep, I wrap joints and bones with flannel and arnica oil. So on and so forth. I was younger I would use the hot springs and soak in the hot water and jump in the cold water ... And of course there is physical therapy and if your service-connected, VA offers some types of therapy. But not to me because I'm rural and I'm not going to drive an hour and a half to get a massage or something lol sorry you're hurting."
      },
      {
        "id": "nx5p8q2",
        "score": 9,
        "body": "I guess it depends on *why* your knees hurt. Are we talking swelling, inflammation, impact pressure, torsion, surgical incisions, what's the rub?\n\nObviously a solid narcotic would solve all of those (temporarily) but narcs are hard to get these days, and while they do give nerve releif they don't solve the problem so when the narc wears off the pain will just be back."
      },
      {
        "id": "nx5rcus",
        "score": 8,
        "body": "22 years of service then retired. She posted in another sub about her service.\n\nPlease use whatever you need to feel better, OP. 420 blaze it if you must. I only did 9 years and occasionally partake to relax."
      },
      {
        "id": "nx6jl8c",
        "score": 7,
        "body": "Hey friend, \n\nGet some voltaren gel and apply it directly to your knees. \n\nCBD+ very tiny THC works better for joint pain\n\nIf you haven't had your vitamin D checked, do that. Being low made my legs hurt so bad. \n\nSigned, another creaky vet"
      },
      {
        "id": "nx5pjzh",
        "score": 7,
        "body": "Are peri or menopausal? HRT helped my joint pain quite a bit. That\u2019s one place to start anyway."
      },
      {
        "id": "nx6ivrk",
        "score": 6,
        "body": "Ah, yes, the infamous \"weather knee\". My mother got them when I was little and I get them now I'm almost 40. That's inflammation, and while it isn't expressly caused by changes in local barometric pressure, it is brought to your attention by said changes.\n\nHot and cold compresses exchanged every couple hours, keep elevated, and yeah probably that thc will do you some good as well. The alcohol... maybe not. Generally alcohol doesn't have any effect on inflamed tissue, just your notice of it. Go easy on the excessive walking, crouching or kneeling for a couple days. I wish you well, op. Hope your doctor listens and takes you seriously."
      },
      {
        "id": "nx63cco",
        "score": 5,
        "body": "Just achy all around the kneecap. I think over using them today or maybe the cooler temperatures in Florida now."
      },
      {
        "id": "nx5u5zh",
        "score": 5,
        "body": "Thanks. Knee pain is fading, don\u2019t know if it\u2019s the 151 or THC. I,TBH, don\u2019t know how strong the THC is in the alcohol. Soaked the flower for 3 months."
      },
      {
        "id": "nx6ce3l",
        "score": 4,
        "body": "THC gummies work better in my opinion on RSO for pain. Start at a small dose first."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1jnz70c",
    "title": "I feel like I lost everything",
    "body": "My career had its ups and downs I didn\u2019t always make the best choices for myself while I was in but I recognize I joined at 19 most of my decision were based off of a survival mindset to get stability. I loved my job,absolutely adored what I was doing who I was helping and the learning and complications the job bright were welcomed because there was always something to learn always someone to help. The first graped happened shortly I got to my first base, buried it. Thought it was my fault. Believed I caused it to happen. I was only forced to process it when OSI pulled me into chat, I didn\u2019t know what it for but when I answered there questions,\u201d like I didn\u2019t want to but it happened\u201d i talked and it all came tumbling out. They wanted my opinion and insight because something happened to another female and people knew the guy and I had \u201crelations\u201d but we didn\u2019t have relations it was only that one time fast forward and he was acquitted of all charges against me and the other girl. I went through alot of care on base because of this and small bases talk. Fast forward and 4 years later I\u2019m graped again. It took everything from me. More PTSD symptoms and problems with that, I developed Rheumatoid Arthritis and Fibromyalgia and a list of other things. And it was this second base where I learned that people will talk from your old base to new base. Little did I know. I found out someone told people at my new base about how I had an investigation against ME for making someone uncomfortable. I was so shocked it hurt me so deeply became this base was my humanitarian assignment. My fresh start. Well it wasn\u2019t because multiple people knew my situation and it wasn\u2019t even the truth. \n\nAfter the second grape. My medical issues affected my job immensely, I had to ask my doctor to put me on a waiver because I was in so much pain, making mistakes, and so unbelievably tired when I got to work. It killed me to ask but she agreed, did the paperwork and I was put on a waiver in 48 hours within the military. I tried to do my best. Show up where I could but it was never enough for my leadership. Why would it be, honestly we were all high functioning and once you lose that I definitely felt like dead weight. My mental took a dive, no one cared about how it was all affecting me, had constant door closed meetings with my supervisor because everyone else wanted to know how I was doing, what was the next update, and always how I could better show up for the office. I couldn\u2019t tell you how many times I said \u201cas far as I know I\u2019m sick and there\u2019s no cure for these diseases and I\u2019ve been told it only gets worse. I\u2019m doing my best.\u201d What stings the most is how I couldn\u2019t show up for the job I loved in my last year of service, and how I will never ever ever be able to work again or experience something like the military again. I will never be able to do what I did before and I miss it so much. I miss my job man. \n\nAnd my vagina after 3 years is still not the same. There\u2019s so much pain now. I feel like I lost a piece of me in every way. I need to let my old job go, I needed to let this out and it felt like the best place was to do it here where someone might be able to relate to me in this way. ",
    "flair": null,
    "score": 26,
    "comment_count": 10,
    "created_at": "2025-03-31T09:27:59+00:00",
    "top_comments": [
      {
        "id": "mkq6v6o",
        "score": 11,
        "body": "I too am a female vet and sexual assault survivor. It took years of fkd up behavior (drink,drugs,etc)on my part and the people I surrounded myself with, before I FINALLY realized that what happened to me was an assault, not a prank but a crime. It took  my sub. abuse counselor 3 years to convince me and finally get me to the point of filing a claim. I\u2019m right here with you \ud83e\udee1#metoo#femalevetsMatter"
      },
      {
        "id": "mknzzxw",
        "score": 6,
        "body": "Hello beautiful stranger, I\u2019m so sorry all of that happened to you. Unfortunately, the military doesn\u2019t handle those type of situations well. I hope you know that none of what happened is your fault, no matter how it happened. I hope you can seek all the physical, mental and emotional help you need to get you through this. You might have to seek it outside of the military, I hope you make it out on the side of this with some good coping mechanisms. \u2764\ufe0f"
      },
      {
        "id": "mko0yag",
        "score": 4,
        "body": "It\u2019s been really hard to let go even two years later, I\u2019m in mental health and I see a bunch of doctors within the VA and outside the VA. It\u2019s so overwhelming and even though I\u2019m trying just feel like my suffering is constant in some way shape or form"
      },
      {
        "id": "ml6ly4s",
        "score": 2,
        "body": "I was raped multiple times in the military. I transferred units and yes they spoke with my old unit. After my transfer, I was raped again. \n\nI reported the first incident and it took years. I decided never to report again as a civilian jury found the first perp not guilty. I had a sane exam and everything. The military found him guilty and kicked him out with a OTH as they didn\u2019t have the ability to give him a dishonorable discharge or do anything more seeing as it was national guard. \n\nI made shitty choices, smoked a ton of weed and drank an absurd amount of alcohol. I got arrested for underage drinking at 20, after two of the assaults. I received a general discharge as a result of my piss test failure. \n\nI smoked weed and drank alcohol when o felt like killing myself. Well that happened to be daily and it still is 9 years later. \n\nAfter getting out, I did school online, got married, had a baby.. BUT I couldn\u2019t retain a job and while I was able to be sober for a few years, I always ended coping with substances. \n\nA few years ago, I was working as a social worker for children\u2019s services. I figured I\u2019d pay it forward and actually help kids/families unlike many other agencies. A detective that I worked on a case with begged me to have an affair while on the job\u2026 he even tricked me into meeting him on the job in which I soon found myself in a scary situation but I left. \n\nI left and internalized everything again. I asked to change cases due to unethical behavior but I did not wish to make a complaint as that FIRST rapist was found not guilty. \n\nI froze. I was locked in a room with a guy twice my height and my age. I knew my chances. Freezing was the BEST and safest way to survive, and it worked because I\u2019m alive today. \n\nWell HR said if I have them any identifying info on that detective that they\u2019d have to file a complaint. Nothing happened. It almost happened but if they found an actual rapist with evidence as not guilty, what the hell is reporting harassment going to do? HR said \u201cwhat about the safety of other employees?\u201d They certainly did everything in their power to pin it on me and finally, at my weakest time, I again repeated history and failed a urinalysis. \n\nSeveral months of horrible treatment at work and I went back to substances. All it took was one time, one day, one mental break down. \n\nI guess the moral of this story is that yes sexual assault apparently is not an issue for much of the population even. Law enforcement across the board (military and civilian) are equally unsafe. Once a target, always a target. The biggest thing I take away is that I can never work again because sexual assault happens in the only field I\u2019m trained/educated in. You aren\u2019t alone. I wish I had a redo. I wish I could\u2019ve stayed at my last job or even in the military. \n\nI\u2019m sharing this because maybe one person will benefit by reading it. A lot of us feel similar and have had similar experiences. I never had a chance. But I\u2019m starting to realize that it\u2019s still not my fault and all of it is not preventable in the workplace (for myself). \n\nKeep your head up OP."
      },
      {
        "id": "mlglb90",
        "score": 2,
        "body": "[deleted]"
      },
      {
        "id": "mks2wly",
        "score": 2,
        "body": "Thank you \u2764\ufe0f"
      },
      {
        "id": "mko0ib6",
        "score": 2,
        "body": "Thank you \u2764\ufe0f"
      },
      {
        "id": "ml7iff3",
        "score": 2,
        "body": "I had a whole thing typed out and it deleted .-.  I had a similar situation before the second rape took place. It was my humanitarian assignment, my fresh start, where no one knew me, but like you said once a target always a target. I don\u2019t think I made myself to be one but he chipped at me, chipped at me for my friendship, chipped at me about my relationship, chipped at me at my confidence. \u201cIf you did this you would feel more confident.\u201d It felt every insecurity I had about my new assignment and what it could bring he saw and just knew what to say to me. I had inappropriate conversations but it realized very quickly he was scary and very manipulative. He was a staff and I was an airman. When I decided I didn\u2019t want to continue, I didn\u2019t think it was a good idea, it was inappropriate for the both of us and we worked together. I told him all this and he wouldn\u2019t leave me alone. He cornered me at the office, in the snack bar, in a conference room just to gauge how I was feeling about him and wanting to move forward with him. He tried to make me feel bad about not moving forward with him all the time. and if he wanted to speak to me I had to listen because he was a staff and I wasn\u2019t an airman even if I was in a completely different section. It got to the point where I just wanted to escape and avoid him all together because no wasn\u2019t working. What made it worse is that people found out. Then I was raped. All within a year of my humanitarian assignment. \n\nI didn\u2019t think anyone shared experiences like this at work, I would beat myself up all the time for what I allowed to happen and I just blamed myself. So guilty. I\u2019ve just been feeling so guilty. \n\nThanks for taking the time and honestly just sharing your experience it\u2019s giving me some clarity and allowed me to let go of some guilt. And honestly I\u2019ve held so much distrust and anger about all of this but after reading your post I feel seen. Understood. I feel less alone. Feels a little weird but I\u2019ll take the peace now that it\u2019s found me. Thank you for sharing. Thank you for helping me."
      },
      {
        "id": "ml8m8ci",
        "score": 2,
        "body": "If you ever want to chat, feel free to message. I don\u2019t check it every day but I will see it. I still feel guilt daily but at the same time I just try to stay logical. I will never go work in any workplace again seeing as this has happened in the military and civilian side of things. It\u2019s sad but honestly, most people really don\u2019t care. Isolation is such a double standard because most of my greatest achievements are surrounded by some of the most traumatic experiences. That alone makes a person want to quit life. Keep moving forward, day by day."
      },
      {
        "id": "mn2slrg",
        "score": 1,
        "body": "That you for your sharing what happened to you. It took me a while to respond because all this can be a bit triggering you know \ud83d\ude2d\ud83d\ude05 I can relate to even saying the other word, it makes me feel a bit better knowing I\u2019m not the only one who still has issues with the grape word. I still shut down and have a hard time saying or thinking it because some flashbacks are still so strong. Thank for sharing when I sought some help for this issue with the chaplain i was told, \u201cwell your so resilient you can push through anything\u201d I think I just wanted someone to tell me I was right for being in pain. Right for being angry. That I had every right to feel this way instead of trying to force me to push through it on their timeline or honestly ignore it and to tell me I\u2019m strong. \n\nAnd I agree. I raised my right hand to fight for my life not to fight against the assault of my own brothers who swore right alongside me."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1jpxrou",
    "title": "Totally ashamed of myself today",
    "body": "I was busy with four kids, but no excuse. Until today I did not know the name Shoshana Johnson. ",
    "flair": null,
    "score": 24,
    "comment_count": 7,
    "created_at": "2025-04-02T19:41:34+00:00",
    "top_comments": [
      {
        "id": "ml397u1",
        "score": 18,
        "body": "There a lot of amazing women who served that we have never heard of. Many we may never know of. This is why we need to share our stories and preserve them."
      },
      {
        "id": "ml2y1hm",
        "score": 12,
        "body": "No shame. When you know better you do better."
      },
      {
        "id": "ml37zv0",
        "score": 7,
        "body": "Thank you for taking me to her story."
      },
      {
        "id": "ml7v9vx",
        "score": 5,
        "body": "I was deployed when this happened in Afghanistan, and I found out about today.  We can\u2019t know everything"
      },
      {
        "id": "ml2u70s",
        "score": 5,
        "body": "I remember that story. I just remember seeing it on the news."
      },
      {
        "id": "ml78h5q",
        "score": 2,
        "body": "I need to look her up."
      },
      {
        "id": "msmu72e",
        "score": 1,
        "body": "You should be ashamed."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1jf8qh4",
    "title": "Misdiagnosis with Military discharge",
    "body": "Does anyone have any experience with a misdiagnosis causing you to get discharged from the military? \n\nI was forced to separate (honorably) due to a Personality Disorder diagnosis in 2017. I have just left my doctor's office through the VA with an Autism/Asperger's diagnosis and a direct discontinuation of my BPD diagnosis. \n\nI lost 2 years of my contract because of this and my dd214 states the personality disorder as the reasoning. What options do I have? I've searched Google a bit, but I want to know your personal experiences on what can be done. I don't want to be vindictive and immediately jump to a lawsuit, but it did significantly ruin my life for a long time after my discharge and I've never fully recovered. \n\nWhat are your opinions and experiences?",
    "flair": null,
    "score": 26,
    "comment_count": 22,
    "created_at": "2025-03-19T21:45:02+00:00",
    "top_comments": [
      {
        "id": "miql5yz",
        "score": 16,
        "body": "Honestly, I left the r/veterans subreddit because I got so tired of the bad attitudes and the way they always defaulted to thinking every veteran is a man."
      },
      {
        "id": "mipyp85",
        "score": 15,
        "body": "Also, y'all are so much nicer than the regular veterans group I asked the same question in. They were judgy jerks."
      },
      {
        "id": "mipybl1",
        "score": 11,
        "body": "Don't file for a discharge upgrade. Don't do that until after you win your service connection for autism first!"
      },
      {
        "id": "mis66mg",
        "score": 9,
        "body": "You probably asked in r/veterans, which is full of angry men. Their sense of entitlement never ceases to amaze me. They are the kings of gatekeeping.\n\nThe worst of the lot are the angry, insecure white men who are mad that they aren\u2019t the de facto bosses of everything anymore. \n\nSo sad for them /s.\n\nThis is the place to be :-)"
      },
      {
        "id": "mis5qfm",
        "score": 7,
        "body": "Mental health professionals that label people with personality disorders are typically doing you a great disservice.\n\nThere are so many reasons you could be exhibiting signs of BPD without even having BPD. PTSD, CPTSD, childhood trauma and even being on the autism spectrum can imitate signs of BPD.\n\nI think BPD is a lazy diagnosis that makes the patient feel condemned to a life of pain and misunderstanding.  \n\nI was misdiagnosed with BPD by a shitty psychiatrist who was nothing more than a high school bully. But I knew what was up and got other opinions.\n\nIf your mental health professional makes you feel condemned or less-than, you need to find another doc/therapist. \n\nNobody deserves to be made to feel this way, especially a veteran who\u2019s been through it all."
      },
      {
        "id": "mip017t",
        "score": 6,
        "body": "I\u2019m sorry this happened and sending you support. I am not sure how to navigate this exactly, but I hope there are others who can share resources."
      },
      {
        "id": "miqd1n3",
        "score": 6,
        "body": "Yeah.... I got diagnosed with anxiety and depression, and then in '23 some genius doctors pushed for a bipolar diagnosis. Was treated for bipolar for over a year, lost my job, mental health (what was left), almost lost my relationship, lost all my friends. After 8 years I finally got a proper diagnosis of cptsd. \n\nPush to see a psychiatrist, ideally through the VA. You can write your congressman and request a review of your discharge"
      },
      {
        "id": "mipytql",
        "score": 6,
        "body": "Oooh that's definitely good advice. I didn't think about that"
      },
      {
        "id": "mipy5wi",
        "score": 5,
        "body": "NVLSP dot org national veterans legal services program. Look it up. They wrote the bible on veteran's benefits. It's called veterans benefits manual. See if you can get a copy of it used or maybe your county service officer has a copy on the shelf. You can fight this and you can win! \ud83d\udcaa"
      },
      {
        "id": "miphp04",
        "score": 4,
        "body": "One thing you can do is file a form 180 to have your DD214 updated. But, I would contact your state veterans service officer; or the VFW. Sometimes they have an office at the VA hospital."
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1j9mfsg",
    "title": "Department of Veteran Affairs (VA) Women Veterans Community Support Forum\nFriday, March 28, 2025",
    "body": "Department of Veteran Affairs (VA) Women Veterans Community Support Forum  \nFriday, March 28, 2025   \n  \nRegister at [https://veteransaffairs.webex.com/webappng/sites/veteransaffairs/meeting/register/854f1a487e6b4045b40760d63cb99571?ticket=4832534b000000057c6f19172d0580a044da69e5241f7396abe8415955eecad5e55a8e830a88652a&timestamp=1741790181345&RGID=r1d0f841d38fbb0ad4a3455c0649b0ff1&isAutoPopRegisterForm=false](https://veteransaffairs.webex.com/webappng/sites/veteransaffairs/meeting/register/854f1a487e6b4045b40760d63cb99571?ticket=4832534b000000057c6f19172d0580a044da69e5241f7396abe8415955eecad5e55a8e830a88652a&timestamp=1741790181345&RGID=r1d0f841d38fbb0ad4a3455c0649b0ff1&isAutoPopRegisterForm=false)\n\nhttps://preview.redd.it/yrk1g7gty9oe1.jpg?width=1080&format=pjpg&auto=webp&s=29dcb09c76cff6a71b43d900dc1a7b1c7ce0c0e0\n\n  \n",
    "flair": null,
    "score": 25,
    "comment_count": 8,
    "created_at": "2025-03-12T15:19:20+00:00",
    "top_comments": [
      {
        "id": "mhel385",
        "score": 7,
        "body": "How about organizing for protests against slashing the budget for veterans"
      },
      {
        "id": "mhexbez",
        "score": 5,
        "body": "At 65 years old with COPD, there isn't much I could do but I would hold up a colorful sign ..."
      },
      {
        "id": "mheqwga",
        "score": 4,
        "body": "I've heard there will be nationwide protests for this on Friday. I've only seen one flyer for Dallas."
      },
      {
        "id": "mhfl5tu",
        "score": 3,
        "body": "A Women Veterans Claims Clinic in my area was cancelled abruptly in February and I figured it was because after one of the exectutive orders they considered anything specific to women as being \"DEI related.\" So I'm actually a little surprised to see this scheduled."
      },
      {
        "id": "mhfptjz",
        "score": 3,
        "body": "They announced on Facebook that they were going to close their FB account and merge with the main VA Facebook page. However, they've since cancelled that announcement and have kept the page. IDK why, but I'm hopeful it's because a bunch of us made a stink about it. \n\nI'm also surprised with this. Let's see how helpful it is."
      },
      {
        "id": "mhfpgkz",
        "score": 3,
        "body": "That's still amazing!"
      },
      {
        "id": "mhlv5ty",
        "score": 2,
        "body": "You are gonna want to google VA march and your area. \n [DC March ](https://action.womensmarch.com/events/everett-wa-solidarity-with-3-14-veterans-march-in-d-c)"
      },
      {
        "id": "mhebipu",
        "score": 1,
        "body": "It looks like OP posted an AMP link. These should load faster, but AMP is controversial because of [concerns over privacy and the Open Web](https://www.reddit.com/r/AmputatorBot/comments/ehrq3z/why_did_i_build_amputatorbot).\n\nMaybe check out **the canonical page** instead: **[https://veteransaffairs.webex.com/](https://veteransaffairs.webex.com/)**\n\n*****\n\n ^(I'm a bot | )[^(Why & About)](https://www.reddit.com/r/AmputatorBot/comments/ehrq3z/why_did_i_build_amputatorbot)^( | )[^(Summon: u/AmputatorBot)](https://www.reddit.com/r/AmputatorBot/comments/cchly3/you_can_now_summon_amputatorbot/)"
      }
    ]
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1jvei1b",
    "title": "\"You Can't Spell Hero Without Her\" Women Veterans Day celebration in Tyler, TX",
    "body": " You Can't Spell Hero Without Her \n\nWomen Veterans Day celebration in collaboration with Veterans Land Board, Texas Veterans Commission Women Veterans Program, Camp V, and UT Tyler Military & Veterans Success Center \n\n\n\nSaturday, June 7th, 2025 | Tyler, TX \n\n\n\nRegister at [https://qrco.de/bfpD3y](https://qrco.de/bfpD3y?fbclid=IwZXh0bgNhZW0CMTAAAR7YHyAx9DaKd7U2K6rUA-aokUrMZ2dYDHTdJcF28uP7w-l_nRWQg55FLYZkug_aem_omGyFkx5G6R3X3DmGUOXWA)\n\nhttps://preview.redd.it/72nlz3o72vte1.jpg?width=612&format=pjpg&auto=webp&s=db535555aae1ad2d6566b287d4a70b2018bd8e1b\n\n  \n",
    "flair": null,
    "score": 23,
    "comment_count": 0,
    "created_at": "2025-04-09T19:29:40+00:00",
    "top_comments": []
  },
  {
    "subreddit": "VeteranWomen",
    "id": "1my2mag",
    "title": "Eagle Scout Project \u2013 Care Packages for post-military Female Veterans (Feedback Wanted)",
    "body": "\n\nHi all,\n\nI\u2019m a Scout working toward Eagle, and for my service project I\u2019m putting together 20 care kits specifically for female veterans. These will be distributed through a nonprofit that serves veterans and their families.\n\nThe idea is to create something practical, respectful, and supportive. Each kit will be packed in a sturdy Osprey backpack and include:\n\t\u2022\t\ud83c\udf92 Backpack: durable women\u2019s travel pack + organizer\n\t\u2022\t\ud83d\udd0c Electronics: Anker power bank, wall charger, charging cables (USB-C & Lightning), and a small protective case\n\t\u2022\t\ud83e\uddf4 Toiletries & hygiene: shampoo/conditioner bars, soap, deodorant, lotion, dental care, lip balm, sanitizer, pads/tampons, wipes\n\t\u2022\t\ud83e\udde6 Comfort & grooming: socks, scrunchies, detangling brush, hair ties, hair clips\n\t\u2022\t\ud83e\ude79 Health & first aid: compact first aid kit, bandages, pimple patches\n\t\u2022\t\ud83d\udd8a\ufe0f Stationery & journaling: notebook, pens, pencils, pouch\n\t\u2022\t\ud83c\udfb2 Entertainment & stress relief: UNO, playing cards, fidget cube, puzzle book, coloring book, crayons\n\nOne challenge I\u2019m running into: I would really like to include underwear and sports bras since those are everyday essentials, but I haven\u2019t figured out the best way to handle sizing, packaging, and cost yet. If anyone has suggestions, I\u2019d love to hear them.\n\nMy goal is to have everything completed and distributed by Veterans Day 2025.\n\nI\u2019d really appreciate feedback from women who\u2019ve served:\n\t\u2022\tDoes this feel useful and respectful?\n\t\u2022\tAre there items you think would be especially helpful that I haven\u2019t thought of?\n\t\u2022\tAnything here that doesn\u2019t make sense or wouldn\u2019t be appreciated?\n\nThanks in advance for any input \u2014 it means a lot to me to get this right.\n",
    "flair": "Seeking Advice",
    "score": 21,
    "comment_count": 16,
    "created_at": "2025-08-23T14:16:14+00:00",
    "top_comments": [
      {
        "id": "na9a3mq",
        "score": 24,
        "body": "There is so much variation in chest size and levels of support needed - I wouldn\u2019t include sports bras."
      },
      {
        "id": "na9cw4n",
        "score": 23,
        "body": "I think you are including plenty enough already. I don't think including undies and sports bras are really going to be a good fit for this project."
      },
      {
        "id": "na9r7o1",
        "score": 13,
        "body": "Skip the underwear and bra. There's just no one size fits most. \n\nWatch some videos online about how Black women care for their hair to see what they need, then try to find the type of brush and clips that are useful to most. \n\nI'd replace crayons with colored pencils just because crayons melt.\n\nThe VA has women's programs and resources. You can contact your local VA hospital's Women Veterans Program Manager to talk over your project and see what resources they have. Go here: https://www.va.gov/find-locations/ Choose VA Health as a facility type and search for a facility that serves your region. You want a hospital, not a clinic. Toward the bottom there should be Women's Health Services. The program manager link should be in that menu."
      },
      {
        "id": "naak1bh",
        "score": 11,
        "body": "I agree that bras and underwear are not something you should include. There\u2019s no way you\u2019d ever land on something that works for everyone/the majority. \n\nOne toiletry you could consider is a nice face sunscreen. I use mine alllllll the time and I feel like many women do. Also, veterans are at a higher risk of melanoma."
      },
      {
        "id": "naahuk9",
        "score": 7,
        "body": "Hell yeah tampons!!!\n\nI like it OP! \n\nThis is really nice of you guys."
      },
      {
        "id": "na9vmu1",
        "score": 7,
        "body": "Thank you. Color pencils it\u2019ll be, I\u2019ll add a pencil sharpener too! I\u2019ll reach out to the local VA hospital.\n\nFrom what I\u2019ve read, the original wet brush appears to be useful for most."
      },
      {
        "id": "naeihju",
        "score": 7,
        "body": "You've done a great job! I'm sure everything you have included is more than enough. It really means a lot. As a female veteran, I don't feel the camaraderie as other male veterans do in veteran spaces. So to be thought of specifically is validating."
      },
      {
        "id": "naeeuzb",
        "score": 5,
        "body": "I\u2019m buying everyone a small teddy bear."
      },
      {
        "id": "naedwjm",
        "score": 4,
        "body": "When I went to go in for my hysterectomy at the VA hospital I was given a care kit and it included a homemade pillow case. It really meant a lot to me in a moment of vulnerability. I still have it on my pillow. So perhaps instead of bra and underwear, a crocheted beanie? Or creative magnet for the fridge? Just something that was made, doesn't have to be perfect."
      },
      {
        "id": "naaq0ez",
        "score": 3,
        "body": "Those are super cool. I would do sunscreen and sunglasses. Doesn\u2019t have to be expensive. I know Trader Joe\u2019s makes a smaller one that I use for my face & arms. It\u2019s more of a gel vs cream and it\u2019s a small container. Sunglasses can be something on the cheaper side. Less than a few bucks. Maybe also a pack of hand wipes or wet wipes. \n\nAll in all I think it\u2019s great. I\u2019d totally dig a care package like that"
      }
    ]
  }
]
```
