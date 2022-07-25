# https://www.acmicpc.net/problem/2577
# 문제2577.숫자의 개수
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 자연수 A
2. 자연수 B
3. 자연수 C
- 100 <= A, B, C <= 1,000
'''



# 출력
'''
1. A x B x C의 결과에 0이 몇번 쓰였는지 출력
2. A x B x C의 결과에 1이 몇번 쓰였는지 출력
...
10. A x B x C의 결과에 9이 몇번 쓰였는지 출력
'''



# 코드
import sys

sys.stdin = open("input_text/0_숫자의개수.txt")

# 3개의 자연수를 입력받아 A, B, C 변수에 할당
A = int(input())
B = int(input())
C = int(input())

# 3개의 자연수 곱하기
multiply = A * B * C

# 곱한 값을 for 반복문으로 돌면서 리스트 자료형에 기록
cnts = [0] * 10   # 인덱스 == 0~9, 값 == 각 숫자의 갯수(0으로 초기화)
for num in str(multiply):
    cnts[int(num)] += 1

# 0부터 9까지 숫자 갯수를 차례로 출력
for cnt in cnts:
    print(cnt)



# 실행결과(메모리:30840KB, 68ms)