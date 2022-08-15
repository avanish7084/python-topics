
def traverse_matrix(matrix,n,m):
    ans=[[] for i in range(n+m-1)]
    for i in range(m):
        for j in range(n):
            ans[i+j].append(matrix[j][i])

    res=[]
    summ=0
    for i in ans:
        if summ<=sum(i):
            summ=sum(i)
            res=i
    return res

matrix=[]
m,n=map(int,input().split())
matrix=[[int(input()) for x in range (n)] for y in range(m)]

print(traverse_matrix(matrix,m,n))
