# https://www.acmicpc.net/problem/1302
# 문제1302번.베스트셀러
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 오늘 하루동안 팔린 책의 갯수 N
- 0 < N <= 1,000
2. 오늘 팔린 책의 제목
- 0 < 제목의 길이 <= 50
'''



# 출력
'''
1. 가장 많이 팔린 책의 제목을 출력
- 가장 많이 팔린 책이 여러 개인 경우, 사전 순으로 가장 앞서는 제목을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/1302.txt')

# 오늘 하루 팔린 책의 갯수 기록
N = int(input())
sold = {}   # 키: 팔린 책이름, 값: 팔린 책의 갯수
for _ in range(N):
    name = input()
    if not sold.get(name):
        sold[name] = 1
        continue
    sold[name] += 1

# 가장 많이 팔린 책 출력
max_cnt = 0   
max_book = []
for name in sold:
    if sold[name] > max_cnt:
        max_book = [name]   # 초기화
        max_cnt = sold[name]   # 더 큰 값으로 갱신
    elif sold[name] == max_cnt:
        max_book.append(name)

max_book.sort()
print(max_book[0])



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)