from operator import truediv
import socket
from threading import Thread
import time
class Client(object):
	def __init__(self):
		"""This initilization for 
		""" 
		try:
			self.host = ''
			self.port = 1233
			self.isConnected = False
			self.ClientSocket = socket.socket()
			self.threadReceive = Thread(target=self._receive)
			self.threadReceive.daemon = True
			self.newData = False
			self.lastRead=None
			self.isTirmenated = None
			return
		except Exception as e:
			print (e)
			return
	def Methood(self):
		"""This initilization for 
		""" 
		try:
			return
		except Exception as e:
			print (e)
			return

	def connect(self,host='',port=1233):
		"""This initilization for 
		""" 
		try:
			self.port = port
			self.host = host
			self.ClientSocket.connect((host, port))
			self.isConnected = True
			self.isTirmenated = False
			self.threadReceive.start()
		except socket.error as e:
			print(str(e))
		except Exception as e:
			print (e)
			return

	def send(self,data):
		try:
			if self.isConnected ==False:
				return False 
			if self.isTirmenated:
				return False
			self.ClientSocket.send(str.encode(data))
			return True
		except Exception as e:
			print (e)
			return

	def read(self):
		try:
			if self.newData:
				self.newData = False
				return self.lastRead
			else:
				return
		except Exception as e:
			print (e)
			return




	def _receive(self):
		try:
			while True:
				self.Response = None

				self.Response = self.ClientSocket.recv(1024)				
				if self.Response != None:
					self.Response = self.Response.decode('utf-8')
					self.newData = True
					self.lastRead = self.Response
				if self.isTirmenated:
					break
			return 
		except Exception as e:
			print (e)
			return

	def stop(self):
		try:
			self.isTirmenated = True
			time.sleep(0.2)
			self.ClientSocket.shutdown(socket.SHUT_RDWR)
			self.ClientSocket.close()
			self.threadReceive.join()
			return
		except Exception as e:
			print (e)
			return		

client = Client()
client.connect()
time.sleep(0.5)
while True:
	message = input("Enter Message ...")
	if client.send(message)==False:
		print("sending failed")
		break
	time.sleep(1)
	if message =="bye":
		client.stop()
	print (client.read())
