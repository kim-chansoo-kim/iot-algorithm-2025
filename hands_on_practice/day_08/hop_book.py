from operator import itemgetter

# 함수
def makeIndex(ary,pos):
    beforeAry = []
    index = 0
    for data in ary:
        beforeAry.append((data[pos], index))
        index += 1

    sortedAry = sorted(beforeAry, key=itemgetter(0))
    return sortedAry

def bookSearch(ary, data):
    pos = -1
    start = 0
    end = len(ary) - 1

    while (start <= end):
        mid = (start + end) // 2
        if data == ary[mid][0]:
            return ary[mid][1]
        elif data > ary[mid][0]:
            start = mid + 1
        else:
            end = mid - 1

    return pos

# 변수
bookAry = [['어린왕자', '쌩떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'], 
           ['신곡', '단테'], ['돈키호테', '세르반테스'], ['동물농장', '조지오웰'], 
           ['데미안', '헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅']]
nameIndex = []
authIndex = []

# main
print('# 책장의 도서 --> ', bookAry)
nameIndex = makeIndex(bookAry, 0)
print('# 도서명 색인표 --> ', nameIndex)
authIndex = makeIndex(bookAry, 1)
print('# 작가명 색인표 --> ', authIndex)

findName = input('책을 입력하세요 : ')
findPos = bookSearch(nameIndex, findName)
if findPos != -1:
    print(findName, '의 작가는', bookAry[findPos][1], '입니다.')
else:
    print('책이 없습니다.')

findName = input('작가를 입력하세요 : ')
findPos = bookSearch(authIndex, findName)
if findPos != -1:
    print(findName, '의 도서는', bookAry[findPos][0], '입니다.')
else:
    print(findName, '작가는 없습니다.')