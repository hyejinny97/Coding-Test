# 문제1206번.View
# 시간: 테스트 케이스 10개 합쳐 30초, 메모리: 256MB



# 입력
'''
<10개의 테스트 케이스 T>
1. 건물의 갯수 N
- 4 <= N <= 1,000
2. N개의 건물의 높이
- 0 <= 높이 <= 255
- 맨 왼쪽 두칸과 맨 오른쪽 두칸에서 건물의 높이는 항상 0
'''



# 출력
'''
1. #{테스트케이스} {조망권이 확보된 세대의 수}
- 조망권 확보 조건: 양쪽 모두 거리 2 이상의 공간이 확보될 경우
'''



# 접근 방법
'''
- 왼쪽 건물(인덱스 -1, -2 위치의 건물), 오른쪽 건물(인덱스 +1, +2 위치의 건물)과 비교
- 만약 현 건물보다 양쪽 건물 중 한 건물이라도 더 높을 경우(diff=now-prev <= 0), 더 볼것 없이 다음 건물로 넘어가기
- 만약 양쪽 건물이 모두 낮을 경우 (diff=now-prev > 0), min(diff들)만큼 조망권 획득 가능
'''



# 코드
import sys

sys.stdin = open('../input_text/1206.txt')


for test_case in range(1, 10 + 1):
    N = int(input())   # 건물의 갯수
    buidings = list(map(int, input().split()))   # N개의 건물 높이
    good_place = 0   # 조망권이 확보된 세대 수
    for i in range(2, N - 2):
        now = buidings[i]
        # 왼쪽 건물과 비교
        if now - buidings[i - 1] <= 0 or now - buidings[i - 2] <= 0:
            continue
        # 오른쪽 건물과 비교
        elif now - buidings[i + 1] <= 0 or now - buidings[i + 2] <= 0:
            continue
     
        good_place += min(now - buidings[i - 1], now - buidings[i - 2], now - buidings[i + 1], now - buidings[i + 2])
    
    print(f'#{test_case} {good_place}')



# 실행 결과: 성공(메모리:60,628 kb, 시간:172 ms)