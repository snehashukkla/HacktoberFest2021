t=int(input())
for tt in range(t):
    x,y=map(int,input().split())
    print(x*2,x*y*(x*y-1))
