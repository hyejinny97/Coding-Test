# https://www.acmicpc.net/problem/2525
# 문제2525번.오븐 시계
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 현재 시각 A시 B분
- 0 <= A <= 23
- 0 <= B <= 59
2. 요리하는 데 필요한 시간 C
- 0 <= C <= 1,000
'''



# 출력
'''
1. 오븐구이가 끝나는 시각을 출력
- 종료되는 시각의 시와 분을 공백을 사이에 두고 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2525.txt')

now_h, now_m = map(int, input().split())
cooking_time = int(input())

end_m = (now_m + cooking_time) % 60
end_h = (now_h + (now_m + cooking_time) // 60) % 24

print(end_h, end_m)


# 실행 결과: 성공(메모리:30616kb, 시간:68ms)