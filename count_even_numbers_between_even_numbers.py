n=int(input())
L=list(map(int,input().split()))
cnt=0
for i in range(1,n-1):
    if L[i]%2==0 and L[i-1]%2==0 and L[i+1]%2==0:
        cnt=cnt+1
print(cnt)