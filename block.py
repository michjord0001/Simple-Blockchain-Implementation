#External Modules
import time
import json 
import hashlib

#Local Modules
import transaction
import state

FORMAT = 'utf-8'

hashedContent = {
    "prevHash": "",
    "nonce": "",
    "timestamp": "",
    "transactions": ""
}

currHash = '0'

def init():
    hashedContent["prevHash"] = 0
    hashedContent["nonce"] = 0
    hashedContent["timestamp"] = int(time.time())
    hashedContent["transactions"] = transaction.init("00", "00")

def increaseNonce():
    timeStart = int(time.time()*1000) #Milliseconds
    nonce = 0
    nonceFound = False
    hashedContent["prevHash"] = state.lastHash
    while nonceFound == False:
        #Update content
        hashedContent["nonce"] = nonce
        hashedContent["timestamp"] = int(time.time()*1000)
        hashedPayload = json.dumps(hashedContent)

        #Calculate Hash
        currHash = calculateHash(hashedPayload)
        
        #Estimate ~10 seconds block time
        if currHash[:5] == "00000":
            nonceFound = True
        else:
            nonce += 1
    hashedContent["nonce"] = nonce
    timeEnd = int(time.time()*1000)
    state.lastHash = currHash

    print("prevHash: ", hashedContent["prevHash"])
    print("hashedContent: ", hashedContent)
    print("currHash: ", currHash)

def calculateHash(_hashedPayload):
    return hashlib.sha256(_hashedPayload.encode(FORMAT)).hexdigest() 

