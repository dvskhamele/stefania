from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os




def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    #for file in os.listdir('C:/Users/aman/chatbot/english/'):
      #convData = open(r'C:/Users/aman/chatbot/english/' + file,encoding='latin-1').readlines()
       #chatbot.set_trainer(ListTrainer)
       #chatbot.train(convData)
       #print("Training completed")
    
    return chatbot

def trainit(bot1):

    bot1.train([
       """difference amount""",
       """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
       """Why is your premium higher?""",
       """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
       """why are you charging such a high""",
       """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
       """compared to others""",
       """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
       """too price""",
       """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])


    bot1.train([
       """too pricy""",
       """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])


    bot1.train([
   """Why are you charging so much?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why is amount so high?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why so expensive?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why there is so much difference in the price?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why is your price more than others?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why is Lombard’s price more than Tata AIG?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why is your price more than HDFC Ergo?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
        ])

    bot1.train([
   """Why Lombard’s price is more than IFFCO-TOKIO?  (List of all competitors to train the bot for similar questions: https://www.policybazaar.com/insurance-companies/general-insurance/)?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Premium is higher?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why is your price more than""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])


    bot1.train([
   """Price is steep?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """You are charging more""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """You are expensive""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """There is a price difference""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Your cost is more""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Amount is higher""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why is amount higher?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why do you charge more?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why am I paying more?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why am I being charged more?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why your price is so high?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """You are expensive!""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Your price is more than Tata AIG [factor for all competitors from the link]Your price is more than Tata AIG [factor for all competitors from the link]Your price is more than Tata AIG [factor for all competitors from the link]Your price is more than Tata AIG [factor for all competitors from the link]Your price is more than Tata AIG [factor for all competitors from the link]""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Why should I pay more?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """You are charging 300 rupees more""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """You are charging XXX more [XXX can be any amount/numbers]""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Your price is XXX more""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """There is a difference of XXX amount""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Price is high""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Premium is expensive""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Premium amount is more than <Competitor>""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Premium amount is more""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Premium is more""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Premium is different""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Premium is pricey""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Premium is costly""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Premium is too high""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Premium is not good, give me discount""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """Reduce premium amount""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """How can you charge so much?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """How come your price is high?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
   """How can you charge more than <competitor>?""",
   """We provide best in class service with dedicated customer care. Our satisfied customers vouch for us and that is why we invest highly in better service which sometimes makes our premium amount slightly higher than others.""",
    ])

    bot1.train([
"oh thats great",
"thankyou :)",
    ])

    bot1.train([
"show garage partners",
"garage",
    ])


    bot1.train([
"some garage partners",
"garage",
])


    bot1.train([
"garage partners",
"garage",
])






    bot1.train([
"book appointment with garage partner",
"""garage""",
])



    bot1.train([
"appointment with garage partner",
"""garage""",
])



    bot1.train([
"book appointment with garage",
"""garage""",
])



    bot1.train([
"appointment garage",
"""garage""",
])



    bot1.train([
"book garage partner",
"garage",
])







    bot1.train([
"I want to login",
"LogInAccount",
])


    bot1.train([
"login",
"LogInAccount",
])


    bot1.train([
"login into account",
"LogInAccount",
])


    bot1.train([
"account login",
"LogInAccount",
])


    bot1.train([
"forget password",
"Kindly provide your Mobile Number to receive OTP for one time sign in. You can then change your password using this OTP.",
])

    bot1.train([
"i forget my password",
"Kindly provide your Mobile Number to receive OTP for one time sign in. You can then change your password using this OTP.",
])


    bot1.train([
"reset password",
"Kindly provide your Mobile Number to receive OTP for one time sign in. You can then change your password using this OTP.",
])


    bot1.train([
"I want to reset password",
"Kindly provide your Mobile Number to receive OTP for one time sign in. You can then change your password using this OTP.",
])
  

    bot1.train([
"can you reset my password",
"Kindly provide your Mobile Number to receive OTP for one time sign in. You can then change your password using this OTP.",
])

    bot1.train([
"I want to check status of ticket number: 1234567",
"It is under processing",
])


    bot1.train([
"status of ticket number 1234567",
"It is under processing",
])


    bot1.train([
"ticket number: 1234567",
"It is under processing",
])


    bot1.train([
"1234567",
"It is under processing",
])



    bot1.train([
"I want to file a claim",
"FileClaim",
])



    bot1.train([
"I want to file a claim",
"FileClaim",
])


    bot1.train([
"file a claim",
"FileClaim",
])




    bot1.train([
"Who developed you?",
"TheFinansol, it develops end to end similar chatbot solutions like me, You can reach out to them at info@thefinansol.com",
])



    bot1.train([
"change nominee",
"Nominee",
])


    bot1.train([
"I Want to change nominee",
"Nominee",
])


    bot1.train([
"Want to change my nominee",
"Nominee",
])





    bot1.train([
"I Want to change contact details",
"ContactDetails",
])


    bot1.train([
"Want change my contact details",
"ContactDetails",
])

    bot1.train([
"change contact",
"ContactDetails",
])



    bot1.train([
"change number",
"ContactDetails",
])



    bot1.train([
"change address",
"ContactDetails",
])





    bot1.train([
"I Want to change number",
"ContactDetails",
])


    bot1.train([
"Want change my mobile number",
"ContactDetails",
])





    bot1.train([
"I Want to change address",
"ContactDetails",
])


    bot1.train([
"Want change my address",
"ContactDetails",
])



    bot1.train([
"who creat you",
"TheFinansol, You can reach out to them at info@thefinansol.com",
])


    bot1.train([
"Who is your boss?",
"ICICI Lombard :)",
])


    bot1.train([
"create Two wheeler proposal",
"policyForm",
])


    bot1.train([
"feedback",
"feedback",
])


    bot1.train([
"I want to give feedback",
"feedback",
])


    bot1.train([
"I want to give Suggession",
"feedback",
])

    bot1.train([
"want to give Suggession",
"feedback",
])


    bot1.train([
"I want give Suggession",
"feedback",
])

    bot1.train([
"I want give feedback",
"feedback",
])

    bot1.train([
"I  give feedback",
"feedback",
])


    bot1.train([
"I  give Suggession",
"feedback",
])
    bot1.train([
"I want buy insurance policy",
"policyForm",
])


    bot1.train([
"buy policy",
"policyForm",
])

    bot1.train([
"I want to buy two wheeler insurance policy?",
"policyForm",
])


    bot1.train([
"branche nearest",
"mapCase",
])

    bot1.train([
"nearest branche",
"mapCase",
])

    bot1.train([
"nearest branch location",
"mapCase",
])


    bot1.train([
"garage nearest",
"garageCase",
])


    bot1.train([
"nearest garage location",
"garageCase",
])

    bot1.train([
"garage nearest me",
"garageCase",
])


    bot1.train([
"find garages near me",
"garageCase",
])




    bot1.train([
"find branches near me",
"mapCase",
])


    bot1.train([
"nearest garage",
"garageCase",
])


    bot1.train([
"recommend IDV",
"What IDV you looking for? (High or Low)",
])

    bot1.train([
"I am looking for High IDV",
"What cover you looking for? (+1 or -1)",
])

    bot1.train([
"I am looking for Low IDV",
"What cover you looking for?",
])

    bot1.train([
"I am looking for +1 cover",
"What features are you looking for? A) Natural Calamity Cover B) 3rd Party C) Zero Dep D) Man-Made Calamity",
])

    bot1.train([
"I am looking for -1 cover",
"What features are you looking for? A) Natural Calamity Cover B) 3rd Party C) Zero Dep D) Man-Made Calamity",
])


    bot1.train([
"A) Natural Calamity Cover",
"Product A",
])

    bot1.train([
"B) 3rd Party",
"Product B",
])

    bot1.train([
"C) Zero Dep",
"Product C",
])

    bot1.train([
"D) Man-Made Calamity",
"Product D",
])


    
    bot1.train([
"Hey",
"Hello",
])
    
    bot1.train([
"Who are you",
"Hi, I am ILVA (ICICI Lombard’s Virtual Assistant). How can I help you?",
])
    
    bot1.train([
"What do you do",
"I can help you by answering frequently asked questions (FAQs) and assisting you in buying/renewing policy",
])

    bot1.train([
"hello",
"hello",
])
  
    bot1.train([
"What are your features",
"I can help you by: answering FAQs and assisting you in buying 2 wheeler insurance policy",
])

    bot1.train([
"How can you help me",
"I can help you by: answering FAQs and assisting you in buying 2 wheeler insurance policy",
])

    bot1.train([
"How can you assist me?",
"I can help you by: answering FAQs and assisting you in buying 2 wheeler insurance policy",
])

    bot1.train([
"What can you do for me",
"I can help you by: answering FAQs and assisting you in buying 2 wheeler insurance policy",
])

    bot1.train([
"Can you help me",
"I can help you by: answering FAQs and assisting you in buying 2 wheeler insurance policy",
])

    bot1.train([
"what is chatbot",
"A bot is computer program that simulates human conversation with the help of AI",
])

    bot1.train([
"what is bot",
"A bot is computer program that simulates human conversation with the help of AI",
])

    bot1.train([
"Are you bot",
"Yes, I am a chatbot",
])

    bot1.train([
"How are you?",
"I am fine thank you:), How can I help you?",




])


    bot1.train([
"How are you different than human?",
"I am an artificially intelligent entity, I do not eat, sleep, breathe or rest",
])
    
    bot1.train([
"How old are you",
"I am still an infant",
])
    
    bot1.train([
"Wil yu marry me",
"Sorry, I already have a boyfriend",
])

    
    bot1.train([
"Where you work",
"ICICI Lombard",
])

    
    bot1.train([
"Where are you from",
"I am from the realm of Artificial Intelligence",
])


    
    bot1.train([
"Where do you live",
"I am from the realm of Artificial Intelligence",
])
    
    bot1.train([
"Ae yu sure",
"Yes!",
])

    
    bot1.train([
"Ae you there?",
"Always",
])

    
    bot1.train([
"Thank you!",
"My pleasure",
])

    
    bot1.train([
"thanks",
"My pleasure",
])

    
    bot1.train([
"tnx",
"My pleasure",
])

    
    bot1.train([
"tenks",
"My pleasure",
])

    
    bot1.train([
"Ha ha ha ha",
"Hehe",
])

    
    bot1.train([
"Bye",
"Bye, take care",
])

    
    bot1.train([
"goodbye",
"Bye, take care",
])

    
    bot1.train([
"bye bye",
"Bye, take care",
])
    
    bot1.train([
"bie",
"Bye, take care",
])
    
    bot1.train([
"Nice to talk to you",
"Pleasure is mine",
])

    
    bot1.train([
"nice talking to you",
"Pleasure is mine",
])


    bot1.train([
"How are you different from human?",
"I am an artificially intelligent entity, I do not eat, sleep, breathe or rest",
])

    bot1.train([
"Are you a chatbot?",
"Yes, I am a chatbot",
])

    bot1.train([
"You are a chatbot",
"Yes, I am a chatbot",
])

    bot1.train([
"Are you human",
"No, I am a chatbot",
])

    bot1.train([
"Heyz",
"Hello",
])


    bot1.train([
"""What is rsa Road Side Assistance 
""",

"""
Road Side Assistance is a service that provides you with the necessary help in case you are stranded on the road when your car breaks down. For example, breakdown cover may include jump starting an automobile, towing a vehicle, helping to change a flat tyre, providing a small amount of fuel when a vehicle runs out of it, or helping people who are locked out of their cars, etc.

""",

])

    bot1.train([
"""What is rsa""",

"""
Road Side Assistance is a service that provides you with the necessary help in case you are stranded on the road when your car breaks down. For example, breakdown cover may include jump starting an automobile, towing a vehicle, helping to change a flat tyre, providing a small amount of fuel when a vehicle runs out of it, or helping people who are locked out of their cars, etc.

""",

])

    bot1.train([
"""rsa""",

"""
Road Side Assistance is a service that provides you with the necessary help in case you are stranded on the road when your car breaks down. For example, breakdown cover may include jump starting an automobile, towing a vehicle, helping to change a flat tyre, providing a small amount of fuel when a vehicle runs out of it, or helping people who are locked out of their cars, etc.

""",

])





    bot1.train([
"Hi",
"Hii, How can I help you?",
])





    bot1.train([
"hello",
"Hii, How can I help you?",
])









    bot1.train([
"""Which are the services provided by ICICI Lombard under RSA Road Side Assistance 
""",

"""
• Breakdown support over phone
• Minor Repairs
• Flat Tyre 
• Battery jump start
• Arrangement of keys
• Towing on breakdown/accident
• Arrangement of rental vehicle
• Arrangement/ Supply of fuel
• Arrangement of Accommodation
• Message Relay

Note: For details kindly refer Policy wordings from Web site for private car package policy.
*For list of services applicable in a policy, please refer policy schedule.

""",])



    bot1.train([
"""Which are the services under RSA Road Side Assistance 
""",

"""
• Breakdown support over phone
• Minor Repairs
• Flat Tyre 
• Battery jump start
• Arrangement of keys
• Towing on breakdown/accident
• Arrangement of rental vehicle
• Arrangement/ Supply of fuel
• Arrangement of Accommodation
• Message Relay

Note: For details kindly refer Policy wordings from Web site for private car package policy.
*For list of services applicable in a policy, please refer policy schedule.

""",])

    bot1.train([
       """Which are the services provided by ICICI Lombard under RSA 
       """,

       """
        • Breakdown support over phone
        • Minor Repairs
        • Flat Tyre 
        • Battery jump start
        • Arrangement of keys
        • Towing on breakdown/accident
        • Arrangement of rental vehicle
        • Arrangement/ Supply of fuel
        • Arrangement of Accommodation
        • Message Relay
    
        Note: For details kindly refer Policy wordings from Web site for private car package policy.
        *For list of services applicable in a policy, please refer policy schedule.
    
       """, ])



    bot1.train([
       """Which are the services provided by under RSA 
       """,

       """
        • Breakdown support over phone
        • Minor Repairs
        • Flat Tyre 
        • Battery jump start
        • Arrangement of keys
        • Towing on breakdown/accident
        • Arrangement of rental vehicle
        • Arrangement/ Supply of fuel
        • Arrangement of Accommodation
        • Message Relay
    
        Note: For details kindly refer Policy wordings from Web site for private car package policy.
        *For list of services applicable in a policy, please refer policy schedule.
    
       """, ])



    bot1.train([
"""Which are the services provided by ICICI Lombard under Road Side Assistance 
""",

"""
• Breakdown support over phone
• Minor Repairs
• Flat Tyre 
• Battery jump start
• Arrangement of keys
• Towing on breakdown/accident
• Arrangement of rental vehicle
• Arrangement/ Supply of fuel
• Arrangement of Accommodation
• Message Relay

Note: For details kindly refer Policy wordings from Web site for private car package policy.
*For list of services applicable in a policy, please refer policy schedule.

""",])

    bot1.train([
"""services provided Under under RSA Road Side Assistance 
""",

"""
• Breakdown support over phone
• Minor Repairs
• Flat Tyre 
• Battery jump start
• Arrangement of keys
• Towing on breakdown/accident
• Arrangement of rental vehicle
• Arrangement/ Supply of fuel
• Arrangement of Accommodation
• Message Relay

Note: For details kindly refer Policy wordings from Web site for private car package policy.
*For list of services applicable in a policy, please refer policy schedule.

""",

])
    
    bot1.train([
"""services provided Under under Road Side Assistance 
""",

"""
• Breakdown support over phone
• Minor Repairs
• Flat Tyre 
• Battery jump start
• Arrangement of keys
• Towing on breakdown/accident
• Arrangement of rental vehicle
• Arrangement/ Supply of fuel
• Arrangement of Accommodation
• Message Relay

Note: For details kindly refer Policy wordings from Web site for private car package policy.
*For list of services applicable in a policy, please refer policy schedule.

""",

])
    
    bot1.train([
"""services provided Under under rsa 
""",

"""
• Breakdown support over phone
• Minor Repairs
• Flat Tyre 
• Battery jump start
• Arrangement of keys
• Towing on breakdown/accident
• Arrangement of rental vehicle
• Arrangement/ Supply of fuel
• Arrangement of Accommodation
• Message Relay

Note: For details kindly refer Policy wordings from Web site for private car package policy.
*For list of services applicable in a policy, please refer policy schedule.

""",

])
    bot1.train([
"""what is meaning of insurance
""",

"""
Insurance is a protection against the financial loss arising on the happening of an unexpected event. A person can avail this protection by paying a premium to an insurance company.

""",
])
    bot1.train([
"""what meaning insurance
""",

"""
Insurance is a protection against the financial loss arising on the happening of an unexpected event. A person can avail this protection by paying a premium to an insurance company.

""",

])

    bot1.train([
"""What is Insurance policies period of General 
""",

"""
Typically, General Insurance contracts are for a one-year period only.

""",
])
    
    bot1.train([
"""period General Insurance policies
""",

"""
Typically, General Insurance contracts are for a one-year period only.

""",
])

    bot1.train([
"""call back me
""",

"""
showing_calendar

""",
])
    
    bot1.train([
"""book an call back
""",

"""
showing_calendar

""",
])
    
    bot1.train([
"""appointment
""",

"""garage""",
])
    
    bot1.train([
"""I want to book an appointment
""",

"""garage""",
])
    
    bot1.train([
"""Insurance policies period General  
""",

"""
Typically, General Insurance contracts are for a one-year period only.

""",
])

    bot1.train([
"""What the period of Insurance policies
""",

"""
Typically, General Insurance contracts are for a one-year period only.

""",
])
 
    bot1.train([
"""What are the benefits of buying Motor Insurance online
""",

"""
When you buy Motor Insurance online, you get an instant policy, as there is no documentation or paperwork involved. In addition, you have the advantage of choosing from multiple payment options e.g. Credit Card (Visa, Master Amex card), Net banking, Debit Card etc.

""",
])

    bot1.train([
"""benefits Motor Insurance 
""",

"""
When you buy Motor Insurance online, you get an instant policy, as there is no documentation or paperwork involved. In addition, you have the advantage of choosing from multiple payment options e.g. Credit Card (Visa, Master Amex card), Net banking, Debit Card etc.

""",
])

    bot1.train([
"""What are the various types of vehicle that I can insure online
""",

"""
Currently only Private Car and Two-wheeler can be insured online.

""",
])
    bot1.train([
"""Why need insure my vehicle
""",

"""
Your vehicle is probably one of the most expensive things you own. Insurance protects this asset and helps you cope with the financial loss caused by accidents, damage or theft. Another reason is that while driving, you are responsible for the safety of:
• Your passengers
• Your fellow drivers
• Other people's property
• Pedestrians
• Yourself
Insurance helps cover the costs of potential damages or injuries in case of an unforeseen accident or theft. Above all, in India it is mandatory to have at least a Third Party Motor Insurance before you can drive on the roads.

""",
])
    bot1.train([
"""Why need insure
""",

"""
Your vehicle is probably one of the most expensive things you own. Insurance protects this asset and helps you cope with the financial loss caused by accidents, damage or theft. Another reason is that while driving, you are responsible for the safety of:
• Your passengers
• Your fellow drivers
• Other people's property
• Pedestrians
• Yourself
Insurance helps cover the costs of potential damages or injuries in case of an unforeseen accident or theft. Above all, in India it is mandatory to have at least a Third Party Motor Insurance before you can drive on the roads.

""",
])


    bot1.train([

"""What is No Claim Bonus NCB
""",

"""NCBDEFINE""",
])

    bot1.train([

"""ncb 
""",

"""NCBDEFINE""",
])

    
    bot1.train([

"""what is ncb 
""",

"""NCBDEFINE""",
])

    
    bot1.train([

"""what ncb no claim bonus is
""",

"""
NCBDEFINE""",
])


    bot1.train([

"""Is my NCB  No Claim Bonus transferable 
""",

"""
Yes, in case you are the customer of ICICI Lombard, or are switching/changing to ICICI Lombard from any other insurance company, and have accrued some NCB from your previous insurer, you can get the same transferred provided the vehicle is insured within 90 days of your renewal due date. The same applies if you switch/change from ICICI Lombard to other insurance company

""",
])


    bot1.train([

"""can ncb transferable    
""",

"""
Yes, in case you are the customer of ICICI Lombard, or are switching/changing to ICICI Lombard from any other insurance company, and have accrued some NCB from your previous insurer, you can get the same transferred provided the vehicle is insured within 90 days of your renewal due date. The same applies if you switch/change from ICICI Lombard to other insurance company

""",
])
    bot1.train([

"""can ncb transferable    
""",

"""
Yes, in case you are the customer of ICICI Lombard, or are switching/changing to ICICI Lombard from any other insurance company, and have accrued some NCB from your previous insurer, you can get the same transferred provided the vehicle is insured within 90 days of your renewal due date. The same applies if you switch/change from ICICI Lombard to other insurance company

""",
])



    bot1.train([

"""is No Claim Bonus transferable   
""",

"""
Yes, in case you are the customer of ICICI Lombard, or are switching/changing to ICICI Lombard from any other insurance company, and have accrued some NCB from your previous insurer, you can get the same transferred provided the vehicle is insured within 90 days of your renewal due date. The same applies if you switch/change from ICICI Lombard to other insurance company

""",
])


    bot1.train([
"""What is the rate at which NCB is transferred from my previous insurance company to ICICI Lombard
""",

"""
The NCB will be transferred to ICICI Lombard motor policy at the same rate that you are entitled to get from the previous insurance company on renewal of your policy. The NCB will be available, provided you show evidence that you are entitled to No Claim Bonus from your previous insurance company. Evidence can be in form of:

• A renewal notice or
• A letter confirming the NCB entitlement from the previous insurer or
• A written declaration (kindly note that in case of a false declaration, the policy will be subject to cancellation)

Click here to view the wordings of the written declaration

""",
])

    bot1.train([
"""rate NCB is transferred from my previous insurance company to ICICI Lombard
""",

"""
The NCB will be transferred to ICICI Lombard motor policy at the same rate that you are entitled to get from the previous insurance company on renewal of your policy. The NCB will be available, provided you show evidence that you are entitled to No Claim Bonus from your previous insurance company. Evidence can be in form of:

• A renewal notice or
• A letter confirming the NCB entitlement from the previous insurer or
• A written declaration (kindly note that in case of a false declaration, the policy will be subject to cancellation)

Click here to view the wordings of the written declaration

""",
])


    bot1.train([
"""rate NCB is transferred from my previous insurance company 
""",

"""
The NCB will be transferred to ICICI Lombard motor policy at the same rate that you are entitled to get from the previous insurance company on renewal of your policy. The NCB will be available, provided you show evidence that you are entitled to No Claim Bonus from your previous insurance company. Evidence can be in form of:

• A renewal notice or
• A letter confirming the NCB entitlement from the previous insurer or
• A written declaration (kindly note that in case of a false declaration, the policy will be subject to cancellation)

Click here to view the wordings of the written declaration

""",
])

    bot1.train([
"""rate NCB transfer ICICI Lombard
""",

"""
The NCB will be transferred to ICICI Lombard motor policy at the same rate that you are entitled to get from the previous insurance company on renewal of your policy. The NCB will be available, provided you show evidence that you are entitled to No Claim Bonus from your previous insurance company. Evidence can be in form of:

• A renewal notice or
• A letter confirming the NCB entitlement from the previous insurer or
• A written declaration (kindly note that in case of a false declaration, the policy will be subject to cancellation)

Click here to view the wordings of the written declaration

""",
])

    bot1.train([

"""Can I renew Two-wheeler insurance policy online
""",

"""
yes, you can renew your Two-wheeler insurance policy online, starting 60 days before the expiry of your existing policy.

""",
])

    bot1.train([

"""Two-wheeler policy renew insurance  online
""",

"""
yes, you can renew your Two-wheeler insurance policy online, starting 60 days before the expiry of your existing policy.

""",
])
    bot1.train([

"""2 wheeler policy insurance renew online
""",

"""
yes, you can renew your Two-wheeler insurance policy online, starting 60 days before the expiry of your existing policy.

""",
])

    bot1.train([

"""renew 2 wheeler policy insurance online
""",

"""
yes, you can renew your Two-wheeler insurance policy online, starting 60 days before the expiry of your existing policy.

""",
])


    bot1.train([
"""What is the penalty that I may have to incur in case my two-wheeler is uninsured
""",

"""
As per section 197 of motor vehicle act 1988, driving without insurance will lead to a fine of up to ` 1000 or imprisonment for up to 3 months or both.

""",
])
    bot1.train([
"""penalty if 2 two wheeler uninsured
""",

"""
As per section 197 of motor vehicle act 1988, driving without insurance will lead to a fine of up to ` 1000 or imprisonment for up to 3 months or both.

""",
])


    bot1.train([

"""Is it mandatory to insure my Two-wheeler as per law
""",

"""
Under the Motor Vehicle Act, third party insurance is mandatory for every vehicle on the road. Third Party Liability covers:
• Legal liability due to permanent injury and/or death of a third party
• Legal liability due to damage to a third party’s property

""",
])

    bot1.train([
"""What is LTTW
""",

"""
The Insurance Regulatory and Development Authority of India (IRDAI) has introduced a long-term insurance policy for two wheelers.
This means that you don’t have to renew your policy every year. Instead, you can opt for an insurance policy that is valid for three years. What’s more, by opting for long term insurance, you are immune to the revision of Third Party Rates every year, resulting in significant savings.

""",
])

    bot1.train([
   """What is Long Term Two-wheeler Insurance
   """,

   """
    The Insurance Regulatory and Development Authority of India (IRDAI) has introduced a long-term insurance policy for two wheelers.
    This means that you don’t have to renew your policy every year. Instead, you can opt for an insurance policy that is valid for three years. What’s more, by opting for long term insurance, you are immune to the revision of Third Party Rates every year, resulting in significant savings.

   """,
])

    bot1.train([
"""What benefits of a Long Term Two-wheeler Insurance
""",

"""benefitsoflongterm 1""",
])

    bot1.train([
   """What benefits of LTTW
   """,

   """benefitsoflongterm 1""",
])

    bot1.train([
""" Long Term Two-wheeler Insurance benefits
""",

"""benefitsoflongterm 1""",
])


    bot1.train([
""" LTTW Insurance benefits
""",

"""benefitsoflongterm 1""",
])



    bot1.train([
"""documents require transfer my NCB
""",

"""
A No Claim Bonus can be availed, provided you show evidence that you are entitled to a No Claim Bonus from your previous insurance company. Evidence can be in the form of:

•   A renewal notice or
•   A letter confirming the NCB entitlement from the previous insurer or

A written declaration (kindly note that in case of a false declaration, the policy will be subject to cancellation)
""",
])
    bot1.train([
"""documents NCB transfer will require to  my 
""",

"""
A No Claim Bonus can be availed, provided you show evidence that you are entitled to a No Claim Bonus from your previous insurance company. Evidence can be in the form of:

•   A renewal notice or
•   A letter confirming the NCB entitlement from the previous insurer or

A written declaration (kindly note that in case of a false declaration, the policy will be subject to cancellation)
""",
])


    bot1.train([ 
   """What NCB No Claim Bonus """,

"""
NCB is a reward for not raising a claim. It is a discount on the premium of the Own Damage (OD) portion of your vehicle when you renew your policy, provided you have not made any claim during the last policy period of one year. The NCB can be accumulated up to a maximum limit of 50% on OD premium.
As for Long Term Two Wheeler Policy holders.

""",
])

    bot1.train([
   """NCB Benefits for 3 Years No Claim Bonus .""",
"""$$--  No Claim During Policy Tenure - 40% NCB.

    $$--  One Claim During Policy Tenure - 30% NCB.

    $$--  Two Claims During Policy Tenure - 20% NCB.

""",
])
    bot1.train([
   """NCB Benefits for 3 Years .""",
"""$$--  No Claim During Policy Tenure - 40% NCB.

    $$--  One Claim During Policy Tenure - 30% NCB.

    $$--  Two Claims During Policy Tenure - 20% NCB.

""",
])


    bot1.train([

"""What is Compulsory and Voluntary Deductible?""",

"""
Compulsory deductible means the amount that you will bear in case of a claim. Two-wheeler Insurance policies carry a Compulsory Deductible of ` 100.
Voluntary deductible is the amount you opt for as a higher deductible over and above the compulsive deductible in the event of the claim. (Final Claim amount will be after deduction of depreciation on parts, VD and compulsory deductible as per IMT)
""",
])

    bot1.train([

"""What is Compulsory duductible""",

"""
Compulsory deductible means the amount that you will bear in case of a claim. Two-wheeler Insurance policies carry a Compulsory Deductible of ` 100.

""",
])

    bot1.train([

   """What is Voluntary duductible""",

   """
Voluntary deductible is the amount you opt for as a higher deductible over and above the compulsive deductible in the event of the claim. (Final Claim amount will be after deduction of depreciation on parts, VD and compulsory deductible as per IMT)
   """,
])


    bot1.train([
"""What are the events covered in ICICI Lombard Motor Insurance policy
""",

"""
The ICICI Lombard Motor Insurance policy is a comprehensive vehicle insurance cover, which offers you:

• Any Loss or damage to your vehicle
• Third Party Liability
• Any permanent injury / death to a person caused by your insured vehicle
• Any damage caused to the property other than property belonging to the insured or held in trust or in custody or control of insured by your vehicle
• A Personal Accident Cover for the owner-driver of the vehicle while he is driving

In case of loss or damage to the vehicle or the accessories insured, the Company covers the insured if the accident occurs due to the following hazards:

• Fire, explosion, self ignition or lightning
• Burglary, housebreaking or theft
• Riot and strike
• Earthquake (fire and shock damage)
• Flood, typhoon, hurricane, storm, tempest, inundation, cyclone, hailstorm, frost
• Accident by external means
• Malicious act
• Terrorist activity
• Whilst in transit by road, rail, inland-waterway, lift, elevator or air
• Landslide and rockslide


""",
])




    bot1.train([
"""What are the events covered in Motor Insurance policy
""",

"""
The ICICI Lombard Motor Insurance policy is a comprehensive vehicle insurance cover, which offers you:

• Any Loss or damage to your vehicle
• Third Party Liability
• Any permanent injury / death to a person caused by your insured vehicle
• Any damage caused to the property other than property belonging to the insured or held in trust or in custody or control of insured by your vehicle
• A Personal Accident Cover for the owner-driver of the vehicle while he is driving

In case of loss or damage to the vehicle or the accessories insured, the Company covers the insured if the accident occurs due to the following hazards:

• Fire, explosion, self ignition or lightning
• Burglary, housebreaking or theft
• Riot and strike
• Earthquake (fire and shock damage)
• Flood, typhoon, hurricane, storm, tempest, inundation, cyclone, hailstorm, frost
• Accident by external means
• Malicious act
• Terrorist activity
• Whilst in transit by road, rail, inland-waterway, lift, elevator or air
• Landslide and rockslide


""",
])


    bot1.train([
"""What are the types of events or losses not covered under this policy
""",

"""
The following events or losses are not covered in this policy:
• Mechanical/ Electrical breakdown
• Wear and tear, ageing of vehicle
• Consequential loss*
• Depreciation
• Deliberate accidental loss
• Intoxicated driving
• Any contractual liability
• Damage to/ by a person driving any vehicles or cars without a valid license

* Consequential loss is an indirect loss, which is not directly resulting out of a loss event, but arising as a consequence of loss event. For example, Mr. Singh was on his way to office for an important meeting with client. Unfortunately, his vehicle met with a road accident resulting in damages to vehicle and it consumed lot of his time. Due to this, he could not attend the meeting resulting in loss of approx `15 Lakhs. Damages to vehicle due to the accident are covered however, but the loss of `15 Lakhs is consequential and hence not covered.

For details, kindly refer to the Two-wheeler Policy Wordings.

""",
])
    bot1.train([
"""What is Third Party Liability cover
 Is it covered
""",

"""
Third Party Liability insurance covers losses to a third person who is not a party to the insurance contract. The Motor Third Party insurance covers the following losses:

• Any permanent injury / death to a person caused by your insured vehicle
• Any damage caused to the property (excluding vehicle) of some other individual by your insured vehicle

Liability is covered for an unlimited amount in respect of death or injury. Any damage to third party property is covered up to `7.5 Lakhs in case of Private Car and `1 Lakh in case of Two-wheeler.
""",
])
    bot1.train([
"""What is Personal Accident Insurance cover
""",

"""
Personal Accident Insurance covers death or disability caused due an unfortunate accident. The motor insurance policy essentially has a Personal Accident cover for the owner-driver, as per tariff, for which no extra premium is to be paid. For a person other than the owner and driver, the Personal Accident cover has to be purchased separately by paying an additional premium. The amount paid as compensation depends upon the extent of cover opted for.

""",
])

    bot1.train([

"""Will I get a Personal Accident cover if the vehicle is registered under someone else's name, but is driven by me and the premium is also paid by me
""",

"""
The policy essentially contains a Personal accident cover for the owner-driver, as per tariff. In case of un-named driver, the personal accident cover has to be purchased separately by paying an additional premium.

""",
])

    bot1.train([

"""Will I be eligible for any discounts if I am a member of the Automobile Association of India
""",

"""
Yes, as a member of any of the following recognized Automobile Associations, a discount on Own Damage (OD) premium is given under the policy. The following Associations are recognized:

• The Automobile Association of Eastern India
• The Uttar Pradesh Automobile Association
• The Western India Automobile Association
• The Automobile Association of Southern India
• The Automobile Association of Upper India

""",
])

    bot1.train([

"""any discount if I install an Anti-theft alarm and Locking system
""",

"""
If your vehicle is fitted with anti theft devices, which are approved by the Automobile Research Association of India (ARAI), a discount on Own Damage (OD) premium is allowed.

""",
])

    bot1.train([

"""any discount if i have locking system?
""",

"""
If your vehicle is fitted with anti theft devices, which are approved by the Automobile Research Association of India (ARAI), a discount on Own Damage (OD) premium is allowed.

""",
])

    bot1.train([

"""any discount if have theft alarm?
""",

"""
If your vehicle is fitted with anti theft devices, which are approved by the Automobile Research Association of India (ARAI), a discount on Own Damage (OD) premium is allowed.

""",
])



    bot1.train([
"""What is Accident Cover for un-named passengers
""",

"""
Passengers other than the insured, including a paid driver and cleaner of the vehicle can be insured under this cover by paying an additional premium. This covers them against death or disability caused due an unfortunate accident.

""",
])
    bot1.train([

"""How is the IDV value vehicle  Insured Declare Value determined
""",

"""
The IDV of the vehicle is to be fixed based on the manufacturer's listed selling price of the brand and model, as the vehicle proposed for insurance at the commencement of insurance /renewal and adjusted for depreciation. 

The IDV of the side car(s) and/ or accessories, if any, fitted to the vehicle, but not included in the manufacturer's listed selling price of the vehicle is also likewise to be fixed. The schedule of depreciation for arriving at IDV is as below:

    Schedule Of Depreciation For Arriving At IDV
---------------------------------------------Age Of The Vehicle    -----    % Of Depreciation Fixing IDV---------------------------------------------------------
## Not exceeding 6 months   --- 5%                                                                            
## Exceeding 6 months but not exceeding 1 year ---  15%
## Exceeding 1 year but not exceeding 2 years   --- 20%
## Exceeding 2 years but not exceeding 3 years ---  30%
## Exceeding 3 years but not exceeding 4 years  --- 40%
## Exceeding 4 years but not exceeding 5 years  --- 50%



""", ])


    bot1.train([

"""How is the IDV value of vehicle determined
""",

"""
The IDV of the vehicle is to be fixed based on the manufacturer's listed selling price of the brand and model, as the vehicle proposed for insurance at the commencement of insurance /renewal and adjusted for depreciation. 

The IDV of the side car(s) and/ or accessories, if any, fitted to the vehicle, but not included in the manufacturer's listed selling price of the vehicle is also likewise to be fixed. The schedule of depreciation for arriving at IDV is as below:

    Schedule Of Depreciation For Arriving At IDV
---------------------------------------------Age Of The Vehicle    -----    % Of Depreciation Fixing IDV---------------------------------------------------------
## Not exceeding 6 months   --- 5%                                                                            
## Exceeding 6 months but not exceeding 1 year ---  15%
## Exceeding 1 year but not exceeding 2 years   --- 20%
## Exceeding 2 years but not exceeding 3 years ---  30%
## Exceeding 3 years but not exceeding 4 years  --- 40%
## Exceeding 4 years but not exceeding 5 years  --- 50%



""", ])



    bot1.train([
"""What are electrical accessoris non-electrical accessories?""",

"""Electrical accessories: Any electrical and/or electronic equipment that is not factory fitted with the vehicle can be covered under electrical accessories at an additional premium of 4% on the value of such fitting. Value of electrical accessories will be as declared by the insured. For example, a Music System that is installed in the car after purchase of the vehicle can be covered.Non-electrical accessories: Any Non-electrical/ Non-electronic equipment that is not factory fitted with the vehicle can be covered under non-electrical accessories at an additional premium of invoice value*. Value of non-electrical accessories should be the Invoice value of the non-electrical accessories up to the maximum limit of ` 20,000. For example, Mag wheels and/ or leather seats that are installed in the car after purchase of the vehicle can be covered. * Own damage rate""",

])

    bot1.train([
"""If I have a LPG/ CNG kit fitted in the car that is tt endorsed in the RC, can I take a policy?
""",

"""Policy will only be issued if the LPG/ CNG kit is duly endorsed on the RC (Registration Certificate) by the concerned RTO.
""",


])

    bot1.train([
"""How to calculate the value of accessories?""",

"""Electrical accessories: Any electrical and/or electronic equipment that is not factory fitted with the vehicle can be covered under electrical accessories at an additional premium of 4% on the value of such fitting. Value of electrical accessories will be as declared by the insured. For example, a Music System that is installed in the car after purchase of the vehicle can be covered.Non-electrical accessories: Any Non-electrical/ Non-electronic equipment that is not factory fitted with the vehicle can be covered under non-electrical accessories at an additional premium of invoice value*. Value of non-electrical accessories should be the Invoice value of the non-electrical accessories up to the maximum limit of ` 20,000. For example, Mag wheels and/ or leather seats that are installed in the car after purchase of the vehicle can be covered. * Own damage rate""",

])

    bot1.train([
"""If I have a LPG/ CNG kit fitted in the car that is not endorsed in the RC, can I take a policy?
""",

"""Policy will only be issued if the LPG/ CNG kit is duly endorsed on the RC (Registration Certificate) by the concerned RTO.
""",


])



    bot1.train([
"""What is Voluntary deductible?
""",

"""voluntry""",


])

    bot1.train([
"""What is the process for obtaining Third Party only cover?
""",

"""To issue only Third Party cover, our local underwriter needs to carry out a risk assessment which cannot be done online. Thus, we request the customer to visit us at the nearest branch.
""",


])

    bot1.train([
"""Third Party only cover process  
""",

"""To issue only Third Party cover, our local underwriter needs to carry out a risk assessment which cannot be done online. Thus, we request the customer to visit us at the nearest branch.
""",


])




    bot1.train([
"""What are the events covered in the ICICI Lombard Two Wheeler policy?
""",

"""The ICICI Lombard Two Wheeler policy is a comprehensive vehicle insurance cover, which offers you cover against:
* Any Loss or damage to your vehicle
* Third Party Liability
* Any permanent injury/death to a person caused by your insured vehicle
* Any damage caused to the property other than property belonging to the insured or held in trust or in custody or control of the insured by your vehicle
* A Personal Accident Cover for the owner-driver of the vehicle while s/he is driving

In case of loss or damage to the vehicle or the accessories insured, the Company offers you a cover if the accident occurs due to the following hazards:
* Fire, explosion, self ignition or lightning
* Burglary, housebreaking or theft
* Riot and strike
* Earthquake (fire and shock damage)
* Flood, typhoon, hurricane, storm, tempest, inundation, cyclone, hailstorm, frost
* Accident by external means
* Malicious act
* Terrorist activity
""",
])




    bot1.train([
"""What are the events covered ?
""",

"""The ICICI Lombard Two Wheeler policy is a comprehensive vehicle insurance cover, which offers you cover against:
* Any Loss or damage to your vehicle
* Third Party Liability
* Any permanent injury/death to a person caused by your insured vehicle
* Any damage caused to the property other than property belonging to the insured or held in trust or in custody or control of the insured by your vehicle
* A Personal Accident Cover for the owner-driver of the vehicle while s/he is driving

In case of loss or damage to the vehicle or the accessories insured, the Company offers you a cover if the accident occurs due to the following hazards:
* Fire, explosion, self ignition or lightning
* Burglary, housebreaking or theft
* Riot and strike
* Earthquake (fire and shock damage)
* Flood, typhoon, hurricane, storm, tempest, inundation, cyclone, hailstorm, frost
* Accident by external means
* Malicious act
* Terrorist activity
""",
])

    bot1.train([
"""Whilst in transit by road, rail, inland-waterway, lift, elevator or air
""",

"""Landslide and rockslide
""",

])

    bot1.train([
"""What is the Accident Cover for un-named passengers?
""",

"""Passengers other than the insured, namely, the co-passenger/pillion rider, can be insured under this cover by paying an additional premium. This covers them against death or disability caused due an unfortunate accident.

""",


])

    bot1.train([
       """What are the factors affecting the premium amount?
       """,

       """The premium payable for your vehicle depends on the below factors:  
        * Cubic capacity of the engine 
        * Age of vehicle
        * Geographical Zone
            $ Type of Model   
            * IDV (Insured declared Value)
       """
    ])

    bot1.train([
       """What are the factors affecting premium amount?
       """,

       """The premium payable for your vehicle depends on the below factors:  
        * Cubic capacity of the engine 
        * Age of vehicle
        * Geographical Zone
            $ Type of Model   
            * IDV (Insured declared Value)
       """
    ])

    bot1.train([
       """What factors affecting premium amount?
       """,

       """The premium payable for your vehicle depends on the below factors:  
        * Cubic capacity of the engine 
        * Age of vehicle
        * Geographical Zone
            $ Type of Model   
            * IDV (Insured declared Value)
       """
    ])

    bot1.train([
       """factors premium amount?
       """,

       """The premium payable for your vehicle depends on the below factors:  
        * Cubic capacity of the engine 
        * Age of vehicle
        * Geographical Zone
            $ Type of Model   
            * IDV (Insured declared Value)
       """
    ])

    bot1.train([
   """What factors affecting the premium amount?
   """,

   """The premium payable for your vehicle depends on the below factors:  
    * Cubic capacity of the engine 
    * Age of vehicle
    * Geographical Zone
        $ Type of Model   
        * IDV (Insured declared Value)
   """
])


    bot1.train([
   """What factors affecting premium amount?
   """,

   """The premium payable for your vehicle depends on the below factors:  
    * Cubic capacity of the engine 
    * Age of vehicle
    * Geographical Zone
        $ Type of Model   
        * IDV (Insured declared Value)
   """
])


    bot1.train([
   """factors affecting premium amount?
   """,

   """The premium payable for your vehicle depends on the below factors:  
    * Cubic capacity of the engine 
    * Age of vehicle
    * Geographical Zone
        $ Type of Model   
        * IDV (Insured declared Value)
   """
])

    bot1.train([

"""What is ARAI?
""",

"""ARAI stands for Automotive Research Association of India. If you have installed an ARAI approved anti-theft device in your vehicle, whose installation is dully certified by the agency, you can get a discount of 2.5% on the OD (Own Damage) premium subject to maximum of ₹500.
""",


])

    bot1.train([
"""What are the different modes of payment on icicilombard.com?
""",

"""You can choose between 6 payment options to pay your premium online:

*Credit Card – Make secure premium payment with your VISA, Master and AMEX card. 

* Net Banking - Transfer the premium amount online through ICICI Bank and 13 other selected Banks


*Debit Card – Just enter your Citibank, HDFC Bank, ICICI Bank or any of the other 7 approved bank’s Debit Card details to pay your insurance premium directly


*Cash Card - Use your Done or ITZ Card to make the payment online


*Cheque/ Demand Draft: You can send a Cheque/ Demand Draft by courier to our office address
""",


])


    bot1.train([
"""modes of payment?
""",

"""You can choose between 6 payment options to pay your premium online:

*Credit Card – Make secure premium payment with your VISA, Master and AMEX card. 

* Net Banking - Transfer the premium amount online through ICICI Bank and 13 other selected Banks


*Debit Card – Just enter your Citibank, HDFC Bank, ICICI Bank or any of the other 7 approved bank’s Debit Card details to pay your insurance premium directly


*Cash Card - Use your Done or ITZ Card to make the payment online


*Cheque/ Demand Draft: You can send a Cheque/ Demand Draft by courier to our office address
""",


])

    bot1.train([
"""How do register my claim?
""",

"""Contact our Toll Free Helpline 1800 2666 to register your claim and get a claim number/ reference number. You can also directly register your claim online*, with our Lodge A Motor Claim service.

# # Please note that as of now, only accidental damage claims can be processed through the 'Lodge A Motor Claim' interface
""",
])

    bot1.train([
"""How file my claim
""",

"""Contact our Toll Free Helpline 1800 2666 to register your claim and get a claim number/ reference number. You can also directly register your claim online*, with our Lodge A Motor Claim service.

# # Please note that as of now, only accidental damage claims can be processed through the 'Lodge A Motor Claim' interface
""",
])



    bot1.train([
"""When should I report to the police?
""",

"""Incidents such as"Third Party Property Damage","Bodily Injury To Self or Third Party"or"Theft"should be reported to the nearest police station as early as possible, under whose jurisdiction the incident has occurred.
""",


])

    bot1.train([
"""What Cashless Claim
""",

"""Cashless Claim : In cashless claim facility, the repair charges of the vehicle are directly paid to the garage by us, provided the vehicle is repaired in our garage network.
""",
])

    bot1.train([
"""Non cashless claim   
""",

"""Non-cashless/ Reimbursement : If the vehicle is repaired in a garage outside the purview of our network, then you will be liable to pay the repair charges of the garage. You can get your claim amount reimbursed by submitting the original bills and payment receipts to our office.
""",

])

    bot1.train([
"""reimbursement claim
   
""",

"""Non-cashless/ Reimbursement : If the vehicle is repaired in a garage outside the purview of our network, then you will be liable to pay the repair charges of the garage. You can get your claim amount reimbursed by submitting the original bills and payment receipts to our office.
""",

])

    bot1.train([
"""What Cashless and non cashless claim?
""",

"""Cashless Claim : In cashless claim facility, the repair charges of the vehicle are directly paid to the garage by us, provided the vehicle is repaired in our garage network.
Non-cashless/ Reimbursement : If the vehicle is repaired in a garage outside the purview of our network, then you will be liable to pay the repair charges of the garage. You can get your claim amount reimbursed by submitting the original bills and payment receipts to our office.
""",
])


    bot1.train([
"""What is claim procedure.
""",

"""ICICI Lombard adopts the following process for settlement of claim:

## For Cashless claim settlement -

* The Customer Relationship Manager (CRM) / Surveyor attends the claim within 24 hours of registering the claim


* Insured must fill the claim form, (click here to download it or collect it from the CRM/ Surveyor/ Dealer) and submit all the required documents to the CRM/ Surveyor/ Dealer
 

* Our CRM will get the estimate for the repairs of insured vehicle and give spot approval after assessment
 
*  After the completion of repairs at our preferred garage, we will make the payment of our share of the loss directly to the garage. Any amount over and above the admissible amount will have to be directly paid by the Insured
 

* The amount of Depreciation as per the rate prescribed under the Indian Motor Tariff and Compulsory Deductions under the policy need to be borne by the Insured

## For Non-cashless/ Reimbursement claim settlement -
 

* The Customer Relationship Manager (CRM) / Surveyor attends the claim within 24 hours of registering the claim


* Insured must fill the claim form (click here to download it or collect it from CRM/ Surveyor/ Dealer) and submit all the required documents to the CRM/ Surveyor/ Dealer
 
* The CRM/ Surveyor assess the loss, estimates the repair amount and then informs the Insured on the same day of assessment. The CRM/ Surveyor will also take photographs of the damaged vehicle
 

* Insured can then get the vehicle repaired at preferred workshop/ garage. The CRM later carries out a re-inspection of the vehicle. The Insured then pays the workshop/ garage as per the CRM/ Surveyor’s assessed estimation, who thereafter releases a ‘Proof of Release’ document. (The proof of release is an authenticated document signed by the insured to release his vehicle from the garage after it is checked and repaired)
 

* Insured needs to submit the original bill, proof of release and cash receipt (derived from the garage) to the CRM/ Surveyor
 

* The CRM/ Surveyor then submits all required documents to ICICI Lombard for settlement of the claim
 

* Upon acceptance of the claim, the company issues the cheque to the Insured within seven working days from the date of receipt of all documents
 
 ## The amount of Depreciation as per the rate prescribed under the Indian Motor Tariff and Compulsory Deductions under the policy need to be borne by the Insured
""",
])

    bot1.train([
"""claim settlement procesdure.
""",

"""ICICI Lombard adopts the following process for settlement of claim:

## For Cashless claim settlement -

* The Customer Relationship Manager (CRM) / Surveyor attends the claim within 24 hours of registering the claim


* Insured must fill the claim form, (click here to download it or collect it from the CRM/ Surveyor/ Dealer) and submit all the required documents to the CRM/ Surveyor/ Dealer
 

* Our CRM will get the estimate for the repairs of insured vehicle and give spot approval after assessment
 
*  After the completion of repairs at our preferred garage, we will make the payment of our share of the loss directly to the garage. Any amount over and above the admissible amount will have to be directly paid by the Insured
 

* The amount of Depreciation as per the rate prescribed under the Indian Motor Tariff and Compulsory Deductions under the policy need to be borne by the Insured

## For Non-cashless/ Reimbursement claim settlement -
 

* The Customer Relationship Manager (CRM) / Surveyor attends the claim within 24 hours of registering the claim


* Insured must fill the claim form (click here to download it or collect it from CRM/ Surveyor/ Dealer) and submit all the required documents to the CRM/ Surveyor/ Dealer
 
* The CRM/ Surveyor assess the loss, estimates the repair amount and then informs the Insured on the same day of assessment. The CRM/ Surveyor will also take photographs of the damaged vehicle
 

* Insured can then get the vehicle repaired at preferred workshop/ garage. The CRM later carries out a re-inspection of the vehicle. The Insured then pays the workshop/ garage as per the CRM/ Surveyor’s assessed estimation, who thereafter releases a ‘Proof of Release’ document. (The proof of release is an authenticated document signed by the insured to release his vehicle from the garage after it is checked and repaired)
 

* Insured needs to submit the original bill, proof of release and cash receipt (derived from the garage) to the CRM/ Surveyor
 

* The CRM/ Surveyor then submits all required documents to ICICI Lombard for settlement of the claim
 

* Upon acceptance of the claim, the company issues the cheque to the Insured within seven working days from the date of receipt of all documents
 
 ## The amount of Depreciation as per the rate prescribed under the Indian Motor Tariff and Compulsory Deductions under the policy need to be borne by the Insured
""",
])




    bot1.train([
"""What documents are required to file a claim?
""",
"""
In case of accidental damages claim, you need to provide the following documents:
 * Claim Form duly signed

*  Valid R.C. copy of the vehicle

*  Valid driving license copy,

 * Policy copy

* FIR, if required (For Theft, Third Party Injury/ Damage; Highway accidents - Major only)


## Original repair bill, proof of release and cash receipt

* Any other document as required to investigate the Claim or Company's obligation to make payment for it

""",

])

    bot1.train([
"""
Please provide me list of garages in my city avail Cashless service?
""",

"""
Click here to search and view the list of garages in your city where you can avail Cashless service
""",


])
    bot1.train([
"""
 list garages i can avaial Cashless service
""",

"""
Click here to search and view the list of garages in your city where you can avail Cashless service
""",


])

    bot1.train([
"""
Cashless service list garages i can avaial
""",

"""
Click here to search and view the list of garages in your city where you can avail Cashless service
""",


])


    bot1.train([
"""What meaning of deductibles? What is the deductible applicable to Private Car and Two-wheeler?
""",

"""Deductible means the amount that you will bear in case of a claim. This amount is deducted from the claim amount. Car Insurance Policy carries a Compulsory Deductible of ` 1,000 (for vehicles not exceeding 1500 cc) or ` 2,000/- (for vehicles exceeding 1500 cc). Two-wheeler Insurance policies carry a Compulsory Deductible of ` 100.
""",
])

    bot1.train([
"""What meaning of deductibles?
""",

"""Deductible means the amount that you will bear in case of a claim. This amount is deducted from the claim amount. Car Insurance Policy carries a Compulsory Deductible of ` 1,000 (for vehicles not exceeding 1500 cc) or ` 2,000/- (for vehicles exceeding 1500 cc). Two-wheeler Insurance policies carry a Compulsory Deductible of ` 100.
""",


])
    bot1.train([
"""meaning of deductibles? What is the deductible applicable to Private Car and Two-wheeler?
""",

"""Deductible means the amount that you will bear in case of a claim. This amount is deducted from the claim amount. Car Insurance Policy carries a Compulsory Deductible of ` 1,000 (for vehicles not exceeding 1500 cc) or ` 2,000/- (for vehicles exceeding 1500 cc). Two-wheeler Insurance policies carry a Compulsory Deductible of ` 100.
""",


])

    bot1.train([
"""What is deductible applicable to Private Car and 2 Two wheeler?
""",

"""Deductible means the amount that you will bear in case of a claim. This amount is deducted from the claim amount. Car Insurance Policy carries a Compulsory Deductible of ` 1,000 (for vehicles not exceeding 1500 cc) or ` 2,000/- (for vehicles exceeding 1500 cc). Two-wheeler Insurance policies carry a Compulsory Deductible of ` 100.
""",


])



    bot1.train([
"""What is meant by Constructive Total Loss?
""",

"""Constructive Total Loss refers to accidental loss/ damage to your vehicle where the aggregate cost of retrieval and/ or repairs amounts to be more than 75% of the Insured's Declared Value (IDV) on your policy.
""",

])


    bot1.train([
           """Constructive Total Loss?
           """,

           """Constructive Total Loss refers to accidental loss/ damage to your vehicle where the aggregate cost of retrieval and/ or repairs amounts to be more than 75% of the Insured's Declared Value (IDV) on your policy.
           """,

        ])

    bot1.train([
"""If I lodge a claim after the expiry of my policy date for an event that occurred during the policy period, will it still be valid?
""",

"""Yes, you will be eligible for the claim even after the expiry of the policy date. This is because the event took place during the policy period.
""",

])


    bot1.train([
           """If I file a claim after the expiry of my policy date for an event that occurred during the policy period, will it still be valid?
           """,

           """Yes, you will be eligible for the claim even after the expiry of the policy date. This is because the event took place during the policy period.
           """,

        ])


    bot1.train([
           """If I report a claim after the expiry of my policy date for an event that occurred during the policy period, will it still be valid?
           """,

           """Yes, you will be eligible for the claim even after the expiry of the policy date. This is because the event took place during the policy period.
           """,

        ])

    bot1.train([
"""policy expired but event occurred during the policy period
""",

"""Yes, you will be eligible for the claim even after the expiry of the policy date. This is because the event took place during the policy period.
""",

])

    bot1.train([
"""if policy expired but the event is occurred during the policy period
""",

"""Yes, you will be eligible for the claim even after the expiry of the policy date. This is because the event took place during the policy period.
""",

])


    bot1.train([
"""What if I fail to produce the required documents?
""",

"""There are some documents that are definitely needed, without which a claim will not be paid. We will try and assist you to find surrogate means to get the required proof.
""",
])

    bot1.train([

"""In case of an accident, when should I report to the police?
""",

"""Incidents such as"Third Party Property Damage","Bodily Injury to Self or Third Party"or"Theft"should be reported to the nearest police station as early as possible, under whose jurisdiction the incident has occurred.
""",


])

    bot1.train([
"""What is an endorsement?
""",

"""An endorsement is a written evidence of an agreed change in the policy. It is a document that incorporates changes in the terms of the policy. Additional premium will charged as applicable.
""",


])

    bot1.train([
"""What is a non-premium bearing endorsement?
""",

"""A non-premium bearing endorsement is the endorsement for which no additional premium is charged. For example, Rectification in contact details, Rectification in engine/ chassis number, Addition of hypothecation, etc.
""",


])

    bot1.train([
"""What is a premium bearing endorsement?
""",

"""A premium bearing endorsement is the endorsement for which additional premium is charged. For example, Transfer of ownership, Addition of LPG/ CNG kit, Change of RTO location, etc.
""",


])

    bot1.train([
"""I want to make changes in my policy
""",

"""
Following changes are allowed in the policy

## Name rectification :

* Please send a mail with the policy details on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done

* You can click here to put in a request
 
* You can also visit our nearest branch with these documents for the same

 "Registration number/ Engine/ Chassis number rectification"

$$  Please send a mail with the policy details and a scanned copy of your RC book on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done

* You can click here to put in a request and upload a scanned copy of your RC book
 
* You can also visit our nearest branch with these documents for the same.

## Address Rectification :

* Please send a mail with the policy details and the correct address details on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done

* You can click here to put in a request and upload a scanned copy of your address proo

* You can also visit our nearest branch with a request letter for the same

## Address change : 
* Please send a mail with the policy details and the correct address details on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done
 
* You can click here to put in a request and upload a scanned copy of your address proof

$$ You can also visit our nearest branch with a request letter for the same

Change in model/Vehicle

$$ Please visit our nearest branch with a copy of your RC book, request letter and policy documents. These changes might affect the premium charged, so please carry a cheque along.

Name transfer (Transfer of ownership)

* If you transfer your vehicle on some other person’s name, the insurance also needs to be transferred on the new owner’s name.
 

##  To get the insurance transferred in the new owner’s name, please visit our nearest branch with:
1. Endorsed copy of Registration Certificate/ Form 29 and Form 30 along with seller request letter for transfer of ownership
2. Proposal form filled and signed by the new owner of the vehicle
3. Vehicle inspection report if the difference between the date of transfer and request for endorsement is greater than 14 days
4. These changes might affect the premium charged, so please carry a cheque along

## Addition of LPG/ CNG kit/ Electrical/ Non-electrical accessories: 

Please visit our nearest branch with the following documents:

* Invoice copy of the CNG kit/ Electrical/ Non-electrical accessories and endorsed RC (with LPG/ CNG) or letter with the declaration value

* Request letter

* Cheque for paying the required premium

## Addition of Anti-theft device: 

$$ Please visit our nearest branch with the following documents:


* Invoice copy of fitted device (ARAI approved) or letter with the declaration value

* Request letter

## Change in RTO/ Registration :

* Please visit our nearest branch with the following documents:

* Copy of your updated endorsed Registration Certificate (RC)
 

* These changes might affect the premium charged, so please carry a cheque along.

## NCB Recovery/ Change :
 
$$ Please visit our nearest branch with the following documents:
 

* Request letter from Insured
 

* Original NCB reserving letter from Previous Insurer
 
*  Proof of sale of old vehicle

## Addition of Hypothecation :
 

* Please send a mail with the policy details, a scanned copy of your request letter, your sanction letter from the financial institution and the endorsed copy of your Registration Certificate (RC) on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done
 

* You can click here to put in a request and upload the scanned copy of request letter, your sanction letter from the financial institution and the endorsed copy of Registration Certificate
 

 $$ You can also visit our nearest branch with these documents for the same

## Change of Hypothecation

 $$ Please send a mail with the policy details, a scanned copy of Request letter, your sanction letter from the new financial institution, NOC from the previous financial institution and the endorsed copy of Registration Certificate on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done

 $$ You can click here to put in a request and upload the scanned copy of Request letter, your sanction letter from the new financial institution, NOC from the previous financial institution and the endorsed copy of Registration Certificate

 $$ You can also visit our nearest branch with these documents for the same

## Cancellation of hypothecation: 

*  Please send a mail with the policy details and a scanned copy of Request letter, your NOC letter from the financial institution documents and the endorsed copy of Registration Certificate on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done

* You can click here to put in a request and upload the scanned copy of Request letter, your NOC letter from the financial institution documents and the endorsed copy of Registration Certificate
*  You can also visit our nearest branch with these documents for the same
""",

])

    
    return bot1
