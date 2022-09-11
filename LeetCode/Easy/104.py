# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 문제104번.Maximum Depth of Binary Tree



# 입력
'''
1. 이진 트리의 노드들
- 0 <= 노드 수 <= 10,000
- -100 <= Node.val <= 100
'''



# 출력
'''
1. 이진 트리의 최대 깊이 출력
'''



# 코드
import sys
from collections import deque

sys.stdin = open('input_text/104.txt')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# print(root)의 결과
# ⇒ TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        q = deque([root])
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                cur_root = q.popleft()
                if cur_root.left:
                    q.append(cur_root.left)
                if cur_root.right:
                    q.append(cur_root.right)
        return depth
        


# 실행 결과: 성공(메모리:15.3 MB, 시간:48 ms)