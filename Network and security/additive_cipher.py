import string
alphabets=[]
for i in string.ascii_uppercase:
    alphabets.append(i)

# for i in range(len(alphabets)):
#     print(alphabets[i]," = ",i)

def encryption():
    text=input("Enter a message:").upper()
    key=int(input("Enter key:"))
    encrypted_text=''
    for letter in text:
        number=alphabets.index(letter)
        #print(number,end =" ")
        #Addition
        number+=key
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

def main():
    choice=int(input("Select operations:\n1.Encryption  2.Decryption\n"))
    if(choice==1):
        encryption()
    elif(choice==2):
        decryption()
    else:
        retry=input('Invalid input!, want to try again?(y/n):')
        if(retry=='y'):
            main()
        else:
            print('Exiting the program...')

    retry=input('Want to run again?(y/n):')
    if(retry=='y'):
        main()
    else:
        print('Exiting the program...')
main()