import socket
import string
import sys
import argparse
import time

class calendar:
    def __init__(owner):
        self.owner = owner
        self.events = []

class event:
    def __init__(name,start,end):
        self.name = name
        self.start = start
        self.end = end
        self.id = 0
        self.timestamp = 0
        self.flag = "F"

class sync:
    def __init__(self):
        self.serverlist = []
    
    def add_server(self, address_string):
        (ip, port) = address_string.split(":")
        self.serverlist.add((ip, port))
    
    def send_to_all(data):
        for server in self.serverlist:
            break
        return
    

class server:
    def __init__(self):
        self.name = ""
        self.id = tcp_port
        self.lasteventid = 0
        # Open files
        self.file = open("cal." + self.id + ".txt", "r+")
        self.sync = sync()
    
    def create_id(self, data):
       self.lasteventid = self.lasteventid + 1
       data = str(self.id) + "." + str(self.lasteventid) + "," + str(time.time()) + ",F," + data
       return data
    
    def add_event(self, data):
        data = self.create_id(data)
        entry = data.split(",")
        
#        if (entry[3].isalpha() == False):
#            return False

#        try:
#            time.strptime(entry[4], '%H:%M')
#           time.strptime(entry[5], '%H:%M')
        
#        except ValueError:
#            return False
        
        print "event added with id %d.%d" %(self.id,self.lasteventid)
        self.file.seek(0,2)
        self.file.write(data)
        sync.send_to_all("SYNC:" + data)
    
    def remove_event(self, id):
        print "removing event"
        id = id.strip()
        lines = self.file.readlines()
        for i, line in enumerate(lines):
            entry = line.split(",")
#            print(entry)
            if entry[0] == id:
                entry[2] = "X"
                lines[i] = ",".join(entry)
#                print(lines[i])
        self.file.seek(0,0)
        self.file.writelines(lines)

    
    
    def list_events(self, data):
        print "listing events"
        self.file.seek(0,0)
        data = self.file.read()
        return data

def parse_arguments():
    global tcp_port
    tcp_port = 31337
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--tcp_port", type=int, help="node tcp_port: default 9559")
    
    args = parser.parse_args()
    
    if args.tcp_port:
        if args.tcp_port < 1024:
            print "Port should be > 1024"
            exit()
        else:
            tcp_port = args.tcp_port
    print "Local listening tcp_port = %d" %tcp_port


if __name__ == "__main__":
    
    parse_arguments()
    
    server = server()
    
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the tcp_port
    server_address = ('localhost', tcp_port)
    print >>sys.stderr, 'starting up on %s tcp_port %s' % server_address
    sock.bind(server_address)
    
    # Listen for incoming connections
    sock.listen(1)
    
    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()
        
        try:
            print >>sys.stderr, 'connection from', client_address
            
            # Receive and respond
            while True:
                data = connection.recv(65535)
                print >>sys.stderr, 'received "%s"' % data
                if data:
                    if data.startswith("ADD:"):
                        #print "%s: Adding " % thisnode.name
                        server.add_event(data[4:])
                        break
                    if data.startswith("REMOVE:"):
                        #print "%s: Removing " % thisnode.name
                        server.remove_event(data[7:])
                        break
                    if data.startswith("LIST:"):
                        #print "%s: Listing " % thisnode.name
                        connection.sendall(server.list_events(data[5:]))
                        break
                    if data.startswith("SYNC:"):
                        break
                    
                    if data.startswith("HEARTBEAT:"):
                        print "%s: Received hb %s" % (thisnode.name, data)
                        break
                else:
                    print >>sys.stderr, 'no more data from', client_address
                    break
        
        finally:
            # Clean up the connection
            connection.close()
