from tree_visualizer.tree_node import TreeNode


def buildTree(level_order_list):
    def _dfs(i):
        # ``None`` is a placeholder for a missing node in the indexed layout.
        if i >= len(level_order_list) or level_order_list[i] is None:
            return None

        left = _dfs(2 * i + 1)
        right = _dfs(2 * i + 2)

        node = TreeNode(level_order_list[i], left, right)
        return node

    return _dfs(0)


def getHeight(root):
    if root is None:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))


def drawTree(root):
    h = getHeight(root)
    # Number of nodes possible on the last level
    max_nodes = 2 ** (h - 1)

    # Minimum number of spaces between leaf nodes
    spacing = 3

    # Width of the entire canvas
    cols = max_nodes + spacing * (max_nodes - 1)

    # Leave one empty row between each tree level.
    rows = 2 * h - 1

    grid = [[" " for _ in range(cols)] for _ in range(rows)]

    def _drawTree(node, row, col, gap):
        if node is None:
            return

        grid[row][col] = str(node.val)
        _drawTree(node.left, row + 2, col - gap, gap // 2)
        _drawTree(node.right, row + 2, col + gap, gap // 2)

    _drawTree(root, 0, (cols - 1) // 2, max_nodes)

    for row in grid:
        print("".join(row).rstrip())
