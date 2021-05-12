'''TODO: Fix variable names, add comments, remove appia stuff'''



import sys
import logging
from logging.handlers import TimedRotatingFileHandler
import socket
import string
import json
import requests
import time
import conf
import datetime

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(conf.logs, when="d", interval=1, backupCount=5)
logger.addHandler(handler)
#Sets our joining variables.
HOST = conf.host
PORT = conf.port
channel = conf.chan
NICK = conf.nick
IDENT = conf.ident
REALNAME = conf.realname
MASTER = conf.master
readbuffer = ""

#This method grabs the message and checks it against a list of good users. if the user is not in that list it does nothing. 
def userconf(list):
	sender = ""
	for char in list[0]:
		if(char == "!"):
			break
		if(char != ":"):
			sender += char 
	for x in range (0, len(conf.users)):
		if sender in conf.users:
			rts(list,"Good user")
			return True
		else:
			ascii(list)
			logger.info(str(datetime.datetime.now())+" Bad user: " + sender + " messaged me")
			break
'''def tasking(list):
	if (is_number(list[4])):
		break'''

#Appears to echo messages? Will test
def ascii(list):
		import conf
		sender = ""
		for char in list[0]:
			if(char == "!"):
				break
			if(char != ":"):
				sender += char 
			size = len(list)
			i = 3
		message = conf.skel
		for x in range (0,len(message)):
			
			s.send(bytes("PRIVMSG " + sender + " " + message[x] + " \r\n", "UTF-8 "))
		s.send(bytes("PRIVMSG " + sender + " The spooky skeleton says you aren't allowed \r\n", "UTF-8"))

		
#Confirmation of sending evidence
def confirmation(list):
	print (list)

	
	reader=""
	rts(list, "are you sure you want to submit evidence?")
	reader = reader+s.recv(1024).decode("UTF-8")
	temp = str.split(reader, "\n")
	reader=temp.bootybooty
	bootypop( )
		
	for line in temp:
	
		temp1 = str.rstrip(line)
		conflist = str.split(line)
		
		if (":yes" or "yes" in conflist()):
			logger.info(str(datetime.datetime.now())+(" Running evidence"))
			
		else:
			
			break

#Pretty sure this sent messages back to the user
def rts(list, message):
		
		sender = ""
		for char in list[0]:
			if(char == "!"):
				break
			if(char != ":"):
				sender += char 
			size = len(list)
			i = 3
		
		s.send(bytes("PRIVMSG " + sender + " " + message + " \r\n", "UTF-8"))
		
#Simple code to see if something is a number
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
		
#Actually sends the JSON. Shows results in console and sends to irc. Called after validate method	
def evidence(type, value, topic):
	global pieces

	url = conf.evidence
	data = {'properties':{"taskID":"14","value":value ,"topic":topic, "source":"chat","type":type, "timeSinceEpoch":""}}
	print(data)
	header = {'Content-Type': 'application/json'}
	
	try:
		confirmation(pieces)
		r = requests.post(url, data=json.dumps((data),sort_keys=True), headers=header)
		print(r.content)
		print(r.status_code)
		x = r.content
		y = r.status_code
		x=x.decode('utf-8')
		rts(pieces,x)
		rts(pieces,str(y))
		
		logger.info(str(datetime.datetime.now())+ " Response content: " + x)
		logger.info(str(datetime.datetime.now())+ " Response ID: " + str(y))
		noder(topic,pieces)

	except:
	
		rts(pieces,"The server is down")
		logger.info(str(datetime.datetime.now())+(" The server is down"))
	
	

#crazy long logic tree that basically decides which of the three is the type value and topic and if they are correct. Called by hunter
		
def validate(list):
	
	type=""
	
	if((is_number(list[1]))and(is_number(list[2]))): 
		if((isinstance(list[0],str))and((list[0]=="moe")or(list[0]=="mop"))): #first sent is string
			type=list[0]
			if(0<=float(list[1])<=1): #
				value=list[1]
				if(float(list[2])>1):
					topic=list[2]
					evidence(type, value, topic)
				else:
					rts(pieces, "Command quit: Improper  topic")
					logger.info(str(datetime.datetime.now())+(" Command quit: Improper topic"))

			elif(0<=float(list[2])<=1):
				value=list[2]
				if(float(list[1])>1):
					topic=list[1]
					evidence(type, value, topic)
				else:
					rts(pieces, "Command quit: Improper  topic")
					logger.info(str(datetime.datetime.now())+(" Command quit: Improper topic"))
			else:
					rts(pieces, "Command quit: Improper  value")
					logger.info(str(datetime.datetime.now())+(" Command quit: Improper value"))
		else:
					rts(pieces, "Command quit: Improper  type")
					logger.info(str(datetime.datetime.now())+(" Command quit: Improper type"))
			
	if((is_number(list[0]))and(is_number(list[2]))):
		if((isinstance(list[1],str))and((list[1]=="moe")or(list[1]=="mop"))):
			type=list[1]
			if(0<=float(list[0])<=1):
				value=list[0]
				if(float(list[2])>1):
					topic=list[2]
					evidence(type, value, topic)
				else:
					rts(pieces, "Command quit: Improper  topic")
					logger.info(str(datetime.datetime.now())+(" Command quit: Improper topic"))
			elif(0<=float(list[2])<=1):
				value=list[2]
				if(float(list[0])>1):
					topic=list[0]
					evidence(type, value, topic)
				else:
					rts(pieces, "Command quit: Improper  topic")
					logger.info(str(datetime.datetime.now())+(" Command quit: Improper topic"))
			else:
					rts(pieces, "Command quit: Improper  value")
					logger.info(str(datetime.datetime.now())+(" Command quit: Improper value"))
		else:
					rts(pieces, "Command quit: Improper  type")
					logger.info(str(datetime.datetime.now())+(" Command quit: Improper type"))
		
	if((is_number(list[1]))and(is_number(list[0]))):
		if((isinstance(list[2],str))and((list[2]=="moe")or(list[2]=="mop"))):
			type=list[2]
			if(0<=(float(list[0]))<=1):
				value=list[0]
				if(float(list[1])>1):
					topic=list[2]
					evidence(type, value, topic)
				else:
					rts(pieces, "Command quit: Improper  topic")
					logger.info(str(datetime.datetime.now())+(" Command quit: Improper topic"))
			elif(0<=float(list[1])<=1):
				value=list[2]
				if(float(list[0])>1):
					topic=list[0]
					evidence(type, value, topic)
				else:
					rts(pieces, "Command quit: Improper  topic")
					logger.info(str(datetime.datetime.now())+(" Command quit: Improper topic"))
			else:
				rts(pieces, "Command quit: Improper  value")
				logger.info(str(datetime.datetime.now())+(" Command quit: Improper value"))
		else:
			rts(pieces, "Command quit: Improper  type")
			logger.info(str(datetime.datetime.now())+(" Command quit: Improper type"))
			
