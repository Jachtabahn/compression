from bhrigu import HuffmanCoding

#input file path
path = "beispiele/plan.txt"

h = HuffmanCoding(path)

output_path = h.compress()
h.decompress(output_path)
