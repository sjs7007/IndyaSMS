#Author : sjs7007@gmail.com


import getpass #to take in password input without displaying it on screen
import os
import pickle
import imp

def dependencyCheckAndInstall():
    found=True;
    try:
        imp.find_module('twill')
        found = True
    except ImportError:
        found = False

        if found == False:
            os.system('cd /tmp;wget http://darcs.idyll.org/~t/projects/twill-0.9.tar.gz; tar -xvf twill-*; cd twill-0.9; sudo python setup.py install')
	    print "Depencency Install restart the application"
	    exit()

dependencyCheckAndInstall()
from twill.commands import *

username=raw_input("Enter username : ")
password=getpass.getpass("Enter password : ") #input password 

class Contact:
	def __init__(self,name,number):
		self.name=name
		self.number=number

def getList(): #returns the contact list
	if os.access("./contactList",os.F_OK):
		tempFile=open(r'contactList','rb')
		contactList=pickle.load(tempFile)
		tempFile.close()
		return contactList

def displayList():
	os.system("clear")
	if os.access("./contactList",os.F_OK):
		print("Contacts")
		contactList=getList()
		for i in range(0,len(contactList)):
			print("id : %d Name : %s Number : %s" %(i,contactList[i].name,contactList[i].number))

def addContact(name,number): #add new contact to the list
	if os.access("./contactList",os.F_OK):
		#print "Contact list is here, reading from it."
		contactList=getList()
		contactList.append(Contact(name,number))
	else:
		#print "No contact list found, creating one."
		contactList=[]
		contactList.append(Contact(name,number))

	tempFile = open(r'contactList','wb')
	pickle.dump(contactList,tempFile)
	tempFile.close()

def deleteContact(id): #delete contact of given id#
	contactList=getList()
	contactList.pop(int(id))
	tempFile = open(r'contactList','wb')
	pickle.dump(contactList,tempFile)
	tempFile.close()

def sendSMS():
	go("http://www.indyarocks.com")
	fv("1","LoginForm[username]",username)
	fv("1","LoginForm[password]",password)
	submit()
	send=1
	contactList=getList()
	temp=raw_input("Enter to number or id: ")
	
	if(len(temp)<10): #if id entered, extract number from list
		number=contactList[int(temp)].number
	else:
		number=temp

	#if number is present in list,use name also
	name='unknown' #default
	if(len(temp)<10):
		name=contactList[int(temp)].name

	while(send==1):
		message=raw_input("Enter message to %s/%s: " %(name,number))
		go("http://www.indyarocks.com/send-free-sms")
		fv("3","FreeSms[mobile]",number)
		fv("3","FreeSms[post_message]",message)
		submit()
		os.system("echo Time : `date` >> sms4log.txt")	
		os.system("echo Name : %s >> sms4log.txt" %name)
		os.system("echo Number : %s >> sms4log.txt" %number)
		os.system("echo Message : %s >> sms4log.txt" %message)
		os.system("echo ---------------------------------------------------------------- >> sms4log.txt")
		send=input("To stop enter 0, else enter 1 : ")


exit=0
while(exit!=1):
	ip=raw_input("1.Add contact\n2.Send sms\n3.View Conacts\n4.Delete Contact\n5.Exit\n")
	if(ip=='1'):
		addContact(raw_input("Enter Name : "),raw_input("Enter Number : "))
	elif(ip=='2'):
		displayList()
		sendSMS()
	elif(ip=='3'):
		displayList()
	elif(ip=='4'):
		displayList()
		deleteContact(raw_input("Enter id of contact to be removed : "))
	elif(ip=='5'):
		print("Exiting.....")
		exit=1
