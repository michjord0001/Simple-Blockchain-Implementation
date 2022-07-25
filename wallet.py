#External Modules
import json
import ecdsa
from ecdsa import SigningKey
import hashlib

#Local Modules
import state
import block

FORMAT = 'utf-8'

def init():
    #Private Key
    sk = SigningKey.generate() # uses NIST192p
    privateKey = sk.to_pem() #Byte format

def checkBalance(usr):
    state.checkBalance(usr)
    
def getPublicKey():
    #Private Key
    sk = SigningKey.generate() # uses NIST192p
    privateKey = sk.to_pem() #Byte format

    #Public Key
    vk = sk.verifying_key
    publicKey = vk.to_pem() #Byte format
    return publicKey        

def sign(sk):
    block.tx_whole["tx_hash"] = block.currHash
    block.tx_whole["tx_content"] = block.hashedContent.encode(FORMAT).hex()
    block.tx_whole["signature"] = signature.hex()

    signature = sk.sign(block.hashedContent.encode(FORMAT)).hex()

def verify(sk):
    vk = sk.verifying_key
    public_key = vk.to_pem() #Byte format

    try:
        vk.verify(block.tx_whole["signature"], block.hashedContent.encode('utf-8'))
        print("Good signature.")
    except:
        print('Bad signature')
