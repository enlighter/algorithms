class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryFreeTree:
    def __init__(self, root):
        self.root = Node(root)
        self.print_tree_selector = {
            'preorder': self.preorder_print,
            'inorder': self.inorder_print,
            'postorder': self.postorder_print
        }

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self, traversal_mode='inorder'):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        print_tree_method = self.print_tree_selector[traversal_mode]
        return print_tree_method(self.root, "")

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start is not None:
            if start.value == find_val:
                return True
            left_search = self.preorder_search(start.left, find_val)
            if left_search:
                return True
            else:
                return self.preorder_search(start.right, find_val)
        ## Alternative
        # if start:
        #     if start.value == find_val:
        #         return True
        #     else:
        #         return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    @staticmethod
    def __populate_traversal(traversal, value):
        if not traversal:
            # first item being added to traversal
            traversal += str(value)
        else:
            traversal += '-' + str(value)
        return traversal

    @classmethod
    def preorder_print(cls, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start is not None:
            traversal = cls.__populate_traversal(traversal, start.value)
            traversal = cls.preorder_print(start.left, traversal)
            traversal = cls.preorder_print(start.right, traversal)
        return traversal

    @classmethod
    def inorder_print(cls, start, traversal):
        if start is not None:
            traversal = cls.inorder_print(start.left, traversal)
            traversal = cls.__populate_traversal(traversal, start.value)
            traversal = cls.inorder_print(start.right, traversal)
        return traversal

    @classmethod
    def postorder_print(cls, start, traversal):
        if start is not None:
            traversal = cls.postorder_print(start.left, traversal)
            traversal = cls.postorder_print(start.right, traversal)
            traversal = cls.__populate_traversal(traversal, start.value)
        return traversal


if __name__ == '__main__':
    # Set up tree
    tree = BinaryFreeTree(4)
    tree.root.left = Node(2)
    tree.root.right = Node(5)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(3)

    # Test search
    # Should be True
    print(tree.search(4))
    # Should be False
    print(tree.search(6))

    # Test print_tree
    # Should be 1-2-4-5-3
    print('preorder traversal', tree.print_tree('preorder'))
    print('inorder traversal', tree.print_tree('inorder'))
    print('postorder traversal', tree.print_tree('postorder'))
