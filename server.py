import socket
import threading
import random


ENCODING = 'utf-8'



def handle_client(conn, addr, quotes, file_handler):

# Here I was using print statements to troubleshoot if my code
# was reaching this point of the code
#    print("goodbye new world")
    
    print("Handling connection from {}".format(addr))
    number = random.randint(0,29)
# Here I was hard-coding the connection variable as I was having issues with it
# establishing a connection with my server as a test run
    conn = '192.168.0.220'
    while conn:
        quote  = quotes[number]
        message = conn.recv(25)
        print(message.decode())

        print("greetings aliens")
        
        if "network" in message.decode():

            print("message is %s", message)
            
            message_to_send = "Hello there " + str(addr) + ". Here is another random quote of wisdom for you:" + quote
            print(message_to_send)
            file_handler.write(message_to_send)
            conn.send(message_to_send.encode())
        break

if __name__ == '__main__':
    with open('quotes.txt', 'r') as f:
        quotes = f.readlines()
    log = open('logfile', 'a')
    #creating a TCP socket
    print("Creating a socket")
     #creating a UDP socket 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    print ("Socket successfully created")
    port = 3389
    server_socket.bind(('', port))        
    print ("socket binded to %s" %(port))
    server_socket.listen(5)    
    print ("socket is listening")

# I was having issues with my client code and my server code communicating with each other,
# so the solution I came up with was to have my server code call and run the client code
# from within itself. That is what this code is accomplishing. It worked in my situation,
# but this line of code probably code not work on any other machine except mine, and thus would
# need to be edited accordingly
    exec(open("C:/Users/craya/OneDrive/Desktop/client.py").read())

    # more print statement troubleshooting
    #print("hello world")
        

    while True:
  # again more print statement troubleshooting
  #      print("mehhhh")

        
        # Here is where I was having the biggest issues with my code. The execution would
        # reach this part of the code and just stopped. No error would show, the program did
        # not terminate on its own, it just stopped. I imagine it was some type of connection
        # issue between it and my actual server. I again tried hard coding the addresses and
        # connections to little success
        connection = '192.168.0.220'
        address = '34.125.159.44'
        # print statement troubleshooting. These statements where made
        # before I hard-coded the variables and wanted to see what they
        # were storing
       # print("connection is %d", address)
       # print("connection is %d", connection)
        print("Received a connection from {}".format(connection))
        thread = threading.Thread(target=handle_client, args=(connection, address, quotes, log))
        thread.start()
