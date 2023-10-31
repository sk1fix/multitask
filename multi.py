from multiprocessing import Pool

def sum_str(x,a):
    s=0
    for i in range(len(a[x])):
        s+=a[x][i]
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
    index=[]
    for i in range(columns):
        index += ((i, mat),)
        print(*mat[i])
    with Pool(8) as f:
        res = f.starmap(sum_str, index)
    print(sum(res))
