import random

# Define a dictionary of keywords and their corresponding actions
keyword_dict = {
    "aura" : ["who is aura",
             "what is aura",
             'what is your name'],
    "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
    "farewell": ["bye", "goodbye", "see you", "see ya"],
    "thank": ["thanks", "thank you", "ok", "asante", "sawa"],
    "internet": ["internet", "broadband", "connectivity"],
    "speed": ["speed", "fast", "slow", "3 mbps", "3mbps", "5 mbps", "5mbps", "mbps ngapi", "mbps gani"],
    "pricing": ["price", "cost", "bill", "charge", "fee", "pesa ngapi", "how much", "pricing "],
    "location": ["location", "area", "wapi"],
    'restricted' : ['gatec', 'gate c', 'gate b', 'gateb', 'gateb', 'juja square', 'conte', 'containers'],
    "contact" : ["support", "help", "assistance", "human",
                 "chukua simu", "hauchukui simu", "haushiki simu"],
    "outage": ["outage", "disruption", "downtime", "not working", 'hakuna net'],
    "payment": ["mpesa", "m-pesa", "unachukua cash", 'hauchukui cash'],
    "installation": ["installation", "setup", "activate", "register", "installed"],
    "modem": ["modem", "router", "gateway", "access point"],
    'discount' : ['discount', 'discounts'],
    'trial' : ['trial', 'free period'],
    'robot':["robot"],
    'daily':['daily',"per day"],
    "monthly":['monthly','per month']
}

