from twill.commands import *
import getpass #to take in password input without displaying it on screen

username=raw_input("Enter username : ")
password=getpass.getpass() #input password 

go("http://www.indyarocks.com")
showforms()
fv("1","LoginForm[username]",username)
fv("1","LoginForm[password]",password)
submit()
showforms()
send=1
while(send==1):
	number=raw_input("Enter to number : ")
	message=raw_input("Enter message : ")
	go("http://www.indyarocks.com/send-free-sms")
	showforms()
	fv("3","FreeSms[mobile]",number)
	fv("3","FreeSms[post_message]",message)
	submit()
	send=input("To stop enter 0, else enter 1 : ")

