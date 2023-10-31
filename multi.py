def sum_str(x,a):
    sum=0
    for j in range(len(a)):
        sum+=a[x][j]
    return sum

if "__main__"==__name__:
    rows=int(input())
    columns=int(input())
    mat=[]
    for i in range(columns):
        elem=[]
        for j in range(rows):
            a=int(input())
            elem.append(a)
        mat.append(elem)
    for i in range(columns):
        print(*mat[i])
    
