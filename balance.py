# balance.py
# ===================================================
# Using a stack to check for unbalanced parentheses
# ===================================================

import numpy as np
import sys

class MyStack():
    def __init__(self):
        """ Initialize stack with np.array set to 4 capacity by default """
        self._array = np.empty([4], str)
        self._capacity = 4
        self._size = 0

    def __str__(self):
        """ Returns the array in string form """
        return str(self._array[:self._size])

    def re_size(self):
        """ Doubles the array capacity """
        new_array = np.empty([self._capacity * 2], str)

        for i in range(self._size):
            new_array[i] = self._array[i]

        self._array  = new_array
        self._capacity = self._capacity * 2

    def push(self, string):
        """ Push a string onto stack after checking capacity """
        for i in range(len(string)):
            if self._size == self._capacity:
                self.re_size()

            self._array[self._size] = string[i]
            self._size += 1

    def pop(self):
        """ Removes the element on top of the stack and returns that element. """
        if self._size > 0:
            self._size -= 1
            return self._array[self._size]
        else:
            return "Array is empty."

    def top(self):
        """ Returns the element on top without removing it from the stack """
        if self._size > 0:
            return self._array[self._size - 1]
        else:
            return self._array[:self._size]

    def is_empty(self):
        """ Returns whether the stack is empty. """
        if self._size == 0:
            return True
        else:
            return False


# Checks whether the input string is balanced
# param: input string
# returns True if string is balanced, otherwise returns False
def is_balanced(input_string):

    # initialize an empty list as the stack
    stack = MyStack()

    # iterate over each character in the string
    for i in input_string:
        if i == "(":
            stack.push(i)
        elif i == "[":
            stack.push(i)
        elif i == "{":
            stack.push(i)
        elif i == ")":
            if not stack.is_empty() and stack.top() == "(":
                stack.pop()
            else:
                return False
        elif i == "]":
            if not stack.is_empty() and stack.top() == "[":
                stack.pop()
            else:
                return False
        elif i == "}":
            if not stack.is_empty() and stack.top() == "{":
                stack.pop()
            else:
                return False
        else:
            pass

    return stack.is_empty()

if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY

    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))
