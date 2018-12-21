import sys
from random import randint


dict_vigenere = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26}


#CAESAR CIPHER
def caesar():
    while True:
        try:
            choice = int(input("Welcome to Caesar cipher program\nPlease select number of preferable action: \n1)Cipher text\n2)Decipher text\n3)Exit the program\n"))
            
            if choice not in [1,2,3]:
                print("Please select a number between 1 and 3")
                while choice not in [1,2,3]:
                    choice = int(input("Welcome to Caesar cipher program\nPlease select number of preferable action: \n1)Cipher text\n2)Decipher text\n3)Exit the program\n"))
            break
        except ValueError:
            print("Please enter a number")
            
        
    #if user wants to exit
    if (choice == 3):
        sys.exit()
        
    text = input("Enter the text: ")
    
    while True:
        try:
            key = int(input("Enter the key "))
            break
        except ValueError:
            print("The key in Caesar Cipher must be an integer")
            
    
    newString = ""
    key = key % 26
    

    #cipher
    if choice == 1:
        for i in text:
            if i.isalpha():
                tmp = i
                #for uppercase
                if i.isupper():
                    if ord(tmp) + key > 90:
                        tmp = chr(64 + (key - (90 - ord(tmp) ) ) )
                #for lowecase
                if i.islower():
                    if ord(tmp) + key > 122:
                        tmp = chr(96 + (key - (122 - ord(tmp) ) ) )
                    else:
                        tmp = chr(ord(tmp) + key)
                
                i = tmp
            newString += i
            
            
            
        print("ciphered text: ", newString)
        
    #decipher    
    if choice == 2:
        for i in text:
            if i.isalpha():
                tmp = i
                #for uppercase
                if i.isupper():
                    if ord(tmp) - key < 65:
                        tmp = chr(91 - (key - (ord(tmp) - 65 ) ) )
                    else:
                        tmp = chr(ord(tmp) - key)
                #for lowecase
                if i.islower():
                    if ord(tmp) - key < 97:
                        tmp = chr(123 - (key - (ord(tmp) - 97 ) ) )
                    else:
                        tmp = chr(ord(tmp) - key)
                
                i = tmp
            newString += i
            
            
            
        print("deciphered text: ", newString)










    
#VIGENERE CIPHER

def validateVigenereKey(key):
    validKey = True

    for i in key:
        if i.isalpha or i == " ":
            continue
        else:
            validKey = False
            break

    return validKey


def vigenere():
    while True:
        try:
            choice = int(input("Welcome to Vigenere cipher program\nPlease select number of preferable action: \n1)Cipher text\n2)Decipher text\n3)Exit the program\n"))
            
            if choice not in [1,2,3]:
                print("Please select a number between 1 and 3")
                while choice not in [1,2,3]:
                    choice = int(input("Welcome to Vigenere cipher program\nPlease select number of preferable action: \n1)Cipher text\n2)Decipher text\n3)Exit the program\n"))
            break
        except ValueError:
            print("Please enter a number")
                    

    #if user wants to exit
    if (choice == 3):
        sys.exit()
        
    text = input("Enter the text: ")

    key = input("Enter the key: ")

    #key validation

    
    if not validateVigenereKey(key):
        while not validateVigenereKey(key):
            print("The key in Vigenere cipher must only contain alphabetical characters!!!")
            key = input("Enter the key: ")


    keyLength = len(key)
    newString = ""

    #inner counter
    j = 0

    #cipher
    if choice == 1:
        for i in text:
            if i.isalpha():
                #check for space non alphabetical character in key
                if not key[j].isalpha():
                    while not key[j].isalpha():
                        j+=1
                        if j == keyLength:
                            j=0
                tmp = i
                #for uppercase
                if i.isupper():
                    if ord(tmp) + dict_vigenere[key[j].lower()] > 90:
                        tmp = chr(64 + (dict_vigenere[key[j].lower()] - (90 - ord(tmp) ) ) )
                #for lowecase
                if i.islower():
                    if ord(tmp) + dict_vigenere[key[j].lower()] > 122:
                        tmp = chr(96 + (dict_vigenere[key[j].lower()] - (122 - ord(tmp) ) ) )
                    else:
                        tmp = chr(ord(tmp) + dict_vigenere[key[j].lower()])
                
                i = tmp
                j+=1
                if j == keyLength:
                    j=0
            newString += i


        print("ciphered text: " + newString)


    #decipher
    if choice == 2:
        for i in text:
            if i.isalpha():
                tmp = i
                #check for space non alphabetical character in key
                if not key[j].isalpha():
                    j+=1
                    if j == keyLength:
                        j=0
                #for uppercase
                if i.isupper():
                    if ord(tmp) - dict_vigenere[key[j].lower()] < 65:
                        tmp = chr(91 - (dict_vigenere[key[j].lower()] - (ord(tmp) - 65 ) ) )
                    else:
                        tmp = chr(ord(tmp) - dict_vigenere[key[j].lower()])
                #for lowecase
                if i.islower():
                    if ord(tmp) - dict_vigenere[key[j].lower()] < 97:
                        tmp = chr(123 - (dict_vigenere[key[j].lower()] - (ord(tmp) - 97 ) ) )
                    else:
                        tmp = chr(ord(tmp) - dict_vigenere[key[j].lower()])
                
                i = tmp
                j+=1
                if j == keyLength:
                    j=0
            newString += i


        print("Deciphered text: " + newString)


