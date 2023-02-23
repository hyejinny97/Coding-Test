# https://www.acmicpc.net/problem/11650
# 문제11650번.좌표 정렬하기
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 점의 개수 N
- 1 ≤ N ≤ 100,000
2. N개의 줄에 각 점의 위치(x, y)
- -100,000 ≤ xi, yi ≤ 100,000
- 위치가 같은 두 점은 없음
'''



# 출력
'''
1. N개의 줄에 점을 정렬한 결과를 출력
- x좌표가 증가하는 순으로 정렬
- x좌표가 같으면 y좌표가 증가하는 순서로 정렬
'''



# 코드 
import sys

sys.stdin = open('input_text/11650.txt')

# N개의 좌표 모두 입력받기
N = int(input())
points = []
for _ in range(N):
    points.append(list(map(int, input().split())))

# 좌표가 증가하는 순으로 정렬
points.sort(key=lambda point: (point[0], point[1]))
for point in points:
    print(*point)


# 실행 결과: 성공(메모리:58180kb, 시간:4408ms)
