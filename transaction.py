#External Modules
import json
import hashlib

#Local Modules
import protocol

tx_content = {
    "fromAccount": "",
    "toAccount": ""
}

def init(_fromAccount, _toAccount):
    tx_content['fromAccount'] = _fromAccount
    tx_content['toAccount'] = _toAccount
    return tx_content

def newTrans(_fromAccount, _toAccount):
    tx_content['fromAccount'] = _fromAccount
    tx_content['toAccount'] = _toAccount
    #protocol.newTrans(cmd)
    return tx_content 

def calculateHash():
    tx_payload = json.dumps(tx_content)
    tx_hash = hashlib.sha256(tx_payload.encode('utf-8')).hexdigest()
    return tx_hash