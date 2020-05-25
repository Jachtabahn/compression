from bhrigu import HuffmanCoding

#input file path
path = "/home/habimm/projekte/_kompression/beispiele/plan.txt"

h = HuffmanCoding(path)

output_path = h.compress()
h.decompress(output_path)
