from multiprocessing import Pool

def sum_str(x,a):
    s=0
    if i <= len(a):
        s=sum(a[x])
    return s

if "__main__"==__name__:
    rows=int(input())
    columns=int(input())
    mat=[]
    summ=0
    for i in range(columns):
        elem=[]
        for j in range(rows):
            a=int(input())
            elem.append(a)
        mat.append(elem)
    index=list(range(columns))
    print(index)
    for i in range(columns):
        print(*mat[i])
    matx=[]
    for i in range(rows):
        
        matx.append(mat)
    #Process(target=sum_str,args=(index,mat,summ))
    res = list(Pool(4).map(sum_str, index, matx))
    print(res)
