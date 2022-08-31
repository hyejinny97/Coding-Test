# 문제13547번.팔씨름
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. K번만큼의 팔씨름 결과
- 1 <= K <= 15
- 결과는 o또는 x로 나타남
'''



# 출력
'''
1. #{테스트케이스} {점심값을 면제받을 가능성이 있다면 ‘YES’, 없다면 ‘NO’}
- 15번 팔씨름을 하여 8번 이상 이기면 점심값을 면제 받을 수 있음
'''



# 코드
import sys

sys.stdin = open('../input_text/13547.txt')

T = int(input())
for test_case in range(1, T + 1):
    play = input()
    
    # 앞으로 이겨야 하는 횟수(= 8 - 승리한 횟수)가 남은 경기 횟수보다 작으면 "YES"
    if 8 - play.count("o") <= 15 - len(play):
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')



# 실행 결과: 성공(메모리:58,508 kb, 시간:149 ms)