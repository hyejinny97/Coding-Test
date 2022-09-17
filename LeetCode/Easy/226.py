# https://leetcode.com/problems/invert-binary-tree/
# 문제226번.Invert Binary Tree



# 입력
'''
1. 이진 트리의 노드들
- 0 <= 노드 수 <= 100
- -100 <= Node.val <= 100
'''



# 출력
'''
1. 주어진 이진 트리를 반전시킨 후, root를 반환
'''



# 코드 1 - 파이썬다운 방식(재귀)
import sys

sys.stdin = open('input_text/226.txt')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# print(root)
# TreeNode{val: 4, left: TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}, right: TreeNode{val: 7, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}}


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None



# 실행 결과: 성공(메모리:13.8 MB, 시간:55 ms)



# 코드 2 - 반복 구조로 BFS를 이용해 풀이
import sys
from collections import deque

sys.stdin = open('input_text/226.txt')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# print(root)
# TreeNode{val: 4, left: TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}, right: TreeNode{val: 7, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}}


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        while q:
            node = q.popleft()   # 현재 노드
            if node:
                # 자식노드 스왑
                node.left, node.right = node.right, node.left

                q.append(node.left)
                q.append(node.right)
        return root
        


# 실행 결과: 성공(메모리:13.8 MB, 시간:44 ms)



# 코드 3 - 반복 구조로 DFS를 이용해 풀이
import sys

sys.stdin = open('input_text/226.txt')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# print(root)
# TreeNode{val: 4, left: TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}, right: TreeNode{val: 7, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}}


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()   # 현재 노드
            if node:
                # 자식노드 스왑
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)
        return root
        


# 실행 결과: 성공(메모리:13.8 MB, 시간:44 ms)