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
