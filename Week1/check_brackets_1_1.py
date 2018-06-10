# python3

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


if __name__ == "__main__":
    text = sys.stdin.read()
    opening_brackets_stack = []   # Use this list as a stack instead of as an array
    error_position = 0
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening brackets
            ob = Bracket(next, i+1)   # i+1 because op index starts at 1
            opening_brackets_stack.append(ob)

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket
            if not opening_brackets_stack:   # is the stack empty
                error_position = i + 1
                break
            matching_ob = opening_brackets_stack.pop()
            if not matching_ob.Match(next):
                error_position = i + 1
                break

    # Printing answer
    if error_position == 0 and not opening_brackets_stack:
        print ("Success")
    else:
        if error_position == 0:
            while len(opening_brackets_stack) > 1:
                opening_brackets_stack.pop()
            error_position = opening_brackets_stack[-1].position
        print (error_position)
