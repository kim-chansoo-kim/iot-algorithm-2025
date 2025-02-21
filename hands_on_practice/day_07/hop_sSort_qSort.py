# 선택 정렬과 퀵 정렬의 성능 비교하기
import random
import time

# 선택 정렬 함수
#----------------------------------------------------------------------------------------
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if (ary[minIdx] > ary[k]):
                minIdx = k

        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
    return ary
#----------------------------------------------------------------------------------------

# 퀵 정렬 함수
#----------------------------------------------------------------------------------------
def sortQuick(ary, start, end):
    if end <= start:
        return

    low = start
    high = end 

    pivot = ary[(low + high) // 2] # 리스트 중간값을 기준값으로
    while low <= high:
        while ary[low] < pivot:
            low += 1
        while ary[high] > pivot:
            high -= 1
        if low <= high:
            ary[low], ary[high] = ary[high], ary[low]
            low, high = low + 1, high - 1

    sortQuick(ary, start, high)
    sortQuick(ary, low, end)
#----------------------------------------------------------------------------------------
def quicksort(ary):
    sortQuick(ary, 0, len(ary)-1)

# 메인코드
#----------------------------------------------------------------------------------------
countAry = [1000, 10000, 12000, 15000]

for count in countAry:
    tempAry = [random.randint(10000, 99999) for _ in range(count)]
    selectAry = tempAry[:]
    quickAry = tempAry[:]

    print('## 데이터수 : ', count, '개')

    start = time.time()
    selectionSort(selectAry)
    end = time.time()
    print('선택정렬 --> %10.3f 초' % (end - start))

    start = time.time()
    quicksort(quickAry)
    end = time.time()
    print('퀵 정렬 --> %10.3f 초' % (end - start))

    print()

    count *= 5
#----------------------------------------------------------------------------------------
