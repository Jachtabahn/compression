#!/usr/bin/env python3

import sys

input = []
for line in sys.stdin.buffer:
  for c in line:
    input.append(bytes([c]))

unique_units = list(set(input))
counts = {unique: input.count(unique) for unique in unique_units}
unique_units.sort()
unique_units.sort(reverse=True, key = lambda unit: counts[unit])

class Tree:

  def __init__(self, path, unit):
    self.path = path
    self.unit = unit
    self.left = None
    self.right = None

  def __str__(self):
    r = ""
    r += "Path: {}\n".format(self.path)
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

encoding = {}
def huffman(units, path=b''):
  if len(units) == 1:
    unit = units[0]
    encoding[unit] = path
    return Tree(path, unit)

  middle = len(units) // 2
  tree = Tree(path, None)
  tree.left = huffman(units[:middle], path + b'\x00')
  tree.right = huffman(units[middle:], path + b'\x01')
  return tree

tree = huffman(unique_units)
# print(tree, end='')
# print(encoding)


# Have the Huffman tree. Now encode a file read into input.

encoded = b''
for c in input:
  encoded += encoding[c]

codes = []
for i in range(0, len(encoded), 8):
  bits_list = encoded[i:i+8]
  byte = 0
  for j, b in enumerate(bits_list):
    if b == 1:
      byte += 2 ** j
  codes.append(byte)

# Some padding should be done here

sys.stdout.buffer.write(bytes(codes))
