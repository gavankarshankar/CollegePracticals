text=input("Enter a message:").upper()


def create_matrix(message):
    encrypted=''
    length=len(message)
    if(length%2==0):
        half_length=int(len(text)/2)
    else:
        half_length=int(len(text)/2)+1
        rows,columns=(int(half_length/2),half_length)
        matrix=[['$']*columns]*rows
        new=[[],[]]
        print(matrix)
    
    
        for i in range(rows):
            for j in range(columns):
                for letter in message:
                    print(matrix[i][j],'=',letter)
                    new[i].append(letter)
                break
            break
            



    print(new)


create_matrix(text)