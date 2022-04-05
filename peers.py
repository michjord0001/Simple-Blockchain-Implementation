import socket
import pandas

FORMAT = "utf-8"

def loadSeedNodes():
    df = pandas.read_csv('seedNodes.csv', usecols=['IP', 'Port']);
    return(df)

#def discoverOtherNodes():

def broadcastMessage(message):
    stx = ascii(2).encode(FORMAT) #Encode Start Transaction
    cmd = message.encode(FORMAT) #Encode command.
    cmd_len = len(cmd).to_bytes(1, byteorder='big') #Convert length of encoded command into bytes.
    etx = ascii(3).encode(FORMAT) #Encode End Transaction
    s.send(stx)
    s.send(cmd_len)
    s.send(cmd)
    s.send(etx)
    #msg = bytearray(stx, cmd_len, cmd, etx)
    #s.send(msg)

def processIncomingMessages():
    data, addr = s.recvfrom(1024)
    print("Message [" + data.decode("utf-8") + "] from [" + str(seedNodes.IP[0]) + "]:[" + str(seedNodes.Port[0]) + "]")

#Load servers and ports
seedNodes = loadSeedNodes()

#Connect to socket. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((seedNodes.IP[0], seedNodes.Port[0]))

#processIncomingMessages()
broadcastMessage("h")

