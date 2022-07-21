# 문제1946.간단한 압축 풀기
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트케이스 갯수 T
2. 압축된 문서의 알파벳과 숫자 쌍의 개수 N
- 1 <= N <= 10
3. N개의 줄에 알파벳 C와 숫자 K가 주어진다
- A <= 알파벳 C <= Z
- 1 <= 숫자 K <= 20
'''

# 출력
'''
1. #테스트케이스
2. 원본 문서를 출력
- 원본 문서의 너비는 10으로 고정됨
- 입력된 각 숫자K만큼 공백없이 알파벳C가 채워져야 함
'''

# 코드 1 - 알파벳 전체를 모두 담고 10개씩 쪼개나감
import sys

sys.stdin = open('SWEA/input_text/1946.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    original = '' # 원본문서를 담을 곳
    # 원본문서에 압축된 파일 풀어서 담기
    for _ in range(N):
        alph, num = input().split()
        original += alph * int(num)
    
    # 글자를 10개씩 끊어서 출력
    print(f'#{test_case}')
    start = 0   # 시작 인덱스
    while start < len(original):
        # 마지막 줄이 아닌 경우
        if start + 10 < len(original):
            print(original[start:start + 10])
        # 마지막 줄인 경우
        else: 
            print(original[start:])
        start += 10

# 실행 결과: 성공(메모리:56,676 kb, 시간:136 ms)


# 코드 2 - 처음 알파벳을 담을 때부터 10씩 담기
sys.stdin = open('SWEA/input_text/1946.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    print(f'#{test_case}')
    original = ''  # 원본문서를 담을 곳
    cnt = 0  
    for n in range(N):
        alph, num = input().split()
        for _ in range(int(num)):
            if cnt == 10:
                print(original)
                original = ''   # 초기화
                cnt = 0    # 초기화
            original += alph
            cnt += 1
        
        # 마지막줄 출력
        if n == N - 1 and original:
            print(original)
            original = ''   # 초기화
            cnt = 0    # 초기화

# 실행 결과: 성공(메모리:56,928 kb, 시간:142 ms)