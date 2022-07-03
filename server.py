# Imports
from cgitb import handler
import socket
from _thread import *
from threading import Thread
from xmlrpc.client import Server
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
			self.connection.close()
			self.isTirmenated =True
			time.sleep(0.3)
			Server.removeConnection(self)
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
	handlers = []	
	def __init__(self):
		"""This initilization for 
		""" 
		try:
			self.host=''
			self.port = 1233
			self.isTirmenated= None
			self.threadServer = Thread(target=self._start)
			self.isRunning = False
			return
		except Exception as e:
			print (e)
			return
	# Declarations
	#host = '127.0.0.1'

	def accept_connections(self):
		try:
			Client, address = self.ServerSocket.accept()
			print('Connected to: ' + address[0] + ':' + str(address[1]))
			connectionHandeller = Connection()
			connectionHandeller.connection = Client
			connectionHandeller.start()
			Server.handlers.append(connectionHandeller)
			print (str("Connection accepted successfully"))
			return
		except Exception as e:
			print (e)
			return
	def removeConnection(connection):
		try:
			Server.handlers.remove(connection)
  				# Do something
		except Exception as e:
			print (e)
			return


	def start(self):
		try:
			self.threadServer.start()
			return
		except Exception as e:
			print (e)
			return

	def shutDown (self):
		try:
			print("start shutdown ")
			for i in range(len(Server.handlers)):
				cConnection = Server.handlers[i]
				if cConnection.isConnected:
					cConnection.connection.close()
			print("server socket closing...")
			self.ServerSocket.shutdown(1)
			print ("threading join")
			self.isTirmenated=True 
			self.ServerSocket.close()
			#self.threadServer.daemon = True
			self.threadServer.join(timeout=0.5)
			print("threadign JOINDED..")
			time.sleep(0.3)
			return
		except Exception as e:
			print("Error in Server Shutdown")
			
			self.ServerSocket.close()
			print (e)
			return

	def _start(self):
		self.ServerSocket = socket.socket()
		try:
			self.ServerSocket.bind((self.host,self.port))
		except socket.error as e:
			print(str(e))
			print ("problem In  socket ")
			self.shutDown()
			return False
		try:
			print(f'Server is listing on the port {self.port}...')
			self.ServerSocket.listen()
			self.isRunning = True		    
			while True:
				self.accept_connections()
				if self.isTirmenated:
					print("terminated ")
					self.ServerSocket.close()
					break
		except Exception as e:
			print (e)
			return

	def getStatus():
		try:
			print ("Total connections : " + str(len(Server.handlers)))
			for i in range(len(Server.handlers)):
				cConnection = Server.handlers[i]
				print_no_newline(str(i)+ ":Connected  "+ str(cConnection.isConnected))
				print_no_newline(" Tirmenated : "+ str(cConnection.isTirmenated))
				print("")
			print ("End Printing ")
		except Exception as e:
			print (e)
			#Server.handlers.remove(cConnection)
			return



def print_no_newline(string):
    import sys
    sys.stdout.write(string)
    sys.stdout.flush()



server = Server()
timeout=15
server.start()



print ("printing status:")
Server.getStatus()
time.sleep(timeout)
print ("printing status:")
Server.getStatus()
time.sleep(timeout)
print ("printing status:")
Server.getStatus()
print ("---- working .... half way ")
time.sleep(timeout)
print ("printing status:")
Server.getStatus()
time.sleep(timeout)
print ("printing status:")
Server.getStatus()
time.sleep(timeout)
print ("printing status:")
Server.getStatus()
time.sleep(timeout)




'''
#server.shutDown()
'''
print ("Finished............ ")

'''
	for c in cPids:
		c.close()
	server.stop()
	server.join()

'''