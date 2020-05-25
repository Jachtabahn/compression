#!/usr/bin/env python3

import sys

units = []
for line in sys.stdin.buffer:
  for c in line:
    units.append(bytes([c]))

units.sort()
unique_units = list(set(units))
counts = {unique: units.count(unique) for unique in unique_units}
unique_units.sort(reverse=True, key = lambda unit: counts[unit])

print(unique_units)
print(len(unique_units))

class Tree:

  def __init__(self, path, index, unit):
    self.path = path
    self.index = index
    self.unit = unit
    self.left = None
    self.right = None

  def __str__(self):
    r = ""
    r += "Path: {}\n".format(self.path)
    r += "Index: {}\n".format(self.index)
    r += "Unit: {}\n".format(self.unit)
    if self.left is not None:
      left_str = str(self.left)
    else:
      left_str = ""
    if self.right is not None:
      right_str = str(self.right)
    else:
      right_str = ""
    return r + left_str + right_str

def huffman(units, path=b''):
  if len(units) == 1:
    unit = units[0]
    return Tree(path, 0, unit)

  middle = len(units) // 2
  tree = Tree(path, middle, None)
  tree.left = huffman(units[:middle], path + b'\x00')
  tree.right = huffman(units[middle:], path + b'\x01')
  return tree

tree = huffman(unique_units)
print(tree, end='')
