"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

import math

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        node = ListNode(value)

        self.length += 1

        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        node = ListNode(value)

        self.length += 1

        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1

        if not self.head and not self.tail:
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        highest_value = -math.inf
        node = self.head

        while node:
            if node.value > highest_value:
                highest_value = node.value

            node = node.next
        
        return highest_value

class Stack:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(ListNode(value))

    def pop(self):
        if self.len() == 0:
            return None
        
        return self.storage.remove_from_tail().value

    def len(self):
        return self.storage.length

class Queue:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(ListNode(value))

    def dequeue(self):
        if self.len() == 0:
            return None
        
        return self.storage.remove_from_head().value

    def len(self):
        return self.storage.length


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
        if self.left:
            self.left.in_order_print(node)
        
        print(self.value)

        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)

        while queue.len() > 0:
            node = queue.dequeue()

            print(node.value)

            if node.left:
                queue.enqueue(node.left)
            
            if node.right:
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)

        while stack.len() > 0:
            node = stack.pop()

            print(node.value)

            if node.left:
                stack.push(node.left)
            
            if node.right:
                stack.push(node.right)

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