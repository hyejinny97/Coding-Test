# 문제10912번.외로운 문자
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 수 T 
2. 알파벳 소문자만으로 이루어진 문자열
- 1 <= 문자열 길이 <= 100
'''



# 출력
'''
1. #{테스트케이스} {같은 두 문자들을 짝지은 후, 남는 문자를 사전 순서대로 출력}
- 어떤 문자도 남지 않는다면 “Good”을 출력
'''



# 코드
import sys

sys.stdin = open('../input_text/10912.txt')

T = int(input())
for test_case in range(1, T + 1):
    string = input()
    
    # 문자열을 순회하면서 문자 짝짓기
    check = set()
    for s in string:
        if s not in check:
            check.add(s)
        else:
            check.remove(s)
    
    if check:
        print(f'#{test_case}', ''.join(sorted(check)))
    else: 
        print(f'#{test_case} Good')



# 실행 결과: 성공(메모리:62,724 kb, 시간:335 ms)