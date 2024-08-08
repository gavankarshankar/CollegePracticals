import string
alphabets=[]
code=[]

for letter in string.ascii_uppercase:
    alphabets.append(letter)

alphabets.append('00')

for i in range(0,27):
    i=f'{i}'
    code.append(i)

def encryption(message):
    enc_message=[]
    for letter in message:
        for alphabet in alphabets:
            if(letter == alphabet):
                #print('Alphabet  is',alphabet)
                #print("Index of ",alphabet,"is",alphabets.index(letter))
                #print(alphabet,"=",code[alphabets.index(letter)])
                enc_message.append(code[alphabets.index(letter)])
    return "".join(enc_message)

def decryption(message):
    text=[]
    for letter1 in message:
        letter2=message.index(letter1)
        for number in code:
        #if(number == letter):
            print('Number  is',f'{letter1}{letter2}')
            print("Index of ",letter,"is",code.index(letter))
            print(number,"=",alphabets[code.index(letter)])
            #text.append(alphabets[code.index(letter)])
    #return " ".join(text)
                
for i in range(len(code)):
    print(alphabets[i],"=",code[i],"|",end="  ")
    
plain_text=input("\nEnter message:").upper()
encrypted_message=encryption(plain_text)
print("\nEncrypted message = ",encrypted_message)
decryption(encrypted_message)
#print(decrypted_message)







