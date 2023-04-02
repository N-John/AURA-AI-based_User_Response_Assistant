# Define a dictionary of keywords and their corresponding actions
keyword_dict = {
    "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
    "farewell": ["bye", "goodbye", "see you", "see ya"],
    "plan": ["plan", "package", "service", "offer", "option"],
    "internet": ["internet", "broadband", "connectivity"],
    "speed": ["speed", "fast", "slow"],
    "price": ["price", "cost", "bill", "charge", "fee"],
    "location": ["location", "area", "address"],
    "support": ["support", "help", "assistance"],
    "outage": ["outage", "disruption", "downtime", "not working"],
    "account": ["account", "login", "username", "password"],
    "email": ["email", "mailbox", "inbox", "spam"],
    "payment": ["payment", "pay", "credit card", "debit card", "bank transfer"],
    "installation": ["installation", "setup", "activate", "register"],
    "modem": ["modem", "router", "gateway", "access point"]
}


keyword_dict = {
    "internet": ["internet", "broadband", "connectivity", "data", "bandwidth"],
    "speed": ["speed", "fast", "slow", "upload", "download"],
    "plan": ["plan", "package", "service", "offer", "option", "subscription"],
    "pricing": ["pricing", "cost", "bill", "charge", "fee", "rate"],
    "installation": ["installation", "setup", "activate", "register"],
    "service": ["service", "support", "assistance", "help", "maintenance"],
    "contact": ["contact", "phone", "email", "chat", "support"]
}

combination_dict = {
    ("internet", "plan"): [
        "We offer a variety of plans with different speeds and pricing. What type of plan are you interested in?",
        "Our plans range from basic to premium, with speeds up to 1Gbps. What level of service are you looking for?",
        "We have plans for individuals, families, and businesses. What type of plan best suits your needs?",
        "Our plans come with a variety of features such as unlimited data and free installation. What features are you looking for?"
    ],
    ("internet", "pricing"): [
        "Our pricing varies depending on the plan you choose. Please visit our website or call us for more information.",
        "Our plans start at $XX per month, with no hidden fees or charges. What's your budget for internet service?",
        "We offer competitive pricing compared to other ISPs in the area. What type of plan are you interested in?",
        "Our pricing is based on the speed and features of the plan. What type of internet service are you looking for?"
    ],
    ("internet", "installation"): [
        "We provide free installation services to our customers. What type of plan are you interested in?",
        "Our technicians will install the equipment and ensure everything is working properly. What type of plan are you considering?",
        "We offer professional installation for all of our plans at no extra cost. What level of service are you interested in?",
        "Our installation process is quick and easy. What type of plan best fits your needs?"
    ],
    ("service", "contact"): [
        "You can contact us by phone, email, or through our website for any customer service or technical support needs.",
        "Our customer service team is available 24/7 to assist you. How can we help you today?",
        "We offer various channels of communication such as phone, email, and chat. Which method do you prefer?",
        "Our technical support team can assist with any issues you may have with your internet service. How can we assist you today?"
    ],
    ("internet", "speed"): [
        "Our plans offer speeds up to XX Mbps, with options for faster speeds available. What speed are you looking for?",
        "We have plans for all types of internet users, from casual browsing to heavy streaming and gaming. What type of user are you?",
        "Our plans come with guaranteed speeds and reliable connections. What type of internet service are you looking for?",
        "We offer speeds up to XX Gbps for businesses and other high-demand users. What type of plan are you considering?"
    ],
    ("plan", "pricing"): [
        "Our plans range from $XX to $XXX per month depending on the level of service you require. What's your budget for internet service?",
        "Our plans are competitively priced compared to other ISPs in the area. What type of plan are you interested in?",
        "We offer various plans with different features and pricing to meet your needs. What type of plan are you considering?",
        "Our pricing is based on the speed and features of the plan. What type of internet service are you looking for?"
    ],
    ("service", "internet"): [
        "Our internet service is reliable and fast, with plans to suit all types of users. What type of plan are you interested in?",
        "We offer various levels of service and support for all of our internet plans. What type of plan are you considering?",
        "Our plans come with 24/7 customer support and technical assistance. What type of internet service are you looking for?",
        "We pride ourselves on providing high-quality internet service with fast and reliable connections. What type of plan best fits your needs?"
],
("installation", "internet"): [
"Our installation process is quick and easy. Our technicians will ensure everything is set up and working properly. What type of plan are you interested in?",
"We offer free professional installation for all of our plans. What type of plan are you considering?",
"Our installation team will work with you to schedule a convenient time to install your equipment. What type of plan best suits your needs?",
"Our technicians are trained to handle all types of installations, ensuring that your internet service is set up correctly the first time. What type of plan are you considering?"
],
("contact", "service"): [
"You can contact our customer service team by phone, email, or through our website for any questions or concerns. How can we assist you today?",
"Our customer service team is available 24/7 to assist you with any issues or concerns. What type of assistance do you need?",
"We offer various channels of communication such as phone, email, and chat for your convenience. Which method do you prefer?",
"Our technical support team can assist with any technical issues you may have with your internet service. How can we assist you today?"
],
("pricing", "plan"): [
"Our plans range from basic to premium, with pricing starting at $XX per month. What type of plan are you interested in?",
"We offer a variety of plans to suit all types of users and budgets. What's your budget for internet service?",
"Our pricing is based on the speed and features of the plan. What type of internet service are you looking for?",
"We offer competitive pricing compared to other ISPs in the area. What type of plan are you interested in?"
],
("speed", "internet"): [
"Our plans offer speeds up to XX Mbps, with options for faster speeds available. What speed are you looking for?",
"We have plans for all types of internet users, from casual browsing to heavy streaming and gaming. What type of user are you?",
"Our plans come with guaranteed speeds and reliable connections. What type of internet service are you looking for?",
"We offer speeds up to XX Gbps for businesses and other high-demand users. What type of plan are you considering?"
]
}


