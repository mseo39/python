#연구소
"""
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 
직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 
일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.
2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

바이러스가 퍼진 뒤의 모습은 아래와 같아진다.
2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
빈 칸의 개수는 3개 이상이다.

출력
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

아니 벽을 어떤 조건을 가지고 세우지...? 고민하고 있었는데 그냥 무작정 벽 3개를 세우란다
이런 멍청한 방식,,

정답은 나오지만 시간초과가 뜸
pypy3로 하길래 해보니깐 런타임 에러 (IndexError) 뜸
다른 사람들과 코드 비교를 해봤는데 다른 부분이 없어서 뭐가 잘못된거지 했다가
주목한 부분이
if now[1]>0 and new[now[0]][now[1]-1]==0:
이 조건문에서 에러가 날 수도 있겠다는 생각이 들었다

그래서 전 문제부터도 그렇고 상하좌우로 움직일 때 다음과 같은 방법을 사용해서 나도 그 방법을 사용하기로 했다

d = [[-1,0],[1,0],[0,-1],[0,1]]

for i in range(4):
    dr = now[0]+d[i][0]
    dc = now[1]+d[i][1]

    if (0<=dr<N) and (0<=dc<M):
        if new[dr][dc] == 0:
            new[dr][dc] =2
            queue.append([dr,dc])
"""
from collections import deque

#입력받은 것을 저장
N, M=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(N)]
max_num=0

#벽 3개를 세우는 함수
def wall(cnt):
    if cnt==3:
        global max_num
        max_num=max(max_num, birus())
        return
    for x in range(N):
        for y in range(M):
            if arr[x][y]==0:
                arr[x][y]=1
                wall(cnt+1)
                arr[x][y]=0

d = [[-1,0],[1,0],[0,-1],[0,1]]

def birus():
    new=[i[:] for i in arr]
    cnt=0
    for x in range(N):
        for y in range(M):
            if new[x][y]==2:
                cnt+=1
                queue=deque([[x,y]])

                while queue:
                    now=queue.popleft()

                    for i in range(4):
                        dr = now[0]+d[i][0]
                        dc = now[1]+d[i][1]

                        if (0<=dr<N) and (0<=dc<M):
                            if new[dr][dc] == 0:
                                new[dr][dc] =2
                                queue.append([dr,dc])
                    """#상
                    if now[1]>0 and new[now[0]][now[1]-1]==0:
                        queue.append([now[0],now[1]-1])
                        new[now[0]][now[1]-1]=2
                    #하
                    if now[1]<N-1 and new[now[0]][now[1]+1]==0:
                        queue.append([now[0],now[1]+1])
                        new[now[0]][now[1]+1]=2
                    #좌
                    if now[0]>0 and new[now[0]-1][now[1]]==0:
                        queue.append([now[0]-1,now[1]])
                        new[now[0]-1][now[1]]=2
                    #우
                    if now[0]<N-1 and new[now[0]+1][now[1]]==0:
                        queue.append([now[0]+1,now[1]])
                        new[now[0]+1][now[1]]=2"""
    return sum([i.count(0) for i in new])

wall(0)
print(max_num)