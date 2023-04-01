from machine import UART, Pin
import machine
import time
import re
#

#tx pin 4
#rx pin 5
#reset 3
#ring

#initialise hardware components
relay = machine.Pin(15, machine.Pin.OUT)  #switch
relay.off()
relay2 = machine.Pin(14, machine.Pin.OUT) #router
reset = machine.Pin(3, machine.Pin.OUT)
reset.on()

led = machine.Pin("LED", machine.Pin.OUT)
led.off()

#SET VARIABLES

phonebook = {}
mpesaSender = ""
sendcall = False




#initialise uart communication
port = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))
phone = "+254702374411"

###############################################################33
phonebook={'0707341429':{'name' :'Gerry',
                         'username' : 'Iq',
                         'price': 1200},
           '0740892684':{'name' : 'John Wamwenga',
                         'username' : 'John4',
                         'price': 1500},
           '0768008600':{'name' : 'John Mbita',
                         'username' :'JohnMw',
                         'price':1500},
           '0718818167':{'name' : 'John Ndungu',
                         'username' : 'John',
                         'price':1200},
           '0794625443':{'name' : 'John Mwangi',
                         'username' : 'JohnM',
                         'price':1500},
           '0711820395':{'name' : 'Linus Irungu',
                         'username' :'Kym',
                         'price':1200},
           '0710950747':{'name' : 'Totcy',
                         'username' :'Totcy1',
                         'price':1200},
           '0794016002':{'name' : 'Victor',
                         'username' :'VICTOR',
                         'price':1200},
           '0799108775':{'name' : 'Ken',
                         'username' :'Ken',
                         'price':1200},
           '0790181044':{'name' : 'Vincent',
                         'username' :'vin',
                         'price':1200},
           '0708448564':{'name' : 'Sam',
                         'username' :'sam',
                         'price':1500},
           '0741905672':{'name' : 'Sam',
                         'username' :'sam',
                         'price':1500},
           '0718149182':{'name' : 'Rolex',
                         'username' :'Rolex',
                         'price':1500},
           '0716246223':{'name' : 'Juliet Wahu',
                         'username' :'Wahu',
                         'price':1200},
           '0724760802':{'name' : 'Serena',
                         'username' :'serena',
                         'price':1500},
           '0706111002':{'name' : 'Moses',
                         'username' :'Moses',
                         'price':1500},
           '0700174413':{'name' : 'Waleh',
                         'username' :'Moses',
                         'price':1500},
           '0775405516':{'name' : 'Robert',
                         'username' :'robert',
                         'price':1500},
           '0702027767':{'name' : 'admin MAGDALENE',
                         'username' :'02027767',
                         'price':00},
           '0702374411':{'name' : 'admin JOHN',
                         'username' :'02374411',
                         'price':00},
           
           }
#contacts = ['0111777188', '0702027767',  '0702374411']

contacts = []
contacts = list(phonebook.keys())
print("'PHONE' : 'NAME' : 'USERNAME' : 'PRICE' : 'SPEED'")
#print(contacts)
#x=len(phonebook)

for p in range(len(phonebook)):
    print(contacts[p] + ' ' , end='')
    #name = phonebook[contacts[p]]['price']
    #print(contacts[p]
    print(phonebook[contacts[p]]['name']+ ' ' , end='')
    print(phonebook[contacts[p]]['username']+ ' ' , end='')
    print(str(phonebook[contacts[p]]['price']))

##################################################################3

#GSM CONTROL
class gsm:
    
    def reset():
        led.on()
        reset.off()
        time.sleep_ms(100)
        reset.on()
        led.off()
    
    def writedata(command):
        led.on()
        TERMINATION_CHAR = '\n\r'
        rxData=bytes()
        port.write(b''+command+ b'' + TERMINATION_CHAR)
        time.sleep(0.1)
        while port.any()>0:
            rxData += port.readline()    
        
        print(rxData.decode('utf-8'))
        r="OK" in rxData.decode('utf-8')
        
    
        led.off()
        return int(r)

    
