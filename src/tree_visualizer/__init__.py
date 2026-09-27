import random
import string

from tree_visualizer.tree import buildTree, drawTree


def main():
    # True marks a node position; None leaves that indexed position empty.
    # Every call receives newly random lowercase labels.
    tree_shapes = {
        "complete tree": [True, True, True, True, True, True, True],
        "uneven tree": [True, True, True, True, None, None, True],
        "left-skewed tree": [True, True, None, True, None, None, None, True],
        "right-skewed tree": [True, None, True, None, None, None, True, None, None, None, None, None, None, None, True],
        "zig-zag tree": [True, True, True, None, True, True, None],
    }

    for name, shape in tree_shapes.items():
        tree_list = [
            random.choice(string.ascii_lowercase) if node else None
            for node in shape
        ]
        print(f"{name}: {tree_list}")
        drawTree(buildTree(tree_list))
        print()


if __name__ == "__main__":
    main()
