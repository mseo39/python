#N과 M (1)

"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오
* 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열

입력
- 첫째 줄에 자연수 N과 M이 주어진다 (1<= M <= N <= 8)

출력
- 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수영을 여러 번 출력하면 안되며,
각 수열은 공백으로 구분해서 출력해야 한다

수열은 사전 순으로 증가하는 순서로 출력해야 한다

예전에 풀었던 방법
수열을 만들어주는 함수를 이용하여 푸는 것

from itertools import permutations

N,M = map(int, input().split())

num=[i for i in range(1,N+1)]

for e in list(permutations(num,M)):
    print(*e)

이번에는 백트래킹을 이용하여 문제를 풀어볼려고 한다
백트래킹에 익숙해지기 위해 풀이를 보면서 풀어보았다

백트래킹의 핵심은 DFS이나 가지치기를 하기 때문에 방문했던 곳을 기억하고 있는 공간이 필요하다는 것이다

백트래킹의 문제를 풀어보니 다음과 같은 규칙을 가지고 있는 것 같다
1. 재귀함수
2. 조건을 주고 그 조건에 맞을 때 출력(결과를 위한)
3. 이미 존재하는 확인, 배열안에 들어갈 조건에 맞는지 확인

위 규칙에 따라 이 문제을 풀어본다면

1. go()
2. 문제를 보면 수열의 길이가 M이어야 한다고 나온다
그럼 수열의 길이가 M일 때 출력하면 된다
3. 배열에 숫자를 넣을 때 숫자가 이미 배열에 있는 지 확인하고 넣는다
"""
def go():
    if len(arr)==M:
        print(*arr)
        return
    for i in range(1,N+1):
        if i not in arr:
            arr.append(i)
            go()
            #여기까지 욌다는 것은 조건에 맞지 않기 때문에 돌아온 것으로
            #pop을 해준다
            arr.pop()

N,M = map(int, input().split())
arr=[]
go()