#쇠막대기
'''
여러 개의 쇠막대기를 레이저로 절단하려고 한다
효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐놓고,
레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다,
쇠막대기와 레이저의 배치는 다음 조건을 만족한다

1. 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다
쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다
2. 쇠막대기를 자르는 레이저는 적어도 하나 존재한다
3. 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다

1. 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 또한, 모든 ‘( ) ’는 반드시 레이저를 표현한다.
2. 쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다.

()일 때는 자르고
(와 ) 둘이 붙어 있지 않는다면 막대기다

(가 나오고 )이 나올 때까지 ()개수를 보고
()개수+1을 해줘서 자른 쇠막대기 개수를 구할 수 있다
'''
import sys
I=sys.stdin.readline
O=sys.stdout.write
"""class stack:
    def __init__(self):
        self.list_=[]
    def Push(self, item):
        self.list_.append(item)
    def Pop(self):
        if self.is_empty():
            return
        else:
            return(self.list_.pop())
    def size(self):
        return len(self.list_)
    def top(self):
        return(self.list_[-1])
    def is_empty(self):
        if len(self.list_)==0:
            return 1
        else:
            return 0"""

stack_=[]
cnt=[]
#문자열을 압력받음
s=list(I())
total=0
i=0 #인덱스 역할
while(i!=len(s)):
    #여는 괄호와 닫는 괄호의 인접한 쌍
    if s[i]=="(" and s[i+1]==")":
        for n in range(len(cnt)):
            cnt[n]+=1
        i+=2
        continue
    elif s[i]=="(":
        stack_.append("(")
        cnt.append(1)
    elif s[i]==")":
        if len(stack_)!=0:
            stack_.pop()
        if len(cnt)!=0:
            total+=cnt.pop()
    i+=1
O(str(total))