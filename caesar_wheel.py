"""Caesar_wheel.py

	Author : Vishnu Ashok 
	Contact : thisisvishnuashok@hotmail.com
			  thisisvishnuashok@gmail.com
			  
	This is a cipher that was used by Julius Caesar two thousand years ago. The good news is that it is simple and easy to learn. The bad news is that because it is so simple, it is also easy for a cryptanalyst to break it. But we can use it just as a simple learning exercise. The Caesar Cipher is also explained on Wikipedia here : 
http://en.wikipedia.org/wiki/Caesar_cipher

"""

# Pyperclip is a cross-platform clipboard module for Python.

import pyperclip

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha = list(alpha)

def main():
    ch = "0"
    while ch not in "123":
        print "\n\n======================"
        print "CAESAR'S CIPHER WHEEL"
        print "======================\n\n"
        print "1.Encode\n2.Decode\n3.Exit\n"
        ch = raw_input("Enter your choice : ")
        if ch == "1":
            encode()
        elif ch == "2":
            decode()
        elif ch == "3":
            exit()
        else:
            print "\n" * 3



def encode():

    msg = raw_input("Enter your message : ")
    key = int(raw_input("Enter your key : "))
    new = []
    
    i = 0
    while(i < len(msg)):
        if msg[i] == " ":
            new.append(" ")
        else:
            temp = alpha.index(msg[i])
            temp = temp + key
            if temp > 25:
                temp = temp - 25
            new.append(alpha[temp])
        i = i + 1
    encoded = "".join(new)
    print "Encoded message : " + encoded
    print "\n1. Copy to clipboard"
    print "Press any other key to continue"
    ch = raw_input("> ")
    if ch == "1":
        pyperclip.copy(encoded)
    


def decode():

    msg = raw_input("Enter your message : ")
    key = int(raw_input("Enter your key : "))
    new = []
    
    i = 0
    while(i < len(msg)):
        if msg[i] == " ":
            new.append(" ")
        else:
            temp = alpha.index(msg[i])
            temp = temp - key
            if temp < 0:
                temp = temp + 25
            new.append(alpha[temp])
        i = i + 1
    decoded = "".join(new)
    print "Decoded message : " + decoded
    print "\n1. Copy to clipboard"
    print "Press any other key to continue"
    ch = raw_input("> ")
    if ch == "1":
        pyperclip.copy(decoded)
    
    
if __name__ == "__main__":
    main()
