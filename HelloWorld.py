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

########################################
# declaration of default mail settings #
########################################
# mail address of the sender
sender = 'PiSpyExtreme@gmail.com'

# fqdn of the mail server
smtpserver = 'smtp.gmail.com'

# username for the SMTP authentication
smtpusername = 'PiSpyExtreme@gmail.com'

# password for the SMTP authentication
smtppassword = 'JuHaOst16'

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
  sendmail('harti.haentze@gmail.com','Test','Dies ist eine Testnachricht.')

  # quit python script
  sys.exit(0)

if __name__ == '__main__':
  main()
