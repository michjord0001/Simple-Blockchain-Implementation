import socket 
import pandas

def loadSeedNodes():
    df = pandas.read_csv('seedNodes.csv', usecols=['IP', 'Port']);
    return(df)

seedNodes = loadSeedNodes()

#Create socket, bind and listen. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((seedNodes.IP[0], seedNodes.Port[0]))
s.listen(10)

#Send messages.
while True:
    clientsocket, address = s.accept()
    print(f"Established connection with {address}.")
    clientsocket.send(bytes("#UprootTheSystem", "utf-8"))
