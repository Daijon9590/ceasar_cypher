# ---This is the max amount of letters in the alphabet that is used when entering the key number
MaxNum=26 
# ---If the user INPUTS encrypt, e, decrypt, or d then the program will return that input in all lowercase. else it will ask again
def EorD():
    while True:
        print('Would you like to Encrypt or Decrypt?')
        mode = input().lower()
        if mode in ('encrypt e decrypt d').split():
        	return mode
        else:
            print('Please choose encrypt or decrypt')
# ---Ask for the message that wants to be E or D
def getMessage():
	while True:
    		message= input('What would you like to say?:')
    		if message.isalpha():
    			print (message)
    			return message
    		elif message.isnumeric():
    			print ('Please enter letters')
    		else:
    			print ('')
# ---Takes what ever number the user inputs and verifies that it is in the peramiters to continue
def getKey():
    key = 0
    while True:
    	try:
    		print('Enter the key number (1-%s)' % (MaxNum))
    		key=int(input())
    		if (key >= 1 and key <= MaxNum):
    			return key
    	except ValueError:
        	print('Error, please input valid number!!!')
        	continue
    	if (key <= 1 or key >= MaxNum):
        	print('Error, please enter valid number')
# ---Takes the input from the mode, message, and key and counts back the keyed amount if it is decryping. Vice versa
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'e':
        key = +key
    translated = ''

    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = EorD()
message = getMessage()
key = getKey()

print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))