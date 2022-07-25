# 세자리수 2개를 입력 받아 변수 A,B에 할당
A, B = input().split()

# A, B 값 뒤집은 후 크기 비교
print(B[::-1] if A[::-1] < B[::-1] else A[::-1])