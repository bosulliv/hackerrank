#!/usr/bin/env python3
"""
An implementation of a stack data structure.
Google interview practice. With unit tests.

2018-02-26: Pylint score of 10/10
"""
import unittest

class Stack(object):
    """
    Implementation of stack. With a subtle twist.

    We push and pop from the end as that is much quicker than doing so at the
    front of the array.

    We reverse the order if somebody prints the whole stack.

        >>> s = Stack()
        >>> s.push(3)
        >>> s.push(2)
        >>> s.push(1)
        >>> s.peek()
        1

        >>> s.pop()
        >>> s.peek()
        2

        >>> s.show()
        [3]

    """
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Push item on top of stack"""
        self.stack.append(item)

    def peek(self):
        """Peak at the item on the top of the stack"""
        last = self.stack
        if self.stack:
            last = self.stack[-1]
        return last

    def pop(self):
        """Pop the item off the top of stack and return it"""
        last = self.peek()
        if last:
            del self.stack[-1]
        return last

    def show(self):
        """Show the entire stack.

        Notice we operate on the 'end' of an array for speed.
        So we need to reverse it to show in 'true' stack order.
        """
        return list(reversed(self.stack))


class TestStack(unittest.TestCase):
    """Don't forget, test cases must begin with word test!"""

    def test_push_1(self):
        """Push single item on stack and peek"""
        stk = Stack()
        stk.push(1)
        self.assertEqual(stk.peek(), 1)

    def test_push_pop_empty(self):
        """Push single item, then pop it, then peek the empty stack."""
        stk = Stack()
        stk.push(1)
        stk.pop()
        self.assertEqual(stk.peek(), [])

    def test_push_many(self):
        """Push many items on stack then compare with show"""
        stk = Stack()
        items = list(range(100))
        for i in items:
            stk.push(i)
        self.assertEqual(stk.show(), list(reversed(items)))

    def test_pop_empty(self):
        """Pop and empty stack many times, then show the empty stack"""
        stk = Stack()
        item = stk.pop()
        item = stk.pop()
        item = stk.pop()
        if not item:
            pass
        self.assertEqual(stk.show(), [])

if __name__ == '__main__':
    unittest.main()
