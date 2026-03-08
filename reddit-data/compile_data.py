import json
import os

def make_post(title, author, url, selftext, score, date, subreddit, comments=None, flair=None):
    return {
        "title": title,
        "author": author,
        "url": url,
        "selftext": selftext,
        "score": score,
        "created_utc": date,
        "subreddit": subreddit,
        "flair": flair,
        "top_comments": comments or []
    }

def make_comment(author, text, score):
    return {"author": author, "body": text, "score": score}

posts = {
    "veteransbenefits": [],
    "veterans": [],
    "veteranwomen": [],
    "military": [],
    "militaryfinance": [],
    "vaclaims": [],
    "veteransaffairs": [],
}

# ==========================================
# r/VeteransBenefits posts
# ==========================================

posts["veteransbenefits"].append(make_post(
    "VA now says 94.8 days 'average to complete' disability claims",
    "Easy-Violinist-1469",
    "https://www.reddit.com/r/VeteransBenefits/comments/1n8r46r/va_now_says_948_days_average_to_complete/",
    "VA now says 94.8 days average to complete disability claims.",
    0, "2026-02-01", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Claimed jumped to 'rating' before C&P exams.",
    "gannon416",
    "https://www.reddit.com/r/VeteransBenefits/comments/1fasf6k/claimed_jumped_to_rating_before_cp_exams/",
    "I had a FDC with DBQs completed for increases on a few of my current ratings. I got a call from Optum to schedule C&Ps and I gave them my availability, but I didn't hear back for 2 weeks. I just checked online and now it is 'Preparing for Decision.' Seems unusual to request the C&P and then to skip it and go to Rating. Anyone else have this happen?",
    8, "2024-09-06", "VeteransBenefits",
    [make_comment("l8tn8", "Could be they feel the rater can make a partial decision based upon the evidence of record.", 10)]
))

posts["veteransbenefits"].append(make_post(
    "TDIU C&P exam for PTSD",
    "moneyman-11",
    "https://www.reddit.com/r/VeteransBenefits/comments/1q15ap5/tdiu_cp_exam_for_ptsd/",
    "Should I expect to have to re-prove that I have ptsd all over again, or will the questions just be about how my ptsd affects my ability to work? Im 68 years old and I just got awarded 70 percent less than 30 days ago for mental health (ptsd, major depressive disorder) and they inferred TDIU and sent me a deferred tdiu in my decision letter. Now they have scheduled me for a brand new C&P exam for PTSD again and I'm terrified the new examiner could have a totally different diagnosis.",
    0, "2026-01-15", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "C&P scheduling for musculoskeletal claims",
    "erb58",
    "https://www.reddit.com/r/VeteransBenefits/comments/1qov2lt/cp_scheduling_for_musculoskeletal_claims/",
    "Just filed for my left knee secondary to my already rated right knee on Sunday January 25, and the VA just called to schedule my c&p for 2 weeks from now. This is the fastest I've ever seen a claim move.",
    0, "2026-02-10", "VeteransBenefits",
    [make_comment("Saebre-Jade", "All of my C & P exams have been scheduled within days of the new claims but then it's a creeping halt.", 0)]
))

posts["veteransbenefits"].append(make_post(
    "Denied - Not Chronic & No Continuity of Symptoms",
    "Outkast983",
    "https://www.reddit.com/r/VeteransBenefits/comments/1j0i9ga/denied_not_chronic_no_continuity_of_symptoms/",
    "I was denied today for my back claim because they determined that my condition hasn't been chronic and that there were no continuity of symptoms from service to present (38 CFR 3.303). However, I included a detailed personal statement that detailed my continuous and persistent issues.",
    0, "2025-02-28", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "New Proposed VA Rating System For Mental Health",
    "Rabble_Runt",
    "https://www.reddit.com/r/VeteransBenefits/comments/1b86uvq/new_proposed_va_rating_system_for_mental_health/",
    "This video kind of breaks it down, but it sounds like good news for us vets. Many will be able to reach 100% after submitted for a re-evaluation with this new system.",
    305, "2024-03-06", "VeteransBenefits",
    [make_comment("Rabble_Runt", "Many will be able to reach 100% after submitted for a re-evaluation with this new system and get higher ratings without needing to be homicidal, suicidal, or be severely crippled by their mental health ailments.", 157)]
))

