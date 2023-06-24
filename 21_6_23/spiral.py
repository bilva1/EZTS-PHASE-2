def spiral(m):
    top=0
    bottom=len(m)-1
    left=0
    right=len(m)-1
    if not len(m) or not m:
        return
    while True:
        if left>right:
            break
        for i in range(left,right+1):
            print(m[top][i],end=' ')
        top=top+1
        if top>bottom:
            break
        for i in range(top,bottom+1):
            print(m[i][right],end=' ')
        right=-1
        for i in range(right,left-1,-1):
            print(m[i][bottom],end=' ')
        bottom=-1
        for i in range(bottom,top-1,-1):
            print(m[i][left],end=' ')
        left=left+1



m=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
spiral(m)
