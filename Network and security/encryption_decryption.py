import string
alphabets=[]
code=[]

for letter in string.ascii_uppercase:
    alphabets.append(letter)

alphabets.append('00')

for i in range(0,26):
    i=f'{i}'
    if(len(i)==1):
        i=f'0{i}'
        code.append(i)
    else:
        code.append(i)
code.append('26')

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
    count=0
    for letter in message:
        for number in code:
            count+=1
        print("i=",i)
        if(num[-1]==i):
            break
        else:
            print("i'th next =",num[count])
        #if(number == letter):
            print('Number  is',f'{letter1}{letter2}')
            print("Index of ",letter,"is",code.index(letter))
            print(number,"=",alphabets[code.index(letter)])
            #text.append(alphabets[code.index(letter)])
    #return " ".join(text)
   
for i in range(len(code)):
    print(alphabets[i],"=",code[i],"|",end="  ")

#plain_text=input("\nEnter message:").upper()
#encrypted_message=encryption(plain_text)
#print("\nEncrypted message = ",encrypted_message)
#decryption(encrypted_message)
#print(decrypted_message)

num='hello'
count=0
for i in num:
    print("i=",i)
    print("i'th next =",num[count])
    count+=1
    




