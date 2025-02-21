# 이미 정렬된 줄에 끼어들기

import random
import time

def BubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        changeYN = False
        for cur in range(0, end):
            if ary[cur] > ary[cur+1]:
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
                changeYN = True

        if not changeYN:
            break
    return ary

def sortQuick(ary, start, end):
    if end <= start:
        return
    
    low = start; high = end

    pivot = ary[(low + high) // 2]
    while low <= high:
        while ary[low] < pivot:
            low += 1
        while ary[high] > pivot:
            high -= 1
        if low <= high:
            ary[low], ary[high] = ary[high], ary[low]
            low, high = low + 1, high - 1

    sortQuick(ary, start, low-1)
    sortQuick(ary, low, end)

def quickSort(ary):
    sortQuick(ary, 0, len(ary)-1)

# 메인코드
tempAry = [random.randint(10000, 99999) for _ in range(1000000)]
tempAry.sort()

rndPos = random.randint(0, len(tempAry)-1)
print('## 데이터 개수 --> ', len(tempAry))
print('## 끼어든 위치 --> ', rndPos)
tempAry.insert(rndPos, tempAry[-1])

bubbleAry = tempAry[:]
quickAry = tempAry[:]

start = time.time()
BubbleSort(bubbleAry)
end = time.time()
print('다시 정렬 시간(버블정렬) --> %10.3f 초' % (end - start))

start = time.time()
quickSort(quickAry)
end = time.time()
print('다시 정렬 시간(퀵정렬) --> %10.3f 초' % (end - start))