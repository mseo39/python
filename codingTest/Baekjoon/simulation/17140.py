#이차원 배열과 연산
"""
시간제한 0.5초
메모리제한 512MB

크기가 3x3인 배열 A가 있다. 배열의 인덱스는 1부터 시작한다. 1초가 지날때마다 배열에 연산이 적용된다.

* R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
* C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.

한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다. 그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다. 
그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다. 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.

예를 들어, [3, 1, 1]에는 3이 1번, 1가 2번 등장한다. 따라서, 정렬된 결과는 [3, 1, 1, 2]가 된다. 
다시 이 배열에는 3이 1번, 1이 2번, 2가 1번 등장한다. 다시 정렬하면 [2, 1, 3, 1, 1, 2]가 된다.

정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있다. 
R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변하고, 
C 연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변한다. 행 또는 열의 크기가 커진 곳에는 0이 채워진다. 
수를 정렬할 때 0은 무시해야 한다. 예를 들어, [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다.

행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간을 구해보자.

입력
첫째 줄에 r, c, k가 주어진다. (1 ≤ r, c, k ≤ 100)

둘째 줄부터 3개의 줄에 배열 A에 들어있는 수가 주어진다. 배열 A에 들어있는 수는 100보다 작거나 같은 자연수이다.

출력
A[r][c]에 들어있는 값이 k가 되기 위한 연산의 최소 시간을 출력한다. 100초가 지나도 A[r][c] = k가 되지 않으면 -1을 출력한다.

문제 정리

* 배열 A가 100*100을 넘어가면 안되고 나머지는 0이어야 된다고 함
  * 그럼 연산할 때마다 증가해야 하나?
  * 메모리 제한이 512MB라서 그냥 처음에 만들어줌
* R연산과 C연산 중 선택할 때 행의 개수와 열의 개수가 중요함
  * r_cnt=3 c_cnt=3를 만들어줌
  * 문제를 처음에 잘못 해석함 행이 가지고 있는 원소의 개수인줄 알았음 근데 행의 개수였음 그냥 개수,,ㅋ
  * 그래서 r_cnt는 열의 개수가 되고 c_cnt는 행의 개수가 됨
* 행의 개수>=열의 개수
  * R연산 - 모든 행에 대해 정렬
    * 행에서 0이 아닌것만 정렬해야하고 행의 원소개수는 열의 개수임 반복문을 통해 0을 아닌 것을 찾아 저장
    * 정렬
    * 정렬한 개수가 100을 넘어가면 자름
    * 정렬한게 증가하면 열의 개수가 늘어나므로 갱신
    * 정렬된 값을 순서대로 저장
    * 만약에 정렬된 값이 원래 길이보다 작으면 나머지는 0으로 채워줘야되므로 len(tmp)~r_cnt을 0으로 채워줌
  * C연산 - 모든 열에 대해 정렬
    * 위 연산과 비슷
* 정렬
  * 먼저 값의 개수를 기준으로 오름차순 정렬하고, 그 다음 값 자체를 기준으로 오름차순 정렬

"""
import sys

def A_sort(v):
    tmp=[]
    # 리스트 v 내의 고유한 값들을 반복하여 처리
    for i in set(v):
        tmp.append([i,v.count(i)]) # 리스트 tmp에 값과 그 값의 개수를 저장
    result=[]
    # tmp 리스트를 정렬하는데, 먼저 값의 개수를 기준으로 오름차순 정렬하고, 그 다음 값 자체를 기준으로 오름차순 정렬
    for i in sorted(tmp, key=lambda x:(x[1],x[0])):
        result.extend(i) # result 리스트에 정렬된 값을 추가
    return result

def R():
    global r_cnt
    # 행을 돌면서
    for x in range(c_cnt):
        tmp=[]
        # 열을 돌면서 0이 아닌 값들을 tmp 리스트에 추가
        for y in range(r_cnt):
            if A[x][y]!=0:
                tmp.append(A[x][y])

        tmp=A_sort(tmp) # tmp 리스트 정렬
        if len(tmp)>100:
            tmp=tmp[:100] # 만약 리스트 길이가 100을 초과하면 100까지만 잘라냄
        r_cnt=max(r_cnt,len(tmp)) # r_cnt 값 갱신
        # 정렬된 값들을 해당 행에 채워넣음
        for y in range(len(tmp)):
            A[x][y]=tmp[y]
        # 남은 공간은 0으로 채움
        for y in range(len(tmp),r_cnt):
            A[x][y]=0
def C():
    global c_cnt
    # 열을 돌면서
    for y in range(r_cnt):
        tmp=[]
        # 행을 돌면서 0이 아닌 값들을 tmp 리스트에 추가
        for x in range(c_cnt):
            if A[x][y]!=0:
                tmp.append(A[x][y])

        tmp=A_sort(tmp) # tmp 리스트 정렬
        if len(tmp)>100:
            tmp=tmp[:100] # 만약 리스트 길이가 100을 초과하면 100까지만 잘라냄
        c_cnt=max(c_cnt,len(tmp)) # c_cnt 값 갱신
        # 정렬된 값들을 해당 열에 채워넣음
        for x in range(len(tmp)):
            A[x][y]=tmp[x]
        # 남은 공간은 0으로 채움
        for x in range(len(tmp),c_cnt):
            A[x][y]=0


r, c, k = map(int, sys.stdin.readline().strip().split())
A=[[0 for _ in range(100)] for _ in range(100)]
# 입력받은 숫자들을 배열 A의 처음 3x3 부분에 채워넣음
for x in range(3):
    tmp=list(map(int, sys.stdin.readline().strip().split()))
    for y in range(3):
        A[x][y]=tmp[y]
cnt=0
r_cnt=3
c_cnt=3
while(A[r-1][c-1]!=k):
    # r_cnt가 c_cnt 이하일 때는 행에 대해 R 함수 호출
    if r_cnt<=c_cnt:
        R()
    else:
        # 그렇지 않을 때는 열에 대해 C 함수 호출
        C()

    cnt+=1 # 연산 횟수 증가
    # 연산 횟수가 100을 넘어가면 더 이상 진행할 수 없으므로 -1 출력 후 종료
    if cnt==101:
        cnt=-1
        break

print(cnt)