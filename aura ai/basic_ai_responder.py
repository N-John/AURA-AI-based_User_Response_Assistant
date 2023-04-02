import random

# Define a dictionary of keywords and their corresponding actions
keyword_dict = {
    "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
    "farewell": ["bye", "goodbye", "see you", "see ya"],
    "thank": ["thanks", "thank you", "ok", "asante", "sawa"],
    "internet": ["internet", "broadband", "connectivity"],
    "speed": ["speed", "fast", "slow", "3 mbps", "3mbps", "5 mbps", "5mbps", "mbps ngapi", "mbps gani"],
    "pricing": ["price", "cost", "bill", "charge", "fee", "pesa ngapi", "how much", "pricing "],
    "location": ["location", "area", "wapi"],
    'restricted' : ['gatec', 'gate c', 'gate b', 'gateb', 'gateb', 'juja square', 'conte', 'containers']
    "contact" : ["support", "help", "assistance", 'human', 'chukua simu', 'hauchukui simu', 'haushiki simu'],
    "outage": ["outage", "disruption", "downtime", "not working", 'hakuna net'],
    "payment": ["mpesa", "m-pesa", "unachukua cash"],
    "installation": ["installation", "setup", "activate", "register"],
    "modem": ["modem", "router", "gateway", "access point"]
}

# Define a dictionary of responses for each type of question
responses_dict = {
    "greeting": ['Hello ◉⁠‿⁠◉', 'hello', 'hi', 'Hello. My name is Aura. How can i help you?', 'Whats up', 'Hello ◉⁠‿⁠◉',]
    "farewell" : ["bye", "goodbye", "see you", "see ya", "Good bye", "Hope i get to hear from you later"]
    "thank" : ['You are welcome', 'Welcome','Ok. anything else?'],
    'location' : ['Behind senate hotel', 'Currently, we are providing buildings behind senate hotel']
    'restricted' : ['we are not currently providing net to that area',
                    'Currently, we are providing buildings behind senate hotel']
    "outage" : ['We work to make sure that we provide maximum uptime to our users',
                'In case of any issue, our technical team is always ready to fix it.']
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
    "plan": ["We offer a variety of plans to suit your needs. What type of plan are you interested in?", 
             "Our plans are designed to offer flexibility and affordability.",
             "Our plans come with many features to meet your internet needs."],
    "pricing": ["Our pricing varies depending on the plan you choose. We have 3 Mbps for 1500, 5 Mbps for 2000 and 10 Mbps for 3000.",
                "Our pricing is competitive with other ISPs in the area.",
                "Our pricing is transparent and straightforward.",
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
                'https://wa.me/c/254702374411']
}

# Define a list of response templates for combinations of keywords
template_list = [
    ["internet", "plan"],
    ["internet", "pricing"],
    ["internet", "installation"],
    ["service", "contact"]
]

# Define a dictionary of responses for each combination of keywords
combination_dict = {
    ("internet", "plan"): ["Our internet plans come with a variety of features to meet your needs.", "Our internet plans are designed with affordability and flexibility in mind.", "Our internet plans offer high-speed and reliable service."],
    ("internet", "pricing"): ["Our pricing varies depending on the plan you choose. Please visit our website or call us for more information.", "Our pricing is transparent and straightforward.", "We offer competitive pricing for our internet plans."],
    ("internet", "installation"): ["Our installation process is simple and easy.", "Our technicians will ensure that your installation is done correctly.", "We offer free installation services to our customers."],
    ("service", "contact"): ["You can contact us by phone, email, or through our website for any customer service or technical support needs.", "Our customer service team is always here to help you with any questions or concerns.", "We take pride in offering the best customer service in the industry."]
}

def interpret_input(input_str):
    # Convert the input string to lowercase for case-insensitive matching
    input_str = input_str.lower()

    # Initialize an empty list to store the keywords found in the input string
    keyword_list = []

    # Loop through the keywords and check if they appear in the input string
    for keyword in keyword_dict.values():
        if keyword in input_str:
            # If a keyword is found, add it to the list
            keyword_list.append(keyword)

    # If no keywords are found, return a default response
    if len(keyword_list) == 0:
        return "Thank you for your interest in our ISP. How may I assist you today?"

    # Check if the input string contains multiple keywords
    if len(keyword_list) > 1:
        # Select a response template based on the combination of keywords
        response_template = None
        for template in template_list:
            if all(keyword in keyword_list for keyword in template):
                response_template = template
                break
        
        # If a template is found, select a response from the corresponding dictionary
        if response_template is not None:
            response_list = combination_dict[response_template]
            response = random.choice(response_list)
        else:
            # If no template is found, select a random response from the list of all keyword responses
            response_list = []
            for keyword in keyword_list:
                response_list += responses_dict[keyword]
            response = random.choice(response_list)
    else:
        # If only one keyword is found, select a response from the corresponding dictionary
        keyword = keyword_list[0]
        response_list = responses_dict[keyword]
        response = random.choice(response_list)

    return response

print('hello')

while 1:
    print('>>>', end ='')
    c = input()
    print(interpret_input(c))
    
