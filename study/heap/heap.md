### 힙 라이브러리
```python
import heapq
```

### 시간복잡도
> 삽입, 삭제 연산에 대한 시간 복잡도는 O(logN)

### 정렬은 어떤 기분으로 되는가?
```python
[1,3] [1,2] [0,2] [4,5] 가 있다면
-> [0,2] [1,2] [1,3] [4,5] 가 된다 즉 맨 앞에서부터 값을 비교하고 정렬하는 것이다 맨 앞에 값이 같다면 그 다음 값을 비교
```

### 함수
```python
heapq.heappush(heap, item) : item을 heap에 추가
heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
```

### 최소힙 만들기
```python
min_heap = []
heapq.heappush(min_heap, n)
```

### 최대힙 만들기
> 파이썬에서는 최소힙만 지원하기 때문에 넣으려는 값에 음수를 붙인다
```python
max_heap = []
heapq.heappush(max_heap, -n)
```

### 힙에서 최소 또는 최대 값 꺼내기
```python
tmp = heapq.heappop(max_heap) #이때 최대힙은 원소가 음수로 되어있으므로 주의
tmp = heapq.heappop(min_heap)
```

### 힘에서 원소를 삭제하지 않고 값 가져오기
```python
# 0인덱스로 접근
heap[0]
```

### 리스트를 heap으로 변환
```python
heap2 = [50 ,10, 20]
heapq.heapify(heap2)
```