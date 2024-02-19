def print_slices(nums):
  n = len(nums)

  subarr1 = nums[0:2] 
  print(subarr1)
  # 2,1,4 ❌
  # 2,1 ✅

  subarr2 = nums[1:n-1]
  print(subarr2)
  # 1,4,6,3 ❌
  # 1,4,6 ✅

def print_forwards(nums):
  n = len(nums)
  print(range(n))
  for i in range(n):
    print(i)


def print_forwards2(nums):
  n = len(nums)
  for i in range(n - 1, -1, -1):
    print(i)

def print_backward(nums):
  n = len(nums)
  for (index, value) in enumerate(reversed(nums)):
    print("index: ", index)
    print("value: ", value)

# most C-like syntax
# range(start, stop, step)
def print_backward2(nums):
  n = len(nums)
  for index in range((n - 1), -1, -1):
    print("index: ", index)
    print("value: ", nums[index])


def sort_arr(arr, shouldReverse = False):
  s = sorted(arr, reverse = shouldReverse)
  print(s)
  return s

def delete_item(nums, index):
  del nums[index]
  print(nums)
  print(len(nums))

def main():
  delete_item([3,5,2,6,4,3], 3)
main()