posts["veteransbenefits"].append(make_post(
    "For those who are 100% P&T for mental health, what evidence did you provide?",
    "Dependent_Ruin_3694",
    "https://www.reddit.com/r/VeteransBenefits/comments/1fidj6j/for_those_who_are_100_pt_for_mental_health_what/",
    "I'm at 70% and currently in VA therapy. I plan to apply for an increase when the treatment ends. I've been getting worse over the years. 2 combat tours to Iraq. 11B and CIB.",
    27, "2024-09-16", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Is it worth it to claim depression and anxiety if I never got seen?",
    "OPwano",
    "https://www.reddit.com/r/VeteransBenefits/comments/1i4sl00/is_it_worth_it_to_claim_depression_and_anxiety_if/",
    "I never got seen by a shrink/therapist while I was in service as I was a maintainer and any appointment I had and missed any time off work not just me but anyone was just auto called a POS and harassed. We had 6 suicides in 1 year.",
    31, "2025-01-19", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Mental Health Claims",
    "BullaloBill69",
    "https://www.reddit.com/r/VeteransBenefits/comments/1il712j/mental_health_claims/",
    "When VA examiners conduct any mental health exam they are looking for deficiencies in: 1. Employment Issues; 2. Family/Social Functions; 3. Appearance/Personal Hygiene; 4. Suicidal Ideation. If you are deficient in all of these areas VA will grant you 100%.",
    198, "2025-02-09", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "50 - 30 - 70: VA proposed to drop my mental health rating",
    "heathcm11",
    "https://www.reddit.com/r/VeteransBenefits/comments/1jk8tb1/50_30_70/",
    "VA proposed to drop my mental health rating from 50% to 30%. I fought it by requesting a Higher-Level Review. Instead of getting dropped, they increased me to 70%. This proves that fighting back works.",
    257, "2025-03-26", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Diagnosed with sleep apnea, what now?",
    "Blue_Banana_69",
    "https://www.reddit.com/r/VeteransBenefits/comments/1jnfd1n/diagnosed_with_sleep_apnea_what_now_what_are_my/",
    "Currently Upper back 10%, Neck 10%, Hip 10%, PTSD 70%. Infantry Vet with burn pit exposure. Got diagnosed with sleep apnea with CPAP, mild IBS-D, mild restless leg syndrome and chronic fatigue.",
    7, "2025-03-30", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Fake Nexus",
    "Material-Birthday531",
    "https://www.reddit.com/r/VeteransBenefits/comments/1iuet4e/fake_nexus/",
    "TLDR - a bunch of nurses are getting rich from writing useless IMOs. As a C&P Au.D I see one or two IMOs each week. 90% are from the same company. There is no reason to pay for this up front. Wait until you're denied.",
    229, "2025-02-21", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Denied for Sleep Apnea - Filed Supplemental With Nexus Letter",
    "rrebelo1",
    "https://www.reddit.com/r/VeteransBenefits/comments/1q8jsbc/denied_for_sleep_apnea_filed_supplemental_with/",
    "I was just denied service connection for OSA. The VA acknowledged I have OSA and use CPAP, but denied because C&P examiner wrote 'less likely than not' (citing obesity/age/anatomy). After denial, I went the secondary route since I'm service-connected for asthma (30%).",
    0, "2026-01-12", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Secondary Conditions for Tinnitus/Hearing Loss/Vertigo",
    "Hot_Ranger33",
    "https://www.reddit.com/r/VeteransBenefits/comments/1hunfx8/secondary_conditions_for_tinnitushearing/",
    "For the past six months I've experienced mental health issues like insomnia and anxiety secondary to Tinnitus/HL/Vertigo. My VSO said I need a nexus statement but private doctors won't do that.",
    7, "2025-01-06", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Did your higher level review actually do anything?",
    "No-Sorbet-3288",
    "https://www.reddit.com/r/VeteransBenefits/comments/1fizq3e/did_your_higher_level_review_actually_do_anything/",
    "I sent my claim up for higher level review but I just have a feeling it's not gonna make a difference.",
    20, "2024-09-17", "VeteransBenefits",
    [make_comment("KurtActual", "I opted for an informal conference. A week later I had the rating I felt I deserved.", 45)]
))

posts["veteransbenefits"].append(make_post(
    "VA Claims Clinics. Find one. Go to them.",
    "humanityinfive",
    "https://www.reddit.com/r/VeteransBenefits/comments/1gvcw2f/va_claims_clinics_find_one_go_to_them/",
    "I found out about this VA claims clinic in Colorado Springs 2 days ago, booked my flight from Texas. Everyone there WANTS to help you. By 12:30 I had done a C&P exam for Migraines & ED secondary to PTSD.",
    667, "2024-11-20", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Ingraham v Collins megathread.",
    "Mysterious-Space-343",
    "https://www.reddit.com/r/VeteransBenefits/comments/1r7s4cx/ingraham_v_collins_megathread/",
    "Obviously this isn't great. No one should sugar coat this. The feedback pathway is not working. We need pressure on the contact to make sure our feedback is heard.",
    0, "2026-02-17", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "VA looking to overturn Ingram v. Collins",
    "t2_6a9zt6cr",
    "https://www.reddit.com/r/VeteransBenefits/comments/1r4uuty/va_looking_to_overturn_ingram_v_collins/",
    "https://public-inspection.federalregister.gov/2026-03068.pdf",
    207, "2026-02-14", "VeteransBenefits",
    [
        make_comment("xAsiNine-", "Bold of you too assume any of us can read", 289),
        make_comment("Personal-Couple-3444", "lmao I actually tried to open that PDF and my brain immediately shut down after the first paragraph of legal jargon.", 105)
    ]
))

posts["veteransbenefits"].append(make_post(
    "U.S. Department of Veterans Affairs Publishes Interim Final Rule on 38 CFR 4.10",
    "t2_13agua9ky2",
    "https://www.reddit.com/r/VeteransBenefits/comments/1r7nbt3/us_department_of_veterans_affairs_publishes/",
    "On February 17, 2026, the VA issued an Interim Final Rule amending 38 CFR 4.10, changing how disability ratings account for medication and treatment effects.",
    0, "2026-02-18", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "What's the most received you in retroactive pay?",
    "Acceptable-World8458",
    "https://www.reddit.com/r/VeteransBenefits/comments/13rlyht/whats_the_most_received_you_in_retroactive_pay/",
    "Let's see...",
    42, "2023-05-25", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "SSDI Claims for all you who are 100% P&T",
    "DowntownDvo",
    "https://www.reddit.com/r/VeteransBenefits/comments/1e5ktxj/ssdi_claims_for_all_you_who_are_100_pt/",
    "Curious to know about what state you are in and if you filed for SSDI after receiving your 100% rating.",
    102, "2024-07-17", "VeteransBenefits",
    [make_comment("hospitallers", "Indiana. No. Fast tracked.", 139)]
))

