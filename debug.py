import smtpd
import asyncore

server = smtpd.DebuggingServer(('127.0.0.1', 8025), None)

asyncore.loop()
