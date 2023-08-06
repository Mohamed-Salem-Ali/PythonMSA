import socket, threading, ipaddress                                                #Libraries import

host = '127.0.0.1'                                                      #LocalHost
port = 7977                                                             #Choosing unreserved port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              #socket initialization
server.bind((host, port))                                               #binding host and port to socket
server.listen()

print("Server is now booted up and is waiting for any client to connect")
netmask = '255.255.255.0'
# Netmask is to decode network and host addresses
def get_broadcast_ip():
    ip = socket.gethostbyname(socket.gethostname()) # Obtain your IP address
    net = ipaddress.IPv4Network(ip + '/' + netmask, False)
    broadcast = str(net.broadcast_address)
    print('My broadcast address =', broadcast)
    return broadcast
    
clients = []
nicknames = []
hostnames =[]
def broadcast_message():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(hostname)
    print(local_ip)

def broadcast( message ):
    broadcast_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    broadcast_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# Enable broadcasting mode
    broadcast_server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
    broadcast_server.settimeout(0.2)
    broadcast_server.sendto( message, ('<broadcast>', port))
    print("message sent!")
    
                        

def sendActiveClients( client ):
    string = ''
    count = 1
    for addr in hostnames:
        string+= str(count)
        string+= "- "
        string+= str(addr)
        string+='\n'
        count+=1
    print(string)
    client.send(string.encode('ascii'))
    
def handle( client ):                                         
    while True:
        try:
            menu = "1- Print All Connected Users \n2- Send Message To specific User \n3- Send message to all Users"
            client.send( menu.encode('ascii') )                                                            #recieving valid messages from client
            choice = client.recv(1024)
            print(choice)
            if( choice.decode('ascii') == '1' ):
                sendActiveClients(client)
            elif( choice.decode('ascii') == '2'):
                sendActiveClients(client)
                client.send("Enter your user number".encode('ascii'))
                choice = client.recv(1024)
                choice = choice.decode('ascii')
                choice = int(choice)
                print(choice)
                if ( choice > 0 and choice <= len(clients) ):
                    client.send("Enter your message".encode('ascii'))
                    message = client.recv(1024)
                    clients[choice - 1].send(message)
                else:
                    client.send("Error please enter valid user number".encode('ascii'))
            elif( choice.decode('ascii') == '3'):
                client.send( "Enter your message".encode('ascii') )
                message = client.recv(1024)
                broadcast(message)
            else :
                client.send("Error please enter valid choice".encode('ascii'))
        except:                                                         #removing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            addr = hostnames[index]
            hostnames.remove(addr)
            break

def receive():                                                          #accepting multiple clients
    while True:
        get_broadcast_ip()
        client, addr = server.accept()
        hostname = socket.gethostbyaddr(addr[0])
        print("Connected with {}".format(str(addr)))       
        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        hostnames.append(hostname)
        clients.append(client)
        print("Nickname is {}".format(nickname))
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
