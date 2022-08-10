# https://www.acmicpc.net/problem/10101
# 문제10101번.삼각형 외우기
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 3개의 줄에 걸쳐 삼각형의 각의 크기가 각각 주어짐
- 0 < 각 크기 < 180
'''



# 출력
'''
1. Equilateral, Isoscelec, Scalence, Error 중 하나를 출력
- 세 각의 크기가 모두 60인 경우
- 세 각의 합이 180이고, 두 각이 같은 경우
- 세 각의 합이 180이고, 같은 각이 없는 경우
- 세 각의 합이 180이 아닌 경우
'''



# 코드
import sys

sys.stdin = open('input_text/10101.txt')

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
sum_3 = angle1 + angle2 + angle3

if sum_3 == 180:
    if angle1 == angle2 == angle3:
        print('Equilateral')
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)