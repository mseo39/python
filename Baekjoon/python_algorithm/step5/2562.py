#최댓값
#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지
'''
입력
첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다
출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력
'''
a=list(int(input())for _ in range(9))
max=max(a)
print(max)
print(a.index(max)+1)