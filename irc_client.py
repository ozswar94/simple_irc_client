#! /bin/usr/env python3

import socket
import time

class Irc_Client:
	
	"""
	Classe Irc_Client, connect irc server, send private message, join channel ect..

	"""
	port = 6667
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def __init__(self, server, username, hostname, realname):
		self.server = server
		self.username = username
		self.hostname = hostname
		self.realname = realname
		self.sock.connect((self.server, self.port))

	def connect_server(self, nick):
		self.sock.sendall(bytes('NICK'+' '+nick+'\r\n','utf-8'))
		self.sock.sendall(bytes('USER'+' '+self.username+' '+self.hostname+' '+self.server+' :'+self.realname+'\r\n', 'utf-8'))
		time.sleep(3)
		print('Connect :')
		rep = self.sock.recv(4096 * 5)
		print(rep.decode())

	def send_pmsg(self,user,message):
		self.sock.sendall(bytes('PRIVMSG '+user+' :'+message+'\r\n', 'utf-8'))
		time.sleep(0.5)
		rep = self.sock.recv(2048)
		rep = rep.decode()
		rep = rep.split(':')
		rep = rep[-1:]
		rep = ' '.join(rep)
		return rep

	def join_channel(self,channel):
		self.sock.sendall(bytes('JOIN '+channel+'\r\n', 'utf-8'))
		print('Join :')
		rep = self.sock.recv(2048)
		print(rep.decode())

	def quit(self):
		self.sock.sendall(bytes('Quit :A+\r\n', 'utf-8'))
		rep = self.sock.recv(2048)
		print(rep.decode())
