import machine
from machine import Pin
from machine import UART
from machine import PWM
import utime
import time
import re
import random
import network
import os
import usocket as socket

#    _   _   _ ____      _    
#   / \ | | | |  _ \    / \
#  / _ \| | | | |_) |  / _ \
# / ___ \ |_| |  _ <  / ___ \
#/_/   \_\___/|_| \_\/_/   \_\
#
#OWNER : N-John
#CREATIONN DATE: 21-APRIL-2023
#last modified : 24-JAN-2024
#GIT : https://github.com/N-John

#Aura is a minimal basic natural language built to run on microprocessors 
#with minimal storage space. It is ment for raspberry pi pico running micropython.
#It can recieve sms sent via gsm and based on the message and predefined data, it responds appropriately.
#it supports a modifiable database which can be set appropriately for desired environment.
#AURA can also perform other multiple functions such as: read, write, store and delete sms, make and receive
#calls schedule multiple gsm actions. It should be noted that this is still an ongoing project.



#Global Variables
port = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17))
phonebook = {}
mpesaSender = ""
admin = "+254712345678"
unaccounted_pay=[]

#ONBOARD LED
stat_led = machine.Pin("LED", machine.Pin.OUT)
stat_led.on()


#BUZZER
bz=machine.Pin(19,machine.Pin.OUT)
bz.off()

#STATUS LED
led=machine.Pin(1,machine.Pin.OUT)
led.off()
led.on()
time.sleep_ms(100)
led.off()
time.sleep_ms(100)
led.on()
time.sleep_ms(100)
led.off()

def blink():
    led.off()
    led.on()
    time.sleep_ms(50)
    led.off()
    time.sleep_ms(50)
    led.on()
    time.sleep_ms(50)
    led.off()

def alart():
    bz.on()
    time.sleep_ms(100)
    bz.off()
    time.sleep_ms(100)
    bz.on()
    time.sleep_ms(100)
    bz.off()


#message response

# Define a dictionary of keywords and their corresponding actions
keyword_dict = {
    "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
    "farewell": ["bye", "goodbye", "see you", "see ya"],
    "thank": ["thanks", "thank you", "ok", "asante", "sawa"],
    "internet": ["internet", "broadband", "connectivity"],
    "speed": ["speed", "fast", "slow", "3 mbps", "3 mbps", "5 mbps", "5 mbps"],
    "pricing": ["price", "cost", "bill", "charge", "fee", "how much", "pricing "],
    "location": ["location", "area"],
    "contact" : ["support", "help", "assistance", "human"],
    "outage": ["outage", "disruption", "downtime", "not working"],
    "payment": ["mpesa", "m-pesa", "cash", 'bank'],
    "installation": ["installation", "setup", "activate", "register"],
    "modem": ["modem", "router", "gateway", "access point"],
}

