# Suraj Ilavala
# Assignment 1: TCP Client
# CMSC 414
##
from socket import *
serverName = 'localhost'
serverPort = 12002

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
# This is where the sentence is formed and the options chosen are sent to the server
sentence = raw_input('Sentence: ')
print "What would you like to do?"
print "1) Convert to uppercase"
print "2) Convert to lowercase"
print "3) Length of String"
print "4) Count vowels"
print "5) Count words"
opt = raw_input('Options: ')
# Sends sentence and options
clientSocket.send(sentence)
clientSocket.send(opt)
# recieves the results from the server and prints it
modifiedSentence = clientSocket.recvfrom(2048)

print modifiedSentence[0]
clientSocket.close()
