import time
import pandas 

#def processMessage(data):

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

def highest_trn():
        transactions = pandas.read_csv('transactions.csv', usecols=['trn', 'fromUser', 'toUser', 'trnTime'])
        highestTrn = transactions['trn'].max()
        return highestTrn