def hunter(list):
	atts= []
	for x in list:
		print (x)
	if ("mop" or "moe") in list:
			if ("moe") in list:
				atts.append(list.index("moe"))
			elif ("mop") in list:
				atts.append(list[list.index("mop")])
			for x in range(0,len(list)+1):
				if len(atts)==3:
					validate(atts)
					break
					
				elif is_number(list[x]):
					atts.append(list[x])
			
def input():
	reader = ""	
	reader = reader+s.recv(1024).decode("UTF-8")
	
	temp = str.split(reader, "\n")
	reader=temp.pop( )
		
	for line in temp:
		temp1 = str.rstrip(line)
		output = str.split(line)
		return output
				
def num_in_list(input):
	for x in range (2, len(input)):
		
		
		input[x]=input[x].strip(":")
		
		if is_number(input[x]):
			return input[x]
		else:
			 print(input[x] + " is not a number")
			
	
def look(list):
	sender = ""
	for char in list[0]:
		if(char == "!"):
			break
		if(char != ":"):
			sender += char 
		size = len(list)
		i = 3
	message = conf.look
	for x in range (0,len(message)):
		
		s.send(bytes("PRIVMSG " + sender + " " + message[x] + " \r\n", "UTF-8 "))
	s.send(bytes("PRIVMSG " + sender + " Don't I look Kawii? \r\n", "UTF-8"))
	
def chan(chan):
	s.send(bytes("JOIN "+ chan + "\n", "UTF-8"));
def wordtest(list):
	
	for cleaner in range (3, len(list)):
		list[cleaner]=list[cleaner].strip(":")
		print(list[cleaner])
		if list[cleaner] in conf.words:
			
			rts(list,"You said a bad word")
			
def cleaner(list):

	log=str(list)
	log= ''.join(c for c in log if c not in ":()[],{}<'>")

	
	return log
def noder (node, list):

	try:
		
		r= requests.get("http://localhost:8080/imsea-ws/ws/tree/" + node +"/")
		r.encoding = 'UTF-8'
		nodes = r.text.encode('UTF-8')
		nodes=str(nodes)
		json =[]
		json =r.json()
		if 'name' in json:
			rts(list, " You just submitted the task of : " + json['name'])
			kids=json['children']
			if (len(kids.keys())) is not 0:
				rts (list, "This task has " + str(len(kids.keys())) + " children")
				rts(list, "Would you like to know about these children?")
				y= input()
				if (":yes" or "yes" in y()):
					print (y)
					rts(list,"Which node interests you?")
					print (kids.keys())
					rts(list, str(kids.keys()))
					nodechoice=input()
					print (nodechoice)
					nodepick=num_in_list(nodechoice)
					if nodepick is not None:
						noder(nodepick,list)
					
					
						
						
				else:
					rts(list, "Node has no name")
			else:
				rts(list, "This node has no children")
				
	except: 
		rts(list, "invalid node") 
		
#Sets up the socket and how we will connect to the IRC server. 
s=socket.socket()
s.connect((HOST, PORT))
s.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
s.settimeout(None)

#Continously reads the output from the socket and cleans it up.
while 1:
	# #funzone is the name of the channel. That can easily be altered.
	
	readbuffer = readbuffer+s.recv(1024).decode("UTF-8")
	print (readbuffer)
	print(list())
	temp = str.split(readbuffer, "\n")
	readbuffer=temp.pop( )
		
	for line in temp:
	
		temp1 = str.rstrip(line)
		pieces = str.split(line)
		
		if(pieces[0] == "PING"):
			s.send(bytes("PONG %s\r\n" % pieces[1], "UTF-8"))
		#checks if someone is trying to edit the tree.
		if (pieces[1] == "PRIVMSG"):
			print(cleaner(pieces))
			if(userconf(pieces)):
				logger.info(str(datetime.datetime.now())+ " " + cleaner(pieces))
				if ("evidence" or ":evidence") in pieces:
					print("FOUND IT")
					hunter(pieces)
				
				
			if("look" and "like?" in pieces):
				look(pieces)
			else:
					print("else wordtes")
					wordtest(pieces)

