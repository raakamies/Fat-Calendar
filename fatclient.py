import socket
import string
import sys
import argparse
import time

class client:
	def _init_ (self)
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#Server address
		serverip
		serverport
		eventlist = []
		self.file = open("config.txt", "r+")

	def create_event (self, data):
		entry = data.split(",")
		new_event = event(entry[3],entry[4], entry[5], entry[6])
		new_event.id = entry[0]
		new_event.timestamp = entry[1]
		new_event.flag = entry[2]
		self.eventlist.append(new_event)

	def attach_note(self, event)
		event.content = raw_input()
		send_event(event)
		
	def send_event(self, event):
		owner = event.owner
		name = event.name
		start = event.start
		end = event.end
		content = event.content
		id = event.id
		timestamp = event.timestamp
		flag = event.flag
		data = "%d,%d,%c,%s,%s,%s,%s,%s" % (id, timestamp, flag, owner, name, start, end, content)
		self.sock.sendto(data,(servip, servport)) 
		

class event:
	def _init_ (self, owner, name, start, end)
		owner = self.owner
		name = self.name
		start = self.start
		end = self.end
		content = NULL
		id = 0
		timestamp = 0
		flag = "F"
		
	

if __name__ == "__main__":
	parse_arguments()
		global tcp_port
		tcp_port = 
	print "Welcome to Fat Calendar"
	
	'''	
	def edit_event(self, id):
		for event in self.eventlist:
			if event.id == id:
				#ask client, what to edit
				edit = raw_input('What do you want to edit? (n,t,c): ')
			
				if (edit == 'n'):
					#edit name
					event.name = raw_input('Enter new name: ')
	
				if (edit 't'):
					#edit time
					event.start = raw_input('Enter new startimg time (hh:mm): ')
					event.end = raw_input('Enter new ending time (hh:mm): ')
		
				if (edit == 'c'):
					#edit content
					event.content = raw_input('Enter new content: ')
	
				#Send edited event to server
				
				send_event(event)
			
				break
'''

	



	


		
	
		