posts["veteransbenefits"].append(make_post(
    "How quickly should I expect the back pay direct deposit?",
    "Existing_Path_2199",
    "https://www.reddit.com/r/VeteransBenefits/comments/1c0kcw0/how_quickly_should_i_expect_the_back_pay_direct/",
    "I have been at 10% since Dec 2013 and was just awarded 60%. They are paying me from the date of the intent to file which was July of 2023.",
    30, "2024-04-10", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "SMC(t) and major case win for veterans! Haskell v. McDonough",
    "lawhopeful24",
    "https://www.reddit.com/r/VeteransBenefits/comments/1fae4c0/smct_and_major_case_win_for_veterans_haskell_v/",
    "I have watched so much misinformation posted by VBA employees over SMC(t). Leadership inside VA for years have tried to make certain benefits harder to reach.",
    153, "2024-09-06", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Best way to utilize the tax-free compensation",
    "No_Rub_8605",
    "https://www.reddit.com/r/VeteransBenefits/comments/1ik7vhp/best_way_to_utilize_the_taxfree_compensation/",
    "I just got my rating and I'm into finance/FIRE. How do you guys maximize your compensation income?",
    23, "2025-02-07", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "PTSD Claim due to MST",
    "NoInfluence4377",
    "https://www.reddit.com/r/VeteransBenefits/comments/1gbc38v/ptsd_claim_due_to_mst/",
    "Had my first C&P exam regarding my PTSD caused by MST. I completely broke down during the exam and the doctor terminated it early saying I have more than enough supporting documents.",
    33, "2024-10-24", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "MST after 40 years Is it possible?",
    "Souless_damage",
    "https://www.reddit.com/r/VeteransBenefits/comments/1j7n6bt/mst_after_40_years_is_it_possible/",
    "I have an enormous amount of PTSD I'm dealing with. After about 2 years in the national guard I went active duty.",
    26, "2025-03-10", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "MST claim without have reported",
    "Expensive-Manager945",
    "https://www.reddit.com/r/VeteransBenefits/comments/1cjndqo/mst_claim_without_have_reported/",
    "My husband was SA'ed while AD in the barracks. He attempted to report but his staff told him no one will believe him and 'men don't get SA'ed.'",
    46, "2024-05-04", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Do MST claims really take over a year?",
    "LeoraKitty78",
    "https://www.reddit.com/r/VeteransBenefits/comments/1izykmq/do_mst_claims_really_take_over_a_year/",
    "ITF in Nov 2024. Primary PTSD due to MST, several secondary conditions. MST claims take at least a year, and it might get worse given federal layoffs.",
    5, "2025-02-28", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "VA rejects more PTSD claims linked to sexual trauma",
    "[deleted]",
    "https://www.reddit.com/r/VeteransBenefits/comments/198watb/va_rejects_more_ptsd_claims_linked_to_sexual/",
    "VA rejects more PTSD claims linked to sexual trauma than any other type.",
    127, "2024-01-17", "VeteransBenefits",
    [make_comment("LastOneSergeant", "Combat is often well documented. MST events may have been told to no one.", 113)]
))

posts["veteransbenefits"].append(make_post(
    "Why isn't the VA talked about when you're still in before you out process?",
    "Ok-Surround-962",
    "https://www.reddit.com/r/VeteransBenefits/comments/1k5qpmf/why_is_isnt_the_va_talked_about_when_your_still/",
    "When I got out in 2008, at no point do I remember anyone telling me about filing a claim for disability or that it was even possible before you get out.",
    110, "2025-04-23", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "F*ck your BDD",
    "t2_g4tdgsxj",
    "https://www.reddit.com/r/VeteransBenefits/comments/1p3ewp7/fck_your_bdd/",
    "Imagine being 5 months from EASing, requesting BDD and C&P exams, and your command tells you 'they can wait until after they get out.'",
    205, "2025-11-22", "VeteransBenefits",
    [make_comment("thesupplyguy1", "Ah shitty leadership rears its ugly head", 329)]
))

posts["veteransbenefits"].append(make_post(
    "Got my rating today. Question...",
    "TX_VetOEF",
    "https://www.reddit.com/r/VeteransBenefits/comments/1jwyqmp/got_my_rating_today_question/",
    "Went from 80-90%. GERD denied, Migraines 30%, Plantar fasciitis 10%. All with private doctors and nexus letters. Should I request a HLR?",
    247, "2025-04-11", "VeteransBenefits",
    [make_comment("Mental-Back6028", "Don't just file one because you feel like it but do it strategically.", 56)]
))

posts["veteransbenefits"].append(make_post(
    "90% the last 10% seems impossible.",
    "t2_zmsrgi5hm",
    "https://www.reddit.com/r/VeteransBenefits/comments/1i86jb2/90_the_last_10_seems_impossible/",
    "I'm rated at 90% and trying to figure out if I'm out of options. 10% ankle, 10% sinusitis, 10% gerd, 30% IBS, 50% Migraines, 50% Sleep Apnea. Denied 10% tinnitus even though my job code was on hazardous noise exposure list.",
    0, "2025-01-23", "VeteransBenefits",
    [make_comment("DesiccantPack", "You're at 88%, rounded up to 90%. Another 10% would only get you to 89.2%.", 19)]
))

posts["veteransbenefits"].append(make_post(
    "They Denied all my claims. I feel so defeated.",
    "Puzzled_Shoe1277",
    "https://www.reddit.com/r/VeteransBenefits/comments/1eywxdw/the_denied_all_my_claims_i_feel_so_defeated/",
    "They said I have current diagnosis for all my claims (migraines, GERD and sleep apnea) and they see it's in my record but in the doctors opinion, it's not service connected.",
    125, "2024-08-22", "VeteransBenefits",
    [make_comment("damnshell", "I would post the decision letter (redacted). We can help you figure out what went wrong.", 96)]
))

posts["veteransbenefits"].append(make_post(
    "IBS should go higher than 30%",
    "Nice_Atmosphere2940",
    "https://www.reddit.com/r/VeteransBenefits/comments/1ji92mk/ibs_should_go_higher_than_30/",
    "IBS should definitely go higher than 30%. This damn disease is BRUTAL. It absolutely runs my life. Also I'm writing this while shitting my pants.",
    95, "2025-03-23", "VeteransBenefits",
    [make_comment("TechImage69", "The VA is really weird with how they rate certain things. Like an above the knee amputation is 60% while sleep apnea with a CPAP is 50.", 40)]
))

