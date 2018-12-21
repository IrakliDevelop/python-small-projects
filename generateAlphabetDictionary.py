'''
the purpose of this program is to generate for you sequence that you can use to create dictionary of alphabetical characters with numeric values of place in alphabet assigned to them
'''

char = 'a'
i = 1
while char <="z":
    print("\"" + char + "\" : " + str(i) + ", ", end="")
    char = chr(ord(char)+1)
    i += 1
