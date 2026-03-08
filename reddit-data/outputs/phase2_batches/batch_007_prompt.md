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
    "subreddit": "MilitaryFinance",
    "id": "1ll5yiz",
    "title": "Army refuses to pay GTC",
    "body": "I used my GTC to pay for a hotel that my unit forced me to go to for port operations. My DTS voucher had been approved for about a month now and they refuse to pay it off or pay me my per diem. Is there any type of law or regulation I can use to get my money? They want me to pay out of pocket instead",
    "flair": null,
    "score": 35,
    "comment_count": 39,
    "created_at": "2025-06-26T17:20:38+00:00",
    "top_comments": [
      {
        "id": "mzx2rt8",
        "score": 49,
        "body": "[deleted]"
      },
      {
        "id": "mzx4z89",
        "score": 27,
        "body": "[deleted]"
      },
      {
        "id": "mzx31p2",
        "score": 19,
        "body": "[deleted]"
      },
      {
        "id": "mzx2v5c",
        "score": 16,
        "body": "Yes"
      },
      {
        "id": "mzx2xzz",
        "score": 15,
        "body": "If you\u2019re voucher has been approved and there\u2019s money in the LOA it\u2019s MOD generated and automatically dispersed to your GTC or bank if you changed the distribution account. First talk to your Lvl 25 or 15. If they can\u2019t answer seek BN S4 / RMO. Just keep working up the chain until you get an answer. It\u2019s end of FY with a drastically reduced budget. There might be some wonky stuff going on with funding accounts right now so they can see how much they have to spend by September."
      },
      {
        "id": "mzxclj1",
        "score": 12,
        "body": "Bad advice\u00a0"
      },
      {
        "id": "mzz0c20",
        "score": 10,
        "body": "I\u2019m a DTS ODTA travel a manager and do this for a living every single day. I know the Joint Travel Regulation (JTR)  in -and-out. DM me and I can walk you through step-by-step if you have questions."
      },
      {
        "id": "mzx43bk",
        "score": 9,
        "body": "You don't owe a dime until your travel claim is liquidated.\n\nYou can contact the cc company to extend your due date to avoid late fees."
      },
      {
        "id": "mzx4m59",
        "score": 9,
        "body": "I can\u2019t check at the moment but I showed it to my LT and he said that I was approved and good to go"
      },
      {
        "id": "mzxeeay",
        "score": 9,
        "body": "Did you submit a tax exemption form to the hotel? Maybe the amounts don't match up and they are fighting you"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1l6v8n7",
    "title": "Purchasing land while active duty",
    "body": "O-3 here single with no kids. I currently own a home and fell in love with the location I\u2019m at. So much that I\u2019d see myself here after retirement (PNW).\n\nI don\u2019t see myself keeping my home. I don\u2019t want to keep to rent (I\u2019d like to free up my VA and don\u2019t want to refinance to change from a VA). I\u2019d like to pocket the equity for my HYSA or towards land.\n\nI want to purchase land (3-15 acres, mountain views, and possibly waterfront) such as priest river, sand point, sagle Idaho, or Spokane. \n\nLooking at land price history\u2019s in the area\u2026 everything has skyrocketed the last 10 years. Land has nonstop went up since the dawn of time I\u2019m sure.\n\nI have student loan debt that will be forgiven with through PSLF and I\u2019ve got a truck payment.  I max the TSP and IRA.\n\nI\u2019m mainly seeking others experience. Anyone have insight over investing in land? Not a lot of information out there with goal in line with mine.\n\n",
    "flair": "Question",
    "score": 34,
    "comment_count": 12,
    "created_at": "2025-06-09T03:55:58+00:00",
    "top_comments": [
      {
        "id": "mwscf9z",
        "score": 47,
        "body": "Over most time periods you would be better off investing in the US stock market and then buying the land when you need it rather than buying the land now and letting it sit unused for a few years.\n\n\nUsing US farm land as an example, in 1950 an acre of land was $750 and in 2024 it's about $4,200, all in 2024 inflation adjusted dollars*.\n\n\nAbout a 4.6x return, after inflation. Not bad.\n\n\nBut look at what the S&P 500 did from 1950 to 2024.\n\n\nhttp://www.moneychimp.com/features/market_cagr.htm\n\n\n$1 became $289. A 289x return. Wow. And that's inflation adjusted, in 2024 dollars.\n\n\n$750 invested in the S&P 500, rather than using it for an acre of land would grow to be $216,750. You could buy 51 acres for that today.\n\n\nSo you can certainly make an argument of buying land now as a purchase of something to look forward to after you leave the military.\n\n\nBut don't count on it being a good investment. And it won't provide income while you're waiting to use it.\n\n\nPersonally, unless I had cash to buy the land and I knew the exact piece of land I wanted... I probably still hold off. A lot can change between now and separation. A partner. Kids. Maybe you find another area of the country that's even prettier.\n\n\n* https://www.ers.usda.gov/topics/farm-economy/land-use-land-value-tenure/farmland-value"
      },
      {
        "id": "mwryytq",
        "score": 11,
        "body": "Are you really investing in land if you plan on retiring there?  It sounds more like you are securing your future."
      },
      {
        "id": "mwrxml5",
        "score": 8,
        "body": "Following. Also an O-3 who wants land, but more like Montana, Idaho, or lower. I want/need a lot of acreage for horses/mules. \n\nI\u2019ve also noticed the price of land constantly going up. I feel dumb for not attempting to buy now (when prices are theoretically lower than they will be when I get out), but the Marine Corps is unlikely to station me there, so I can\u2019t use the VA loan now. So I\u2019d have to wait to get out, then use it"
      },
      {
        "id": "mwsjtx9",
        "score": 7,
        "body": "All great points, thank you!"
      },
      {
        "id": "mwu071x",
        "score": 7,
        "body": "I said that because the VA loan is for your \u201cprimary residence.\u201d It would be a hard sell to convince the bank Montana is my primary residence while stationed in 29 Palms, California."
      },
      {
        "id": "mwtpc7f",
        "score": 4,
        "body": "E6 here at 14yos, \n\nWife and I are looking at buying 80acres (off market, mostly tillable)in the area we want to retire at, not really viewing as an investment, but more of an area our kids (3yo 1yo) can grow up at. Live the country life style..\n\nResearch we have done so far:\n\n-who/whom are on the deeds for the parcel of land we want. \n\n-any mineral rights? If so, are they leased out and when does that expire?\n\n-zoning (most of the area is farm land with little local/twp/county zoning\n\n-building codes,\n\n-septic and well testing (are there any restrictions like property line off set)\n\n-electrical ( is 3 phrase electrical easily available or just single, how many \u201cpoles\u201d are needed from the road to an acceptable building site, can the line be unground? \n\n-basic building prices and floor plans. Keeping in mind most don\u2019t include prep/dirt work\n\nHope this helps!\n\nEdit: formatting on mobile"
      },
      {
        "id": "mwrvs6c",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1hqdbse/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "mwxi3dt",
        "score": 1,
        "body": "Keep in mind that not all lenders offer land loans and the ones that do may charge significantly higher interest rates. When we bought land in 2019, it was at 10% when mortgages for houses were like 3%. I don\u2019t have updated information so it may be comparable now but it would be worth considering buying land with some kind of house on it."
      },
      {
        "id": "mwzg16j",
        "score": 1,
        "body": "Keep in mind the insane price increases in a lot of places for over the last several years it going to hit a bubble breaking point soon if they already haven\u2019t. I\u2019ve seen some places finally start cooling down and given the current economic situation, I think it\u2019ll cool off more, if not crash in some places. Maybe take some time to find a more perfect lot and let things settle out more before potentially buying at a peak. There have been times over the last couple of decades I wish I would have bought sooner, but lately I\u2019m more glad we waited on the most recent purchase. (I would have waited longer, but my wife was more impatient and she put up the money, so you know the saying). But good land can disappear to develop and go up quickly based on what\u2019s going on around it, so you need to be tuned into that area\u2019s market and overall general going ons. Also, keep in mind your priories and desires might change. A spouse, kids and many other things could shift your mindset. Looking back when I first joined to now, it\u2019s mind blowing how much I\u2019ve charged \u2013 my likes, interests and goals changed \u2013 compared to my teens, 20s, 30s and 40s."
      },
      {
        "id": "mws1bs0",
        "score": 1,
        "body": "Investing in a since of saving money on the front so I\u2019m not paying way more in the future. I also see what you\u2019re saying, yes I\u2019d be retiring there or at least that\u2019d be the goal."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1ky5kka",
    "title": "Am I crazy? Stop contributing to TSP or not?",
    "body": "We are mil-mil (Es), both planning on retiring in ~10 years. We are currently in early 30s, expecting to withdraw from both TSPs at 59 1/2 (if we don't roll them over into IRAs and withdraw contributions sooner). \n\nWe each have ~$200k in TSP currently. According to a 401k calculator, if we lower contributions to 5% for the matching for the next 10 years (currently maxing), with a 6% return and 3% inflation rate, we would have a total of ~$380k at our end of service (stopping contributions at this time) and ~$1.15M at withdrawal age (~$650k today). \n\nIf we withdraw at fixed purchasing power monthly,\u00a0~$5.4k/month can be withdrawn from age 60 and increase 3% per year until 85. It is equivalent to\u00a0~$3.1\u00a0in purchasing power today.\n\nGoing by today's numbers, because it is easier for me to do the math, we can expect to pull ~$6.2k from our TSPs combined (~$74.k yearly) + retirements (~$60k) = ~$134k (not including disability because nothing is guaranteed, but even higher if so). \n\nDo we need anymore $$ than that at 60+?? Kids will be out of the house and expecting a house (or 2) to be paid off. We currently spend ~60k/year in a HCOLA (minus mortgage), and I feel like we live a full life. All of our needs are met, multiple staycations/vacations per year, kids have everything they need + most they want, etc. \n\nAm I crazy to think we can lower our TSPs to 5% and invest that more into the kids (currently have UTMAs, maybe setup 529s even tho they will get our GI bills)/fancier vacations/private schools (never considered this a realistic option)/the Now instead of the Future/etc, and still be good when it comes time to fully retire? \n\nEdit:\nBoth have IRAs: ~$50k\nHYSA:~$20k\nTaxable: ~$110k\nPlan: at least spouse FIREs, if I have to work it shouldn't be hard to get a job, and I wouldn't mind too much (historically seen ~$150k/yr with similar backgrounds)",
    "flair": "Question",
    "score": 30,
    "comment_count": 37,
    "created_at": "2025-05-29T08:29:18+00:00",
    "top_comments": [
      {
        "id": "muuox2m",
        "score": 47,
        "body": "You are not crazy, but anything can happen in 10 years. If you were at 17 years you could probably feel okay doing it, but you have a long way to go. I would double check your TSP calculations because those seem high for your current balance\n\nOne of you could end up with a situation where you need a med board, we could end up in another war where you both deploy constantly, we could have another riff. These are just a few examples where your pension plan could change and you would be thankful for more TSP\n\nThere\u2019s additional things to consider, such as the price in the area you want to retire, price of hobbies, etc all outpace inflation and you end up coming short again\n\nBL: double check TSP withdraws. Anything can happen in the future and it pays to be prepared"
      },
      {
        "id": "muw02fp",
        "score": 18,
        "body": "I thought I was good at my 10 year mark. That was 2010.\n\nFrom 2014 to 2016 we went through sequestration and I barely made it through the process of retention during draw down boards. I got selcon as an option, many did not.  Some had seven months to depart the army. \n\nA lot can happen in the next ten years. \n\nI would continue to contribute more than the match amount."
      },
      {
        "id": "muvnycf",
        "score": 11,
        "body": "Think about the order of operations for retirement- 1) Traditional Investment Accounts (brokerage). 2) Tax-deferred Accounts (traditional TSP/401K, employer matches, Traditional IRA). 3) Tax-advantaged accounts (Roth TSP/401K). 4) Roth IRA in this order: contributions, conversions, earnings. \n\nThe reason for this order is to allow Roth accounts the longest time possible to keep growing tax-free prior to making withdrawals. Withdrawing your TSP contributions prior to 59.5 is going to take away a TON of potential gains so I\u2019d avoid that if at all possible and use a brokerage account first. \n\nA brokerage account can bridge the gap between when you retire from the military and when you turn 59.5. It will allow you to FIRE much earlier, too. Figure out what age you want to FIRE and subtract that from 59.5, then figure out how much you\u2019ll need to make MONTHLY, not including your pension and any VA disability. Multiply that monthly number by 12 and again by how many years early you want to retire under 59.5. The result is how much you should aim to get stashed away in the brokerage account.\n\nMy wife and I have a joint brokerage set up for this exact purpose. Any excess money after TSP/401k, IRA\u2019s and 529 goes into this account every month. We don\u2019t do anything crazy with it, just have it all in an S&P 500 index fund. We want to FIRE at age 55, so we need 5 yrs expenses less my pension/VA claims saved to bridge that gap. Plus the brokerage account can be used for a retirement home down payment or curveballs if necessary. It\u2019s all about prolonging the Roth accounts and letting them grow for as long as possible. \n\nBut 59.5 is just the age you\u2019re ELIGIBLE to start making penalty-free withdrawals. It doesn\u2019t mean you HAVE to. So ideally if you can find a way to postpone TSP withdrawals and stash away more money in the brokerage to let your TSP keep growing a few years past 59.5, do it! \n\nLook into SWD\u2019s (Safe Withdrawal Rate). Typically people live on 3-4% annually during retirement. $5.4K is 5.6% of $1.5M, so your calculation is almost double the recommended amount, unless you really are wanting to burn through your TSP quickly. \n\nMy understanding with the GI Bill is that it typically does not cover every single aspect of college and so opening a 529 in addition is the recommended best option (there are some great threads about 529\u2019s in this sub). That way you have options with the 529: either your kid uses the money for school, they can roll the 529 into a Roth IRA and jumpstart their own retirement, you can withdraw the amount of any scholarships they got tax-free, or if they don\u2019t use the account you can always take the 10% penalty and get 90% back for yourself. \n\nI personally believe you can never have enough in TSP. You literally never know what will happen and there are options to still maximize that excess money down the road. Ultimately, having more money in your TSP will also extend how long you can leave your Roth IRA untouched, which is going to maximize those tax-free gains for you or your family (since you shouldn\u2019t be tapping this account until the very end anyway). And if you feel you have too much in your TSP, you could roll it over into your primary Roth IRA (or open a separate Roth IRA) and name your kid(s) as beneficiaries.\n\nIt\u2019s possible to never even touch your Roth IRA if you can live off your brokerage, pension, VA and TSP alone! And thanks to the Secure Act 2.0, Roth IRA\u2019s are now exempt from RMD\u2019s at age 72, so you don\u2019t have to make those mandatory/additional withdrawals at that point in retirement. If your kid(s) are the beneficiaries on your Roth IRA, they have 10 years to withdraw all of the unused money after your death, so theoretically the balance at your death should be able to double by the time they need to withdraw the money. Imagine passing your kid(s) your untouched or barely-touched Roth IRA\u2019s! \n\nCheck out r/coastFIRE. \n\nAnd here are some Retirement Calculators I like:\n\n\u2022https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator - quickly calculate compound interest, savings goals, and RMD\u2019s; has a handy \u201crange of return\u201d feature\n\n\n\u2022https://walletburst.com/tools/fire-calculator/ - detailed FIRE calculator \n\n\n\u2022https://walletburst.com/tools/coast-fire-calc/ - this is a super cool calculator for figuring out your Coast FIRE age, FIRE age, and annual net worth increase to see if you\u2019re on track for your goals \n\n\n\u2022https://www.cfiresim.com - this is a more advanced Coast FIRE calculator that takes lots of variables into consideration besides inflation, then runs scenarios to give you a 0-100% chance of successfully retiring in the given year you enter \n\n\n\u2022https://financialmentor.com/calculator/best-retirement-calculator - this is called the Ultimate Retirement Calculator. Lots of good features to try and estimate future retirement nest egg\n\n\n\u2022https://marketbeat.com/dividends/calculator - amazing dividend calculator\n\n\n\u2022https://www.nesteggly.com/retirement-calculator - another Ultimate Retirement Calculator (not as customizable) \n\n\n\u2022https://www.nesteggly.com/investment-withdrawal-calculator - simple calculator to estimate how long your nest egg will last\n\n\n\u2022https://www.nesteggly.com/fire-retirement-calculator - simple calculator to estimate FIRE status\n\n\n\u2022https://financialmentor.com/calculator - link to 80 different types of financial calculators (retirement, mortgage, savings, etc)\n\n\n\u2022https://livingwage.mit.edu/ - useful to see living wage and average annual salary based on number of dependents for every state \n\n\n\u2022https://www.calculatorsoup.com/calculators/financial/investment-inflation-calculator.php - Investment Inflation Calculator"
      },
      {
        "id": "muuun6x",
        "score": 10,
        "body": "Usual withdrawal rates I\u2019ve seen are 4%, so I would\u2019ve expected closer to 60k for TSP withdrawals. I just always used the 7% gains to approximate, so balance should double every 10 years, which would have you around 1.6 million at 60 (assuming you\u2019re 30 today)\n\nI would also consider how you\u2019re going to purchase a house in HCOL in retirement. As far as I know, investments won\u2019t count towards DTI"
      },
      {
        "id": "muv4x3o",
        "score": 7,
        "body": "Consider, instead of investing the difference in accounts for the kids, start to invest in a regular taxable brokerage account with that money instead. That will give you much more freedom with what you choose to do with that money and you won't have to wait until 59.5 to do it. You can still gift it to the kids if you choose to do so, but if not, it's yours to keep. A UTMA will make it the kid's money forever, and I'm personally not a fan of that inflexibility.\n\nThat's what we did. Once we had enough invested in retirement accounts that we could retire comfortably at 65 (no pension, separating) without ever contributing a single additional dollar, we cut our TSPs back to the match and started dumping money in our brokerage account at Fidelity. If we ever choose to retire early, that flexibility will be invaluable. We do still max our Roth IRAs because those contributions can be withdrawn tax and penalty free at any time in the future, if needed."
      },
      {
        "id": "muuqxow",
        "score": 6,
        "body": "I have spent countless nights thinking about those unexpected/worst case situations. If it happens, we can and will adapt. \n\nThe current place is where we plan to retire, HCOLA. No idea on how to price future hobbies, but current ones are semi-expensive...\n\nI double-checked the 2 calculators, all set to 6% gain and 3% inflation, I'll run them again tomorrow and see if I was wrong with fresh eyes. \n\nAge: 31 (+/-2)\nBalance: 200,000\nPay: 60k\nContributions/Match: 5%\n\nOutcome:\nAge: 41 (+/-)\nBalance: $380k-410k\n\nThen I input:\nAge 41 (+/-)\nBalance 380k\nContributions: 0\nRetirement age: 60\n\nOutcome:\nBalance ~$1.15M\n\nThanks the reply and food for thought!"
      },
      {
        "id": "muwvv0i",
        "score": 6,
        "body": "Good point, especially with the way our world is today. Thanks!"
      },
      {
        "id": "muuqjhb",
        "score": 5,
        "body": "If one of you gets a deployment, max your Roth contributions during that 6 months (entirely tax free), otherwise just the 5% is plenty.\n\nAside from the tax-advantage, the TSP doesn't really do a whole lot better than the S&P over time, regardless of the funds you choose.\n\n529s sound like a much better move (you're gonna be stuck paying for those kiddos one way or another anyway)  \n\n\nI looked up the qualified expenses out of curiosity:\n\n\\- Tuition and mandatory fees: These are the core expenses for enrollment.\n\n\\- Books and supplies: Required materials for classes.\n\n\\- Certain room and board: Housing and meal plans provided by the institution or at a reasonable cost for students living off-campus.\n\n\\- Special needs equipment: Necessary for students with disabilities.\n\n\\- Computers, software, and internet access: Essential for coursework.\n\n\\- Student loans: Principal and interest payments on qualified education loans.\n\n\\- Qualified apprenticeship program expenses: Fees, books, and supplies for registered apprenticeship programs."
      },
      {
        "id": "muwnenm",
        "score": 3,
        "body": "So there's 4 outcomes here based on 2x2 choices: retire / not retire from the military and invest / not invest more into retirement.\n\n**If you continue to invest 10% of gross compensation...**\n\nCase 1: Retire. You are over-funded in retirement, but can access your money in your 40s by simply rolling your TSP (hopefully you are doing Roth) into a Roth IRA, then withdrawing the contributions. Your gains are locked up until 59.5, but you'll probably still need that to supplement your pension(s).\n\nCase 2: Don't retire. In this case, your retirement is likely properly funded and you don't have to worry about things like catch-up contributions or cutting expenses dramatically. **Outcome always positive**.\n\n**If you don't invest 10% of gross compensation...**\n\nCase 3: Retire. In this case, no harm, no foul. You executed your plan as intended.\n\nCase 4: don't retire. In this case, you're up shit's creek to figure out how to fund your retirement in your 40s and 50s.\n\n**Outcome can be significantly negative**\n\nSo you should continue to invest. Perhaps less aggressively, but 5% of basic pay is too little. You can access funds in an over-funded retirement account significantly easier than you can make up a shortfall."
      },
      {
        "id": "muux3k0",
        "score": 3,
        "body": "74k is higher than anything I\u2019ve seen then. I estimated a higher return and for a lower withdraw rate\n\nDTI is debt to income. Don\u2019t quote me on the issues with it though, I\u2019ve just seen it mentioned on some of the FIRE posts. If a mortgage lender doesn\u2019t take into account your investments, you wouldn\u2019t qualify for very much"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1pzhhfw",
    "title": "Financial Azimuth Check - Approaching 20 years AD Service",
    "body": "Looking for feedback on how/if should change allocations.\n\nActive Duty O-5. Married with three kids (15, 13, and 6). 20 years of service next year (and upcoming PCS) and am likely to retire within the next 1\u20133 years. I will probably need to get another job after retiring, but maybe lower pay/stress. Don't know yet where we will live or what I will do. Just want to have more flexibility to spend more time with family.\n\nFinancial breakdown below (no debt/don't own any houses/own 1 car)\n\n**Tax-Advantaged**\n\n* **Roth TSP:** $275k\n   * Contributing **8% of monthly pay ($902.81)**\n   * Allocation: **90% C Fund / 5% S Fund / 5% I Fund**\n* **Roth IRA :** $361k\n   * **Maxing annually** ($583.66/month)\n   * Allocation: Mostly index funds\n* **Spouse Roth IRA:** $268k\n   * **Maxing annually** ($583.66/month)\n   * Allocation: Mostly index funds\n\n**Taxable**\n\n* **Brokerage Account 1:** $133k (\\~$500/month)\n   * Allocation: Mostly index funds\n* **Brokerage Account 2:** $5k\n\n**Kids / Education (may need to fund private school at our next post. I have some of my GI bill left as well)**\n\n* **Custodial Brokerage (15yo):** $33k\n* **Custodial Brokerage (13yo):** $4k\n* **529 (15yo):** $21k\u2014 not contributing\n* **529 (13yo):** $20k \u2014 not contributing",
    "flair": "Question",
    "score": 31,
    "comment_count": 23,
    "created_at": "2025-12-30T12:58:26+00:00",
    "top_comments": [
      {
        "id": "nwq428y",
        "score": 48,
        "body": "Age is mid to late 40's with 15-20 years to retirement. \n\nYou've got $900K in retirement funds. Left alone and assuming 7% returns, that money will double twice(ish) from 900 to 1.8 to $3.6M in today's dollars?\n\nSince you have 20 years to go there's nothing wrong with your allocation.\n\nThe $133K in taxable is your cushion as you figure out how to bridge from retirement funds to needed spending and other savings goals.\n\nJust me, but I think you should have less of an allocation question and more of a career transition planning question.\n\nLooks like you're doing great."
      },
      {
        "id": "nwqd4kk",
        "score": 14,
        "body": "Overall, you\u2019re in great shape for long term retirement from working in your 60s, and you\u2019re investing into good assets. Where I see concerns are in your short to medium term:\u00a0\n\n1. Post military retirement, you will likely get a house. This will involve a large down payment that may wipe out your brokerage accounts.\u00a0\n\n2.\u00a0\u00a0If you want to help your kids get through college debt free, you are not well positioned to do that. Each of your 529 accounts might cover one year of in-state tuition at a state university for one kid. Transferring GI Bill benefits helps, but cannot cover 3 kids for undergraduate tuition, and you have already used some of that benefit.\u00a0\n\nThe fact that both these needs are likely to come up within a few years of each other may indicate a financial requirement gap. There are plenty of ways around this, if you find the trade-offs acceptable. VA loans don\u2019t need down payments, though no down payment means more debt. Kids can go to community college for their first two years and /or use the military to pay for college. You can also seek higher-paying jobs to cover these costs, but that could mean more stress.\n\nOverall, though, you really are in good financial shape. Where you go from here is more a matter of managing priorities than addressing mistakes or oversights."
      },
      {
        "id": "nwq9eeu",
        "score": 12,
        "body": "Thanks. Appreciate it. 20 years came quickly."
      },
      {
        "id": "nwq8cjv",
        "score": 6,
        "body": "I have a custodial and 529 plans for kids. I plan to use the 529s for either private high school (if allowed) or college. Very interesting point on the 529 in my name. I don't know whether any of them will actually need them. I could see myself using it for my next career. Will have to look into this, thanks."
      },
      {
        "id": "nwq5fpt",
        "score": 5,
        "body": "Have you determined your monthly expenses post retirement vs your expected retirement check? Will your spouse be working or will it be on you to cover the difference? Do you plan on buying into SBP? (Mostly hypothetical questions if you haven\u2019t discussed yet). \n\nPersonally I\u2019d recommend paying a fee-only fiduciary financial advisor to do a real azimuth check for your situation. We are now <2 years out from retirement and we did one at ~5 years out for a temp check, and will do one final session 6-9 months before retirement. It was extremely helpful to have visualizations of our various income streams and identify when we pull from which pots of money in the future. You can find one via the XY Planning Network then filter by Profession (military/vet). Of course also happy to share my POC. \n\nLastly, how\u2019s your life insurance situation looking? Recommend locking up 30 year term policies for you and your wife, you in particular before retirement and VA claim processing. We used an individual broker to shop the best rates."
      },
      {
        "id": "nwq2ugp",
        "score": 5,
        "body": "I don\u2019t have anything to contribute but a question since I\u2019m in a similar situation. \n\nWhy are u using a brokerage account for your kids education? If it\u2019s for private school 529s allow k-12 usage and Vanguard has some pretty nice variety of index\u2019s.\n\nAlso, speak to your financial professional but might be best having a 529 on you since the balance isn\u2019t as heavy used for financial aid. Online it says it\u2019s 5% for a parent or 20% for the child. a financial professional can confirm that or not."
      },
      {
        "id": "nwq2z7t",
        "score": 4,
        "body": "What\u2019s your marginal tax rate right now? \n\nDoes your wife work/have a career? \n\nDoes she want to after you leave service?\n\nWhat are your Career goals after service?\n\nDo you have additional family obligations (parents/siblings needing care?)\n\nWhere do you want your kids to go to high school/college? \n\nHow\u2019s a VA claim looking?"
      },
      {
        "id": "nwqaipj",
        "score": 4,
        "body": "ADSO for a PCS is just one year and retirement packets can be submitted at 24 months with the current ETP extension."
      },
      {
        "id": "nwqfqhv",
        "score": 4,
        "body": "Idk if you\u2019re familiar with the new law to also allow $35k be transferred out to a Roth Tax free if open for I believe 15 years. But it still follows the max contribution limit of $7,500 for 2026. \n\nAnd also don\u2019t forget Roth Contributions can be withdrawn not earnings. Not sure if that helps things or complicates them. Your situation maybe different so don\u2019t take my word talk to a pro, I only pretend to play one on Reddit."
      },
      {
        "id": "nwqi1bb",
        "score": 3,
        "body": "I\u2019m in a similar situation, 34 TIS, O5 (12 years prior enlisted time). It\u2019s my understanding that once you submit your retirement you won\u2019t PCS again. But your branch can assist you with the location and transition timing.\n\nHighly recommend community colleges for your kids while living at home for the first few years and only taking the GI Bill as needed. We did this and it created a very manageable situation for our son and his employer is paying off the remainder of his student loan."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1mz2hz2",
    "title": "Anybody use AMEX high yield savings?",
    "body": "Have way too much money just sitting in my normal share savings (NFCU), looking to put it somewhere where it can at least grow Enough to minimize the effect of inflation. \n\nThinking about using navy fed just for checking and then having a savings in AMEX? ",
    "flair": "Question",
    "score": 31,
    "comment_count": 57,
    "created_at": "2025-08-24T17:55:16+00:00",
    "top_comments": [
      {
        "id": "nagatij",
        "score": 87,
        "body": "I do. It's easy to use and transfer back and forth from USAA. Great for emergency funds."
      },
      {
        "id": "nag87kc",
        "score": 59,
        "body": "I use Amex HYSA. I choose to support them since it's a great company over fighting for 0.2% somewhere else."
      },
      {
        "id": "nag8g9o",
        "score": 29,
        "body": "HYSAs are a dime a dozen \n\nI've stuck with Ally the last few years \n\nDepending on how much you have in savings it's not worth switching to the higher rates \n\nIf you have $50k sitting in an account at 3.4% and you want to switch to someone with 3.5% it's a difference of **$50** for the year"
      },
      {
        "id": "naihyht",
        "score": 29,
        "body": "Great CS, waive fees for military more often than most others, competitive rates, easy interface, really no complaints all around."
      },
      {
        "id": "nagaxwb",
        "score": 21,
        "body": "I've used Amex HYSA for over 7 years now. It's pretty straightforward. I would recommend them."
      },
      {
        "id": "nahmppp",
        "score": 15,
        "body": "Neither of what I'm about to recommend are technicaly HYSAs but Wealthfront or a Fidelity CMA are both solid.\n\nWealthfront is 4% while Fidelity CMA is ~4.3% both compounding monthly.\n\nAMEX HYSA looks good on paper because it compounds daily but the reality is that you end up losing in the long run compared to the two mentioned above.\n\nWealthfront w/$5k after 10 years is $7,454.16\nAMEX HYSA w/$5k after 10 years is $7,095.22\n\nOh and Wealthfront has instant transfer with NFCU. Pulled 30k out of WF and it was in my NFCU within 2 minutes to use as a down payment on a new vehicle.\n\nRegardless, something is better than nothing so as long as you're at least getting 3%+"
      },
      {
        "id": "nageoor",
        "score": 12,
        "body": "But he doesn't have it in any high yield savings. NFCU savings accounts are .25%. Basically just losing money to inflation at that point."
      },
      {
        "id": "naij2jf",
        "score": 8,
        "body": "Free same day wire transfers. You can\u2019t get that kind of service imo."
      },
      {
        "id": "nag8lh2",
        "score": 7,
        "body": "I use Fidelity cash management for the same apr but it\u2019s easier for me since I use Fidelity for my 401k and brokerage"
      },
      {
        "id": "nagb75z",
        "score": 6,
        "body": "I use an online bank that gives like 4.5%.\n\nWebster bank. I just googled high rates and promos years ago, and that\u2019s what came up. Been happy ever since. Might be better promos now somewhere else if you shop around"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1me0xyk",
    "title": "Start Here: Military Money 101, Prime Directive, Flow Chart, Updates Monthly",
    "body": "Welcome to the getting started thread for military money. This will cover 90% of what you need to know to be successful with your military paycheck and build wealth in the military.\n\nSome of the most frequent questions in on this subreddit goes:\n\n* **\"I have $X, what should I do with it?\"**\u00a0or\n* **\"How should I handle my debt/finances/money?\"**\n\nMilitary Personal Finance and Investing Flow Chart: [https://imgur.com/a/akrEcUS](https://imgur.com/a/akrEcUS)\n\n# Step 1: Budget and reduce expenses, set realistic goals\n\nFundamental to a sound financial footing is knowing where your money is going. Budgeting helps you see your sources of income less your expenses. You should minimize your required expenses to the extent practical. Housing costs, utilities, and basic sustenance are harder to eliminate than entertainment, eating out, or clothing expenses.\n\nThere are many great apps available to discover what you're spending money on and where there are opportunities to save money. Monarch Money, YNAB, Copilot Money, EveryDollar are just a few of the apps available.\n\nOnce your budget is figured out, you need to figure out what your goals are. Financial independence? Retire early? Military retirement? Buy a house? Save for a car?\n\nSetting SMART goals - Specific, Measurable, Achievable, Relevant, and Timely goals can mean the difference between financial success and failure. For example, you might want to finish your first enlistment with a $100,000 net worth or achieve early retirement after 20 years of service. These are SMART goals.\n\n# Step 2: Build an emergency fund\n\nAn emergency fund should be a relatively liquid sum of money that you don't touch unless something unexpected comes up. Unexpected travel, essential appliance replacement, and cars breaking down are all real world examples of emergency funds in action.\n\nIf you need to draw from your emergency fund at any time, your first priority as soon as you get back on your feet should be to replenish it. Treat your emergency fund right and it will return the favor.\n\nStart with a $1,000 emergency fund. Eventually build it up to 3-6 months of expenses or a few of months of expenses plus\n\n**How should I size my emergency fund?**\n\nFor most people, 3 to 6 months of expenses is good. Or maybe you want to cover a few months of expenses, plus a roundtrip airfare for you and your family to go back to your home stateside.\n\n**What if I have credit card debt?**\n\nCredit cards generally have very high interest rates (typically 15-25% APR) and that is a pretty big deal. If this applies to you, you should prioritize paying down the debt first.\n\nA smaller emergency fund of $1,000 (or 1 month of expenses) is temporarily acceptable while paying off credit card debt or other debts with interest rates above 10%.\n\n**What kind of account should I hold my emergency fund in?**\n\nA checking account, savings account, or a high yield savings account (HYSA). Something FDIC insured and accessed in a few days.\n\n# Step 3: 5% Into the Thrift Savings Plan\n\nThe Thrift Savings Plan (TSP) is the military and government's version of a 401(k) retirement savings plan. All servicemembers enlisting since 2018 are covered by the Blended Retirement System (BRS). The BRS has 3 primary components to help servicemembers save for retirement:\n\n1. 5% matching contribution to the TSP\n2. Continuation pay bonus between the 8th and 12th year of service (depends on branch)\n3. Military pension. A 2% mutliplier is used for each year of service. So if you retire after 20 years of active duty service, you'll earn an inflation adjusted, lifetime pension of 40% of your base pay. (20 years \\* 2 = 40%)\n\nAfter 60 days of service, the Department of Defense (DOD) will automatically contribute 1% of your base pay to the Traditional TSP.\n\nStarting in the 25th month of service, your contributions are matched, up to 5%. So if you contribute 5%, the DOD will contribute 5%. This is a risk free, 100% return on your contributed funds.\n\nThe default investment for anyone in the BRS is a Lifecycle fund with their birth year + 65. For example, if you were born in 2005, you'll be placed in the Lifecycle 2070 Fund.\n\nThe Lifecycle Funds are a mix of the 5 TSP Funds, designed by professional fund managers.\n\nThe 5 TSP Funds are:\n\n* C Fund - Tracks S&P 500, made up of the 500 largest companies in America. You can use the ETF SPY or VOO to track it.\n* S Fund - Tracks Dow Completion index, basically all the mid- and small- capitalization companies in America outside of the S&P500. ETF equivalent VXF.\n* I Fund - International stocks. MSCI ACWI IMI ex USA ex China ex Hong Kong Index. 5,500 companies in this index. representing 90% of the investable world market cap outside the US. Similar to ETF VXUS but without Chinese or Hong Kong stocks.\n* F Fund - Fixed income. Corporate bonds. Use ETF AGG to see performance.\n* G Fund - Lowest risk, lowest long term return fund. The G Fund invests in a special\u00a0non-marketable\u00a0treasury security issued specifically for the\u00a0TSP\u00a0by the U.S. government. This fund is the only one in the\u00a0TSP\u00a0that guarantees the return of the investor\u2019s principal. No comparable ETF.\n\n# Step 4: Pay down high interest debts\n\nOnce you're taking advantage of the 5% BRS TSP match, you should use your extra money to pay down your high interest debt (e.g., debts much over 4% interest rate).\n\nIn all cases, you should make the minimum payments on all of your debts before paying down specific debts more quickly.\n\nThere are two main methods of paying down debt:\n\n* With the\u00a0**avalanche**\u00a0method, debts are paid down in order of interest rate, starting with the debt that carries the highest interest rate. This is the financially optimal method of paying down debt, and you will pay less money overall compared to the snowball method.\n* With the\u00a0**snowball**\u00a0method, popularized by Dave Ramsey, debts are paid down in order of balance size, starting with the smallest. Paying off small debts first may give you a psychological boost and improve one's cash flow situation, as paid off debts free up minimum payments. The downside is that larger loans (that may be at higher interest rates) are left untouched for longer, costing more in the long run.\n\nAs an example, Debtor Dan has the following situation:\n\n* Loan A: $1,100 with a minimum payment of $100/month, 5% interest\n* Loan B: $3,300 with a minimum payment of $300/month, 10% interest\n* Sudden windfall: $2,000\n\nDan needs to first pay $100 + $300 = $400 to make the minimum payments on loans A and B so the payments are recorded as \"on time.\" The extra $1,600 can either go towards Loan A (smallest balance, snowball method), eliminating it with $600 left to go towards Loan B, or Loan B entirely (highest interest rate, avalanche method).\n\nWhat's the best method?\u00a0\u00a0tends to favor the avalanche method, but do not underestimate the psychological side of debt payments. If you think that the psychological boost from paying off a smaller debt sooner will help you stay the course, do it! You can always switch things up later. The important thing is to start paying your debts as soon as you can, and to keep paying them until they're gone. You can use\u00a0[unbury.me](http://unbury.me/)\u00a0to help you get an idea of how long each method will take, and how much interest you'll be paying overall.\n\n**Should I be in a hurry to pay off lower interest loans? What rate is \"low\" enough to where I should just pay the minimum?**\n\nDepending on your attitude towards debt, you may want to stop paying more than the minimum payment on loans with low interest rates once you have paid all other loans above that threshold. A common argument is that the long-term return from investments in the stock market will likely exceed the interest rate from a low-interest loan. While this has been true in the past, keep in mind that paying down a loan is a guaranteed return at the loan's interest rate. Stock performance is anything but guaranteed. The rough consensus is that loans above 4% interest should be paid off early in the debt reduction phase, while anything under that can be stretched out.\n\n# Step 5: Max out Retirement Accounts - Roth IRA and Roth TSP\n\nThe next step is to contribute to a Roth IRA for the current tax year. You can also contribute for the previous tax year if it's between January 1st and April 15th. See\u00a0[the IRA wiki](http://www.reddit.com/r/personalfinance/wiki/iras)\u00a0for more information on IRAs.\n\nRoth IRA and Roth TSP contribution limits are different and do not cross over. You can contribute the maximum out your Roth IRA and your Roth TSP. Matching contributions do not count against your personal TSP contribution limit.\n\n* [Roth and Traditional IRA limits on IRS.gov](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-ira-contribution-limits)\n* [Roth and Traditional TSP limits on TSP.gov](https://www.tsp.gov/making-contributions/contribution-limits/)\n\nThe most often recommended places to open a Roth IRA are at Vanguard, Fidelity, or Schwab. Most banks offer substandard Roth IRA products and you should not open Roth IRA accounts there.\n\n**Should I do Roth or Traditional?**\n\nRead\u00a0[Roth or Traditional](https://www.reddit.com/r/personalfinance/wiki/rothortraditional).\n\nFor most servicemembers (O-3 and below), **you'll be better off contributing to the Roth IRA**, since military pay is so low taxed. Much of our military pay is untaxable allowances, such as Basic Allowance for Housing (BAH), Overseas Housing Allowance (OHA), and Basic Allowance for Sustenance (BAS).\n\n**Why contribute to an IRA if I have the TSP?**\n\nRoth IRA's have access to low cost investments similar to what you'll find in the TSP. However, you can always withdraw Roth IRA\u00a0*contributions*\u00a0at any time, tax and penalty free.\n\nAfter you've fully funded your Roth IRA, you can look at maxing out your Roth TSP.\n\nBefore saving for other goals, you should save at least 15% and up to 20% of your gross income for retirement. If you are\u00a0[behind on retirement savings](https://www.fidelity.com/viewpoints/retirement/how-much-money-do-i-need-to-retire), you should try to save more than 15% if you can. If you can't save 15%, start with 10% or any other amount until you are able to save more.\n\n**Where should I open my Roth IRA?**\n\nVanguard, Fidelity, or Schwab. Read up about the Bogleheads 3 Fund Portfolio before selecting an investment option.\n\n# Step 6: Save for other goals\n\nMilitary servicemembers and spouses covered by TriCare are\u00a0**not**\u00a0eligible for Health Savings Accounts (HSA0.\n\n* If you wish to save for college for your kids, yourself, or other relatives, consider a\u00a0[529 fund in your state](http://www.clark.com/clarks-529-plan-guide).\n* Save for more immediate goals. Common examples include saving for down payments for homes, saving for vehicles, paying down low interest loans ahead of schedule, and vacation funds.\n* Save more so you can potentially retire early (also see \"advanced methods\", below), only using taxable accounts after maxing out tax-advantaged options.\n* Make an impact through giving. One of the rewards of practicing a sound financial lifestyle is that giving becomes easier. If you're on top of your health care costs, future education costs, and you've made it to this step, you can help\u00a0[make a difference for others by giving](https://www.reddit.com/r/personalfinance/wiki/charity). If you can't afford to make monetary donations, there are other ways to give.\n* Maybe you're interested in financial independence or retiring early, also known as FIRE? There are many resources out there on military financial independence and early retirement.\n\nThe time frame for these goals will dictate what kind of account you save in. For short-term goals (under 3-5 years), you'll want to use an FDIC-insured savings account, CDs, or I Bonds. If your time horizon is longer or you can afford to adjust your plans, you might consider something riskier like a balanced index fund or a three-fund portfolio (both are a mix of stocks and bonds). The best savings or investment vehicle will vary depending on time frame and risk tolerance.\n\nKeep in mind that (especially for a young person) the more time your money has to grow, the more powerful the effects of compounding will be on your savings. If the goal is early retirement (even before the age of 59\u00bd), you should definitely maximize the use of any available tax-advantaged accounts (IRA, 401(k) plans, HSA accounts, etc.) before using a taxable account because there are\u00a0[ways to get money out of tax-advantaged accounts before 59\u00bd without penalty](https://www.reddit.com/r/personalfinance/comments/434ey1/psa_retirement_funds_are_not_locked_up_until_age/).\n\nIf you are using a taxable account for any goal, you'll want to have a decent grasp on\u00a0[asset allocation in multiple accounts](http://www.bogleheads.org/wiki/Asset_allocation_in_multiple_accounts)\u00a0and\u00a0[tax-efficient fund placement](http://www.bogleheads.org/wiki/Principles_of_tax-efficient_fund_placement).\n\n# Military State Taxes\n\nYour\u00a0**home of record**\u00a0is the place you enlisted or commissioned from. This cannot be changed unless there was an error.\n\n**State of legal residence**\u00a0is the state that you claim as your residence. If you only have military income, you will pay state income tax only to this state.\n\nYou can establish residency several ways:\n\n* Registering to vote in that state\n* Obtaining a driver\u2019s license in that state\n* Titling and registering your vehicle in that state\n* Drafting a Last Will and Testament naming that state as your domicile\n* Purchasing residential property in that state\n* Changing your military and finance records to reflect residency in that state.\n\nThe simplest way to establish residency is to PCS to that state and establish residency while you are a resident.\n\nState with no income tax include: Alaska, Florida, Nevada, South Dakota, Tennessee, Texas, Washington, and Wyoming. Many other states have no tax for military servicemembers stationed outside the state.\n\nSimply engaging in one of the above acts alone will not likely render you taxable by a state; however, the more points of contact you make with a state increases your chances of becoming a taxpayer to that state. It is important to concentrate the majority of your points of contact in the one state where you intend to pay state taxes; otherwise, you may find yourself owing taxes to more than one state as a part-year resident.\n\nSource:\u00a0[Fort Knox Legal Assistance Office](https://home.army.mil/knox/application/files/5915/6623/5548/Legal_Residency.pdf)\n\n# Military Spouse Residency Relief Act\n\nThanks to the Military Spouse Residency Relief Act, Veterans Auto and Education Improvement Act of 2022, and Servicemembers Civil Relief Act:\n\n(A) The residence or domicile of the servicemember.\u201c\n\n(B) The residence or domicile of the spouse.\n\n\u201c(C) The permanent duty station of the servicemember.\u201d\n\nMilitary spouses and military servicemembers can pick 1 of 3 options for their state of legal residence:\n\n(A) The residence or domicile of the servicemember.\n\n(B) The residence or domicile of the spouse.\n\n(C) The permanent duty station of the servicemember.\n\nSo either match the servicemember, keep your old state, or change to the current state you're in.\n\n# Military Bonuses\n\nMilitary bonuses have federal income taxes withheld automatically at 22%. You may have state taxes withheld as well. Because your marginal tax rate is often much lower than this, you will receive a large portion of that withheld tax back when you file your tax return the following year.\n\nIf you don't know what to do with a military bonus, directing some of it to your Roth TSP is a great place to park it.\n\nAfter reading all that, go ahead with any other questions you have about getting started with your military money.",
    "flair": null,
    "score": 31,
    "comment_count": 6,
    "created_at": "2025-07-31T13:01:04+00:00",
    "top_comments": [
      {
        "id": "n670ddp",
        "score": 5,
        "body": "USAA and Navy Fed are fine, but using something else like SOFI, Ally, Capitol One, etc is probably better. USAA (not sure about Navy Fed) does have a true HYSA. Somewhere like SOFI gets you a checking and savings where the savings is already a HYSA (as long as you use the checking for direct deposit). And the vaults feature to \"break\" it up into multiple accounts is nice"
      },
      {
        "id": "n7k3qsw",
        "score": 2,
        "body": "Hi!\nMy spouse is a Lt. Commander w/20 years service making $140,000 before taxes ( not including bonuses or anything else as I wanted to work up the plan based solely on her salary). And while she\u2019s excels at so many things, investing in the TSP, Roth IRA, and/or an S&P 500 isn\u2019t one of them. Lol. So. I\u2019ve been doing my research and we finally have a plan going but I\u2019m comPletely open to advice on exactly how/how much and in what order we should do these things to maximize - considering she wants to put on XO then CO and then retire and go into another field/career but with a lot less stress. Ha. So maybe serving another 10 yrs and she\u2019ll be the big 50 then. \ud83e\udd70. Currently there\u2019s about 12 grand in savings, just paid off a huge chunk of high interest debt with about 40 grand left to get rid of. \nI want to get us in the best possible position so she can relax a bit before deciding on her next career and then be financially set when she decides to fully retire. \nAll informed advice is welcome! Thank you in advance!! And you are appreciated."
      },
      {
        "id": "n65p2gp",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1hqdbse/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "n80w3x8",
        "score": 1,
        "body": "I have 15k at APR of 8.99 percent. Monthly payments of 400. I have 16k in savings. I could pay off my loan but only have 1k left in savings which wouldn't be ideal. \n\nI take out a CD secured loan of 15k at a rate of 6.25 percent. My monthly payments are now only 300 dollars. I only have 1k in savings but I have not only lowered my monthly payment and interest rate, but here is the real kicker, when I make a payment, a couple days later, the 300 bucks shows up in my savings account and my principal has gone down. Now, all I have to do is not spend that 300 bucks, use it over and over again to lower my loan amount. It's not for everyone but it is a tool I have used to get out of a high interest loan until a lower one. It shows payments and builds credit."
      },
      {
        "id": "n6kktff",
        "score": 0,
        "body": "Don't know if many people know that Navy Fed has what's called a certificate pledged loan. \n\nA Safe, Smart Way to Borrow\r\nThe Program\r\nBorrow your own money. Use the principal in your Navy Federal certificate(s) as collateral on a low-interest-rate loan. The loan\u2019s Annual Percentage Rate (APR) is just two percentage points higher than the certificate rate, and the certificate continues to earn dividends at the \r\nrate at which it was purchased.\n\r\nEligibility\r\nYou must be 18 years or older and be the \r\nowner or joint owner of the certificate.\r\nThe Navy Federal certificates that can \r\nbe pledged as collateral are:\r\n3-, 6-, 9-, 12-, 18- and 24-month \r\nshort-term certificates\r\n3-, 4-, 5-, 6- and 7-year long-term certificates$1,000, $10,000, $20,000, $50,000 and $100,000 minimum certificates\n\r\nAccounts not eligible are:\r\nthree-year Variable Rate Certificates\r\nEasyStartSM Certificates\r\nCustom Club\u00ae Accounts\r\ncustodial accounts\r\nall IRA/ESA accounts\r\nThere\u2019s a maximum of one loan\r\nper certificate.\r\nReceiving the Funds\r\nYou can choose to have the funds:\r\ndeposited into your Navy Federal \r\nsavings, checking or Money Market \r\nSavings Account (MMSA)\r\ndisbursed to you at a Navy Federal \r\nbranch mailed to you as a draft\r\nbank-wired to another financial institution\r\nFriends and Family\r\nYou can pledge the funds in your own \r\ncertificate and co-sign the loan for a friend or family member who\u2019s a Navy Federal member so that they can qualify for a low-interest-rate loan. \nYou must provide written consent, which \r\ncan be faxed to 703-206-4250.\r\nPaying Your Loan\r\nYou can choose to make payments through:\r\nDirect Deposit\r\nautomatic transfer from checking \r\nor savings\r\nNavy Federal Online\u00ae\r\na Navy Federal ATM or branch mail\r\nDividends earned on your certificates can be used toward paying your loan. There\u2019s no penalty for paying off your loan early."
      },
      {
        "id": "n80khgx",
        "score": 0,
        "body": "I don't understand this program at all. You borrow against your own cash 2% points higher than the rate you're earning on the CDs?\n\n\nThis seems designed to hurt people who are bad at math."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1jgttqs",
    "title": "What\u2019s your rank and what percentage of your income are you saving per month?",
    "body": "E4 with 5 years TIS. My goal is to save 40%, but trending closer to 35%. \n\nCurious to see what others are able to save. ",
    "flair": "Question",
    "score": 32,
    "comment_count": 74,
    "created_at": "2025-03-21T22:47:25+00:00",
    "top_comments": [
      {
        "id": "mj24c8m",
        "score": 155,
        "body": "Just a reminder for those who see this: This sub definitely skews toward the high savers. \n\nIf you are meeting your goals, you're doing great, even if your percentage is lower than some others. \n\nIf you are not meeting your goals but you're working on it, keep it up! You're on the right track! \n\nIf you don't know what your goals are or how much you need to be saving for them, that's something to work on."
      },
      {
        "id": "mj28280",
        "score": 69,
        "body": "Just to go against the grain here, E6, I'd say like 2k/month is \"saved\" but I also go on international vacations and cruises with my wife 3 or 4 times a year and spend it, or spend it on my project car, or concerts, or something else, it gets spent is the point.  We have a mortgage and no other debt, not even car payments, but we have very little \"cash savings\" because we are enjoying life to the fullest."
      },
      {
        "id": "mj2bef2",
        "score": 53,
        "body": "Comparison is the thief of joy and a disclaimer like this should be on every finance post."
      },
      {
        "id": "mj23meb",
        "score": 28,
        "body": "I\u2019m an E4 and my wife has the same income as me, we have 2 kids, no debt, and we save around 50% total income (including BAH & BAS) of our income every month and that includes our TSPs, Roth IRAs, and regular savings, but I will say when we were not married, stationed separately, and had no kids I was def able to save a higher %, (but not a higher dollar amount) due to just having no expenses and being in the dorms."
      },
      {
        "id": "mj2bs1s",
        "score": 24,
        "body": "O-4, 40%. Having a spouse that works helps a lot"
      },
      {
        "id": "mj24xqt",
        "score": 21,
        "body": "I'm gonna need you to get the rest of the E4s on board man... Well done!"
      },
      {
        "id": "mj2otq2",
        "score": 18,
        "body": "What's the point in money if you're not spending it?"
      },
      {
        "id": "mj2grcp",
        "score": 15,
        "body": "O3, 60%. Been 50-70% since I was an E-3."
      },
      {
        "id": "mj2drwr",
        "score": 12,
        "body": "I\u2019d say it\u2019s more of us being lucky and having a good income (a lot of military spouses are 1 income families and it\u2019s pretty rough to save). We are in a pretty HCOLA and combined income is $135k. I think having no debt is important (majority of people everywhere in the U.S. have huge car payments and even have high interest CC debt) and saving about 65-70k a year I would say we still live a very good life we go on small trips pretty often as well. Grocery shop at the commissary tax free and don\u2019t eat out 3-4 times a week for lunch/dinner."
      },
      {
        "id": "mj2b4jd",
        "score": 11,
        "body": "O-4. Not sure the exact amount, but I'd say around 35%. I max traditional TSP and Roth, then put a decent amount into an HYSA."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rl5ig7",
    "title": "Robinhood announces Platinum Card",
    "body": "https://robinhood.com/us/en/creditcard/platinum/\n\nHey guys, Robinhood just announced a juicy new credit card. Their cards are serviced by Coastal Community Bank. Has anyone gotten credit cards with them, and do they waive annual fees for AD?",
    "flair": null,
    "score": 14,
    "comment_count": 17,
    "created_at": "2026-03-05T02:33:30+00:00",
    "top_comments": [
      {
        "id": "o8pp50b",
        "score": 25,
        "body": "\\> The actual platinum card \\*\n\n\\* It's only a coating, and the coating isn't even pure platinum\n\nedit: Seems pretty useless guys  \n*$250 Annual DoorDash Credits*: Once you activate DashPass through your Platinum Card, you will receive up to three (3) $10 off discounts each January and up to two (2) $10 off discounts in every other calendar month. Apply up to one discount per qualifying delivery order with a minimum subtotal of $50, excluding fees and taxes.\n\nOura Membership:  \nTo receive the benefit, Cardholder must opt in via the Robinhood Banking App and within six (6) months, purchase Oura Ring with a pre-paid annual Oura Membership  \n\\- so can't be combined with the Amex oura credit\n\n$200 Health Wearables Statement Credit:  \n\\- maybe this will cover the ring? Or an apple watch\n\nEvery credit is so chopped up and then put against minimum spend conditions that it's not saving anyone money. The stuff that isn't chopped like the health benefits are not particularly useful for someone with tricare and are in a grey area if you are using it to get prescriptions youre PCM won't give you especially if you're hiding it from them\n\n[https://api.robinhood.com/creditcard/legal/platinum-benefits-overview](https://api.robinhood.com/creditcard/legal/platinum-benefits-overview)"
      },
      {
        "id": "o8prjky",
        "score": 12,
        "body": "I rolled my eyes at the DoorDash one. Even with the sapphire reserve it's become more trouble than it's worth. That's with only a $10 spend minimum "
      },
      {
        "id": "o8pokxs",
        "score": 4,
        "body": "Yes"
      },
      {
        "id": "o8pxug7",
        "score": 3,
        "body": "Just got the gold card after finally coming off the waitlist yesterday \ud83e\udee0"
      },
      {
        "id": "o8qqi8d",
        "score": 3,
        "body": "Robinhood doesn't waive fees for their gold card (i have one and it's my daily driver when I'm not working on SUBs). Doubt they would waive this new one."
      },
      {
        "id": "o8poj62",
        "score": 3,
        "body": "Bilt is waiving the annual fee?"
      },
      {
        "id": "o8ps2ke",
        "score": 3,
        "body": "Yup I got mine waived! Takes an email though."
      },
      {
        "id": "o8puc1f",
        "score": 3,
        "body": "Palladium"
      },
      {
        "id": "o8rq50j",
        "score": 2,
        "body": "You have to sign up for their robinhood gold which is a fee for their platform not card. Getting the card is a benefit of their gold tier. "
      },
      {
        "id": "o8pua8y",
        "score": 2,
        "body": "Which bilt card?"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rl35gm",
    "title": "Is DFAS/Treasury violating my rights?",
    "body": "I was unknowingly overpaid $500 after separating from the Navy. They sent a letter saying they\u2019re offsetting my tax return. (Completely fair) but simultaneously sent my account to the treasury for garnishment essentially increasing my already paid debt by 20% for fees and collection that came way of an unnecessary garnishment. 20% of $500 isn\u2019t something to blow up over but it still matters the way they\u2019re attempting to take this money and from what I\u2019ve seen they\u2019re doing this to countless other veterans. Not only that they demand adp collect indefinitely until they say not to regardless of if the lien was met. So far it\u2019s $500/$500 DFAS $700/$600 Treasury. They also demand that payment is sent to them via usps check. Convince me my 5th amendment or 4th isn\u2019t being infringed.",
    "flair": null,
    "score": 0,
    "comment_count": 21,
    "created_at": "2026-03-05T00:47:22+00:00",
    "top_comments": [
      {
        "id": "o8pd63j",
        "score": 10,
        "body": "There is absolutely zero here on your 4/5th amendment. I would specifically love to hear your 5th amendment argument.\n\nWhen were you notified of this debt? It seems like a while ago, and they sent it for garnishment. In the meantime, you filed taxes and they took it from your refund.\n\nDone. Totally legal and, likely, months/years overdue on your part."
      },
      {
        "id": "o8p4m7y",
        "score": 9,
        "body": "What unlawful search occurred, and how were you denied the right to not incriminate yourself."
      },
      {
        "id": "o8p48hq",
        "score": 9,
        "body": "what are you talking about man?  You were overpaid(you should have kept track of it and notify them).  What 4th/5th amendment are you talking about?..."
      },
      {
        "id": "o8p7f0c",
        "score": 9,
        "body": "No I\u2019m saying that you sound insane and that are ignoring that they audit your entire pay record when you separate and likely found an overpaid travel voucher in addition to your overpayment at separation. "
      },
      {
        "id": "o8p6j5z",
        "score": 8,
        "body": "It\u2019s not an unlawful seizure though. "
      },
      {
        "id": "o8qxg6g",
        "score": 7,
        "body": "Read the DoDFMR, volume 16. \n\nThere is almost 0 chance that it went from them finding an overpayment to tax offset without any other attempts at contact. Primarily because that\u2019s handled by a different office (if I recall correctly, the tax/pension offset is a third office and would be the third or fourth notice of indebtedness?) \n\nThere is other useful information in that regulation for you to reference too. \n\nBut, if the amount was offset by taxes and they\u2019re still doing salary offset, it might be wise to contact them. It\u2019s possible that it\u2019s an error where they don\u2019t see that it was rectified by tax offset or an inaccurate number was entered and it still shows balance due. \n\nAs far as whether this is a violation of any rights? We sign a lot of documents when we joined the military. I would place a wager that we signed something suggesting that we effectively allowed the government to do this in such a situation. I\u2019d further wager that in DoDFMR volume 16 the references would have something that gives them the authority."
      },
      {
        "id": "o8p4q3c",
        "score": 6,
        "body": "These are standard procedures and you\u2019ve likely passed on several other opportunities/ways of clearing the debt, highly unlikely your rights are being violated. More likely is this is codified in law or government policy. I\u2019d pick one means of paying the debt and complete that. Once cleared, it should cancel the rest of the collection attempts once it goes through."
      },
      {
        "id": "o8p70fb",
        "score": 5,
        "body": "Ok guy"
      },
      {
        "id": "o8rm16t",
        "score": 3,
        "body": "Navy sure dodged a bullet..."
      },
      {
        "id": "o8ph03b",
        "score": 3,
        "body": "Your job is to ensure you are getting the correct amount(over or under) and to report to DFAS if there\u2019s a mistake.  You were hoping they would never find out but it didn\u2019t work out like you had hoped for\u2026"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rkcgyn",
    "title": "Advice on car insurance?",
    "body": "I\u2019m a E-3 in tech school wanting to get a mustang,\n\nYes I know I don\u2019t need a car, however I\u2019m only gonna be young once.\n\nI don\u2019t have an exact car but around a 2014 mustang gt with 100k miles for $16-$20k\n\nI got $5k for a down payment and navy fed offered to loan me $15k at 5.79% APR with a monthly payment of $456\n\nI\u2019m trying to get my insurance to like 200 or just as low as possible. What tips do you have? \n\nI know of the gps tracker, good student discount, and maybe keeping the car on base will get it lower? I\u2019m open to doing any courses or anythin to get it lower. Do I need full coverage o",
    "flair": "Question",
    "score": 0,
    "comment_count": 16,
    "created_at": "2026-03-04T04:59:38+00:00",
    "top_comments": [
      {
        "id": "o8jlif7",
        "score": 22,
        "body": "Don\u2019t do it kid"
      },
      {
        "id": "o8kzkh5",
        "score": 10,
        "body": "This is a shit post, right?"
      },
      {
        "id": "o8jr7dy",
        "score": 9,
        "body": "Yeah this has to be bait lol\n\nIf not listen to the other guy"
      },
      {
        "id": "o8kgd8l",
        "score": 6,
        "body": "I love the justification of I\u2019m only young once so I have to get a mustang. If you think being young means driving a car that between gas, payments, and insurance will be around 1/3 of your monthly take home is smart you need to reconsider. You\u2019re going to be the \u201ccool kid\u201d with a car that\u2019s asking their friends to buy your chipotle because you\u2019re going to be so broke but hey at least your car is loud.\n\nAlso this is a finance page no one is going to recommended this. Be smart and open retirement accounts and put as much money in them. The younger you are the more compounding interest helps you. Work hard when you\u2019re young and able too so when you\u2019re a little older now you have assets and can really have fun."
      },
      {
        "id": "o8oepff",
        "score": 6,
        "body": "Classic"
      },
      {
        "id": "o8le4zr",
        "score": 5,
        "body": "Suggesting an exercise, sit down with a spreadsheet and start at the top with your LES, chart out all of your income, then start adding all your deductions until you get to your take home pay.\n\nNow start adding in all of your living expenses, make your \"budget\", and look at how much you have leftover.  How much are you saving? Investing? Can your monthly finances support a $500 car payment and a $300 insurance bill?\n\nThat's 800 a month for what?"
      },
      {
        "id": "o8jrgg5",
        "score": 5,
        "body": "You will not get insurance on a mustang gt at your age for $200 a month.  Yes you will need full coverage.  Ask your loan officer.  Expect to pay at least $300 per month."
      },
      {
        "id": "o8n4rq2",
        "score": 4,
        "body": "DO NOT DO IT! buy a beater and learn how to invest pls"
      },
      {
        "id": "o8og026",
        "score": 3,
        "body": "Bro just marry the first girl you meet. You'll get more money each month and that'll pay for your monthly car payment"
      },
      {
        "id": "o8luz2v",
        "score": 3,
        "body": "There\u2019s a slight difference in the risk between an old guy driving a 2019 forester and a teenager driving a 2014 Mustang GT. "
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rjf114",
    "title": "Buying a car",
    "body": "Looking to buy a car as an E4, don\u2019t make a whole lot of money lol, about to hit my two year mark in July so a slight increase in pay then.\n\nLooking for tips and guidance, this will be my first car bought and I want to make the right decision when choosing a vehicle and.\n\nShould I buy new or used, who should I finance with?\n\nWhat would be a good price range for a car whether I\u2019m buying new or used? ",
    "flair": "Navy",
    "score": 9,
    "comment_count": 14,
    "created_at": "2026-03-03T03:53:26+00:00",
    "top_comments": [
      {
        "id": "o8cxku9",
        "score": 12,
        "body": "Should buy used and something reliable at this stage. I\u2019m E7 and still buy used. If you don\u2019t have good credit it might be tough to get good rate, but do not go to any car lots outside the base offering pre approval for 30% apr for a mustang or charger"
      },
      {
        "id": "o8dkj59",
        "score": 12,
        "body": "Was looking at Toyota Camrys and Honda civics lol, nothing crazy"
      },
      {
        "id": "o8d8yso",
        "score": 8,
        "body": "Buy used, you can go with financing if its below 7% if you are strapped for cash, but really you should put as much down as possibly. Realistically you should be looking at 5-8yr old car. \n\nI am a captain and still choose to buy used so I can save and invest my money."
      },
      {
        "id": "o8d4jcu",
        "score": 7,
        "body": "Buy used and pay cash. Open a high yield savings account and save your money there. Trust me, you don\u2019t want that car payment and the insurance payment to go with it. Sure you can afford more, but pay yourself first by investing and you will be much happier."
      },
      {
        "id": "o8cxl2p",
        "score": 6,
        "body": "If it\u2019s possible, I\u2019d really highly recommend taking someone with you that has already been through a few vehicle purchases. They\u2019ll be able to guide you and make sure you don\u2019t get screwed. \n\nIf you\u2019re not car savvy and looking at used vehicles, bring someone that has knowledge of cars. \n\nI financed through Navy Federal, did it all on the app, got the check mailed to me and brought it with me to the dealership. \n\nYour price range, new or used, will depend on your budget. Your best bet is to get a used vehicle that\u2019s not too old, and is reliable, and drive it until the wheels fall off. I\u2019m assuming/hoping you also have money tucked away in savings for a down payment and emergency funds as well."
      },
      {
        "id": "o8cycom",
        "score": 5,
        "body": "What branch are you in? Cause it\u2019s always crazy to me to hear how members in other branches get E-4 so quickly. Genuinely wondering."
      },
      {
        "id": "o8dkmo1",
        "score": 3,
        "body": "Navy, E-4 advancement was included with my contract."
      },
      {
        "id": "o8dz4hf",
        "score": 2,
        "body": "I didn\u2019t see this mentioned- check your home of record for vehicle registration for AD military. Some states - Florida for example - give a tax break with certain parameters if registering there."
      },
      {
        "id": "o8g5oh2",
        "score": 2,
        "body": "Go to a credit union, i.e. Navy Federal, Commonwealth, etc. and get a loan from them. You'll have the money in hand which leverages your stance. If you buy from a dealership then it's most likely worth it, because pre-owned vehicles from dealerships generally have had great reviews. If not, then you still have leverage."
      },
      {
        "id": "o8cq26r",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rjdred",
    "title": "Credit/Debit card for Poland?",
    "body": "hi, i'm pcsing to poland in a few months and i am wondering what are good cards for poland? I current have a AMEX Gold and Plat, and I bank with Navy Fed. I would appreciate any help on this, thank you",
    "flair": "Question",
    "score": 4,
    "comment_count": 5,
    "created_at": "2026-03-03T02:55:06+00:00",
    "top_comments": [
      {
        "id": "o8d5zed",
        "score": 8,
        "body": "Get the Chase Sapphire Reserve. It's good to have regardless, but most importantly it's a Visa. Almost nowhere I went in Poland took Amex.  They all take Visa."
      },
      {
        "id": "o8cksbb",
        "score": 3,
        "body": "Chase Sapphire Reserve. No foreign transaction fees and $300 annual travel credit plus a lot of other credits.\n\nMuch better acceptance of Visa and Mastercard rather than American Express outside the United States. [https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit\\_cards\\_military\\_benefits\\_scra\\_mla\\_annual/](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)"
      },
      {
        "id": "o8clgx3",
        "score": 2,
        "body": "Mae sure to get a Visa or Mastercard. There are a lot of places that don\u2019t take AmEx."
      },
      {
        "id": "o8cgrls",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o8chzqb",
        "score": 1,
        "body": "I would recommend the navy fed flagship, you don\u2019t get charged with foreign fees and get a bonus. Also it covers your Amazon prime membership.\u00a0\n\nIf you are willing to get one with capital one a few over there are solid.\n\nIf you fairly new in the credit card game I would ignore and go with Chase because of the 5/24 rule.\n\nI just focus on bonuses while overseas and no fees for currency change and all of that.\n\nI hope this is helpful."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rj2wyj",
    "title": "Question for next year",
    "body": "Ok I\u2019m in a bit of a quibble for next year.\n\nMy husband is active duty Air Force. He\u2019s currently in pre trial confinement for CSAM. I\u2019m planning on divorcing him after the trial(should be sometime this spring/summer). Since he\u2019s being prosecuted under the UCMJ he\u2019s still getting paid.\n\nHere\u2019s the trillion dollar question: do I count the income as prison income on next years tax return? It technically is but it technically isn\u2019t. Leave it to me to deal with grey area shit lol.\n\nNote: due to him being arrested July 1 of last year I chose NOT to exclude it since doing so would exclude all of his income from last year, not just the portion earned while he was in confinement.\n\nThank you so much!",
    "flair": "Question",
    "score": 16,
    "comment_count": 7,
    "created_at": "2026-03-02T19:41:49+00:00",
    "top_comments": [
      {
        "id": "o8aay2m",
        "score": 25,
        "body": ">do I count the income as prison income on next years tax return?\n\nNo.  Under the UCMJ (Uniform Code of Military Justice), pretrial confinement is similar to being held in jail while awaiting trial in the civilian system.  He is still legally presumed innocent until convicted.  He remains on Active Duty status while in pretrial confinement.\n\nFor tax purposes, his income is still treated as regular military compensation, not prison wages."
      },
      {
        "id": "o8b9kof",
        "score": 9,
        "body": "I\u2019m sorry to hear that you\u2019re going through this. I recommend that you seek free legal assistance through your base\u2019s legal assistance office. Many CSAM cases result in brig time, total forfeitures of pay, reduction to E-1, and a punitive discharge. The legal assistance attorney can walk you through this process and any other legal matters that may impact you."
      },
      {
        "id": "o8hmka1",
        "score": 6,
        "body": "Is there a reason you can't file separate taxes?"
      },
      {
        "id": "o8f29uj",
        "score": 5,
        "body": "I already have my own JAG(got one since I\u2019m a victim; he posted our private videos without my consent). I know everything that\u2019s going on via her. She gave me the ok to not count last year\u2019s pay as prison income.\n\nMy main question is wtf to do for next year. His home of record is IL so if I count it as prison income I can\u2019t deduct it which means I\u2019ll owe. I do not want to pay his taxes if I don\u2019t have to.\n\nBut really, tax softwares should have a \u201care you or your spouse in military pre trial confinement\u201d button, followed by a box asking for an arrest date. Then another section asking about a trial and when pay was stopped. Life would be a LOT easier."
      },
      {
        "id": "o8hp4xm",
        "score": 4,
        "body": "I was advised to file jointly for this year by all parties(my folks, his folks, my JAG, etc). Despite a few snafus I submitted it and everything went through perfectly. Just got paid Friday.\n\nThis post is wtf to do for NEXT year. I plan on doing separate since I plan on divorcing him once the trials over. I\u2019ll have to file his taxes again since he\u2019ll be in prison by then. If I exclude he\u2019ll owe in his resident state(IL) and I don\u2019t want to pay it if you know what I mean.\n\nTrust me I had no idea how many issues PTC would cause. Grr."
      },
      {
        "id": "o8iwwom",
        "score": 3,
        "body": "Thank god! Crisis averted!\n\nThank you so much!"
      },
      {
        "id": "o8a819z",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1riulm9",
    "title": "Military FIRE",
    "body": "The r/MilitaryFIRE exists, but the last post was more than 2 years ago and the mods are MIA.  Is there any interest in a new military FIRE sub?",
    "flair": null,
    "score": 14,
    "comment_count": 9,
    "created_at": "2026-03-02T14:41:46+00:00",
    "top_comments": [
      {
        "id": "o8bu3db",
        "score": 16,
        "body": "Yes, but realistically this sub is barely even \"active\" so i think getting a dedicated military FIRE sub is going to be an uphill slog"
      },
      {
        "id": "o8bks5p",
        "score": 7,
        "body": "For sure since career military FIRE is very different than conventional"
      },
      {
        "id": "o8gh8dl",
        "score": 3,
        "body": "For those on FB still, there is an active Military FIRE group "
      },
      {
        "id": "o8apj0e",
        "score": 2,
        "body": "Yes"
      },
      {
        "id": "o88hsm0",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o8je24g",
        "score": 1,
        "body": "Yea lets do it"
      },
      {
        "id": "o8bg5c1",
        "score": 0,
        "body": "Yep"
      },
      {
        "id": "o8h1tru",
        "score": -1,
        "body": "I\u2019ll pass."
      },
      {
        "id": "o8bmqxp",
        "score": -3,
        "body": "r/Mil_Fire is active."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1ri4rro",
    "title": "Co-worker told me the TSP is a bad investment - suggested to do an IUL instead",
    "body": "",
    "flair": null,
    "score": 14,
    "comment_count": 26,
    "created_at": "2026-03-01T18:25:26+00:00",
    "top_comments": [
      {
        "id": "o83fj62",
        "score": 97,
        "body": "Run as fast as you can from that co-worker, and never listen to their financial advice again."
      },
      {
        "id": "o83fryr",
        "score": 55,
        "body": "Your co-worker isn't the brightest individual."
      },
      {
        "id": "o83h7fi",
        "score": 43,
        "body": "Pretty ironic for someone to suggest the TSP has hidden fees, and then recommend a complicated insurance product instead. A fool and his money are soon parted."
      },
      {
        "id": "o83gfhu",
        "score": 21,
        "body": "Okay? They're either a salesperson or are fully bought in on cash value insurance.\n\n\nThe data speaks for itself - heavily commissioned insurance doesn't outperform index funds. Hell, if you want to blow their mind ask what the universal life fund is indexed to and ask who keeps the cash value of the plan when you die."
      },
      {
        "id": "o83hxql",
        "score": 17,
        "body": "At least you now know to never listen to your coworker!"
      },
      {
        "id": "o83kqh1",
        "score": 12,
        "body": "Hope to god that isn\u2019t your supervisor"
      },
      {
        "id": "o83rcpo",
        "score": 10,
        "body": "EXACTLY."
      },
      {
        "id": "o83sk6d",
        "score": 8,
        "body": "The only people who believe in IULs are the people who sell IULs.\n\n[https://personalfinanceclub.com/is-iul-a-scam-yes/](https://personalfinanceclub.com/is-iul-a-scam-yes/)\n\n[https://personalfinanceclub.com/iuls-vs-index-funds/](https://personalfinanceclub.com/iuls-vs-index-funds/)"
      },
      {
        "id": "o84h4vz",
        "score": 6,
        "body": "Your co-worker probably contributes to only the G fund :D"
      },
      {
        "id": "o83q11q",
        "score": 5,
        "body": "Met guys like this in the service but they were the \u201cput your money in silver/bitcoin/nfts/spacebucks\u201d folks."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rhtw96",
    "title": "TSP Account Balances at Enlisted Retirement",
    "body": "I am creeping up on retirement here in about 3.5 years (age 40) but only have been serious about TSP investing for the last 5-6 years (maxing last 2-3 years). I opted into the BRS due to uncertainties with me staying in until retirement, but here we are. I currently have no desire to work a GS job so contributions should stop in 2029/2030. Currently sitting at $253K.\n\nFor those that retired, do you care to share your TSP balance at the time of your retirement? I am struggling to find enlisted peers that took investing in TSP seriously.",
    "flair": null,
    "score": 29,
    "comment_count": 36,
    "created_at": "2026-03-01T10:21:11+00:00",
    "top_comments": [
      {
        "id": "o81j81j",
        "score": 41,
        "body": "2x your income in retirement savings at age 40 is the usual benchmark. You\u2019ll probably be around 300k then, and if you stopped contributing and let it grow until 60, you\u2019ll have ~$1.2 mil. That\u2019s decent, and with the pension and healthcare you\u2019ll be fine.\n\nI don\u2019t know why you got so attacked for a general question. Sometimes people just need reassurance they\u2019re on track and not a granular examination of their financial situation."
      },
      {
        "id": "o81vnpx",
        "score": 16,
        "body": "I\u2019m a 40y/o E-6, 13 months til retirement which will be at 20 years and 1 month of service. Current TSP 431K."
      },
      {
        "id": "o81frpy",
        "score": 10,
        "body": "You\u2019re in a pretty decent spot for only investing for 5-6 years. You have a few years until 40 and your TSP will grow for another 22 years (ish) after that, and if you calculate it out I\u2019m sure 1-1.5 million is possible. That\u2019s a great diversification from the pension, and something spouses and dependents can keep if you pass away.\n\nI\u2019m at 13 YOS (32) and just passed 100k last month. Been seriously putting in $ since 2019. Before that I wasted all my time in G fund. Based on current inputs and a conservative gain, Im planning to be around $300k at retirement (39) or $350k if I stay until 41."
      },
      {
        "id": "o81mfwa",
        "score": 7,
        "body": "If it helps, also went BRS as soon as it hit 01-Jan-2018:\n\nEnlisted 2014, was in G fund, < 5% contributions till 2016, maxed out and moved to 100% C in 2017 and kept it that way since\n\n100k in 2020\n200k in 2024\n380k currently, 8 years to go till 20.\n\nCalcs say with a monthly contribution of 3k that i just averaged out over the next 8 years due to the annual limit increasing, and a 7% growth rate, the balance will be around 1.05m at 20. I wont be able to withdraw till 20 years after in which the balance without anymore contributions at 7% growth still will be 4.24m. \n\nTotal invested 668k, total gains 3.57m"
      },
      {
        "id": "o81pssi",
        "score": 6,
        "body": "Congrats on getting the balance to that much. I have about 4 years left and only have 56k in it. I wish I started when I was younger"
      },
      {
        "id": "o819bog",
        "score": 6,
        "body": "I don't think it is completely useless information and does give insight to my future if someone has gone the path already, whether was a rockstar at TSP or sucked at it. I do understand we all have our own needs and goals that differ greatly but getting a \"progress check\" doesn't hurt. \n\n  \nThis was my actual question: \"For those that retired, do you care to share your TSP balance at the time of your retirement?\"\n\n  \n"
      },
      {
        "id": "o817utt",
        "score": 6,
        "body": "Yes I have. Thank you for asking. The posted you added are referring more to total Net Worth and TSP balance at 60 years old. I was hoping for people to chime in more specific to a 20-year enlisted career.  "
      },
      {
        "id": "o829vem",
        "score": 5,
        "body": "I\u2019m an 9 year E-6, I have the roughly the same balance; currently sitting at 238k."
      },
      {
        "id": "o83k3wu",
        "score": 5,
        "body": "I\u2019ve frequently seen 3x income by 40 as the rule of thumb.\n\nEdit to add: Most of the rules of thumb assume traditional retirement age and a percent of income replacement supplemented by social security."
      },
      {
        "id": "o81cfco",
        "score": 5,
        "body": "No, they other poster is spot on. Everyone's situation is different and what they require to sustain themselves through retirement is unique. There are too many variables to consider that an arbitrary number like \"your current TSP balance\" doesn't even begin to encompass. What you want to ask is exactly what the other poster specified, \"How much do I need to draw each year during retirement to be confortable?\" The answer to that question is what you really want know. Use that information and work backwards.\n\nFor example, if you want to draw 80k per year during retirement to sustain you and your family's lifestyle, then you will need roughly about 1.5 mil saved to draw at 4% per year in addition to your retirement pension. Of course, like I said previously, everyone's situation is unique and if you have other sources of income, that number will be subject to change. The total amount saved required would also different for someone who is single with no dependants versus someone who is married and has 4-5 young dependents."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rhlrsq",
    "title": "I just requested a full withdrawal of my tsp, how long will it take?",
    "body": "Please and thanks. I know the pros and cons and had to do it for personal reasons\u2026.",
    "flair": null,
    "score": 3,
    "comment_count": 9,
    "created_at": "2026-03-01T02:46:51+00:00",
    "top_comments": [
      {
        "id": "o7zupnf",
        "score": 22,
        "body": "Only a couple of weeks probably. We did a hardship withdrawal last February and we got it within a couple of weeks. Also, don't let people make you feel bad about doing that. You gotta do what you gotta do sometimes."
      },
      {
        "id": "o7zv9tx",
        "score": 18,
        "body": "Thanks, yes. I know is not the best decision but i had to do it in order to save my mom\u2019s life basically, not going into details but ya that\u2019s the main reason\u2026"
      },
      {
        "id": "o80bphy",
        "score": 9,
        "body": "Good luck to you! Hope everything works out in your favor."
      },
      {
        "id": "o805h0j",
        "score": 3,
        "body": "I believe mine took about 2 weeks, they sent 2 checks in the mail. I\u2019m sure direct deposit is faster."
      },
      {
        "id": "o7znqdw",
        "score": 2,
        "body": "Some ppl had told me that it they have requested it tuesday and received by Thursday, but want to hear other opinions."
      },
      {
        "id": "o807rmh",
        "score": 2,
        "body": "Up to 2 days for them to process then its on your bank.  3 to 7 days from start to finish"
      },
      {
        "id": "o8ec4eh",
        "score": 2,
        "body": "I\u2019m thinking of requesting a hardship withdrawal today as well. To help get ahead and eliminate all of my debt prior to retirement. How did the process work?"
      },
      {
        "id": "o8fkafp",
        "score": 2,
        "body": "You log into your TSP, and it has withdrawal page, you'll go there and you have to answer some questions and it'll tell you if you qualify to do a hardship withdrawal, then after that it'll preview and they'll mail you a check but they will also deposit it into your bank account!"
      },
      {
        "id": "o7zlrph",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rhi6z2",
    "title": "Credit Cards Military Benefits, SCRA, MLA, Annual Fee Waivers, Chase, American Express, Spouses | Updates Monthly",
    "body": "This is a monthly thread to discuss or ask questions about military benefits on credit cards.\n\nIn general: American Express, Chase, and some other banks waive the annual fees on credit cards for active duty, Guard and Reserve on 30 day or greater active orders, and dependent spouses.\n\nThese individuals are known as \"covered borrowers\" of the Servicemembers Civil Relief Act (SCRA) and Military Lending Act (MLA).\n\nThe simplest definition of a covered borrower is active duty military personnel, Guard and Reserves on 30 day or greater active duty orders, or dependent spouses of any of the above.\n\nThe simplest way to check if you will receive MLA or SCRA protections on your account is to check the [MLA Database](https://mla.dmdc.osd.mil/) or [SCRA Database](https://scra.dmdc.osd.mil/).\n\nThe MLA and SCRA database are the same databases that the credit card companies check to determine if you qualify for MLA or SCRA benefits.\n\n**If you are not listed as eligible in these databases, you will not receive MLA and SCRA benefits applied to your account.**\n\n**You must be listed as eligible in these databases for the credit card companies to apply your military benefits.**\n\n# Are military spouses eligible to open their own card accounts?\n\nYes, military dependent spouses are eligible to open their own card accounts on Chase, American Express, Citi, U.S. Bank, and Bank of America and receive their own annual fee waivers.\n\nCheck the MLA database before applying [MLA Database](https://mla.dmdc.osd.mil/) to ensure you will receive your fee waiver without any issue. If you are not listed in the MLA database, check DEERS to ensure your Social Security number and name are listed correctly.\n\nYou must be listed in the MLA database when the account is opened / established or you will not be eligible for fee waiver benefits. For example, if you opened an Amex or Chase card before you married the active duty servicemember, that account will never be eligible for MLA benefits. The account must be established while *you* are eligible for MLA benefits, as confirmed in the MLA database.\n\n# What Cards are Eligible for SCRA or MLA benefits?\n\n**American Express**\n\n* The Platinum Card\u00ae from American Express\n* American Express Platinum Card\u00ae for Schwab\n* American Express Platinum Card\u00ae for Morgan Stanley\n* American Express\u00ae Gold Card\n* American Express\u00ae Green Card\n* Marriott Bonvoy Brilliant\u2122 American Express\u00ae Card\n* Marriott Bonvoy Bevy\u2122 American Express\u00ae Card\n* Delta SkyMiles\u00ae Reserve American Express Card\n* Delta SkyMiles\u00ae Platinum American Express Card\n* Delta SkyMiles\u00ae Gold American Express Card\n* Blue Cash Preferred\u00ae Card from American Express\n* Hilton Honors American Express Aspire Card\n* Hilton Honors American Express Surpass\u00ae Card\n\n**Chase**\n\n* Chase Sapphire Preferred\u00ae\n* Chase Sapphire Reserve\u00ae\n* Southwest Rapid Rewards\u00ae Plus Credit Card\n* Southwest Rapid Rewards\u00ae Priority Credit Card\n* Southwest Rapid Rewards\u00ae Premier Credit Card\n* United Explorer Card\n* United Quest Card\n* United Club Infinite Card\n* Aeroplan Card\n* Marriott Bonvoy Boundless\n* Marriott Bonvoy Bountiful\n* Ritz-Carlton Credit Card\n* IHG One Rewards Premier Credit Card\n* Disney Premier Visa Card\n* World of Hyatt Credit Card\n* British Airways Visa Signature\u00ae card\n* Aer Lingus Visa Signature\u00ae card\n* Iberia Visa Signature\u00ae card\n\n**Citi**\n\n* Citi\u00ae Strata Elite\n* Citi\u00ae / AAdvantage\u00ae Platinum Select\u00ae World Elite Mastercard\u00ae\n* Citi\u00ae / AAdvantage\u00ae Executive World Elite Mastercard\u00ae\n* Citi\u00ae Premier\u00ae Card\n* Citi\u00ae Prestige\u00ae Card\n\n**U.S. Bank**\n\n* U.S. BANK ALTITUDE\u00ae RESERVE VISA INFINITE\u00ae CARD\n* U.S. BANK FLEXPERKS\u00ae GOLD AMERICAN EXPRESS\u00ae CARD\n* Korean Airlines SKYPASS Select Visa Signature\u00ae Card\n\n**Bank of America**\n\n* Bank of America\u00ae Premium Rewards\u00ae Elite Credit Card\n* Atmos\u2122 Rewards Summit Visa Infinite\u00ae\n\n\n\n\n|*Card Issuer*|*Fees Waived Under MLA*|*Fees Waived Under SCRA*|\n|:-|:-|:-|\n|American Express|All Personal Cards|All Personal Cards|\n|Capital One|None|All Personal Cards|\n|Chase|All Personal Cards|All Personal Cards**|\n|Citi|All Personal Cards\\*|Unknown|\n|U.S. Bank|All Personal Cards|All Personal Cards|\n|Bank of America|All Personal Cards|Unknown|\n\n\\*For Citi, you must send a copy of your active orders and your MLA certificate from the MLA Database to [MILITARYORDERS@CITI.COM](mailto:MILITARYORDERS@CITI.COM) and request MLA benefits. You must also have a statement balance on your account in the month you are charged the annual fee or you will not receive the MLA annual fee credit.\n\n\\**Recent data points suggest that Chase business cards, opened before active duty start, can be annual fee waived if the account holder applies for SCRA benefits after they go active duty.\n\n# Which Act Applies, SCRA or MLA?\n\nThe military benefits you receive on credit cards depend on when you establish or open the account.\n\n**Open account before active duty = SCRA**\n\n**Open account while on active duty = MLA**\n\nIf you apply for the account **prior** to active duty orders, you are eligible for Servicemembers Civil Relief Act (SCRA) benefits while you are on active duty orders.\n\nIf you apply for the credit card account **while you are on active duty orders**, a Guard and Reservists on 30 day or greater active orders, or a dependent of an active duty servicemember, you are eligible for Military Lending Act (MLA) benefits while you are on active orders or a dependent of someone on active orders.\n\nThe banks and credit card companies may deny you SCRA benefits if you opened the account while on active duty. In that case, confirm they are applying MLA benefits and if they are not, check MLA database and then apply for MLA benefits.\n\n# SCRA & MLA Covered Borrowers Details\n\nTo qualify for SCRA benefits, the credit account **must be established before active duty orders start.**\n\nCovered borrowers of SCRA defined as:\n\n* Active duty US military on Title 10 orders in the Army, Navy, Air Force, Space Force, Marines, or Coast Guard\n* National Guard or Reservists on 30 day or greater active duty orders (such as Title 32, Title 10)\n* Public Health Service and NOAA Commissioned Officers\n\nTo qualify for MLA benefits, the credit account **must be established while your or your active duty sponsor is on active duty orders of greater than 30 days.**\n\nCovered borrowers of MLA are defined as:\n\n* Active duty member of the Army, Navy, Marines, Air Force, Space Force, or Coast Guard\n* Guard or Reservists on 30 day or greater active orders\n* A spouse or child dependent of an Active Duty member of the Armed Forces as defined in 38 USC 101(4) \n\n# Best Starter Credit Card\n\nCheck your credit score through your bank, [Credit Karma](https://www.creditkarma.com/), or [Credit Sesame](https://creditsesame.com).\n\nIf you don't have a credit score or your score is below 700, **start with a no annual fee credit card from USAA or Navy Federal Credit Union** **(NFCU)**.\\\\\n\nOr, apply for a secured credit card from another military friendly bank or credit union. That should be your best option to build a higher credit score.\n\n# What Fees Are Waived Under MLA and SCRA?\n\n In general, the following fees are waived by Chase and American Express\n\n* **Annual Membership fees**\n* Authorized user fees\n* Overlimit fees\n* Late Payment fees\n* Returned Payment fees\n* Statement Copy Request fees\n\nAmerican Express and Chase are very cryptic in the benefits they actually provide under MLA or SCRA. Usually the customer service reps just read a script if you call and ask. This is not helpful and why we've collected this data here.\n\nIf you have additional data points, please share them, as this information is only as accurate as the data points we collect.\n\nIf you have any other questions on credit cards in the military, please comment below.\n\nReminder: no referral links or solicitation of referral links.",
    "flair": null,
    "score": 20,
    "comment_count": 15,
    "created_at": "2026-03-01T00:01:49+00:00",
    "top_comments": [
      {
        "id": "o7ywwu9",
        "score": 5,
        "body": "Anyone have DP for annual fee reimbursement for new Bilt cards? Customer service informed me that active duty should get AF waived but personally haven\u2019t pulled the trigger on the card"
      },
      {
        "id": "o7zeini",
        "score": 4,
        "body": "I can confirm that I got my AF waived. Had to send in orders to verify MLA. Pretty easy process and surprised this megathread isn\u2019t updated to reflect as many others have reported having their AF waived."
      },
      {
        "id": "o7zezmk",
        "score": 3,
        "body": "I haven\u2019t got charged at all. Support@card.bilt.com just let them know you would like to apply for MLA and get the annual fee waived."
      },
      {
        "id": "o80jelu",
        "score": 2,
        "body": "Not sure if it\u2019s the same thing but I had two freedom cards that were opened before 2017. I PCed them to CSR in 2024 and got both of them waived"
      },
      {
        "id": "o8599g9",
        "score": 2,
        "body": "I was able to get it applied to my platinum in this way. Have had it for over 5 years. Married last year. S/O joined 2 years ago. Got 2 years of fees refunded"
      },
      {
        "id": "o88zd8u",
        "score": 2,
        "body": "The fee is waived as long as you open the card while on orders. If you open a CSR card while on orders for example. You won't pay the annual fee of $795 for the first year. If you are not on orders when your anniversary comes around the next year, you will get charged."
      },
      {
        "id": "o7zeqe7",
        "score": 2,
        "body": "Which email did you send them? And did you get charged then sent them an email? I haven\u2019t gotten charged an annual fee yet"
      },
      {
        "id": "o7yuehi",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o807ndh",
        "score": 1,
        "body": "Anyone had any luck getting MLA benefits applied to a Sapphire Reserve card opened before the MLA officially passed and/or prior to September 2017? I tried once or twice back in the day and I seemed to be in a weird loophole where I don't apply for either parameter, according to their online reps. Thanks!"
      },
      {
        "id": "o874cfp",
        "score": 1,
        "body": "If you're Guard/reservist on orders >30 days, how long is the fee waived? Hypothetically if someone was on a months long TDY and opened a card?"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rg95se",
    "title": "BAH question",
    "body": "I'm getting married soon after tech school and my spouse wants go live in florida no matter where i get stationed...\n\nafter we get married if we use the va loan to buy in florida does the bah cover her living expenses? ",
    "flair": null,
    "score": 0,
    "comment_count": 26,
    "created_at": "2026-02-27T15:07:27+00:00",
    "top_comments": [
      {
        "id": "o7pti3j",
        "score": 49,
        "body": "Does she have valid reasons for wanting to live in Florida whether you are there or not?\n\nDoes she work and have a healthy income?\n\nAre you sure this is the right person to be marrying?\n\nEven if it is the right person, is now the right time to get married?\n\nYou don't want to start your military career off being financially irresponsible. That will cause a lot of stress for you and could lead to poor work performance and distractions. Plus, you might be miserable. "
      },
      {
        "id": "o7pxtz3",
        "score": 33,
        "body": "Please listen to everyone here. This is not a good idea. Do not get married right now or after tech school. Definitely wait to see where you get stationed. Wait to see if you will deploy once at your unit. Give yourself time to adjust to the mil life. Save up some money first and start the marriage on good footing. Give it at least a year. Please."
      },
      {
        "id": "o7pvhsh",
        "score": 32,
        "body": "This is the shit I'm really wondering about. How are you going to get married to an active duty soldier and immediately say \"We're not going to live together\" right out the gate. On the surface, it seems like a REALLY bad idea all the way around. But maybe there are some mitigating circumstances..."
      },
      {
        "id": "o7pn80i",
        "score": 20,
        "body": "Most definitely not.  You will be receiving the BAH rate for the duty location you are at. These can be easily looked up online as well."
      },
      {
        "id": "o7pwto9",
        "score": 15,
        "body": "Okay, I know it's not really the question you're asking but please delay the marriage and do not have children yet. I've seen this happen more than once and it almost always results in a divorce. You have a very young marriage in play here and your spouse to be is already telling you that regardless of where you are, they want to be somewhere else because something else is more important to them than your marriage's success.\n\n\nAt an absolutely bare minimum, you should be going through full marriage counseling and I don't mean at some random Church. Call military One source and get couples counseling. It's completely free and is paid for. This can play out any number of ways, but you need to be prepared for a situation where, if you stay in the military, you complete this tour and then you get assigned to another tour of that isn't in Florida and you're away from your spouse for years on end. It's one thing to Geo batch when you're an established couple and you've been together through some hard times, it's an entirely other thing to get married to someone and then have them bolt immediately.\u00a0\n\n\nBah is just in your pay and it will be based on your assignment, not her location in this case. You can use it for whatever you want. You can functionally live in a rented cardboard box and spend an enormous amount of money on a pickup truck if you want. The problem with your plan here is that you're setting up to buy a house or your absentee wife, who presumably isn't going to be working, and then you're going to provide for your own welfare and housing some other way. This is a very high-risk situation."
      },
      {
        "id": "o7pmyxg",
        "score": 14,
        "body": "Absolutely not. You'll get BAH for your location.\n\nOne exception for going overseas on an unaccompanied tour."
      },
      {
        "id": "o7pwyts",
        "score": 12,
        "body": "She can live wherever she wants.  Your BAH rate will be for your duty station's location, the money gets deposited into your account along with the rest of your paycheck.  Just be aware that you'll also need to cover for a place for you to live in, government quarters will no longer be an option as a married SM receiving BAH.\n\n  \n"
      },
      {
        "id": "o7ptb8h",
        "score": 12,
        "body": "I think they mean like your living arrangements at any duty station you get. For the Army if you\u2019re getting BAH, you can\u2019t live in free government housing as well. So you getting BAH to pay for a house in FL, but you living in CA you\u2019ll be SOL living in a tent since BAH won\u2019t cover both places\n\nAlso why would you get married and buy a house if you\u2019re not gonna be living in it or seeing your spouse? Some people do it cause they won\u2019t want to up root children who are already established and in HS but not children seems odd"
      },
      {
        "id": "o7pyy5q",
        "score": 12,
        "body": "....so you're paying for this woman's housing and for her mother's housing. They want your money and are indifferent as to whether you are with them.\n\n\nYou are racing towards a really unhappy life. What is driving the urge to get married? Why don't you just send your girlfriend $500 a month or so? A gift is better here because you can stop at will and don't need to go through this problem."
      },
      {
        "id": "o7q2o47",
        "score": 7,
        "body": "Why are you marrying someone you don\u2019t plan on living with? Is this a temporary thing for her to live in Florida? Does she have plans to eventually live wherever you are. Also everyone wants to go to Florida. I will be shocked if you get stationed there."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rfrrck",
    "title": "CA State taxes: Husband stationed in VA and his SLR is CA (not subjected to state taxes), yet current filing is showing we owe",
    "body": "Navy spouse here. \n\nTaxes haven\u2019t actually been filed yet, and I\u2019m working with a tax professional(hr block) this year because he also has some gambling winnings and it\u2019s all become a bit too complicated for me to do myself. I also live in nyc currently for school and as such my tax lady only knows her way around ny tax laws/policies and is doing some research before we submit. \n\nI\u2019m just wondering if any ca residents stationed out of state have any insight!",
    "flair": null,
    "score": 0,
    "comment_count": 16,
    "created_at": "2026-02-27T00:34:59+00:00",
    "top_comments": [
      {
        "id": "o7manxe",
        "score": 4,
        "body": "Military income earned outside of CA is tax exempt. The gambling earnings are not exempt and are why you owe unless the taxes were withheld. I\u2019d also look into weather they\u2019re taxable to CA or if they are taxable to VA. Because it\u2019s one or the other\n\nAlso note that you have the option to file in CA jointly due to MSRRA and that your income is nonresident, non California source income and therefore not subject to CA tax"
      },
      {
        "id": "o7mvrtf",
        "score": 2,
        "body": "I've sorry but if you're paying a tax professional and they can't figure this out themselves, you need to pay a new tax professional.\n\nI'm AD, my wife and I are both CA residents and haven't lived there in over a decade and we never owe CA any taxes. I'm not sure how gambling income works, but I've had significant non-military income (such as investment income) and I've never owed taxes on that...\n\nFull disclosure, I've been using a CPA for 20 years now. We file state taxes in 3-4 states and they take care of all of it. I never have to go to Reddit myself. They're worth every penny. Please find a good CPA."
      },
      {
        "id": "o7me04i",
        "score": 2,
        "body": "I thought filing as a nonresident in CA would apply only if we lived together/I moved with him to his assignment?"
      },
      {
        "id": "o7m6bm1",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o7m8ew6",
        "score": 1,
        "body": "There isn't really a question here.\n\nWhat states are you filing to and what states are saying you owe? What state was withheld (or not) throughout the year?"
      },
      {
        "id": "o7mbpod",
        "score": 1,
        "body": "Is he counting only gambling profit or the entire amount he won?"
      },
      {
        "id": "o7sft31",
        "score": 1,
        "body": "Based on the info you provided here and in the comments, your tax return isn't that complicated:\n\n* Your husband should file CA, non-resident return. He can exempt his military income, but not the gambling income. Your husband *always* must file a CA state return, even if nothing was withheld, because CA is the state listed on his LES so that's where his income gets reported.\n   * The CA return could either be married, filing separately or married, filing jointly. However, since there are non-military gambling earnings, married, filing jointly will maximize your standard deductions.\n   * The above does not matter whether you are or are not a 'legal resident' of CA (a phrase which actually holds no meaning)\n* Since your husband is not stationed in NY, then you need to file a NYS tax return as a resident. The MSRRA only applies when you are in a state for the sole purpose of executing your military spouse's orders. If you spent more than 180 (or is it 183?) days domiciled in NY *not* executing your husband's military orders, then you are a resident for tax purposes. This is spelled out in the NYS tax return forms and instructions. Same schpeil about married filing jointly / separately... you want to file married, filing jointly in order to maximize your deductions.\n* If the gambling winnings exceeded the minimum for reporting, husband needs to also file a return in the state where he *earned* the gambling money *and* CA (do the state other than CA first, then deduct it from CA income). If this was online, then you're in luck - it's only CA. You should do this married filing *jointly* in order to maximize the standard deduction.\n\nSo to recap:\n\nYou:\n\nFile a resident NY return. Do it married, filing jointly to maximize deductions.\n\nHusband:\n\nFiles a non-resident return in state where gambling winnings were earned, if necessary. Do it married, filing jointly to maximize deductions.\n\nFiles a non-resident return with CA, deducting state income tax paid from gambling winnings if applicable. Do it married, filing jointly to maximize deductions."
      },
      {
        "id": "o82j77x",
        "score": 1,
        "body": "My understanding for CA residents stationed outside of CA was that we had state tax deducted from our checks and we just got it all back when we filed as part of the refund. At least thats how it's worked for me."
      },
      {
        "id": "o7seks1",
        "score": 1,
        "body": "Most 'tax professionals' who handle regular personal income tax returns are bottom of the barrel accountants.\n\nAlso, 'tax professionals' get certified in their state and are never going to be familiar with out of state tax laws / regulations."
      },
      {
        "id": "o7ma375",
        "score": 1,
        "body": "Filing to NY & CA, NY will be giving a refund, CA shows taxes will be owed. My NY tax was withheld all year, his CA tax was not withheld because CA doesn\u2019t tax residents who are stationed out of state."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rfiouy",
    "title": "New LT, confusing Tax Laws",
    "body": "New LT PCSing to Alabama. my HOR is Missouri which has a 100% tax deduction for Active Duty military. My wife is moving with me and working remote for a Missouri based company. SCRA says that she will pay Missouri state taxes but Im finding conflicting info on if her income can be considered a deduction as well. Some websites are saying yes, some are saying no, and the statutes aren't clear. Curious if anyone else has experience with Missouri taxes.",
    "flair": "Question",
    "score": 4,
    "comment_count": 20,
    "created_at": "2026-02-26T18:48:30+00:00",
    "top_comments": [
      {
        "id": "o7ka4mr",
        "score": 22,
        "body": "https://dor.mo.gov/forms/5735.pdf\n\nThis says no, its fully taxable.\n\nTypically only the military pay gets exceptions."
      },
      {
        "id": "o7kahhy",
        "score": 12,
        "body": "Perfect document. Lays it out clearly. Thank you! That\u2019s what I assumed but didn\u2019t want the IRS to come knocking"
      },
      {
        "id": "o7kk6rf",
        "score": 8,
        "body": "Follow MSRRA rules.\n\nRef: https://dor.mo.gov/forms/Military%20Reference%20Guide.pdf\n\nYour wife pays state taxes to her State of Residency.  Not Missouri unless that is her SoR.\n\nShe can claim same SoR as you.\n\n\"The\u00a0Military Spouses Residency Relief Act\u00a0prevents income earned by servicemembers\u2019 spouses from being taxed by any state other than the state they declare as their state of residence\"\n\nSo look at what is most beneficial for you both. Whether its Alabama or Missouri. And if you ever get stationed to a no income tax state change to it and keep it the rest of your mil career."
      },
      {
        "id": "o7n9r94",
        "score": 7,
        "body": "At least I didn\u2019t botch my green to gold interview you only had years to prepare for \ud83d\ude2c\ud83e\udd37\ud83c\udffb\u200d\u2642\ufe0f"
      },
      {
        "id": "o7kwrhk",
        "score": 5,
        "body": "Let\u2019s make this real easy for you going forward:\n\nYour HOR is Missouri, they don\u2019t tax military income at the state level (most states don\u2019t now). So go to finance, fill out a state tax exception form, and you will not have any state taxes taken out for the rest of your career. If Army, the form is DD 2058-1. This is better than getting it all during tax season as your checks are bigger now.\n\nYour wife\u2019s residency can be Missouri, your HOR, under MSRRA. Have her fill out a state tax exemption form, every state has their own. Do this so then you don\u2019t need to worry about filing a state tax return. Or, just file a state return for in MilTax. It\u2019s takes a little finagling but you essentially just mark her as a non resident and she\u2019ll be able to get it all back. However, if you know you\u2019re going to be somewhere for awhile, just do the state tax exempt form in that respective state for her."
      },
      {
        "id": "o7kfbjb",
        "score": 5,
        "body": "Please note that the individual state laws vary. It doesn't affect you if you always just keep Missouri for the remainder of your life, you'd just keep filing an MO tax return. But, some states do not tax any active duty income or any income made by a spouse who is living outside the state to be with a military member on PCS orders. So in some cases it may be advantageous to switch residence if you have the opportunity *and* if the tax laws make sense for you to do so financially."
      },
      {
        "id": "o7kjytn",
        "score": 3,
        "body": "Not always true, if he switches SoR.\n\nWrong reference. He needs to follow MSRRA guidelines for his spouse.\n\nhttps://dor.mo.gov/forms/Military%20Reference%20Guide.pdf"
      },
      {
        "id": "o7kyk54",
        "score": 3,
        "body": "The problem is his wife's income is not exempt.  She will still need to file state taxes to her SoR which I am assuming is Missouri. She needs to establish residency in a non-income taxed state first before MSRRA benefits are fully realized."
      },
      {
        "id": "o7kp211",
        "score": 3,
        "body": "The question was if the Spouse's income can be deductible in Missouri, and the answer to that is no. \n\nHer income is still taxable by Missouri (I presumed both their state of legal residence is Missouri). She can file taxes in Missouri or her state of legal residence if other than Missouri. \n\nWhen they move to Alabama, she would be exempt from Alabama income tax if the she maintains a state of legal residence elsewhere, but she is still subjected to the state of legal residence income tax. There isn't an exemption for her income to be not taxed at all on the state level unless your state of legal residence does not have an income tax, like Florida."
      },
      {
        "id": "o7krbgh",
        "score": 2,
        "body": "For you as a MO resident, I found that setting your state deductions to \u201c99\u201d was enough to eliminate your MO state income tax withholding (you won\u2019t owe tax but they may still be withholding tax until you file for your return unless you\u2019ve somehow stopped the withholding). I still filed at the end of every year to ensure MO didn\u2019t think I owed them money but it kept me from granting the Governor an interest free loan for the entire tax year until I could claim it back. 99 deductions was enough to eliminate my entire state withholdings up past at least O4, but I eventually started having state tax withheld again as a military non-resident as my income grew. But I sure wish I\u2019d been smart enough to establish FL residency when I was stationed there to eliminate the entire problem for the next few decades and avoid having to file a state return every year\u2026"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rfgtkh",
    "title": "State taxes from the state I\u2019ve joined while claiming residency from another?",
    "body": "I have currently held a residence in Tennessee for the last 2 years due to being stationed at Fort Campbell. Whenever I go into do my taxes, the company makes Iowa give all state taxes back since I have a DL, registration, adress, and had a voting card for Tennessee. However I noticed I still am under Iowa when it comes to my Army Les as they collect taxes and come tax season they give it back since Tennessee has no income taxes and they see me as residing in Tennessee. I am moving to Oklahoma soon and was wondering if I should update my les when I am stationed there or can I just keep it under Iowa as I plan to return there after service? Thank you!",
    "flair": null,
    "score": 5,
    "comment_count": 10,
    "created_at": "2026-02-26T17:41:03+00:00",
    "top_comments": [
      {
        "id": "o7jyldj",
        "score": 6,
        "body": "You can and should update your withholdings to TN and keep it that way."
      },
      {
        "id": "o7jzw58",
        "score": 4,
        "body": "Your State of Residency does not change, unless you change it.  It is best for tax benefits to claim the State that does not charge income taxes or on military income while out of state.\n\nThe problem comes into play in that you are registered to vote in Tennessee which is not your state of residency.\n\nFortunately for you, Tennessee does not charge state income tax so that works for you for tax benefits (so they won't ever come after you saying you owe them taxes). Iowa also does not charge state taxes provided you are not stationed within Iowa --- that is why you are getting refunds.\n\nBut your main issue is you need to clean up your residency. Since you are registered to vote in Tennessee, change your State of Residency with military finance to Tennessee and be done with.  You won't have to file State income taxes each year to TN either which is another bonus.\n\nYour other option is to keep your Iowa residency, but you need to register to vote in Iowa.  You have to file State taxes each year to get your refund (if withholding is required), and if you ever get stationed in Iowa you will owe State taxes."
      },
      {
        "id": "o7k2rvn",
        "score": 3,
        "body": "Had a similar conversation in another thread earlier today. Home of record doesn't change, but State of Residency CAN change. It's based on a state's interpretation of indicators such as drivers license, voter registration, DD 2058, etc. Agree with everything else above though. It's best to put in effort to keep all your residency documents aligned. That eliminates room for doubt and gives you a basis to argue against any arbitrary determinations by random state tax officials."
      },
      {
        "id": "o7k698p",
        "score": 3,
        "body": "You are still in TN. Does not matter that you are moving soon. All you need is a valid address which you have.\n\nTell your NCO you need to update your paperwork with finance. Spend the 1-2 hrs it takes to get this done and be done for the rest of the time you are in the military.\n\nIf you want to remain Iowa resident. You are free to register your car, get a DL in any state.  You just can't register to vote in any other state. You will need to register to vote in Iowa.\n\nAgain tax implications and benefits you best to change to TN residency. If not for yourself, benefits for your spouse if you ever get married later. Unless there is some benefit in remaining Iowa resident I dont know about."
      },
      {
        "id": "o7k08tc",
        "score": 2,
        "body": "Not illegal, but I don\u2019t see why you\u2019d want to."
      },
      {
        "id": "o7ju608",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o7jztsf",
        "score": 1,
        "body": "I gotcha and will definitely see about doing that. From a legal standpoint though just in case, is it legal to keep my state taxes in Iowa if it\u2019s where I joined even if I turned in my license and registration for Tennessee? Trying to make sure there\u2019s nothing illegal about keeping Iowa as state taxes for the last 2 years and if for whatever reason i didn\u2019t switch and I had Iowa down in the future."
      },
      {
        "id": "o7k1e57",
        "score": 1,
        "body": "I understand. My voter registration expired I believe and I also am leaving Tennessee really soon and kinda screwed up not switching to Tennessee when I had the chance based on the comment above. When I get to Oklahoma and switch my DL and registration to OK can I still claim Iowa then?"
      },
      {
        "id": "o7k7qab",
        "score": 1,
        "body": "Yes poor wording. I added that context that you can change it if you want."
      },
      {
        "id": "o7k1hsy",
        "score": -1,
        "body": "Yeah I should\u2019ve when I had the chance but I\u2019m within days of leaving. Might still try to. Appreciate the help."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rfe9yv",
    "title": "AMEX Platinum Card fee waiver - chicken or egg?",
    "body": "Hello, hopefully a simple question: When is the fee waived?\n\n* Is the military check immediate upon card application, so no fee is charged from the start?\n* Or, is the fee charged upon card grant and we have to follow-up with a fee waiver request?\n\nThe concern with the second bullet is, what if they deny the request and I'm on the hook for $900? Thanks!",
    "flair": null,
    "score": 0,
    "comment_count": 10,
    "created_at": "2026-02-26T16:10:35+00:00",
    "top_comments": [
      {
        "id": "o7jirh8",
        "score": 7,
        "body": "Reserve shouldn\u2019t get the fee waiver, technically."
      },
      {
        "id": "o7kl7dd",
        "score": 5,
        "body": "Jesus fucking Christ.\n\nYou're NOT eligible. You're not a covered borrower under MLA. I'm constantly amazed at people willing to play games with $900 af cards. Do some basic god damn research."
      },
      {
        "id": "o7jbb0w",
        "score": 4,
        "body": "If your in military you shouldn\u2019t be charged with regardless. What you need to worry about is if you\u2019ll keep the card when you\u2019re out. A lot of people say just cancel it but understand how it\u2019ll affect your credit score (dropping your credit age, credit utilization etc)"
      },
      {
        "id": "o7js27y",
        "score": 3,
        "body": "Reserves do not get the fee waived. You have to provide them a copy of 30+ day orders. They are also fairly quick about it. They got me like a month after I dropped to the reserves. \n\nThey will retroactively backpay you since I got hit in Feb with the fee one year, showed orders that started in Mar and they credited me the fee."
      },
      {
        "id": "o7jajqu",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o7kzwls",
        "score": 1,
        "body": "You have to have been on orders/in for atleast 30 days before you apply because that\u2019s how long it takes to be in the MLA data base."
      },
      {
        "id": "o7krcsh",
        "score": 1,
        "body": "You do not seem eligible, as you are not on active duty orders. Check the MLA database before applying: [https://mla.dmdc.osd.mil/mla/](https://mla.dmdc.osd.mil/mla/)"
      },
      {
        "id": "o7kxzcx",
        "score": 1,
        "body": "The answer I'm looking for, thank you!"
      },
      {
        "id": "o7l7peq",
        "score": 1,
        "body": "Do basic research before you mess around with this stuff..\n\nhttps://www.reddit.com/r/MilitaryFinance/s/9wr5ySJr3K"
      },
      {
        "id": "o7kyaxj",
        "score": -2,
        "body": "You seem nice. That was sarcasm, you don't seem nice."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rfaqz3",
    "title": "Confused about Home of Record vs State of Legal Residence (GA / FL / VA military tax situation)",
    "body": "Hi everyone. I\u2019m hoping someone can help because I genuinely don\u2019t understand how this works.\n\nMy wife joined the Navy last year at 32. We did things a little differently than most. We didn\u2019t like the recruiter in Georgia (where we lived), so she worked with a recruiter in Florida through her network. Because she knew she would be going down to Florida multiple times for MEPS, paperwork, swearing in, and eventually her ship date in September, she stayed at a Florida address for the summer during that process and used that address when she enlisted. Since I work remotely, I was down there a lot. \n\nAs a result, her Home of Record shows Florida, and she currently isn\u2019t paying state income tax since Florida doesn\u2019t have one.\n\nHere\u2019s where I\u2019m confused:\n\n* We never moved our stuff to Florida. It stayed in Georgia even though she was down there all of summer 2025 and I was down there for about half of that. \n* She hasn\u2019t lived in Georgia since July.\n* She was physically in Florida for just over two months before shipping out.\n* She\u2019s now in A-school/C-school and we\u2019re moving to Virginia Beach, VA at the end of March.\n* We are currently renting an apartment in Georgia, but once I move out to join her in Virginia, I won\u2019t have a Georgia address anymore.\n\nWhen she checks her state withholding page, it shows Florida for tax purposes. I understand that \u201cHome of Record\u201d and \u201cState of Legal Residence\u201d aren\u2019t necessarily the same thing, but I\u2019m not sure what officially applies here or how it affects me.\n\nI would prefer to keep my residency in Georgia. I don\u2019t know if that\u2019s technically called Home of Record for me, but I want Georgia to remain my legal residence. My confusion is: when I leave the Georgia apartment and I physically move to Virginia, how do I maintain Georgia residency without a Georgia address? How does that work with employers. \n\nI\u2019m also wondering whether it would be smarter for me to just claim Florida since that\u2019s what she has now, even though I never actually moved there.\n\nSo my two main questions are:\n\n1. Since my wife didn\u2019t pay Georgia state taxes for the military (because she enlisted using a Florida address), does that create any issues for me when we file taxes if I remained in Georgia?\n2. Going forward, what is the correct way for me to maintain Georgia residency while living in Virginia as a military spouse \u2014 especially if I no longer have a physical Georgia address \u2014 or would it be more beneficial (and legal) to switch to Florida instead?\n\nI don't want to do anything wrong. I do not like tax time and I just want to pay what I legally owe and move on. I just genuinely don\u2019t understand how military residency and tax rules interact when things don\u2019t follow the \u201cnormal\u201d path. I also do not live near a base to just go to for help. My nearest is Dobbins Air Reserve Base in Marietta, or Robins Air Force Base in Warner Robbins. I will go there if someone can help. Maybe I should go to H&R Block? \n\nAny clarity would really help.",
    "flair": null,
    "score": 10,
    "comment_count": 9,
    "created_at": "2026-02-26T13:53:54+00:00",
    "top_comments": [
      {
        "id": "o7im7tp",
        "score": 17,
        "body": "Why are you so worried about maintaining GA residency? Is it for voting?\n\nOtherwise just claim FL and stop paying state income tax."
      },
      {
        "id": "o7imve3",
        "score": 4,
        "body": "I think you would fall under MSRRA. I believe you have the option to claim FL or the state you get a job at. Since her legal residence says FL, prob be beneficial to claim that when filing MFJ. But yea you'll prob want to talk to an actual tax expert."
      },
      {
        "id": "o7jv85u",
        "score": 3,
        "body": "Forewarning:\n\n* I am not a Tax Expert or Legal Advisor, so take my advice for what it is worth.  Seek outside counsel.  However, your best bet is to contact Military OneSource, they have free tax advisors to help the military community.\n* What I can provide is 20-years of experience taking advantage of SCRA and MSRRA benefits to essentially not pay any state tax on my military income and my wife's (civilian) income.\n\nMain law that matters to you: MSRRA - you can essentially establish your Residency the same as your wife, without ever stepping foot in FL.  Previously the law required that you reside together with your spouse within the same State in order to establish residency; this is now changed and requirement removed.\n\n* Since the Navy processed the paperwork as such, your wife lived in FL, your wife already established her residency of FL.  She is good to go, never change that the entire time she is in.\n* You can check her military entry documents DD Form 4 for Home of Record / Place of Entry.  If any of this list a Florida address on it, she is good to go! It is hard to contest that she was not a FL resident at this point if it is listed on her DD Form 4.\n* You can claim FL residency the same date she became AD if she already had her FL residency established by then.\n\nOn both your taxes, you would file the following:\n\n* File Georgia - Resident for months you were both civilian. I.e. Jan-Jun 2025 (earlier for your wife since she lived in FL)\n* File Georgia - Non-Resident for months you were both military i.e. Jul-Dec 2025 & exempt all income earned during this period from Georgia state taxes (claim as taxes paid to FL).\n* There is no state filing requirement for FL, so nothing to file and nothing going forward.\n\nAlso, in order to make it irrefutable, both of you should register to vote in FL.\n\nReferences:\n\n* [Military Spouses Residency Relief Act | Military OneSource](https://www.militaryonesource.mil/financial-legal/legal/military-spouses-residency-relief-act/)\n* [Military Spouse Income Taxation Under SCRA Timeline of Changes](https://finred.usalearning.gov/assets/downloads/SCRA-Timeline-of-Changes-FINAL.pdf)\n* [Change to MSRRA.pdf](https://www.columbus.af.mil/Portals/39/documents/other/Change%20to%20MSRRA.pdf?ver=2019-01-31-154619-590)\n\nP.S.  Also note, MSRRA applies across the board for State Taxes. Local/Municipality (City) Taxes are different, for you contact your local tax office to see if they offer MSRRA.  My wife worked in different cities throughout our moves.  Some charged city taxes others offered exemptions/refunds.  But these you have to file manually.\n\nAdditionally, going forward not just in VA, whichever state you end up, ensure you file a State Withholding Exemption with your future employers (if in a State-income taxed State).  This will keep your income from having State taxes withheld.  If you don't do this, you are going to have to file State taxes each year to get your refund."
      },
      {
        "id": "o7iisb6",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o7j220y",
        "score": 1,
        "body": "You have a few options, as someone who's navigated part of this with their own spouse. See below link from Mil One Source (great resource btw)\n\nMilitary Spouses Residency Relief Act | [Military OneSource](https://share.google/DxyZFqPRHB9Li2CGE)\n\nThe summary is your spouse can maintain their residency at their HOR, or change it to somewhere they can show intent to reside (buying property, living there, registering to vote, there's a whole list of criteria and while I don't think a defined threshold you generally want to be consistent in where you maintain your residency). \n\nYou as the spouse can choose to set your residency where you are (VA soon), match your spouse (FL if they don't change it, even if you never lived there yourself), or as of 2022 maintain your home state from before you maried. \n\nThis can look odd in practice but you basically just do as much as you can with your resident state. Register and actively vote, maintain your car registrations in that state, my wife actually got a TX driver's license with our GA address on it (not sure if that's something all states can do or if TX is just very accustomed to working with out-of-state military). \n\nYou're an exception to the rule so most DMVs and other state resources might not always get it right, especially when you consider \"DMV\" really means whatever clerk you're talking to that day. Just be informed on the laws pertaining, stay persistent in what you need, and don't hold back on trying again if you just get a dud county worker one call."
      },
      {
        "id": "o7jqv22",
        "score": 1,
        "body": "From a logistical perspective, you can maintain two different states of residence and it's fine BUT it can make preparing your own tax returns more painful if you have to prepare a GA return for yourself while excluding your spouse's income and prepare a FL return for your spouse while excluding yours. It's not impossible, I did it for a few years before the MSRRA revision that let spouses claim their military member's state without establishing a physical presence there.\n\nAlso VA loves to charge property taxes on everything. It's not a hard process but just anticipate that your wife may need to submit paperwork for vehicles to exclude tax collection on them. \n\nFor employers, you will submit a form VA-4 to attest that you are an out-of-state resident in VA solely to be with your spouse on PCS orders. They will stop withholding state income tax from your pay. If you don't submit the form then they will withhold VA income tax by default and then you would get it refunded when you submit your tax return (assuming you do the tax return properly)."
      },
      {
        "id": "o7knnlr",
        "score": 1,
        "body": "I had my husband (he's still AD) change his state of residency to FL before I got out. Otherwise, I'd be stuck paying NY taxes as a dependent (or NC). His HOR is NY, but his state of residency is FL and uses my parents address so we both have FL licenses. Of course, now we're in NC and I contract and my company is playing me telling me they don't do the dependent waiver for state taxes (\\*insert eye roll). I just paid it last year because it was less than a hundred bucks and will just pay it this year. If you have family in Florida, I would highly recommend just both becoming FL residents and if you work in VA make sure you do the dependent tax exemption form. It's literally a thing across the US, but I think my company wasn't familiar."
      },
      {
        "id": "o7keazq",
        "score": 1,
        "body": "So I work full time remote and my employer will remain the same. And their office is in Tennessee (which I go to a few times every year). I'm guessing this mean no VA-4? I did contact Military OneSource this morning and what you said reinforces what the tax expert said. Still working through this. Looks like I'll be establishing my residency as the same as my wife in Florida."
      },
      {
        "id": "o7vlfdx",
        "score": 1,
        "body": "If you work remote, then you'll owe income tax to the state where the income is earned. You can only apply the MSRRA exemption to the state where you are domiciled with your military spouse as a result of military orders (VA).\n\nNote that for tax purposes, there's nothing you need to do to 'establish' FL residency. You are able to keep a GA driver's license and vote in GA even though you are a tax resident of FL.\n\nFunctionally, you should file a married, filing jointly non-resident return in GA to get a larger standard deduction. You exempt all of your husband's mil income and your income gets taxed, which will be at a rate as if you were the single earner of the household.\n\nYou don't file any income taxes in either VA (they have no clue that you earned money since your W-2s will all be sent to GA) or FL (because they have no income tax).\n\nIf you were to quit your job and start working in VA, you would work with your employer to exempt your pay from withholdings due to the MSRRA and claiming FL for tax residency purposes."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rez3gz",
    "title": "Best Credit Card for Active Duty with 0 Credit History?",
    "body": "Trying to find the best credit card for active duty military with zero credit history. I want to build my credit mostly. ",
    "flair": "Question",
    "score": 4,
    "comment_count": 19,
    "created_at": "2026-02-26T03:20:35+00:00",
    "top_comments": [
      {
        "id": "o7gcexn",
        "score": 18,
        "body": "Easy button is a USAA or NFCU simple Cashback card with no international exchange fees."
      },
      {
        "id": "o7jaqgf",
        "score": 6,
        "body": "I always encouraged my Marines to enroll in Navy Federal's cashRewards Secured Credit Card as a first card, for a few reasons.\n\n1. It began the credit line as secured line with a deposit requirement. This helps to ensure that they are recognizing it is ultimately their money that they are spending, and not the banks.\n2. It still gives purchase protections, and cashback.\n3. After 3 months, it gives a credit increase w/o deposit. It then graduates into an unrestricted 2% cashback card after six months + returns them back the $200 deposit they initially made.\n\nI think this probationary period is necessary for young servicemembers who are just starting to learn about credit. Just my two cents. \n\nIf you're a cadet close to graduation, I usually recommend to them the Capital One Student Savor card followed by the Venture X card. Savor functions as a 3% cash-back for dining, groceries, entertainment with no ftx fees and no annual fee. The Venture X card effectively functions as a catch-all 2% cashback card with premium travel protections, no foreign transaction fees + you can submit for an SCRA exemption to the annual fee IF you had the card BEFORE you begin your active duty base date. (If they attempt to apply AFTER they begin active duty, Capital One will DENY their request for an SCRA waiver.) Savor and Venture X work well in combination.\n\nOtherwise, thereafter there are some good cards out like the Chase Sapphire Reserve, Amex Gold and/or Amex Platinum. \n\nJust got to be careful with credit as it becomes a dangerous game for those who don't exactly know how to be afraid of it."
      },
      {
        "id": "o7izcs7",
        "score": 5,
        "body": "It is unnecessary and puts the person into unnecessary debt. A credit card is all it takes to start building credit. And time."
      },
      {
        "id": "o7ge3si",
        "score": 4,
        "body": "NFCU Cash Rewards Plus is my catch all or the flagship would be fine too and I have almost every credit card you can think of. It\u2019s just a great catch all card with good customer service."
      },
      {
        "id": "o7i7hn9",
        "score": 3,
        "body": "I started with the Star Card to use the 10% off first purchase on a washer and dryer. Otherwise, its pretty meh. 10% off exchange restaurants is a good deal too.\n\nI then got the USAA cash back card. Good cash back rate if you buy groceries and gas on base, otherwise also meh, but I got it with almost no credit history (literally that one Star Card purchase a few months before).\n\nYou can use those to build a solid credit history and apply for better cards later. I only have one other card, but having cards that give good benefits for the things you already purchase is the best approach."
      },
      {
        "id": "o7ge96c",
        "score": 3,
        "body": "They do not need a personal loan. They can simply open a basic CC and use it responsibly by paying it off every month."
      },
      {
        "id": "o7gk05s",
        "score": 3,
        "body": "Eventually, this person is likely in the teens or very early 20s and have 0 credit history and probably very little if any financial literacy yet."
      },
      {
        "id": "o7jcb3i",
        "score": 2,
        "body": "I would clarify that SCRA does not apply if they attempt to apply for a Capital One card to waive annual fees while active duty. \n\nIf they had the card before becoming active duty (such as like a Midshipmen, or Cadet, or regular ol' civilian) Capital One will waive additional fees under SCRA if a request is submitted."
      },
      {
        "id": "o7k3ecz",
        "score": 2,
        "body": "It's not weird at all.\n\nI've also been building my credit since I was 18. \n\nWhat you're suggesting isn't necessarily harmful, there are loans intended just for building credit, but it's just unnecessary. You can build solid credit with one card, expanding to two cards after a year or so, and keeping those accounts active."
      },
      {
        "id": "o7g9d0m",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rev2rb",
    "title": "Should I stop contributing to my TSP to pay off debt",
    "body": "tldr: should I stop contributing to my tsp to py off my debt\n\nthis is my first time being in debt and it all just creeped up on me. I hate this feeling I got a spouse who makes about 200k a year but she has spending issues and I have been trying to keep up with is not easy the dinners the dates the little extra things we buy here and there add up. anyway we did talk about it and I told her I am not going to be spending any more money and all my extra cash will go to paying off my debt and if she wants to go out or do anything she'll either have to do it herself or pay for everything. she was understanding so thats good.\n\nI got a total of 23k of debt a mix of credit cards and loans all credit cards are at 4% apr i got 2 loans from affirm at 35% (i know i know) and a car loan at 9%.\n\nI have been contributing $330 (10%) of my pay to my tsp.\n\nI will be adding more to my credit card soon too since I I PCSing and ill have to buy all brand new things like pots pans and everyday items since my spouse can not move due to work so ill be geobatching. I feel like im slowly drowning and I am thinking of just stop contributing to my tsp until I at least pay off half my debt. \n\nas of now I have about an extra $900 after all expenses to do whatever with. so thats going to paying down my debt if I stop contributing to my tsp ill have 1.2k extra.\n\nif anyone has ever been in a similar situation I would appreciate some advice.",
    "flair": null,
    "score": 11,
    "comment_count": 20,
    "created_at": "2026-02-26T00:24:25+00:00",
    "top_comments": [
      {
        "id": "o7fhps1",
        "score": 30,
        "body": "Keep at least 5% going toward TSP to keep the match - you make more money from the match than you lose by accruing interest. I would recommend reducing to that 5% to pay off the affirm loans, and also probably until you pay off the car loan, as well. The credit cards at 4% are not a big concern - by the time you get around to focusing on them, you are probably better off returning to a higher TSP contribution rate.\n\nFinally, your relationship is your own, but I\u2019d recommend seeing if you two can get a sit down with a financial counselor to figure out your budget and set things straight. It seems like you\u2019re mostly keeping finances separate, which is obviously your business, but having knowledgeable third party input may help you two come to an even better way of doing things."
      },
      {
        "id": "o7fkjol",
        "score": 24,
        "body": "Are you in the BRS? If so, don't go below 5%. 100% return on your money is still better than whatever the interest rates are.\n\nBesides that, you two really need to sit down and get this under control. $200k income (plus yours) has no reason being in debt. The #1 reason for divorce is financial problems, and that seems like where this is headed. Seek counseling if you need to. \n\n\"If she wants to go out\" isn't an option. You both either get on the same page with paying off this debt, or don't. "
      },
      {
        "id": "o7fg89q",
        "score": 7,
        "body": "Because those two loans have such a high APR, I would stop all contributions and get those handled. After that, would start contributions back up. 9% is still high, but not outrageous."
      },
      {
        "id": "o7fmnb5",
        "score": 6,
        "body": "I would assume he\u2019s BRS if 10% is only $300 and his base pay is 3k he\u2019s an E3-E4.\n\nOP you\u2019re not a typical military family income. Theres no reason you guys should be in this much CC debt.\n\nYou guys need to get on the same page about this and realize you both are married (in my opinion once you\u2019re married everything should be combined and goals become one even if it is a personal goal the other person should be on board). \n\nYou guys can clear this in 6 months easily if you both can get serious and both be on board. \n\nSeek some couples counseling as well."
      },
      {
        "id": "o7ffmsn",
        "score": 3,
        "body": "At the beginning of our marriage & investment journey, I reduced the contributions, but didn\u2019t stop it completely. I even opened other retirement accounts later & put some rather than none all the while still knocking down debt. I\u2019d focus on those higher percent interest loans first! Snowball those payments once you pay one off, move it on to the next & so on. Good luck."
      },
      {
        "id": "o7fvfbv",
        "score": 3,
        "body": "You have a hole in your bucket.. you\u2019re trying to fill your bucket but you\u2019re losing water quicker than what you can put into it. Fix the leak."
      },
      {
        "id": "o7fly13",
        "score": 2,
        "body": "If you\u2019re BRS I\u2019d drop my TSP to 5% to keep the match. Then aggressively pay off your 35% affirm loans, those are killer. Depending on how long that takes, watch out for interest rate changes on your credit card and continue working down your car and credit cards. I\u2019d consider 9% on a car loan also fairly high and would pay it down before ramping up my TSP. \n\nI\u2019m glad you\u2019re talking finances with your spouse. It can be a major factor for divorce so keep being honest with each other and open about your concerns. You\u2019ve got a good plan, stick to it and get out from under this debt."
      },
      {
        "id": "o7jealj",
        "score": 2,
        "body": "Here's the initial roadmap for how you should prioritize any incoming money: \n\n1. Emergency fund of $1000 to cover deductibles.\n2. 5% TSP Matching\n3. High interest debt (debt above 9+%)\n4. Emergency fund of 3-6 months expenses.\n\nIf I might add for your moving woes, I HEAVILY suggest to look into used furniture goods rather than trying to buy everything brand new. You will find many families who are PCSing that are dying to get rid of items they don't need or want. Check Facebook marketplace or with local military groups that have items they are trying to get rid of.\n\nThe reason why the matching is important has to do with it basically being a 100% guaranteed rate of return of up to 5% of your money. Unless you somehow have debts that annualize over 100% APR, then that's basically free money you're throwing away.\n\nHope this helps."
      },
      {
        "id": "o7g9ixl",
        "score": 2,
        "body": "E4 actually but yeah we talked we are good and we have a plan now its just figuring out how i'll go about it. Which i got from everyone's comments I think i'll keep my contribution at 5% and use the rest tk pay off my debt."
      },
      {
        "id": "o7gdmq4",
        "score": 2,
        "body": "That\u2019s great! \n\nYes, I would still at least do the 5%. CC debt is insanely bad just focus on knocking that all out asap and then get back to TSP. \n\nIf she truly makes $200k in all taxable income plus yours then you guys should both be contributing to Traditional TSP to reduce your tax bill now. \n\nA few questions.\n\nIs her job/career stable and is it extremely likely for her income to stay like this for a long period? \n\nIs her job dependent on location? If so, will you be getting out when contract ends? \n\nWere you guys together prior to the military, if so what made you join?"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1ret8y8",
    "title": "Southwest credit card",
    "body": "Does anyone have a Southwest credit card as the primary cardholder and have the annual fee waived? I just called and the agent told me the fee is only waived for the service member but everything online says its for the spouse too. I know the internet isn't always accurate but if the agent was wrong I'd like to know because it'd be easier for me to manage it in my name with him as an authorized user \ud83d\ude05",
    "flair": "Question",
    "score": 2,
    "comment_count": 26,
    "created_at": "2026-02-25T23:12:01+00:00",
    "top_comments": [
      {
        "id": "o7f43yd",
        "score": 5,
        "body": "It\u2019s MLA policy. My wife and I have half a dozen chase cards each. If you are going to simply call again why bother asking here? Someone making 20-25 an hr as a CSR does not know all the nuances of the largest corporate banks MLA waiver policies. \n\nIf your spouse is in the MLA database- she is waived just like you are."
      },
      {
        "id": "o7f20ds",
        "score": 4,
        "body": "Its service member and spouse"
      },
      {
        "id": "o7f2xbt",
        "score": 4,
        "body": "Agents are not always correct"
      },
      {
        "id": "o7f2k2t",
        "score": 3,
        "body": "While I don\u2019t have the Southwest Credit Card, I know that Southwest CC is powered through Chase, and Chase gives the waived fees to the service member and the spouse. Same with AMEX."
      },
      {
        "id": "o7f4n2w",
        "score": 2,
        "body": "Did you have it opened before you got married or after you got married? \n\nIf before marriage, the card with spouse as primary (no AD spouse) does not qualify. \n\nIf you got it after you got married, it should count, especially if you add the AD spouse."
      },
      {
        "id": "o7fs3vp",
        "score": 2,
        "body": "I believe that! The only reason im considering it is for the free companion pass offer right now. SW is around the same price (~500-600$) per person as the other airlines that fly where we'll need to go the next 3 trips so I think it would be worth it to save at least $1000 \ud83e\udd74"
      },
      {
        "id": "o7f92l8",
        "score": 2,
        "body": "Oh....I guess I won't call then\ud83e\udd2d"
      },
      {
        "id": "o7f15iz",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o7f8iy1",
        "score": 1,
        "body": "I\u2019ve had my SW card a long time and still pay the fee, I\u2019ll have to call them."
      },
      {
        "id": "o7g0pnn",
        "score": 1,
        "body": "I have a SW card through Chase with no fee"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1ressyu",
    "title": "Unsure if AMEX will waive my Platinum Card Fee",
    "body": "I am a military spouse, and in the card membership agreement,t it acknowledges me as a covered borrower under the military lending act. However, every time I call them, they proceed to say they cannot guarantee that it will be waived and I will have to wait till my first billing statement to see if it is. The problem is, if its not waived and they won't waive it I want to cancel this card. My first billing statement won't come out until after the 30-day cancellation. Do I keep calling and annoy them enough to give me a straight answer or is this one of those things that they cannot give me a straight answer because it is a liability? Should I calm down and just breathe?   ",
    "flair": null,
    "score": 0,
    "comment_count": 12,
    "created_at": "2026-02-25T22:55:22+00:00",
    "top_comments": [
      {
        "id": "o7eyoj1",
        "score": 7,
        "body": "If it says you\u2019re a covered borrower you will get the fee waived. No need to stress or call them anymore."
      },
      {
        "id": "o7gyf6e",
        "score": 4,
        "body": "> Do I keep calling and annoy them\n\nMy lord in Christ.. they don't owe you an answer. If AMEX eventually decides to stop waiving fees under the MLA, it's going to be because an army of entitled people like you finally broke their CS department and they decided their favorable interpretation of the MLA language needs to change. \n\nKnow why other banks like Capital One don't waive their fees under MLA? Because they simply decided not to. \n\nPeople need to understand what they're fucking around with before they play games with almost $1,000 annual fee cards.\n\nYou're going to ruin this for the rest of us. I'm going to link this post in my routine rants to this sub to STOP MAKING AMEX's CSR DEPT MISERABLE."
      },
      {
        "id": "o7exzvu",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o7eymfo",
        "score": 1,
        "body": "[removed]"
      },
      {
        "id": "o7ez3s2",
        "score": 1,
        "body": "I've got a card (active duty) and my spouse has one too. We don't pay the fee at all."
      },
      {
        "id": "o7kqu8p",
        "score": 1,
        "body": "Referral links are not allowed on this subreddit, thanks."
      },
      {
        "id": "o7f09ai",
        "score": 0,
        "body": "My civilian wife got 5 Amex Plat. I got 5 too. We got 10 to splur on the benefits. Customer support rep doesn't have the correct answer.\n\nThe answer is in your agreement with the word \"Covered Borrower\". You're waived. Why are u worrying? Lol. Relax & enjoy."
      },
      {
        "id": "o7fzxpd",
        "score": 0,
        "body": "There is an SCRA/MLA database where you can verify. The site is clunky but it will generate pdf letter of proof that you're covered"
      },
      {
        "id": "o7f9uke",
        "score": -1,
        "body": "I'll take your word for it, must have been reading it wrong. So yeah, I'm still young, would rather be overly cautious then mess up big time."
      },
      {
        "id": "o7f3vlg",
        "score": -2,
        "body": "Thank you!"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1reow8i",
    "title": "Retirement pay",
    "body": "just wanted to clarify.\n\nI retired 1 Feb and don't think I'm getting paid my first retirement check tomorrow. if they get me squared away next week, will they pay out then, or just double up April's check?\n\ntia",
    "flair": "Question",
    "score": 2,
    "comment_count": 20,
    "created_at": "2026-02-25T20:29:57+00:00",
    "top_comments": [
      {
        "id": "o7e5y9m",
        "score": 2,
        "body": "Whenever they're done with it."
      },
      {
        "id": "o7ffgxp",
        "score": 2,
        "body": "Once it\u2019s all figured out you\u2019ll get your Feb retirement pay, regardless.  Then you\u2019ll get your next retirement payment April 1.  Regardless, you started earning retirement pay Feb 1.\n\nIn my experience, I got a few automated DFAS emails around the first of the month and my pay actually came around the 5th, the following month it came on time."
      },
      {
        "id": "o7e3hjl",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o7e4m21",
        "score": 1,
        "body": "You'll get backpaid. And VA won't be earned until March, paid in April (or backpaid later, if you don't have your rating yet)\u00a0"
      },
      {
        "id": "o7e4wml",
        "score": 1,
        "body": "Dunno but I\u2019ll offer a relevant anecdote:  A buddy retired 1 Jan and got his first retirement check on 1 Feb. His VA BDD claim took another few weeks but it was backdated to January."
      },
      {
        "id": "o7eqtk9",
        "score": 1,
        "body": "The earliest you will receive retirement check will be 1 MAR, but depending on processing time and them verifying there weren't any overpayments that needed to be cleared it might not hit until 1 APR.  In very rare instances it will take even longer, but again rare.  This is why a really solid emergency fund is important to get people through several months.  "
      },
      {
        "id": "o7g0908",
        "score": 1,
        "body": "I'm in the same boat as you, so we will see \ud83e\udd23. Got my DFAS Smart Docs Retirement emails that work ID was completed at the end of January, should be on time for 27 Feb payday. If not, waiting till 1 April lol"
      },
      {
        "id": "o7samv3",
        "score": 1,
        "body": "I retired 1 Feb as well.\n\nI received my retired pay on 23 Feb.\n\nI am still missing my last Jan EOM AD paycheck.  Probably because my terminal leave didn't get closed out until Mid-Feb.  Don't know if it is my local CPTS or what, but all leave processing has always been delayed.\n\nI haven't received my BDD yet."
      },
      {
        "id": "o7e5ft2",
        "score": 1,
        "body": "So backpaid on 1 April ?"
      },
      {
        "id": "o7erd54",
        "score": 1,
        "body": "I get that. I'm not getting 1 march cause they're still determining my top 3 shizz.\n\nI'm guessing, if all gets worked out, I should get paid double 1 April.\n\nBut didn't know for sure, like if they finished everything 5 March, would they cut the first check then, or double up for April.\n\nI get there are and can be delays."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rd2d4k",
    "title": "Google Sheet Share: Cost of Thriving Index (COTI), 2026 Inflation Adjusted, Retirement Comparison",
    "body": "Hi all, 20-something years in, retirement-eligible Army guy here. I came across the Cost of Thriving Index (COTI) ([https://americancompass.org/2023-cost-of-thriving-index/](https://americancompass.org/2023-cost-of-thriving-index/)) which is a pretty interesting way to judge what it *really* takes to live (and thrive) in specific locations. They offer an excel data workbook download from the linked page.\n\nWith that workbook, I imported inflation data to bring their 2022 numbers up to 2026. Not perfect, I know, as the inflation index varies by item category, but probably close enough.\n\nI created this workbook (https://docs.google.com/spreadsheets/d/1kzdtW0unu5GTwDbqcSEdpRmFACVjNRgubICCnusUeVU/edit?usp=sharing) which you can access as view only. If you want, you can duplicate it to your own google drive and plug your retirement income into cell M2, and you will see a surplus / deficit calculation for each location in the spreadsheet.\n\nOr, if you don't want to duplicate the doc, you can just look at column K (COL SUM 2026 Adjusted) to see the COTI for each location adjusted to 2026 dollars.",
    "flair": null,
    "score": 28,
    "comment_count": 7,
    "created_at": "2026-02-24T02:29:28+00:00",
    "top_comments": [
      {
        "id": "o72i3zp",
        "score": 5,
        "body": "Seriously impressive.  Thank you for your efforts here."
      },
      {
        "id": "o72ljm5",
        "score": 2,
        "body": "I don't see taxes factored in here. Is it part of the calculation somewhere and I missed it?"
      },
      {
        "id": "o779usl",
        "score": 2,
        "body": "There's a lot wrong with the website's methodology (just use PCE), and clearly bias they are out to prove, but anyway...\n\nYou shouldn't adjust for inflation from 2022 because military pensions are adjusted for inflation every year and your typical 4% retirement account withdrawal strategy includes giving yourself inflation raises. If you did the math right, your COTI would not change from 2022 to 2026, as you don't have access to the price data COTI is using after that year and instead are substituting the already known CPI."
      },
      {
        "id": "o72q6b1",
        "score": 2,
        "body": "No, I don't think you missed anything. I didn't factor in taxes, and from my reading of the COTI methodology, it doesn't seem that they did either. I think they operated on the assumption that wages are post-tax? Not sure. State taxes on retirement income would be a good addition to this worksheet. I might get to that this next weekend. Thanks for the suggestion."
      },
      {
        "id": "o72qmkr",
        "score": 2,
        "body": "Thanks, appreciate the effort here"
      },
      {
        "id": "o72eyrb",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o78k2lp",
        "score": 1,
        "body": ">You shouldn't adjust for inflation from 2022 because military pensions are adjusted for inflation every year and your typical 4% retirement account withdrawal strategy includes giving yourself inflation raises.\n\nThat's valid, their index calculation wouldn't change. I applied the inflation factor to their raw numbers (their estimate of cost of living in dollars), and not the index, which *is* required in order to compare a 2026 pension to dollar figures calculated in 2022.. I think my wording might have been confusing."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rd1zk7",
    "title": "What was the best financial decision you made?",
    "body": "",
    "flair": "Question",
    "score": 26,
    "comment_count": 78,
    "created_at": "2026-02-24T02:12:38+00:00",
    "top_comments": [
      {
        "id": "o72cb0o",
        "score": 139,
        "body": "Joined the military"
      },
      {
        "id": "o72cjpr",
        "score": 65,
        "body": "I don\u2019t like to brag but my beanie baby investment gonna be worth more than gold"
      },
      {
        "id": "o72edj1",
        "score": 65,
        "body": "Controlling lifestyle creep."
      },
      {
        "id": "o73329h",
        "score": 49,
        "body": "Marrying a loyal woman who loves the challenge of stretching a dollar."
      },
      {
        "id": "o72gcle",
        "score": 42,
        "body": "1- Education resulting in better pay\n\n2- Investing as much as possible as early as possible, and just leaving it alone in a ROTH ROTH ROTH lifecycle fund\n\n3- not buying a bunch of dumb shit that I don\u2019t need (depreciating assets)\n\nHow many guys do you see commuting in a compensator truck or some other flashy car, but no TSP? What\u2019s the point. Your friends don\u2019t care, they don\u2019t even really notice.  Even if somehow your buds were impressed by your yet-another-huge-truck, y\u2019all are gonna PCS in a couple years. Who are you trying to impress? Women don\u2019t care, at least not the ones you should care about. For that once in a blue moon that you need a truck you can rent one for like $50."
      },
      {
        "id": "o72e1f4",
        "score": 31,
        "body": "Tsp contributions, pay future self first"
      },
      {
        "id": "o72ghvo",
        "score": 29,
        "body": "By dumping their high school savings in Apple"
      },
      {
        "id": "o76f7fj",
        "score": 28,
        "body": "Joining the military and buying a house at 23 with no money down.  Then selling it 4 years later for 150k profit."
      },
      {
        "id": "o72wwkt",
        "score": 28,
        "body": "Annual raise, up tsp. Another year in, up tsp. Promote, up tsp. Leave no extra money to creep with."
      },
      {
        "id": "o73k2kl",
        "score": 25,
        "body": "Not having to pay for a divorce is a big one."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rd0uyb",
    "title": "Debt collection from Army",
    "body": "I received a debt notification from DFAS saying I owe $4,600 in debt. I got out in 2022, this looks like my retirement/401k I pulled out. I paid a penalty on it because I believe the amount was more like $5600 but what the heck? Am I missing something? It\u2019s my retirement money that I pulled out and paid the penalties on for cashing it out. ",
    "flair": null,
    "score": 7,
    "comment_count": 7,
    "created_at": "2026-02-24T01:31:07+00:00",
    "top_comments": [
      {
        "id": "o725ugk",
        "score": 12,
        "body": "This is not your TSP.\n\nIt's a debt that you owe from an audit."
      },
      {
        "id": "o72u2nk",
        "score": 7,
        "body": "It is not your TSP, they over paid you.  The TSP money at that point had already been contributed into a separate retirement account."
      },
      {
        "id": "o759tlc",
        "score": 2,
        "body": "no it\u2019s his TSP man he said it"
      },
      {
        "id": "o724vvk",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o7a6scl",
        "score": 1,
        "body": "Thats an audit. Stepdad died in May of 2024, still screwing with them on a final audit bill of 12k"
      },
      {
        "id": "o797uxs",
        "score": 1,
        "body": "Update: it wasn\u2019t my TSP, it was my final payout plus my leave balance being paid to me. My bank statement says I was paid the 23rd and DFAS is saying I was paid the 24th. A day after my no pay status went into effect. So it must\u2019ve flagged their system. I\u2019m ignorant I\u2019ll admit it"
      },
      {
        "id": "o7289g0",
        "score": -4,
        "body": "It is my TSP, for more context it reads. 1 NPT debt is due to payments received after you entered a no pay status due to separation as of 06/23/2022. These payments are as follows: separation payment dated 06/24/2022 for 4,633 \n\nThese payments first date is the day I got out of the military. I guess pulled my TSP out a day later and that was a day after I entered a no pay status???? But why would I enter a no pay status due"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1rcpquq",
    "title": "VETERANS UNITED PROCESS",
    "body": "Hello all,\n\nI am currently selling my home to a buyer who is using a VA loan and going with Veterans United. We went under contract 2/19 and are scheduled to close on 3/26. I went with their offer becuase it was in line with others and because my brother was having issues buying due to VA loan misconceptions. I grew up with many of my family members in the military and want to help out. I need a bit of help with the process.\n\n1. When does the Loan officer order the appraisal after the signed agreement? plus when does it get finished?\n\n2. My home is in great shape, I just sanded and prepped to paint the chipping/ flaking areas, that is all I think I will need to do to pass MPR's. unless others have ideas?\n\n3. Is the timeline realistic for the buyers and myself?\n\n4. How many VA loans appraise under value? The local comps are a bit less than my sale price.\n\n  \nPlus any tips you can give me to help reach the finish line with my Veteran buyer would be appreaicated.",
    "flair": null,
    "score": 1,
    "comment_count": 13,
    "created_at": "2026-02-23T18:36:38+00:00",
    "top_comments": [
      {
        "id": "o6zvkft",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o703g5x",
        "score": 1,
        "body": "[removed]"
      },
      {
        "id": "o720vpm",
        "score": 1,
        "body": "Thank you!"
      },
      {
        "id": "o75odz0",
        "score": 1,
        "body": "First off\u00a0 props to you for taking the VA offer. A lot of sellers still shy away from VA just because of old myths, so that\u2019s cool of you. Let me break this down in plain English.\n\nWhen does the appraisal get ordered?  \nUsually once the contract is signed and the buyer has completed their initial loan paperwork, the lender orders it pretty quickly typically within a few days. Most VA appraisals come back in about 7\u201314 days depending on the market. Your 2/19 contract with a 3/26 close is very normal. That\u2019s a standard VA timeline if everything moves the way it should.\n\nOn the MPR stuff (VA property requirements)  \nVA isn\u2019t looking for a perfect house. They\u2019re looking for safe and livable. Peeling or flaking paint is one of the most common things they flag, so the fact that you already handled that puts you in good shape. Beyond that, they\u2019re mainly looking for obvious safety issues broken windows, roof problems, exposed wiring, that kind of thing. They\u2019re not nitpicking cosmetic stuff.\n\nIs the timeline realistic?  \nYes. Totally realistic. Most VA deals close in about 30\u201335 days. When they don\u2019t, it\u2019s usually because of paperwork or communication not because it\u2019s VA.\n\nHow often do VA loans appraise low?  \nNot more often than conventional in my experience. An appraisal is an appraisal it\u2019s based on comps, not loan type. If it does come in under, there\u2019s something called Tidewater where agents can submit additional comps before the value is finalized. So there\u2019s a built-in buffer there.\n\nTips to get to the finish line smoothly:\n\nIf the appraiser notes something small, just knock it out quickly. Stay in touch with the buyer\u2019s agent. Don\u2019t stress over VA horror stories you read online. Keep everything as-is until closing.\n\nVA loans are actually really solid financing when the lender knows what they\u2019re doing. You\u2019re probably going to be just fine. And again good on you for helping out a Veteran buyer."
      },
      {
        "id": "o77i4c7",
        "score": 1,
        "body": "1) usually it\u2019s ordered right after initial docs are signed. And It comes back 10-14 days later\n2) just wait for the appraiser to come out. The only other thing that usually is added is a handrail if there are a lot of stairs. \n3) my turn around time for va is usually 30 days so you\u2019re good! \n4) if it appraises below it\u2019s called a tidewater and they inform the LO and then the agents should find comps to justify why the home should be worth more. \n\nAs long as they send documents into the LO quickly they should close quickly."
      },
      {
        "id": "o70elj1",
        "score": 1,
        "body": "Thank you for responding! I am trying to make sure this goes as smoothly as possible for both parties. I am going to be extremely available to the lender if need be, just hope my listing agent communicates in a timely manner. Is VU generally quick with turn and how long until the apprasier shows up at my place?"
      },
      {
        "id": "o7761hj",
        "score": 1,
        "body": "Thank you for the great response. I\u2019m almost finished with painting. I cut out the rotted window sill and replaced that as well for the buyer. I have not heard word on when the appraisal is scheduled or anything from my listing agent. I hope it gets scheduled soon since I read that in the Midwest it\u2019ll take 15 days or so. I just don\u2019t want there to be an issue for myself or the veteran"
      },
      {
        "id": "o77qi2k",
        "score": 1,
        "body": "Thank you for the response. When it\u2019s ordered, how long does it take for the appraiser to come out?"
      },
      {
        "id": "o77qunt",
        "score": 1,
        "body": "It\u2019s pretty quick usually. Depends on the appraisers schedule but you have time!"
      },
      {
        "id": "o7828ez",
        "score": 1,
        "body": "I\u2019m just nervous I won\u2019t have enough time to do the repairs before the closing date. If there are any. Any way to know if the appraisal has been ordered?"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r9zxj6",
    "title": "Early TSP Withdrawal After Separation",
    "body": "Context: I just finished my 6 year obligation in the reserves and have dropped to the IRR. My TSP has just shy of 12K in it as of today and after what TSP withholds for taxes I\u2019d be able to withdraw a little under 11K (I\u2019d pay the 10% penalty and state taxes on my filing for 2027). My current career offers a differed comp plan on top of the normal retirement with a 100% match that I contribute to every check. I can also pull from my primary retirement at 49 years old vs. 59.5 with TSP. \n\nQuestion: I\u2019m currently building a home on a plot of land I inherited. The extra 10K or so from an early withdrawal not on a loan with interest would be a major benefit for me at this time. I have absolutely 0 plans to go back into federal employment so the TSP will no longer be contributed to. I know I can roll it into an IRA but this isn\u2019t as appealing to me since I have a very solid retirement through my employer. I have to wait 7 days for TSP to verify my account for direct deposit so I wanted some options before I pull the trigger. In this case could it be a good idea to do the withdrawal to save myself on the loan and dodge interest??",
    "flair": null,
    "score": 0,
    "comment_count": 19,
    "created_at": "2026-02-20T16:26:05+00:00",
    "top_comments": [
      {
        "id": "o6g3dcy",
        "score": 23,
        "body": "No, it is never a good idea to pull from your TSP/401k. That should be an absolute last resort to you being homeless, not a want.\n\nDo not do this. Just leave it in the TSP or roll it over to an IRA."
      },
      {
        "id": "o6g6355",
        "score": 16,
        "body": "Yes? You don't just withdraw your retirement savings because you got a new job."
      },
      {
        "id": "o6g7jkv",
        "score": 11,
        "body": "You can absolutely leave it in the TSP, and likely should for the access to the G fund in retirement."
      },
      {
        "id": "o6g3s6v",
        "score": 4,
        "body": "The answer to your question, with a lot of facts that aren't relevant, that you'll get here is a resounding \"no.\" I'd personally take the loan vs the withdrawal with penalties and taxes. \n\nLet's rephrase it - would you take 10k early from your current retirement plan, because that's the same question, just reframed."
      },
      {
        "id": "o6g7qo7",
        "score": 3,
        "body": "It's also a no from me. TSP C, S, and I funds are pretty good. Look at it like this you have 12k in a  diversified account waiting for you to hit 60. Do the math if your account doubles ever 7 years. If you are 26 and it doubles ever 7 years at age 61 that's over 350k."
      },
      {
        "id": "o6g6eo3",
        "score": 3,
        "body": "Your first comment answers your question. It doesn't matter if you're contributing or not. You're getting tax deferred (traditional) or tax free (roth) growth vs paying 10% in penalties and xx% in taxes. In other words, the loan you'd have to take better be at ~20% or more interest because that's your cost if you cash out."
      },
      {
        "id": "o6g7s90",
        "score": 3,
        "body": "Gotcha maybe I misunderstood then. The person I got when I called with questions wasn\u2019t super helpful I\u2019ll do some more research."
      },
      {
        "id": "o6gl1i1",
        "score": 3,
        "body": "One thing to add that many people don't realize is most 401k plans do not allow you to roll money into the plan unless you're an active participant (as in currently working for them).  \n\nTSP is fairly unique in that they will always allow you to roll money in as long as you keep the account open.  \n\nSo in your current position this may not be something you care about, but for any jobs you hold in the future (and then subsequently leave), TSP is a great retirement account aggregator.  \n\nI personally rolled all Roth out, because I wanted it in my IRA (for the numerous benefits that offers). But I kept my Traditional in TSP (because I'm right around the Roth IRA income limits, it's very competitive with most private sector 401k's, and it works well for future account aggregation)."
      },
      {
        "id": "o6gow1l",
        "score": 3,
        "body": "Correct.  \n\nRollovers are not contributions, you can continue to roll money into TSP from other eligible accounts even when you're not an employee. Most employers don't allow rollovers in once you separate from the company, TSP does."
      },
      {
        "id": "o6gtgjn",
        "score": 3,
        "body": "Yup take my upvote I misread and misunderstood.\u00a0"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r7ljm3",
    "title": "Tsp advice",
    "body": "",
    "flair": null,
    "score": 1,
    "comment_count": 10,
    "created_at": "2026-02-17T22:51:24+00:00",
    "top_comments": [
      {
        "id": "o5yelba",
        "score": 6,
        "body": "L 2075 and chill. It is 99% in stocks, approximates the global stock market pretty well, and it maintains your allocation for you all for only 0.037% per year. That's only $3.70 per $10,000 invested. It will stay 99% in stocks until October of 2047 so you won't have to even think about it for a long time."
      },
      {
        "id": "o63b0ed",
        "score": 2,
        "body": "[removed]"
      },
      {
        "id": "o5y8yxw",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o5yb26m",
        "score": 1,
        "body": "If it was me, I would personally swap the S (small/mid-size U.S companies) and I (International stocks) contributions; maximize domestic growth exposure while keeping some global diversification."
      },
      {
        "id": "o5yy71v",
        "score": 1,
        "body": "I\u2019ve been seeing a lot and agree with that, I\u2019ve just seen mixed opinions. But I definitely am considering just putting my money into the L 2075. For that would you recommend putting all money currently invested into the L Fund or just new money being invested per month ? If that makes sense"
      },
      {
        "id": "o644niq",
        "score": 1,
        "body": "No self promotion, advertising, or spam on the subreddit. Thank you."
      },
      {
        "id": "o5yyc51",
        "score": 1,
        "body": "I have it that way because how the International market has been fairing"
      },
      {
        "id": "o5yyvca",
        "score": 1,
        "body": "Once you decide on an allocation, I think it makes sense to change everything to that allocation, especially in a qualified account like the TSP where you don't have to worry about tax implications. I have 100% of my current holdings and 100% of my contributions in L 2075."
      },
      {
        "id": "o5zh7y0",
        "score": 1,
        "body": "This is the same reasoning I have in going to mainly VT with a sprinkling of VYMI vs VTI and VYM in ETFs. While the magnificent seven are keeping the US markets afloat, it's pretty likely that current domestic economic policies are having lasting effects raising a need for international exposure. \n\nWith this said, I'm a 70 C, 15 S, 15 I, but have been this way since 2004."
      },
      {
        "id": "o5z30tt",
        "score": 1,
        "body": "That makes sense thank you a lot for your insight"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r6tfr6",
    "title": "How much should I be saving?",
    "body": "I\u2019m at about 1.5 years in. E-3. \n\nI currently have 5.3k in a HYSA with Amex\n\nI also have around 6k+ in my Roth TSP that I just bumped up to 30% contribution.\n\nI was putting 19% in my tsp and 45% of my net pay in the HYSA. Now it\u2019s 30% and 20% \n\nI have a car with no payment and no debts. \n\nIn 6 months im about to go OCONUS for 3 years and sell my vehicle as well. (So the bonus of COLA pay and my job also gets per diem and commrats)\n\nMy issue is that I feel like after my bills, mostly subscriptions (WiFi, Xbox, Spotify, gas, etc.) and insurance I\u2019m at about 250$ per paycheck to spend on fun which doesn\u2019t go far in SoCal.\n\nAs a 19 year old, would you prioritize fun until PCS, then save more  or would you keep aggressively saving? And how would you save the money? Mostly TSP? Even it out with the HYSA?  Another form of saving?",
    "flair": "Question",
    "score": 17,
    "comment_count": 25,
    "created_at": "2026-02-17T02:13:05+00:00",
    "top_comments": [
      {
        "id": "o5syl2o",
        "score": 25,
        "body": "You are CRUSHING the savings rate.  I did as well and looking back I was able to retire as an e6 at age 38 but I do wish I'd have lived a tiny bit more in my prime years."
      },
      {
        "id": "o5sp1ws",
        "score": 9,
        "body": "Keep a small emergency fund in HYSA (3-6 months expenses depending on risk tolerance and potential expenses), maximize Roth TSP and regular Roth, then trickle excess savings into other tax advantaged plans or taxable brokerages. There\u2019s a sweet flowchart on r/bogleheads that breaks it down somewhere. Building these habits now will be huge for your savings when you start getting pay increases down the line."
      },
      {
        "id": "o5umjbc",
        "score": 5,
        "body": "Invest in self-development. What education and training will set you up for success later in life? \n\nYou are crushing it and well beyond the financial experience of your peers. No issues with the HYSA or TSP. Consider opening a Roth IRA and maybe a brokerage account once your income increases. \n\nHowever, start planning long term from a career perspective. Shorter term, travel on a budget while OCONUS and take advantage of the overseas financial benefits. Any TDY opportunities to a CZTE?"
      },
      {
        "id": "o5va61g",
        "score": 5,
        "body": "100% stocks"
      },
      {
        "id": "o5v2nz0",
        "score": 5,
        "body": "As a single junior enlisted with no kids, it's definitely sustainable."
      },
      {
        "id": "o5vapuf",
        "score": 4,
        "body": "Not familiar with czte. What\u2019s that"
      },
      {
        "id": "o5vyu67",
        "score": 4,
        "body": "Roth IRA gives you access to higher growth stocks than the \u201cC\u201d, \u201cI\u201d ect which you should take advantage of since you\u2019re 19 and your risk tolerance should be very high. So yes max your IRA and do as much as you can past threshold for matching reasonable in your Roth TSP and your expenses/savings plans."
      },
      {
        "id": "o5unqer",
        "score": 3,
        "body": "My question would be more how are you investing those savings. In the TSP and Roth are they set to bonds or stocks? As for high yield savings that should be your emergency fund money and operational liquidity. Everything else should be invested into assets honestly to hedge against inflation since the money printer goes BRRRRT."
      },
      {
        "id": "o5v3uu4",
        "score": 3,
        "body": "First, read the pinned comment, and understand it well. It actually answers your questions pretty thoroughly.\n\n>As a 19 year old, would you prioritize fun until PCS, then save more or would you keep aggressively saving?\n\nYou can both save and have fun. Fun doesn't have to cost a lot of money. For example, when I was stationed in Colorado, there was a junior enlisted program where they would give you ski/snowboard rentals, drive you to the mountain, drive you back, and include the lift ticket, for like $60 bucks. I did this at least 4 times every winter.\n\nJust don't spend all your money on booze, restaurants, nicotin, etc and you'll always have plenty of money.\n\n>would you keep aggressively saving? \n\nAs a junior enlisted, I was putting 60% of my paycheck in the TSP (~$1k). I was putting $600/month towards my student loans. My car payment and insurance totaled $300/month. I lived on half my BAH (2 roommates). My savings account still increased each month. I still had tons of fun. It might be tougher now, especially if you are stationed in a HCOL and inflation, but you should be able to have fun and save a shit ton. You have few expenses.\n\n>And how would you save the money? Mostly TSP? Even it out with the HYSA? Another form of saving?\n\nRead the Military 101/Prime Directive link in the pinned comment. TSP match, max Roth IRA, and then I personally would dump as much into the TSP as you can. Your taxable income is so low as a junior enlisted - you're not likely to make so little ever again, even in retirement. After 3 years AD, I had $30k in my TSP, and that was with most of the first year only putting in $200/month."
      },
      {
        "id": "o5zp4s1",
        "score": 3,
        "body": "[removed]"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r6oyuz",
    "title": "Spouses Amex annual fee not waived",
    "body": "I\u2019m on active duty. Amex has never not waived my fees and I have 9 cards with them. My wife has opened a few Chase cards over the last couple of years and they\u2019ve always waived the fee without having to request it. They just know she is my dependent when she applies. She recently opened 3 American Express cards and the fees were not waived. Has anyone seen this before?",
    "flair": "Question",
    "score": 8,
    "comment_count": 72,
    "created_at": "2026-02-16T23:01:18+00:00",
    "top_comments": [
      {
        "id": "o5rqkfz",
        "score": 48,
        "body": "how many cards??? jesus"
      },
      {
        "id": "o5rrk4a",
        "score": 46,
        "body": "Did you ask Amex why before coming here? Several years ago when I got my Amex Platinum, I had to go into a specific section of my profile to apply for the SCRA/MLA benefits nullifying the annual fee. Maybe she needs to do the same, or maybe they don't have her info on file. Either way, the only way to get this resolved is to contact Amex."
      },
      {
        "id": "o5s1beq",
        "score": 27,
        "body": "When you leave active you wait until the annual fee hits and downgrade it to a no annual fee card if it\u2019s not worth it. If there is no option for no annual fee cards (like with platinums) you just close it. \n\nThe negative effects that opening a bunch of cards and closing a bunch of cards later has on your credit is going to vary widely based on each individuals credit profile, but it\u2019s generally greatly exaggerated. If you are t carrying some giant balance on a card that results in your overall utilization jumping up over 30% or something like that, closing a few cards over the course of a year or two isn\u2019t going to meaningfully drop most peoples scores."
      },
      {
        "id": "o5s0trt",
        "score": 12,
        "body": "Ya I\u2019ve never had to do this with myself or my spouse but I\u2019d be calling the number on the back of the card, not asking Reddit. People crack me up with this stuff."
      },
      {
        "id": "o5s144w",
        "score": 12,
        "body": "Twice the benefits for zero of the dollars."
      },
      {
        "id": "o5s1iyj",
        "score": 12,
        "body": "Sometimes they let you go years without having to pay the fee after you get out, especially AMEX. Even then, they alert you that you\u2019ll have to pay the fee or cancel. I\u2019m on OPs side with all of this."
      },
      {
        "id": "o5rybmr",
        "score": 10,
        "body": "I have a shit ton also. I think 7 myself? There really isn\u2019t a downside unless you are bad with credit cards and carry balances"
      },
      {
        "id": "o5rsgi3",
        "score": 9,
        "body": "My spouse has had fees waived on her own cards."
      },
      {
        "id": "o5rtqe6",
        "score": 7,
        "body": "It\u2019s certainly generous"
      },
      {
        "id": "o5rthk6",
        "score": 7,
        "body": "How\u2019s that look when you leave active?"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r6k77q",
    "title": "Question About Filing State Tax Under MSRRA",
    "body": "My spouse is currently stationed in Korea, and his home of record (as shown on his LES) is Alabama. I live and work in NYC, and my W-2 reflects New York income. Can anyone confirm whether I\u2019m eligible to file my state taxes in Alabama under the MSRRA before I move forward with filing (married jointly)?",
    "flair": null,
    "score": 4,
    "comment_count": 55,
    "created_at": "2026-02-16T20:01:26+00:00",
    "top_comments": [
      {
        "id": "o5x34b6",
        "score": 3,
        "body": "Where do you see that? The current law ([50 USC 4001](https://www.law.cornell.edu/uscode/text/50/4001), including the amendments of the VAEIA), still includes that line:\n\n> (c) Income of a military spouse\n\n> Income for services performed by the spouse of a servicemember shall not be deemed to be income for services performed or from sources within a tax jurisdiction of the United States if the spouse is not a resident or domiciliary of the jurisdiction in which the income is earned because the spouse is in the jurisdiction solely to be with the servicemember serving in compliance with military orders."
      },
      {
        "id": "o5sgegd",
        "score": 2,
        "body": "You are eligible to file state taxes as an AL resident.  \n\nThe [VBTA of 2018](https://www.govinfo.gov/content/pkg/COMPS-15338/pdf/COMPS-15338.pdf) added the following to SCRA:  \n\n> \u2018(B) ELECTION.\u2014For any taxable year of the marriage,\nthe spouse of a servicemember may elect to use the same\nresidence for purposes of taxation as the servicemember\nregardless of the date on which the marriage of the spouse\nand the servicemember occurred.\u2019  \n\nNote that this **does not** say anything about the spouse needing to physically live in the service members state.  \n\nFor further confirmation, here's an Army.mil [article](https://www.army.mil/article/216870/scra_changes_reach_beyond_income_tax_updates):  \n\n> The military spouse can now elect to use the same legal residence as the service member for tax purposes. **The spouse does not have to physically live in the state and meet any other state residency requirements to do so.**  \n\nWill New York throw a fit and try to come after you if they think you're legally a NY resident? Sure...but SCRA and the VBTA of 2018 says they cannot legally do so if you file the same legal residency as your spouse.  \n\nThat said, if you're hesitant because there is conflicting information out there due to the pre-2018 change, go speak with legal so they can reaffirm the above."
      },
      {
        "id": "o5sh6qn",
        "score": 2,
        "body": "I filed AL. Federal is accepted. AL owe and NY refund are pending now"
      },
      {
        "id": "o5shjrz",
        "score": 2,
        "body": "Awesome. You may want to exempt yourself from NY with your employer...or see if they can accept AL as your state of residency (under the appropriate laws). If they can't you might need to make estimated quarterly payments to avoid penalties with AL (if necessary).  \n\nThat said, hopefully NY doesn't hassle you about it forcing you to get the appropriate legal authorities involved."
      },
      {
        "id": "o5rwai6",
        "score": 2,
        "body": "You are crossing streams.\n\nFederal law (SCRA and MSRRA) takes precedence. So there are two cases:\n\n\\-You / your spouse normally file as NY residents (like yours truly) because NY is listed on your spouse's LES\n\n\\-You / your spouse don't file as NY residents because one of the other 49 states are listed on your spouse's LES\n\nIn *my* case, if I get stationed in NY then I need to pay NYS income taxes on my military income. And in that case, the rules you found on ChatGPT apply. But I'm not stationed in NY, and so each year I file a non-resident return to exempt all of my earned military pay.\n\nIf I were in case 2 and stationed in NY, the SCRA / MSRRA would apply. I would not file a NYS return. I would file a return in the state listed on my LES. NYS would have no idea that I got paid because they wouldn't receive my W-2.\n\nIf you were going to file in AL, you should have coordinated with your employer to exempt your pay from NYS withholdings. That would eliminate the requirement for you to file a NYS return at all.\n\nBut since you didn't do that, you would file a non-resident return and use the exemption code for military spouse, and subtract all of your earned income to get 100% of your withholdings returned.\n\nAs I posted above - the 100% legal answer is you pay NYS taxes because you are living /working in NYS by choice and not as a result of your husband's orders. But no one is going to check / verify that."
      },
      {
        "id": "o5rxg1v",
        "score": 2,
        "body": "It's in the MSRRA. There are criteria for exempting spousal income from the state that you are currently living / working in and one of them is that your presence in that state is strictly a result of your spouse's military orders.\n\nProvided that criteria is met, you can elect your spouse's state for income tax purposes even if you never lived there.\n\nNot your case, but the most common way this 'test' fails is when people first get married and they are living in the non-military spouse's original state of residence. Again, to use my own personal example... if I get hitched in CA to a CA resident, she can't (legally) claim NY for income tax purposes until we leave the state of CA, although I'm quite sure in practice that many people do this without knowing they are breaking the law.\n\nIn your case, you decided to move / work in NYS separate from your husband. You probably have a much more legally defensible leg to stand on to use the MSRRA to exempt your NY income if your spouse's orders are unaccompanied."
      },
      {
        "id": "o5sgrmc",
        "score": 2,
        "body": "> The federal law doesn\u2019t force states to honor that election automatically \u2014 they apply their own residency tests.  \n\nVBTA 2018 explicitly made it so spouses **do not** have to meet residency tests to claim their service members state of legal residence as their own. If NY is trying to tax you while you're claiming AL residency under SCRA/MSRRA, they're violating federal law."
      },
      {
        "id": "o5sijqe",
        "score": 2,
        "body": "If 2025 works out, I will amend 2024 tax year. I told my employer about form 2104-E but they didn\u2019t require me to do this form (or they didn\u2019t know), they only told me to update on portal w4 and one more form"
      },
      {
        "id": "o5t8up4",
        "score": 2,
        "body": "Go read VBTA/SCRA/MSRRA.  \n\nFor civilian spouses of military members, those absolutely do limit how states can tax stuff. Specifically, if the civilian is living and working in NY, and they are claiming a different state as their residence (with the military spouse), their civilian income is no longer considered income earned in NY and is therefore not taxable in NY.  \n\nThese laws were specifically added to simplify tax filing for military members and their spouses. It wouldn't make sense for the laws to exist if states can just choose to ignore them."
      },
      {
        "id": "o5x0tyu",
        "score": 2,
        "body": "I agree with /u/nagisan that you can file as an AL resident along with your husband. However, because you are not in NY solely to be with your servicemember who is stationed there, I believe you are subject to NY state income tax--you'd file as a nonresident with NY-sourced income."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r6htdi",
    "title": "Worrying about retirement",
    "body": "I am 32 and just sort of at a crossroads. I have been on a journey since getting out of the Navy in 2019. I didn't know it at the time but I managed to make something good of myself while stationed in San Diego. I left without with filing any VA (my ship told met that with my medical record that I wouldn't which by the way they never updated) and been on a journey that has had me more times than the military.\n\n  \nAnyway I have started to reorient to retirement and my 401k. I am 32 and only have 45k in retirement. I have upped my contributions. I have debated on going back to active duty because I am high-3 but I don't know if I want to move around a lot again. I make 120k but it doesn't seem to go that far anymore with how expensive everything is in Northern Virginia. The only thing that is holding me back from going back to active duty is I want to run for city council next year because it was a goal of mine when I was in my 20s but the pandemic and life got in the way.\n\n  \nI am very scattered brain but often time I miss the safety net of the military but not so much the work of it. I also see how well a high-3 retirement is now that I am older.",
    "flair": null,
    "score": 9,
    "comment_count": 10,
    "created_at": "2026-02-16T18:35:50+00:00",
    "top_comments": [
      {
        "id": "o5qo890",
        "score": 12,
        "body": "Just do Guard/Reserves.\n\nYou get a safety net with medical, continued paycheck, and can still earn a pension.\n\nThe continued military service and gradual rank increases might help with election as well"
      },
      {
        "id": "o5q905o",
        "score": 6,
        "body": "[deleted]"
      },
      {
        "id": "o5qs0m1",
        "score": 5,
        "body": "Also something to think about is the new BBA & your rate. Make yourself a budget & put as much as you can away in your Roth 401k & absolutely max out a Roth IRA to start. Also having a lil emergency fund cushion is in your best interest, AD or not. 32 is still fairly young & at least you got something. Don\u2019t worry how the market is doing. Buying low will be in your best interest later down the line. You have a long time til retirement."
      },
      {
        "id": "o5rd1ut",
        "score": 4,
        "body": "You are still young and time is on your side. Be happy that you make $120k already. You can easily max out your 401k. I make less than you and i'm still able to max out my 401k and IRA and I have an unemployed wife and two kids. I have no retirement pension or va disability. Claim your VA and enjoy life and stop reminiscing about the military. Most importantly, live within your means."
      },
      {
        "id": "o5ruwhh",
        "score": 2,
        "body": "You're on track by merely investing 10% of your income from now until retirement.\n\n[https://www.calculator.net/retirement-calculator.html?cagenow=32&cretireage=67&clifeexp=85&cincomenow=120%2C000&cincomeinc=0&cretinclevel=100&crilunit=p&cinvreturn=6.5&cinflation=0&cotherincome=2%2C000&csavingnow=45%2C000&cannualsave=10&csaveunit=p&ctype=1&x=Calculate](https://www.calculator.net/retirement-calculator.html?cagenow=32&cretireage=67&clifeexp=85&cincomenow=120%2C000&cincomeinc=0&cretinclevel=100&crilunit=p&cinvreturn=6.5&cinflation=0&cotherincome=2%2C000&csavingnow=45%2C000&cannualsave=10&csaveunit=p&ctype=1&x=Calculate)"
      },
      {
        "id": "o5q7ugz",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o6xs665",
        "score": 1,
        "body": "You're asking the right question at the right time. The issue isn't options, it's about fear and regret. Best thing to do is focus more on what you want and then put a apan into place to acheive it. then obviously you have to commit to daily action - thats the part most mess up."
      },
      {
        "id": "o5qjkd5",
        "score": 1,
        "body": "I needed this. Thank you!"
      },
      {
        "id": "o5t2p0q",
        "score": 1,
        "body": "I feel like I needed to hear this also. I just always worry if I am going to make it in life you know. "
      },
      {
        "id": "o5ta96g",
        "score": 1,
        "body": "When i was 37yo, i only had $35k in 401k and $35k in debt."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r6ch97",
    "title": "Car Insurance w Navy Fed or USAA?",
    "body": "Exactly what the title says, I want to get off my family's plan and hop on my own to just make it easier for them and hoping it's a little cheaper under one of the banks above. \n\nI had two roommates who used NFCU and USAA for car insurance, so far I'd only heard about the app that tracks speed, braking, etc, which also may lead to a lower insurance. On this end, apparently my USAA roommate had an easier time getting a lower rate because the app only took into account when you drove safe/efficient vs NFCU where it tracked everything and would raise rates accordingly. ",
    "flair": null,
    "score": 0,
    "comment_count": 15,
    "created_at": "2026-02-16T15:24:27+00:00",
    "top_comments": [
      {
        "id": "o5p44bb",
        "score": 9,
        "body": "Navy Fed doesn't offer car insurance.\u00a0\n\n\nUSAA has pretty trash customer service, I would recommend shop around with nationwide insurance companies and just use their military discount.\u00a0"
      },
      {
        "id": "o5pt5ol",
        "score": 5,
        "body": "USAA's customer service is still top-notch. My only (recent) complaint is the AI prompts when you call with an issue, but that is par for the course in every customer service line. Breaking the 'do loop' to get to a human instead of having a computer read me information that is available on their website can be a frustrating experience. I get it, for every one of me there are 100 retirees over 80 calling who don't know how to open a web browser, but I only call when something is complicated. Anyway, once you break that do-loop, you'll be talking to a rep in under 2 minutes.\n\nThe issue with USAA is that USAA proper only insures officers. If you are enlisted or a dependent, they write your policy under a subsidiary... which has different (typically worse) rates.\n\nRegardless, claims are all handled by the same customer service and adjuster team, regardless of rank. I have never had an issue with a claim, and they are extremely quick and responsive. The vast majority of people I talk to IRL are satisfied with USAA, and the vast majority of gripes revolve around unrealistic expectations of a bank / insurance company due to the 'exclusive' membership pool. Also, USAA, like all insurance companies, are feeling the hurt from the massive wave of personal injury fraud and that's the primary driver of recent rate hikes. I would be leery of making any decisions based on a story that starts with \"I know a guy who...\"\n\n[https://www.reddit.com/r/USAA/comments/1ehh0ar/officer\\_vs\\_enlisted/](https://www.reddit.com/r/USAA/comments/1ehh0ar/officer_vs_enlisted/)\n\nThe worst bank I've dealt with customer service wise is Bank of America and the worst insurance was State Farm (other driver who was at fault). The latter took 6 months for me to get paid and way too many hours on the phone."
      },
      {
        "id": "o5po42e",
        "score": 4,
        "body": "It's insurance. They all suck. Find the lowest rate (which may or may not be USAA) and go with them. Just make sure you read the fine print about introductory offers and the coverage you selected so that you are comparing apples-to-apples.\n\nYou have to purposefully sign up separately for any programs that would track your driving.\n\nHonestly, if you want the lowest rate, look up local insurance agents and give them a call. They will write you a policy with a regional insurance company that beats any company that puts expensive commercials on TV."
      },
      {
        "id": "o5p7da8",
        "score": 3,
        "body": "Get quotes from everyone."
      },
      {
        "id": "o5pscia",
        "score": 2,
        "body": "This. Like half price for me specifically but YMMV."
      },
      {
        "id": "o6na9v5",
        "score": 2,
        "body": "Have no idea why you were downvoted. I have been a USAA member for 20 years (im 38) and I was in a few accidents in my 20s\u20261 was my fault\u2026and each time the customer service was absolutely fantastic. I felt so lucky especially when I heard others complain about theirs. An elderly lady hit my car and took off (was found) last April and I am JUST getting to repair my car. Long story short, the adjuster was ghetto, lazy, clearly didn\u2019t like her job\u2026would take forever to get back with me. I had to do all the legwork, contact the police, get the parking lot video. I wondered what exactly I was paying $156/month them for (have never received a speeding ticket, only one at fault accident.) Had to fight them to not have to pay my $1500 deductible and cover rental car. Then I just got an email that they are raising my premium. I am shopping around for the first time in my life. "
      },
      {
        "id": "o5p2lot",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o5p72eu",
        "score": 1,
        "body": "Progressive.  Usaa is outrageous and ripping off troops"
      },
      {
        "id": "o5pizqi",
        "score": 1,
        "body": "State Farm for me.  Beats them both, badly too."
      },
      {
        "id": "o5ppfng",
        "score": 1,
        "body": "Geico's not bad. They offer military discount."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r69b79",
    "title": "Single income as E4, LCAL area.",
    "body": "My husband and I have been planning to be a stay at home mom for years. Now that I\u2019m pregnant and me quitting my job has a date on it, I\u2019m having a ton of anxiety. I have always had anxiety surrounding finances. I\u2019m curious if what we are doing is a bad idea. Here are our current finances:\n\nHusband is E4 and will get a pay increase in May once he hits 4 years. It is also likely he will make SSGT, but that\u2019s not guaranteed so I\u2019m not budgeting for it. I\u2019m not entirely sure how much his take home pay will be after his 4 year increase either, but if I had to guess after taxes, $150 extra a month.\n\nOur side hustles make us about $200 per month, but this is not a fixed income and likely will slow down a bit when the baby comes so I\u2019m not even including it in the budget.\n\n\\* we are currently practicing and living on this budget as if we had one income:\n\nBills: $836\n\nFood: $720\n\n(Projected) baby costs: $350\n\nGas: $170\n\nHousehold supplies: $100\n\nWants: $300\n\nContribution to our Roth IRAs: $374\n\nHYSA contribution: \\~$150\n\nWe have:\n\n\\~$29,000 in a HYSA\n\nIn my retirement when I quit I will have \\~$23,500 (about $8k in my Roth and the rest in 401k)\n\nHe has $3,500 in a Roth IRA and contributes at least 5% to his TSP, not sure at the moment how much he has.\n\n$3,381 in a brokerage\n\nHe is planning on staying in for 20 so take that into account for our future retirement. \n\nOther notes:\n\n\\- we use base housing so no potential for house repairs\n\n\\- we use tricare prime\n\n\\- we are eligible for WIC so that will supplement some food income\n\n\\- savings contributions will be a light for awhile if he doesn\u2019t make SSGT but I feel like $29,000 is a good spot for now especially since we don\u2019t have to worry about sudden medical costs or house repairs.\n\nWe are currently living off this income for practice and it\u2019s been fine. Is there something I\u2019m not thinking of?",
    "flair": null,
    "score": 1,
    "comment_count": 11,
    "created_at": "2026-02-16T13:14:38+00:00",
    "top_comments": [
      {
        "id": "o5op9jv",
        "score": 8,
        "body": " If it were me I\u2019d stop putting more money into the brokerage until you can begin maxing that Roth IRA and then he can focus on putting more into TSP.  \n\nDo you have any high interest debt?\n\n30K might be good enough for the emergency fund for now, since he has stable employment and plans to stay in.  So you could move that towards the Roth."
      },
      {
        "id": "o5oslwz",
        "score": 3,
        "body": "Hard to say if this is really a good budget or not without knowing your total monthly income, but I'm assuming it's at least a net zero or positive budget (meaning what you posted results in $0 remaining or a little extra that can slip into savings here or there).  \n\nPersonally I think you may see you need to reallocate some of that money. $300/mo for wants can easily go if need be, as can the HYSA contribution (you have quite a bit saved and stable income).  \n\nA quick Google search suggests a new baby without childcare (due to you becoming a stay at home mom) can range from $400-800 per month, so your $350 may be optimistically low."
      },
      {
        "id": "o5oehkg",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o5ssb4t",
        "score": 1,
        "body": "Not trying to talk you into not staying home, but I would get on the post childcare waiting list in case you decide you still want to work. Childcare is super affordable for military with the MCCYN (child care aware) matching what you would pay on post in the community also. On post is in a sliding scale based on your income level. Also, meals are included for kids in daycare on post. \n\nJust AN option if you decide you do want to continue to work."
      },
      {
        "id": "o5ufyqm",
        "score": 1,
        "body": "sounds like you\u2019ve got a really solid cushion with $29k in your HYSA BankTruth can help you figure out if it\u2019s working as hard as it could while staying liquid for baby needs"
      },
      {
        "id": "o5pl72c",
        "score": 1,
        "body": "No debt over 5% interest. The only debt we have are my student loans. Well, he does have a car loan but it\u2019s at 0%"
      },
      {
        "id": "o5stpr8",
        "score": 1,
        "body": "Thank you! I\u2019ve considered this in case I change my mind last second. I think we will do it just to be safe"
      },
      {
        "id": "o5pl1hp",
        "score": 1,
        "body": "I had twins in 2015... extremely frugal O4 living on an E5 budget at the time. My biggest costs for babies were clothes and some formula to supplement after you've got the car seat, beds, etc. We went with the cheaper convertible crib to infant bed that lasted until about age 4. \n\nThrift shops and on post online mom groups solved the clothes up until around age 5-6, but especially year 1-2 when you can get lightly used baby clothes at an extreme discount. shoes for little kids are especially the biggest rip off. \n\nJust some food for thought and stuff you've likely heard - things to consider.\n\nMy biggest out of pocket expense was 3k for a head shaping helmet not covered by Tricare for one kid with extreme torticollis which was causing major flatness as his skull was forming. Worth every dime, but a chunk out of the paycheck."
      },
      {
        "id": "o5surlh",
        "score": 1,
        "body": "No harm in being on the waitlist, you can always just reject the slot. But if you don\u2019t get on it months in advance, there are usually no baby spots when you need them."
      },
      {
        "id": "o5pm8pb",
        "score": 1,
        "body": "Thanks for the tips! We\u2019ve been thinking about the convertible bed. I\u2019m not sure if all branches have it, but the Air Force has a free thrift shop for E5 and below on every base. They are constantly over flowing with baby stuff, so that is where we will get most clothes. We are already stocking up. They also offer free packs of diapers per week and formula/baby food.\n\nIt definitely won\u2019t supplement all diapers and food for the baby, but it helps some. Once the baby reaches 4 or even before that, I think I will want to at least work part time as well."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r67sqx",
    "title": "Missing any financial opportunities on deployment?",
    "body": "Hey everyone\n\nI\u2019m currently in a CZTE, and will be for the next 2-3 years. O-3 with 9 years of service. I\u2019m single and debt free. My bills are extremely minimal, less than $200 a month. I\u2019m under the BRS. I\u2019m currently maxing the Roth TSP (current balance 200k), a Roth IRA (30k), and contributing an extra \\~1k a month to the traditional TSP (45k). I have about 60k in a brokerage account, mostly VT. I have 20k in a HYSA and have maxed out the SDP.\n\nI have about 45k in my traditional TSP, and I plan on rolling it over to Roth while my taxable income is low these next couple years. I know it comes with a tax hit, but I\u2019m able to cover it. Does anyone know if my standard deduction would help wipe out a portion of that tax hit?\n\nI also had the thought to sell everything in my brokerage and rebuy it immediately, with the idea of increasing my cost basis while not triggering long term capital gains tax since my taxable income is so low. Let me know if this is dumb.\n\nAny thoughts on something I may be doing wrong or thinking about incorrectly, like the brokerage and Roth rollover? Any financial opportunities I\u2019m missing? The goal is to FIRE after my 20 years, and maybe buy a house in the next 5 if I end up stationed back in the states. Thanks for your time",
    "flair": "Question",
    "score": 16,
    "comment_count": 12,
    "created_at": "2026-02-16T12:01:29+00:00",
    "top_comments": [
      {
        "id": "o5ofrcp",
        "score": 18,
        "body": "You\u2019ve got the right idea. If all your other income is tax free, you could convert up to the standard deduction amount of your non-tax exempt, Traditional TSP balance to Roth without paying taxes on it. (You will also have tax-exempt Traditional TSP money which I believe would have to be converted pro-rats.\n\nYou could also do some \u201ctax gain harvesting\u201d to take advantage of the 0% long term gains rate.\u00a0\n\nFor example, let\u2019s say all your military pay for 2026 is tax free and your traditional TSP balance is $22.5k taxable (contributions from regular pay, matching, growth) and $22.5k is tax-exempt (contributions from tax free pay). \u00a0You could convert $32.2k from your traditional balance to get $16.1k in taxable income, which you can deduct. You could also sell with of your brokerage to get $49k in long term gains, and still pay $0 federal income taxes.\u00a0\n\nIf you have any losses in your brokerage account, watch out for the wash sale rules.\u00a0"
      },
      {
        "id": "o5q22yo",
        "score": 3,
        "body": "Do exactly this for three years and you will be balling. \n\nhttps://themilitarywallet.com/maximizing-your-thrift-savings-plan-contributions-in-a-combat-zone/"
      },
      {
        "id": "o5qq5ew",
        "score": 3,
        "body": "We are in extremely similar situations. I\u2019m contributing the max annual additions limit ($72k) and rolling my contributions into Roth each month. Only able to reset the cost basis for a few of my stocks, but it\u2019s smart to do them all if you\u2019re able. There are so many benefits to the CZTE that people don\u2019t realize, glad you have them figured out!"
      },
      {
        "id": "o5osw4u",
        "score": 3,
        "body": "Wash sale rules are pretty liberal because the IRS has chosen to never clarify \"Substantially Identical\" so even switching between two providers for the same index fund still allows for the loss deduction. \n\nIf you sell VOO for a loss and buy SPY you can still deduct the loss for instance because it's two different products from two different companies that while based on the same index have different purchases strategies and allocations. For all practical purposes \"Substantially Identical\" means the exact same ticker. Just don't do that and you're good."
      },
      {
        "id": "o5r8hcz",
        "score": 2,
        "body": "Yes, standard deduction will reduce the amount of tax owed."
      },
      {
        "id": "o5wr0of",
        "score": 2,
        "body": "I'm in year 3 of 4 in your position, just different in having other taxable income and traditional inherited IRA to drawdown. I would do up an Excel spreadsheet as we did last year to ensure you're accurately estimating taxable income as you roll traditional TSP and sell stocks to rebuy. You've got multiple years to execute so take the time to plan."
      },
      {
        "id": "o5o44jb",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o5ufust",
        "score": 1,
        "body": "looks like you\u2019re in a perfect spot to do that Roth TSP rollover while deployed BankTruth can help you estimate the tax hit and how much of the standard deduction can offset it"
      },
      {
        "id": "o6evc0m",
        "score": 1,
        "body": "You can put like 40k or so extra Into tsp when you\u2019re czte. It has to be in traditional after the 24,500 Roth. I\u2019d do that if you have extra to figure out what to do with."
      },
      {
        "id": "o5pena9",
        "score": 1,
        "body": "This helps\u2014thanks!"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r60wwh",
    "title": "State tax (unnecessarily) withheld my entire career",
    "body": "I realized today that my state taxes have been automatically withheld for my entire career, despite my state (Pennsylvania) not taxing active duty income earned while stationed outside of PA. Don\u2019t be like me.\n\nMy question is\u2026 is it possible to amend previous tax returns to recoup that withheld state tax? \n\nI see I can request a W-2C, but not sure if that\u2019s exactly what I need since the tax was withheld, but I shouldn\u2019t have been taxed on it. I\u2019ve tried reading through some old posts but can\u2019t seem to find a definite solution. \n\nIf I can amend the last 3 years worth of returns, I will get back a little over $4K. \n\nAgain, don\u2019t be like me. If your state doesn\u2019t tax military income, verify it, but then opt out of the military automatically paying it anyways. I\u2019ve wasted more than a decade paying tax unnecessarily.",
    "flair": "Question",
    "score": 12,
    "comment_count": 40,
    "created_at": "2026-02-16T05:20:08+00:00",
    "top_comments": [
      {
        "id": "o5mw5uq",
        "score": 30,
        "body": "You would have been refunded state tax when you filed your return if you filed properly\n\nCheck your state rules to see how far back you can amend returns"
      },
      {
        "id": "o5mw6fw",
        "score": 25,
        "body": "Ohio withholds mine, but when I file their return I get it all back."
      },
      {
        "id": "o5mwcdg",
        "score": 7,
        "body": "You sure you didn't get it back when you filed? Every tax software specifically asks you if your wages are military, and then files for a refund from your state.\n\nYou don't need W-2Cs, as your W-2 is correct. You just need to file correctly."
      },
      {
        "id": "o5mzb29",
        "score": 5,
        "body": "How long has this been happening?"
      },
      {
        "id": "o5n27b3",
        "score": 4,
        "body": "Recommend you just fill out a state tax exemption form with your finance office. If you\u2019re Army is a DD 2058. Unless you\u2019re using Mil Tax or another free software, you\u2019re wasting money having to file a state return. Either way I\u2019d rather have more in my paycheck now than get lunch money back during tax season and give the government an interest free loan."
      },
      {
        "id": "o5p3fjx",
        "score": 3,
        "body": "Just wanted to chime in that you can use Military One Source's MilTax software (H&R Block) which lets you file both Federal and State for free. You will need to verify eligibility through their website. I used it the last two years and I've had minimal issues. Military One Source also has free tax consultants. You should try to speak to one of them as they may be able to assist (if you still have questions/need help)."
      },
      {
        "id": "o5mzpqc",
        "score": 2,
        "body": "TurboTax never properly credited my military pay to Ohio too. My husband always did the filing and he didn\u2019t realize I should have been getting that money back, and I was working 60-80 hour weeks so I didn\u2019t look. I took over doing taxes this year and realized the error, now I am working on amending the last 3 years\u2019 worth of state returns."
      },
      {
        "id": "o5p41gr",
        "score": 2,
        "body": "Why didn't you file to get them returned to you???"
      },
      {
        "id": "o5mxjyy",
        "score": 2,
        "body": "Before I turned off withholding, The one source software did not refund me all of my CA tax when plugged in. It treated it like a normal person even after marking military. Once I figured out I didn\u2019t have to pay anything I had to adjust the income within it in order for it to refund all of what was withheld."
      },
      {
        "id": "o5my1oa",
        "score": 2,
        "body": "You need to file an amendment(s). If you don't know how to do that, contact a CPA/tax professional."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r5svdl",
    "title": "Need advice on multiple credit cards",
    "body": "While active in duty, I ended up with over a dozen different credit cards. It feels like a chore to keep track of the rewards and offers while I do want to get the most out of my cards, I don't want to spend hours keeping track of that. I'm curious how you manage your credit cards usage? Do you just use excel to keep track or is there any app/website that helps you?\n\n",
    "flair": null,
    "score": 0,
    "comment_count": 12,
    "created_at": "2026-02-15T23:00:42+00:00",
    "top_comments": [
      {
        "id": "o5la2e7",
        "score": 5,
        "body": "This is not a military specific issue. If you Googled your question you would have found a number of solutions (multiple apps, websites, excel templates, etc.)"
      },
      {
        "id": "o5m45eb",
        "score": 2,
        "body": "I heard [The Perky App](https://theperkyapp.com) is pretty good. Track perks, partial usage (eg, used $50/$100 of your Resy credit), and even loyalty points."
      },
      {
        "id": "o5me8mq",
        "score": 2,
        "body": "Google Keep checklist"
      },
      {
        "id": "o5l8qel",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o5lxhe5",
        "score": 1,
        "body": "Lots of apps out there. TravelFreely for example. CardPointers. I just use an excel spreadsheet and focus on the big wins and don't sweat the small stuff (looking at you, $7 Dunkin credit)."
      },
      {
        "id": "o5pdyjf",
        "score": 1,
        "body": "I'm tracking 30 amex cards between me and my spouse. Along with 10 other chase/Citi/US Bank cards, all from a custom spread sheet. We constantly update what we've used, and it works for us."
      },
      {
        "id": "o5yh4ef",
        "score": 1,
        "body": "Tracking the hotel nights and when each free night resets is what I hate most"
      },
      {
        "id": "o6nihsd",
        "score": 1,
        "body": "CardPointers app. Helps manage the 30+ cards my wife and I have. Best part is the browser extension that auto adds all the coupons so you never miss out."
      },
      {
        "id": "o5lwfau",
        "score": 1,
        "body": "This, but also personal opinion, you will drive yourself crazy trying to min/max your benefits across all the cards. Better to just stick to two, maybe three tops and the rest just put a token charge on every half a year to keep the account active"
      },
      {
        "id": "o5mat7e",
        "score": 1,
        "body": "Damn this is tits"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r55abb",
    "title": "Living Trust/ Special Needs Trust",
    "body": "I am currently active duty and a Florida resident currently stationed in Virginia. I am married, wife is SAHM, and three children, my oldest is 6 with severe autism and I'm just thinking ahead about setting up a Special Needs Trust (SNT). While I'm at it, should I just do a living trust as well? Currently I don't have alot of assets. I want to get additional term life insurance, but should I wait until I have a trust set up so I can name it as a beneficiary? Also which state should I contact an attorney in? Florida or Virginia? We are kind of up in the air about where we will be at retirement, but I want to plan ahead so my daughter is taken care of in case something happens to me and her mother. ",
    "flair": null,
    "score": 1,
    "comment_count": 17,
    "created_at": "2026-02-15T04:24:45+00:00",
    "top_comments": [
      {
        "id": "o5ghb6j",
        "score": 2,
        "body": "Without significant assets, you really don't need a trust. Set beneficiaries for all of your accounts and you'll be good.\n\nFor a special needs trust, contact an attorney in your legal state of residence. They will guide you through it."
      },
      {
        "id": "o5gicw4",
        "score": 2,
        "body": "No...as you said, that's not significant. Set beneficiaries for those accounts. Done. That skips probate."
      },
      {
        "id": "o5gfw4e",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o5i1avm",
        "score": 1,
        "body": "Look into ABLE accounts, very similar to SNTs"
      },
      {
        "id": "o5ghxbm",
        "score": 1,
        "body": "Im at 8 years of service and have 150k in my tsp and maxing contributions and I've started investing in a brokerage account. So I'm building wealth, but still not really warranting a living trust? Just special needs trust so my daughter wouldn't lose any benefits."
      },
      {
        "id": "o5i1hm2",
        "score": 1,
        "body": "You are missing somethjng significant. A disabled person cannot have assets in their name directly or they lose state benefits. So a SNT or ABLE account is needed"
      },
      {
        "id": "o5j1hgq",
        "score": 1,
        "body": "He is saying I should get a SNT, but not a living trust.\n\nWhat would you consider significant assets which would justify a living trust? From my research looks like I can do a SNT and combine it into a living trust later if I want. Which seems like the best option for me now. My daughter is only 6, but I'm just trying to plan as best I can as it seems she will need help throughout life. I want to get additional term life insurance around 2-3mil since I have 3 kids and wife does not work and oldest may require help throughout her life, but I've seen if she inherited money at 18 she would lose any government assistance so a SNT is required so it can be the beneficiary. And say my brother, who is incredibly smart financially, could be the trustee and manager the funds for her. If I'm understanding everything correctly."
      },
      {
        "id": "o5j1t58",
        "score": 1,
        "body": "You didn't reference my first comment, did you?"
      },
      {
        "id": "o5j267y",
        "score": 1,
        "body": "Real estate, businesses, etc would warrant a trust. Basic accounts, you can just set beneficiaries. It's not really about the $ value of assets, but the type of assets."
      },
      {
        "id": "o5j33ub",
        "score": 1,
        "body": "Thats the issue, the child CANNOT be the direct beneficiary. This is where you must be cautious or he will lose any gov benefits. The only two ways around this are ABLE accounts or a SNT. There are no other options."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r4pchm",
    "title": "SCRA and MLA advice",
    "body": "I enter AD in March as a LT, looking to get the Chase Sapphire Reserve, wanting to know is there a way I can open this before my orders start so I can apply SCRA benefits to drop interest to 4% but also avoid the annual fee under MLA? Not sure if this will work because SCRA only applies to credit before entering AD (to my understanding) and MLA is for AD. Any help is appreciated. Thanks",
    "flair": "Question",
    "score": 0,
    "comment_count": 11,
    "created_at": "2026-02-14T16:44:47+00:00",
    "top_comments": [
      {
        "id": "o5d577n",
        "score": 17,
        "body": "Wait for MLA.\n\nIf you're worried about an interest rate, don't get the card at all. You should never carry a balance on a credit card."
      },
      {
        "id": "o5db306",
        "score": 9,
        "body": "If you can, open a Capital One Venture X now. C1 won't apply SCRA benefits until after you enter active duty, but they also won't apply MLA/SCRA benefits of the card is opened after you enter active duty."
      },
      {
        "id": "o5dizvh",
        "score": 3,
        "body": "This is the best advice!!"
      },
      {
        "id": "o5d6ntg",
        "score": 2,
        "body": "This. Interest rate should be irrelevant if you're managing the money right"
      },
      {
        "id": "o5dj41f",
        "score": 2,
        "body": "Idk why you are downvoted already, this is 100% accurate and people recommend opening VX before joining to get the AF waived. \n\nAlso, people have had luck having a No AF Venture or venture one they can PC over to VX and have the fee waived."
      },
      {
        "id": "o5dbege",
        "score": 2,
        "body": "To be specific and ATQ: The 6% interest rate cap applies to existing **debt** and not existing **lines of credit**. You cannot permanently lower the interest rate on the card through the SCRA.\n\nFor example, if you run up a $500 bill prior to swearing in, the SCRA can force the creditor to 'forgive' accrued interest over 6%. However, the double-digit interest rate on the card will still remain in effect after you enter service for any new purchases you make.\n\nFurthermore, the waiving of annual fees on the card after you enter service is not an aspect of the SCRA, it's a military discount offered by the creditor. I mention this so that you pay attention to this in the future and also so you don't get wound up when a company won't waive their fees."
      },
      {
        "id": "o5d3wfv",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o5h9o70",
        "score": 1,
        "body": "I am in similar situation as OP, and was advised by C1 SCRA support to do so as well. Do you know any other good cards to apply for with similar requirements of getting before entering AD?"
      },
      {
        "id": "o5ha277",
        "score": 1,
        "body": "When I applied for SCRA benefits with C1, I got a refund check for my Venture annual fee. It's worth noting that product changing to VX from venture will not allow you to earn the sign up bonus."
      },
      {
        "id": "o5dbzlg",
        "score": 1,
        "body": "Good to know. Thank you"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r40ejl",
    "title": "New Military Spouse",
    "body": "Hello! As the title says I am new to military life and was wondering how do I know if BAH has kicked in. My husband shipped on Jan 12th, his first paycheck was $1491. When I was able to speak to him that Sunday, he said he was told his BAH would be $2100. His next paycheck was $1112. I don't know what his base pay is as an E1 and want to make sure he is getting paid properly before the next time I speak to him. Is BAH one lump sum or is that split up as well? ",
    "flair": null,
    "score": 6,
    "comment_count": 23,
    "created_at": "2026-02-13T20:36:35+00:00",
    "top_comments": [
      {
        "id": "o589jz2",
        "score": 21,
        "body": "Talk to your husband. You both need to figure this out as you go. He is the best source of information since he is learning, and if he doesn't know, he'll ask his supervisor.\n\nBAH is split between the two checks. Looks like he's not getting it, but he needs to look at his LES."
      },
      {
        "id": "o58kg42",
        "score": 15,
        "body": "It\u2019ll kick in 45 days after his first day in basic not reception. He\u2019ll get back pay. That\u2019s how it was for me at least and I just graduated basic Jan 30."
      },
      {
        "id": "o589z0i",
        "score": 12,
        "body": "Yeah but if the guy's in boot camp is he really going to have a lot of time to dig around and check this stuff? I remember they just had us fill out paperwork to set up direct deposit and then we never saw anything about pay again until after graduating and getting to tech school. Maybe they have more downtime and computer access these days though so legit asking."
      },
      {
        "id": "o58a33r",
        "score": 6,
        "body": "I have talked to him. I'm only able to speak to him on Sundays since he's at BCT, but before the next time I speak to him I want to make sure everything is fine on my end before I tell him \"your BAH hasn't come yet\" and it really has."
      },
      {
        "id": "o58asdn",
        "score": 5,
        "body": "He needs to look at his LES."
      },
      {
        "id": "o589c2s",
        "score": 4,
        "body": "Hello and congratulations!\n\nDefense Finance and Accounting Service (DFAS) is the official reference for all things regarding military pay [https://www.dfas.mil/Pressroom/Article/4391719/2026-military-pay-tables-on-dfas-website/](https://www.dfas.mil/Pressroom/Article/4391719/2026-military-pay-tables-on-dfas-website/) but other sources like [military.com](http://military.com) are generally reliable (here's their pay chart link: [https://www.military.com/benefits/military-pay/charts](https://www.military.com/benefits/military-pay/charts) ). Base pay is based on your paygrade and how many years you've been in (goes up every 2 years of service), and it usually increases by a small amount (say, 1.5% to 4% range on average) every year for everyone.\n\nAn Active Duty E-1 with fewer than 2 years of service gets $2,407 base pay. \n\nBAH and BAS are split up between midmonth paycheck and end-of-month paycheck.\n\nIt may take a while for BAH to kick in but you will be backpaid to the date you were first eligible to receive it.\n\nThe initial paychecks may look funky because some amount is taken out for gear and uniform issue."
      },
      {
        "id": "o589lth",
        "score": 3,
        "body": "Paystub.  Can be accessed through [MyPay](https://mypay.dfas.mil/#/) if you have the login info.  \n\nYou can look up [his base pay](https://www.military.com/sites/default/files/2026-01/2026%20AD%20Pay%20Official.xlsx%20-%202026%20AD%20Pay.pdf) and his [BAH rate](https://www.travel.dod.mil/Allowances/Basic-Allowance-for-Housing/BAH-Rate-Lookup/) based on rank and **your** zip code, add them together, divide by two and that\u2019s roughly how much each paycheck should be."
      },
      {
        "id": "o58a7md",
        "score": 2,
        "body": "He's also learning as he goes so I wanted to speak to someone one who has a little more experience"
      },
      {
        "id": "o58anlo",
        "score": 2,
        "body": "Thank you, my guess is it hasn't kicked in yet. I'm also going to check out those links. I appreciate the information."
      },
      {
        "id": "o58az3a",
        "score": 2,
        "body": "Yes, they have time to look at their LES and go fix problems.\n\nEveryday? No. Still plenty of time though. Likely directed to, as well as how to read it."
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r3uf4l",
    "title": "VA assumption loan at 4.25%",
    "body": "Bought my home in 2022 with the above interest rate. I am military and am waiting to hear back on potential orders that may move me in the summer of 2027. Obviously I can\u2019t foresee what rates will be like then but would listing my home with an assumable VA loan with this interest rate be attractive in today\u2019s housing climate? Or just selling normally when the time comes is the better option without knowing too much with what mortgage rates will look like in a year +.\n\nI understand that ideally the buyer would need to be military otherwise the buyer would have my VA entitlement tied up with them if they are not but my wife is also military and we haven\u2019t touched her benefits so I\u2019m not particularly concerned there. For context, I am based out of Killeen Texas in the fort hood community. Thank you for any advice and just trying to plan ahead in case this coa happens.",
    "flair": "Question",
    "score": 13,
    "comment_count": 19,
    "created_at": "2026-02-13T16:53:01+00:00",
    "top_comments": [
      {
        "id": "o56xqzs",
        "score": 14,
        "body": "Depends on the rate and how much equity you have. Many people cannot afford to cover the equity in cash."
      },
      {
        "id": "o56ze38",
        "score": 7,
        "body": "Equity is the difference between your mortgage and the home's value, whatever you can sell it at."
      },
      {
        "id": "o576ako",
        "score": 6,
        "body": "As someone who will be looking to do an assumption, you should definitely advertise it. The other guy said the buyer needs to bring the cash for the equity gap - it can be a second mortgage. Im looking at assuming a 180k loan from 2022 thats worth 280 now and do a second mortgage on the 100k equity difference."
      },
      {
        "id": "o570wem",
        "score": 6,
        "body": "Equity is not based what you bought the home for. It's what your mortgage is. There's a difference.\n\nAnd again, maybe. Some people can't come up with $100k to cover that difference. Also who knows what the rates will be in a year.\n\nYou can certainly try!"
      },
      {
        "id": "o57g3hu",
        "score": 4,
        "body": "We sold our home via assumption in 2023.  1- it sold at our asking price, which we set based on the home\u2019s value and we didn\u2019t set a higher price based on the loan (2.25%).  2- We were fortunate that we had a Veteran buyer, so I got my entitlement back and they had sold their house, so they could afford the extra cash they needed to bring to closing (130k).  3- It was a pain to get Freedom mortgage to approve the assumption.  They say they are for Vets but the process took about 3-4 months longer than a normal approval process."
      },
      {
        "id": "o56y5vc",
        "score": 3,
        "body": "So just to make sure I have this right from my research. If I bought my home for 270,000 and I have 30k of equity accrued into my home the buyer would have to pay me that 30k cash? And follow up how does that equity get determined by county appraisal, how much it\u2019s listed for etc? Sorry for the slew of questions just trying to understand this better"
      },
      {
        "id": "o56zdk2",
        "score": 3,
        "body": "You have the concept correct, but the equity they have to pay (\"the gap\") is simply determined by the difference in what you sell the house for and what is still owed on the loan."
      },
      {
        "id": "o571rcl",
        "score": 3,
        "body": "$30k is not that hard of an ask.  There are ways to generate a small amount of liquidity.  Mind you, not everyone can pull it off.  We're PCSing later this year and I'm looking for assumable loans at our new assignment.  \n\nIMO, what makes assumable mortgages so out of reach is the the insane housing markup that happened a couple years ago.  Think about when people were getting these 2.25% - 3% loans... The prices were reasonable too.  The market we're currently in, South Florida, saw houses increase in price $200k - $500k in a couple of years.  When we moved here, sure... I could have got a home with an assumable, but I would have been on the hook for inflationary equity (no idea if that is a real term or not, lol).  I didn't have $300k just to buy someone's house who bought at 'the right time'.\n\n  \nYou happen to be leaving Charlottesville, Virginia?  :P "
      },
      {
        "id": "o56x92g",
        "score": 1,
        "body": "Welcome to r/MilitaryFinance! \n\nPlease check out our [\"Start Here: Military Money 101 & Prime Directive\"](https://www.reddit.com/r/MilitaryFinance/comments/1oksn2s/start_here_military_money_101_prime_directive/) thread for essential information and resources.\n\nYou may also find these helpful:\n- [Credit Cards & Military Benefits (SCRA, MLA, Annual Fee Waivers)](https://www.reddit.com/r/MilitaryFinance/comments/1ola48e/credit_cards_military_benefits_scra_mla_annual/)\n- [Tax & State Residency (MSRRA) Questions & Discussion](https://www.reddit.com/r/MilitaryFinance/comments/1oksnru/tax_state_residency_msrra_questions_discussion/)\n\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/MilitaryFinance) if you have any questions or concerns.*"
      },
      {
        "id": "o5fd7o3",
        "score": 1,
        "body": "I have a loan program to help bridge the gap for people on this but they still would have to cover about 10%. The other thing is you may want your entitlement restored so you would have to sell to a vet but you can have more than 1 va loan at once so depending on purchase price of the new home you potentially wont have a down payment"
      }
    ]
  },
  {
    "subreddit": "MilitaryFinance",
    "id": "1r3ejyi",
    "title": "Did anyone with a long career live exclusively on base housing during their time in?",
    "body": "And then not end up buying property until they got out? The reason I\u2019m asking is I\u2019m an O3, no debt, good spot financially, and feeling the pressure to buy a house because everyone else around me is.\n\nBut I don\u2019t want the stress of buying a house and the extra costs that come with it (maintenance, etc). I love the convenience of living on base.\n\nI know it could be a good financial investment, but I\u2019m curious if anyone went against the grain and didn\u2019t buy property until much later in life, growing income instead with other investments while renting or living on base.\n\nHope that makes sense.",
    "flair": "Question",
    "score": 28,
    "comment_count": 56,
    "created_at": "2026-02-13T03:36:19+00:00",
    "top_comments": [
      {
        "id": "o53rqi3",
        "score": 66,
        "body": "[deleted]"
      },
      {
        "id": "o5464fi",
        "score": 46,
        "body": "We rented off base for 23 years. Been retired for 2 now. Still renting.\n\nNever do something just because everyone around you is doing it. \n\nHouses are money pits. Rent and invest as much as you can. Buy a house if and only if the numbers make sense financially (ALL the numbers) and you decide being a homeowner is the lifestyle you want."
      },
      {
        "id": "o54w7cd",
        "score": 28,
        "body": "I rented 9 out of 12 years of active duty. Became a millionaire by O-4. My one property investment netted $40,000 when I sold it. It was fine. Very stressful. Happy to rent the rest of my career.\n\nYou don't need to buy a house to build wealth in the military. Resist the pressure."
      },
      {
        "id": "o53r7bc",
        "score": 23,
        "body": "Extremely common and/or renting off base. Many people cannot afford to own a home."
      },
      {
        "id": "o53ry30",
        "score": 15,
        "body": "If you\u2019re an O-3 it might not make a lot of sense to buy a house. You\u2019ll probably be moving every 2-3 years right? There are sunk costs every time you buy and sell a house like financing, legal fees, inspections, lawyer fees.  You pay mostly interest at the beginning of the loan so you don\u2019t build much equity until you\u2019ve been in a few years. At the beginning, you\u2019re just paying mostly interest instead of rent.\n\nLots of people think they\u2019re going to buy a house and then rent it out when they PCS. Even if you\u2019re able to turn a small profit doing that, you\u2019ll be stressed about it constantly and you can actually lose money paying the mortgage on a vacant house when it\u2019s not filled. Also maintenance. homeowner\u2019s/landlord insurance, taxes (income and property), and property management fees really eat into any profit.\n\nLiving off post, you gotta factor in commute costs as well. Time and money. \n\nIf you can get a job that will keep you at the same duty station forma few years, in a state with low insurance premiums and taxes, and a stable housing market then maybe it\u2019s worth it, barely. But your FOMO of getting rich buying a house is misguided if you\u2019re gonna pcs every 3 years."
      },
      {
        "id": "o55k6xv",
        "score": 12,
        "body": "Thank you. Reassuring to hear to that."
      },
      {
        "id": "o53tlki",
        "score": 10,
        "body": "Yeah the quality of life is a huge consideration for me. Thanks."
      },
      {
        "id": "o590vmv",
        "score": 10,
        "body": "My rent is providing us a stress free shelter. I couldn't care less about how rich our landlord is getting because of it. It's a fair trade as far as I'm concerned. \n\nI don't want to be a homeowner.\n\nDo you say the same thing every time you go eat at a restaurant? It's the same thing."
      },
      {
        "id": "o53soxw",
        "score": 9,
        "body": "Many people do, O3 with no debt you will be just fine. There are a lot of variables that factor in if you should or shouldn't buy a house. \n\nYou are more than likely in a position that you would be fine to buy a house, buy a decent enough one and get a good inspection and you probably won't have any major maintenance issues during your stay there. Sell after a few years and you will probably either break even compared to renting. Depending on the area you may even walk away with some extra cash. \n\nIf you like living on base then live on base, if you like not worrying about MX then rent, if you want to probably break even or make a few bucks compared to renting but risk running into a roof replacement then buy.\n\nIt's not a black and white answer you need to pick what is most valuable to you at the time"
      },
      {
        "id": "o55i9tx",
        "score": 7,
        "body": "It\u2019s low risk, I\u2019ll tell you that. You\u2019re missing out on money on the table, but it\u2019s like keeping your TSP in the G Fund.\n\nAll of the people telling you \u201cIt\u2019s a no brainer to buy at every duty station\u201d didn\u2019t go through a housing collapse where houses lost half of their value during a 3-year tour. Then they were stuck with short sales and years of debt.\n\nRecently, it\u2019s been a good deal to buy at all full length duty stations. But if you\u2019re going the 0% down route, you won\u2019t stand to gain much.\n\nLiving on base (or renting) your entire career can let you be more flexible with Broadening Assignments, Black book hires, and can keep you more nomadic. Takes the worry about figuring out how to manage properties, HVAC units, taxes, etc."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1lxeub2",
    "title": "I am the last person left alive from the squad that I served with in Iraq.",
    "body": "That's it they are all dead. 3 to suicide and 2 to cancer and one drank himself to death and I dont know where the last one is , he ghosted years ago. \n\nI was the platoon medic, I helped all I could and it didn't work or help. Its even worse now at the VA in Texas. The pain of surviving and still being here. I cannot show or let this effect me at work or at home cause I am a guy. And its not acceptable for us older dudes to show that stuff.   \nTrying to talk to non military people do not understand my wife, kids look at me as I am strange because I have walled off everything. \n\nIt hurts. But hey, I aint heard no bell...   \nI miss and love you all.   \nDoc Davis",
    "flair": "Venting",
    "score": 749,
    "comment_count": 83,
    "created_at": "2025-07-11T18:42:57+00:00",
    "top_comments": [
      {
        "id": "n2mvd7g",
        "score": 52,
        "body": "Thank you everyone, I feel sad that I have to turn to my people on Reddit to be able to talk about this.  \nLove u all"
      },
      {
        "id": "n2o9v9w",
        "score": 49,
        "body": "Doc Davis, I feel for you. One of my best friends is retired 0311 USMC. He took an IED to the face and thankfully survived. But, a lot like you, his brothers have been lost to suicide, cancer, and motorcycle crashes. He\u2019s been through hell and back.\n\nHe and I bonded over survivors guilt while selling motorcycles back in the day. Mine from somehow miraculously surviving a very aggressive and deadly cancer. Different experiences but he and I both wake up in the morning wondering why the fuck we\u2019re still here and others aren\u2019t.\n\nHe and I have a deal. If he or I get close to the \u201cedge\u201d we call or text each other, no questions asked. So far he and I are 4/4.\n\nI haven\u2019t been through the same as you, but I\u2019m going through some pretty awful shit right now. Been in the hospital for 10 days at the moment for my 3rd spinal fusion in 3 years following 2 seizures out of nowhere.. If you ever want to chat, hit me up man. I\u2019m sorry for your losses. I\u2019m pulling for you.\n\n-Derek"
      },
      {
        "id": "n2p6san",
        "score": 42,
        "body": "Look I\u2019m not going to tell you what to believe but I am going to be brutally honest with you because I don\u2019t see things getting more manageable if someone isn\u2019t. I\u2019ve watched too many men die over the idea that \u201cmen can\u2019t show emotion\u201d it\u2019s bullshit and it actively prevents you working through the pain you\u2019re carrying, it doesn\u2019t make you weak or less it takes a shit load of courage to open up to the people that love you and ask for help. \n\nYou\u2019re not ok and given the hell you\u2019ve been through you frankly shouldn\u2019t be. For your brothers in arms, for your family for those you\u2019ve lost talk to someone, anyone because you deserve support for serving your country. If it\u2019s helpful I\u2019m happy to chat."
      },
      {
        "id": "n2lmv3l",
        "score": 32,
        "body": "I\u2019m so sorry man. \n\nI have a bracelet with the names of three close friends that off\u2019d themselves. We were all in Afghanistan together. \n\nI noticed the pain I felt when I couldn\u2019t remember their first names. Or the specific day they died. \nI carry them with me mentally and emotionally. It has been helpful for me to have a physical representation of that weight. \nI never take it off.  I\u2019m on my third of fourth one. I  just changed from stainless steel to bronze. Hope I don\u2019t need to add more names cause I\u2019m running out of room."
      },
      {
        "id": "n2qv8s9",
        "score": 29,
        "body": "It absolutely IS acceptable for you to show those emotions as a man. Society has conditioned you to believe otherwise, especially being in Texas. \n\nSpeak up to your family, seek community, seek help. Asking for help and talking about the way you feel is not weakness- it\u2019s a sign of great strength. Good luck my friend. Sending you comfort and peace"
      },
      {
        "id": "n2mtduz",
        "score": 27,
        "body": "I'm a 53yo dude w/ PTSD. Learning to cry is so hard, but you can, you need to, regardless of the bullshit macho programming we all got.\n\nEvery one of you guys deserved better than to be used up and tossed aside to suffer in silence. Their failure to look after you is not your fault.\n\nYou have to feel that shit, even if you cry until you vomit.\n\nIf you never show what you're feeling, what message does that really give to the next generation of soldiers under your care? You have an opportunity to show them a new way, a path towards healing, or at least making the shared trauma a little bit easier to carry.\n\nBut it's hard. I've now spent more time in therapy than in uniform, I know it's not easy. Society's expectation that you not show your pain is bullshit. What favours has social norms actually done for you? What aid has their expectations given you. Love yourself enough to let it out, my friend."
      },
      {
        "id": "n2r5cor",
        "score": 25,
        "body": "You should try writing. Even if you decide not to share it. You seem like a naturally good writer. I think it might help you the most, but I also think that it might help the world in general.\u00a0\nSo many people are actually afraid to ask veterans what they go through, what they've seen, how they felt, and what it's like.\u00a0\nThere might not ever be a way to fully explain to anyone who hasn't experienced it themselves, but there are stories that just aren't meant to be carried by one person alone. Man, woman, soldier, some things are just too heavy.\u00a0\nI think it's incredibly brave, especially for men, to be that open about something so personal.\u00a0\nI wish you all the peace in the world that there is to be had.\u00a0\nThank you for sharing and for all you guys do...which is more than I'll ever know. But I know it's gotta be a lot.\ud83d\udc97"
      },
      {
        "id": "n2n4883",
        "score": 24,
        "body": "Non-military here but friends and family and several ex boyfriends who were. Vietnam to Afghanistan, respectively.\n\nI know my PTSD and your PTSD are two different things, but I know what it\u2019s like having survivors guilt and trauma that you cannot connect with anyone else with. It\u2019s embarrassing, and therapists just love to tell us to breathe and name 5 things you can see.\n\n\nAll that to say - I am so sorry. You deserve way more respect and support than what you\u2019re given"
      },
      {
        "id": "n2lrqc4",
        "score": 21,
        "body": "You\u2019re right . Everyone untouched who are civilians think it\u2019s over and time heals all wounds\u2026  It doesn\u2019t. Really shitty place you\u2019re in. And yeah , older guys have a different burden of holding up and staying squared away.  No disrespect to feeling like you weren\u2019t able to succeed in helping your guys - but you did help your brothers. They hung on longer than they likely would have without you.  Those years gave their families that much more time with them. You know what that means to those people.. You can\u2019t take away what you didn\u2019t cause - but you sure as hell made a difference whether it was for a month , a year or decades. Brother , you\u2019re the one chosen to carry the story. Thank you for sharing a part of it with us. Well done. #NeverForgotten"
      },
      {
        "id": "n2n0nsd",
        "score": 21,
        "body": "But brother you\u2019ve got a place to talk about it, and that\u2019s what\u2019s important."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1nw4ix9",
    "title": "Grandfather randomly send me a FedEx envelope full of traumatic photos and information from my childhood",
    "body": " I'm already on 75mg zoloft. I got a notice from my apartment complex management that I had a packet waiting at the office when I went to pick it up it was the FedEx envelope.\n\n Inside the envelope were 20 photos of emaciated child me living in a trash heap tin shack with piles of garbage everywhere. There were like 3 photos with me in them the rest were all of the living conditions I was in.\n\n There was a ton of papers old medical records of SA examinations on me and letters of what appears to be of my grandfather writing maybe child protective services? \n\n He didn't leave any context as to why he sent this stuff. I saw the pictures and just sobbed for like 20min. I have been doing so well but now I can't stop thinking of my childhood\n  I just keep praying that these horrible feelings go away. ",
    "flair": "Support",
    "score": 500,
    "comment_count": 69,
    "created_at": "2025-10-02T13:57:44+00:00",
    "top_comments": [
      {
        "id": "nhffobn",
        "score": 139,
        "body": "It sounds like he tried to save you. He wanted you to know that he saw you and he was on your side,that he tried the best he could. He's showing you he believes you and knows it happened."
      },
      {
        "id": "nhkf282",
        "score": 113,
        "body": "I don\u2019t know him so I could be wrong but it sounds like he\u2019s trying to communicate that he tried to save you but was unsuccessful. This must have meant a lot to him if he was willing to part with such important documents & knowing you\u2019re an adult now, he probably thought it was \u201cthe right thing to do\u201d. He likely didn\u2019t know how much it would hurt you or factor in that it would be difficult to revisit this. Try reaching out to him. It sounds like he\u2019s trying to show you he loves you a lot & he needs someone to be there for him like he tried to be there for you."
      },
      {
        "id": "nhk1a4y",
        "score": 72,
        "body": "I'm so sorry \ud83d\ude14 \n\n\nMaybe, sounds like Grandfather tried to get the situation solved, but failed, and wants you to know that he was fighting for you?\n\nKeep everything (in a locked safe somewhere) to pursue something later, beyond the initial shock + painful and validating mixed feelings?\n(edited: grammar + spelling)"
      },
      {
        "id": "nhfbyv3",
        "score": 68,
        "body": "Maybe he came across it and didn't feel right throwing it away. Having a record like that is more proof than some people get. Doesn't mean you have to keep it, but maybe you can burn it or dispose of it in a way that gives you some type of strength. You never have to be that kid again; but that kid will always be inside of you. Just protect that kid. Protect you. You don't need to look at it again. Maybe a friend can help you bury it. What would make you feel satisfied? Is there anyone else you would want to show it to, or someone who can take if off your hands to dispose of it on your behalf?"
      },
      {
        "id": "nhi80zm",
        "score": 63,
        "body": "\ud83e\udec2\ud83d\udc9c Sending lots of love, hugs and healing light your way. \n\nIs there any chance it was sent as a way to make sure you had them for proof of everything if needed if he was no longer around? Perhaps he assumed to throw them away would be getting rid of evidence you may need at any point in your life in a court case or otherwise and didn't want to be the one to decide whether or not to make that choice of whether to keep it or pass it on to you...? Either way, there DEFINITELY should have been a warning or something that went along with such a triggering package."
      },
      {
        "id": "nhj35hh",
        "score": 58,
        "body": "This is horrible. Please check in on grandpa. Sounds like he was the only one that was fighting for you."
      },
      {
        "id": "nhgpvp8",
        "score": 56,
        "body": "Did he maybe pass a way and someone had been given notice to send this to you ?"
      },
      {
        "id": "nhg2mfk",
        "score": 51,
        "body": "That\u2019s a difficult package to receive out of the blue. You survived every moment documented in those papers and pictures; you are here and are a survivor. Only your grandfather can tell you why he sent the photos. The rest of us can only speculate. first and foremost, take care of your mental health. Reach out to your prescriber to let them know you\u2019ve had a situation and may need to come in for additional support.  Second, when you are ready then talk to your grandfather. Third, allow yourself to grieve for the childhood you lost. Finally, remember you\u2019ve survived every day so have faith in yourself that you can keep going."
      },
      {
        "id": "nheuf03",
        "score": 50,
        "body": "I don't know that your grandfather did this 'randomly' though it may seem so, to your perspective.  I think it is a gift, and that he is telling you that he feels as strongly about it as you do, and that he trusts your strength to be able to handle it. \n\nI am told that, when I was eleven years old, a storm came and destroyed my house.  We lost everything.  Books my grandfather had given me.  My dog. A roof over my head.  Everything.  I have no memories of it.  From February of 1978 to about July or August of 1979 is a complete blank to me.  Nothing.  \n\nI both wish I had pictures from then, and fear to know what happened.  I am sure that, if someone mailed me pictures of that time, I would react as you have.   I wish I could cry over it, but I can not for I do not truly know what happened.\n\nI am told we lived for a while with my maternal grandparents, which surely was a shockingly toxic situation, and than in a variety of motels and/or rental apartments until my father, who was both working full time (this was pre FLMA) and house-hunting, as my mother was drastically useless (she is an actual sociopath), and he was able to purchase a new house.  Not long after, my parents divorced, and my dad eventually drank himself to death, I think in large part because of the realization of the monster he married. \n\n I think your grandfather gave you a gift of knowledge.  Yes, it hurts.  Maybe it hurts him just as much.  Perhaps you could talk to him about it?"
      },
      {
        "id": "nhe2ex8",
        "score": 50,
        "body": " No I'm not going to sue my parents. My mom was 15 when she had me. My father was also a teenager. My mom has a traumatic brain injury from a head injury when she was 12. She was never capable of taking care of her self let alone children. I don't know my father well but from what I gather he had some mental trauma of his own and battles with a drug addiction till this day. I have forgiven them both. My mother may not live long and I wouldn't want to make her feel bad or like I hated her before she goes. \n\n   This is the life I was given & I have to deal with it. It's not always easy and I honestly didn't realize I was still so affected until I got that envelope. I will work through this, it is hard in this moment because for now I have to relieve the pain and deal with the flashbacks and I'm going in and out of hysterical crying fits and like this weird numb zoning out or disassociation. \n\n These feelings will pass. It's a shame that I have no control over it that I can't just toughen up and tell myself it's the past, it's over, get over it and live your life. Nothing I can do about the past so why dwell on it, why does it even bother me anyways I am in control of my life now. It's unfortunate that I can't just turn it off like a light switch"
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1mmaj56",
    "title": "My coworker got written up for intentionally jump-scaring me repeatedly",
    "body": "What the title says. This guy at work thought it was funny how severly I'd startle if he made a sudden loud noise or appeared close to me without me noticing him approach. I asked him to stop multiple times and he would always just kind of laughed it off. I didn't feel like it was something I could go to HR about. I don't want to seem like a complainer, whining about my coworker, you know? \n\nLast week it came to a head. He snuck up to where I was working and slammed his hand as hard as he could against the glass surrounding my cubicle. He was laughing until he saw that I was hyperventilating. He asked, \"Whoa! Are you ok?\" I couldn't talk and started crying and another employee ran and got the manager. Long story short, coworker got a write-up and an official warning that any further harassment would be grounds for immediate termination. I was given the rest of the day off.\n\nWhy are people like this? Why can't they understand that this isn't a joke? I'm so angry right now. Has anyone else gone through something like this?\n\nEdit: Thank you all so much for your kindness and support! I'm so grateful. So far, coworker has been avoiding me like the plague, so I think he got the message. I actually slept ok last night and I think it's going to be an ok day. Thank you all again!",
    "flair": "Venting",
    "score": 472,
    "comment_count": 75,
    "created_at": "2025-08-10T05:36:23+00:00",
    "top_comments": [
      {
        "id": "n7yyt7f",
        "score": 51,
        "body": "I\u2019m so glad the coworker and manager did something. \n\nI got told I shouldn\u2019t work in manufacturing plants if I couldn\u2019t handle \u201cthe culture\u201d (bullying, sexual harassment, and homophobia was the culture) by the HR rep when they got fed up of me calling out how they were to myself and some others."
      },
      {
        "id": "n7xs8ma",
        "score": 42,
        "body": "Not ok at all. In my opinion people do this because they feel power or control in scaring someone they know is more reactive. Doing it once without knowing is one thing, but after they ask you to stop is another. You didn\u2019t deserve that treatment and I am so sorry it has been happening. An adult acting this way is not acceptable. I would expect this from middle schoolers not an adult."
      },
      {
        "id": "n82cdj0",
        "score": 36,
        "body": "I read somewhere \u201cif both people aren\u2019t laughing, it\u2019s just sparkling abuse\u201d"
      },
      {
        "id": "n7xm4s2",
        "score": 33,
        "body": "He does it because it makes him feel powerful. Sorry you work with this jerk. All the best to you."
      },
      {
        "id": "n7x3r2b",
        "score": 32,
        "body": "My heart rate went up just reading that! Not only grounds for termination but also getting slapped hard. Sorry for you and really happy your employer reacted fairly."
      },
      {
        "id": "n7yuved",
        "score": 31,
        "body": "My ex- who was very violent and hurt me for years- used to do this and thought it was hysterical. I had the same reaction as you. It\u2019s a power thing. This is not a good guy who is doing this to you. To this day I HATE being scared. My kids did it occasionally (but not in a malicious way, and they stopped once I let them know I wasn\u2019t ok with it)."
      },
      {
        "id": "n80oynt",
        "score": 30,
        "body": "My FIL does this. No matter how much I tell him off or the rare occasion his son decides to say something he'll do it regardless. I've taken to asking why someone else's discomfort or pain is his entertainment. No answer."
      },
      {
        "id": "n7wdu5z",
        "score": 28,
        "body": "I'm sorry you had to deal with that, and glad your manager dealt with him properly. But in the future, this is actually something you should go to HR about. You have a medical condition and he was harassing you. He is lucky he wasn't fired. Hopefully he has learned his lesson now, but if he ever tried it again, report it immediately. You shouldn't have to tolerate that."
      },
      {
        "id": "n7x4eac",
        "score": 28,
        "body": "That\u2019s a good start. Keep in mind, you still work with this dick, so don\u2019t hesitate to report any further harassment."
      },
      {
        "id": "n80i12i",
        "score": 27,
        "body": "People think it's funny and don't realize how cruel it is. Especially if you have PTSD. I had a coworker who thought it was funny to startle me by saying my name really loudly and suddenly when he got to work. Luckily I told someone else that I wished he wouldn't do that because I have PTSd and don't calm down right away like a normal person would after being startled. Luckily that got around to him and he stopped doing it. \n\nYour coworker got what he deserved, you asked him to stop and he didn't."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1mjo1n7",
    "title": "Please be cautious when sharing your traumatic experiences on Reddit.",
    "body": "Small edit at the bottom. \n\nTW: Sexual Violence, Self-harm, Suicide\n\nLong post warning but I would appreciate even one person to read it and take note of the main message. \n\nI have debated whether to post about this, mostly because I feel I am to blame but if the following makes even one person take precaution and be prepared for what could come from their post, then I am happy with that\u2026 \n\nIt was 4am a few weeks back and I was in an absolute state of panic and terror. I don\u2019t want to disclose too many details in fear that someone will find my old post (on another account which I have now abandoned). I had a flashback and continued to suffer panic attacks for several hours. My throat felt like a rope was being tightened around my neck, my vision became blurry, my heart was jumping through my chest, I threw up several times, my thoughts were racing at a pace I just couldn\u2019t keep up with and I  couldn\u2019t type properly I was shaking that much. \n\nI was DESPERATE for someone to help but as most of you can relate, I didn\u2019t want to burden anybody. Not even the emergency helplines despite that being their job. So I decided to create an alt account and post on one of the subreddits dedicated to survivors of sexual abuse. I NEEDED someone to talk to, someone who could even remotely relate to my experiences. Just anybody to listen. I was in so much fucking pain, it was like my soul was being sucked from my body and it felt like it would never end. \n\nSo I posted, detailing my experience and that I needed someone to talk to, to make sense of it, to listen to me, literally just assurance that not every human being is a piece of shit\u2026 I get no comments but within minutes my DMs are FLOODED. I mean more than a dozen messages came through. What I saw made my blood run cold. \n\nI should mention here that the moderators of these subreddits make it clear that users should disable the ability for them to receive private messages, to report users to them who violate this and also to Reddit for disturbing content. But I was new to these communities and just in a state of panic, I never even saw those warnings. Hence, it\u2019s my own fault. \n\nThe following are samples of what I can recall from the messages sent to me by other users. I will add a spoiler as they can be very triggering and are just fucking sick. (I hope I do it correctly, I have never tried before) \n\n>!You weren\u2019t raped. You were trained like a dog and you loved it.!<\n>!It isn\u2019t possible to rape women, it shouldn\u2019t even be illegal.!<\n>!You\u2019re a whore. Your body reacted the way it did because you obviously wanted it.!<\n>!You reached orgasm and you call that rape? Lmao bitch your pussy was ready for the pounding.!<\n>!You can\u2019t call that rape, you signalled you wanted to get railed. You literally asked for it.!<\n>!They ran a train through you HAHAHA fucking slut.!<\n>!In one message, I was sent screenshots of a video where a woman was being gang raped.!<\n\nOthers asked for the disturbing details of my experience. They wanted to know exactly how I felt, what I felt, what I tasted, what I smelled etc. One user tricked me. They appeared at the beginning to be very caring, they mentioned they had similar experiences and said I could talk to them if I needed to. I took what I could in that moment and word vomited every awful thing that happened to me. How dirty I felt, details of the abuse, how many there were, how I had already showered 3 times but my insides still felt fucking disgusting.  \nThis user then proceeded to tell me they were masturbating to my messages and how hot it was. I felt violated all over again.!<\n\nI logged out of the account, I don\u2019t even remember the password, I just wanted to forget that post was even made. I just sobbed, my heart had finally fully broke. Many of you will know first hand how evil human beings can be, but this was so god damn depraved and just so cruel. Maybe for some of you this isn\u2019t a shock, but I was totally blindsided that this was even a thing. Before logging out, I checked some of their profiles and the fact that Reddit allow communities dedicated to rape fetishes to even exist makes me SICK to my stomach. The content of their posts was just too graphic\u2026 I never knew \u201cmisery porn\u201d was even a thing. \n\nFor days afterwards I just could NOT stop crying. My face was swollen, I had major headaches and I just stopped eating. My body felt like it had taken its final beating. I relapsed with self-harm after 5+ years clean before making an attempt on my life. It felt like any hope I ever had in people was destroyed beyond repair, everything was just so dark. In a moment of desperate need, complete strangers took enjoyment (YET AGAIN) in my pain and misery. In online communities dedicated to victims/survivor\u2019s of the most awful experiences life has to offer, there are literal freaks lurking these same communities to target people like me and you. \n\nAfter this experience, I have nothing left for anyone to take. I was abused for years as a child/teenager, my body became like a rag doll, limp and defenceless. People could do what they wanted because it was no longer MY body. After years of therapy, I was rebuilding my foundation and in one night of impulsiveness, total strangers broke it all over again. \n\nI don\u2019t want sympathy or pity, this was only a hard lesson learned. I just desperately want to warn you about the risk of sharing your traumatic experiences in communities dedicated to people like us. Not every person in here is human at even the basic level. I hate how bleak that sounds, maybe one day with enough therapy I can become hopeful again. \n\nThank you for taking the time to read and please be sure to share this warning with new users to your communities in the event you detect they are panic posting without knowing the risks. I want to share this post in several communities and then I will abandon this account. I made it simply because I wanted to get this message out there.\n\nEDIT: I have just come back to this post and I'm overwhelmed by the supportive comments in r/PTSD and r/CPTSD. Thank you to everyone who took the time to read and respond, sincerely. I've read every response and feel better knowing that I'm not the only one to have endured such exploitative depravity. \n\nI want to genuinely thank the mods at r/PTSD and r/CPTSD for allowing this post to stay. I was insta banned from several adjacent subreddits which is unfortunate but I respect the decision.  I really hope it remains and is used to help others who may have similar experiences.\n\nI will now be abandoning this account to focus on my recovery. I wish every single one of you the best of luck in your own journey to healing and hope you find the ability to be as kind to yourself as you have been to me. \n\nTake care and much love to you. \u2764\ufe0f",
    "flair": "CW: abuse",
    "score": 413,
    "comment_count": 69,
    "created_at": "2025-08-07T02:21:01+00:00",
    "top_comments": [
      {
        "id": "n7dbkb1",
        "score": 27,
        "body": "Shit. I shouldn't have looked at that. It made me ill and fucking enraged. When men say \"not all men\" my response is yeah, but THESE are the fucking men we deal with way too often. I am so sorry you had to deal with that. Please turn off your DMs on Reddit. You don't need to deal with that kind of bs."
      },
      {
        "id": "n7gq3uz",
        "score": 25,
        "body": "[removed]"
      },
      {
        "id": "n7ej5eh",
        "score": 21,
        "body": "So there are people who read trauma subreddits because it turns them on?\nI really didn't expect that. I don't even want to know what else people like that do."
      },
      {
        "id": "n7dyahg",
        "score": 17,
        "body": "We always had this in mind when working with SA victims support. An anonymous forum would be the perfect place for creeps to thrive.\n\nWe end up creating a closed group for people and have very few members. 60 if I'm not mistaken but it's really hard to keep the place alive.\n\nWhat I can say is nothing of that was your fault. Don't blame yourself for other people's ill intent.\n\nI hope you can be safe. Don't give up on therapy, please. You worth it."
      },
      {
        "id": "n7e5owy",
        "score": 15,
        "body": "As a man of God, bound to my wife in a marriage covenant, whom has experienced rape and sexual assault (not by my hand obviously).\n\nI apologise, sincerely.\nIt makes me sick because her I am doing everything in my power to work through my wife's trauma with her and support her in any way, and yet, there are \"men\" in the world, acting this way (demonic behaviour) and it makes my relationship with my own wife just that much more difficult.\n\nMy wife sent me this thread.\n\nAgain, I'm so sorry.\nNot all men are evil, please believe that.\n\nBeat them all, recover, come back alive and stronger \ud83d\udcaa\ud83c\udffb \nThey will detest that.\n\nGod bless you!"
      },
      {
        "id": "n7eekw9",
        "score": 14,
        "body": "Im so sorry. \n\nThank you for sharing this. \n\nIt is important for men to see what happens when women speak up for themselves."
      },
      {
        "id": "n7fyhjr",
        "score": 14,
        "body": "You deserved empathy and support in that moment. Those responses are horrific and violating and retraumatizing because they are also a form of sexual violence. I am so sorry. sending love your way and I hope your recovery goes as well as possible. Be gentle with yourself \u2764\ufe0f\u200d\ud83e\ude79"
      },
      {
        "id": "n7e9zcz",
        "score": 13,
        "body": "Jesus Christ. People can be so cruel. Thanks for the warning. Hopefully none of us will get any messages like this. But you didn\u2019t deserve that at all. I hope that you never get more messages like that. You deserve to feel safe\u2764\ufe0f"
      },
      {
        "id": "n7dxz46",
        "score": 12,
        "body": "Hey Hun. You gotta name and shame people to the mods. This isn't a place for someone to speak like that."
      },
      {
        "id": "n7cp83h",
        "score": 12,
        "body": "I am so sorry this happened to you. Thank you for warning people. I hope you find some peace and healing."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1o7a51h",
    "title": "In the spirit of transparency: let's be clear",
    "body": "Recently, a user who was banned for transphobic comments created another account to post targeted hate against our moderation team and our community. That post was quickly reported by our members and ultimately removed by Reddit on account of violating the content policy.\n\nWe\u2019re sharing this for transparency \u2014 not drama. We believe our members deserve to know how we moderate and why.\n\nHere\u2019s what we said to the individual as per their ban appeal, demanding to be unbanned immediately:\n\n> Let's be clear:\n\n> * Calling trans men men isn\u2019t transphobic. Calling trans women \u201cmen\u201d is. That\u2019s not \u201cspeaking truth\u201d \u2014 it\u2019s refusing to acknowledge someone\u2019s gender identity.\n\n> * The OP describing distrust toward trans people doesn\u2019t make it fair game to generalize or dehumanize. You could have discussed trauma and trust without crossing into transphobia.\n\n> * \u201cDisprove my claim\u201d isn\u2019t how this works \u2014 the burden of proof lies with the person making the assertion.\n\n> * Whether trans people have co-morbid mental health conditions isn\u2019t relevant here. Many do \u2014 largely because of stigma, discrimination, and exactly the kind of rhetoric you\u2019re repeating.\n\n> * \u201cBiological man/woman\u201d is a meaningless term outside of TERF and right-wing talking points. Biology is complex, and gender isn\u2019t a debate topic in this space.\n\n> * \u201cFree speech\u201d doesn\u2019t apply here. This is a private support community, not a public square. Speech here has consequences, especially when it harms others.\n\n> * Trans people are not the enemy. The fact that you felt entitled to come into a trauma-support forum to \u201cprove\u201d otherwise only confirms that your ban was the right decision. We should've left your original ban.\n\n> Ban remains permanent.\n\nWe\u2019re here to support everyone who\u2019s navigating trauma \u2014 including our trans members \u2014 and we will not tolerate hate or misinformation in this community.\n\nThank you to everyone who continues to make this subreddit a safe, compassionate space.\n\n~ The r/PTSD Mod Team\n\nStill very real. Still very much in reality.",
    "flair": "Meta",
    "score": 363,
    "comment_count": 52,
    "created_at": "2025-10-15T12:51:44+00:00",
    "top_comments": [
      {
        "id": "njqousj",
        "score": 42,
        "body": "We absolutely do not need to be gatekeeping who can experience trauma and benefit from this supportive community. Thanks for keeping it safe for all!"
      },
      {
        "id": "njnn6y8",
        "score": 41,
        "body": "Thank you so much!  As a trans person navigating PTSD myself, it means so much to see this, and the thought process the mod team uses to keep us safe.\n\n\ud83e\ude77"
      },
      {
        "id": "njp8417",
        "score": 31,
        "body": "Idk what happened but as a trans person just wanted to say thank you"
      },
      {
        "id": "njnrpjd",
        "score": 30,
        "body": "you have PTSD. You have as much right to be here as anybody else with PTSD"
      },
      {
        "id": "njqp8ta",
        "score": 29,
        "body": "I hate that \u201c\u2014\u201c is now a sign of ai. It is proper grammar that many authors and writers used long before ai was a thing, the very authors that things like ChatGPT train themselves on. It\u2019s a symbol that I\u2019ve had to unlearn using in my own writing in fear of being accused of this very thing. And yet, when I see it lately, I can\u2019t help but think the same thing."
      },
      {
        "id": "njp1q7r",
        "score": 28,
        "body": "This is the kind of moderation subreddits should have. Free speech doesn't mean freedom of consequence"
      },
      {
        "id": "njopqus",
        "score": 27,
        "body": "Thanx mods, as a trans person with PTSD, I appreciate it. I don't post pretty much at all, but knowing alone that this place exists is a relief."
      },
      {
        "id": "njo19fa",
        "score": 25,
        "body": "Thank you mods for managing this situation. I have some trauma due to a loved one being trans and the current dialog in this country around trans people and seeing that post would have been very triggering for me, and I\u2019m sure even more so for trans people here. I appreciate you taking action and making this a safe place for trans people and their loved ones."
      },
      {
        "id": "njno07l",
        "score": 25,
        "body": "Oh my god thank you. Thank you."
      },
      {
        "id": "njns2ur",
        "score": 25,
        "body": "Preach it, trauma brother/sister/sibling mods! Damn fine moderation right there."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1mzkk69",
    "title": "I found a homemade DVD of my stepfather abusing me",
    "body": "My stepfather abused me when I was a little girl. My mind hid all the sensations and details; I only remembered what happened, and that's why I hated my stepfather. During lockdown, I bought an old MacBook with a disc drive. I went down to the basement to look for movies and family memories to watch. And that's where I found many DVDs of my stepfather abusing me. It was totally shocking. Those sensations and feelings that my mind had suppressed, when I watched the DVD, came back so vividly that they overwhelmed me. I remembered every detail, every sensation. And it shocked me so much that I didn't know what to do. It completely changed the image I had of him; it confused me a lot. I no longer felt hatred toward him; it made me rethink many things. I felt shame and guilt for the feelings I had felt as a child.\n\nHe passed away last year, so there's no one to blame. My mother didn't know; she was working as a babysitter outside the home while this was happening. I don't have money for therapy yet, so I hope someone can talk to me and understand me.\n\nI'm Spanish and I'm helping myself with Google Translate. If something is misspelled, that's why.",
    "flair": "CW: SA",
    "score": 358,
    "comment_count": 77,
    "created_at": "2025-08-25T08:05:22+00:00",
    "top_comments": [
      {
        "id": "namot9u",
        "score": 58,
        "body": "This is horrible advice. Talk to a counselor."
      },
      {
        "id": "namuv81",
        "score": 50,
        "body": "Writing through her trauma in a journal would be better than giving material for an AI to add to its information learning caches. \n\nAI is not a verified, reliable or certified form of mental health care. AI is not designed or equipped for medical care of any kind."
      },
      {
        "id": "nannyt8",
        "score": 28,
        "body": "Did you ask OP's permission to share their story to ChatGPT? \n\nIf so, cool. But consent is important."
      },
      {
        "id": "naqta69",
        "score": 27,
        "body": "In some countries, the authorities have help for victims, so even if you don't have anyone to prosecute, speaking to the police may open doors to therapy and help regardless."
      },
      {
        "id": "nap2iv1",
        "score": 26,
        "body": "Omg im sorry :("
      },
      {
        "id": "namzeii",
        "score": 26,
        "body": "Baby i am so sorry \u2026 My heart literally aches reading your post \u2026 I really do hope that you have a good support system :( \ud83d\udc95"
      },
      {
        "id": "nanhyjl",
        "score": 24,
        "body": "I am so sorry. I have repressed memories, and it might help to see it like this; those memories are back now and can be dealt with. You can journal about them and process them, and eventually get some therapy and truly heal. Please know that what happened wasn't your fault and try to be extra kind to yourself."
      },
      {
        "id": "nana4px",
        "score": 23,
        "body": "Don't blame yourself for what you experienced as a child, you didn't consent to the situation and we're not in control of his choices. He was clearly not a good person but a pedophile who was acting out his pathology on a victim. That should not have been allowed to happen. Be greatful that he is dead and please continue to view him as the perpetrator and child sexual predator he was when he was alive. This is abhorrent and he has no excuses. You on the other hand, have every excuse, a child can't make these choices for an adult."
      },
      {
        "id": "nakx805",
        "score": 23,
        "body": "There\u2019s some other subs that will be very helpful through this as well, friend, this one is great, but you\u2019ll want more outlets. Keep talking, keep reaching out, you\u2019re very much not alone. \n\nr/CPTSD\nr/TraumaToolbox\nr/DadforaMinute or r/MomforaMinute if that sort of thing would be helpful."
      },
      {
        "id": "nalf6zh",
        "score": 21,
        "body": "This is the worst title I\u2019ve read on Reddit. So sorry."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1opdm8b",
    "title": "I\u2019m tired of people using the term ptsd lightly",
    "body": "I\u2019ve had it with hearing people using \u201cptsd\u201d to describe anything from trauma, trigger, anxiety or make a joke and I\u2019ve decided to try to speak up about it\u2026 \n\nwell I just ran into a post where I tried to explain (I think politely) that if op thinks they have ptsd they can go and check themselves but otherwise please don\u2019t use the term. I\u2019m somehow getting downvoted for that. How are we supposed to politely tell people \u201cif you think you have ptsd, go check yourself. Otherwise, please don\u2019t use the term\u201d Is it too much to ask? \n\nAlso that\u2019s some random post on Reddit. How am I supposed to say it in real life when people are making jokes that traffic to work gives them PTSD?!",
    "flair": "Venting",
    "score": 341,
    "comment_count": 152,
    "created_at": "2025-11-05T20:06:34+00:00",
    "top_comments": [
      {
        "id": "nncg67u",
        "score": 23,
        "body": "Thank you!!\nMy PTSD is from decades of being a 1st responder, as well as military and contract security work.\nAdd in a little child abuse and molestation for good measure. \n\nI get so pissed when I see people on here saying \" someone gave me a dirty look and now I have ptsd\"..or some other BS.\n\nNo, you're upset, that's not PTSD!!"
      },
      {
        "id": "nnaz40f",
        "score": 18,
        "body": "[deleted]"
      },
      {
        "id": "nnce81f",
        "score": 18,
        "body": "It is extremely frustrating. Im a female and prior military so when I talk about my cptsd they always assume only combat related and wont accept answers of not wanting to discuss it. While ptsd can happen to anyone from anything the brain seems as traumatic, its not from a minor inconvenience."
      },
      {
        "id": "nnc4v32",
        "score": 18,
        "body": "Heard and FELT. Do most people have traumatic experiences? Yes. Do most people develop ptsd? Definitely not. My symptoms on and off have crippled me and impacted my daily life. Fully trusting people won\u2019t be a thing for me ever again. No matter how many times I talk to my loved ones about my ptsd, they say they understand but then still are ableist in action (like expecting me to be at full cognition in an environment that\u2019s triggering to me and irritated with me when I\u2019m not). There are things in this life I\u2019ll never be able to do or do again because of my PTSD. I also got my ptsd from a physical attack from someone muuuuuch stronger than me and I almost died, so it\u2019s really upsetting to hear jokes about it or people improperly using it. \n\nI think it\u2019s acceptable to say that \u201cwhile trauma is common, ptsd isn\u2019t and using the two interchangeably makes it harder for those who most likely have ptsd to recognize it, validate themselves, and get help.\u201d If someone gets upset at you for saying that, I would reply with \u201cIf there\u2019s small changes I can make in my language to help others, I want to do it. Compassion is free, community health matters.\u201d then leave it at that."
      },
      {
        "id": "nng0k94",
        "score": 18,
        "body": "I weirdly don\u2019t feel the same although I don\u2019t blame you. I think I don\u2019t trust anyone to understand what PTSD is really like until I meet them. I only have one close friend who actually has PTSD and her and I can talk for hours and share the truth about what it has done to us and everyone else when they use it idk I just know they have no idea what they are talking about and I don\u2019t even consider it the same word. Like I think there is a colloquial PTSD that people use that means \u201cit reminds me of something that made me feel mildly upset\u201d and then there is OUR PTSD which is like \u201can involuntary maladaptive and often destructive or distressing bodily reaction to triggers that remind us of what happened to us in the past\u201d you know? So yeah, f@*! em for using our word and diluting its meaning for their insidious experiences! Haha but at the same time idk somehow I have found peace with it I think because I don\u2019t expect anyone to understand me unless they truly show me they do. And I dont really care if they don\u2019t because I at least know one person who does and that\u2019s enough for me"
      },
      {
        "id": "nncnikb",
        "score": 17,
        "body": "Bipolar disorder enters the chat"
      },
      {
        "id": "nnb2hcy",
        "score": 17,
        "body": "Yea I was down voted to hell over a year ago cause I said we shouldn't go around saying everyone has ptsd after covid. I tried explaining that it kind of erased people with ptsd who did struggle with helping people understand their symptoms. I wasn't being a jerk but asking for specific usage with ptsd is equated to invalidating struggles and trauma. It's really frustrating how people don't respond well to trying to course correct the term."
      },
      {
        "id": "nnihf3k",
        "score": 17,
        "body": "Agreed. Terms like this are becoming so common in everyday language and it\u2019s infuriating. \n\nPeople on social media saying a haircut gave them ptsd, or joking or using a term lightly like saying they\u2019re so depressed etc or that something is triggering their ocd is so disgusting. \n\nIt makes people who actually suffer feel degraded, and I don\u2019t think it should be okay to say unless you are actually diagnosed. \n\nI also hate when people blame things of their \u201cadhd\u201d or \u201cocd\u201d for example, when they\u2019ve never been diagnosed. If you haven\u2019t been diagnosed you can\u2019t claim you have something to others."
      },
      {
        "id": "nnbevh5",
        "score": 17,
        "body": "I\u2019m like this with \u201ctrigger\u201d.\n\nI get it, whatever. But girl your trigger is not the color blue and all caps in discord. \n\nI am NOT for self diagnosis\u2026 I am a prime example. Self diagnosed with depression and anxiety, found lazy ass doctor who said \u201cyep\u201d and put me on SSRIS, had me frothing at the mouth thinking I was god 6 states away ruining my life for 3 weeks. Not depression and anxiety btw. I get it, finding a doctor who cares and isn\u2019t expensive sucks, but self diagnosing is so dangerous. It\u2019s not a cold or stomach bug or pregnancy.\n\nC-PTSD, BIPOLAR 1!!, ADHD, Panic Disorder. Yeah that self diagnosis journey was so great."
      },
      {
        "id": "nnb48uh",
        "score": 16,
        "body": "Speaking up will always come with backlash unfortunately. Proud of you for advocating for your community though. Some people just don\u2019t understand that PTSD doesn\u2019t need a trigger. PTSD is immobilizing, PTSD can look like OCD and Borderline Personality Disorder and Bipolar disorder. I wish people would stop using the term lightly too, because then we don\u2019t get taken seriously when we suffer our symptoms."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1m5wpma",
    "title": "What\u2019s the one thing you HATE people saying about ptsd",
    "body": "Was told at work by a coworker, as we were discussing MH issues and I brought up that I have PTSD. He replied by saying \u201coh I know some guys with proper ptsd from the Afghanistan war\u201d like girl you weren\u2019t even in Afghanistan plus there\u2019s no hierarchy of who had it worst  ",
    "flair": "Venting",
    "score": 318,
    "comment_count": 328,
    "created_at": "2025-07-21T22:12:50+00:00",
    "top_comments": [
      {
        "id": "n4fldcx",
        "score": 47,
        "body": "When people say \u201comg that gave me ptsd\u201d and it\u2019s just like a runny omelette or something."
      },
      {
        "id": "n4ieq56",
        "score": 35,
        "body": "For me it's the opposite. I was a military medic and, when I talk about the difficulties I face, I often get the response \"well, everyone's a little bit PTSD so it shouldn't be a big deal for you\" and then they get mad at me when I go \"oh! Did you also get the image of a friend's body torn apart by a grenade stuck in your mind when that concert at the park ended with a surprise fireworks show? Hate when that happens right before the weekend, I wanted to go to the beach\"\u00a0"
      },
      {
        "id": "n4fvym4",
        "score": 34,
        "body": "[removed]"
      },
      {
        "id": "n4gakvh",
        "score": 32,
        "body": "My cousin recently told me that I need to \u201cstop telling people you have PTSD\u201d. It really hurt because I have been fairly silent the past five years about it. I have finally opened up about my experience more publicly with encouragement from my therapist in hopes to heal and help others experiencing domestic violence. \n\n\u26a0\ufe0fTrigger warning:\n\nFor context I witnessed someone take their life with a firearm."
      },
      {
        "id": "n4gdohr",
        "score": 31,
        "body": "Oh, are you a veteran?!?!?\n\nNope, just sexually abused by uncles"
      },
      {
        "id": "n4faqzv",
        "score": 29,
        "body": "One of my friends recently discovered he had PTSD, and I opened up to him that I had it too. He got it from his rough home life, and he knew mine was better, so he asked me how I got it and I explained that it was from the mental institution I was put in a few years ago. \n\nIt\u2019s not easy for me to talk about it. I usually just refer to it as \u201cthe bad place\u201d because calling it what it is makes my heart hammer. I opened up to him and he said I had \u201cwimp PTSD\u201d and explained how he had it worse.\n\nHe didn\u2019t know I saw someone die in there. He didn\u2019t know I was trapped for 53 days. He didn\u2019t know I was only 13 years old and he didn\u2019t know I thought I\u2019d die in there too, but to this day what he said really sticks with me. It gets in my head and calls me weak and pathetic. I can\u2019t be mad at the guy, he just didn\u2019t know and I never told him."
      },
      {
        "id": "n4i50yp",
        "score": 29,
        "body": "\u201cHow can you have ptsd? You\u2019ve never been to war."
      },
      {
        "id": "n4f80uf",
        "score": 26,
        "body": "I hate when they say \u201cyou don\u2019t change the past but you can control your reality\u201d like hold on let me just bang my head against the wall to restart my life and forget 10 years of trauma and abuse"
      },
      {
        "id": "n4hd8z7",
        "score": 25,
        "body": "\u201cyeah, but everyone has trauma\u201d sends me.. it\u2019s like \u201ceveryone has a bit of adhd\u201d or \u201ceveryone is a little autistic\u201d\u2026  \ni do love when people try to play the trauma olympics tho because i have zero filter and am stabilised, so ill trauma dump with extreme graphic detail and they\u2019ll immediately shut the f*ck up. \nno one should have to give random people details as \u2018proof\u2019. unfortunately people who make claims of whether or not others trauma is valid don\u2019t actually want to know what happened, they don\u2019t actually care, they just want to invalidate your suffering/diagnosis. \nall trauma is valid, but having a diagnosis of ptsd or cptsd requires specific criteria to get the diagnosis."
      },
      {
        "id": "n4ldpyj",
        "score": 25,
        "body": "Soldiers are the Poster Boys for PTSD. But it's pretty ignorant to think it's only limited to war veterans. Anyone is a candidate"
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1pbqmna",
    "title": "a man in a famous texas band raped me",
    "body": "i am going to be a vague as i can per MOD rules. a couple of years ago i was raped by the guitarist of a famous band based out of texas. i know 2 other women this happened to and i am posted this to see if there are other women and to know im here. we are resilient and we are strong. please message me if you think this happened to you.",
    "flair": "Support",
    "score": 316,
    "comment_count": 60,
    "created_at": "2025-12-01T22:14:34+00:00",
    "top_comments": [
      {
        "id": "nrstyfe",
        "score": 77,
        "body": "sending love and solidarity. i was assaulted by a major and well known person too and wish i could speak out"
      },
      {
        "id": "nrtke34",
        "score": 68,
        "body": "Well yeah me too. Very long ago. I was only 18 but was raped by a band member of a famous band. I've never talked about it and who'd even care after 50 plus years."
      },
      {
        "id": "nrti73c",
        "score": 65,
        "body": "A (married) nba player in Orlando back in the day roofied me and was trying to take me home, but my group of girlfriends were FIERCE. not today satan/ **!!   $@&%s"
      },
      {
        "id": "nrsjqx3",
        "score": 61,
        "body": "Sending love and solidarity. This shit hurts - myself and several people were raped by a man who is in some vaguely popular metal/goth bands in Montreal and it still freaks me out when I see him pop up in another artists music video or some shit. \n\nI\u2019ll never forget trying to have a community discussion about this man only to be told it was just a \u201ccocaine psychosis\u201d by the people who partied with him who I thought were also my friends (that happened over many years to multiple women \u2026 okay sure yall)\n\nBest of luck and all the love \ud83d\udda4"
      },
      {
        "id": "nrtktsp",
        "score": 58,
        "body": "who was it? people here care. people care more now than before. I\u2019m sorry that happened"
      },
      {
        "id": "nrshaii",
        "score": 58,
        "body": "i want to but the last time i did i got the post removed for doxxing. message me"
      },
      {
        "id": "nrsh769",
        "score": 52,
        "body": "Name and shame."
      },
      {
        "id": "nrsa1hw",
        "score": 51,
        "body": "he is no longer in the band."
      },
      {
        "id": "nrwp9db",
        "score": 49,
        "body": "The guy who raped me in college is now the lead singer in a band that is somewhat known in the city where I went to school. That city felt like home more than any other city in this country ever did, but in the end the fear of bumping into him and the trigger of seeing his face plastered to every lamppost advertising his gigs was just too much.\n\nI\u2019m so sorry. None of this is fair. We deserved and deserve so much better than this."
      },
      {
        "id": "nrwjtnq",
        "score": 44,
        "body": "Name and shame. Don\u2019t say anything else, just names. This trash needs to be taken out."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1lijvuo",
    "title": "What Really Happened After I Took FMLA Leave for My Mental Health",
    "body": "I did everything by the book.\n\nI filled out the FMLA paperwork. I got it approved. I took a short leave to focus on my mental health, something I\u2019d avoided for years, but finally couldn\u2019t anymore. PTSD, BPD\u2026 real stuff I needed to deal with.\n\nI came back thinking things would go back to normal. Instead, the atmosphere shifted.\n\nNothing was said outright, but the coldness was obvious. I felt watched. Doubted. Then came the Performance Improvement Plan. Something I\u2019d never received before in my entire time there. It didn\u2019t come from nowhere, but it didn\u2019t make sense either. Suddenly, my work was being scrutinized in ways it never had been. The timing? Just a few weeks after my FMLA leave was approved.\n\nAt that point, I knew what was coming. The PIP wasn\u2019t about support,  it was about setting up the next move.\n\nEventually, they fired me. And the official reasons?\n\nI ordered too much food for a client dinner and I missed a showroom graphic.\n\nThat was it. Not the PIP. Not my performance. Just those two incidents. Small things that would\u2019ve been handled with a conversation in any normal situation. But by then, the decision had already been made. I wasn\u2019t a safe employee anymore.\n\nThis is what retaliation looks like in 2025. Not a dramatic blow-up, just a slow, quiet push out the door, dressed up in HR language and concerns.\n\nAnd the worst part? It\u2019s not rare.\n\nI\u2019m not sharing this because I want sympathy. I\u2019m sharing it because people need to understand that FMLA isn\u2019t always the shield it\u2019s supposed to be. Mental health \nawareness is one thing. But when you actually need support, it can cost you everything.\n\nIf any of this sounds familiar, if you\u2019ve been punished for asking for help,you\u2019re not alone. And you\u2019re not crazy.",
    "flair": "Support",
    "score": 299,
    "comment_count": 74,
    "created_at": "2025-06-23T15:40:14+00:00",
    "top_comments": [
      {
        "id": "mzcmez8",
        "score": 26,
        "body": "You nailed it. I\u2019m in management and have been in the room during many discussions about people that become \u201cproblems\u201d. They absolutely conspired to get rid of you. They would not give you time for lunch if it wasn\u2019t dictated by law."
      },
      {
        "id": "mzcoyck",
        "score": 26,
        "body": "Yep, it's 100% real, even in places where they push out loud how \"aware\" they are.\n\nMy concern for this happening to me is exactly why I want no documentation whatsoever by my employer in reference to any \"behavioral health\" issue.\n\nIt isolates me in a way, because I have to keep my struggles to myself and sometimes my frustration and pain appears to lack context that I could provide in a real, actual supportive environment (as in, not in the workplace where it's a luxury to be human). \n\nIt just reinforces that yucky old \"trust no one\" feeling that poisons every decision tree I have at my disposal. But I get to keep my job and have a home to live in, so there's that, I guess."
      },
      {
        "id": "mzdn22i",
        "score": 23,
        "body": "Please call an employment lawyer. Many of them work on contingency (they only get paid if they get you a settlement or win at trial) and will give you a free consultation."
      },
      {
        "id": "mzdva8s",
        "score": 23,
        "body": "Similar thing happened to me. I took FMLA to attend court for my sister\u2019s murder. Even though I was outperforming the rest of the team combined I got a written warning for tardies (5-15 minutes max, I was having heavy nightmares and it made it hard to wake up). Outrageous how little they care when life happens. \n\nHR had some bogus solution that would be taking a major pay cut and more time off than I needed. I wound up finding a new job because I couldn\u2019t stand the indignity of it anymore.\n\nEdit: accidentally a word"
      },
      {
        "id": "mzgjauw",
        "score": 22,
        "body": "nine normal upbeat thought worm spoon pause roll apparatus birds\n\n *This post was mass deleted and anonymized with [Redact](https://redact.dev/home)*"
      },
      {
        "id": "mzcnhs4",
        "score": 20,
        "body": "It has happened at almost every job where I've taken FMLA. My first job where I took it was the only one that was understanding and I lasted another 3 years after my leave. But my most recent job where I took FMLA was the worst. I came back and no one would talk to me. No one would acknowledge my comments in our Team meetings. And I had been gone for 6 weeks and not a single person had reached out to me. One girl who I had been close with shut me out completely and kept sabotaging my tasks (Telling the boss I wasn't doing certain tasks, when she had never passed on the message to me, Taking a task from me and claiming she was picking up my \"slack\" when she just did it before I could) until I finally just quit. Not a single person said goodbye to me on my last day, and this team was *tight*. We would all hang out on weekends, host parties, go camping. And I was just cut off. I decided after that to never be open about my mental health issues again. Like, I'll take FMLA again if I need it but I'm definitely going to say it's a family members health concern."
      },
      {
        "id": "mzft49t",
        "score": 17,
        "body": "Thank you for bringing awareness to this."
      },
      {
        "id": "mzdeuqo",
        "score": 16,
        "body": "[removed]"
      },
      {
        "id": "mzih1j2",
        "score": 16,
        "body": "Speaking from experience please document everything every situation every conversation take screenshots of messages document things even if they seem silly. Good luck!"
      },
      {
        "id": "mzf6nkz",
        "score": 14,
        "body": "[removed]"
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1qw6in5",
    "title": "Everything coming out about the Epstein files is making me feel so retraumatized",
    "body": "I just need to rant because i\u2019m sure plenty of other people in this sub feel similar and I\u2019m looking for some mutual support. \n\nI\u2019m sure other people feel like me, like they remember being in situations that mirror the ones of the files victims. Every exchange between these men reminds me how they see us as prey. \n\nI feel like prey again and it\u2019s making me feel sick. These men made me an anorexic and obedient pure submissive child. We were all fucking conditioned. \n\nI haven\u2019t had nightmares for a few months but they\u2019re back and worse than ever now. My ptsd symptoms have been worsening. I feel constantly reminded of all the things men got away with doing to me, things I couldn\u2019t even report and never got justice for. \n\nHugs to everyone ",
    "flair": "Venting",
    "score": 278,
    "comment_count": 77,
    "created_at": "2026-02-05T00:44:46+00:00",
    "top_comments": [
      {
        "id": "o3n77zu",
        "score": 20,
        "body": "The lack of justice is the hard part for me, and I don't believe that even if direct and very clear evidence along with full confessions were in evidence that justice would be done. \n\nI find myself fighting the dark hopelessness that goes in tandem with the lack of justice, and I refuse to let that space reclaim me, so I'm using as many coping skills as I possibly can right now. \n\nSome of that includes avoiding (as best as I can) political things, because too many people in politics are connected (or have their own skeletons that I know may not be related but echo that irreverence for the dignity of other humans). Some of that includes focusing on as much beauty as I can, when and where I can. Some of that means staying away from TV shows that include trauma or harm (I used to binge British Baking Show, and I'm trying to find as many shows that have that same feel even if it's a different type). And some of it is simply holding on as best as I can through some days. \n\nIt's so hard right now, and it's so important to find the points of light in the darkness, whenever and wherever we can."
      },
      {
        "id": "o3n9brk",
        "score": 12,
        "body": "May you find some comfort in Pete Walker\u2019s tips to handle emotional flashbacks at https://pete-walker.com/pdf/13strategies_flashbacks_management.pdf"
      },
      {
        "id": "o3n1i1o",
        "score": 11,
        "body": "Yes I have a very hard time with it. Very much triggering. I'm sorry to you and anyone else suffering through these difficult times.  Sending lots of love and prayers."
      },
      {
        "id": "o3pna7o",
        "score": 10,
        "body": "My real trauma was the years long cover ups and the institutional bullying from powerful people.\n\nThis is breaking me. I can't handle seeing powerful people just get away with the worst crimes imaginable. Like they're walking around free.\n\nThere is no justice."
      },
      {
        "id": "o3rn8aa",
        "score": 9,
        "body": "Honestly I\u2019d say to be very mindful about social media and media useage at this time as it\u2019s triggering as FUCK . Even if you wanted to avoid it \u2026. It\u2019s hard . But I\u2019d advise everyone to have a mindful block , delete and input day - as it\u2019s incredibly important to mimimise the ugly noise of this . Stick to kitten posts and trivia \u2764\ufe0f"
      },
      {
        "id": "o3ntcym",
        "score": 8,
        "body": "It\u2019s so difficult. My nightmares have gotten insane, I feel so sad. Just so so sad."
      },
      {
        "id": "o3mto59",
        "score": 8,
        "body": "Yeah I have a hard time with it too. I can't read any of the files. I don't want to see the pictures. All of it is a reminder that they can get away with it."
      },
      {
        "id": "o3mzz55",
        "score": 8,
        "body": "It's an outrage, and even more of an outrage is that they are still walking around without being charged. What a slap in the face for justice! I am so sorry you are going through this and that these terrible people are not incarcerated. Also, remember that you don't have to look at any of it - secondary trauma is a real thing too!"
      },
      {
        "id": "o3pbc9i",
        "score": 8,
        "body": "I was doing pretty good with just reading about it. But the pictures coming out have me getting the craziest flashbacks. Now my mind has started obsessing over it and I just feel disgusting inside and out. Especially the thoughts of everyone being evil around me."
      },
      {
        "id": "o3pdrf6",
        "score": 8,
        "body": "Was just talking to my therapist about this. It feels disgusting. Just disgusting. It's not just the information but it feels like subtext to society that we are just casually fine about PDFs and SA. \n\nEven trying to get my mind off of it. 28 years later is also doing this. I was just annoyed as like Ralph Fiennes but it also feels they just shoe horned in a reference to a PDF which isn't a reference to the time frame. \n\nFuck this world. But I have to do just media black out."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1prvmo8",
    "title": "survivor of brown shooting, not doing well",
    "body": "hello r/ptsd, happy holidays, hope everyone is staying safe\n\nlast week i was involved in the horrific events that took place at brown university. i was in the room with the shooter, heard the shots, and escaped unharmed. miraculously i am home safe now with my family, but not doing well. there are times throughout the day when i don\u2019t feel safe, i feel like the shooter is right behind me again and i need to take cover or barricade the door. i am very irritable, keep lashing out at the people i love, want to isolate, and am going in and out of states of numbness. i oscillate between feeling starving and too sick to eat. i dont feel like myself at all.\n\ni was wondering if anyone here could give me any guidance on what to expect in the weeks to come, or what i can do to help set myself up for the best road to recovery. will it ever end? will i ever be able to get my old life back? it feels like everything changed in such a short time. how do i approach my family members, who don\u2019t understand?\n\ni feel so lost and confused, and am wrestling with so many conflicting feelings. any advice or support from other survivors much appreciated\n\nthank you",
    "flair": "Advice",
    "score": 261,
    "comment_count": 80,
    "created_at": "2025-12-21T02:40:55+00:00",
    "top_comments": [
      {
        "id": "nv5iqzi",
        "score": 29,
        "body": "Hi friend,  \nI'm so sorry that you had to go through this. I survived the mass shooting in Las Vegas 8 years ago, so I understand what you are going through. I had a lot of the same symptoms that you are having in the early days. So jumpy, feeling so unsafe all the time, I didn't eat for like 5 days afterwards.\n\nSome thoughts and advice:\n\n\\-You just went through something that changes the way that you see the world. You're going to have a hard time figuring out how this experience fits into your worldview. You're going to see everything differently. You know a truth now that the people around you have the privilege of not knowing, and that is going to make you feel different from other people. But even though you feel distant from other people, talk about what you went through. Don't isolate yourself. Go out in the world and show yourself that just because one dangerous experience happened doesn't mean that you are always in danger. \n\n\\-You might have a hard time with your sleep. Medication can help your body to learn how to relax again. You might also want to get your cortisol levels checked if the sleep issues go on for a long time. My cortisol started to spike in the middle of the night after my experience, and would cause me to wake up in the middle of the night.\n\n\\-You might feel like you are a different person than you used to be. Going through something like this changes you, and one of the hardest things for me was accepting that I would no longer get to be the version of myself that I was before the shooting. 8 years later, I appreciate this version of myself, because I have been through a lot and come out the other side. Be patient with yourself. Allow yourself to grieve. \n\n\\-Therapy is immensely helpful as you are adjusting to life as a survivor. You will probably qualify for victims of crime compensation, which can help you pay for therapy. Ask the police department about this.\n\n\\--Time will move forward, and things will feel less intense as time goes on. Right now, it probably is taking up all of your waking thoughts. It did for me, too. But I promise you, there will come a day when you realize that you didn't think about it. And then there will be multiple days. It will happen, but it takes time, and you can't make it happen faster than your brain is ready for it. Take things at your pace. Be gentle with yourself. Rest. Talk about it. Take care of your body. Cry. Laugh. Allow yourself to be a human.\n\nI'm so, so sorry that you are now a member of this club of survivors. Please know that you have so many people around the world whose footsteps you are following in, and whose thoughts are with you and the other survivors from Brown."
      },
      {
        "id": "nv9tpny",
        "score": 20,
        "body": "You need to see a therapist asap and in the meantime, play tetris, I read that helps somehow"
      },
      {
        "id": "nv5s3dk",
        "score": 19,
        "body": "My condolences.\n\nYou saw people you knew suddenly and senselessly killed in the same room as you.\n\nI\u2019m not going to sugarcoat it: you *will* live with this experience for the rest of your life, and it\u2019s going to have a lasting and permanent effect on you. Therapy might or might not be effective, but it\u2019s always better to try, and the sooner, the better.\n\nTrauma doesn\u2019t disappear, it can ebb and fade over time and with help, but it never truly goes away. \n\nI was raped at knifepoint 15 years ago and despite years of therapy and being prescribed prazosin for nightmares, I still regularly have vivid nightmares about it, and wake my husband up screaming in my sleep.\n\nYou can expect to be emotionally detached, not feeling like yourself, and feeling like you\u2019re constantly in fight or flight mode. This will diminish over time, but right now it\u2019s raw, and likely feels like it won\u2019t ever end. \n\nYour experience was extremely publicized. If I were you and my family members somehow didn\u2019t understand, I\u2019d show them the headlines. You were one psychotic person\u2019s trigger reflex away from death, and if your family cannot understand how that affects you, they are wrong, not you.\n\nMy heart goes out to you."
      },
      {
        "id": "nv7cdqa",
        "score": 19,
        "body": "Please get EMDR right away. Traditional talk therapy didn\u2019t cut it for my PTSD symptoms and I suffered needlessly for a long time.\n\nI experienced the lashing out at people I loved, isolation, flashbacks, hyper vigilance- all of it.  I isolated myself and got much, much worse. I ended up drowning in self loathing and shame. Please don\u2019t do this to yourself. \n\nDon\u2019t isolate and get help. This is an injury that time alone will not heal."
      },
      {
        "id": "nv6u77e",
        "score": 18,
        "body": "I would go to a trauma informed therapist immediately. Not everyone develops PTSD, and your chances are better if you go early. \n\nNo matter what, you've been through a traumatic event that would traumatized anyone. You are safe now, even if you dont feel like it. It sucks, but youll get through this. Surround yourself with loved ones and be patient with yourself."
      },
      {
        "id": "nv4yrng",
        "score": 17,
        "body": "What you\u2019re describing are things common among recent trauma survivors. In the days and weeks after trauma, things like feeling on guard, being irritable, feeling numb, having appetite changes, and feeling unsafe can be very common. It doesn\u2019t mean this is how it will always be. Many trauma survivors do slowly find their footing again, even if it doesn\u2019t feel possible right now.\n\nIf you can, gentle things like sticking to basic routines, grounding exercises, and limiting news exposure can help a little. Trauma-informed therapy can also make a big difference. You may also wish to talk about your symptoms with a doctor and see if medication can help, especially if you find yourself experiencing sleep disturbances.\n\nWhen it comes to family who don\u2019t understand, sometimes it might help to say something simple like: \u201cI experienced trauma and am still early in the healing process. Please be patient with me.\u201d\n\nIt\u2019s feels hard and insurmountable at first, but many survivors go on to cope and can manage symptoms well in everyday life when they arise. Give yourself time and grace. Take things one day at a time"
      },
      {
        "id": "nv76ki3",
        "score": 17,
        "body": "A therapist once told me: Getting PTSD is like being dropped in the middle of the ocean. At first, the waves are enormous, you keep going under, and it\u2019s very overwhelming and terrifying. Eventually, you start learning how to swim with the waves. It takes a lot of time. But it will get better. I was diagnosed five years ago, and the difference between then and today is apparent. \n\nI\u2019m not \u201cbetter\u201d nor will I ever be, but I can at least tell when the storm is coming now."
      },
      {
        "id": "nv5bs9u",
        "score": 15,
        "body": "I'm really sorry that happened to you and you aren't alone.\n\nWhen I was 14, I had to protect my sister from a peer trying to murder us. We were trapped in his family's house, not knowing if we\u2019d make it out alive. In my late 30s, I still remember it like yesterday.\n\nThe intensity gradually decreases and can stabilize.\n\nLet's go over a couple key points:\n\nYou were in the same room as the shooter. This, which you'll either find out soon from a therapist or already know, creates captivity trauma.\n\nWhen this occurs a part of you feels like you're still trapped in that room and like that moment is still happening. It's why many say Bruce Wayne is still the scared kid in the alley. Our nervous systems freeze in that moment. I wish I could say that goes away, but I still feel like I'm trapped in that house around 25 years later. However, the pain and fear decreases with time.\n\nEven though you \u201cescaped unharmed.\u201d In near homicide incidents, our nervous system can register it as if we did die. That's one of the most brutal aspects of near homicide trauma. Ever since then I've felt like a ghost, half alive, and like I am living on borrowed time. That isn't on survivors, it\u2019s a natural part of it.\n\nOur hypervigilance becomes more heightened than most people with trauma because what we experienced is severe. Since that night I've always felt like somebody was waiting to ambush and kill me. Walking into a pitch dark room paralyzes me with terror. Again, that isn't our fault.\n\nIrritability, lashing out, wanting to isolate isn't a fault of your own either. My mom didn't understand. She called it my \"mean phase.\" She had no idea how much I was actually hurting. She was also too scared to face it. Your behavior isn't because of anything you did. It stems from you naturally still feeling on edge. You are responding how anyone in near death situations does. You aren't alone.\n\nStates of numbness - definitely. I fluctuate between drowning, heavily disassociating, and times where it doesn\u2019t haunt me. I almost made a senior thesis film about the attack. In a video I made depicting who I am it starts with an image of teen self harming. At the time I told my professors I was perfectly healthy. Looking back that level of disassociating is haunting at how much I sometimes couldn't see what I was feeling and going through. Apparently that\u2019s common.\n\nExperiencing a near homicide for many, including myself, is identity changing. You went through more at a young age than most will ever have to deal with in their entire lifetime. That is why it feels like many ranging from family to others who didn't go through it can\u2019t understand. It's isolating because of how rare surviving a near homicide is.\n\nI don't want to serve up any false platitudes. I know when I was young I never would have believed them and they made me feel more alone so I'll be honest.\n\nDoes it ever go completely go away? No, but it does get better. We have experiences akin to what soldiers have. We didn't volunteer to go war, but we have shocks as if we did. Soldiers aren't ever the same after, neither are we. But our lives can stabilize and good things can still happen for us.\n\nWill you ever get your old life back? Yes and no. Can you have love for the things you used to? Yes. Can you completely forget what happened? No. You don't want to either even though it seems like it would be better; I significantly disassociated starting in college and I'm just now getting those emotional memories back so I can heal. The only way to get better is through it rather than avoidance. Avoidance  or disassociation leaves pain, but no way to heal.\n\nI'd say be open with your family and explain how much pain you feel. In 2002, psychologists said that adolescents bounce back and don't feel trauma - that hurt me a lot; it was maladaptive. Today everyone knows adolescents experience trauma, thus they'll respond with more understanding. Connecting is healing.\n\nConflicting feelings is normal and it's part of the trauma. Most with trauma deny how hurt they are. That goes doubly for us. Some days I acknowledge what I lived through hurt me. Other days I wonder why I felt pain over being almost murdered and wonder if I\u2019m in the right to feel pain over it; to stop there - it is absolutely normal and natural to be devastated by a near homicide, our minds just sometimes makes it difficult to accept that. It's all part of it.\n\nI felt like something was inherently wrong with me and that\u2019s why it happened to me. It wasn\u2019t. But trauma can lead to that perception and it hurts a lot more when the trauma is a near homicide.\n\nThere is also survivor's guilt. I blamed myself for the attack. Being in the house, not noticing the signs sooner, not acting fast enough, wondering why I survived. These are all very natural responses to have. You are not to blame for what happened to you. Let me repeat, what happened has nothing to do with what you did. It wasn\u2019t your fault. It wasn\u2019t your fault at all.\n\nHow can you recover? Seek out a specialist that deals with violent life or death trauma. Hopefully your school will have the resources for you. If not, ask your classmates (everyone is struggling right now). If you're nervous about doing so, that's okay and understandable - look online at places like Psychology Today particularly for therapists well versed in domestic violence, first responder and veteran trauma, and working with the body (EMDR) and parts (IFS).\n\nTalk therapy doesn't really help much in these regards because what we survived lives in our bodies instead.\n\nThere are specialists available who can help you.\n\nThe aftermath is difficult. I survived, lead a moderately balanced life and I'm very successful career wise. You can too. I'm here if you need an ear.\n\nAdding: Some single lethal event survivors may stabilize sooner. I was in two situations where I had to prevent family from being killed, at 14 and 19; thus, some aspects may be intensified because of that."
      },
      {
        "id": "nv57xrq",
        "score": 15,
        "body": "Play tetris immediately."
      },
      {
        "id": "nv5jy1v",
        "score": 14,
        "body": "Find a counsellor who is trained in trauma therapy. Do this sooner than later, and go for at least a couple of months. So many people start counselling with the expectation it will cure their trauma overnight. It doesn\u2019t, so stick with it. \n\nSorry this happened to you. There is hope; you will feel better with time and support."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1nve17z",
    "title": "\u201cThe single greatest mistake in medical history\u201d: doctors believed infants couldn\u2019t feel pain \u2014 my story.",
    "body": "Until the 1990s, doctors believed that infants couldn\u2019t feel pain. This was based on incorrect research: studies had claimed the infant brain wasn\u2019t developed enough to actually interpret pain. \n\nFor decades, infants were treated horrifically in surgery. Over a period of nearly sixty years, millions of children were operated on without proper anesthesia or sufficient pain management. It wasn\u2019t until 1985, when a child died after open-heart surgery with no anesthesia, that there was a push for change. Dr. David B. Chamberlain has called it, \u201cthe single greatest mistake in the whole of medical history.\u201d\n\nMost adults affected by the denial of infant pain are still not being helped. Many people don\u2019t even know they were affected as infants. They stumble through the system getting labels and medications that never touch the root cause.\n\nSome of this lack of support is structural: the American Psychiatric Association does not include Developmental Trauma Disorder (DTD) in its list of officially recognized conditions, even though experts have urged its inclusion for years. Its absence blocks research funding, leaves practitioners without proper tools, and prevents insurance from covering treatment.\n\nDTD identifies trauma in childhood as having a unique and lasting imprint on the brain and body. It has been tied to conditions like heart disease, fibromyalgia, digestive issues, autoimmune disorders, and postural conditions. Understanding these connections can lead to more effective treatments.\n\nDTD is not just psychological. It\u2019s an injury to the nervous system, affecting people through their entire adult life.\n\n\u2014\u2014\u2014\u2014-My Story\u2014\u2014\u2014\u2014\u2014\u2014\n\nI was born in 1984 with a misshapen leg, and only three fingers on my left hand. At six months old, doctors amputated my right foot and used a bone saw to split my left hand into two fingers. My records show I was highly distressed and shaking uncontrollably in recovery. \n\nAt age two, surgeons cut my right femur in half and bolted it back together with metal pins that stuck out of my skin. I was placed in a body cast from chest to thighs. For a toddler, that kind of immobilization is now recognized as highly traumatic.\n\nAt age four, doctors tried the same surgery again. My medical records quote me saying, \u201cPain is so bad, cut my leg off\u2026 feels like it\u2019s separating apart; it\u2019s moving, it\u2019s jumping.\u201d \n\nThere were more surgeries: another osteotomy, a growth plate fusion with near-death-experience compilations, and a revision amputation. I never received any trauma care or trauma-informed care. Even into adulthood, no therapist explained why my body started shaking at night, or why phantom pains returned to my amputated leg, decades later.\n\nLearning about DTD finally gave me language for what had happened to me. None of these procedures were \u201cneutral, full-recovery\u201d events as doctors told my family. Operating on me so early, under the belief that I wouldn\u2019t remember the pain, caused serious injury to my nervous system.\n\n\n\u2014\u2014\u2014\u2014\u2014\u2014-\n\nAnand, K.J.S., & Hickey, P.R. (1987). Pain and its effects in the human neonate and fetus. The New England Journal of Medicine, 317(21), 1321\u20131329.\nThis pivotal article demonstrated that neonates and even fetuses mount clear physiological and behavioral responses to pain, overturning the long-held belief that infants could not feel pain, and triggering major changes in pediatric anesthesia and pain management.\n\n\u2014\u2014\u2014\u2014\n\nThe Infancy of Infant Pain Research: The Experimental Origins of Infant Pain Denial by Elissa N. Rodkey & Rebecca Pillai Riddell (J. Pain, 2013) Examines the history of infant surgeries performed before 1987, when babies were often operated on with little or no anesthesia, and the long-term traumatic consequences of those practices\n\n\u2014\u2014\n\nEdwards, S. The Long Life of Early Pain. On The Brain. (2011) The Harvard Mahoney Evidence shows that early painful procedures in infants produce long-term alterations in pain sensitivity, stress hormone regulation, and neurodevelopment.\n\n\u2014\u2014\u2014\u2014\n\nMonell, Terry T. (2011). Living Out the Past: Infant Surgery Prior to 1987. Journal of Prenatal & Perinatal Psychology and Health, 25(3).\n\nExamines the history of infant surgeries performed before 1987, when babies were often operated on with little or no anesthesia, and the long-term traumatic consequences of those practices.\n\n\u2014\u2014",
    "flair": "Venting",
    "score": 252,
    "comment_count": 71,
    "created_at": "2025-10-01T17:07:44+00:00",
    "top_comments": [
      {
        "id": "nhb3ix3",
        "score": 52,
        "body": "There are thousands of people out there with PTSD from things they can't remember. It's not about memory. It's about the biological, chemical reaction to extreme stress, which does physical damage to the developing brain and nervous system. The body keeps the score."
      },
      {
        "id": "nh8kao2",
        "score": 49,
        "body": "They knew damn well children could feel pain. They knew damn well that abuse had lasting effects. It's a lie they told themselves so they wouldn't have to feel guilty about all those screaming male babies being mutilated under their care. And it's why it's still difficult to fund, perform or print research on the subject today."
      },
      {
        "id": "nhcm8l6",
        "score": 48,
        "body": "They believe this about black people, also. That they don't feel pain, or can handle more pain. They do it to women as well and even today say the cervix cannot feel pain. Doctors are truly evil at times."
      },
      {
        "id": "nhai12i",
        "score": 41,
        "body": "Medical trauma is so real and it's not talked about enough. It's like people think \"well they fixed you and you're alive, you should be grateful, don't you know how many people can't access medicine?\" but the brain doesn't work like that. Pain is pain."
      },
      {
        "id": "nh9iugp",
        "score": 38,
        "body": "Doctors are fucking nuts, how can you watch how easily a baby gets upset with the slightest hurt and conclude they don't feel pain?"
      },
      {
        "id": "nh9ncpz",
        "score": 36,
        "body": "Thank you for sharing this.  My toe was caught in my mother uterus after being born a few weeks early, and I had to have it reattached, was in the NICU for a month, went on to wear braces and shoes with a metal bar until age 5.  My mom Complains about the \u201clooks she got\u201d with a baby in a cast, but never once addressed what I was going through emotionally."
      },
      {
        "id": "nhaww49",
        "score": 33,
        "body": "My baby had blood sugar issues when he was born this past November. They came in and pricked his heel every few hours and would scream. It took a long time for him to feel comfortable with someone touching his foot. I felt so bad, but they were threatening to take him for observation away from me for 24 hours if I didn't let them."
      },
      {
        "id": "nh9m23l",
        "score": 28,
        "body": "This is totally valid. I had abdominal surgery at 6 weeks old, awake but paralyzed. I know others with the same story. PTSD has been our whole lives, we never had a before."
      },
      {
        "id": "nhbqs3m",
        "score": 25,
        "body": "The most disturbing thing is the people in this thread rationalising this."
      },
      {
        "id": "nha7bpu",
        "score": 24,
        "body": "I am absolutely shook. Tears streaming down my face for you and all the other precious babies who have suffered immensely. My heart is absolutely broken, I cannot believe this and yet it is true (just did some reading). Thank you for sharing your story and resources on this topic. I hope you find peace."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1m2nmgc",
    "title": "What\u2019s something your PTSD ruined for you?",
    "body": "Horror movies. Obviously PTSD ruined things that you would expect like trust, healthy relationships with people, being calm etc but something that makes me sad is I LOVED horror movies as a child, after my trauma in my teens I can\u2019t watch them anymore, the feeling of being scared and darkness triggers me into flashbacks. I miss being able to watch a horror movies and enjoy them without reliving the past.",
    "flair": "Venting",
    "score": 240,
    "comment_count": 316,
    "created_at": "2025-07-18T00:07:06+00:00",
    "top_comments": [
      {
        "id": "n3qq3ej",
        "score": 29,
        "body": "Men. Relationships with men are nearly impossible. I don\u2019t trust them, and male behaviors are frightening. \n\nI worked in 2 maximum security male prisons, and a violent marriage at the same time. A lot of the ways men posture, interact with each other, treat women, all make me feel like I\u2019m in danger."
      },
      {
        "id": "n3qzb3m",
        "score": 22,
        "body": "my memory. the worst and most visible affect my cptsd/ptsd had on me is that my long term AND short term memory are shot. i have roughly 10 clear memories from 2002-2020 and i cant remember vacations, things taught to me in school, book plots of books ive read, movies ive watched. and on top of that, my short term memory also suffered. my girlfriend will give me directions when driving and I'll forget immediately. ill talk to someone and just forget. im very insecure about my memory loss"
      },
      {
        "id": "n3qb0wo",
        "score": 15,
        "body": "[deleted]"
      },
      {
        "id": "n3qrunu",
        "score": 15,
        "body": "Going out. My body is in a constant state of stress just from going grocery shopping"
      },
      {
        "id": "n3qwrxq",
        "score": 15,
        "body": "Gotta say sex"
      },
      {
        "id": "n3tshfo",
        "score": 14,
        "body": "The idea of relationships of any kind"
      },
      {
        "id": "n3qc4d0",
        "score": 13,
        "body": "People - or at least, enjoying socialising"
      },
      {
        "id": "n3r44o7",
        "score": 13,
        "body": "Sadly, babies and children crying/playful screaming. My adorable 3 year old son is a loud talker in general but when he\u2019s really excited or having fun he does this shriek that paralyzes me to my core. I am a survivor of a hostage/sex trafficking operation that lasted months, and the screams that I heard all night and all day from other victims and captives were the most depraved, horrifying sounds I\u2019ve ever heard."
      },
      {
        "id": "n3qajmp",
        "score": 12,
        "body": "Healthy concept of motherhood"
      },
      {
        "id": "n3qen8r",
        "score": 11,
        "body": "Being able to lay down in certain positions, the ability to be alone with men and not have anxiety and horrible thoughts of \u201cpossibilities\u201d. Trusting people (especially around my children). \n\nFeeling safe in general. I simply can\u2019t relax or get too comfortable. I can\u2019t drive by the house I was attacked in. I avoid looking at any photos I took around that time because the date/month is triggering. The list goes on\u2026"
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1k0wcma",
    "title": "I said it once and I\u2019ll say it again people with PTSD should not drink alcohol.",
    "body": "Said from much experience. ",
    "flair": "Venting",
    "score": 238,
    "comment_count": 99,
    "created_at": "2025-04-16T21:43:48+00:00",
    "top_comments": [
      {
        "id": "mni0ax3",
        "score": 47,
        "body": "I feel like blanket statements are usually inaccurate."
      },
      {
        "id": "mniachi",
        "score": 39,
        "body": "People forget that alcohol is a depressant. You think you're self medicating, but you're actually self harming. I enjoy a girly cocktail or a glass of wine every now and then. I wouldn't say that people with PTSD should never drink, but I would say they should exercise extra caution. There's a huge difference between a mimosa with the girls and buying a handle from the liquor store on the regular. PTSD is difficult to manage. PTSD with alcoholism or addiction... more so."
      },
      {
        "id": "mnhgp8g",
        "score": 23,
        "body": "Pretty ok on me. Just say no to broad generalization."
      },
      {
        "id": "mnie8gb",
        "score": 20,
        "body": "Recipe for a meltdown of unknown origin (in my experience)."
      },
      {
        "id": "mnhpv1k",
        "score": 19,
        "body": "All my friends with PTSD that killed themselves were drinking at the time. Handguns were also involved. \n\nI\u2019m an alcoholic. \n\nCannabis is way better than alcohol."
      },
      {
        "id": "mnhvvfl",
        "score": 18,
        "body": "I have PTSD and drink heck my mom has CPTSD and drinks we don't have issues"
      },
      {
        "id": "mnhiunn",
        "score": 18,
        "body": "I love drinking responsibly lately lol. I actually feel it helps ground me sometimes and allows me to cry and process things <3"
      },
      {
        "id": "mnlw185",
        "score": 15,
        "body": "This sounds like a stuck point. I think it\u2019s all subjective to your person. If you have issues with alcohol then you should recognize your limits and/or not drink. PTSD or not."
      },
      {
        "id": "mnhp04f",
        "score": 15,
        "body": "I drink between 0 to 3 times a year. Others drink the amount they are ok with.\n\nSure for anyone, ptsd or not, ideal amount should be zero, but it\u2019s not necessarily that dramatic for everyone."
      },
      {
        "id": "mnmv9m4",
        "score": 14,
        "body": "I have PTSD, I drink very little but I drink, it doesn't bother me at all. It depends on the person."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1khesg5",
    "title": "PTSD is so much more real than I ever knew",
    "body": "Holy shit I've never known hell like PTSD. I've always been very supportive and understanding of mental health, but I'm realizing I never truly understood PTSD.\n\nI didn't realize that it just...takes over you. I guess I thought...I'm not sure what I thought. But I didn't imagine that I'd be in a position where I wake up, get triggered by seemingly nothing, then go cry and rock back and forth in a park for 2 hours. Again. \n\nIts like a force of pure agony hijacks my body until it spits me back out. Its like I'm not even me, I'm not in my body or mind while triggered. I'm something else. Or more accurately, something else is me for the duration. \n\nIm so sorry to all of you who are also struggling. I'm very educated and I still had not the slightest clue what PTSD truly was. Much love and coregulation to you all ",
    "flair": "Venting",
    "score": 233,
    "comment_count": 50,
    "created_at": "2025-05-08T01:56:54+00:00",
    "top_comments": [
      {
        "id": "mr6nu7m",
        "score": 19,
        "body": "I appreciate seeing others who have the empathy and understanding to feel and recognize this. I suffered secretly for a decade before I mentally collapsed from my PTSD. That said, I'm lucky, I'm finally after two years of therapy resembling a bit more of who I once was. \n\nBut then there are days where I can't even get out of bed and even a light can severely aggrevate a depression episode. \n\nThank you again"
      },
      {
        "id": "mr6osvh",
        "score": 17,
        "body": "It feels like it\u2019ll never go away but it gets easier and you start to not feel so heavy. Healing isn\u2019t linear but it always gets easier. Try to master grounding exercises in whatever way you know how. Teaching yourself peace is the thing I guess. It\u2019s like relearning how to walk. Confusing as hell too"
      },
      {
        "id": "mr7n2i0",
        "score": 16,
        "body": "It's very difficult to even accept you've got it, let alone deal. Understanding PTSD and the rewired brain is a long drawn out journey in itself. This goes for people from all walks of life and experiences. \n\nThanks for being in this space together in the struggle."
      },
      {
        "id": "mr6w5fz",
        "score": 13,
        "body": "Blessings and hugs to all my fellow survivors.\nThat's what we are, the proof is in the PTSD we suffer and yet push on. \u2764\ufe0f"
      },
      {
        "id": "mr6ippq",
        "score": 12,
        "body": "It\u2019s a very different journey. I was diagnosed in 2016. Hid it for five years out of fear and shame.\n\nAfter two years of therapy, I\u2019m making progress. It\u2019s a hard battle, but I owe it to myself and my family to keep going.\n\nOne thing I\u2019ve realized is I will never be the person I once was. But, I\u2019ve come to understand that, with therapy, I will come through this a better person.\n\nHang in there. Be gentle and kind with yourself. \u2764\ufe0f"
      },
      {
        "id": "mr8u64s",
        "score": 12,
        "body": "It takes immense courage to acknowledge and articulate such a vulnerable experience, especially when you've always been someone who offered support to others. Your honesty is a powerful reminder that understanding mental health on an intellectual level can never fully equate to the lived experience."
      },
      {
        "id": "mr8zgs1",
        "score": 12,
        "body": "Exactly this! No amount of what I thought was PTSD before was as dissociative and overtaking as what o experience since the single incident where I got shot in the head. All the doctors told me it wasn\u2019t the TBI causing most of my symptoms, rather PTSD. I didn\u2019t believe them till I spent some time in psychiatric care and got on antidepressants and anti-anxiety meds."
      },
      {
        "id": "mr6eznw",
        "score": 11,
        "body": "This was kind of validating to read. Sometimes I forget others don\u2019t really get it until they\u2019ve lived it, even if they\u2019re educated on it, and it\u2019s really sad because it does make you feel more alone. I\u2019m really sorry for whatever happened that caused you to develop it, and I hope you find your way on your healing journey soon. There is definitely joy and bright spots even in the healing process. It\u2019s been over said at this point but remember \u201chealing is not linear\u201d and a bad day doesn\u2019t mean you have derailed any progress you made."
      },
      {
        "id": "mrat9hx",
        "score": 11,
        "body": "We were at an airport and I got separated from my wife at customs right when a panic attack started. I didn't know what to do, so I went to my gate. There was another layer of security before the gate and when security pulled me aside, I was shaking and sweating, I just curled up in a ball in the corner. \n\nEventually the medic8ne kicked in, but that was 30 to 45 minutes of sheer terror while looking very suspicious at a checkpoint"
      },
      {
        "id": "mrb7ukx",
        "score": 10,
        "body": "I feel the same. I was already bipolar and mania RUINED My life several times, but i sure thought everything was fine while I was busy being out of control. \n\nNOW - I get triggered by people being disrespectful and REACT. And, the beautiful thing about being bipolar is then they decide im crazy... and the rumors have gotten out of control."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1m92dmv",
    "title": "my suicide plan saved my life",
    "body": "I planned everything, I packed up all my stuff, wrote all my notes, had all the equipment I needed. I was so ready to end my life that day. 3 days have passed now, I'm still alive and breathing, and it was exactly the plan that was supposed to kill me that ended up saving my life.\n\nI've had suicidal thoughts for a very long time. I managed them well, but recently things have pushed me over the edge. I won't get into detail about that part, things were just not good at home, and it was effecting my life outside of home. The plan was fully in motion now. I was passing through my days knowing I'm going to die. Part of my plan was to fuck up my life as much as I can before I go. I had been sober for a long time but I'd started drinking again. \n\nI made three attempts. The first two times I failed, but I was determined to try again. On the day I tried again, I knew I wouldn't fail. I bought some alcohol and got quite drunk. I had my equipment in a gym bag beside me and I was just walking around with it for the whole day. I wanted to have some fun before I died, so I had called some escorts, and I asked them if they're available. 2 ladies. It was all part of the plan. \n\nI gave them a lot of money but it didn\u2019t matter to me, money has no value when you're dead, right? My gym bag was in the same room, just beside the bed, they asked what's inside, I just said my gym clothes. The problem was, I was so far gone, emotionally and physically, that I couldn't even get hard. I had 2 beautiful, naked women in front of me and I felt absolutely nothing. I had a massive breakdown in front of them. I was ready to leave at that time but they stopped me, and they talked to me. I put my clothes back on, we ordered some wine, and we sat there all night just talking. I dumped everything on them and they listened, I showed them all my hobbies and the things I've created, I told them about the lives I've changed through my work. Lives that I have saved. \n\nThey actually showed me... love? Or some kind of love that I haven't known. They showed me how much I actually matter. It was the place I least expected to feel something like that. They didn't even watch the time or anything, they let me stay as long as I needed, and I'd gone way over the time limit that I paid for. I apologised, but they gave me their personal phone numbers and we've texted eachother.\n\nBefore I left, I told them they just saved my life, and that I won't be ending my life tonight. We hugged, and then I left. Still had my equipment with me, and now I'm even more drunk, but I reached out for help this time. I called an ambulance. I was sat there around midnight on the street all alone with just my suicide equipment beside me. They took a long time to come, I had started to think they weren't coming and had another massive breakdown. But they came, and they took me to the hospital. \n\nI don\u2019t think that money went to waste, I think I used that money to buy myself some more time. I'm getting help now, and I'm grateful to still be here.\n\nThank you for reading if you made it this far.",
    "flair": "CW: suicide",
    "score": 229,
    "comment_count": 30,
    "created_at": "2025-07-25T15:34:53+00:00",
    "top_comments": [
      {
        "id": "n58ho40",
        "score": 17,
        "body": "I guess the phrase that angels or whatever come in strange and unusual forms/ways is true. always the most unexpected thing to prevent it. mine rn is my cat because no one will care for him the way I do"
      },
      {
        "id": "n542ire",
        "score": 16,
        "body": "Sometimes humanity shows up where we least expect it. Good luck out there and don\u2019t forget those lives you haven\u2019t saved yet."
      },
      {
        "id": "n560g62",
        "score": 14,
        "body": "You are a very brave person and I'm so glad you're still here and you posted this. \n\nThis is not something I ever talk about but it might help someone if I post. \n\nI went through a profound spiritual experience in 2018. Among other things, it opened me up to information I'd never had before. \n\nA couple years afterwards, I was going through some stuff and suddenly realized I had actual past life memories so strong and clear I could validate the data. I discovered who I was in my most recent past life. I had committed suicide at the age of 19.\n\nI came back as who I am now, with all of my present problems plus all of her past problems. My life has been very, very, very difficult and quite unpleasant. \n\nOnce I found this out, I began working through both sets of issues. My advice to anyone is, don't do it. Things will be twice as hard when you come back. \n\nSending you love and hugs, friend. You are very brave and very strong. I'm glad you're still here."
      },
      {
        "id": "n5azuwi",
        "score": 13,
        "body": "SWers are therapist."
      },
      {
        "id": "n57jri0",
        "score": 12,
        "body": "I am so grateful they took the time to listen to you and that you felt love. So grateful you are here. Sending you lots of love."
      },
      {
        "id": "n557rzi",
        "score": 10,
        "body": "So glad you\u2019re still here. And that you opened up and human kindness saved you."
      },
      {
        "id": "n57o3u3",
        "score": 9,
        "body": "Glad you changed your mind because somewhere you matter to someone rather it be those ladies or a parent or child , sibling or cousin you matter and that would leave someone devastated forever from your choice . Your  story touched me my niece lost 3 of her children to suicide and she will never be the same  so I\u2019m thankful you got help . Help to help you through that rough time in your life ."
      },
      {
        "id": "n56o7ed",
        "score": 9,
        "body": "Glad you're still here. I wish you a long life filled with happiness."
      },
      {
        "id": "n57g1z7",
        "score": 9,
        "body": "Glad you're here"
      },
      {
        "id": "n5zmg62",
        "score": 8,
        "body": "Man this was the most moving post I have read since joining Reddit around 2017. \n\nAs someone who struggles with PTSD to another, you give me hope. Thank you for sharing this!"
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1pohz14",
    "title": "Anyone else feel like their PTSD didn\u2019t start until after everything was over?",
    "body": "I used to think PTSD was about what happened\u00a0*during*\u00a0the crisis.\n\nBut for me, the symptoms didn\u2019t really show up until months later \u2014 when the danger was gone, the adrenaline wore off, and everyone else expected life to go back to normal.\n\nThat part confused me the most. I kept thinking:  \n*Why now? Why can\u2019t I just move on like everyone else seems to have?*\n\nI\u2019m starting to realize that delayed reactions don\u2019t mean we\u2019re weak or broken \u2014 they mean our nervous systems finally ran out of ways to hold everything together.\n\nIf this resonates, you\u2019re not alone. I\u2019m still figuring it out too.",
    "flair": "Support",
    "score": 204,
    "comment_count": 86,
    "created_at": "2025-12-17T00:07:33+00:00",
    "top_comments": [
      {
        "id": "nugpgxz",
        "score": 25,
        "body": "PTSD doesn't happen during trauma but POST trauma, so after. During trauma you have a traumatic reaction that can later on lead to PTSD."
      },
      {
        "id": "nufdw22",
        "score": 17,
        "body": "Ma\u2019am or sir, that\u2019s what ptsd is; after it\u2019s over. \n\nPOST traumatic stress disorder.\n\nWhat happened during the crisis was your nervous system activating your fight or flight responses. \n\nDelayed reactions are normal. \n\nI hope I didn\u2019t sound sarcastic bc that wasn\u2019t my intention!"
      },
      {
        "id": "nufekia",
        "score": 17,
        "body": "I mean it literally has to be months later for PTSD to be considered at all. If not, it is considered an \u201cacute\u201d stress reaction."
      },
      {
        "id": "nugfs3f",
        "score": 15,
        "body": "My PTSD showed up 20 years after the trauma. It can hit anytime."
      },
      {
        "id": "nuibghc",
        "score": 14,
        "body": "Post tsd\u00a0"
      },
      {
        "id": "nufkj9s",
        "score": 11,
        "body": "What you\u2019re saying is exactly what our bodies do.\n\nThe events that gave me PTSD, were also wrapped up in 2yrs of proceedings. \nWhile I was going thru everything I was so strong and fought so hard everyday, even on little sleep.\n\nBut!!! All hell hit when things were quiet. \nTaking a simple shower was a panic attack, a car near my home\u2026\u2026panic\n\nI\u2019m getting better and growing and feeling stronger but, I\u2019m not sure it will ever really be gone"
      },
      {
        "id": "nuge8ld",
        "score": 11,
        "body": "Yes. Depending on how you\u2019re able to process the events can lead to different outcomes entirely. If a person doesn\u2019t remember their trauma, they can go decades without symptoms that are severe. Most don\u2019t remember until their psyche tells them it\u2019s safe to remember and process. It can be difficult, it can be traumatic sometimes. It all depends on how you choose to approach it. Therapy is difficult, I won\u2019t tell you it\u2019s easy and you will feel better after five sessions. You\u2019ll probably feel worse or less likely to want to explore your memory. But nothing worthwhile ever comes easy, for those that need answers or want understanding of themselves on a deeper level."
      },
      {
        "id": "nugcsli",
        "score": 10,
        "body": "I'm that person too. \nI held life together for many years and then suddenly just kinda slowly fell apart. One too many traumas piled up, one too many responsibilities. \nNow I've got a laundry list of diagnoses and a lot of medications. I'm still going in life, limping along."
      },
      {
        "id": "nugwb5x",
        "score": 10,
        "body": "Yeah. This is how I experienced it.\n\nIt all suddenly hit me. \n\nGranted I was also involved in a cover up (my incident was covered up) and was bullied relentlessly. So it never really ended for me."
      },
      {
        "id": "nughbaz",
        "score": 9,
        "body": "I blocked most my horrific childhood, I always thought it was weird I couldn\u2019t remember growing up like other people, had traumatic birth of twins and almost died, abused by a nurse while my appendix burst and it wasn\u2019t until last year when I had a Takotsubo cardiomyopathy in the emergency room while being abused again by a nurse that I finally broke. It\u2019s been a year now since I\u2019ve finally gotten help. I repressed everything, my nervous system broke down and I stopped eating because I couldn\u2019t even swallow. Yep, your nervous system can only handle so much. I\u2019m thankful for my husband, he really made me get through it by finding help. I put everyone else first, my focus was always on my children and husband. Nobody knew my struggle, because I just kept going even though I was drowning.\n\nWhen my best friend told me most people never have so much trauma and I was the strongest person she\u2019d ever known, I realized it\u2019s not weak to tell your truth."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1qzjnt1",
    "title": "This Epstein crap is so triggering",
    "body": "(TW: CSA, grooming) I am trying not to be triggered by it, but it is everywhere. I feel like every time I get to a point where it's not triggering, something else is said that ends up being triggering. Maybe if I wasn't trying to process this trauma, it would be different.\n\nWhen I was groomed, they all called me \"jailbait\" and it's already hard enough to accept it was their way of ignoring that I was \\*a child.\\* I've already had issues coming to terms with the fact that I was groomed and now there are pedophiles everywhere, running free because they have power. \n\nAm I alone in this? Maybe it wouldn't bother me so much, but I have chronic sexual trauma, so it's hard for it not to. This rant stemmed from seeing a post that said \"there's no such thing as an underage woman, that is a child\" and it's triggering me because \\*I\\* was a fucking child. How are people just letting this injustice happen? Where is the accountability? ",
    "flair": "Venting",
    "score": 196,
    "comment_count": 80,
    "created_at": "2026-02-08T20:21:20+00:00",
    "top_comments": [
      {
        "id": "o4d0x6g",
        "score": 17,
        "body": "No, youre definitely not alone. I've been spiraling for the last week or so after being triggered by an image that came across my feed and it was downhill from there. I feel absolutely insane because it just feels I'm the only one who actually cares. Like, why does no one else seem to want to scream and cry and break everything in sight? Why does no one else want to set the whole world on fire?! Where is the rage???"
      },
      {
        "id": "o4bbchf",
        "score": 15,
        "body": "It's impacting me in a very bad way as well."
      },
      {
        "id": "o4dieb9",
        "score": 14,
        "body": "Same. The worst part about this for me are the jokes/memes. I hate the normalization of rape jokes, it\u2019s so fucking disgusting."
      },
      {
        "id": "o4b9tho",
        "score": 12,
        "body": "Absolutely not alone. I'm in a trauma support group, and we talked about this last week."
      },
      {
        "id": "o4bdb8o",
        "score": 12,
        "body": "I feel this too. It sucks to have your experience be a source of social commentary but at the same time it feels like nobody cares about justice."
      },
      {
        "id": "o4buyg6",
        "score": 11,
        "body": "There have been a lot of posts like this in r/CPTSD and r/Eptsein and no, you are not alone! We are struggling a lot with this.\n\nI was groomed and raped as a teen too. This has all been extremely triggering. I have tried to adjust my algorithm as best I can to not have it pop up constantly on my feed. But I\u2019m still seeing it, and I\u2019m so fucking mad. The rage I have at the lack of public reaction\u2026. I have been so depressed and angry watching all of this unfold and most people just don\u2019t care or believe the victims."
      },
      {
        "id": "o4bzvkd",
        "score": 11,
        "body": "I think for me it feels like a win that it's out. I never got justice for what I had to endure, my abusers walk free bc I was too traumatized to take them down. I'm cheering for the public outcry. I am part of the public outcry. We all want justice. Rich and powerful or not .. THEY should be scared."
      },
      {
        "id": "o4co3ux",
        "score": 10,
        "body": "Very much so.   Them exposing all this isn't actually accomplishing anything.  These people have all gotten away with it ,and continue to. He's the only one who paid it seems. Everyone will just defend the ones they like,or just make up some dumb excuse. So I decided I'm not paying any attention to any of it. It's beyond frustrating . It honestly makes me feel like giving up. I wont, but it's gross and disgusting. The people who abused me as a child all got away with it. I've seen several people in my adult life get away with it, as well. I'm so sorry you have to go through this.You aren't alone in this.  Sending love."
      },
      {
        "id": "o4bmrgi",
        "score": 9,
        "body": "I honestly thought I\u2019ve been going crazy. Since this administration took over, I feel like I have no sex drive whatsoever. And while my sex drive has never been \u201cnormal,\u201d I\u2019m angry often and at every little thing and try not to think about sex. It goes without saying that I cannot look at the files. I HATE the victim blaming that people have rationalized. I just can\u2019t fucking take it."
      },
      {
        "id": "o4ciix2",
        "score": 9,
        "body": "You aren\u2019t alone, the Epstein Files is triggering for a lot of people, myself included. Ever since this new data set has been out, I\u2019ve had increased anxiety and I feel sick to my stomach since the files are all over my Reddit and Instagram"
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1q6a9za",
    "title": "Three years ago I hit rock bottom - today my therapist said I \"no longer meet the criteria for a PTSD diagnosis\"",
    "body": "Three years ago, I made my first of two suicide attempts. Along with my untreated Bipolar Disorder, my PTSD was overwhelming. I couldn't sleep, I couldn't leave my house, any sudden touch or loud sound could trigger a flashback or panic attack and I didn't want to endure another 30 years of suffering.\n\nAfter spending time in treatment, an incredible amount of difficult work, my wonderful therapist, some effective medication, and a support network of people that I couldn't have made it without, I was told today by my care team that I don't have enough symptoms anymore to be diagnosed with PTSD. I just needed to share this. I'm really proud of myself.\n\n\n\n",
    "flair": "Success!",
    "score": 192,
    "comment_count": 31,
    "created_at": "2026-01-07T08:45:37+00:00",
    "top_comments": [
      {
        "id": "ny62paw",
        "score": 7,
        "body": "Wish I could upvote this more than once but I can't."
      },
      {
        "id": "ny7r19h",
        "score": 5,
        "body": "This is amazing, and I'm taking it as a sign. I came to this subreddit to ask if it ever gets better. I recently started EMDR after being in therapy for almost two years, and I've tried a few medications but nothing is working so far (although EMDR is very, very fresh). Can I ask which medications you found the most helpful? And, if you spent time in a hospitalization program (PHP, IOP, or inpatient), did you find that it was beneficial?"
      },
      {
        "id": "nyazrxu",
        "score": 5,
        "body": "Im just a stranger on the internet, but I am so proud of you. I've recently started doing EMDR for my PTSD and the work is no joke. It's hard to push through all this. Be so proud of yourself"
      },
      {
        "id": "nycj65l",
        "score": 4,
        "body": "Hell yeah! This gives me hope"
      },
      {
        "id": "ny7vrc6",
        "score": 4,
        "body": "   Same. I was starting to think because my SA was violent (though all SA is violence period) I couldn\u2019t get better. I get in severe physical pain and some of my flashbacks are actually terrifying. This brings me hope that it\u2019s possible to heal."
      },
      {
        "id": "ny63j8e",
        "score": 3,
        "body": "Proud of you!!!!! \u2764\ufe0f\u2764\ufe0f"
      },
      {
        "id": "ny6sjaz",
        "score": 3,
        "body": "That's amazing, so happy for you!"
      },
      {
        "id": "ny7lq3t",
        "score": 3,
        "body": "Massive congratulations, that's a huge accomplishment!!\u00a0"
      },
      {
        "id": "ny9dfeh",
        "score": 3,
        "body": "That's an incredible achievement, really proud of you for facing this head-on. How do you feel about this positive change in your diagnosis?"
      },
      {
        "id": "nyd6qbm",
        "score": 3,
        "body": "This is awesome"
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1klcvx8",
    "title": "PTSD brain be like here, forget important thing that you need to do and instead remember awful thing from years ago. Good luck!",
    "body": "Seriously?! What's up with that! Gee thanks \ud83e\udee0",
    "flair": "Meta",
    "score": 182,
    "comment_count": 16,
    "created_at": "2025-05-13T04:11:56+00:00",
    "top_comments": [
      {
        "id": "ms1n3oi",
        "score": 15,
        "body": "I read about a study done a couple years ago about traumatic memories.   Brains have three types of memory, long, short and that real short dream memory.\n\nNormally memories in short term get moved to long term and then those memories start to feel distant to us.\n\nThe study found out these traumatic memories get glitched.   They show up in the brain as short term memories even though they are stored as long term.\n\nSo when one of us with PTSD says it always feels like it just happened it really does."
      },
      {
        "id": "ms5bvrr",
        "score": 9,
        "body": "\u201cYou need to go to work today? Hell no bozo let\u2019s have a 30 minute panic attack instead to start the day - yeehaw!\u201d"
      },
      {
        "id": "ms5yebq",
        "score": 6,
        "body": "I can\u2019t remember anything other than terrible things \ud83d\ude2d whyyyyyy?!"
      },
      {
        "id": "ms3i5jt",
        "score": 4,
        "body": "I definitely get this feeling as well. It\u2019s like why would I need to remember a list of things to do at work when I could remember specific smells from the past. That is super adaptive and helpful. I definitely didn\u2019t need to know that work stuff anyway. /s"
      },
      {
        "id": "ms67ijc",
        "score": 4,
        "body": "EXACTLY!\nI hate it (for all of us).\nWhy hang out with friends when you can flashback movie night instead?"
      },
      {
        "id": "ms7s2z2",
        "score": 2,
        "body": "ONG. Forgot what you said 4 seconds ago, but memories of torture? I gochyu"
      },
      {
        "id": "mt1fe8u",
        "score": 2,
        "body": "\u00a0 Exactly. It\u2019s driving me absolutely nuts and it\u2019s so frustrating because isn\u2019t PTSD affecting my life negatively enough ? And then when people don\u2019t understand and think you just don\u2019t care. \ud83d\ude43"
      },
      {
        "id": "mse4co4",
        "score": 2,
        "body": "My shrink told me while I was in treatment that your brain acts like the trauma is happening to you now but the goal is to make it into a memory. Made some progress but past week has been shit :("
      },
      {
        "id": "ms1c0dh",
        "score": 1,
        "body": "*r/ptsd has generated this automated response that is appended to every post*\n\nWelcome to r/ptsd! We are a supportive & respectful community. If you realise that your post is in conflict with our rules (and is in risk of being removed), you are welcome to edit your post.  You do not have to delete it.\n\nAs a reminder: never post or share personal contact information. Traumatized people are often distracted, desperate for a personal connection, so may be more vulnerable to lurking or past abusers, trolls, phishing, or other scams. *Your safety always comes first!*  If you are offering help, you may also end up doing more damage by offering to support somebody privately. Reddit explains why: [Do NOT exchange DMs or personal info with anyone you don't know!](https://www.reddit.com/r/SWResources/comments/dmu24/why_shouldnt_i_share_my_contact_information/)\n\nIf you or someone you know is in immediate danger, please contact your GP/doctor, go to A&E/hospital, or call your emergency services number.  Reddit list: [US and global, multilingual suicide and support hotlines](https://www.reddit.com/r/SuicideWatch/wiki/hotlines).  Suicide is not a forbidden word, but please do not include depictions or methods of suicide in your post. \n\nAnd as a friendly reminder, PTSD is an equal opportunity disorder. PTSD does not discriminate. And neither do we. Gatekeeping is not allowed here.\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/ptsd) if you have any questions or concerns.*"
      },
      {
        "id": "msdeszd",
        "score": 1,
        "body": "Yeah, it\u2019s the worst!"
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1ox7ty4",
    "title": "My girlfriend is so traumatized she cant function",
    "body": "My girlfriend is in the hospital for the fourth time this year. She struggles with CPTSD, Bipolar, general anxiety and autism. She has more trauma than anyone I\u2019ve ever met, yet she is the kindest person I know and tries so hard. She is constantly overwhelmed with flashbacks of all her trauma and there's nothing I can do but restrain her when she breaksdown.\n\nRecently she had an interaction on Reddit with someone who tried to \u201cteach her a lesson\u201d by telling her the world is cruel and she needed to toughen up. They mocked her and said awful things. She already knows how cruel the world is... she didn\u2019t need it thrown in her face. Social media is usually a coping mechanism for her, but this pushed her over the edge.\n\nShe\u2019s an adult and I can\u2019t just tell her not to use Reddit, even when people like this hurt her mental health. She was manic that day and did say things she shouldn\u2019t have, which isn\u2019t okay, but it\u2019s also not anyone\u2019s job to \u201cteach lessons\u201d to strangers. All this person did was push someone already extremely mentally ill back into inpatient care.\n\nShe is constantly on the brink of suicide. She\u2019s been in therapy for years and is still trying to regulate her medications. She genuinely believes she\u2019s weak and a monster. She feels everything intensely and replays hurtful interactions for days. I\u2019m trying my best, but I\u2019m at my wits\u2019 end. She\u2019ll do okay for weeks or months, then one bad moment sends her straight back to inpatient.\n\nReddit had been a positive space for her for three years... she met good people and loved the communities. But the recent harassment made her delete her account, which was a huge deal for her. I\u2019m upset that something that once helped her so much has become a source of pain.\n\nI want to help her, but she\u2019s so traumatized and unstable that one cruel comment can send her running into traffic. She constantly feels like the world is against people who can\u2019t function \u201cnormally,\u201d and the voice in her head is constantly telling her she should die. Please, do you have any suggestions? I don\u2019t know what to do to help her anymore. ",
    "flair": "Advice",
    "score": 179,
    "comment_count": 159,
    "created_at": "2025-11-14T20:37:23+00:00",
    "top_comments": [
      {
        "id": "nowzpiq",
        "score": 28,
        "body": "I am not a doctor. I am a person with C-PTSD from many traumatic events in the \"severe\" category with very little reprieve between them over the course of my life.  \n  \nShe needs appropriate psychiatric and psychological intervention if posts on reddit are tipping her over the edge. This is not a comment meant to imply weakness, but if you hit something with an object that is large and heavy enough times then eventually it can crumble with a gentle tap. No amount of you that you pour into her is going to improve this. \n\nSingular short stays in the MH unit are not sufficient for PTSD - most likely with prolonged exposure to trauma over a significant part of her life means she has C-PTSD. She needs an intensive treatment plan with a licensed practitioner (or two) and needs to be participating in it for months, possibly years.   \n  \nIt's curable, but it doesn't get cured on its own. You are good to want to support her, but you can't fix this."
      },
      {
        "id": "nox7gvg",
        "score": 25,
        "body": "I am glad that works for you but I have seen her off her meds and she's even worse. She truly does have bipolar, her experiences are very real. Nature and a journal isn't all she needs and the health care system has helped her so much regarding her therapist. The one person who had her back for 10 years and fought for her was her therapist. Trust me I wish it was this easy but this reads like r/thanksimcured"
      },
      {
        "id": "np064y4",
        "score": 24,
        "body": "I concur EMDR , and look for a peer specialist or peer advocate.  They help along side therapist as some ne who can identify with her as they have been through it as well."
      },
      {
        "id": "nowd2bo",
        "score": 22,
        "body": "You are a very compassionate person and this post shows how much you\u2019re trying to alleviate your gfs agony. The hard truth is that, you can\u2019t make this go away, therapy can help but the trauma will always reside within her, unfortunately. I have CPTSD and borderline traits. I\u2019ve never been this severe but I have been in therapy for a long time and what I\u2019ve learned is that it\u2019s a lifetime journey of managing life after trauma. \n\nMy point is that, you can either accept your girlfriend as she is and accept that she will likely always be in and out of inpatient or chronically struggling with suicidal ideation, set your boundaries to keep you safe during these moments, and live life with her on this journey, not ever expecting her to be \u201cnormal\u201d or \u201chealed\u201d. Sounds like she is trying her best and that\u2019s all that she can do. The constant emptiness and despair are just something she, and anyone close with her will have to live with. You will become burnt out as it already seems like you are. You need to take care of yourself and protect your own emotional well being while caring for her as well. And accept that this is a chronic life long journey for her."
      },
      {
        "id": "noy2sgq",
        "score": 22,
        "body": "I\u2019m really glad you\u2019re there for your girlfriend, OP. I hope she can get to a more peaceful place soon. My husband\u2019s steady kindness and love have healed me in ways I never expected, so I know how much a supportive partner can matter.\n\nI\u2019ve been dealing with CPTSD for more than 25 years, and here\u2019s what has actually helped. Gentle nudges are good, but they have to be driven by her. As you\u2019ve observed, people with trauma are usually very sensitive to shame, so the difference between an invitation and a directive is huge. For example, invite her on a walk, don\u2019t tell her to go walk.\n\nMundane, gentle physical activity can shift things when you\u2019re triggered or shut down. Walking, small chores, simple movement. I\u2019ve learned that when I least want to walk is usually when I need it most. My therapist told me that rumination literally creates more waste products in the brain, and physical activity helps clear them.\n\nI use an app called Finch to keep my small tasks, coping tools, and self-care reminders in one place. The little bird keeps me motivated, and it has grounding and breathing exercises that help when I\u2019m overwhelmed.\n\nL-theanine, an amino acid found in green tea, has been great for calming anxiety.\n\nOther things that help: comforting scents, firm pressure hugs, moist heat. Hot yoga has been huge for me. Basically anything that invites calm while still encouraging a bit of movement or creativity helps pull the brain out of survival mode.\n\nAnd when she\u2019s ready for it, EMDR has been life changing for me. It\u2019s intense, and it took time to stabilize enough to tolerate it, but the long-term impact has been worth it.\n\nWishing both of you the best. And make sure you\u2019re caring for yourself too.\n\nP.s. I just block DMs, it\u2019s almost never worth the trouble"
      },
      {
        "id": "noxxj7z",
        "score": 17,
        "body": "Social media is poison for our mental health. You need to talk with her about her consumption of social media content. I am for real."
      },
      {
        "id": "np060t8",
        "score": 17,
        "body": "I would enjoy to move to a complete remote place, near a lake or a river, just watching the sun transition from sunrise to sunset, accompanied by the weekly drives to a supermarket to later on get back into solitude and enjoy serenity, without the modern day devices, maybe a super old handy for emergency calls.\n\nAll encompassed by some kind of farmwork, but without livestock."
      },
      {
        "id": "nozgz91",
        "score": 15,
        "body": "I don\u2019t have the bandwidth to write a full response, but echo my what others have said here. EMDR changed my life. I was crippled by my cPTSD. Couldn\u2019t leave the house. Function. EMDR makes things worse before it makes things better but I think I can now say after two years I no longer meet the diagnostic criteria for PTSD. \n\nYou sound like a wonderful partner. Take care of yourself too"
      },
      {
        "id": "nowp89p",
        "score": 15,
        "body": "There's only so much you can do, and that's reasonable to do.\u00a0 You need to look after yourself, get into therapy if you aren't already.\u00a0 YOU need support.\u00a0 The load you are carrying is not sustainable without help and tools.\u00a0 Good luck"
      },
      {
        "id": "noxjn8a",
        "score": 15,
        "body": "Thank you for being with her. I wouldn\u2019t made it if it wasn\u2019t for my boyfriend/husband today. \nPlease reach out to me, I have a few ideas that might shed some light on."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1n37muk",
    "title": "Update on employee written up for intentionally repeatedly jump-scaring me",
    "body": "A quick update for anyone who read my first post and was interested. The guy that got written up for intentionally scaring me repeatedly is currently suspended. He is under investigation for something, but I don't know what. He actually texted me or I wouldn't have had any clue.(Another coworker gave him my number. I had a very serious conversation with her about how that was unacceptable and potentionally very dangerous. I told her that she may NEVER give out any of my personal information again without my express permission. She realized how wrong it was once I explained and was extremely apologetic. She is very young, niave, and inexperienced and had honestly never considered that any harm could come from it.)\n \nAnyway, he texted me saying that he was suspended and under investigation for something, but said he didn't know what. He  demanded to know if I'd made another complaint against him. I told him I hadn't and had no idea what was happening. I told him not to contact me again and blocked his number. \n\nI'm very confused. I thought if you were under investigation for something that your employer had to tell you what that something is? However, I've never been in that situation, so maybe I'm wrong? Does anyone know?\n\n All I know is that the company had all the locks in the building changed and he hasn't been back. I haven't heard anything since. I'll let you all know if I hear anything else. It's a weird situation.  \ud83e\udd37\u200d\u2640\ufe0f\n\nEdit: OK, I stopped by HR on lunchbreak and explained about the text. They asked if he's tried to contact me any other way. I said no. They said thank you for telling them and please tell them if I have any further contact from him. \n\nThank you all for your advice and support!",
    "flair": "Venting",
    "score": 176,
    "comment_count": 34,
    "created_at": "2025-08-29T13:35:47+00:00",
    "top_comments": [
      {
        "id": "nbee2qz",
        "score": 52,
        "body": "HR here (with PTSD). \n\nHim contacting you and specifically asking you directly if you made the complaint is a huge no no. I had a similar instance in my career and terminated for it. \n\nHR is not obligated to explain why someone is out of work pending an investigation. Typically, if the complaint is unfounded the person is compensated for any lost wages. \n\nYour feelings are valid and you\u2019re doing the right thing. Also kudos for explaining to your colleague why giving out your personal cell phone number without consent is important. \n\nDo not block him, but also do not respond to him. This will allow you to collect more \u201cevidence\u201d. If it gives you some peace of mind to block him, then do so."
      },
      {
        "id": "nbefm3h",
        "score": 48,
        "body": "With my situation if someone jump scares me there is a really good chance I\u2019m going to punch them so hard I\u2019ll be arrested.  \nMy coworkers know I have PTSD but don\u2019t know my triggers.  A couple of the younger one thought they would try to find them out but my supervisor told them if they tried anything they would be severely punished.  That put a stop to that. My company is a stickler for the ADA and has been sued too many times to let people willingly violate it."
      },
      {
        "id": "nbbe4zl",
        "score": 37,
        "body": "the locks were changed? jesus, he really did something lol\n\nand yeah, when I whistle-blew on my manager about manager abuse and breaking rules they suspended her without telling her. She'd been there for 5-10 yrs or something. When they finished they straight up fired her, so she was making more mistakes then even I thought"
      },
      {
        "id": "nbc30ln",
        "score": 28,
        "body": "If you filed a complaint about him previously, him contacting you is harrassment. Report it.\n\nI totally get the jumpscare issue. I was terminated from a job in my early 20's because I knocked the guy the fuck out."
      },
      {
        "id": "nbbco13",
        "score": 27,
        "body": "Wow, I'm glad he's no longer at your workplace. Should you alert HR that he has gotten your number (without your permission) and contacted you during his suspension? Not to get him in further trouble, but to make sure there is a paper trail for his behaviour post suspension. Good luck!"
      },
      {
        "id": "nbi0cii",
        "score": 23,
        "body": "As they changed all the locks, he probably made threats after being confronted."
      },
      {
        "id": "nbbds8e",
        "score": 22,
        "body": "That's a really good thought! I'll stop by and mention to HR that, hey, I got this text. Just FYI. Thank you for the good advice!"
      },
      {
        "id": "nbhbo9j",
        "score": 21,
        "body": "I'm glad you blocked him. OP, please be careful. I don't like how this guy is seemingly obsessing over you :("
      },
      {
        "id": "nbdcr9j",
        "score": 19,
        "body": "im intrigued to see if he gets let go i feel like logically  this is the next step because he was  again unprofessional  by contact you about his suspension.   from an general manager perspective i have suspended and then terminated someone for this behavior... and i didnt have to give reason...  they were talked to about bullying,   there was then hostility  towards the person who reported  causing me to further investigate their behavior and ultimately i decided  it was a zero tolerance policy for bullying and harassment  and  they didnt get it the first time so    i didnt need another reason to fire them.\n\nOn a side note i have also had to call a staff meeting with 25 people and explain the importance of not giving out private numbers  or information that would be considered sensitive  and never giving anyone  other staff memebers phone numbers or shedule information ie: if someone calls  to ask when so and so works again you do not tell them their schedule... you have no idea that person is not a stalker.   this came after my assistant manager   gave a random person my contact info instead of the companies  alone with my full name my schedule,   my lunch break times, and some very concerning questions about when i was not supervising the store  or when  our bank drops were   if they were supervised,  if our cameras at cash desk worked, and a lot more.  i ended up coming into work she told me about it and that she gave them all the answers and had no idea who it was they didnt identify themselves.... i was like k so you gave my whereabouts  at all times, as well as the cash  our bank deposit info, and didnt see a problem with that?  i tried to then get the company to hire security for my girls that had to do bank drops every night off property and they werent willing so i  asked the  mall sucurity to escort my employees  after work to the edge of the property and watch them  to make sure they get to the bank ok and my employees had to use a buddy system for a month because i wouldnt let any of them walk to the bank or to their cars or bus stops alone.   the assistant manager got fired  after one more security risk of failing to lock the door a week later anyone could have gotten thousands of dollars just walking by.  i felt bad firing her cause she was also being evicted and her husband just lost his job but  i wasnt willing to trust her and she was a manager!\n\nthe staff also had the option to not do the deposit drop and leave it in store for me to do when i get in but  that was against  H.O policy and they  got made at me for deposits not being every night( i didnt care  its  reasonable to me to not risk my employees lives  at night time off the clock  when i can do it during the day and assume  the risk myself."
      },
      {
        "id": "nbdbsd1",
        "score": 14,
        "body": "If you continue to have contact with this person, and it becomes a problem, don\u2019t be afraid to reach out to the police about harassment. I did that with somebody and it really changed things for me for the better."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1mad4m3",
    "title": "PTSD is such a lonely experience",
    "body": "I feel so separated from others who haven't experienced what I experienced. They don't know the intricate details of what it's like to experience SA, how it destroys your sense of trust, how your connection to your body gets severed, how you move through the world scanning for threats, what it feels like to relive the trauma in your mind and in your body over and over again in response to innocuous triggers. They don't know what it's like to fear sleep, or the dark, or the very space where you're supposed to feel safe. They don't know what it's like to have to check each movie before you watch it for triggers, or how strongly you have to manage your emotions when triggered in public, or what it's like to fear intimacy. They just don't know, and I'm envious of them. It's such a lonely experience.",
    "flair": "CW: SA",
    "score": 178,
    "comment_count": 30,
    "created_at": "2025-07-27T04:19:03+00:00",
    "top_comments": [
      {
        "id": "n5go4qr",
        "score": 9,
        "body": "It's true, people don't know the level of suffering.  They just see the surface.  They don't know the nightmares, flashbacks, PTSD is something from a movie to them.  That's why it's very wrong to re-define PTSD as a catch-all and validation for any mental disturbance.  But that's whats happened in much of the US with the \"trauma awareness\" movement.  It actually means awareness of common disturbances, and continued stigma of less common ones."
      },
      {
        "id": "n5ds3m8",
        "score": 7,
        "body": "you explained this beautifully (although i know it\u2019s not a beautiful experience). it\u2019s a very tough and lonely feeling trying to navigate any type of relationships after having gone through something so traumatic. you are not alone in these feelings, if it makes you feel any type of better, this post has made me feel less alone in my experiences bc i resonate so deeply. thank you for sharing and best wishes \ud83e\ude77"
      },
      {
        "id": "n5hv5dl",
        "score": 7,
        "body": "I am absolutely convinced that one reason movies do not depict PTSD well is that an accurate depiction would be deeply disturbing to watch\u2014and at times, boring or impossible to understand for the uninitiated."
      },
      {
        "id": "n5ds1bq",
        "score": 6,
        "body": "You may feel lonely right now, but you are far from alone. Lots of us SA survivors out there and out here for each other. Take each day, one at a time. You are getting through today and every day before this one - go girl! Work on yourself in therapy, get some tools for your toolbox and know that this isn\u2019t the end. Things get better. (And sometimes they get worse again! \ud83d\ude33). But you got this and if you need someone to chat, hit me up! \u2764\ufe0f"
      },
      {
        "id": "n5gm2nj",
        "score": 6,
        "body": "Oddly, I find comfort in how many people can't understand my PTSD.  There's something oddly reassuring about knowing how few other people have experienced what I have. Like I took one for the team, so to speak.\n\nAt the same time, I get where you're coming from. You wish there was more of a community for people like us. And while this sub is excellent sometimes, it does lack something vital. So my best suggestion is to find a little group of your own to talk about the things other people can't understand. \n\nI know several guys who we all have PTSD from different sources. Service, incarceration, childhood abuse, etc. But we all lean on each other because we understand those fears and hesitations. We're 4 guys who understand the \"crazy\" inside each other and try to help. It does wonders for not feeling alone, frankly.\n\nSo I'd suggest finding your own group. A few people who, like you, understand the hardships you face and can talk to you on that level. Even my therapist can't fully process what it's like to live like this, so I really do believe it fulfills the community need for people like us.\n\nThank you for reaching out, and I hope you find some peace. Please let us know if we can help anymore, and I wish you the best of luck."
      },
      {
        "id": "n5dzkuh",
        "score": 5,
        "body": "I totally resonate with you and i can see that so many others around us as well. It's not easy, i get it. It takes so much time and it's lonely and frustrating. The body holds so much, it holds on to everything and no one who has not experienced abuse can ever know what it's like. \n\nBut you're not alone. We're here. You have yourself. Make your heart and your mind and your life so beautiful and filled with all kinds of experiences that even if loneliness creeps in, you can welcome it with open arms as a friend. \n\nRemember, you will always have yourself. And you are a beautiful survivor."
      },
      {
        "id": "n5f3t18",
        "score": 5,
        "body": "It takes a long time for it to get better, but it does. I remember early on after my SA that the trust I had for others was nonexistent. Going into a store to shop my hands shook uncontrollably like I had Parkinson\u2019s, every time I left my house I thought people were following me. The world was not safe, and when I was alone in my deepest darkest thoughts I wasn\u2019t safe to myself. But I went and got help, tried the medications, did the therapy, and the best thing for me, I got a service animal. I know not everyone is able to do that, he was more of an emotional support animal that I was able to train and he was the one who helped me, get back in the public. Know not everyone is scary, but if they are, dogs are incredible judges and he would warn me. It takes a long time, it took me many years. 7 years after my trauma date, I finally had not too bad of a day on the day of. Of course my day wasn\u2019t normal, I wore protective earmuffs, blared music, and did things to make sure my body knew it was safe and that I was safe (which make look different for some people). But I say all that to say, you\u2019re not alone \u2764\ufe0f it feels lonely as hell but there are supports, this Reddit is one of them. And I say all this to say it gets better too. There\u2019s going to be rough days but there will be beautiful days too, it\u2019s all a garden"
      },
      {
        "id": "n5gcuh9",
        "score": 5,
        "body": "im sorry for what happened to you :(\ni personally haven\u2019t experienced PTSD/have it but my gf does and i\u2019m on this sub to better understand how she experiences the world (on top of what she tells me). your post really does help a lot, i hope you find your light at the end of the tunnel one day. i\u2019m trying so hard to be there for her through all of this so i truly do appreciate you speaking your mind here. best of luck <3"
      },
      {
        "id": "n5i6ppk",
        "score": 5,
        "body": "It\u2019s true that there aren\u2019t many people who can relate specifically to having diagnosed ptsd from SA (I can though, wish we weren\u2019t in this club) but a lot of people have been through traumatic things. I don\u2019t know that you could find an adult woman who hasn\u2019t been mistreated in some way by men. We all go through things and I\u2019ve found that when I\u2019m honest with people, even in vague ways like that I\u2019m having a hard time, they are nice about it and have often been through something really shitty themselves."
      },
      {
        "id": "n5jfkfq",
        "score": 5,
        "body": "Thank you for sharing with us. It made me feel not alone."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1lsfukq",
    "title": "I just saw one of my friends get his hand blown off",
    "body": "long story short\n\nYesterday, a friend of mine held a firework launcher and blew off a couple of fingers. When i saw his shirt covered in blood, I ran to him and wrapped my bandana around his hand, and kept his arm above his head. Whenever I think about it, I get anxious, and then I start breaking down. Idk if it is because I was overwhelmed, or if it was some form of ptsd but if someone could give me their thoughts ",
    "flair": "Advice",
    "score": 177,
    "comment_count": 52,
    "created_at": "2025-07-05T17:56:39+00:00",
    "top_comments": [
      {
        "id": "n1jgd56",
        "score": 67,
        "body": "I mean, it's pretty normal to be emotional about seeing someone get explosively and seriously injured.  People who show disdain for your emotions suck.  You did great to keep your head about you and help him out.  However you feel about it is just part of processing, and it's OK.  The more you can talk about it, write about it, tell ppl on line about it, the more likely you'll be able to figure it out and move on.  These unexpected and dramatic/chaotic events kind of shake our world, it can take a minute to find our feet again.  We've all been there."
      },
      {
        "id": "n1i9ni8",
        "score": 50,
        "body": "Play lots of Tetris over the next couple of days. It\u2019s been shown to prevent PTSD in some cases. \n\nI\u2019m so sorry this happened to you and your friend. I don\u2019t think you made the situation worse. I think you did a great job! A bit of water really won\u2019t hurt. Please be gentle with yourself. \ud83e\udec2"
      },
      {
        "id": "n1liszy",
        "score": 47,
        "body": "You acted quickly and rationally. It\u2019s amazing what you did. I have been through limb trauma and let me tell you, not everyone acts that way and keeps a cool head. It may catch up with you later, and how you process is ok too.\n\nThe \u201ctapping\u201d EMDR is used by the military and I learned it 30 years ago. Talk to someone or there is even an app, though you should talk to someone who deals with trauma too.\n\nYour friend had a life altering event. You.may not know what to say but don\u2019t ignore him. He is going to need help and support. Take care of yourself, so reach out too, it may help you as well. He will be in pain, need rehab and adjusting and it\u2019s good to not feel alone.  For me the pain never went away and I have brutal scarring. I had one friend open up about her son having lost part of a hand the same way and the chronic pain too."
      },
      {
        "id": "n1mnzxq",
        "score": 40,
        "body": "If you can, play Tetris immediately and go for long walks while thinking about the traumas. It has been proven that this has a similar effect to EMDR and helps prevent a trauma response from becoming PTSD."
      },
      {
        "id": "n1krqe9",
        "score": 36,
        "body": "Sorry youve gone through that. Its acute trauma and its normal to feel like youll break down. Your body and brain are trying to process. I remember after seeing my family member bust their head and hands open after a big fall and having to rush them to the emergency room, it took my body and brain several weeks at least to process it. Its ok to reach out to talk to someone if thats accessible to you. It can help. Heck, ive used free hotlines/textlines before and legit found them helpful. The people staffing them are always so nice and non judgmental. Take care."
      },
      {
        "id": "n1jddwi",
        "score": 33,
        "body": "Your girlfriend is literally trying to gaslight you dude. That\u2019s a form of emotional abuse. She doesn\u2019t get to dictate how you feel about something. Her only job is so comfort you. I\u2019m personally concerned for your future with someone that doesn\u2019t take your feelings seriously. That is a horrible thing to witness, it\u2019s not weird that you\u2019re traumatized. You just witnessed something brutal and out of the ordinary, of course you\u2019re affected. If she\u2019s willing to gaslight you over something most people would be traumatized by, it makes me wonder about all the little things too."
      },
      {
        "id": "n1j795y",
        "score": 23,
        "body": "I\u2019m so sorry \ud83d\ude22 I recommend calling your dr and setting up therapy if possible. Reacting with humor is also pretty normal. Like another person said, you don\u2019t want it to turn into PTSD so getting help soon could benefit you long term. I\u2019m going to hope that this is just a bad experience and won\u2019t affect your ability to function in day to day life. I hope your friend will be able to deal with the loss he\u2019s going through as well. \n\nDamn fireworks"
      },
      {
        "id": "n1nbxsx",
        "score": 20,
        "body": "2003 I got my fingers smashed in a 40 ton hydraulic metal press and had to have some amputation because they were basically hamburger meat. To this day certain sounds and even thinking about the situation gives me crazy PTSD symptoms --- best thing I've found is DISTRACTION. Anything to get my head FOCUSED on something is the only way to really pull me out of it"
      },
      {
        "id": "n1j2n1l",
        "score": 15,
        "body": "When I was about 16 or 17 I was a volunteer firefighter and witnessed some tough stuff. For about a week I struggled with some symptoms after responding to a traumatic death of someone I knew in the community. I kept seeing the images and felt the horror all over again on repeat and was very uncomfortable being alone. Luckily for me this didn\u2019t cause any long term symptoms and eventually I was able to move forward without thinking about it constantly. I developed PTSD later in life due to many other things. I hope you also don\u2019t have long lasting symptoms. It\u2019s ok that you feel the way you do right now and will probably feel this for a couple days to a couple weeks. However, time will tell if this will truly develops into PTSD. Everyone is different but my symptoms don\u2019t usually show up right away. It takes a couple weeks before I reach complete debilitation after an event. \n\nDo you already have a diagnosis prior to this happening yesterday? \n\nOddly, in January I witnessed a man ejected from his car and land on the pavement in front of my car and was dying in front of me breathing his last breath as I was on the line with 911. I felt nothing and after making a statement to the police when they arrived I continued with my life as usual. I felt bad for him and his family, but this didn\u2019t trigger my PTSD. My therapist says this can happen for people with the diagnosis, nothing really seems as bad as the things that gave me this ugly condition."
      },
      {
        "id": "n1jarwd",
        "score": 15,
        "body": "So this was a trauma, regardless of whatever happens or you continue to be affected by this. It is very common to have what are essentially PTSD like reactions in the immediate aftermath of a trauma, that doesn\u2019t mean it will necessarily \u2018stick around\u2019. \n\nMost traumas don\u2019t cause PTSD, even say a combat veteran won\u2019t necessarily have long term traumatic reactions from everything they\u2019ve experienced. There\u2019s a lot of things that go into it, but don\u2019t be alarmed that you\u2019re having these symptoms now, it\u2019s normal. Most people would be feeling like you\u2019re feeling. Doing things now such as playing Tetris can help you not develop longer term ptsd. Get good sleep, talk about how you feel, take care of yourself. \n\nYou are having a normal reaction to an abnormal event."
      }
    ]
  },
  {
    "subreddit": "PTSD",
    "id": "1jrdk4o",
    "title": "I\u2019m 17. I didn\u2019t go to war \u2014 but war came to me, and now I can\u2019t unsee it.",
    "body": "I dont know if this counts as PTSD, because Im not a veteran or a soldier. But I live in Ukraine. Kyiv. And war is part of my life now.\n\nSome days are calm. Some days a plane flies overhead and I flinch so hard I spill whatever I\u2019m holding.  \nSome nights, even when nothing explodes, I still hear things in my head.  \nI used to think trauma was only what happens when you lose a limb or see someone die in front of you.  \nNow I think it\u2019s also about trying to live normally when your brain still thinks it\u2019s under threat.\n\nI wrote a longer version of this experience \u2014 maybe someone here will relate: [https://medium.com/p/56e1ac5e3aa2](https://medium.com/p/56e1ac5e3aa2)",
    "flair": "Venting",
    "score": 175,
    "comment_count": 30,
    "created_at": "2025-04-04T14:42:16+00:00",
    "top_comments": [
      {
        "id": "mlf5prq",
        "score": 22,
        "body": "Of course it counts. PTSD and trauma are not just for soldiers. Please be kind to yourself \u2764\ufe0f"
      },
      {
        "id": "mlejxkh",
        "score": 19,
        "body": "Trauma is exactly trying to live normally while your brain and body still feel under threat. Your experience is completely valid and not unexpected under the circumstance."
      },
      {
        "id": "mle3enj",
        "score": 17,
        "body": "[deleted]"
      },
      {
        "id": "mlg3lc2",
        "score": 16,
        "body": "This may come across as nitpicking but it isn't. I and my children have been in a traumatizing circumstances for a while now. A 9yo refugee child from Ukraine happens to be the only one with whom my daughter can talk about it.\n\n\n**Post Traumatic** Stress Disorder is post traumatic, you are in trauma. During trauma various extreme behaviors and feelings are healthy survival reactions.\u00a0\n\n\nLookup the symptoms of Acute Traumatic Stress Disorder, that is the precursor to PTSD but is also post traumatic. Now, for the advice:\n\n\n- Symptoms of ATSD are acceptable while the threat is ongoing and real\n- Reassure yourself that dealing with ongoing threat presents not with symptoms but adaptations, all part of survival.\u00a0\n- Be aware of these symptoms and that they are supposed to pass, when the danger is rationally over.\u00a0"
      },
      {
        "id": "mle0tml",
        "score": 15,
        "body": "Anything that makes you fear for your life can be traumatic enough to cause PTSD.\n\nI can't diagnose you, but I would *absolutely* think that living in a city on the forefront of a 3 year war qualifies. \n\nBe gentle with yourself and take all the time you need to process / feel things. Its completely normal. Don't be afraid to talk to a professional if it's available / if you feel you need to."
      },
      {
        "id": "mlei8a1",
        "score": 13,
        "body": "You and everyone around you is likely experiencing PTSD. You don't have to be a soldier to suffer. I hope you can get the help you need."
      },
      {
        "id": "mldtc0a",
        "score": 13,
        "body": "Only a qualified health professional can tell you whether you have PTSD, but you definitely don\u2019t need to be a veteran or soldier to get it - I\u2019m not and I still got diagnosed. The criteria states that PTSD comes from being exposed to actual or threatened death, sexual violence, or severe bodily harm."
      },
      {
        "id": "mle1j29",
        "score": 12,
        "body": "u poor thing. ptsd doesnt have to be from military service."
      },
      {
        "id": "mliaroq",
        "score": 12,
        "body": "I\u2019m so sorry on behalf of America."
      },
      {
        "id": "mljscgh",
        "score": 11,
        "body": "I\u2019m a couple years older than you. It makes me sick to my stomach to see that politicians can still get away with destroying millions of lives, and for what? An ego boost? Richer pockets? I haven\u2019t personally been through war but I know ppl who have. I get you on the PTSD. I used to drink to make it all go away but it never did. All I gotta say is keep your head up no matter what. If you drown in sorrow, people like Putin win. Utilize your anger. Even when there aren\u2019t bombs exploding, the mind still has a way of exploding on its own and it sucks. I genuinely wish you the best. Stay safe. Stay alive. People like Putin will destroy themselves with their own insanity. Power like that always corrupts, all you can do is wait and let it all unfold. War sucks."
      }
    ]
  }
]
```