posts["veteransbenefits"].append(make_post(
    "Denied 100%",
    "Recent-Revenue59",
    "https://www.reddit.com/r/VeteransBenefits/comments/1ja6quk/denied_100/",
    "Since 2018 dealing with bad back, PTSD, lower extremities, migraines. Keep getting denied for unemployability even though decision letters say I qualify. My VA rep isn't getting this done.",
    92, "2025-03-13", "VeteransBenefits",
    [make_comment("Hour-Ad863", "You last worked Nov 2024 and DID NOT provide what they requested.", 180)]
))

posts["veteransbenefits"].append(make_post(
    "Reevaluated when already 100% P&T",
    "t2_8yucsa5i",
    "https://www.reddit.com/r/VeteransBenefits/comments/16q5lnm/reevaluated_when_already_100_pt/",
    "What opens the door to being reevaluated when already 100% P&T? DAV says submitting a new claim within first 10yrs opens the door for reevaluation.",
    48, "2023-09-23", "VeteransBenefits",
    [make_comment("Prize_Way_6300", "If you open a claim to increase the disability it will. If you open a claim for an effective date review it wont.", 39)]
))

posts["veteransbenefits"].append(make_post(
    "Tinnitus - VA rating change",
    "Temporary_Eagle_4601",
    "https://www.reddit.com/r/VeteransBenefits/comments/1ojgl55/tinnitus_va_rating_change/",
    "Filed tinnitus/hearing loss claim in April 25. Denied due to no nexus in July. Filed ITF in August. VA changed the tinnitus rating in April 25. Will a supplemental claim fall under old or new rating?",
    0, "2025-10-15", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "An insider tip for using VR&E for school",
    "squirrelyguy08",
    "https://www.reddit.com/r/VeteransBenefits/comments/1elvwqi/an_insider_tip_for_using_vre_for_school/",
    "Don't wait until July to apply for VR&E if you want to start school in August. I scheduled 79 applicants for their initial orientation today.",
    47, "2024-08-06", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "60 years old.",
    "Humble-Grapefruit-64",
    "https://www.reddit.com/r/VeteransBenefits/comments/1f6cnua/60_years_old/",
    "Is there even a point in trying for benefits at my age? I was stupid and never attempted before. I can't produce medical history because the doctors no longer have my records.",
    169, "2024-09-01", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Just got denied PACT Act presumptive condition",
    "RomeoGoth",
    "https://www.reddit.com/r/VeteransBenefits/comments/1g9yvn8/just_got_denied_pact_act_presumptive_condition/",
    "I have COPD and Asthma. I thought these were presumptive conditions through the PACT Act. I even had a nexus letter from a pulmonologist.",
    27, "2024-10-23", "VeteransBenefits",
    [make_comment("Jmoste", "You need a yes to one of the following: You served in the Vietnam War, the Gulf War, Iraq...", 17)]
))

posts["veteransbenefits"].append(make_post(
    "PACT Act Presumptives Expanded",
    "b-1245",
    "https://www.reddit.com/r/VeteransBenefits/comments/1j98fkt/pact_act_presumptives_expanded/",
    "For years I've been working on getting survivor benefits for my mom after my dad died in 2016 from Multiple Myeloma. Multiple myeloma is now presumptive without the head/neck caveat.",
    329, "2025-03-12", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Presumptive conditions denial",
    "t2_myawxcvf",
    "https://www.reddit.com/r/VeteransBenefits/comments/1kztid4/presumptive_conditions_denial/",
    "My husband has just got his second denial (going on two years now) for Asthma. He has failed multiple VA tests, has letters from his doctors, and takes a daily inhaler. His VSO says he qualifies under presumptive conditions.",
    21, "2025-05-31", "VeteransBenefits",
    [make_comment("This_Lychee_319", "Asthma is only presumptive if diagnosed after service. If diagnosed during service, you need direct service connection.", 13)]
))

posts["veteransbenefits"].append(make_post(
    "Tdiu backpay",
    "t2_qdq437pp",
    "https://www.reddit.com/r/VeteransBenefits/comments/1jkpvor/tdiu_backpay/",
    "In group therapy, met a veteran already 100% P&T filing TDIU to get backpay from his SSDI date, about 7 years. Me and another VA employee were shaking our heads.",
    0, "2025-03-26", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "HLR statement",
    "Quirky_Mission_8761",
    "https://www.reddit.com/r/VeteransBenefits/comments/1jq3dlb/hlr_statement/",
    "Would like some feedback on this HLR statement. Any comments or suggestions welcomed.",
    32, "2025-04-02", "VeteransBenefits",
    [make_comment("anglflw", "This looks really good. As for the BVA decision, they are not precedential.", 6)]
))

posts["veteransbenefits"].append(make_post(
    "Obstructive sleep apnea",
    "WhereasGlittering289",
    "https://www.reddit.com/r/VeteransBenefits/comments/1g3du4p/obstructive_sleep_apnea/",
    "Diagnosed with OSA, at 90% disability with back pain, migraines, tinnitus, knee pain. Gained almost 100lbs since leaving the army in 2018.",
    6, "2024-10-14", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "Presumptive Conditions - PACT ACT",
    "t2_99r7j7s7",
    "https://www.reddit.com/r/VeteransBenefits/comments/1k70lmh/presumptive_conditions_pact_act/",
    "How many of you were able to use the PACT ACT and burn pits to your advantage? I was denied on items with medical evidence. Is the presumptive list useless?",
    3, "2025-04-24", "VeteransBenefits",
    [make_comment("nickusmp", "Presumptive conditions put me over 100%, they are awesome. GERD however isn't on that list.", 5)]
))

posts["veteransbenefits"].append(make_post(
    "How much disability does MST get someone?",
    "Aggravating-Team-672",
    "https://www.reddit.com/r/VeteransBenefits/comments/1no4hpx/how_much_disability_does_mst_get_someone/",
    "Earlier this year I had a very bad MST case. I reported it and it was founded. I've gone to BH for the mental trauma and stress. This event has ruined my military career and made me very depressed and suicidal.",
    0, "2025-12-01", "VeteransBenefits"
))

