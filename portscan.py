#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(6)

host = input("Please enter the IP")     #IP

port = int(input("Please enter the port")     #Port

def portScanner(port):
   if s.connect_ex((host, port)):
      print("The port is closed")
   else:
      print("The port is open."

portScanner(port)
