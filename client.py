import socket
import pandas

def loadSeedNodes():
    df = pandas.read_csv('seedNodes.csv', usecols=['IP', 'Port']);
    return(df)

seedNodes = loadSeedNodes()

#Connect to socket. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((seedNodes.IP[0], seedNodes.Port[0]))

#Receive messages. 
data, addr = s.recvfrom(1024)
print("Message [" + data.decode("utf-8") + "] from [" + str(seedNodes.IP[0]) + "]:[" + str(seedNodes.Port[0]) + "]")
