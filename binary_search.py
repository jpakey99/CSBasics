import unittest


class Tree:
    def __init__(self, root, left_tree, right_tree):
        self.root : int = root
        self.right_tree : Tree = right_tree
        self.left_tree : Tree = left_tree


def binary_search(tree:Tree, value):
    # value should be in increasing order from left to right
    if tree is None:
        return False
    elif tree.root == value:
        return True
    elif tree is None:
        return False
    elif value < tree.root:
        return binary_search(tree.left_tree, value)
    elif value > tree.root:
        return binary_search(tree.right_tree, value)


# test cases
class BinarySearchTest(unittest.TestCase):
    def test_one_node__search_complete(self):
        tree = Tree(50, None, None)
        self.assertTrue(binary_search(tree, 50), '50 is at root')

    def test_one_node_value_not_in_tree(self):
        tree = Tree(50, None, None)
        self.assertFalse(binary_search(tree, 55), '50 is at root')


if __name__ == '__main__':
    tree = Tree(root=50, left_tree=Tree(root=40, left_tree=None, right_tree=None), right_tree=Tree(root=60, left_tree=None, right_tree=None))
    print(binary_search(tree, 50))