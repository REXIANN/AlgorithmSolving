import sys
sys.stdin = open("14499input.txt", "r")

tc = int(input())
for _ in range(tc):
    N,M,y,x,K=map(int,input().split())
    g=[list(map(int,input().split())) for _ in range(N)]
    a=b=c=d=e=f=0
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    for i in map(int,input().split()):
       if 0<=x+dx[i-1]<M and 0<=y+dy[i-1]<N:
          x+=dx[i-1]
          y+=dy[i-1]
          if i==1:a,b,c,d,e,f=a,f,c,e,b,d
          elif i==2:a,b,c,d,e,f=a,e,c,f,b,d
          elif i==3:a,b,c,d,e,f=b,c,d,a,e,f
          elif i==4:a,b,c,d,e,f=b,c,d,a,e,f
          if g[y][x]==0:g[y][x]=b
          else:b=g[y][x];g[y][x]=0
          print(d)