# 문제13229번.일요일
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 문자열 S
'''



# 출력
'''
1. #{테스트케이스} {다음 일요일까지 며칠 남았는지 출력}
'''



# 코드
import sys

sys.stdin = open('../input_text/13229.txt')

# 요일마다 번호부여
days = {
    "SUN": 7,
    "MON": 6,
    "TUE": 5,
    "WED": 4,
    "THU": 3,
    "FRI": 2,
    "SAT": 1
}

T = int(input())
for test_case in range(1, T + 1):
    day = input()
    print(f'#{test_case} {days[day]}')



# 실행 결과: 성공(메모리:58,524 kb, 시간:150 ms)