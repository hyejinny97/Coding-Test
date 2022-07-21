# 문제1989.초심자의 회문 검사
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트 케이스 개수 T
2. 단어 한개
- 3 <= 단어 길이 <= 10
'''

# 출력
'''
1. #테스트케이스
2. 단어가 회문구조이면 1, 아니면 0을 출력
'''

# 접근방법
'''
<접근방법1>
1. 문자를 뒤집어서 원래 문자와 같은지 비교하면 쉽게 구할 수 있다
<접근방법2>
1. left, right 포인터를 만든다
2. left 포인터는 단어를 왼쪽에서 오른쪽으로 스캔해가고, right 포인터는 단어를 오른쪽에서 왼쪽으로 스캔해나간다
3. 두 포인터가 가리키는 알파벳이 같으면 계속 이동하고, 다르면 break를 걸고 0을 출력한다
4. 두 포인터가 같은 인덱스에 도달했거나 left 인덱스 > right 인덱스가 된 경우에는 회문구조가 맞으므로 break로 빠져나와서 1을 출력
'''

# 코드 1 
import sys

sys.stdin = open('SWEA/input_text/1989.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    word = input()
    print(f'#{test_case} {1 if word == word[::-1] else 0}')

# 실행 결과: 성공(메모리:56,688 kb, 시간:129 ms)


# 코드 2
sys.stdin = open('SWEA/input_text/1989.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    word = input()
    left = 0   # 가장 첫번째 인덱스
    right = len(word) - 1   # 가장 마지막 인덱스
    rst = 1   # 초기값: 회문구조 O
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            rst = 0
            break
    
    print(f'#{test_case} {rst}')

# 실행 결과: 성공(메모리:56,680 kb, 시간:136 ms)