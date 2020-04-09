import  os

#current working directory

def cwd():
    cwd=os.getcwd()
    print(cwd)

cwd()

#retriving the path of the particular file
#There are two types of path absolute and  relative path
#abs:- Gives the path right from the C drive
#relative path:- Gives the path right from the cwd

def cwd_of_directory(filename):
    path=os.path.abspath(filename)
    print(path)

fileName='sample.txt'
cwd_of_directory(fileName)

#2:- Importing Time

import time

epoch_time=time.time()
print(epoch_time)
#epoch time is after 1970, so when ever we want something we have to change it to this format.

localTime=time.localtime(epoch_time)
print(localTime)
print(localTime.tm_year)
print(time.ctime(epoch_time))


#nextModule SMTP
#Simple Mail transfer protocol

import smtplib
#What domain name and what port number we are using 587 TLS default port number.

smtbObj=smtplib.SMTP('smtp.gmail.com', 587)
smtbObj.ehlo()

#we'll put the smtp in TLS mode
smtbObj.starttls()
#
# smtbObj.login('tejustejus95@gmail.com','Goldenratio1.6180')

from os import path
#Creating a file
def CreateFile(dest):
    if not (path.isfile(dest)): #Checking if the file already exists or not.
        f=open(dest,'w')
        f.write("Welcome to the folder")
        f.close()

dest="C:\\Users\\tejus\\PycharmProjects\\myproject\\MMN-master\sample.txt"

CreateFile(dest)
print("Hello World")
