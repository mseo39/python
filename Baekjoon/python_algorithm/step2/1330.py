#두 수 비교하기
'''
A가 B보다 큰 경우에는 >를 출력
A가 B보다 작은 경우에는 <를 출력
A가 B보다 같은 경우에는 ==를 출력
'''
a,b= map(int, input().split())
if a>b: print(">")
elif a<b: print("<")
else: print("==")

'''
- 인덱스를 사용해서 문제를 품

a,b=map(int,input().split())
print(['><'[a<b],'=='][a==b])

a==b가 true라면
['><'[a<b],'=='][1] '==' 이 출력됨

a==b가 false라면
['><'[a<b],'=='][0] -> '><'[a<b]

a<b가 true라면
'><'[1] '<' 이 출력됨

a<b가 false라면
'><'[0] '>' 이 출력됨
''' 