#Local modules
import state

def init(self, publicKey, lastBlockHash):
    self.publicKey = str(publicKey)
    self.lastBlockHash = str(lastBlockHash)

def turnHash(self):
    hashData = self.publicKey + self.lastBlockHash
    hashData = hash(hashData).hexdigest()
    return hashData

#def selectWinner():
#    lowestTrunc = None
#    for i in len(peers):
#        if (peers[i].truncValue < peers[i-1].truncValue):
#            lowestTrunc = peers[i]