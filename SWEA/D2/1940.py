# 문제1940.가랏! RC카! (문제가 좀 이상한 것 같다..)
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트케이스 갯수 T
2. command 수 N
- 2 <= N <= 30
3. N개의 command들
- command 종류: 0(가속도 유지), 1(가속), 2(감속)
- 가속도의 단위: m/s^2
- RC카의 초기 속도는 0 m/s
- 가속도의 값은 1 m/s^2 또는 2 m/s^2
- 현재 속도보다 감속할 속도가 더 클 경우, 속도는 0 m/s가 됨
'''

# 출력
'''
1. #테스트케이스
2. N개의 command를 모두 수행했을떄, N초동안 이동한 거리를 계산해 출력
'''

# 접근방법
'''
<문제 접근 전>
1. 가속도(x m/s^2): 1초마다 x m/s씩 속도 변화
- 가속(x m/s^2): 1초마다 x m/s씩 속도 증가
- 감속(x m/s^2): 1초마다 x m/s씩 속도 감소
2. 이동거리: 1초동안 x m/s 속도로 이동하면 총 이동거리는 x m가 됨
<1번 테스트케이스 풀이 과정 설명>
1. 2 m/s^2 가속
- 1초마다 2 m/s씩 속도 증가
- 1초동안 2 m/s 속도로 이동했으므로, 이동거리는 2 m
2. 1 m/s^2 감속
- 1초마다 1 m/s씩 속도 감소
- 1초마다 (2-1) m/s 속도로 이동했으므로, 이동거리는 1 m
3. 따라서 총 이동거리는 (2 + 1) m
'''

# 코드 1
import sys

sys.stdin = open('SWEA/input_text/1940.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tot_dis = 0   # 총 이동거리
    prev_vel = 0   # 이전 속도
    for _ in range(N):
        # 가속도에 따라 변화된 현재 속도 구하기
        now_vel = prev_vel   # 현재 속도
        acc = input().split()
        # 가속할 경우
        if acc[0] == '1':   
            now_vel += int(acc[1])
        # 감속할 경우
        elif acc[0] == '2':
            if prev_vel < int(acc[1]):   # 현재 속도보다 감속할 속도가 더 큰 경우
                now_vel = 0
            else:
                now_vel -= int(acc[1])
        
        # 1초동안 계산한 속도로 이동한 거리 구해서 더하기 
        tot_dis += 1 * now_vel
        prev_vel = now_vel
        
    print(f'#{test_case} {tot_dis}')

# 실행 결과: 성공(메모리:56,928 kb, 시간:146 ms)