"""Binary Tree + Search + Traversal"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val) -> None:
        pass


class BST:
    def __init__(self, val) -> None:
        self.root = TreeNode(val)

    def insert(self, val) -> None:
        self.root.insert(val)


def inorderTraversal(root: TreeNode) -> List[int]:
    # Inorder = node is visited second (l-n-r)
    # Base case: root is None -> return nada
    if root is None:
        return
    # Recursive case: return call self on left + [root.val] + call self on right
    left = inorderTraversal(root.left) or []
    right = inorderTraversal(root.right) or []
    return left + [root.val] + right


def inorderTraversal(self, root: TreeNode) -> List[int]:
    if root is None:
        return  # Base case: root is None -> return nada
    # Recursive: return call self on left + [root.val] + call self on right
    left = self.inorderTraversal(root.left) or []
    right = self.inorderTraversal(root.right) or []
    return left + [root.val] + right


def preorderTraversal(self, root: TreeNode) -> List[int]:
    if root is None:
        return  # Base case: root is None -> return nada
    # Recursive: return call self on left + [root.val] + call self on right
    left = self.preorderTraversal(root.left) or []
    right = self.preorderTraversal(root.right) or []
    return [root.val] + left + right


def postorderTraversal(self, root: TreeNode) -> List[int]:
    if root is None:
        return  # Base case: root is None -> return nada
    # Recursive: return call self on left + [root.val] + call self on right
    left = self.postorderTraversal(root.left) or []
    right = self.postorderTraversal(root.right) or []
    return left + right + [root.val]
