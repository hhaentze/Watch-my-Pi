#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Creation:    16.08.2013
# Last Update: 07.04.2015
#
# Copyright (c) 2013-2015 by Georg Kainzbauer <http://www.gtkdb.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#

# import required modules
from email.mime.text import MIMEText
import smtplib
import sys
import io

########################################
# declaration of default mail settings #
########################################
#Daten aus .txt Datei laden
path = "/opt/Watch-my-Pi/src/TestEmailData.txt"
emailData = ""
file = open(path, 'r')
emailData = file.read()
if(emailData == ""):
  emailData ="a|b|c"
data_array = emailData.split("|")
file.close()

# mail address of the sender
sender = data_array[0]

# fqdn of the mail server
smtpserver = data_array[1]

# username for the SMTP authentication
smtpusername = data_array[0]

# password for the SMTP authentication
smtppassword = data_array[2]

# use TLS encryption for the connection
usetls = True

########################################
# function to send a mail              #
########################################
def sendmail(recipient,subject,content):

  # generate a RFC 2822 message
  msg = MIMEText(content)
  msg['From'] = sender
  msg['To'] = recipient
  msg['Subject'] = subject

  # open SMTP connection
  server = smtplib.SMTP(smtpserver,587)

  # start TLS encryption
  if usetls:
    server.starttls()

  # login with specified account
  if smtpusername and smtppassword:
    server.login(smtpusername,smtppassword)

  # send generated message
  server.sendmail(sender,recipient,msg.as_string())

  # close SMTP connection
  server.quit()

########################################
# main function                        #
########################################
def main(message,subject):
    # call sendmail() and generate a new mail with specified subject and content
    sendmail(data_array[0],subject,message)
    
if __name__ == '__main__':
  main()

def init():
  file = open(path, 'r')
  emailData = file.read()
  if(emailData == ""):
    emailData ="a|b|c"
  data_array = emailData.split("|")
  file.close()

  # mail address of the sender
  sender = data_array[0]

  # fqdn of the mail server
  smtpserver = data_array[1]

  # username for the SMTP authentication
  smtpusername = data_array[0]

  # password for the SMTP authentication
  smtppassword = data_array[2]

def testMail(sender,smtp,password,subject,content):

  # generate a RFC 2822 message
  msg = MIMEText(content)
  msg['From'] = sender
  msg['To'] = sender
  msg['Subject'] = subject

  # open SMTP connection
  server = smtplib.SMTP(smtp,587)

  # start TLS encryption
  if usetls:
    server.starttls()

  # login with specified account
  if smtpusername and smtppassword:
    server.login(sender,password)

  # send generated message
  server.sendmail(sender,sender,msg.as_string())

  # close SMTP connection
  server.quit()