# Define a dictionary of responses for each type of question
responses_dict = {
    'monthly': ["For monthly, We have 3 Mbps for 1500, 5 Mbps for 2000 and 10 Mbps for 3000.",
                "Our monthly internet plans include 3 Mbps for Ksh1500, 5 Mbps for Ksh2000, and 10 Mbps for Ksh3000.",
                "Choose from our selection of monthly internet plans, including 3 Mbps for only Ksh1500, 5 Mbps for Ksh2000, and 10 Mbps for Ksh3000.",
                "Looking for fast and reliable internet? Our monthly plans offer 3 Mbps for Ksh1500, 5 Mbps for Ksh2000, and 10 Mbps for Ksh3000.",
                "Upgrade your internet speed with our monthly plans, which include options such as 3 Mbps for Ksh1500, 5 Mbps for Ksh2000, and 10 Mbps for Ksh3000.",
                "Enjoy lightning-fast internet with our monthly plans, featuring 3 Mbps for Ksh1500, 5 Mbps for Ksh2000, and 10 Mbps for Ksh3000."
                ],
    'daily' : ['For dily, Get 3Mbps for Ksh50',
               "Enjoy speeds of up to 3Mbps for only Ksh50!",
                "If you are looking for affordable daily internet, Get 3Mbps at just Ksh50.",
                "Experience affordable internet with 3Mbps for just Ksh50.",
                "Don't want to break the bank for internet. Get 3Mbps at an unbeatable price of Ksh50.",
                "Affordable internet made easy! Get 3Mbps for just Ksh50."],
    'trial' : ['Lucky for you, there is an ongoing trial period.',
               "You're in luck! We currently have a trial period going on.",
               "Fortunately for you, we have an ongoing trial period.",
               "You're in a good spot! Our trial period is still running.",
               "We're happy to let you know that we have an ongoing trial period.",
               "You've come at the right time! We have a trial period going on now.",
               "You're lucky! Our trial period is still in progress.",
               "Good news! We're still offering our trial period.",
               "It's your lucky day! Our trial period is still available.",
               "You're in for a treat! Our ongoing trial period is here for you.",
               "You hit the jackpot! We're still offering our trial period."],
    'discount': ['You will be informed of any discounts present when you choose an installation package.',
                 'Discounts are available depending on the day you want your installation. Ask our support team for discounts. I can give you their contact.',
                 'Discounts are time based. Currently there are none.',
                 'Currently there are no discount but there is an ongoing trial periode',
                 "While there are no discounts available right now, you can still take advantage of our ongoing trial period.",
                 "At this time, we do not offer any discounts, but we do have a trial period that you can use to test our services.",
                 "Unfortunately, we do not have any discounts available at the moment, but we are currently offering a trial period.",
                 "We do offer discounts, but they are only available on certain days. Contact our support team for more information on our available discounts.",
                 "Our pricing varies depending on the day of installation, so be sure to ask our support team about available discounts.",
                 "If you're looking for a discount, our support team can help. Just give them a call and ask about our available discounts."],
    'aura' : ["Hello am AURA. I am an AI-Based User Response Assistant which means i am not real but am always ready to help",
              'I am Aura'],
    'robot' : ['I am a robot?',
               'I am a robot',
               'Technicly i am an AI. The difference is a robot is physical while AI, as i am, is basicly a thinking algorithm. Hope thaat helps.',
               '?????????????????????????',
               'I am NOT a robot!',
               'who said am a robot?'],
    'modem' : ['You can get connected through ethernet to a router that accept internet through WAN.'],
    'payment' : ['We accept payment through cash and/or mpesa.',
                 'You can pay through mpesa provided to you.'],
    "greeting": ['Hello ◉⁠‿⁠◉', 'hello', 'hi', 'Hello. My name is Aura. How can i help you?', 'Whats up.', 'Hello ◉⁠‿⁠◉.'],
    "farewell" : ["bye", "goodbye", "see you", "see ya", "Good bye.", "Hope i get to hear from you later."],
    "thank" : ['You are welcome', 'Welcome','Ok. anything else?'],
    'location' : ['Behind senate hotel.', 'Currently, we are providing buildings behind senate hotel.'],
    'restricted' : ['we are not currently providing net to that area.',
                    'Currently, we are providing buildings behind senate hotel.'],
    "outage" : ['We work to make sure that we provide maximum uptime to our users.',
                'In case of any issue, our technical team is always ready to fix it.'],
    "internet": ["We provide high-speed internet services to our customers.",
                 "Our internet services are reliable and fast.",
                 "Our internet services are optimized for high bandwidth usage.",
                 "At our company, we're committed to delivering speedy and reliable internet services to our customers.",
                 "Say goodbye to buffering and slow connections with our lightning-fast high-speed internet services, designed to keep you connected and productive.",
                 "Get the fastest internet around with our high-speed internet services, designed to meet the needs of even the most demanding users.",
                 "Experience lightning-fast internet with our high-speed internet services."],
    "speed": ["Our internet speed varies from 3mbps to 10mbps depending on the plan you choose. What speed are you looking for?",
              "We offer different speed tiers to meet your needs.",
              "Our internet speed is constantly improving to meet customer demand.",
              "We offer internet plans with speeds ranging from 3mbps to 10mbps. Which speed works best for you?",
              "Depending on the plan you choose, our internet speeds can range from 3mbps to 10mbps. What's your preference?",
              "At our company, we provide internet speeds tailored to your needs. Our plans range from 3mbps to 10mbps. What speed works best for you?",
              "Looking for a specific internet speed? Our plans range from 3mbps to 10mbps, so you can choose the speed that's right for you.",
              "Our internet speed options vary depending on the plan you select. Would you prefer a speed of 3mbps, 5mbps, or 10mbps?"],
    "plan": ["We have 3 Mbps for 1500, 5 Mbps for 2000 and 10 Mbps for 3000."],
    "pricing": ["Our pricing varies depending on the plan you choose. We have 3 Mbps for 1500, 5 Mbps for 2000 and 10 Mbps for 3000.",
                "Our pricing is competitive with other ISPs in the area. We offer 3Mbps for 1500, 5Mbps for 2000 and 10mbps for 3000",
                "Our pricing is transparent and straightforward with prices ranging from as low as 1500.",
                "We offer multiple plans with different speeds and prices, including 3 Mbps for 1500, 5 Mbps for 2000, and 10 Mbps for 3000.",
                "Our pricing is flexible and varies depending on the internet plan you choose. We offer different plans with varying speeds and prices, including 3 Mbps for 1500, 5 Mbps for 2000, and 10 Mbps for 3000.",
                "We understand that our customers have different internet needs, which is why we offer multiple plans with different speeds and prices. Our plans include 3 Mbps for 1500, 5 Mbps for 2000, and 10 Mbps for 3000, so you can choose the plan that works best for you."],
    "installation": ["We offer free installation for PALYJOTE PALACE and nearby buildings. For others, installation is just 2500.",
                     "Sign up now to get free installation services for Palyjote Palace and nearby buildings. Other buildings can be installed for just 2500.",
                     "Free install for Palyjote & nearby ones. Others: 2500.",
                     "No charge for install at palyjote Palace & surrounding bldgs.",
                     "Get free install for Palyjote palace & nearby. Charge for others.",
                     "Enjoy free installation services for Palyjote Palace and adjacent buildings with us. For other buildings, installation costs just 2500.",
                     "Get free installation services for Palyjote Palace and surrounding buildings with our service. Other buildings can be installed for just 2500.",
                     "We'll install for free at Palyjote Palace and surrounding buildings. Installation at other buildings only costs 2500."],
    "service": ["We offer excellent customer service and technical support 24/7.",
                "Our customer service team is always here to help you with any questions or concerns.",
                "Questions or concerns? Our customer service team is just a call or click away!",
                "Don't hesitate to reach out! Our team is always ready to help you with any questions or concerns.",
                "You're never alone. Our customer service team is here to help you whenever you need it."],
    "contact": ["You can call, text or whatsapp John on 0702374411.",
                "For any information, feel free to call or message us on 0702374411.",
                "We are always happy to hear from our customers. Call or sms us on 0702374411.",
                "For calls or sms, feel free to use our number 0702374411.",
                "Have a question or concern? We're here to help! Give us a call at 0702374411 and one of our friendly representatives will be happy to assist you.",
                "We're always here to help! If you have any questions, please don't hesitate to give us a call at 0702374411.",
                "At Wired Networking, we value our customers and want to make sure you have the support you need. Please feel free to give us a call anytime at 0702374411.",
                "Need assistance? Our friendly support team is just a phone call away! You can reach us at 0702374411.",
                'https://wa.me/c/254702374411'],
    "wrong": ["I dont understand. How may i help you?",
              "What is it you mean by this?",
              "Could you use other words to explain your question?",
              "It seems like you need assistance that i cannot provide.Luckily Our friendly support team is just a phone call away! You can reach us at 0702374411.",
                'I may not not be able to do that click on link https://wa.me/c/254702374411']

}


