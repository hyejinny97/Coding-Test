# https://www.acmicpc.net/problem/2495
# 문제2495번.연속구간
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 3개의 줄에 각각 여덟자리 정수
'''



# 출력
'''
1. 3개의 줄에 각각 입력되 수 내에서 같은 숫자가 연속하여 나오는 가장 긴 길이를 출력
- 연속해서 같은 숫자가 나오는 것이 없으면 1 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2495.txt')

for _ in range(3):
    num = input()

    cnt = 1
    max_cnt = 1
    for i in range(0, 6 + 1):   # 앞에서부터 여덟자리 확인
        if num[i] == num[i + 1]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1   # 초기화
    
    # 끝부분에 연속된 수도 갱신해줘야 함
    max_cnt = max(max_cnt, cnt)

    print(max_cnt)



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)