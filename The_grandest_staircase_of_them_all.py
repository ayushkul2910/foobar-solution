

n=int(raw_input())


m=[[0 for i in range(n+1)] for j in range(n+1)]

m[0][0]=1

for i in range(1,n+1):
    for j in range(0,n+1):
        m[i][j]=m[i-1][j]
        if j>=i:
            m[i][j]+=m[i-1][j-i]


print(m[n][n]-1)
