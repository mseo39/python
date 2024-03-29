#자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 
# 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
#예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 
#소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

min_num=int(input()) #최소값 입력
max_num=int(input()) #최대값 입력
num_list=[] #빈배열 생성하기
for i in range(min_num,max_num+1): #입력한 범위 내에서
    cnt=0#소수인지 아닌지 확인하기 위한 변수
         #0이면 소수이고 아니면 소수가 아니다
    for j in range(2,i):#2부터 자기자신까지 
        if(i%j==0):#나머지가 0이라면 소수가 아님
            cnt+=1#증가
            break
    if (cnt==0 and i!=1):#cnt가 0이면 1과 자기자신 외에 나눠지는 값이 없었다는 것으로
        num_list.append(i)#리스트에 삽입
if (len(num_list)==0):#빈 배열이라면
    print(-1)#-1을 출력
else:#아니라면
    print(sum(num_list))#배열에 있는 값들을 합해준다
    print(num_list[0])#0번째 인덱스 값을 출력