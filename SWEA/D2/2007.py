# 문제2007번.패턴 마디의 길이
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 길이가 30인 문자열
'''



# 출력
'''
1. #{테스트케이스} {마디의 길이}
- 마디: 패턴에서 반복되는 부분
'''



# 코드 
import sys

sys.stdin = open('../input_text/2007.txt')

T = int(input())
for test_case in range(1, T + 1):
    strings = input()

    # 슬라이싱 크기를 점차 증가시키면서 마디 찾기
    size = 1
    while True:
        # 마디가 맞는지 확인
        if strings[0:size] == strings[size:2 * size]:
            break

        size += 1    

    print(f'#{test_case} {size}')



# 실행 결과: 성공(메모리:56,676 kb, 시간:130 ms)