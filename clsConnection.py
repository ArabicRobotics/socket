# Imports
from cgitb import handler
import socket
from _thread import *
from threading import Thread
#from xmlrpc.client import Server
import time

class Connection(object):
	def __init__(self):
		"""This initilization for 
		""" 
		try:
			self.isConnected = False
			self.isTirmenated = False
			self.connection = None
			self.connectionThread =  Thread(target=self.client_handler)
			self.connectionThread.daemon=  True # first
			return
		except Exception as e:
			print (e)
			return
	def start(self):
		"""This initilization for 
		""" 
		try:
			self.isConnected = True
			self.connectionThread.start()
			return
		except Exception as e:
			print (e)
			return
	def stop(self):
		try:
			self.isConnected = False
			self.connection.shutdown(socket.SHUT_RDWR)
			self.connection.close()
			self.isTirmenated =True
			time.sleep(0.3)
			#Server.removeConnection(self)
			print("Connection closed successfully")
			#print("Connection stopped Closed!") 
			return 
		except Exception as e:
			self.isConnected =False
			print("Connection stop error")
			print (e)
			return

	def client_handler(self):
		try:
			self.connection.send(str.encode('You are now connected to the replay server... Type BYE to stop'))
			while True:
				if self.isTirmenated:
					self.stop();
					return
				data = self.connection.recv(2048)
				message = data.decode('utf-8')
				if len(data)>0:
					self.read(message)					
				#reply = f'Server: {message}'
					#self.send(message)
				if not data:
					self.stop()
		except BrokenPipeError:
			print ("Broken pip Error Catch")
			self.stop()
		except Exception as e:
			print("Connection handeller error")
			self.stop()
			print (e)
			return


	def send(self,data):
		try:
			self.connection.sendall(str.encode(data))
			
			return
		except Exception as e:
			print("Error in send ")
			self.stop()
			print (e)
			return

	def read(self,data):
		try:
			print ("read :"+ str(data))
			
			if  '__B__' in  data:
				self.stop()
			if '__status__' in data:
				self.send("Connected")
			return
		except Exception as e:
			print("Error in read ")
			self.stop()
			print (e)
			return