posts["veteransbenefits"].append(make_post(
    "100% P&T 18 months later",
    "t2_xomhed7ap",
    "https://www.reddit.com/r/VeteransSuccess/comments/1qxo79k/100_pt_18_months_later/",
    "I am so beyond grateful. Originally granted 70% for MH in 2014. In 2024 I filed for an increase and was denied. The C&P examiner was rude, dismissive, and short. The exam was 10 minutes. Joined Berry Law for an HLR. HLR denied. Submitted a supplemental claim and finally got 100% P&T.",
    0, "2026-02-06", "VeteransBenefits"
))

# ==========================================
# r/Veterans posts
# ==========================================

posts["veterans"].append(make_post(
    "Denied TDIU w/ Proposed Reduction",
    "SimpleLuck4",
    "https://www.reddit.com/r/Veterans/comments/g4zy6g/denied_tdiu_w_proposed_reduction/",
    "Filed initial claim Sep 2019. Granted 70% PTSD in November. Applied for TDIU Dec 2019. C&P exam not favorable. Examiner felt condition improved. My decision letter said non-service condition qualifies for TDIU but not my SC.",
    13, "2020-04-20", "Veterans"
))

posts["veterans"].append(make_post(
    "Help with TDIU claim",
    "PinkTessa90543",
    "https://www.reddit.com/r/Veterans/comments/piggsy/help_with_tdiu_claim/",
    "Rated combined 90%, 70% PTSD w/alcohol use disorder and 50% cirrhosis. Haven't been able to work since 2017. VA rejected TDIU claim. Attorney filed supplemental claim. Rejected again - doctor's letter 'does not constitute relevant evidence.'",
    0, "2021-09-05", "Veterans"
))

posts["veterans"].append(make_post(
    "What Happens At C&P Exams - The Reason So Many People Hate Going?",
    "ChanelAce91",
    "https://www.reddit.com/r/Veterans/comments/1j200oi/what_happens_at_cp_exams_the_reason_so_many/",
    "The goal is to figure out whether your condition is linked to your time in service. So, why do so many people hate these exams?",
    54, "2025-03-02", "Veterans",
    [make_comment("_liveunderpar", "I feel like I am at the whims on their ability to be in a good mood. Instead of describing the disability I feel like I'm in court trying to prove beyond a certain preponderance of evidence.", 134)]
))

posts["veterans"].append(make_post(
    "Bills Introduced in 2025 Concerning Veterans",
    "Infinite_Flounder958",
    "https://www.reddit.com/r/Veterans/comments/1itmz7o/bills_introduced_in_2025_concerning_veterans/",
    "Dental Care for Veterans Act, Disabled Veterans Housing Support Act, Veterans Foreign Medical Coverage Act, Veteran Overmedication and Suicide Prevention Act, Veterans' True Choice Act, Veterans Health Care Freedom Act.",
    304, "2025-02-20", "Veterans"
))

posts["veterans"].append(make_post(
    "Getting laid off, thinking of going back to school on GI bill",
    "V0latyle",
    "https://www.reddit.com/r/Veterans/comments/1iybfdz/getting_laid_off_at_end_of_next_month_thinking_of/",
    "Employer is selling the product line. Considering GI bill for electronics engineering degree. Married with 2 kids, wife is stay at home mom. Can I support my family on Post 9/11?",
    41, "2025-02-26", "Veterans"
))

posts["veterans"].append(make_post(
    "Jan 2026 GI Bill text check in",
    "t2_1jmvnd60rz",
    "https://www.reddit.com/r/Veterans/comments/1quayev/jan_2026_gi_bill_text_check_in/",
    "Did anyone get the end of month text asking if you were enrolled for January? It's 2 Feb and I didn't get the text.",
    3, "2026-02-02", "Veterans"
))

posts["veterans"].append(make_post(
    "Anyone not get their housing allowance on post 9/11 GI Bill yet?",
    "t2_itfjwi59",
    "https://www.reddit.com/r/Veterans/comments/1pz1t0c/anyone_not_get_their_housing_allowance_on_post/",
    "Anyone still waiting on post 911 GI Bill? I usually get it on the 28th or 29th. Worried about Rent. My wife doesn't work and we rely heavy on that money.",
    3, "2025-12-29", "Veterans"
))

posts["veterans"].append(make_post(
    "Interesting Rolling Stone article on future of Veterans preference and VA benefits",
    "91361_throwaway",
    "https://www.reddit.com/r/army/comments/1ip373h/interesting_rolling_stones_article_on_future_of/",
    "Rolling Stone article about Trump/Musk/DOGE impact on military and veterans.",
    134, "2025-02-14", "Veterans",
    [make_comment("Holeyfield", "How am I supposed to read this? I'm being paywalled.", 153)]
))

posts["veterans"].append(make_post(
    "Father discharged honorably and died, is his GI bill gone?",
    "GreasyFDR",
    "https://www.reddit.com/r/VeteransBenefits/comments/1g0ka00/father_discharged_honorably_and_died_due_to/",
    "My father killed himself when I was 14 and ever since then I have gotten no survivor benefits and his GI bill became inaccessible. I'm 22 and don't know where to turn.",
    10, "2024-10-10", "Veterans"
))

# ==========================================
# r/VAClaims posts
# ==========================================

posts["vaclaims"].append(make_post(
    "I used AI to analyze 52 weeks of VA claim appeals data",
    "t2_9ph1se7k",
    "https://www.reddit.com/r/VAClaims/comments/1q9msbe/i_used_ai_to_analyze_52_weeks_of_va_claim_appeals/",
    "Supplemental Claims dropped from 467k pending to 283k in 2025. If you were denied, don't wait - the VA is processing appeals fast right now.",
    0, "2026-01-11", "VAClaims"
))

posts["vaclaims"].append(make_post(
    "I analyzed all 12 months of VA appeals data from 2025",
    "t2_9ph1se7k",
    "https://www.reddit.com/r/VAClaims/comments/1q5o43s/i_analyzed_all_12_months_of_va_appeals_data_from/",
    "VA completed 1M+ appeals in 2025. Processing times dropped 49%. But the math is suspicious and patterns look like metric gaming.",
    0, "2026-01-06", "VAClaims"
))

