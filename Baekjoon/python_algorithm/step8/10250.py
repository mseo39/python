#ACM 호텔
#호텔 방 번호의 규칙을 찾아 출력하는 문제
'''
호텔정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성

각층에 W개의 방 H층 건물, 엘레베이터는 가장 왼쪽에 있다
호텔 정문은 1층 엘레베이터 앞
인접한 두 방 사이의 거리는 1이다

방번호는 YXX나 YYXX형태인데 Y나 YY는 층 수를 XX는 엘레베이터에서 부터 세었을 때 방번호

손님은 엘레베이터를 타고 이동하는 거리는 신경 X
다만, 걷는 거리가 같다면 아래층을 선호

예를 들면 102 호 방보다는 301 호 방을 더 선호하는데, 102 호는 거리 2 만큼 걸어야 하지만 301 호는 거리 1 만큼만 걸으면 되기 때문이다. 같은 이유로 102 호보다 2101 호를 더 선호한다.


: 그럼 결국엔 반 배정하는 순서는
101->201->301-> ---->102->202-> 이렇게 됨

입력
T 는 입력의 맨 첫 줄에 주어진다
각 테스트 데이터는 한 행으로서 H(호텔의 층 수), W(각 층의 방 수), N(몇 번째 손님), 세 정수를 포함하고 있다

출력
 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.

풀이
N%H를 하면 층을 알 수 있고
N/H를 하면 호를 알 수 있다
'''
for _ in range(int(input())):
    H,W,N=map(int,input().split())
    print (H*100+int(N/H) if N%H==0 else N%H*100+int(N/H+1))