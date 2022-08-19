#!/usr/bin/python3
import os #For getting current dir
import tftpy #Tftp lib will need to be installed with pip
import sys #For getting command args
serverdir = 'placeholder'
serverport = 69
serverip = '0.0.0.0'

#Get directory to serve files from.
if len(sys.argv) != 2:
    serverdir = os.getcwd()
else:
    serverdir = sys.argv[1]

print("Starting TFTP server. Dir:" + serverdir + " IP:" + serverip + " Port:" + str(serverport))

server = tftpy.TftpServer(serverdir) #change as needed
server.listen(serverip, serverport)
