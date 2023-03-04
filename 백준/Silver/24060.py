# https://www.acmicpc.net/problem/24060
# 문제24060번.알고리즘 수업 - 병합 정렬 1
# 시간: 1초, 메모리: 512MB



# 입력
'''
1. 배열 A의 크기 N, 저장 횟수 K
- 5 <= N <= 500,000
- 1 <= K <= 100,000,000
2. 서로 다른 배열 A의 원소
- 원소: 서로 다른 양의 정수
'''



# 출력
'''
1. 배열 A에 K 번째 저장 되는 수를 출력
- 단, 저장 횟수가 K 보다 작으면 -1을 출력
'''



# 코드

# 접근방법
'''
배열        [4, 5, 1, 3, 2]
분할      [4, 5, 1]    [3, 2]
분할    [4, 5]   [1]  [3]   [2]
분할   [4]  [5]  [1]  [3]   [2]
병합    [4, 5]   [1]    [2, 3]
병합      [1, 4, 5]     [2, 3]
병합        [1, 2, 3, 4, 5]
'''
import sys

sys.stdin = open('input_text/24060.txt')

def merge_sort(A, start, end):  # 분할
  if start < end:
    mid = (start + end) // 2
    merge_sort(A, start, mid)      # 왼쪽 배열 분할
    merge_sort(A, mid + 1, end)  # 오른쪽 베열 분할
    merge(A, start, mid, end)        # 병합정렬


def merge(A, start, mid, end):
  global K, rst
  i, j = start, mid + 1   
  tmp = []          # 병합 정렬 결과
  while i <= mid and j <= end:
    if A[i] <= A[j]:
        tmp.append(A[i])
        i += 1
    else:
      tmp.append(A[j])
      j += 1
    
  while i <= mid:   # 왼쪽 배열 부분이 남은 경우
    tmp.append(A[i])
    i += 1

  while j <= end:   # 오른쪽 배열 부분이 남은 경우
    tmp.append(A[j])
    j += 1

  i, t = start, 0
  while i <= end:   # 병합 정렬 결과를 배열 A에 저장
    A[i] = tmp[t]
    K -= 1
    if K == 0:
      rst = tmp[t]

    i += 1
    t += 1



N, K = map(int, input().split())
arr = list(map(int, input().split()))
rst = None
merge_sort(arr, 0, N - 1)
print(rst if rst else -1)


# 실행 결과: 성공(메모리:90308kb, 시간:2476ms)