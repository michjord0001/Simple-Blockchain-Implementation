#External Modules
import time
import pandas 
import sys
#from weakref import finalize

#Local Modules
import state
HEADER = 1
FORMAT = 'utf-8'

def newTrans(cmd):
        try:
                trn = highest_trn() + 1
                fromUser = cmd[1:3]
                toUser = cmd[3:5]
                trnTime = time.time()
                approved = cmd[5]
                approveTrn = cmd[6:8]
                state.addTransaction(trn, fromUser, toUser, trnTime, approved, approveTrn)
                state.ok_msg()
        except:
                print("Error adding new transaction.")
                state.nok_msg() 

def highest_trn():
        transactions = pandas.read_csv('transactions.csv', usecols=['trn', 'fromUser', 'toUser', 'trnTime'])
        highestTrn = transactions['trn'].max()
        return highestTrn

def highest_trn_res(trn):
        try:
                highestTrn = int(highest_trn())
                return highestTrn.to_bytes(2, byteorder='big')
        except:
                print("Error encoding highest_trn")

def processMessage(clientsocket):
        try:
                stx = clientsocket.recv(HEADER).decode(FORMAT)
                cmd_len = int.from_bytes(clientsocket.recv(HEADER), byteorder='big')
                cmd = clientsocket.recv(cmd_len).decode(FORMAT)
                etx = clientsocket.recv(HEADER).decode(FORMAT)
        except:
                print("Error interpretting message protocol.")
                sys.exit()   
                        
        #print(f'Message: {stx} {cmd_len} {cmd} {etx}')

        return stx,cmd_len,cmd,etx

'''
def createMessage(message):
        #calculate message length
        msg_length = len(message)

        msg = bytearray()
        msg.append(2)
        msg.append(msg_length)
        msg += message
        msg.append(3)

        return msg 
'''