posts["vaclaims"].append(make_post(
    "Should I file an HLR or Supplemental claim?",
    "t2_dbqzp",
    "https://www.reddit.com/r/VAClaims/comments/1qrdd5v/should_i_file_an_hlr_or_supplemental_claim/",
    "Just got denied for GERD and Moderate OSA. Diagnosed with both. ChatGPT thinks I should file a supplemental claim.",
    5, "2026-01-30", "VAClaims",
    [make_comment("Dry_Sorbet_1202", "You need a Nexus for both", 5)]
))

posts["vaclaims"].append(make_post(
    "Ingram v. Collins Is Dead: VA Just Changed How Medication Affects Your Disability Rating",
    "PrestigiousBarnacle",
    "https://www.reddit.com/r/VAClaims/comments/1r588ak/ingram_v_collins_is_dead_va_just_changed_how/",
    "Rule signed by Secretary Collins Feb 11, 2026. Affects over 500 diagnostic codes and 350,000 pending claims. Classified as major rule with $100M+ annual impact.",
    0, "2026-02-15", "VAClaims"
))

posts["vaclaims"].append(make_post(
    "Ingraham v Collins is going to hose a lot of veterans' claims",
    "t2_1i3u048r",
    "https://www.reddit.com/r/VAClaims/comments/1r67dc6/ingraham_v_collins_is_going_to_hose_a_lot_of/",
    "VA Secretary Doug Collins said it 'will not be enforced at any time in the future' due to veteran community's reaction. But the announcement infuriated veterans and advocacy groups - VFW, DAV, American Legion all criticized it.",
    0, "2026-02-16", "VAClaims"
))

posts["vaclaims"].append(make_post(
    "What part of the VA claim process frustrated you the most?",
    "t2_1w3au9fiyl",
    "https://www.reddit.com/r/VAClaims/comments/1n8apbm/what_part_of_the_va_claim_process_frustrated_you/",
    "For me, it wasn't the paperwork - it was the waiting. The long gaps with no updates and the feeling like everything was stuck in limbo.",
    16, "2025-09-04", "VAClaims",
    [make_comment("Outrageous-World-438", "The back and forth. I had one claim I fought with three HLRs before it was adjudicated 18 months after claim submission.", 15)]
))

posts["vaclaims"].append(make_post(
    "VA Claims Backlog Shrinking",
    "t2_2v1qaeof",
    "https://www.reddit.com/r/VAClaims/comments/1mpgc2v/va_claims_backlog_shrinking/",
    "I'm going to take this as a good sign. Claims seem to be moving fast.",
    78, "2025-08-13", "VAClaims",
    [
        make_comment("FluffyDownstairs", "They're rushing through claims to say they've reduced the backlog but aren't adjudicating in the best interest of the veteran.", 61),
        make_comment("educatemyself1", "As a VBA Rater, rushing actually helps Veterans. It's so much easier for me to grant than deny.", 93)
    ]
))

posts["vaclaims"].append(make_post(
    "Been waiting since September and they denied everything!",
    "Available_Mixture819",
    "https://www.reddit.com/r/VAClaims/comments/1k4htfw/been_waiting_since_september_and_the_denied/",
    "My father had a stroke in Feb 2024. He's basically a vegetable. Social worker said he needs at least 70% to qualify for care support program.",
    35, "2025-04-21", "VAClaims"
))

posts["vaclaims"].append(make_post(
    "Why Was This Denied?",
    "t2_n3l94gbvv",
    "https://www.reddit.com/r/VAClaims/comments/1llcxjo/why_was_this_denied/",
    "No complaints in records but I'm literally in physical therapy for this and C&P said I have symptoms.",
    13, "2025-06-26", "VAClaims",
    [make_comment("scotty_dont81", "You don't have a diagnosis, only symptoms. No diagnosis, no service connection.", 12)]
))

posts["vaclaims"].append(make_post(
    "NEW VA RATING CRITERIA",
    "SpeakerOwn4589",
    "https://www.reddit.com/r/VAClaims/comments/1r6fpad/new_va_rating_criteria/",
    "Even if you have claims submitted before this change you will still be rated off the new criteria?",
    0, "2026-02-17", "VAClaims"
))

posts["vaclaims"].append(make_post(
    "BENEFITS FRAUD 18 FEB 26",
    "Postnutfomo",
    "https://www.reddit.com/r/VAClaims/comments/1r8paxj/benefits_fraud_18_feb_26/",
    "Before this turns into mass panic: VA cannot legally reduce a rating without due process under 38 CFR 3.105. There are 5-year, 10-year, 20-year protections and stability of rating rules.",
    0, "2026-02-18", "VAClaims"
))

posts["vaclaims"].append(make_post(
    "C&P examiners are not your friends or your doctor",
    "bmattock",
    "https://www.reddit.com/r/VAClaims/comments/1mlb3o9/cp_examiners_are_not_your_friends_or_your_doctor/",
    "C&P examiners are paid by the VA. They do not work for you. Veterans walk into exams thinking they will explain their way into a diagnosis.",
    0, "2025-07-01", "VAClaims"
))

posts["vaclaims"].append(make_post(
    "Insomnia secondary to tinnitus?",
    "t2_sts6csy1",
    "https://www.reddit.com/r/VAClaims/comments/1qx5k5j/insomnia_secondary_to_tinnitus/",
    "My ptsd claim got denied but they added insomnia as a secondary to tinnitus? I thought this wasn't allowed.",
    6, "2026-02-06", "VAClaims"
))

posts["vaclaims"].append(make_post(
    "Already 100% P&T why are they trying to make me TDIU",
    "[deleted]",
    "https://www.reddit.com/r/VAClaims/comments/1oy51oo/im_already_100_pt_why_are_they_trying_to_make_me/",
    "[deleted]",
    65, "2025-11-15", "VAClaims",
    [make_comment("Neat-Gap-8383", "VA operates under the Duty to Assist which mandates TDIU investigation if evidence 'reasonably raises' the issue of unemployability.", 22)]
))

