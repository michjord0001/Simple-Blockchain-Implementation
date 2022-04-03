import socket   
import pandas
import time 
import sys
import threading
#import getopt

HEADER = 1
FORMAT = 'utf-8'

def loadSeedNodes():
    df = pandas.read_csv('seedNodes.csv', usecols=['IP', 'Port'])
    return(df)

def scheduleNextMessage(clientsocket, address):
    clientsocket.send(bytes("System", FORMAT))
    time.sleep(5)

def handleUserActions(clientsocket, address):
    print(f"Connected with {address[0]}:{address[1]}")
    
    connected = True
    while connected:
        try:
            stx = clientsocket.recv(HEADER).decode(FORMAT)
            cmd_len = clientsocket.recv(HEADER).decode(FORMAT)
            cmd = clientsocket.recv(int(cmd_len)).decode(FORMAT)
            etx = clientsocket.recv(HEADER).decode(FORMAT) 
            #msg = clientsocket.recv(HEADER).decode(FORMAT)
            #msgList = msg.split()              
            #stx = str(msgList[0])
            #cmd_len = str(msgList[1])
            #cmd = str(msgList[2])
            #etx = str(msgList[3])       
        except:
            print("Error interpretting message protocol.")
            sys.exit()   
            
        print(f'Message: {stx} {cmd_len} {cmd} {etx}')

        if stx != "2": print(f"Invalid input for <STX>"); sys.exit()  
                
        #Insert switch statement for cmd

        if (etx == '3'): connected = False
    clientsocket.close()

#Protocol design (i): Require username argument. 
def verifyInput():
    if(len(sys.argv) < 2):
        print("Require username argument.") 
        sys.exit()
    if(len(sys.argv[1]) > 2):
        print("Invalid username length.") 
        sys.exit()

#Load servers and ports
seedNodes = loadSeedNodes()

#Create socket, bind and listen. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((seedNodes.IP[0], seedNodes.Port[0]))
s.listen(10)
print(f'Listening on {seedNodes.IP[0]}:{seedNodes.Port[0]}')

#Receive messages.
while True:
    verifyInput()
    clientsocket, address = s.accept()
    #Broadcast message
    scheduleNextMessage(clientsocket, address)

    #Thread connections from clients
    thread = threading.Thread(target=handleUserActions, args=(clientsocket, address))
    thread.start()


