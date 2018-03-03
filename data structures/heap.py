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

2018-02-28: Pylint score of 9.64/10
"""
import unittest

class Heap(object):
    """
    Binary Heap, using an array.
    """
    def __init__(self):
        self.heap = []

    def check_sides(self, lst):
        """
        No sides is a valid heap.
        Left must be full before right.
        Left must be bigger than right.
        """
        if not lst[0] and not lst[1]:
            return True
        elif not lst[0] and lst[1]:
            return False
        elif lst[0] and not lst[1]:
            return True
        else:
            return lst[0] >= lst[1]

    def check_top(self, lst):
        """Check top is biggest"""
        if not lst:
            # Empty list is false
            return False
        
        return max(lst) == lst[0]

    def check(self, lst):
        """
        Check a list is a valid binary heap.
        The top node must be the largest for all elements below.
        The left must be bigger than the right.
        Trees must always be filled left to right.
        """
        if not lst:
            # empty list is false
            return False
        elif len(lst) == 1:
            # A single sub-tree is a valid heap
            return True
        elif len(lst) in [2, 3]:
            l_top = self.check_top(lst)
            l_side = self.check_sides(lst[1:3])
            log = l_top & l_side
            return log


class TestHeap(unittest.TestCase):
    """Don't forget, test cases must begin with word test!"""
    def test_top_smallest(self):
        """Check small top is not okay"""
        heap = Heap()
        lst = [0, 1, 2]
        self.assertTrue(not heap.check_top(lst))

    def test_top_biggest(self):
        """Check biggest top is okay, with equal sides"""
        heap = Heap()
        lst = [2, 1, 1]
        self.assertTrue(heap.check_top(lst))

    def test_top_biggest_none(self):
        """Check top with empty sides"""
        heap = Heap()
        lst = [2]
        self.assertTrue(heap.check_top(lst))

    def test_check_smallest(self):
        """Small top is wrong"""
        heap = Heap()
        lst = [0, 1, 2]
        self.assertTrue(not heap.check(lst))

    def test_check_biggest(self):
        """Large top is good"""
        heap = Heap()
        lst = [2, 1, 0]
        self.assertTrue(heap.check(lst))

    def test_check_single_item(self):
        """Check single item is okay"""
        heap = Heap()
        lst = [0]
        self.assertTrue(heap.check(lst))

    def test_check_empty_item(self):
        """Empty list is not okay"""
        heap = Heap()
        lst = []
        self.assertTrue(not heap.check(lst))

    def test_check_equal_sides(self):
        """equal sides are okay"""
        heap = Heap()
        lst = [3, 1, 1]
        self.assertTrue(heap.check(lst))

    def test_check_right_side_high(self):
        """larger right side is not okay"""
        heap = Heap()
        lst = [3, 1, 2]
        self.assertTrue(not heap.check(lst))

    def test_sides_okay(self):
        """Check sides are okay"""
        heap = Heap()
        lst = [3, 2]
        self.assertTrue(heap.check_sides(lst))

    def test_sides_right_bigger(self):
        """Check right bigger than left is not okay"""
        heap = Heap()
        lst = [2, 3]
        self.assertTrue(not heap.check_sides(lst))

    def test_sides_left_only(self):
        """Check one side is okay"""
        heap = Heap()
        lst = [3, None]
        self.assertTrue(heap.check_sides(lst))

    def test_sides_none(self):
        """Check None is okay"""
        heap = Heap()
        lst = [None, None]
        self.assertTrue(heap.check_sides(lst))

    def test_sides_right_only(self):
        """Check right only is not okay"""
        heap = Heap()
        lst = [None, 2]
        self.assertTrue(not heap.check_sides(lst))

if __name__ == '__main__':
    unittest.main()
