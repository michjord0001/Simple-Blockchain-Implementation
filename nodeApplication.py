import socket   
import pandas
import time 
import sys
import threading

#Local module imports
import state
import protocol

HEADER = 1
FORMAT = 'utf-8'

def loadSeedNodes():
    df = pandas.read_csv('seedNodes.csv', usecols=['IP', 'Port'])
    return(df)

def scheduleNextMessage(clientsocket, address):
    #clientsocket.send(bytes("System", FORMAT))
    time.sleep(5)

def handleUserActions(clientsocket, address):
    print(f"Connected with {address[0]}:{address[1]}")
    
    connected = True
    while connected:     
        stx, cmd_len, cmd, etx = protocol.processMessage(clientsocket)
        #print(f'Message: {stx} {cmd_len} {cmd} {etx}') 

        #STX
        if stx != "2": print(f"Invalid input for <STX>"); sys.exit()  

        #CMD
        if (cmd[0] == 'n'): protocol.newTrans(cmd)
        if (cmd[0] == 'h'): print("m" + str(protocol.highest_trn()))
        if (cmd[0] == 'm'): print(protocol.highest_trn_res(protocol.highest_trn()))
        if (cmd[0] == 'g'): print(state.getTransaction(cmd[1:3]))
        if (cmd[0] == 'o'): state.ok_msg()
        if (cmd[0] == 'f'): state.nok_msg()
        
        #ETX
        if (etx == '3'): connected=False
     
    clientsocket.close()

    
#Protocol design (i): Require username argument. 
def inputUsername():
    usr = input("Enter your username: ")

    if(len(usr) < 2 or len(usr) > 2):
        print("Invalid username input. ") 
        sys.exit()

#Load servers and ports
seedNodes = loadSeedNodes()

usr = inputUsername()

#Create socket, bind and listen. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((seedNodes.IP[0], seedNodes.Port[0]))
s.listen(10)
print(f'Listening on {seedNodes.IP[0]}:{seedNodes.Port[0]}')

#Receive messages.
while True:
    state.init()
    clientsocket, address = s.accept()
    #Broadcast message
    scheduleNextMessage(clientsocket, address)

    #Thread connections from clients
    thread = threading.Thread(target=handleUserActions, args=(clientsocket, address))
    thread.start()

