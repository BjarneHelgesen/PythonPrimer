'''
Print a Christmas tree using hash symbols, e.g. like this for a 5 hash height plus stem: 
    #
   ###
  #####
 #######
#########
    #

Let the user input the height. 

Example: The printing for a 5-height would be: 
4 spaces + 1 hash
3 spaces + 3 hashes
2 spaces + 5 hashes
1 space  + 7 hashes
0 spaces + 9 hashes
4 spaces + 1 hash for the stem


Optional: unit tests
'''

def unit_test():
    assert create_christmas_tree(0) ==  "#"
    assert create_christmas_tree(1) ==  "#\n#"
    assert create_christmas_tree(2) ==  " #\n###\n #"
    assert create_christmas_tree(3) ==  "  #\n ###\n#####\n  #"
    print("Unit test passed")

def create_christmas_tree(height):
    christmas_tree = ""
    tree_line = "#"
    for i in range(height):
        christmas_tree += " "*(height-i-1) + tree_line + "\n"
        tree_line += "##"
    if height > 0:
        christmas_tree += " "*(height-1)
    christmas_tree += "#"
    return christmas_tree


unit_test()

print (create_christmas_tree(12))









































