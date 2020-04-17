# Suraj Ilavala
# Assignment 1: TCP Server
# CMSC 414
##
from socket import *
serverPort = 12002
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print "The server is ready to receive"
while 1:
	print "Waiting ..."
	connectionSocket, addr = serverSocket.accept()
	print "accept"
	sentence = connectionSocket.recv(2048)
	opt = connectionSocket.recv(2048)
	out = ""
	# processes the options according to what the client has chosen
	if("1" in opt):
		# converts the sentence to uppercase
		out = out + "\n1) " + sentence.upper()
	if("2" in opt):
		# converts the sentence to lowercase
		out = out + "\n2) " + sentence.lower()
	if("3" in opt):
		# length of the strings
		out = out + "\n3) " + str(len(sentence))
	if("4" in opt):
		# counts the vowels
		count = 0
		vowels = set("aeiouAEIOU")
		for letter in sentence:
			if letter in vowels:
				count = count + 1
		out = out + "\n4) " + str(count)
	if("5" in opt):
		# counts the words
		words = sentence.split(" ")
		out = out + "\n5) " + str(len(words))
	# sends the results back to the client
	connectionSocket.send(out)
	connectionSocket.close()
