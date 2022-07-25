from tabnanny import check
import time
import pandas 
import sys

currentUser = ''
trnCols = ['trn', 'fromUser', 'toUser', 'trnTime', 'approved', 'approveTrn']
balCols = ['user', 'balance', 'lastTrnTime']
transactions = pandas.read_csv('transactions.csv', usecols=trnCols)
balances = pandas.read_csv('balances.csv', usecols=balCols)
userInitials = []
genesis = ''
consensusMechanism = ''
model = ''
encoding = ''
blockCount = 0
lastHash = '0'

def init():
    transactions = pandas.read_csv('transactions.csv', usecols=trnCols)
    balances = pandas.read_csv('balances.csv', usecols=balCols)

def getTransaction(trn):
    transactions = pandas.read_csv('transactions.csv', usecols=trnCols)
    return(transactions.loc[transactions['trn'] == int(trn)])

def checkBalance(usr):
    balances = pandas.read_csv('balances.csv', usecols=balCols)
    try: 
        userBalance = balances.loc[balances['user'] == usr, 'balance']
        return(int(userBalance))
    except:
        print('User not found:', usr) 
        sys.exit()

def addTransaction(trn, fromUser, toUser, trnTime, approved, approveTrn):
    #Security check
    if (checkBalance(fromUser) < 1):
        print("Insufficient funds")
        sys.exit()

    #Read database
    transactions = pandas.read_csv('transactions.csv', usecols=trnCols)
    balances = pandas.read_csv('balances.csv', usecols=balCols, dtype=object)

    #Edit database
    dfEntry = pandas.DataFrame({'trn': [trn], 'fromUser': [fromUser], 'toUser': [toUser], 'trnTime': [trnTime], 'approved': [approved], 'approveTrn': [approveTrn]})
    transactions = pandas.concat([transactions, dfEntry])
    
    #Transfer without needing approval
    if (approved == '1'):
        balances.loc[balances['user'] == fromUser, balCols] = [fromUser, int(balances.loc[balances['user'] == fromUser, "balance"]) - 1, trnTime]
        balances.loc[balances['user'] == toUser, balCols] = [toUser, int(balances.loc[balances['user'] == toUser, "balance"]) + 1, trnTime]

    #Transfer requiring approval

    #Approval of transfer
    #if (toUser == currentUser):
        

    #Write database
    transactions.to_csv("transactions.csv", index=False)
    balances.to_csv("balances.csv", index=False)

    print('Transaction added.')

#def replaceTransaction(trn, fromUser, toUser, trnTime):

def ok_msg():
    print('OK')

def nok_msg():
    print("Not OK")
