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