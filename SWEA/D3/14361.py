# 문제14361번.숫자가 같은 배수
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 자연수 N
- 1 <= N <= 1,000,000
'''



# 출력
'''
1. #{테스트케이스} {주어진 자연수에 나타난 숫자들을 재배열하여 더 큰 배수를 만들 수 있다면 ‘possible’, 불가능하다면 ‘impossible'}
'''



# 코드 1
import sys

sys.stdin = open('../input_text/14361.txt')

T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    nums = set(str(num))
    possible = False
    x = 2
    while True:
        mul = x * num
        if len(str(num)) < len(str(mul)):
            break
        
        if set(str(mul)) == nums:
            possible = True
            break
        x += 1
    
    if possible:
        print(f'#{test_case} possible')
    else:
        print(f'#{test_case} impossible')
    
    
   
# 실행 결과: 성공(메모리:56,936 kb, 시간:145 ms)



# 코드 2
import sys

sys.stdin = open('../input_text/14361.txt')

T = int(input())
for test_case in range(1, T + 1):
    num = input()
    sorted_num = sorted(num)
    possible = False
    for x in range(2, 10):
        mul = x * int(num)
        if sorted(str(mul)) == sorted_num:
            possible = True
            break
    
    if possible:
        print(f'#{test_case} possible')
    else:
        print(f'#{test_case} impossible')
    
    
   
# 실행 결과: 성공(메모리:56,924 kb, 시간:151 ms)