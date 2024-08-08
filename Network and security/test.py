matrix=[[1,2,3],[4,5,6]]
text='COLLEGE'
new=[[],[]]
for i in range(len(text)):
    if(i<3):
        new[0].append(text[i])
    else:
        new[1].append(text[i])

while(len(new[0])!=len(new[1])):
    new[1].append('$')
print(new)
#matrix=new
#print(matrix)

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(i,j,end=" ")
        

print(matrix)