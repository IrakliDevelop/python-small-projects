import sys




def caesar():
    while True:
        try:
            choice = int(input("Welcome to Caesar cipher program\nPlease select number of preferable action: \n1)Cipher text\n2)Decipher text\n3)Exit the program\n"))
            
            if choice not in [1,2,3]:
                print("Please select a number between 1 and 3")
                while choice not in [1,2,3]:
                    choice = int(input("Welcome to Caesar cipher program\nPlease select number of preferable action: \n1)Cipher text\n2)Decipher text\n3)Exit the program\n"))
            break;
        except ValueError:
            print("Please enter a number")
            
        
        #if user wants to exit
    if (choice == 3):
        sys.exit()
        
    text = input("Enter the text: ")
    
    while True:
        try:
            key = int(input("Enter the key "))
            break;
        except ValueError:
            print("The key in Caesar Cipher must be an integer")
            
    
    newString = ""
    key = key % 26
    
    if choice == 1:
        for i in text:
            if i.isalpha():
                tmp = i
                #for uppercase
                if ord(tmp) + key > 90 and ord(tmp) + key < 97:
                    tmp = chr(64 + (key - (90 - ord(tmp) ) ) )
                #for lowecase
                elif ord(tmp) + key > 122:
                    tmp = chr(96 + (key - (122 - ord(tmp) ) ) )
                else:
                    tmp = chr(ord(tmp) + key)
                
                i = tmp
            newString += i
            
            
            
        print("ciphered text: ", newString)
        
        
    if choice == 2:
        for i in text:
            if i.isalpha():
                tmp = i
                #for uppercase
                if i.isupper():
                    if ord(tmp) - key < 65:
                        tmp = chr(91 - (key + (ord(tmp) - 65 ) ) )
                    else:
                        tmp = chr(ord(tmp) - key)
                #for lowecase
                if i.islower():
                    if ord(tmp) - key < 97:
                        tmp = chr(123 - (key + (ord(tmp) -97 ) ) )
                    else:
                        tmp = chr(ord(tmp) - key)
                
                i = tmp
            newString += i
            
            
            
        print("deciphered text: ", newString)


    



caesar()
                    