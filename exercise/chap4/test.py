def solution(n,q):
    a = 0
    for i in range(n):
        for j in range(n):
            if a[i][j]==q:
                print("{}行{}列的矩阵中 {} 处于第{}行，第{}列".format(n,n,q,i,j))
                break
            a[i][j] = a[i][j] + 1 
            
            
n = int(input('请输入n：'))
q = int(input('请输入q：'))
solution(n,q)