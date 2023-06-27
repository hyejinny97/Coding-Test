# https://school.programmers.co.kr/learn/courses/30/lessons/178870
# 코딩테스트연습 < 연습문제 < 문제.연속된 부분 수열의 합



# 입력
'''
1. 수열을 나타내는 정수 배열 sequence
- 5 ≤ sequence의 길이 ≤ 1,000,000
- 1 ≤ sequence의 원소 ≤ 1,000
- sequence는 비내림차순으로 정렬되어 있음
2. 부분 수열의 합을 나타내는 정수 k
- 5 ≤ k ≤ 1,000,000,000
'''



# 출력
'''
1. 조건을 만족하는 부분 수열의 시작 인덱스와 마지막 인덱스를 배열에 담아 return
- 수열의 인덱스는 0부터 시작

<부분 수열 조건>
- 부분 수열의 합은 k
- 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾음
- 길이가 짧은 수열이 여러 개인 경우 시작 인덱스가 작은 수열을 찾음
'''



# 코드 1

# 접근방법
'''
sequence를 idx 0부터 끝까지 순회하면서,
현재 idx까지 sequence가 있다고 가정을 하고,
현재 idx에 해당하는 수열을 포함한 부분 수열의 합 중에 k가 존재하는지 확인
'''
import sys

sys.stdin = open('input_text/연속된부분수열의합.txt')

def solution(sequence, k):
    rst = [0, 1000001]  
    for i in range(len(sequence)):
        sum_subseq = sequence[i]  # 부분 수열의 합
        j = i
        while sum_subseq < k and (j - 1) >= 0:
            j -= 1
            sum_subseq += sequence[j]
        
        if sum_subseq != k:
            continue
        
        # (부분 수열의 합 = k)인 경우
        if (rst[1] - rst[0]) > (i - j):
            rst = [j, i]
        elif (rst[1] - rst[0]) == (i - j):
            if rst[0] > j:
                rst = [j, i]

    return rst


# 실행 결과: 실패(일부 TC 시간초과)



# 코드 2

# 접근방법
'''
위 코드에 '누적합'을 적용시키자
'''
import sys

sys.stdin = open('input_text/연속된부분수열의합.txt')

def solution(sequence, k):
    # 누적합
    new_sequence = [0] + [sequence[0]]
    for i in range(1, len(sequence)):
        new_sequence.append(sequence[i] + new_sequence[-1])

    rst = [0, 1000001]  
    for i in range(1, len(sequence) + 1):
        sub_seq = False  # (연속된 부분 수열의 합 = k) 조건 만족 여부
        j = i
        while (j - 1) >= 0:
            if (new_sequence[i] - new_sequence[j - 1]) < k:
                j -= 1
                continue
            elif (new_sequence[i] - new_sequence[j - 1]) == k:
                sub_seq = True
            break
        
        if not sub_seq:
            continue
        
        # (부분 수열의 합 = k)인 경우
        start, end = j - 1, i - 1
        if (rst[1] - rst[0]) > (end - start):
            rst = [start, end]
        elif (rst[1] - rst[0]) == (end - start):
            if rst[0] > start:
                rst = [start, end]

    return rst


# 실행 결과: 실패(시간초과)



# 코드 3

# 접근방법
'''
투 포인터 이용
참고) https://school.programmers.co.kr/questions/48640
'''
import sys

sys.stdin = open('input_text/연속된부분수열의합.txt')

def solution(sequence, k):
    rst = [0, 1000001] 
    sub_sum = sequence[0]

    right = 0
    for left in range(len(sequence)):
        while right + 1 < len(sequence) and sub_sum < k:
            right += 1
            sub_sum += sequence[right]
        
        if sub_sum == k:
            if (rst[1] - rst[0]) > (right - left):
                rst = [left, right]
            elif (rst[1] - rst[0]) == (right - left):
                if rst[0] > left:
                    rst = [left, right]
        
        sub_sum -= sequence[left]

    return rst


# 실행 결과: 성공