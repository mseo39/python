# 주사위 굴리기
"""
시간제한 2초
메모리제한 512MB

크기가 NxM인 지도가 존재한다. 지도의 오른쪽은 동쪽, 위쪽은 북쪽이다. 이 지도의 위에 주사위가 하나 놓여져 있으며, 주사위의 전개도는 아래와 같다. 
지도의 좌표는 (r, c)로 나타내며, r는 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수이다. 

  2
4 1 3
  5
  6

주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y) 이다. 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.
지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 
0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.
주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

입력
첫째 줄에 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.
둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다.
주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 
지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.
마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.

출력
이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

풀이
처음에 주사위 때문에 1시간동안 고민했다 이동할 때 마다 변하기 때문,, 그래서 힌트를 얻었는데
주사위를 굴릴때마다 인덱스를 이동해주면 된다는 것이다

주사위는 이동할 때 다음과 같이 칸이 변경된다
현재 = [1,2,3,4,5,6]
오른쪽으로 이동 = [4,2,1,6,5,3]
왼쪽으로 이동 = [3,2,6,1,5,4]
아래로 이동 = [2,6,3,4,1,5]
위로 이동 = [5,1,3,4,6,2]

그래서 위와 같이 이동하는 방향에 따라서 변경해주면된다,, 막상 알면 쉬운건데 거기까지 도달하는게 너무 어려운 것 같다 연습이 답이지 뭐,,

그리고 이동한 칸이 0이면
-> 주사위 바닥면의 값울 이동한 칸에 복사한다
0이 아니라면
-> 이동한 칸 값을 주사위 바닥면으로 복사한다
-> 이동한 칸의 값은 0이 된다

내가 처음에 틀린 이유
map_list를 정수가 아닌 문자로 해버린 바람에 이동한 칸이 0일때 확인할 때 문제가 발생한것,,
"""
import sys

N,M,x,y,k = map(int, sys.stdin.readline().strip().split())
map_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
k_list= list(map(int,sys.stdin.readline().strip().split()))
location=[[0,1],[0,-1],[-1,0],[1,0]]
result=[0 for _ in range(6)]

for k in k_list:
    if 0<= x+location[k-1][0]<N and 0<= y+location[k-1][1]<M:
        x+=location[k-1][0]
        y+=location[k-1][1]

        if k==1:
            result=[result[3], result[1], result[0], result[5], result[4], result[2]]
        elif k==2:
            result=[result[2], result[1], result[5], result[0], result[4], result[3]]
        elif k==3:
            result=[result[4], result[0], result[2], result[3], result[5], result[1]]
        else:
            result=[result[1], result[5], result[2], result[3], result[0], result[4]]
        
        if map_list[x][y]==0:
            map_list[x][y]=result[-1]
        else:
            result[-1]=map_list[x][y]
            map_list[x][y]=0

        print(result[0])