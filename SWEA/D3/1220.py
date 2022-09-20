# 문제1220번.Magnetic
# 시간: 30초, 메모리: 256MB



# 입력
'''
<총 10개의 테스트 케이스 T>
1. 정사각형 테이블의 한 변의 길이 (항상 100)
2. 100개의 줄에 정사각형 테이블의 정보가 주어짐
- 100 x 100 크기의 테이블
- 1: N극 자성체
- 2: S극 자성체
- N극은 테이블 위, S극은 테이블 아래에 위치 
'''



# 출력
'''
1. #{테스트케이스} {교착 상태의 개수}
- 테이블에서 일정 간격을 두고 강한 자기장을 걸었을 때, 시간이 흐른 뒤에 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수를 구해야 함
- 한 쪽 방향으로 움직이는 자성체의 개수가 많더라도 반대 방향으로 움직이는 자성체가 하나라도 있으면 교착 상태에 빠져 움직이지 않음
- 자성체끼리는 반응하지 않음
'''



# 코드
import sys

sys.stdin = open('../input_text/1220.txt')

T = 10
for test_case in range(1, T + 1):
    # 100 x 100 크기의 테이블을 2차원 리스트로 생성
    row_size = int(input())
    matrix = [input().split() for _ in range(row_size)]

    # 100 x 100 크기의 테이블을 아래에서 위로 읽어나가면서, '2' -> '1'쌍 갯수 세기
    cnt = 0   # 총 교착 상태의 갯수
    for c in range(0, 99 + 1):
        magnetics = "" 
        for r in range(99, 0 - 1, -1):
            if matrix[r][c] != '0':
                magnetics += matrix[r][c]
        cnt += magnetics.count("21")
    
    print(f'#{test_case} {cnt}') 

    

# 실행 결과: 성공(메모리:62,476 kb, 시간:194 ms)