n=int(input())
L=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if L[i]%2==0:
        print(i)
        break