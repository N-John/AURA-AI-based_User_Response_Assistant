import random

# Define a dictionary of keywords and their corresponding actions
keyword_dict = {
    "internet": "internet",
    "speed": "speed",
    "plan": "plan",
    "pricing": "pricing",
    "installation": "installation",
    "service": "service",
    "contact": "contact"
}

# Define a dictionary of responses for each type of question
responses_dict = {
    "internet": ["We provide high-speed internet services to our customers.", "Our internet services are reliable and fast.", "Our internet services are optimized for high bandwidth usage."],
    "speed": ["Our internet speed varies depending on the plan you choose. What speed are you looking for?", "We offer different speed tiers to meet your needs.", "Our internet speed is constantly improving to meet customer demand."],
    "plan": ["We offer a variety of plans to suit your needs. What type of plan are you interested in?", "Our plans are designed to offer flexibility and affordability.", "Our plans come with many features to meet your internet needs."],
    "pricing": ["Our pricing varies depending on the plan you choose. Please visit our website or call us for more information.", "Our pricing is competitive with other ISPs in the area.", "Our pricing is transparent and straightforward."],
    "installation": ["We provide free installation services to our customers.", "Our installation process is simple and easy.", "Our technicians will ensure that your installation is done correctly."],
    "service": ["We offer excellent customer service and technical support 24/7.", "Our customer service team is always here to help you with any questions or concerns.", "We take pride in offering the best customer service in the industry."],
    "contact": ["You can contact us by phone, email, or through our website.", "Our contact information is listed on our website.", "We are always happy to hear from our customers."]
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
    for keyword in keyword_dict.keys():
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
    
