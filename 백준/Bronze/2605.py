# https://www.acmicpc.net/problem/2605
# 문제2605번.줄 세우기
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 학생의 수 N
- 0 < N <= 100
2. 줄을 선 차례대로 학생들이 뽑은 번호
- 0 <= 번호
'''



# 출력
'''
1. 학생들이 처음에 줄을 선 순서대로 1번부터 번호를 매길 때, 학생들이 최종적으로 줄을 선 순서를 그 번호로 출력
'''



# 코드
import sys

sys.stdin = open("input_text/2605.txt")

N = int(input())
nums = [0] + list(map(int, input().split()))   # 인덱스: 1~N번 학생번호, 값: 뽑은 번호
rst = [0]   # 인덱스: 줄을 선 순서, 값: 1~N번 학생번호 
for i in range(1, N + 1):
    # 줄에 서야하는 위치 = 학생번호 - 뽑은 번호
    rst.insert(i - nums[i], i)

print(*rst[1:])



# 실행 결과: 성공(메모리:30864kb, 시간:68ms)