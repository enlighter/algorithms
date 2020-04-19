class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
        self._print_tree_selector = {
            'preorder': self._preorder_print,
            'inorder': self._inorder_print,
            'postorder': self._postorder_print
        }

    def insert(self, new_val):
        pass

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.__preorder_search(self.root, find_val)

    def print_tree(self, traversal_mode='inorder'):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        print_tree_method = self._print_tree_selector[traversal_mode]
        return print_tree_method(self.root, "")

    def __preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start is not None:
            if start.value == find_val:
                return True
            left_search = self.__preorder_search(start.left, find_val)
            if left_search:
                return True
            else:
                return self.__preorder_search(start.right, find_val)
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
    def _preorder_print(cls, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start is not None:
            traversal = cls.__populate_traversal(traversal, start.value)
            traversal = cls._preorder_print(start.left, traversal)
            traversal = cls._preorder_print(start.right, traversal)
        return traversal

    @classmethod
    def _inorder_print(cls, start, traversal):
        if start is not None:
            traversal = cls._inorder_print(start.left, traversal)
            traversal = cls.__populate_traversal(traversal, start.value)
            traversal = cls._inorder_print(start.right, traversal)
        return traversal

    @classmethod
    def _postorder_print(cls, start, traversal):
        if start is not None:
            traversal = cls._postorder_print(start.left, traversal)
            traversal = cls._postorder_print(start.right, traversal)
            traversal = cls.__populate_traversal(traversal, start.value)
        return traversal


class BST(BinaryTree):
    def __init__(self, root):
        super().__init__(root)

    def insert(self, new_val):
        current_node = self.root
        while current_node is not None:
            if new_val < current_node.value and current_node.left is None:
                current_node.left = Node(new_val)
                return
            if new_val >= current_node.value and current_node.right is None:
                current_node.right = Node(new_val)
                return
            if new_val < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
    ## Alternative
    # def insert(self, new_val):
    #     self.insert_helper(self.root, new_val)
    #
    # def insert_helper(self, current, new_val):
    #     if current.value < new_val:
    #         if current.right:
    #             self.insert_helper(current.right, new_val)
    #         else:
    #             current.right = Node(new_val)
    #     else:
    #         if current.left:
    #             self.insert_helper(current.left, new_val)
    #         else:
    #             current.left = Node(new_val)

    def search(self, find_val):
        current_node = self.root
        while current_node is not None:
            if current_node.value == find_val:
                return True
            if find_val < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
    ## Alternative
    # def search(self, find_val):
    #     return self.search_helper(self.root, find_val)
    #
    # def search_helper(self, current, find_val):
    #     if current:
    #         if current.value == find_val:
    #             return True
    #         elif current.value < find_val:
    #             return self.search_helper(current.right, find_val)
    #         else:
    #             return self.search_helper(current.left, find_val)
    #     return False


if __name__ == '__main__':
    # Set up tree
    tree = BinaryTree(4)
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

    # Set up BST
    tree = BST(4)

    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(3)
    tree.insert(5)

    # Check search
    # Should be True
    print(tree.search(4))
    # Should be False
    print(tree.search(6))

    # def test(start):
    #     if start is not None:
    #         print(start.value)
    #         print('left')
    #         test(start.left)
    #         print(start.value)
    #         print('right')
    #         test(start.right)
    # test(tree.root)

    # Test print_tree
    # Should be 1-2-4-5-3
    print('preorder traversal', tree.print_tree('preorder'))
    print('inorder traversal', tree.print_tree('inorder'))
    print('postorder traversal', tree.print_tree('postorder'))