def otp():
    while True:
        try:
            choice = int(input("Welcome to OTP(One-Time-Pad) cipher program\nPlease select number of preferable action: \n1)Cipher text\n2)Decipher text\n3)Exit the program\n"))
            
            if choice not in [1,2,3]:
                print("Please select a number between 1 and 3")
                while choice not in [1,2,3]:
                    choice = int(input("Welcome to OTP(One-Time-Pad) cipher program\nPlease select number of preferable action: \n1)Cipher text\n2)Decipher text\n3)Exit the program\n"))
            break
        except ValueError:
            print("Please enter a number")


    #if user wants to exit
    if (choice == 3):
        sys.exit()
        
    text = input("Enter the text: ")

    keySequence = list()
    newString = ""




    '''
    ======================================================
    Since OTP cipher is much similar in implementation to Caesar (besides random generated keys) I copy-pasted some of Caesars code here
    ======================================================
    '''

    #cipher
    if choice == 1:
        for i in text:
            if i.isalpha():
                key = randint(1, 26)
                tmp = i
                #for uppercase
                if i.isupper():
                    if ord(tmp) + key > 90:
                        tmp = chr(64 + (key - (90 - ord(tmp) ) ) )
                #for lowecase
                if i.islower():
                    if ord(tmp) + key > 122:
                        tmp = chr(96 + (key - (122 - ord(tmp) ) ) )
                    else:
                        tmp = chr(ord(tmp) + key)
                keySequence.append(key)
                i = tmp
            newString += i
    
        print("ciphered text: ", newString)
        print("Key Sequence: ", keySequence)


    #decipher
    if choice == 2:
        keySequence = list(map(int, input("Please enter the key sequence. For OTP you need to enter as much keys as you have letters in the text: ").split()))
        #initialize list counter
        j = 0
        for i in text:
            if i.isalpha():
                tmp = i
                #for uppercase
                if i.isupper():
                    if ord(tmp) - keySequence[j] < 65:
                        tmp = chr(91 - (keySequence[j] - (ord(tmp) - 65 ) ) )
                    else:
                        tmp = chr(ord(tmp) - keySequence[j])
                #for lowecase
                if i.islower():
                    if ord(tmp) - keySequence[j] < 97:
                        tmp = chr(123 - (keySequence[j] - (ord(tmp) - 97 ) ) )
                    else:
                        tmp = chr(ord(tmp) - keySequence[j])
                
                i = tmp
                j+=1
            newString += i
            
            
            
        print("deciphered text: ", newString)
    




def program():
    while True:
        try:
            choice = int(input("Welcome to ciphering program\nSelect the needed ciphering technique:\n1)Caesar Cipher\n2)Vigenere Cipher\n3)OTP (One-Time-Pad) Cipher\n4)Quit\n"))
            if choice == 1:
                caesar()
            elif choice == 2:
                vigenere()
            elif choice == 3:
                otp()
            elif choice == 4:
                sys.exit()
            else:
                print("SOMETHING WENT WRONG")
            break
        except ValueError:
            print("PLEASE ENTER VALID INDEX!!!")
    







program()