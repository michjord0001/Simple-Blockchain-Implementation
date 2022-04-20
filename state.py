import time
import pandas 

trnCols = ['trn', 'fromUser', 'toUser', 'trnTime']
balCols = ['user', 'balance', 'lastTrnTime']
transactions = pandas.read_csv('transactions.csv', usecols=trnCols)
balances = pandas.read_csv('balances.csv', usecols=balCols)
userInitials = []

def init():
    transactions = pandas.read_csv('transactions.csv', usecols=trnCols)
    balances = pandas.read_csv('balances.csv', usecols=balCols)

def getTransaction(trn):
    transactions = pandas.read_csv('transactions.csv', usecols=trnCols)
    return(transactions.loc[transactions['trn'] == int(trn)])

def addTransaction(trn, fromUser, toUser, trnTime):
    transactions = pandas.read_csv('transactions.csv', usecols=trnCols)
    dfEntry = pandas.DataFrame({'trn': [trn], 'fromUser': [fromUser], 'toUser': [toUser], 'trnTime': [trnTime]})
    transactions = pandas.concat([transactions, dfEntry])
    transactions.to_csv("transactions.csv", index=False)
    print('Transaction added.')

#def replaceTransaction(trn, fromUser, toUser, trnTime):


#def checkBalance(usr):

def ok_msg():
    print('OK')

def nok_msg():
    print("Not OK")