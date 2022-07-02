# Imports
from cgitb import handler
import socket
from _thread import *
from threading import Thread
from xmlrpc.client import Server


class Connection(object):
	def __init__(self):
		"""This initilization for 
		""" 
		try:
			self.connection = None
			self.connectionThread =  Thread(target=self.client_handler)
			return
		except Exception as e:
			print (e)
			return
	def start(self):
		"""This initilization for 
		""" 
		try:
			self.connectionThread.start()
			return
		except Exception as e:
			print (e)
			return
	def stop(self):
		try:
			self.connection.close()
			print("Connection closed successfully")
			if self.connectionThread.is_alive():
				self.connectionThread.join()
			print("Connection stopped Closed!") 
			return 
		except Exception as e:
			print("Connection stop error")
			print (e)
			return

	def client_handler(self):
		try:
			self.connection.send(str.encode('You are now connected to the replay server... Type BYE to stop'))
			while True:
				data = self.connection.recv(2048)
				message = data.decode('utf-8')
				if  '__B__' in  message:
					self.stop()
				reply = f'Server: {message}'
				self.connection.sendall(str.encode(reply))
		except BrokenPipeError:
			print ("Broken pip Error Catch")
			self.stop()
		except Exception as e:
			print("Connection handeller error")
			self.stop()
			print (e)
			return

class Server(object):
	def __init__(self):
		"""This initilization for 
		""" 
		try:
			self.handlers = []
			self.host=''
			self.port = 1233
			return
		except Exception as e:
			print (e)
			return
	# Declarations
	#host = '127.0.0.1'


	def accept_connections(self,ServerSocket):
		Client, address = ServerSocket.accept()
		print('Connected to: ' + address[0] + ':' + str(address[1]))
		connectionHandeller = Connection()
		connectionHandeller.connection = Client
		connectionHandeller.start()
		self.handlers.append(connectionHandeller)
		print (str("Connection accepted successfully"))
	def start(self):
		ServerSocket = socket.socket()
		try:
			ServerSocket.bind((self.host,self.port))
		except socket.error as e:
			print(str(e))

		print(f'Server is listing on the port {self.port}...')
		ServerSocket.listen()
	    
		while True:
			self.accept_connections(ServerSocket)







server = Server()
server.start()


'''
	for c in cPids:
		c.close()
	server.stop()
	server.join()

'''