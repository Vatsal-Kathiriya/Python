import string
import random

St = input("Enter the string : ")

Encryption = input("Enter 1 for encryption and 0 for decryption : ")

Encryption = True if (Encryption == "1") else False

# print(Encryption)


if (Encryption):
    
    for i in range(0 , len(St)):
        print(chr(ord(St[i]) + 3) , end = "")
        
else:
    
    for i in range(0 , len(St)):
        print(chr(ord(St[i]) - 3) , end = "")