# Define a dictionary of responses for each type of question
responses_dict = {
    'modem' : ['you can get connected through fibre to the home'],
    'payment' : ['we accept payment through cash and/or mpesa',
                 'you can pay through mpesa provided to you'],
    "greeting": ['Hello ◉⁠‿⁠◉.', 'hello.', 'hi.', 'Hello. My name is Aura.', 'Whats up.',],
    "farewell" : ["bye", "goodbye", "see you", "see ya", "Good bye", "Hope i get to hear from you later"],
    "thank" : ['You are welcome', 'Welcome','Ok. anything else?'],
    'location' : ['Everywhere', 'Currently, we are providing internet all around the country'],
    'restricted' : ['we are not currently providing net to that area',
                    'Currently, that area is not fibre ready'],
    "outage" : ['We work to make sure that we provide maximum uptime to our users',
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
    "plan": ["We offer a variety of plans to suit your needs. What type of plan are you interested in?", 
             "Our plans are designed to offer flexibility and affordability.",
             "Our plans come with many features to meet your internet needs."],
    "pricing": ["Our pricing varies depending on the plan you choose. We have 3 Mbps for 1500, 5 Mbps for 2000 and 10 Mbps for 3000.",
                "Our pricing is competitive with other ISPs in the area.",
                "Our pricing is transparent and straightforward.",
                "We offer multiple plans with different speeds and prices, including 3 Mbps for 1500, 5 Mbps for 2000, and 10 Mbps for 3000.",
                "Our pricing is flexible and varies depending on the internet plan you choose. We offer different plans with varying speeds and prices, including 3 Mbps for 1500, 5 Mbps for 2000, and 10 Mbps for 3000.",
                "We understand that our customers have different internet needs, which is why we offer multiple plans with different speeds and prices. Our plans include 3 Mbps for 1500, 5 Mbps for 2000, and 10 Mbps for 3000, so you can choose the plan that works best for you."],
    "installation": ["We offer free installation at select places. For others, installation is just 2500.",
                     "Sign up now to get free installation in select places. Other locations can be installed for just 2500.",
                     "Free install at select places. Others: 2500.",
                     "No charge for install at select places.",
                     "Get free install at select places. Charge for others.",
                     "Enjoy free installation services at select places with us. For other locations, installation costs just 2500.",
                     "Get free installation services at select places with our service. Other locations can be installed for just 2500.",
                     "We'll install for free at select places. Installation at other locations only costs 2500."],
    "service": ["We offer excellent customer service and technical support 24/7.",
                "Our customer service team is always here to help you with any questions or concerns.",
                "Questions or concerns? Our customer service team is just a call or click away!",
                "Don't hesitate to reach out! Our team is always ready to help you with any questions or concerns.",
                "You're never alone. Our customer service team is here to help you whenever you need it."],
    "contact": ["You can call, text or whatsapp John on 0712345678.",
                "For any information, feel free to call or message us on 0712345678.",
                "We are always happy to hear from our customers. Call or sms us on 0712345678.",
                "For calls or sms, feel free to use our number 0712345678.",
                "Have a question or concern? We're here to help! Give us a call at 0712345678 and one of our friendly representatives will be happy to assist you.",
                "We're always here to help! If you have any questions, please don't hesitate to give us a call at 0712345678.",
                "At [isp] Networking, we value our customers and want to make sure you have the support you need. Please feel free to give us a call anytime at 0712345678.",
                "Need assistance? Our friendly support team is just a phone call away! You can reach us at 0712345678.",
                'you cann go to our website at https://github.com/N-John/']
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
    ("internet", "plan"): ["Our internet plans come with a variety of features to meet your needs.",
                           "Our internet plans are designed with affordability and flexibility in mind.",
                           "Our internet plans offer high-speed and reliable service."],
    ("internet", "pricing"): ["Our pricing varies depending on the plan you choose. Please visit our website or call us for more information.",
                              "Our pricing is transparent and straightforward.",
                              "We offer competitive pricing for our internet plans."],
    ("internet", "installation"): ["Our installation process is simple and easy.",
                                   "Our technicians will ensure that your installation is done correctly.",
                                   "We offer free installation services to our customers."],
    ("service", "contact"): ["You can contact us by phone, email, or through our website for any customer service or technical support needs.",
                             "Our customer service team is always here to help you with any questions or concerns.",
                             "We take pride in offering the best customer service in the industry."]
}

def interpret_input(input_str):
    single_list = []#lista of all keywords supported
    response = ''
    
    for values in keyword_dict.values():
        single_list += values
    input_str = input_str.lower()
    keyword_list = []
    for keyword in single_list:
        #strr += keyword
        if keyword in input_str:
            # If a keyword is found, add it to the list
            for key, values in keyword_dict.items():
                if keyword in values:
                    keyword = key
                    keyword_list.append(keyword)

    # If no keywords are found, return a default response
    if len(keyword_list) == 0:
        return "i don't understand"

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
            
            for keyword_check in keyword_list:
                response += random.choice(responses_dict[keyword_check])
    else:
        # If only one keyword is found, select a response from the corresponding dictionary
        response = random.choice(responses_dict[keyword_list[0]])

        if keyword_list[0] == 'greeting':
            response +=' How can i help you?'
    return response  

#GSM CLASS
class gsm:
    def start():
        try:
            alart()
            blink()
            while 1: #initialise the gsm
                stat_led.off()
                x=0
                if 'OK' in gsm.writedata('AT'):
                    x=x+1
                    
                if 'OK' in gsm.writedata('AT+CMGF=1'):
                    x=x+1
                    
                if 'OK' in gsm.writedata('AT+CNMI=2, 1, 0, 0, 0'):#'AT+CNMI=1, 2, 0, 0, 0'
                    x=x+1
                
                stat_led.on()
                #gsm.writedata('AT+CSQ')#signal quality tester
#                 gsm.writedata('AT+CCID')#read sim info
                gsm.writedata('AT+CREG?')#check if sim is registered
                #gsm.writedata('AT+CSQ')#signal quality tester
                
                stat_led.off()
                if x==3:
                    print('---GSM INIT SUCCESSFUL---')
                    blink()
                    stat_led.on()
                    break
                else:
                    print('FAILED GSM STARTUP')
                    led.on()
                    stat_led.on()
                    time.sleep_ms(100)
                    stat_led.on()
                    led.off()
                time.sleep(3)
                stat_led.off()
        
        except Exception as e:
            er='<gsm.start ERROR>: '+str(e)
            alart()
            print(er)
        
    def writedata(command):
        try:
            led.on()
            
            TERMINATION_CHAR = '\n\r'
            rxData=bytes()
            print('<----'+"b''"+str(command)+" b'' "+ str(TERMINATION_CHAR) ,end='')
            port.write(b''+command+ b'' + TERMINATION_CHAR)
            
            time.sleep(0.1)
            while port.any()>0:
                rxData += port.readline()    
            
            print('----> '+ str(rxData))
            
            print('')
            led.off()
            return str(rxData)
        
        except Exception as e:
            er="<GSM.WRITEDATA> ERROR: " +str(e)
            print(er)
            led.off()
            alart()
            return er
        

#AURA CLASS
class aura:
    def log(dat):
        try:
            led.on()
            with open('logs.txt','a') as lg:
                lg.write('\n -->'+dat)
            
            print('logged')
            led.off()
            
            return 1
        except Exception as e:
            er="<AURA.LOG> ERROR: " +str(e)
            print(er)
            led.off()
            alart()
            return 0
        
    def logsms(dat):
        try:
            led.on()
            with open('log.txt','a') as lg:
                lg.write('\n'+dat)
            
            print('logged')
            led.off()
            return 1
        except Exception as e:
            er="<AURA.LOG> ERROR: " +str(e)
            print(er)
            aura.log(er)
            blink()
            alart()
            
            return 0
        
            
    def sendsms(contact,text):
        try:
            blink()
            resno=str(contact)
            mes=str(text)
            mes=mes.strip()+'\x1A'
            
            gsm.writedata('AT+CMGS=\"' + resno + '\"')
            #gsm.writedata(mes+'\x1A')
            led.on()
            
            rxData=bytes()
            print('<----'+"b''"+str(mes)+" b'' "+ str('\n\r') ,end='')
            port.write(b''+mes+ b'' + '\n\r')
            
            time.sleep(0.1)
            
            while 1:
                if port.any()>0:
                    rxData += port.readline()    
                    print('----> '+ str(rxData))
                    #print('')
                if 'OK' in rxData:
                    aura.logsms('<-- '+resno+': '+mes)
                    return 1
            led.off()
            #return str(rxData)
            
            
        except Exception as e:
            er="<AURA.SENDSMS> ERROR: " +str(e)
            aura.log(er)
            print(er)
            alart()
            blink()
            
            return 0
        
    def readsms(message):
        try:
            blink()
            head=message.strip().split('\n')[0].replace('+CMT:','').replace('"','').strip()
            text=message.split('\n')[-2].strip()
            sender=head.split(',')[0].strip()
            date=head.split(',')[-2].strip()
            tme=head.split(',')[-1].split('+')[0].strip()
            
            print('sender: '+ sender)
            print('date: '+ date)
            print('time: '+ tme)
            print('message: '+ text)
            
            aura.logsms('--> '+message)
            
            aura.smsaction(sender,text)
                
        except Exception as e:
            er="<AURA.READSMS> ERROR: " +str(e)
            print(er)
            aura.log('--> '+er)
            blink()
            alart()
            
            return 0
    def readstoredsms(message):
        try:
            blink()
            aura.logsms('--> '+message)
            message=message.split('+CMGR:')[1].strip()
            message=message.replace('\r\n\r\nOK\r\n','').strip()
            #print('no1: '+str(message.split('\\r\\n')[1]))
            text=message.split('\\r\\n')[1].strip()
            
            led.on()
            head=message.replace('"','').split('\r\n')[0].strip()

            sender=head.split(',')[1].strip()
            date=head.split(',')[3].strip()
            tme=head.split(',')[-1].split('+')[0].strip()
            
            print('sender: '+ sender)
            print('date: '+ date)
            print('time: '+ tme)
            print('message: '+ text)
            print('-'*100)
            
            blink()
            
            aura.smsaction(sender,text)
            
        except Exception as e:
            er="<AURA.READ STORED SMS> ERROR: " +str(e)
            print(er)
            aura.log('--> '+er)
            blink()
            alart()
            
            return 0
    
    
    def makecall(phn):
        try:
            blink()
            phn=str(phn)
            phn=phn.strip()
            if phn[0] == '0':
                numbr=phn.strip()
                phn = phn[:0] + '+254' + phn[1:]
            
            gsm.writedata('ATD+ '+phn+';')
            aura.logsms('<-- MAKING CALL TO'+phn)
            '''
            while 1:# if you want to proceed on call
                if port.any()>0:
                    TEXT=""
                    rxData1=bytes()        
                    rxData1 += port.read()
                    received = rxData1.decode('utf-8')        
                    print('UNDER GOT MAKE CALL------------------'+received)
                    
                    if 'NO CARRIER' in received or 'BUSY' in received:
                        print('CALL ENDED')
                        break
            '''
            time.sleep(10)
            blink()
            gsm.writedata('ATH')
            print('HANGING UP')
            return 1
            
        except Exception as e:
            er="<AURA.MAKECALL> ERROR: " +str(e)
            print(er)
            aura.log('--> '+er)
            blink()
            alart()
            return 0
        
    def gotcall(pldata):
        try:
            bz.on()
            blink()
            caller=pldata.split(",")[0].split('"')[1].strip()
            print('GOT CALL FROM: '+caller)
            
            aura.logsms('--> Hangup call from '+caller)
            
            '''
            while 1:# if you want call to proceed
                if port.any()>0:
                    TEXT=""
                    rxData1=bytes()        
                    rxData1 += port.read()
                    received = rxData1.decode('utf-8')        
                    print('UNDER GOT CALL------------------'+received)
                    
                    if 'NO CARRIER' in received:
                        print('CALL ENDED')
                        break
            '''
                    
            gsm.writedata('ATH')
            print('HANGING UP')
            bz.off()
            blink()
            return 1
        except Exception as e:
            er="<AURA.dotcall> ERROR: " +str(e)
            print(er)
            aura.log('--> '+er)
            blink()
            alart()
            
            return 0
    
    def stored():
        try:
            #gsm.writedata('AT+CMGR={}')#read a specific stored sms
            #gsm.writedata('AT+CMGD={},0')#delete a specific stored sms
            #gsm.writedata('AT+CMGL="ALL"')  # List all SMS messages
            #gsm.writedata('AT+CPMS?')  # List all SMS messages AT+CMGD=1,4
            #gsm.writedata('AT+CMGD=1,4')#delete all messages stored
            led.on()
            print('CHECKING STORED')
            stred_sms=0
            stored_cnt=str(gsm.writedata('AT+CPMS="SM"')).split(':')[1].strip().split(',')[0].strip()
            print(int(stored_cnt))
            if int(stored_cnt) ==0:
                print('NO STORED SMS')
                return 1
            
            
            for i in range(int(stored_cnt)+1):
                if i==0:
                    continue
                msg=gsm.writedata('AT+CMGR='+str(i))#stored sms
                aura.readstoredsms(str(msg))
                gsm.writedata('AT+CMGD='+str(i)+',0')
                #print('*'*i + str(msg))
            
            blink()
            
            '''
            while 1:
                if port.any()>0:
                    
                    TEXT=""
                    rxData1=bytes()        
                    rxData1 += port.read()
                    received = rxData1.decode('utf-8')        
                    print(received+ 'END')
            '''      
            
        except Exception as e:
            er="<AURA.STORED> ERROR: " +str(e)
            print(er)
            aura.log('--> '+er)
            blink()
            alart()
            
            return 0
        
    def listen():
        try:
            blink()
            aura.stored()
            print('RUNNING LISTENER...')
            blink()
            while 1:
                if port.any()>0:
                    
                    TEXT=""
                    rxData1=bytes()        
                    rxData1 += port.read()
                    received = rxData1.decode('utf-8')
                    alart()
                    print(received+ 'END')
                    
                    if "+CMT:" in received:
                        print("RECEIVED SMS")
                        aura.readsms(received)
                    
                    elif "+CLIP:" in received:
                        print("RECEIVED call")
                        aura.gotcall(received)
                        
                    elif "+CMTI:" in received:
                        print("STORED SMS")
                        aura.stored(received)
            
        except Exception as e:
            er="<AURA.STORED> ERROR: " +str(e)
            print(er)
            blink()
            alart()
            return 0
    

    def smsaction(sendr,mess):
        try:
            blink()
            print("SMS ACTION for '"+sendr+"' with message: '"+mess+"' ............................ ",end='')
            if sendr==admin:
                #admin action
                pass
    
            else:
                aura.sendsms(sendr,interpret_input(mess))#respond to sms
                print("...NONE FOUND!!!")
            
            blink()
            return 1
        except Exception as e:
            er="<AURA.SMSACTION> ERROR: " +str(e)
            print(er)
            aura.log('--> '+er)
            led.off()
            alart()
            
            return 0


         

#MAIN LOOP
gsm.start()
#aura.stored()

aura.log('_'*100+'STARTUP' +'_'*100)
while 1:
    aura.listen()



while 1:
    if port.any()>0:
        
        TEXT=""
        rxData1=bytes()        
        rxData1 += port.read()
        received = rxData1.decode('utf-8')        
        print(received+ 'END')
        
        if "+CMT" in received:
            print("RECEIVED SMS")
            aura.readsms(received)
        
        elif "+CLIP:" in received:
            print("RECEIVED call")
            aura.gotcall(received)
        
        





    
        