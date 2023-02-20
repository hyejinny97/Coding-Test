# https://www.acmicpc.net/problem/2566
# 문제2566번.최댓값
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 아홉 번째 줄까지 한 줄에 정수 아홉 개
- 0 <= 정수 <= 100
'''



# 출력
'''
1. 9×9 격자판에 쓰여진 81개의 정수 중 최댓값을 출력
2. 최댓값이 위치한 행 번호와 열 번호 출력
- 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2566.txt')

# 9 x 9 크기의 행렬
matrix = [list(map(int, input().split())) for _ in range(9)]

# 최댓값, 최댓값 위치 구하기
max_value = -1     # 최댓값
location = ()      # 최댓값 위치
for r in range(9):
    for c in range(9):
        if matrix[r][c] > max_value:
            max_value = matrix[r][c]
            location = (r + 1, c + 1)

print(max_value)
print(*location)


# 실행결과(메모리:31256KB, 시간:40ms)