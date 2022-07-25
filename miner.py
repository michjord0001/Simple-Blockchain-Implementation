#Local Modules
import block
import transaction
import state

tx_whole = {
    "tx_hash": "",
    "tx_content": "",
    "signature" : "",   
}

def init():
    run()

def run():
    while state.blockCount < 10:
        print("Mining Block #", state.blockCount + 1,"/10")
        block.init()
        block.increaseNonce()
        addTransaction("00", "00")
        state.blockCount += 1

def addTransaction(_fromAccount, _toAccount):
    transaction.init(_fromAccount, _toAccount)
    currHash = transaction.calculateHash() 