import string
alphabets=[]
for i in string.ascii_uppercase:
    alphabets.append(i)

# for i in range(len(alphabets)):
#     print(alphabets[i]," = ",i)

def encryption():
    text=input("Enter a message:").upper()
    indexes=[]
    first_letter=[text[0]]
    key=int(input("Enter key:"))
    encrypted_text=''
    for letter in text:
        number=alphabets.index(letter)
        indexes.append(number)
        #Auto-key
        if(letter==first_letter):
            number+=key
            if(number>25):
                mod=number%26
                encrypted_text+=(alphabets[mod])
            else:
                encrypted_text+=(alphabets[number])
        else:
            number+=indexes[]
            if(number>25):
                mod=number%26
                encrypted_text+=(alphabets[mod])
            else:
                encrypted_text+=(alphabets[number])

    print(encrypted_text)
    

def decryption():
    text=input("Enter a message:").upper()
    key=int(input("Enter key:"))
    decrypted=''
    for letter in text:
        index=alphabets.index(letter)
        if(key>index):
            index+=26
            value=index-key
            decrypted+=(alphabets[value])
        else:
            value=index-key
            decrypted+=(alphabets[value])
    print(decrypted)

# text=input("Enter a message:").upper()
# key=int(input("Enter key:"))
# encrypted_text=encryption(text,key)
# print("Encryption:",encrypted_text)
# decrypted_text=decryption(encrypted_text,key)
# print("Decryption:",decrypted_text)
encryption()
#decryption()