# ==========================================
# r/VeteransAffairs posts
# ==========================================

posts["veteransaffairs"].append(make_post(
    "Just lost two Doctors in a month",
    "Velodrome321",
    "https://www.reddit.com/r/VeteransAffairs/comments/1j9k74o/just_lost_two_doctors_in_a_month/",
    "100% SC for PTSD. I need to build trust to open up. Finally had a good psychiatrist after years. Both chief of psychiatry and head of primary are gone. I have a feeling this is from DOGE.",
    185, "2025-03-12", "VeteransAffairs"
))

posts["veteransaffairs"].append(make_post(
    "What do you think the real issue is with the VA?",
    "SageinIt",
    "https://www.reddit.com/r/VeteransAffairs/comments/1joivcn/what_do_you_think_the_real_issue_is_with_the_va/",
    "I'm a VA employee. If I hear one more time that VA medical care is terrible, I'm going to scream. RIF and everything happening isn't the answer. Morale is crappy.",
    70, "2025-04-01", "VeteransAffairs"
))

posts["veteransaffairs"].append(make_post(
    "If the VA really cared about saving money they'd cancel Oracle Cerner EHR",
    "nahhhright",
    "https://www.reddit.com/r/VeteransAffairs/comments/1j7wfhk/if_the_vaadministration_really_cared_about_saving/",
    "Paused in April 2023 due to issues. Initially paid 10 billion. They want the system broken for privatization. Estimated staff loss of 80,000.",
    194, "2025-03-10", "VeteransAffairs"
))

posts["veteransaffairs"].append(make_post(
    "An open letter to Secretary Collins",
    "mcub66",
    "https://www.reddit.com/r/VeteransAffairs/comments/1j4yfux/an_open_letter_to_secretary_collins/",
    "Given recent workforce reductions across federal agencies, I urge you to prioritize displaced employees for vacant VA positions.",
    182, "2025-03-06", "VeteransAffairs"
))

posts["veteransaffairs"].append(make_post(
    "Has anyone heard how many VA jobs will be cut?",
    "Fun_Drawer5972",
    "https://www.reddit.com/r/VHA_Human_Resources/comments/1jpbtlo/has_anyone_heard_how_many_va_jobs_will_be_cut/",
    "Specifically VHA - done have a percentage of people they plan to RIF?",
    38, "2025-04-02", "VeteransAffairs",
    [make_comment("VA-Person", "They want staffing levels from 2019. Not accounting for roughly 1 million new Veterans since PACT Act expanded care. Estimated staff loss of 80,000.", 93)]
))

# ==========================================
# r/Military posts
# ==========================================

posts["military"].append(make_post(
    "Veterans benefit group deleted my post regarding project 2025",
    "Optimus-fallen",
    "https://www.reddit.com/r/Military/comments/1dtznto/veterans_benefit_group_deleted_my_post_regarding/",
    "The admins are against us informing each other. I'm banned from posting after asking the question.",
    431, "2024-07-02", "Military",
    [make_comment("RutabagaJoe", "They list changes to our benefits: More reevaluation exams, Removing concurrent receipt...", 283)]
))

posts["military"].append(make_post(
    "Project 2025 would slash veterans' hard-earned benefits",
    "h20poIo",
    "https://www.reddit.com/r/Military/comments/1ejepb1/project_2025_would_slash_veterans_hardearned/",
    "From Task & Purpose article on Project 2025 implications for veterans.",
    470, "2024-08-03", "Military",
    [make_comment("billsatwork", "It baffles me how many veterans love their TriCare and disability checks but continually vote for the party that wants to slash their services.", 215)]
))

posts["military"].append(make_post(
    "American veterans now receive absurdly generous benefits",
    "ATLs_finest",
    "https://www.reddit.com/r/Military/comments/1h2z6fv/american_veterans_now_receive_absurdly_generous/",
    "Apparently taking care of veterans who fight for their country is 'absurdly generous.' Coming from the Economist, who supported the war in Iraq.",
    1263, "2024-11-29", "Military",
    [make_comment("Wr3nch", "If I volunteer to put my life on the line defending my nation and their rich politicians' interests...", 1063)]
))

posts["military"].append(make_post(
    "Project 2025 wants to get rid of concurrent retirement and VA disability pay",
    "catatonic_envy",
    "https://www.reddit.com/r/Military/comments/1dtokgo/project_2025_wants_to_get_rid_of_concurrent/",
    "VA should eliminate concurrent eligibility for both disability benefits and retirement benefits, reducing outlays by $160 billion. This is horrendous.",
    1300, "2024-07-02", "Military",
    [make_comment("chufenschmirtz", "If they are concerned with outlay, start with abolishing Retirement Benefits for Members of Congress.", 719)]
))

posts["military"].append(make_post(
    "New VA disability rule: OPEN COMMENT PERIOD, make your voice heard!",
    "rockylizard",
    "https://www.reddit.com/r/Military/comments/1r8mq0k/new_va_disability_rule_open_comment_period_please/",
    "The VA can now consider your improvement with medication when choosing to grant benefits. Federal Register comment period is LIVE NOW until April!",
    0, "2026-02-18", "Military"
))

posts["military"].append(make_post(
    "Veterans slam new VA rule for determining disability ratings",
    "RutabagaAny7427",
    "https://www.reddit.com/r/uscg/comments/1r7t7ji/veterans_slam_new_va_rule_for_determining/",
    "Stars and Stripes article on new VA disability rule.",
    0, "2026-02-18", "Military",
    [
        make_comment("Deep-Kangaroo6010", "This was outlined in project 2025. Whoever voted for trump voted for this.", 109),
        make_comment("u-give-luv-badname", "This is a BIG deal. Check the Ingraham v. Collins megathread.", 0)
    ]
))

