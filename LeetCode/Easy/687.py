# https://leetcode.com/problems/longest-univalue-path/
# 문제687번.Longest Univalue Path



# 입력
'''
1. 이진 트리의 노드들
- 0 <= 노드 수 <= 10,000
- -1,000 <= Node.val <= 1,000
'''



# 출력
'''
1. 이진 트리에서 동일한 값을 지닌 두 노드간 의 가장 긴 경로의 길이(diameter)를 출력
- 가장 긴 경로는 root를 통과하지 않을 수도 있음
'''



# 코드
import sys

sys.stdin = open('input_text/687.txt')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# print(root)
# TreeNode{val: 5, left: TreeNode{val: 4, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 1, left: None, right: None}}, right: TreeNode{val: 5, left: None, right: TreeNode{val: 5, left: None, right: None}}}

# (이 문제에서의) 상태값: 현재 노드와 동일한 값을 가지는 자식 노드까지의 거리
class Solution:
    longest = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0
            
            # 존재하지 않는 노드까지 DFS 탐색
            left = dfs(node.left)    # 왼쪽 자식 노드의 상태값 
            right = dfs(node.right)  # 오른쪽 자식 노드의 상태값

            # 현재 노드가 자식 노드와 동일한 경우 거리(상태값) 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0   # 초기화
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0   # 초기화
            
            # 왼쪽과 오른쪽 자식 노드 간 거리(상태값)의 합 최댓값이 결과
            self.longest = max(self.longest, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)

        dfs(root)
        return self.longest

        

# 실행 결과: 성공(메모리:17.8 MB, 시간:1016 ms)