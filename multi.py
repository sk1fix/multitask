from multiprocessing import Pool

def sum_str(x,a):
    s=0
    if x <= len(a):
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
    index=[]
    for i in range(rows):
        index += ((i, mat),)
    print(index)
    for i in range(columns):
        print(*mat[i])
    with Pool(8) as f:
        res = f.starmap(sum_str, index)
    print(sum(res))
