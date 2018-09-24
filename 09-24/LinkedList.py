
class Node:
  def __init__(self, x):
    self.val = x
    self.next = None

class LinkedList:
  def __init__(self, head = None, L = []):
    self.head = None
    self.__length = 0
    if L:
      self.construct(L)
  
  def show(self):
    if not self.head:
      print(self.head)
    else:
      cur = self.head
      while cur:
        print(cur.val, '-> ', end = '')
        cur = cur.next
      print('None')
  
  def construct(self, L):
    self.empty()
    for n in L:
      self.push(n)

  def push(self, val):
    self.__length += 1
    node = Node(val)
    if not self.head:
      self.head = node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = node

  def pop_front(self):
    if self.__length > 0:
        temp = self.head
        self.head = None if self.length == 1 else self.head.next
        self.__length -= 1
        del temp

  def pop(self):
    return self.delete(self.size() - 1)
  
  def reverse(self):
    if self.head and self.head.next:
      oldPrevious = None
      previous = self.head
      current = self.head.next
      previous.next = None

      while current.next:
        oldPrevious = previous
        previous = current
        current = current.next
        previous.next = oldPrevious
      
      current.next = previous
      self.head = current
  
  def delete(self, i):
    if self.head:
      self.__length -= 1
      if i == 0:
        temp = self.head
        num = temp.val
        self.head = self.head.next
        del temp
        return num

      node = self.__get_node(i - 1)
      if node:
        temp = node.next
        num = temp.val
        node.next = temp.next
        del temp
        return num

  def delete_kth_from_back(self, k):
    if k > 0 or k <= self.size():
      i = 0
      left = self.head
      right = self.__get_node(k)
      while right:
        left = left.next
        right = right.next
        i += 1
      self.delete(i)

  def to_list(self):
    L = []
    cur = self.head
    while cur:
      L.append(cur.val)
      cur = cur.next
    return L

  def max(self):
    
    if self.__length == 0:
      return None

    cur = self.head
    max_val = 0
    while cur:
      if cur.val > max_val:
        max_val = cur.val
      cur = cur.next
    return max_val

  def min(self):
    if self.__length == 0:
      return None

    cur = self.head
    min_val = 0
    while cur:
      if cur.val < min_val:
        min_val = cur.val
      cur = cur.next
    return min_val

  def sort(self, rev = False):
    L = self.to_list()
    L.sort(reversed = rev)
    self.construct(L)

  def empty(self):
    cur = self.head
    while cur:
      temp = cur
      cur = cur.next
      del temp
    self.__length = 0
    self.head = None

  def at(self, i):
    node = self.__get_node(i)
    return node.val if node else None

  def is_empty(self):
    return self.__length == 0

  def __get_node(self, i):
    if i < self.__length and i >= 0:
      cur = self.head
      j = 0
      while j < i:
        cur = cur.next
        j += 1
      return cur
    return None

  def size(self):
    return self.__length






