def scoreSort(ary):
    n = len(ary)
    for end in range(1, n): # end -> 1...n-1
        for cur in range(end, 0, -1): # cur -> 거꾸로
            if(ary[cur - 1][1] > ary[cur][1]):
                ary[cur - 1], ary[cur] = ary[cur], ary[cur - 1]
        print(f'정렬 중 -> {scoreAry}')
    return ary

scoreAry = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]

print(f'정렬 전 -> {scoreAry}')
dataAry = scoreSort(scoreAry)
print(f'정렬 후 -> {scoreAry}')

print('## 성적별 조 편성표 ##')
for i in range(len(scoreAry)//2):
    print(scoreAry[i][0], ':', scoreAry[len(scoreAry)-1-i][0])