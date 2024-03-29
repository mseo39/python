# 드래곤 커브
"""
드래곤 커브는 다음과 같은 세가지 속성으로 이루어져 있으며, 이차원 좌표 평면 위에서 정의된다. 
좌표 평면의 x축은 → 방향 y 축은 ↓ 방향이다.
1. 시작 점
2. 시작 방향
3. 세대

0세대 드래곤 커브는 아래 그림과 같은 길이가 1인 선분이다. 아래 그림은 (0, 0)에서 시작하고, 시작 방향은 오른쪽인 0세대 드래곤 커브이다.

1세대 드래곤 커브는 0세대 드래곤 커브를 끝 점을 기준으로 시계 방향으로 90도 회전시킨 다음 0세대 드래곤 커브의 끝 점에 붙인 것이다. 
끝 점이란 시작 점에서 선분을 타고 이동했을 때, 가장 먼 거리에 있는 점을 의미한다.

2세대 드래곤 커브도 1세대를 만든 방법을 이용해서 만들 수 있다. (파란색 선분은 새로 추가된 선분을 나타낸다)

3세대 드래곤 커브도 2세대 드래곤 커브를 이용해 만들 수 있다. 아래 그림은 3세대 드래곤 커브이다.

즉, K(K > 1)세대 드래곤 커브는 K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝 점에 붙인 것이다.
크기가 100x100인 격자 위에 드래곤 커브가 N개 있다. 
이때, 크기가 1x1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구하는 프로그램을 작성하시오. 
격자의 좌표는 (x, y)로 나타내며, 0 ≤ x ≤ 100, 0 ≤ y ≤ 100만 유효한 좌표이다.

입력
첫째 줄에 드래곤 커브의 개수 N(1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 드래곤 커브의 정보가 주어진다. 
드래곤 커브의 정보는 네 정수 x, y, d, g로 이루어져 있다. 
x와 y는 드래곤 커브의 시작 점, 
d는 시작 방향, g는 세대이다. (0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)

입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다. 드래곤 커브는 서로 겹칠 수 있다.

방향은 0, 1, 2, 3 중 하나이고, 다음을 의미한다.

0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)

출력
첫째 줄에 크기가 1x1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 출력한다.

문제 풀이
예를 들어 시작점은 0,0이고 시작 방향은 오른쪽이라 한다면
0,0의 오른쪽으로 이동한 좌표 1,0을 구해주고 road에 오른쪽의 반대방향인 왼쪽을 넣어준다

다음 road에 있는 값을 꺼내보니 왼쪽이라는 방향이 있었고 이것을 90도로 돌리면 위쪽이 된다
1,0을 위쪽으로 이동한 1,-1울 구해주고 위쪽의 반대방향인 아래를 넣어준다

다음 road=[왼쪽, 아래쪽]이 있고 뒤에서부터 방향을 꺼내준다
1,-1을 아래쪽을 90도 돌린 왼쪽 방향으로 이동해주면 0,-1이 되고 road에 왼쪽의 반대인 오른쪽을 넣어준다
0,-1을 왼쪽을 90도 돌린 위쪽 방향으로 이동해주면 0,-2가 되고 road에 위쪽의 반대인 아래쪽을 넣어준다

다음 road=[왼쪽, 아래쪽, 오른쪽, 아래쪽]이고 뒤에서부터 방향을 꺼내준다
0,-2에서 아래쪽을 90도 돌린 왼쪽 방향으로 이동해주면 -1,-2가 되고 road에 왼쪽의 반대인 오른쪽을 넣어준다
-1,-2에서 오른쪽을 90도 돌린 아래 방향으로 이동해주면 -1,-1이 되고 road에 아래쪽의 반대인 위를 넣어준다
-1,-1에서 아래쪽을 90도 돌린 왼쪽 방향으로 이동해주면 -2,-1이 되고 road에 왼쪽의 반대인 오른쪽을 넣어준다
-2,-1에서 왼쪽을 90도 돌린 위쪽 방향으로 이동해주면 -2,-2가 되고 road에 위쪽의 반대인 아래쪽을 넣어준다

위 방식을 반복하면 되는 것이다
즉 처음에는 반대 방향만 넣어주고
그 다음부터 road에 저장된 방향을 뒤에서부터 따라가면서 90도 돌려서 이동하고 반대 방향을 추가해주면 되는 것이다

"""

import sys

# 초기화
result = [[0 for _ in range(101)] for _ in range(101)]  # 101x101 크기의 2차원 리스트 초기화
loc = [[1, 0], [0, -1], [-1, 0], [0, 1]]  # 방향에 따른 이동 좌표
turn = [3, 0, 1, 2]  # 방향을 오른쪽으로 90도 회전시키는 인덱스
back = [2, 3, 0, 1]  # 현재 방향에서 반대 방향으로 바뀌는 인덱스

# 드래곤 커브 생성 및 표시
for _ in range(int(sys.stdin.readline())):
    road = []  # 드래곤 커브의 이동 방향을 저장하는 리스트
    x, y, d, g = map(int, sys.stdin.readline().strip().split())  # 입력값 받기
    result[y][x] = 1  # 시작점 표시
    for _ in range(g + 1):
        if len(road) == 0:
            x += loc[d][0]
            y += loc[d][1]
            road.append(back[d])
            result[y][x] = 1
        else:
            tmp = []
            for k in road[::-1]:
                x += loc[turn[k]][0]
                y += loc[turn[k]][1]
                tmp.append(back[turn[k]])
                result[y][x] = 1
            road.extend(tmp)

# 정사각형 개수 계산
cnt = 0
for y in range(100):
    for x in range(100):
        if result[y][x] == result[y][x + 1] == result[y + 1][x] == result[y + 1][x + 1] == 1:
            cnt += 1
print(cnt)
