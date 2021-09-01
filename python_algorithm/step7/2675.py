#문자열 반복
#각 문자를 반복하여 출력하는 문제
'''
입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 
출력
각 테스트 케이스에 대해 P를 출력한다.
'''
#문자열 연산을 사용할줄 아는가
for _ in range(int(input())):
    sum=''
    a,b=input().split()
    for i in b:
        sum+=i*int(a) #다른방법: print(int(a)*j, end='')
    print(sum)