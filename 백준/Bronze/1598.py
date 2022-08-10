# https://www.acmicpc.net/problem/1598
# 문제1598번.꼬리를 무는 숫자 나열
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 두 개의 자연수
- 0 < 수 <= 10,000,000
'''



# 출력
'''
1. 두 개의 자연수 사이의 직각거리 출력
- 4줄짜리 표에 왼쪽부터 수를 아래로 1부터 순서대로 적어감
- 직각거리 = 동서방향거리 + 남북방향거리
'''



# 코드 1
import sys

sys.stdin = open('input_text/1598.txt')

# 가로 좌표 위치 찾기
def find_x(num):  
    return num // 4 if num % 4 == 0 else num // 4 + 1

# 세로 좌표 위치 찾기
def find_y(num):
    return 4 if num % 4 == 0 else num % 4


n1, n2 = map(int, input().split())

# 동서방향거리
dx = abs(find_x(n1) - find_x(n2))
# 남북방향거리
dy = abs(find_y(n1) - find_y(n2))
# 직각거리
print(dx + dy)



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)



# 코드 2
import sys

sys.stdin = open('input_text/1598.txt')

# 가로 좌표 위치 찾기
def find_x(num):  
    return (num - 1) // 4

# 세로 좌표 위치 찾기
def find_y(num):
    return (num - 1) % 4


n1, n2 = map(int, input().split())

# 동서방향거리
dx = abs(find_x(n1) - find_x(n2))
# 남북방향거리
dy = abs(find_y(n1) - find_y(n2))
# 직각거리
print(dx + dy)



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)