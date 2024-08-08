'''num='01050124'
print(num)
count=0
two=[]
final=[]
for i in num:
    count+=1
    #print(f'{i}{num[count]}',end=" ")
    try:
        two.append(f'{i}{num[count]}')
        final.append(f'{i}{num[count]}')
    except:
        print('bye')

print(two)

for i in range(len(two)):
    if(i%2==0):
        pass
    else:
        print(two[i])
        final.remove(two[i])
print('Final',final)
'''
        


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
    two=[]
    final=[]
    for i in message:
        count+=1
        #print(f'{i}{num[count]}',end=" ")
        try:
            two.append(f'{i}{message[count]}')
            final.append(f'{i}{message[count]}')
        except:
            pass


    for i in range(len(two)):
        if(i%2==0):
            pass
        else:
            final.remove(two[i])
    print('Final',final)

    for numbers in final:
        for cod in code:
            if(numbers == cod):
                #print('Alphabet  is',alphabet)
                #print("Index of ",numbers,"is",code.index(numbers))
                #print(numbers,"=",alphabets[code.index(numbers)])
                text.append(alphabets[code.index(numbers)])
                
    
    return " ".join(text)
   
for i in range(len(code)):
    print(alphabets[i],"=",code[i],"|",end="  ")

plain_text=input("\nEnter message:").upper()
encrypted_message=encryption(plain_text)
print("\nEncrypted message = ",encrypted_message)
print(encrypted_message)
decrypted_message=decryption(encrypted_message)
print(decrypted_message)

'''
num='028211'
count=0
for i in num:
    print("i=",i)
    #print("i'th next =",num[count])
    count+=1
    print(f'{i}{num[count]}',end=" ")
 '''




