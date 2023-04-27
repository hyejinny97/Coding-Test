# https://www.acmicpc.net/problem/26069
# 문제26069번.붙임성 좋은 총총이
# 시간: 1초, 메모리: 1024MB



# 입력
'''
1. 사람들이 만난 기록의 수 N
- 1 <= N <= 1,000
2. N개의 줄에 각각 사람들이 만난 기록(사람A, 사람B)
- 0 < 이름 A,B 길이 <= 20
- 사람의 이름은 대소문자를 구분함
'''



# 출력
'''
1. 마지막 기록 이후 무지개 댄스를 추는 사람의 수를 출력
- 총총이(ChongChong)는 춤을 춤
- 무지개 댄스를 추지 않고 있던 사람이 무지개 댄스를 추고 있던 사람을 만나게 된다면, 만난 시점 이후로 무지개 댄스를 추게됨
'''



# 코드 
import sys

sys.stdin = open('input_text/26069.txt')

N = int(input())
dance_people = {'ChongChong'}  # 현재 춤을 추는 사람들 명단

for _ in range(N):
    p1, p2 = input().split()
    if (p1 in dance_people) or (p2 in dance_people):
        dance_people.add(p1)
        dance_people.add(p2)

print(len(dance_people))


# 실행 결과: 성공(메모리:31256kb, 시간:76ms)

