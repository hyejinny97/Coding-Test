# https://leetcode.com/problems/diameter-of-binary-tree/
# 문제543번.Diameter of Binary Tree



# 입력
'''
1. 이진 트리의 노드들
- 0 <= 노드 수 <= 10,000
- -100 <= Node.val <= 100
'''



# 출력
'''
1. 이진 트리에서 두 노드간 가장 긴 경로의 길이(diameter)를 출력
- 가장 긴 경로는 root를 통과하지 않을 수도 있음
'''



# 코드
import sys

sys.stdin = open('input_text/543.txt')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# print(root)의 결과
# TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 5, left: None, right: None}}, right: TreeNode{val: 3, left: None, right: None}}

class Solution:
    longest = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if not node:
                return -1
            
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)    # 왼쪽 자식 노드의 상태값
            right = dfs(node.right)  # 오른쪽 자식 노드의 상태값

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 현재 노드의 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest
      


# 실행 결과: 성공(메모리:16.3 MB, 시간:46 ms)