posts["military"].append(make_post(
    "P2025 wants to eliminate several VA benefits, including CDRP, CRSC",
    "twicefriedwings",
    "https://www.reddit.com/r/army/comments/1e51k20/p2025_wants_to_eliminate_several_va_benefits/",
    "Heritage Foundation proposals: eliminate concurrent eligibility for disability and retirement benefits. Other recommendations that would affect all veterans.",
    627, "2024-07-16", "Military"
))

posts["military"].append(make_post(
    "Secretary Collins' message to Veterans and VA employees",
    "Imadick2",
    "https://www.reddit.com/r/navy/comments/1iirfmd/secretary_collins_message_to_veterans_and_va/",
    "It is my life's honor to serve America's Veterans as secretary of Veterans Affairs.",
    79, "2025-02-06", "Military"
))

# ==========================================
# r/MilitaryFinance posts
# ==========================================

posts["militaryfinance"].append(make_post(
    "Best way to utilize the tax-free compensation",
    "No_Rub_8605",
    "https://www.reddit.com/r/VeteransBenefits/comments/1ik7vhp/best_way_to_utilize_the_taxfree_compensation/",
    "I just got my rating and I'm into FIRE. How do you maximize your compensation income?",
    23, "2025-02-07", "VeteransBenefits"
))

posts["militaryfinance"].append(make_post(
    "Introduce Means-Testing for VA Disability Compensation",
    "Polvbear",
    "https://www.reddit.com/r/USMC/comments/1iasgtv/introduce_meanstesting_for_eligibility_for_vas/",
    "This misses why disability for veterans exists. The level of employability is not the whole picture. My quality of life is definitively less.",
    74, "2025-01-26", "USMC"
))

posts["militaryfinance"].append(make_post(
    "How Does VA Disability Calculate Into Net Worth?",
    "t2_xulo2nw33",
    "https://www.reddit.com/r/DaveRamsey/comments/1el3onj/how_does_va_disability_calculate_into_net_worth/",
    "100% disability = roughly 2.4 million dollars tax free over 50 years. No copays, no health insurance premiums, no property taxes in most states.",
    2, "2024-08-06", "DaveRamsey"
))

posts["militaryfinance"].append(make_post(
    "Any former military here? Looking for advice on veteran benefits and FIRE",
    "BaryOwen",
    "https://www.reddit.com/r/financialindependence/comments/8jdl76/any_former_military_here_looking_for_advice_on/",
    "I get small passive income through VA as well as access to healthcare. I have a Purple Heart. In California, any kids I have will save on tuition at UC. Any other veteran hacks?",
    16, "2018-05-14", "financialindependence"
))

# ==========================================
# r/VeteranWomen posts (MST-related since r/VeteranWomen is small)
# ==========================================

posts["veteranwomen"].append(make_post(
    "PTSD Claim due to MST",
    "NoInfluence4377",
    "https://www.reddit.com/r/VeteransBenefits/comments/1gbc38v/ptsd_claim_due_to_mst/",
    "Had my first C&P exam regarding my PTSD caused by MST. I completely broke down during the exam. Doctor terminated it early - enough supporting documents.",
    33, "2024-10-24", "VeteransBenefits"
))

posts["veteranwomen"].append(make_post(
    "MST claim without have reported",
    "Expensive-Manager945",
    "https://www.reddit.com/r/VeteransBenefits/comments/1cjndqo/mst_claim_without_have_reported/",
    "My husband was SA'ed while AD in the barracks. Staff told him no one will believe him and 'men don't get SA'ed.'",
    46, "2024-05-04", "VeteransBenefits"
))

posts["veteranwomen"].append(make_post(
    "Do MST claims really take over a year?",
    "LeoraKitty78",
    "https://www.reddit.com/r/VeteransBenefits/comments/1izykmq/do_mst_claims_really_take_over_a_year/",
    "ITF in Nov 2024. Primary PTSD due to MST. Hearing MST claims take at least a year, might get worse with federal layoffs.",
    5, "2025-02-28", "VeteransBenefits"
))

posts["veteranwomen"].append(make_post(
    "VA rejects more PTSD claims linked to sexual trauma",
    "[deleted]",
    "https://www.reddit.com/r/VeteransBenefits/comments/198watb/va_rejects_more_ptsd_claims_linked_to_sexual/",
    "VA rejects more PTSD claims linked to sexual trauma than any other type.",
    127, "2024-01-17", "VeteransBenefits",
    [make_comment("LastOneSergeant", "Combat is well documented. MST events may have been told to no one.", 113)]
))

posts["veteranwomen"].append(make_post(
    "How much disability does MST get someone?",
    "Aggravating-Team-672",
    "https://www.reddit.com/r/VeteransBenefits/comments/1no4hpx/how_much_disability_does_mst_get_someone/",
    "Had a very bad MST case. Reported it. I've gone to BH for the mental trauma. It has ruined my military career and made me very depressed and suicidal.",
    0, "2025-12-01", "VeteransBenefits"
))

posts["veteranwomen"].append(make_post(
    "MST after 40 years Is it possible?",
    "Souless_damage",
    "https://www.reddit.com/r/VeteransBenefits/comments/1j7n6bt/mst_after_40_years_is_it_possible/",
    "I have an enormous amount of PTSD I'm dealing with from MST that occurred 40 years ago.",
    26, "2025-03-10", "VeteransBenefits"
))

# Write JSON files
output_dir = "C:/Users/ccdmn/code/bvaapi/reddit-data"

for sub, filename in [
    ("veteransbenefits", "posts_veteransbenefits.json"),
    ("veterans", "posts_veterans.json"),
    ("veteranwomen", "posts_veteranwomen.json"),
    ("military", "posts_military.json"),
    ("militaryfinance", "posts_militaryfinance.json"),
    ("vaclaims", "posts_vaclaims.json"),
    ("veteransaffairs", "posts_veteransaffairs.json"),
]:
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(posts[sub], f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(posts[sub])} posts to {filename}")

total = sum(len(v) for v in posts.values())
print(f"\nTotal posts collected: {total}")
