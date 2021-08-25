#exec()함수
'''
문자열로 표현된 문을 인수로 받아 파이썬 컴파일 코드로 변환

ex)
a=5 exec('a=a+4') print(a)->9
'''
#eval()함수
'''
문자열로 표현된 파이썬 식을 인수로 받아 파이껀 컴파일코드로 변환
단, 식만 처리가능하며 문(a=a+1)을 인수로 받으면 오류가 난다

ex)
a=1 a=eval('a+4') print(a)-> 5
'''
#join()함수
'''
리스트에 있는 요소를 합쳐서 문자열로 바꿔줌

-.join(리스트): ['a','b','c']를 'abc'의 문자열로 합쳐서 반환 - 여기서 구분자는 공백
-'구분자'.join(리스트): '_'.join(['a','b','c'])이면 "a_b_c"
'''
#문자열[::-1]
'''
문자열을 뒤집어준다
[3:0:-1]은 인덱스 3번부터  1까지 역순으로 출력 abcde->dcb
[3::-1]은 인덱스 3번부터 0번까지 역순으로 출력 abcde->dcba
'''
#문자열[::2]
'''
문자열을 두개씩 잘라준다

a='abcdefgh'
print(a[::2]) -> aceg
'''
#for문 거꾸로 반복하기
'''
range()는 3개의 파라미터가 있다
range([start],stop,[step]) -start와 step은 생략 가능(start=0, step=1)
start는 시작 숫자 stop은 끝 숫자, step은 숫자 사이의 거리를 의미
(단, 끝 숫자는 포함되지 않는다)

: start=n stop=0 ** step=-1로 지정하면 n부터 1까지 출력된다
'''