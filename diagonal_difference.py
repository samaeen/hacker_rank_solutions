n=int(input())
a= [list(map(int, input().split())) for i in range (n)]
firstDiagonal = sum(a[i][i] for i in range(n))
secondDiagonal = sum(a[i][n-i-1] for i in range(n))
print(abs(firstDiagonal-secondDiagonal))