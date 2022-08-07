# https://www.acmicpc.net/problem/1076
# 문제1076번.저항
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 첫번째 색
2. 두번째 색
3. 세번째 색
'''



# 출력
'''
1. 저항의 저항값을 계산해서 출력
- 처음 색 2개는 저항의 값
- 마지막 색은 곱해야하는 값
'''



# 코드
import sys

sys.stdin = open('input_text/1076.txt')

colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
colors = dict(zip(colors, range(0, 9 + 1)))

r = ''
for n in range(1, 3 + 1):
    color = input()
    
    # 첫번째와 두번째 색
    if n <= 2:
        r += str(colors[color])
    
    # 마지막 색
    else:
        mul = 10 ** colors[color]
        r = int(r) * mul

print(r)



# 실행 결과: 성공(메모리:30840kb, 시간:84ms)