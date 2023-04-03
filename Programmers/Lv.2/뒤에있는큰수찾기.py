# https://school.programmers.co.kr/learn/courses/30/lessons/154539
# 코딩테스트연습 < 연습문제 < 문제.뒤에 있는 큰 수 찾기



# 입력
'''
1. 정수로 이루어진 배열 numbers
- 4 ≤ numbers의 길이 ≤ 1,000,000
- 1 <= number <= 1,000,000
'''



# 출력
'''
1. 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return
- 뒷 큰수: 배열의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수
- 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담음
'''



# 코드 1
import sys

sys.stdin = open('input_text/뒤에있는큰수찾기.txt')

def solution(numbers):
    rst = []
    for i in range(len(numbers)):  # 기준 숫자
        for j in range(i + 1, len(numbers)):  # 비교할 숫자
            if numbers[i] < numbers[j]:
                rst.append(numbers[j])
                break
        else:
            rst.append(-1)

    return rst


# 실행 결과: 실패(시간초과)



# 코드 2

# 접근방법
'''
(|: 기준, ←→: 비교대상)

1) 코드 1번 풀이: 내(기준) '뒤'에 숫자(비교) 중 자신보다 '크고' 가까이 있는 수
numbers  2 3 3 5
         | ←---→
           | ←-→
              | →
                |

2) 코드 2번 풀이: 내(기준) '앞'에 숫자(비교) 중 자신보다 '작은' 수
numbers  2 3 3 5
         |
         ← |
           ← | 
           ←--→ |
'''
import sys

sys.stdin = open('input_text/뒤에있는큰수찾기.txt')

def solution(numbers):
    answer = [-1] * (len(numbers))
    stack = []   # 아직 뒷큰수를 못찾은 인덱스
    for i in range(len(numbers)):  
        while stack and numbers[stack[-1]] < numbers[i]: 
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer

# 실행 결과: 성공