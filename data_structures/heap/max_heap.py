from math import floor

class MaxHeap:
  def __init__(self):
    self.heap = [None]
    self.heap_size = 0

  def parent(i: int):
    return floor(i / 2)

  def left(i: int):
    return (2 * i)

  def right(i: int):
    return (2 * i) + 1

  def heapify(self, i: int):
    if self.heap_size == 0:
      return None

    left = self.left(i)
    right = self.right(i)
    largest = i
    
    # check overflow condition of left and right
    if left < self.heap_size and self.heap[left] > self.heap[i]:
      largest = left
    elif right < self.heap_size and self.heap[right] > self.heap[i]:
      largest = right
    
    if largest == i:
      return None
    
    temp = self.heap[i]
    self.heap[i] = self.heap[largest]
    self.heap[largest] = temp
    return self.heapify(largest)

  def peek_max(self):
    if self.heap_size == 0:
      return None

    return self.heap[1]

  def remove_max(self):
    if self.heap_size == 0:
      raise Exception("The heap is empty.")

    max = self.heap[1]
    self.heap[1] = self.heap[self.heap_size]
    self.heap_size -= 1
    self.heapify(1)
    
    return max

  def insert(self, key: int):
    # append the key as a leaf of the heap
    self.heap.append(key)

    # increase heap_size
    self.heap_size += 1

    i = self.heap_size
    while self.parent(i) > 0 and self.heap[i] > self.heap[self.parent(i)]:
      parent = self.parent(i)
      temp = self.heap[parent]
      self.heap[parent] = self.heap[i]
      self.heap[i] = temp
      i = parent


