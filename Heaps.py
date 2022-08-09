##############################################
# Title: PA4 - Heaps
# Author: Rhea Toves
# Version: 1.0
# Date: March 28, 2022
#
# Description: This assignment displays the use of
# BinaryHeap, BinaryMaxHeap, and TernaryMaxHeap.
###############################################

import numpy.random as rand
import sys

class BinaryMaxHeap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def __str__(self):
        return str(self.heap_list)

    def __len__(self):
        return self.size

    def __contains__(self, item):
        return item in self.heap_list

    def is_empty(self):
        # Compare the size attribute to 0
        return self.size == 0

    def find_max(self):
        # Finds the largest item is at the root node (index 1)
        if self.size < 0:
            max_val = self.heap_list[1]
            return max_val
        return None

    def insert(self, item):
        # Appends the item to the end of the list
        self.heap_list.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def del_max(self):
        # The max item in the tree is at the root and replaces the root with the last item in the list.
        max_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.heap_list.pop()
        self.size = self.size - 1
        self.percolate_down(1)
        return max_val

    def max_child(self, index):
        # This method returns the index of the largest child. If there is no right child, return the left child.
        # If there are two children, return the smallest of the two.
        if index * 2 + 1 < self.size:
            return index * 2
        else:
            if self.heap_list[index * 2] > self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def build_heap(self, alist):
        # Build a heap from a list of keys to establish complete tree property
        index = len(alist) // 2 # any nodes past the halfway point are leaves
        self.size = len(alist)
        self.heap_list = [0] + alist[:]
        while index > 0:
            self.percolate_down(index)
            index -= 1

    def percolate_up(self, index):
        # Take the index as a starting point and located the parent value.
        # This method is called within the insert() method above.
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index //= 2

    def percolate_down(self, index):
        # Compares the current node value with the other values down the index.
        # This method is called within the del_max() method above.
        while (index * 2) <= self.size:
            mc = self.max_child(index)
            # Below is where the swapping of data points occur
            if self.heap_list[index] > self.heap_list[mc]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[mc]
                self.heap_list[mc] = temp
            index = mc

    def remove(self, item):
        # Removes an item from the heap. The item may not be at the root of the heap.
        if self.is_empty():
            return
        if item is None:
            return
        item_index = -1
        for n in self.heap_list:
            if n == item:
                item_index = self.heap_list.index(n)
            if item_index != -1:
                self.heap_list[item_index] = -sys.maxsize-1
                self.percolate_up(item_index)
                self.del_max()

class TernaryMaxHeap:
    def __init__(self):
        # Initializes the ternary heap
        self.heap_list = [0]
        self.size = 3
        self.item = []
        self.type = max

    def __str__(self):
        return str(self.heap_list)

    def __len__(self):
        return self.size

    def __contains__(self, item):
        return item in self.heap_list

    def is_empty(self):
        # Compare the size attribute to 0
        return self.size == 0

    def get_length(self):
        # Returns the length
        return len(self.item)

    def insert(self, item):
        # Appends the item to the end of the list
        self.heap_list.append(item)
        self.size += 1

    def top(self):
        # Returns the item at the top of the heap
        return self.item[0]

    def delete(self):
        # Deletes items directed in main or other functions
        self.item.pop()
        if self.item:
            self.going_down(0)

    def get_parent(self, temp):
        # Finds the parent index
        return (temp - 2) // self.size + 1

    def get_children(self, temp):
        # Finds the index of the three possible children
        first_child = temp * self.size - 1
        second_child = temp * self.size
        third_child = temp * self.size + 1
        return first_child, second_child, third_child

    def going_down(self, temp):
        # Function to shift downwards after deletion has taken place
        curr = self.item[temp]
        while True:
            child = tuple((self.item[x], x) for x in self.get_children(temp))
            if not child:
                return
            element, element1 = self.type(child)
            if self.type(curr, element) is curr:
                return
            self.item[element1], self.item[temp], temp = curr, element, element1

    def going_up(self, temp):
        # Function to shift upwards after deletion has taken place
        curr = self.item[temp]
        while temp:
            parent1 = self.get_parent(temp)
            parent = self.item[parent1]
            if self.type(parent, curr) is parent:
                return
            self.item[parent1], self.item[temp], temp = curr, parent, parent1

def main():
    h = TernaryMaxHeap()
    p = BinaryMaxHeap()

    for i in range(1, 11):
        x = rand.randint(1, 100)
        h.insert(x)

    print("TernaryMaxHeap Test: ", h)

    for i in range(1, 11):
        x = rand.randint(1, 100)
        p.insert(x)

    print("BinaryMaxHeap Test: ", p)

main()