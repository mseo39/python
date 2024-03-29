#아기상어
"""
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.
아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 
나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 
즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.

둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.

0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
아기 상어는 공간에 한 마리 있다.

출력
첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.
"""

import sys
from collections import deque

location =[[1,0],[0,1],[-1,0],[0,-1]]
cnt=0
size=2
fish=[]

def bfs(x,y,d):
    queue = deque()
    queue.append([x,y,d])
    visited=[[0 for _ in range(N)] for _ in range(N)]
    visited[x][y]=1
    fish.clear()

    while queue:
        nx, ny, d = queue.popleft()
        for i in location:
            dx=nx+i[0]
            dy=ny+i[1]
            if 0<=dx<N and 0<=dy<N and visited[dx][dy]==0:
                if N_list[dx][dy]==0 or N_list[dx][dy]==size:
                    queue.append([dx,dy,d+1])
                elif N_list[dx][dy]<size:
                    fish.append([dx,dy,d+1])
                visited[dx][dy]=1

def chk():
    for x in range(N):
        for y in range(N):
            if N_list[x][y]==9:
                bfs(x,y,0)
                N_list[x][y]=0
                return
            
def sorting_criteria(fish):
    return (fish[2], fish[0], fish[1])

#공간의 크기
N= int(sys.stdin.readline())
#공간의 상태
"""
0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
"""
N_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
chk()

tmp=0
while(True):
    if len(fish)==0:
        print(tmp)
        break
    if len(fish)==1:
        cnt+=1
    else:
        fish = sorted(fish, key=sorting_criteria)
        cnt+=1
    if size==cnt:
        cnt=0
        size+=1
    N_list[fish[0][0]][fish[0][1]]=0
    tmp=fish[0][2]
    bfs(fish[0][0],fish[0][1],fish[0][2])

"""from collections import deque

# 상, 하, 좌, 우로 이동하는 방향을 표현하는 리스트
direction =[[-1,0],[1,0],[0,-1],[0,1]]
#아기상어 크기
size=2

#bfs  탐색 시작할 위치
def bfs(x,y):
    global size
    visited = [[0]*T for _ in range(T)]
    queue=deque([[x,y,0]])
    #먹을 수 있는 물고기 위치 x,y,거리
    fish=[]
    visited[x][y] = 1
    
    while queue:
        now=queue.popleft()
        for i in direction:
            dx=now[0]+i[0]
            dy=now[1]+i[1]
            if 0<=dx<T and 0<=dy<T and visited[dx][dy] == 0:
                #물고기를 먹는 경우
                #아기 상어보다 크기가 작은 경우, 0은 물고기가 아니니 제외
                if map_list[dx][dy]<size and map_list[dx][dy]!=0:
                    #먹을 물고기를 찾으면 
                    fish.append({"x":dx,"y":dy,"distance":now[2]+1})
                #이동할 수 있는 곳은 큐에 저장
                #크기가 같은 곳, 빈칸인 곳
                elif map_list[dx][dy]==size or map_list[dx][dy]==0:
                    queue.append([dx,dy,now[2]+1])
                print("=======")
                print(dx, dy)
                print(queue)
                print(fish)
                visited[dx][dy] = 1

    size+=1
    result=sorted(fish, key=lambda x: (x["distance"], x["x"], x["y"]))
    map_list[result[0]["x"]][result[0]["y"]]=0
    return [result[0]["x"],result[0]["y"],result[0]["distance"]]


T = int(input())
map_list=[]

for x in range(T):
    map_list.append(list(map(int, input().split())))
    if 9 in map_list[x]:
        loc=[x,map_list[x].index(9)]

total=0
while True:
    if T*T==sum([i.count(0) for i in map_list])+1:
        break
    if size <= min([min(i) for i in map_list]):
        break
    loc=bfs(loc[0], loc[1])
    total+=loc[2]
    print("총합: ",loc[2])
    print(total)

print(total)"""