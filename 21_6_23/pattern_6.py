#hollow triangle
for i in range(1,5):
    for j in range(1,5):
        if i==j or j==1 or i==4:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
