# https://leetcode.com/problems/invert-binary-tree/
# 문제617번.Merge Two Binary Trees


# 입력
"""
1. 이진 트리의 노드들 1, 이진 트리의 노드들 2
- 0 <= 노드 수 <= 2,000
- -10,000 <= Node.val <= 10,000
"""


# 출력
"""
1. 주어진 이진 트리를 병합한 후, root를 반환
- 중복되는 노드의 값은 합산
"""


# 코드
import sys

sys.stdin = open("input_text/617.txt")


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, t1: Optional[TreeNode], t2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)

            return node
        else:
            return t1 or t2


# 실행 결과: 성공(메모리:15.5 MB, 시간:128 ms)
