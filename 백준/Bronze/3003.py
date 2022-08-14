# https://www.acmicpc.net/problem/3003
# 문제3003번.킹, 퀸, 룩, 비숍, 나이트, 폰
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수
- 0 <= 개수 <= 10
'''



# 출력
'''
1. 주어진 순서대로 몇 개의 피스를 더하거나 빼야 되는지를 출력
- 수가 양수인 경우: 그 개수만큼 피스를 더해야함
- 음수인 경우: 그 개수만큼 피스를 빼야함
- 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수가 각각 1, 1, 2, 2, 2, 8개가 되어야 함
'''



# 코드
import sys

sys.stdin = open('input_text/3003.txt')

peices = list(map(int, input().split()))
normal = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(normal[i] - peices[i], end=' ')   



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)