class Solution:
    def buildTree(self, inorder, postorder):
        index = {value: i for i, value in enumerate(inorder)}
        post = len(postorder) - 1

        def build(left, right):
            nonlocal post

            if left > right:
                return None

            root_val = postorder[post]
            post -= 1

            root = TreeNode(root_val)

            mid = index[root_val]

            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)