#COMMANDS FOR CONTROLS ON BOARD ######################################################################################
class board:
    
    def blink():
        led.on()
        time.sleep(0.02)
        led.off()
        time.sleep(0.02)
        
    def log(buff):
        led.on()
        try:
            # open the file in read mode and read its contentS
            with open("do_log.txt", "r") as log_file:
                log_contents = log_file.read()
        
            # modify the contents as needed
            log_contentsnew = log_contents + buff
            log_contents = log_contents.replace(log_contents, log_contentsnew)
            # open the file in write mode and write the modified contents back to the file
    
            with open("do_log.txt", "w") as log_file:
                log_file.write(log_contents)
        except:
            print('FAILED TO CREATE LOG')
            send_sms(phone, 'LOG ERROR')
            
        led.off()
        
    def mdos(mbuf):
        if "SWITCH OFF" in mbuf:
            relay.on()
            sms.send(phone,'DONE. ' + "SWITCH OFF")
        elif "SWITCH ON" in mbuf:
            relay.off()
            sms.send(phone,'DONE. ' + "SWITCH ON")
        elif "SWITCH RESTART" in mbuf:
            relay.on()
            time.sleep(5)        
            relay.off()
            sms.send(phone,'DONE. '+"SWITCH RESTART")            
        elif "ROUTER OFF" in mbuf:
            relay2.on()
            sms.send(phone,'DONE. '+"ROUTER OFF")
        elif "ROUTER ON" in mbuf:
            relay2.off()
            sms.send(phone,'DONE. '+"ROUTER ON")
        elif "ROUTER RESTART" in mbuf:
            relay.on()
            time.sleep(5)        
            relay.off()
            sms.send(phone,'DONE. '+"ROUTER RESTART")
        elif "CLEAR" in mbuf:
            with open("do_log.txt", "w") as log_file:
                log_file.write(' ')
            sms.send(phone,'DONE. '+ 'LOG FILE CLEARED')
        else:
            sms.send(phone,'FAILED TO UNDERSTAND')
    
#SMS INTERUCTION ################################################################################################3
class sms:
    
    def amount(buf):
        led.on()
        
        
        print('amount start------' + buf)
        amnt = buf.split(' ', 7)#get first 4 letters splited text
        print('======amnt' + str(amnt))
        rec = 0
        rec = len(amnt)
        print('======rec' + str(rec))
        rstr = ''
        rint = -1
        j = 0
    
        for j in range(rec):
            
            if 'Ksh' in amnt[j]:
                
                print('ammount check'+str(amnt[j]))
                try:
                    rint = int(re.search(r'\d+', amnt[j]).group(0))
                    print('*******rint' + str(rint))
                    rstr = amnt[j]
                    rstr = 'of '+ rstr
                except:
                    rint = -1
                    rstr =  ' '
                    board.log('AMMOUNT DECODE ERROR')
                    print('AMMOUNT DECODE ERROR')                    
                break
        
        #return rint #int form
        led.off()
        return rstr #string form
    
    def foward(text):
        led.on()
        try:
            gsm.writedata('AT+CMGF=1')
            gsm.writedata('AT+CMGS=\"' + phone + '\"')
            #gsm.writedata('AT+CMGS=\"+254702374411\"')
            gsm.writedata(text)
            f= gsm.writedata('\x1A')
            print('SMS FOWARDED')
        except:
            print('FOWARDING FAILED')
            board.log('FOWARDING FAILED:\n' + text + '\n')
            f = 0
        
        led.off()
        return f
        
    def send(number, text):
        led.on()
        try:
            print('SENDING SMS')
            board.log('SMS TO: ' + number + '\n' + text)
            gsm.writedata('AT+CMGF=1')
            gsm.writedata('AT+CMGS=\"' + number + '\"')
            #gsm.writedata('AT+CMGS=\"+254702374411\"')
            gsm.writedata(text)
            s = gsm.writedata('\x1A')
            time.sleep(5)
            
        except:
            print('FAILED TO SEND SMS')
            board.log('FAILED TO SEND SMS\n NUMBER: ' + number + 'CONTENTS: ' + text)
            s= 0
            
        
        led.off()
        return s
    
    
    def sender(buf):
        led.on()
        try:
            b=buf.split(",",3)
            #print('IS ' + b[3])
            sender=b[0].split(" ")[1]
            date=b[2]
    
            time_message=b[-1].split("\n")
            #print(time_message[1])
            #print(f"sender:{sender}\ndate :{date} {time_message[0]}\nmessage:{time_message[1]}")                
        except:
            sender = '0000000000'
            print('SENDER NOT FOUND')
            board.log('ERRO SENDER NOT FOUND FOR: ' + buf)
        
        led.off()
        return sender
    
    def contents(cbuf):
        led.on()
        try:
            b=buf.split(",",3)
            #print('IS ' + b[3])
            time_message=b[-1].split("\n")
            #print(time_message[1])    
            #print(f"sender:{sender}\ndate :{date} {time_message[0]}\nmessage:{time_message[1]}")
            scontents = time_message[1]
        except:
            scontents = ' '
            print('CONTENTS NOT FOUND')
            board.log('CONTENTS NOT FOUND')
            
        led.off()
        return scontents
    
    def execute(cbuf):
        led.on()
        try:
            board.log(cbuf)
            print(cbuf)
            b=cbuf.split(",",3)
            print('IS ' + b[3])
            sender=b[0].split(" ")[1]
            date=b[2]    
            time_message=b[-1].split("\n")
            #print(time_message[1])    
            #print(f"sender:{sender}\ndate :{date} {time_message[0]}\nmessage:{time_message[1]}")
            
            
            #MPESA MESSAGE--------------------
            if "w405543514" in sender:
                print("mpesa sms")
                message = time_message[1]
                #print('has ' + str(len(message)))
                
                c = message.split(' ', 1)
                code = c[0]
                #print(amount(message))
                #print(time_message[1])
                if 'received' in message:
                    i = len(contacts)
                    for x in range(i):
                        #print('\n' + str(x))
                        if contacts[x] in time_message[1]:
                            #print(contacts[x])
                            
                            name = phonebook[contacts[x]]['name']
                            username = phonebook[contacts[x]]['username']
                            price = phonebook[contacts[x]]['price']
                            prs = sms.amount(message)
                            #print(amnt)
                
                            sms.send(contacts[x] , code + ' PAYMENT RECEIVED. Hello ' + name + '. Your funds '+ prs +' to Wired networking have been received. Thank you for staying with us. FOR QUERIES CONTACT 0702374411')
                            time.sleep(20)
                            sms.send(phone, code + ' RECEIVED AND CONFIRMED FUNDS '+ prs +' FROM ' + name)
                            time.sleep(10)
                            sendcall = True
                            call.call()
                    
                            break
            
                        if x >= i-1:
                            print('FAILED TO FIND SENDER')
                            sms.foward('FAILED TO FIND SENDER OF:' + message)                            
                            time.sleep(10)
                            
                            
                sms.send(phone, 'FROM MPESA: ' + message)
                time.sleep(10)
                            
            
            
            elif phone in sender: #ADMIN SMS-------------------------------------------------------------------                
                board.mdos(time_message[1])
                
            elif '35166616279636@6w6' in sender: #SAFARICOM SMS-------------------------------------------------------------------
                sms.send(phone, 'FROM SAFARICOM: ' + time_message[1])
                time.sleep(10)
                
            elif "w4378677162796" in sender: #MSHWARII SMS-------------------------------------------------------------------
                sms.send(phone, 'FROM MSHWARI: ' + time_message[1])
                time.sleep(10)
                
            else:#FROM UNSAVED NUMBER-----------------------------------------------------------------------------------
                sms.foward('GOT SMS FROM: ' + sender + ' CONTENTS: ' + time_message[1])
                time.sleep(5)
                
            
                
            led.off()   
            return 1
        
        except:
            board.log('SMS EXECUTE FAILED\n')
            print('SMS EXECUTE FAILED\n')
        
            led.off()
            return 0         
        
 
