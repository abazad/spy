#!/usr/bin/env python
print "Content-Type: text-html"
print
import cgitb
cgitb.enable()
import cgi
import sms
form = cgi.FieldStorage()

sms = sms.Sms(form["rcpt"].value,form["msg"].value)
sms.send()
#sms.close()

