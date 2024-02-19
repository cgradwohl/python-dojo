# The concatination operation are O(N) EACH TIME, so since the concat operation happens in a loop based on the input,
# The result is O(N^2)
# The reason is that strings are immutable in Python, so each time you concat, you are creating a new String object,
# which requires writing each character to a new memory allocation.
def reverse_strin_ALSODUMB(s):
  stack = list(s)
  result = ""

  while len(stack) != 0:
    result += stack.pop()
  return result


def reverseStringDUMB(s):
    stack = list(s)
    result = ""

    for i in range(len(s)):
        item = stack.pop()
        result += item
    return result


# O(N)
def reverse_string(s):
  # O(N)
  stack = list(s)
  result = list()

  # O(N)
  while len(stack) != 0:
    result.append(stack.pop())
  
  # O(N)
  return ''.join(result)
