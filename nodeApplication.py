#External Modules
import socket   
import pandas
import time 
import sys
import threading

#Local Modules
import state
import protocol
import wallet
import miner 

HEADER = 1
FORMAT = 'utf-8'

def init():
    state.init()
    wallet.init()
#    miner.init()

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
        if (cmd[0] == 'c'): print("{\'blocks\':",state.blockCount,"}")
        if (cmd[0] == 'f'): state.nok_msg()
        if (cmd[0] == 'g'): print(state.getTransaction(cmd[1:3]))
        if (cmd[0] == 'h'): print(str(protocol.highest_trn()))
        if (cmd[0] == 'm'): print(protocol.highest_trn_res(protocol.highest_trn()))
        if (cmd[0] == 'n'): protocol.newTrans(cmd)
        if (cmd[0] == 'o'): state.ok_msg()
        
        #ETX
        if (etx == '3'): connected=False
     
    clientsocket.close()

    
#Protocol design (i): Require username argument. 
def inputUsername():
    state.currentUser = input("Enter your username ('00' = Genesis): ")

    if(len(state.currentUser) < 2 or len(state.currentUser) > 2):
        print("Invalid username input. ") 
        sys.exit()

def selectConfiguration():
    #Questions
    state.genesis = input("Create new genesis block(s)? (y/n): ")
    if (state.genesis == 'y'):
        miner.init()
    state.consensusMechanism = input("Enter preferred Consensus Mechanism (\"pow\" or \"pos\"): ")
    state.model = input("Enter preferred Model \"db\" or \"utxo\"): ")
    state.encoding = input("Enter preferred encoding method (\"json\" or \"byte\"): ")

selectConfiguration()

#Load servers and ports
seedNodes = loadSeedNodes()

#Create socket, bind and listen. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((seedNodes.IP[0], seedNodes.Port[0]))
s.listen(10)
print(f'Listening on {seedNodes.IP[0]}:{seedNodes.Port[0]}')

#Receive messages.
while True:
    init()
    clientsocket, address = s.accept()

    #Broadcast message
    scheduleNextMessage(clientsocket, address)

    #Thread connections from clients
    thread1 = threading.Thread(target=handleUserActions, args=(clientsocket, address))
    #thread2 = threading.Thread(target=handleUserActions, args=(clientsocket, address))
    #thread3 = threading.Thread(target=handleUserActions, args=(clientsocket, address))
    #thread4 = threading.Thread(target=handleUserActions, args=(clientsocket, address))
    
    thread1.start()
    #thread2.start()
    #thread3.start()
    #thread4.start()
