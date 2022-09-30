# 문제8931번.제로
# 시간: 30초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 T
2. 정수 K
- 1 <= K <= 100,000
3. K개의 줄에 정수가 하나씩 주어짐
- 0 <= 정수 <= 100,000
"""


# 출력
"""
1. #{테스트케이스} {받아 적은 수의 합}
- 만약 정수가 0일 경우에는 최근에 쓰고 지우지 않았던 수를 지워야 하며, 그렇지 않을 경우 해당 수를 써야 함
"""


# 코드
import sys

sys.stdin = open("../input_text/8931.txt")

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())
    stack = []

    for _ in range(K):
        num = int(input())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)

    print(f"#{test_case} {sum(stack)}")


# 실행 결과: 성공()
