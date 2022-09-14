# 문제1208번.Flatten
# 시간: 30초, 메모리: 256MB



# 입력
'''
<10개의 테스트 케이스>
1. 덤프 횟수
- 덤프: 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업
- 1 <= 덤프 <= 1,000
2. 각 상자의 높이값
- 1 <= 상자 높이 <= 100
- 가로 길이는 항상 100
'''



# 출력
'''
1. #{테스트케이스} {최고점과 최저점의 높이차}
- 평탄화: 높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업
- 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환
'''



# 코드 1
import sys

sys.stdin = open('../input_text/1208.txt')

for test_case in range(1, 10 + 1):
    N = int(input())   # 덤프 횟수
    heights = list(map(int, input().split()))

    # 평탄화
    while N > 0:
        max_h, max_i = 0, None
        min_h, min_i = 100, None
        for i in range(100):
            if heights[i] > max_h :
                max_h = heights[i]
                max_i = i
            if heights[i] < min_h:
                min_h = heights[i]
                min_i = i
        # 덤프 작업
        heights[max_i] -= 1
        heights[min_i] += 1
        N -= 1
    
    # 최고점과 최저점의 차이
    print(f'#{test_case} {max(heights) - min(heights)}')



# 실행 결과: 성공(메모리:61,408 kb, 시간:158 ms)



# 코드 2
import sys

sys.stdin = open('../input_text/1208.txt')

for test_case in range(1, 10 + 1):
    N = int(input())   # 덤프 횟수
    heights = sorted(list(map(int, input().split())))

    # 평탄화
    while N > 0:
        heights[-1] -= 1
        heights[0] += 1
        heights.sort()
        N -= 1
    
    # 최고점과 최저점의 차이
    print(f'#{test_case} {heights[-1] - heights[0]}')



# 실행 결과: 성공(메모리:58,792 kb, 시간:154 ms)