

# How to split the data into units

What is a unit? Is a unit one UTF 8 character? Or is a "word"? The whole data stream consists of units.

* One UTF-8 character by another.
* Several UTF-8 characters by several.
* Look up, what is a word in the regular expression?
* Whole bunch of whitespace characters is one word.
* Divide a complex word separated by - into several words, e.g. `universal-stake-holder` into three words.

# Evaluate all the units

* Make a frequency count of all the units.
* Sort the units by their frequency counts.

# Construct balanced tree from the evaluation

* Recursive call to create a subtree
* Non-recursive call to create a leaf encoding a unit
* Visualize the output tree.
