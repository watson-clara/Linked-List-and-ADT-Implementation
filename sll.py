# Name: Clara  Watson
# OSU Email: watsoncl@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Linked-List-and-ADT-Implementation
# Due Date: Monday April 15, 2021

from logging import currentframe
from operator import countOf
from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        TODO: This method adds a new node at the beginning of the list
        """
        insert = SLNode(value)
        insert.next = self._head.next
        self._head.next = insert
        

    def insert_back(self, value: object) -> None:
        """
        TODO: This method adds a new node at the end of the list
        """
        insert = SLNode(value)
        if self._head is None: 
            self.insert_front(value)
            return
        current = self._head
        while current.next != None: 
            current = current.next
        current.next = insert 
        
        
        

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: This method inserts a new value at the specified index position in the linked list.
        """
       
        if index < 0:
            raise SLLException
        if index > self.length():
            raise SLLException
        count = 0
        prev = self._head
        node = self._head.next
        cur = prev.next
        if node != cur: 
                cur = node
        while count < index:
            prev = prev.next
            count += 1
        end = prev.next
        prev.next = SLNode(value)
        prev.next.next = end      
                

    def remove_at_index(self, index: int) -> None:
        """
        TODO: This method removes the node at the specified index position from the linked list.
        """
       
        if index < 0:
            raise SLLException
        if index > self.length()-1:
            raise SLLException
        
        count = 0
        prev = self._head
        node = self._head.next
        cur = prev.next
        while count < index:
            if node != cur: 
                cur = node
            prev = prev.next
            count += 1
        cur = node.next
        end = prev.next.next
        prev.next = end

    def remove(self, value: object) -> bool:
        """
        TODO: This method removes the node.
        """
        prev = self._head
        node = False
        cur = prev.next
        if node != cur: 
                cur = node
        while prev.next != None:
            if prev.next.value == value:
                prev.next = prev.next.next
                node = True
                break
            prev = prev.next
        cur = prev.next
        return node

    def count(self, value: object) -> int:
        """
        TODO: This method counts the number of elements in the list that match the provided “value” object. 
        """
        count = 0 
        node = self._head.next
        while node:
            if node.value == value: 
                count = count + 1 
            node = node.next
        return count
        
    def find(self, value: object) -> bool:
        """
        TODO:This method returns a Boolean value based on whether or not the provided “value” object exists in the list.
        """
        node = self._head.next
        while node:
            if node.value == value: 
                return True  
            node = node.next
        return False
        

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        TODO: This method returns a new LinkedList object that contains the requested number of nodes from the original list, starting with the node located at the requested start index
        """
        node = self._head.next
        prev = self._head
        count = 0
        lst = LinkedList()
        if start_index < 0:
             raise SLLException
        if start_index > self.length()-1:
            raise SLLException
        if start_index + size > self.length():
             raise SLLException
        if size < 0:
            raise SLLException
        if size == 0:
            return lst
        cur = prev.next
        while count < start_index -1:
            if node != cur: 
                cur = node
            node = node.next
            count = count +1
        if start_index == 0:
            if size == 0:
                lst.insert_back(node.value)
            else: 
                cur = node
            lst.insert_back(node.value)
            size = size -  1
        while size > 0:
            if node != cur: 
                cur = node
            node = node.next
            lst.insert_back(node.value)
            size = size -  1
        return lst
        
        
        
if __name__ == '__main__':

    print('\n# insert_front example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_front('A')
    lst.insert_front('B')
    lst.insert_front('C')
    print(lst)

    print('\n# insert_back example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_back('C')
    lst.insert_back('B')
    lst.insert_back('A')
    print(lst)

    print('\n# insert_at_index example 1')
    lst = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_at_index example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)

    print('\n# remove example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# remove example 2')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# count example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# find example 1')
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Clause"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Clause"))

    print('\n# slice example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print(lst, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(lst, ll_slice, sep="\n")

    print('\n# slice example 2')
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", lst.slice(index, size))
        except:
            print(" --- exception occurred.")
