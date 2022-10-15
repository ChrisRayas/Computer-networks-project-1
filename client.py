import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as q:

    #serverName = "34.125.159.44"
    #serverPort = 22

    #clientSocket = socket(AF_INET, SOCK_STREAM)
    #clientSocket.connect((serverName, serverPort))

    ip_address = input("input IP address: ")
    server_port = int(input("input server port: "))

    q.connect((ip_address, server_port))

    sentence = input('Input lowercase sentence: ')

    q.send(sentence.encode())

 #   q.send(ip_address)
 #   q.send(int(server_port))

    modifiedSentence = q.recv(1024)
    print('From Server: ', modifiedSentence.decode('utf-8'))

    q.close()