# Define a list of response templates for combinations of keywords
template_list = [
    ["internet", "plan", "We offer a variety of plans with different speeds and pricing. What type of plan are you interested in?"],
    ["internet", "plan", "Our plans range from basic to premium, with speeds up to 1Gbps. What level of service are you looking for?"],
    ["internet", "plan", "We have plans for individuals, families, and businesses. What type of plan best suits your needs?"],
    ["internet", "plan", "Our plans come with a variety of features such as unlimited data and free installation. What features are you looking for?"],
    ["internet", "pricing", "Our pricing varies depending on the plan you choose. Please visit our website or call us for more information."],
    ["internet", "pricing", "Our plans start at $XX per month, with no hidden fees or charges. What's your budget for internet service?"],
    ["internet", "pricing", "We offer competitive pricing compared to other ISPs in the area. What type of plan are you interested in?"],
    ["internet", "pricing", "Our pricing is based on the speed and features of the plan. What type of internet service are you looking for?"],
    ["internet", "installation", "We provide free installation services to our customers. What type of plan are you interested in?"],
    ["internet", "installation", "Our technicians will install the equipment and ensure everything is working properly. What type of plan are you considering?"],
    ["internet", "installation", "We offer professional installation for all of our plans at no extra cost. What level of service are you interested in?"],
    ["internet", "installation", "Our installation process is quick and easy. What type of plan best fits your needs?"],
    ["service", "contact", "You can contact us by phone, email, or through our website for any customer service or technical support needs."],
    ["service", "contact", "Our customer service team is available 24/7 to assist you. How can we help you today?"],
    ["service", "contact", "We offer various channels of communication such as phone, email, and chat. Which method do you prefer?"],
    ["service", "contact", "Our technical support team can assist with any issues you may have with your internet service. How can we assist you today?"]
]



# Define a dictionary of responses for each type of question
responses_dict = {
    "order": [
        "Please visit our website to place an order.", 
        "You can call us to place an order."
    ],
    "product": [
        "We have a wide range of products. What specific product are you interested in?"
    ],
    "price": [
        "Please visit our website or call us for pricing information."
    ],
    "delivery": [
        "Our standard delivery time is 3-5 business days.", 
        "We offer expedited delivery options for an additional fee."
    ],
    "availability": [
        "Please call us or visit our website for product availability information."
    ],
    "return": [
        "Please visit our website or call us for information on our return policy."
    ],
    "refund": [
        "Please visit our website or call us for information on our refund policy."
    ]
}

