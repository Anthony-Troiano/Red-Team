#!/usr/bin/env python
import socket
import subprocess
import sys
import ipaddress
from datetime import datetime

# Note: Will only work if the given IP address has a PTR DNS record.

# clear the screen
subprocess.call('clear', shell=True)

# ask for input
HostIP = raw_input("Enter a remote host to scan: ")
remoteIP = socket.gethostbyaddr(HostIP)[2][0]

# print a banner with information on which ip we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteIP
print "-" * 60

# check what time the scan started
t1 = datetime.now()

# scan ports 1-1024
try:
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteIP, port))
		if result = 0:
			print "Port {} \t Open".format(port)
		sock.close()

except KeyboardInterrupt:
	print "You pressed Ctrl+C\n"
	sys.exit()

except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()

except socket.error:
	print 'Couldn't connect to server"
	sys.exit()

# checking time again
t2 = datetime.now()

# calculate the difference of time
total = t2 - t1

# print the information to screen
print "-" * 60
print 'Scanning completed in: ', total
print "-" * 60