#if keyword combination of the form
faq = {
    'plan':["internet", "plan"],
    'price':["internet", "pricing"],
    'monthly price': ["monthly", "installation"],
    'monthly price': ["pricing", "monthly"],
    'monthly price': ["monthly", "pricing"],    
    'instal':["internet", "installation"],
    'contact':["service", "contact"]
}

faq_ans = {
    'monthly price':["We have 3 Mbps for 1500, 5 Mbps for 2000 and 10 Mbps for 3000."],
    'plan': ["Our internet plans come with a variety of features to meet your needs.",
                           "Our internet plans are designed with affordability and flexibility in mind.",
                           "Our internet plans offer high-speed and reliable service."],
    'price': ["Our pricing varies depending on the plan you choose. We have 3 Mbps for 1500, 5 Mbps for 2000 and 10 Mbps for 3000.",
                "Our pricing is competitive with other ISPs in the area. We offer 3Mbps for 1500, 5Mbps for 2000 and 10mbps for 3000",
                "Our pricing is transparent and straightforward with prices ranging from as low as 1500.",
                "We offer multiple plans with different speeds and prices, including 3 Mbps for 1500, 5 Mbps for 2000, and 10 Mbps for 3000.",
                "Our pricing is flexible and varies depending on the internet plan you choose. We offer different plans with varying speeds and prices, including 3 Mbps for 1500, 5 Mbps for 2000, and 10 Mbps for 3000.",
                "We understand that our customers have different internet needs, which is why we offer multiple plans with different speeds and prices. Our plans include 3 Mbps for 1500, 5 Mbps for 2000, and 10 Mbps for 3000, so you can choose the plan that works best for you."],
    'instal': ["Our installation process is simple and easy.",
                                   "Our technicians will ensure that your installation is done correctly.",
                                   "We offer free installation services to our customers."],
    'contact': ["You can contact us by phone, email, or through our website for any customer service or technical support needs.",
                             "Our customer service team is always here to help you with any questions or concerns.",
                             "We take pride in offering the best customer service in the industry."]
}


# Define a dictionary of responses for each combination of keywords

def respond(buf):
    buf = buf.lower()
    keyword_list = [] # a list with all the keywords
    keywords = []
    #create a list of all the keywords    
    for value_list in keyword_dict.values():
        keyword_list += value_list
    
    #scan for keywords in input, have dictionery key in keywords
    for keyword in keyword_list:        
        if keyword in buf:
            for key, values in keyword_dict.items():
                if keyword in values:
                    keywords.append(key)

    #if no keyword, stop the check
    if len(keywords) == 0:
        return random.choice(responses_dict['wrong'])


    #if only one keywords
    if len(keywords) == 1:
        return random.choice(responses_dict[keywords[0]])
    
    #if keywords are in pre-defined set
    
    #if multiple keywords
    outpt = ''   
    if len(keywords) > 1:
        for key, value in faq.items():
            if set(value) == set(keywords):
                response_list = faq_ans[key]
                outpt = random.choice(response_list)
                #print(outpt)
                return outpt
                break
            

        #print(keywords)
        #print(len(keywords)-1)
        for x in range(len(keywords)):
            #print(keywords[x] + str(x))
            bf = random.choice(responses_dict[keywords[x]])
            outpt = outpt + ' ' + bf

    return outpt

print('hello')
while 1:

    print('>>>', end ='')
    cc = input()
    print('<<<' + respond(cc))
    

