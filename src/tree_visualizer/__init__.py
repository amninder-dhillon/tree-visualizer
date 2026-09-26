from collections import deque

from tree_visualizer.tree import buildTree

from .tree_node import TreeNode


def main():

    def bfs(node):
        ans = []
        if node is None:
            return []
        q = deque()
        q.append(node)

        while q:
            ll = len(q)
            level = []
            for _ in range(ll):
                curr = q.popleft()
                level.append(str(curr.val))
                if curr.left is not None:
                    q.append(curr.left)

                if curr.right is not None:
                    q.append(curr.right)

            ans.append(level)

        return ans

    tree = [1, 2, 3, 4, 5, 6, 7]
    levels = bfs(buildTree(tree))
    h = len(levels)
    gap = 2 ** (h - 1)
    max_nodes = 2 ** (h - 1)
    spacing = 3
    cols = max_nodes + (spacing * (max_nodes - 1))
    rows = h

    grid = [[" " for _ in range(cols)] for _ in range(rows)]
    mid_col = (cols - 1) // 2
    grid[0][mid_col] = levels[0][0]
    i = 1
    gap = gap // 2

    v1 = mid_col - gap
    v2 = mid_col + gap
    grid[1][mid_col - gap] = levels[1][0]
    grid[1][mid_col + gap] = levels[1][1]

    gap = gap // 2
    grid[2][v1 - gap] = levels[2][0]
    grid[2][v1 + gap] = levels[2][1]
    grid[2][v2 - gap] = levels[2][2]
    grid[2][v2 + gap] = levels[2][3]

    for r in range(rows):
        print(*grid[r])
        print()


if __name__ == "__main__":
    main()
