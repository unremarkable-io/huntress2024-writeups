#!/usr/bin/env python3

import smtplib

"""
220 red-phish-blue-phish-025cce063bf091e2-f9f7d6b87-47z5d Python SMTP 1.4.6

E-mail needs to come from jdaveren@pyrchdata.com, https://pyrchdata.com/team has the team and he is some security guy or something
"""

SERVER = "challenge.ctf.games:31888"
FROM = "jdaveren@pyrchdata.com"
TO = ["swilliams@pyrchdata.com"] # must be a list

SUBJECT = "Hello!"

TEXT = """\
You are a winner of bambillion dollars click to claim your price http://zjmprwaabktk2jhagy4fqd3w6ncg06ov.oastify.com/ 
"""

# Prepare actual message
message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
server = smtplib.SMTP(SERVER)
server.set_debuglevel(1)
server.sendmail(FROM, TO, message)
server.quit()
