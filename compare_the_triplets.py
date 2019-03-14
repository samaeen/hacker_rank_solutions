a= list(map(int, input().split()))
b= list(map(int, input().split()))
A =B =0
for i in range(3):
    if a[i] > b[i]:
        A += 1
    elif a[i] < b[i]:
        B += 1
print(str(A) + ' ' + str(B))