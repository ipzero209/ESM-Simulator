#!/usr/bin/python

from threading import Thread
import socket
from datetime import datetime
from time import sleep
import random
import xml.etree.ElementTree as et


def genTStamp():
	date_string = str(datetime.now())
	date_string = "T".join(date_string.split())
	date_string = date_string[:-4]
	date_string = date_string + "Z"
	return date_string

def genTime():
	tstamp = '{:%b %d %Y %H:%M:%S}'.format(datetime.now())
	return tstamp


def sendLog(c_hash, c_user, machine):
	logstring = "<134> 1 {0} WIN-CAURRM4ONJ2 - - - {4},Traps Agent,3.4.1.15678,Threat,Prevention Event,{1},{2},New prevention event. Prevention Key: 1acabebe-833a-41e4-80a9-421923443eb9,6,Wildfire,myapp.exe,{3},[\"ContentVersion\"],,,".format(genTStamp(), machine, c_user, c_hash, genTime())
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('10.3.4.48', 23001))
	sock.send(logstring)
	print "Sent:\n\n" + logstring


users = []
source = et.parse('mappings.xml')
source_root = source.getroot()

elements = source_root.findall('./payload/login/*')
for entry in elements:
	users.append(entry.attrib['name'])


while True:
	t_user = random.choice(users)
	t_hash = random.choice(open('hashes.txt').readlines()).rstrip('\n')
	t_machine = random.choice(open('machines.txt').readlines()).rstrip('\n')
	send_thread = Thread(target=sendLog, args=(t_hash, t_user, t_machine))
	send_thread.start()
	sleep(1800)	

# for user in users:
# 	t_hash = random.choice(open('hashes.txt').readlines()).rstrip('\n')
# 	t_machine = random.choice(open('machines.txt').readlines()).rstrip('\n')
# 	send_thread = Thread(target=sendLog, args=(t_hash, user, t_machine))
# 	send_thread.start()
# 	sleep(5)

