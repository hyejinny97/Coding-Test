# https://www.acmicpc.net/problem/4673
# 문제4673번.셀프 넘버
# 시간: 1초, 메모리: 256MB



# 입력
'''
없음
'''



# 출력
'''
1. 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력
- d(n) = n + n의 각 자리수의 합
- n: d(n)의 생성자
- 셀프 넘버: 생성자가 없는 숫자
'''



# 코드
# import sys

# sys.stdin = open('input_text/2920.txt')

# 인덱스:1부터 10000까지 수, 값: 해당 인덱스가 셀프넘버이면 True
self_number = [True] * 10001   

for num in range(1, 10000 + 1):
    dn = num + sum([int(n) for n in str(num)])
    if dn <= 10000:
        self_number[dn] = False

for idx in range(1, 10000 + 1):
    if self_number[idx]:
        print(idx)



# 실행 결과: 성공(메모리:30840kb, 시간:80ms)