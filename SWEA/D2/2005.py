# 문제2005번.파스칼의 삼각형
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 파스칼 삼각형의 크기(높이) N
- 1 <= N <= 10
'''



# 출력
'''
1. #{테스트케이스} {파스칼의 삼각형}
<파스칼의 삼각형 특징>
1) 첫 번째 줄은 항상 숫자 1
2) 두 번쨰 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성됨
'''



# 코드 
import sys

sys.stdin = open('../input_text/2005.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # 파스칼의 삼각형 만들기
    triangle = []
    for n in range(1, N + 1):   # 몇 번째 줄인지
        triangle.append([])
        for i in range(n):
            # 자신의 왼쪽과 오른쪽 위의 숫자를 더할 수 있는 경우
            if i - 1 >= 0 and i < n - 1:
                triangle[-1].append(sum(triangle[-2][i - 1:i + 1]))
            else:
                triangle[-1].append(1)

    # 파스칼의 삼각형 출력
    print(f'#{test_case}')
    for row in triangle:
        print(' '.join(map(str, row)))



# 실행 결과: 성공(메모리:56,708 kb, 시간:140 ms)