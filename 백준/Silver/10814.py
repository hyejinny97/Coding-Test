# https://www.acmicpc.net/problem/10814
# 문제10814번.나이순 정렬
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 회원의 수 N
- 1 ≤ N ≤ 100,000
2. N개의 줄에는 각 회원의 나이와 이름
- 입력은 가입한 순서로 주어짐!
- 1 <= 나이 <= 200
- 0 < 이름 길이 <= 10
'''



# 출력
'''
1. N개의 줄에 걸쳐 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/10814.txt')

# N명의 회원 정보 입력받기
N = int(input())
members = []
for _ in range(N):
    age, name = input().split()
    members.append((int(age), name))

# 회원을 나이순, 가입한 순으로 정렬
members.sort(key=lambda member: member[0])
for member in members:
    print(*member)


# 실행 결과: 성공(메모리:46276kb, 시간:3948ms)
