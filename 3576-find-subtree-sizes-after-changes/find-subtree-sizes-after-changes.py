
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        def dfs(node):
            ch = s[node]
            old = last.get(ch)

            if old is not None:
                new_parent[node] = old

            last[ch] = node

            for child in children[node]:
                dfs(child)

            if old is None:
                last.pop(ch)
            else:
                last[ch] = old

        dfs(0)

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        answer = [1] * n

        def count(node):
            for child in new_children[node]:
                answer[node] += count(child)
            return answer[node]

        count(0)

        return answer

