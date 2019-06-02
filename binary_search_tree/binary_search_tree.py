class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree
  def insert(self, value):
    if self.value:
      if value < self.value:
        if self.left is None:
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)
      elif value > self.value:
        if self.right is None:
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)
    else:
        self.value = value

  # searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not
  def contains(self, target):
    if self.value == target:
      return True
    elif self.left is None and self. right is None:
      return False
    elif target < self.value:
      return self.left.contains(target)
    else:
      return self.right.contains(target)


  # returns the maximum value in the binary search tree
  def get_max(self):
    if self.value: 
      max_value = self.value
      if self.right:
        max_value = self.right.value
        return self.right.get_max()
      else:
        return max_value
    else:
      return None

  # performs a traversal of every node in the tree, executing the passed-in callback function on each tree node value. There are myriad to perform tree traversal; in this case any of them should work.
  def for_each(self, cb):
    if self.value:
      cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)