#CALLS COMMANDS ###########################################################################################################
    
class call:
    
    def call():#ONLY CALLS ADMIN
        led.on()
        try:
            gsm.writedata('ATD+ +254702374411;')
            time.sleep(10)
            c=gsm.writedata('ATH')
            time.sleep(2)
        except:
            print('FAILED TO CALL')
            board.log('FAILED TO CALL ADMIN: \n')
            c= 0
            
        led.off()
        return c
    
    def hangup(ibuf):
        led.on()
        try:
            b=ibuf.split(",")
            print(b)
            caller=b[0].split(" ")[1]
            caller = caller.replace('"', '')
            print(caller)    
            gsm.writedata('ATH')
            time.sleep(3)
            
            #i = int(caller)
            k = caller in contacts
            print(k)
            if k:
                n = phonebook[caller]['name']
                print(n)
                sms.foward('RECEIVED CALL FROM: '+ n + ' ID: '+ caller)
                time.sleep(5)
                
            
            else:
                sms.foward('RECEIVED CALL FROM: '+ caller)
                time.sleep(5)
                
                
            i = 1
        except:
            print('FAILED HANGUP')
            board.log('FAILED HANGUP PROCESS FROM: \n' + ibuf)
            i= 0
        led.off()
        
    def caller(cbuf):
        led.on()
        try:
            b=buf.split(",")
            #print(b)
            caller=b[0].split(" ")[1]
            print(caller)
            c = caller
        except:
            print('CALLER NOT FOUND')
            board.log('FAILED TO FIND CALLER: \n' + cbuf)
            c= 'NOT FOUND'
        
        return c      
        led.off()
            

#START #################################################################################################
    
def start():
       
    for p in range(10):
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)
    

    gsm.writedata('AT')
    gsm.writedata('AT+CMGF=1')
    gsm.writedata('AT+CNMI=1, 2, 0, 0, 0')
    
    #gsm.writedata('AT+CMGL="ALL"')
    
    
    
    return 1
    
            
#########################CODE BEGIN########################################################################            
while not start():
    1
    
print('began')
sms.send(phone, 'ONLINE')
time.sleep(5)
    
i = 0
text = ""
received = ""


while 1:
    if sendcall == True:
        call()
        sendcall = False

    
    
    if port.any()>0:
        TEXT=""
        rxData1=bytes()        
        rxData1 += port.read()
        received = rxData1.decode('utf-8')        
        print(received)
        #board.log(received)
        TEXT=text
        #####################################################################################
        
        if "RING\r" in received:
            print("Its Call")
            call.hangup(received)
        
        text = received.split(" ")[0]
        if text=="\r\n+CMT:":
            print("IS SMS")
            print(received)
            sms.execute(received)
            
