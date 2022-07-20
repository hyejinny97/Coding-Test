# 문제1204.최빈수 구하기
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트 케이스 총 개수 T
2. 테스트 케이스의 번호
3. 1000명의 학생들의 각 점수
- 0 <= 점수 <= 100
'''

# 출력
'''
1. #테스트케이스
2. 최빈수 출력
- 최빈수가 여러 개일때는 가장 큰 점수를 출력
'''

# 코드 1
import sys

sys.stdin = open('SWEA/input_text/1204.txt', 'r')

T = int(input())
for _ in range(T):
    test_case = int(input())
    scores = map(int, input().split())
    
    # 0점부터 100점까지 학생들이 받은 점수에 따라 학생 수 카운트 
    # 인덱스: 점수, 값: 해당 점수를 받은 학생 수
    cnt = [0] * 101   
    for score in scores:
        cnt[score] += 1
    
    # 최빈값 구하기
    mode_cnt = -1
    mode_score = []
    for i in range(len(cnt)):
        # 특정 점수를 받은 학생 수가 더 많을 때마다 갱신
        if mode_cnt < cnt[i]:
            mode_cnt = cnt[i]   
            mode_score = []   # 초기화
            mode_score.append(i)
        # 현재까지의 학생수 최빈값과 동일한 학생수를 가지는 또다른 점수가 있다면 추가
        elif mode_cnt == cnt[i]:
            mode_score.append(i)
    
    print(f'#{test_case} {max(mode_score)}')

# 실행 결과: 성공(메모리:56,704 kb, 시간:144 ms)


# 코드 2
sys.stdin = open('SWEA/input_text/1204.txt', 'r')

T = int(input())
for _ in range(T):
    test_case = int(input())
    scores = map(int, input().split())
    
    # 0점부터 100점까지 학생들이 받은 점수에 따라 학생 수 카운트 
    # 인덱스: 점수, 값: 해당 점수를 받은 학생 수
    cnt = [0] * 101   
    for score in scores:
        cnt[score] += 1
    
    # 최빈값 구하기
    mode_score = []
    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            mode_score.append(i)
    
    print(f'#{test_case} {max(mode_score)}')

# 실행 결과: 성공(메모리:60,372 kb, 시간:150 ms)
