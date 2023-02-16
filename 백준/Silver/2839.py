# https://www.acmicpc.net/problem/2839
# 문제2839번.설탕 배달
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 배달해야하는 설탕 무게 N
- 3 ≤ N ≤ 5,000
'''



# 출력
'''
1. 상근이가 배달하는 봉지의 최소 개수를 출력
- 정확하게 N킬로그램을 만들 수 없다면 -1을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2839.txt')

N = int(input())

for cnt_5 in range(N // 5, 0 - 1, -1):
    if (N - 5 * cnt_5) % 3 == 0:
        cnt_3 = (N - 5 * cnt_5) // 3
        print(cnt_5 + cnt_3)
        break
else:
    print(-1)


# 실행 결과: 성공(메모리:31256kb, 시간:88ms)