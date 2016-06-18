!/usr/bin/env python
# -*- coding: utf-8 -*-
#Das ist eine Testeingabe
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

########################################
# declaration of default mail settings #
########################################
# String with requiered data
data = 'PiSpyExtreme@gmail.com|smtp.gmail.com|PiSpyExtreme@gmail.com|JuHaOst16|Your Raspberry Pi can not work anymore. \n\n The world is no place for hardware NOOBS!!!'
data_array = data.split("|")

# mail address of the sender
sender = data_array[0]

# fqdn of the mail server
smtpserver = data_array[1]

# username for the SMTP authentication
smtpusername = data_array[2]

# password for the SMTP authentication
smtppassword = data_array[3]

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
def main():

  # call sendmail() and generate a new mail with specified subject and content
  sendmail('harti.haentze@gmail.com','Raspberry Pi',data_array[4])

  # quit python script
  sys.exit(0)

if __name__ == '__main__':
  main()
