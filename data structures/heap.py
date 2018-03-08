#!/usr/bin/env python3
r"""
An implementation of a binary heap structure.
Google interview practice. With unit tests.
This uses an array to hold the heap.

A sorted list in descending order will build a heap. So this array creates this
binary heap:

    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

             9
          /     \
         8       7
       /   \    / \
      6     5  4   3
     / \   /
    2   1 0

A binary heap has these rules:

   * A sub-tree of a max heap must have its biggest value at the top.
   * It must always be filled left to right, with no gaps on the left.

By this definition, we can add these observations:

   * It doesn't matter if sibling trees are bigger or smaller, so long
     as the trees have the biggest at the top.
   * It doesn't matter the order of the left and right nodes when
     present, they just have to be smaller than all those above.
   * As such, a binary heap is only partially ordered.

2018-02-28: Pylint score of 9.55/10
"""
import unittest

class Heap(object):
    """
    Binary Heap, using an array.
    """
    def __init__(self, heap=[]):
        self.heap = heap

    def parent(self, child):
        """
        Given the position of a child, return the position of the parent
        """
        if child % 2 == 0:
            parent = (child-2)/2
        else:
            parent = (child-1)/2
        return int(parent)

    def swap(self, child):
        """ Swap a child with its parent """
        print('swap')
        temp = self.heap[child]
        par = self.parent(child)
        self.heap[child] = self.heap[par]
        self.heap[par] = temp

    def check(self, child):
        """
        Check if a given child is smaller than its parent.
        If it isn't, swap it. Then keep checking the new
        parent until its in the correct position.
        """
        if child == 0:
            return

        par = self.parent(child)
        if self.heap[child] > self.heap[par]:
            self.swap(child)
            # After swap, check again
            self.check(par)
            self.check(child)
        else:
            return

    def heapify(self):
        """
        Given a list heap, turn into a binary heap by swapping
        children with parent if they are larger.
        The stragegy #1 is to work from the bottom and work our
        way to the top.
        """
        i = len(self.heap) - 1
        while i > 0:
            self.check(i)
            i = i - 1


class TestHeap(unittest.TestCase):
    """Don't forget, test cases must begin with word test!"""
    def test_child_bigger_lvl_1(self):
        """Position one is in wrong place. Check it moves."""
        lst = [3, 4, 2, 1, 0]
        ok_lst = [4, 3, 2, 1, 0]
        heap = Heap(lst)
        heap.check(1)
        self.assertListEqual(heap.heap, ok_lst)

    def test_child_bigger_lvl_2(self):
        """Position three is in wrong place. Check it moves."""
        lst = [1, 3, 2, 4, 0]
        ok_lst = [4, 3, 2, 1, 0]
        heap = Heap(lst)
        heap.check(3)
        self.assertListEqual(heap.heap, ok_lst)

    def test_child_smaller_lvl_1(self):
        """Check a valid heap doesn't need to change"""
        lst = [4, 3, 2, 1, 0]
        ok_lst = lst
        heap = Heap(lst)
        heap.check(1)
        self.assertListEqual(heap.heap, ok_lst)

    def test_child_smaller_lvl_2(self):
        """Check a valid heap doesn't need to change"""
        lst = [4, 3, 2, 1, 0]
        ok_lst = lst
        heap = Heap(lst)
        heap.check(3)
        self.assertListEqual(heap.heap, ok_lst)

    def test_heapify_swap_1(self):
        """Check we can heapify a heap with one item in the wrong place"""
        lst = [1, 3, 2, 4, 0]
        ok_lst = [4, 3, 2, 1, 0]
        heap = Heap(lst)
        heap.heapify()
        self.assertListEqual(heap.heap, ok_lst)

    def test_heapify_swap_all(self):
        """Check we cna heapify a worst case heap. Back to front"""
        lst = [0, 1, 2, 3, 4]
        ok_lst = [4, 3, 2, 1, 0]
        heap = Heap(lst)
        heap.heapify()
        self.assertListEqual(heap.heap, ok_lst)

if __name__ == '__main__':
    unittest.main()
