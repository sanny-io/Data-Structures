class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value: # go left!
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else: # go right!
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, value):
        if value == self.value:
            return True
        
        if value < self.value and self.left:
            return self.left.contains(value)
        
        if self.right:
            return self.right.contains(value)
        
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        node = self.right

        while node:
            if node.right:
                node = node.right
            else:
                break
        
        return node and node.value or self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, callback):
        callback(self.value)

        if self.left:
            self.left.for_each(callback)
        
        if self.right:
            self.right.for_each(callback)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

    def __repr__(self):
        return str(self.value)