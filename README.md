# AURA - AI-based User Response Assistant

Formaly known as MIA, Aura is an automatic user manager that opperates through sms where it manages user payments through reading sms and provides required response.

Aura will read sms via a gsm module and interprate the data. A response is generated in accordance to if the sender is admin, a customer or an unknown number.</br></n>
</n>

If the sender is a user, Aura will be able to answer simple questions such as if there are any network issues, power failure or other queries.</br></n>


If the user is an unknown user number, Aura will first apresent itself to see if its a wrong number or a potential user. If it is a potential customer, Aura will answer the user's basic questions and try to provide as much informarion through a set of variables. If it is not able, it would refer the user to the admin in hopes of letting them answer.</br></n>


Aura can also control hardware components from relays connected to it. Aura can control a mikrotik routor through telnet to control user wifi connection and set up schedulers for connecting and disconnecting users to the internet. The pico can read M-PESA payment messages, find out how much they have paid and connect them to the internet for as many days as for which they have paid for.</br></n>


<h3>ADMIN POWER</h3>
The admin will have a lot of power over Aura. This include:</br>
*Gets first hand notification from Aura</br>
*Notifies them of payments made</br>
*Can delete chats from the pico .txt
*

<h3>AURA CAPABILITIES</h3>
<h5>Get payments</h5>
*Aura recieves M-pesa sms and interprates them to find out how much was sent, and the sender. If the money is from a customer, it determines how much and determines for how long they have paid. Through telnet, it connects to the mikrotik router and connects the user to the internet. It then sets up/edits the respective scheduler and to disconnect the user from the network once their period expires.</br>
<h5>RESPONDS TO USER QUERIES</h5>
Through gained user data collected, Aura is able to answer user questions and is able to communicate to both users and non users. Aura can hold basic ocommunication with non users and introduce them to the network. It can their questions and provide required answers.
<h5>CONTROL HARDWARE COMPONENTS</h5>
With the help of relays connected to Aura, it can control basic electronic components. This will be usefull for resetting, turning off or turning on connected switches and routers.
