rows=int(input("rows:"))
cols=int(input("columns:"))
matrix=[]
for i in range(rows):
    l=[]
    for j in range(cols):
        l.append(int(input()))
    matrix.append(l)
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")
    print()
for i in range(rows):
    for j in range(cols):
        if(i==j):#finding diagonal elements
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("Lower diagonal elements:")
for i in range(rows):
    for j in range(cols):
        if(i>j):
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("Upper diagonal elements")
for i in range(rows):
    for j in range(cols):
        if(i<j):
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")

    print()
            
                      
