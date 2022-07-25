# 6081: 16진수 구구단 출력하기
# 시간제한:1초 / 메모리제한:128MB
# hexa = [1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
# 10진수로 16x16단을 작성한 후, 각 숫자를 16진수로 변환

hexa = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
dan = hexa[input()]
for i in range(1, 15 + 1):
    print(f'{dan:X}*{i:X}={(dan * i):X}')