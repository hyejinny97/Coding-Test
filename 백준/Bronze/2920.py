# https://www.acmicpc.net/problem/2920
# 문제2920번.음계
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 8개의 숫자(음)
- 1부터 8까지 숫자가 한번씩 등장
- 'cdefgabC' => '12345678'
'''



# 출력
'''
1. ascending/descending/mixed인지 확인하고 출력
- ascending: 1부터 8까지 차례대로 연주하는 경우
- descending: 8부터 1까지 차례대로 연주하는 경우
- mixed: 위 두개와 같은 상황이 아닌 경우
'''



# 코드
import sys

sys.stdin = open('input_text/2920.txt')

nums = list(map(int, input().split()))

if nums == list(range(1, 8 + 1)):
    print('ascending')
elif nums == list(range(8, 1 - 1, -1)):
    print('descending')
else:
    print('mixed')


# 실행 결과: 성공(메모리:30840kb, 시간:68ms)