

import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from RSA import generate_keypair,encrypt,decrypt

SERVER_IP    = gethostbyname( 'DE1_SoC' )
PORT_NUMBER = 5000
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )
message='hello'

#first generate the keypair
#get these two numbers from the excel file
p=1297333
q=1297693
###################################your code goes here#####################################
#generate public and private key from the p and q values
pk = generate_keypair(p,q) #RSA Keypairs
public=pk[1] 
private=pk[0]
message=('public_key: %d %d' % (public[0], public[1]))
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER))
while True:
        message=input()
        ###################################your code goes here#####################################
        #message is a string input received from the user, encrypt it with RSA character by character and save in message_encoded
        #message encoded is a list of integer ciphertext values in string format e.g. ['23131','352135','54213513']
        
        for i in message: #loop through message, and send each character through RSA encrytion with private key
             message_encoded=str(encrypt(private,i))
             mySocket.sendto(message_encoded.encode(),(SERVER_IP,PORT_NUMBER))
#[mySocket.sendto(code.encode(),(SERVER_IP,PORT_NUMBER)) for code in message_encoded]
sys.exit()
