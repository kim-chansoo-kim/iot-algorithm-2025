# iot-algorithm-2025
IoT 개발자 자료구조와 알고리즘(코딩테스트) 리포지토리 2025

## 1일차

### 자료구조
- 데이터를 구성하고 효율적으로 관리하는 형태

#### 자료구조 종류
- 단순 자료구조
    - 정수, 실수, 문자, 문자열

- 선형 자료구조
    - 배열, 리스트, 스택, 큐

- 비선형 자료구조
    - 트리, 그래프

- 파일 자료구조
    - 순차파일, 색인파일, 직접파일

### 알고리즘
- 문제를 해결하는 논리적인 방법, 순서

#### 알고리즘 성능
- `빅오 표기법`(빠른 순서)
    - $O(1)$ : 데이터 수에 관계없이 항상 일정한 시간이 걸리는 것
    - $O(log n)$ : 단순 for문인데 전체 중 일부만 처리하는 것
    - $O(n)$ : 단순 for문
    - $O(n log n)$ : 이중 for문인데 안쪽 for문이 전체 중 일부만 처리
    - $O(n^2)$ : 이중 for문
    - $O(n^3)$ : 삼중 for문
    - $O(2^n)$ : 팩토리얼 등등...(가장 느림)

### 리스트 복습
- 1차원, 2차원
    - 리스트 생성, 인덱싱, 슬라이싱(!), 함수들...
    - 2차원 행, 렬 개념, 생성...

## 2일차

- 기초문법
    - 리스트 컴프리헨션 복습 : [노트북](./day02/da01_list_again.ipynb)

- 자료구조
    - 선형 리스트 : [노트북](./day02/da02_linear_list.ipynb)
    - 연결 리스트 : [노트북](./day02/da04_linked_list.ipynb)

## 3일차
- 자료구조
    - 연결 리스트 
        - 연결리스트 구현 : [파이썬](./day03/da01_linked_list.py)
        - 이중연결 리스트, 원형 리스트
        - 파이썬 list() : 연결리스트와 유사
        - 연결 리스트 실습 : 
            - 주소록[파이썬](./hands_on_practice/hop_linked.py)
            - 헨젤과 그래텔[파이썬](./hands_on_practice/hop_cook.py)
            - URL[파이썬](./hands_on_practice/hop_url.py)
        - 원형 연결 리스트 - 시작노드 변경시 오버헤드 없음
        - 이중 연결 리스트 - 앞에서 검색, 뒤에서 검색 용이
        - 연결 리스트 사용예 - 가상 메모리 관리, 윈도우 이벤트 관리 ...

    - 스택 : [노트북](./day03/da02_stack.ipynb)
        - 노트북 참조
        - 알고리즘 DFS(깊이우선탐색)시 스택 사용
        - 스택 구현 : [파이썬](./day03/da03_stack.py)

    - 큐 : [노트북](./day03/da04_queue.ipynb)
        - 개념, 노트북 참조
        - 알고리즘 BFS(너비우선탐색)시 사용

## 4일차
- 자료구조
    - 큐
        - 큐 구현 : [파이썬](./day04/da01_queue.py)
        - 원형 큐 구현[파이썬](./hands_on_practice/hop_cirqueue.py)
        - 맛집 대기열[파이썬](./hands_on_practice/hop_rest.py)

    - 이진 트리 : [노트북](./day04/da02_binary_tree.ipynb)
        - 컴퓨터 시스템 등 많은 분야에서 사용
        - 이진 트리 구현 : [파이썬](./day04/da03_binary_tree.py)
        - 이진 트리 실습
            - 편의점[파이썬](./hands_on_practice/hop_conve.py)
            - 폴더 및 하위 폴더에 중복된 파일 이름 찾기[파이썬](./hands_on_practice/hop_duplication_file.py)

## 5일차
- 자료구조
    - 그래프 : [노트북](./day05/da01_graph.ipynb)
        - 깊이우선탐색 : [파이썬](./day05/da02_dfs.py)
            - 최소비용신장트리 : [파이썬](./day05/da03_min_cost_spanningtree.py)
            - 허니버터칩 실습 : [파이썬](./hands_on_practice/hop_honey.py)

    - 재귀호출 : [노트북](./day05/da04_recursive_call.ipynb)

## 6일차
- 자료구조/알고리즘
    - 재귀호출
        - 재귀호출 연습
        
    - 정렬