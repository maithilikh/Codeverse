def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    tr = []
    def iot(node):
        if not node:
            return
        iot(node.left)
        tr.append(node.val)
        iot(node.right)
    iot(root)
    return tr
