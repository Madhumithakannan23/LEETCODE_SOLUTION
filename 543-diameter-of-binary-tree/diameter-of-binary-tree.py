
class Solution:
    def diameterOfBinaryTree(self, root):
        self.d = 0

        def recursion(root):
            if root is None:
                return 0

            left = recursion(root.left)
            right = recursion(root.right)

            self.d = max(self.d, left + right)

            return 1 + max(left, right)

        recursion(root)
        return self.d

