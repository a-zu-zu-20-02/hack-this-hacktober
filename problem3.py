"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
import json
class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    
def objToDict(input_node):
    input_dict = input_node.__dict__
    for key,value in input_dict.items():
        # if the value of object property is object convert it o a dictionary recursively
        if type(value) == type(input_node):
            input_dict[key] = objToDict(value)
    return input_dict

def dictToObj(input_dict):
    # to convert the given dictionary to tree
    output_node = Node(input_dict["val"])
    output_node.left = input_dict["left"]
    output_node.right = input_dict["right"]
    # if the left or right has dictionary as value convert that dictionary to object using recursion
    if type(input_dict["left"]) == dict:
        output_node.left = dictToObj(input_dict["left"])
    if type(input_dict["right"]) == dict:
        output_node.right = dictToObj(input_dict["right"])
    return output_node

def serialize(input_node):
    # convert given function into dictionary
    input_dict = objToDict(input_node)
    # convert the dictionary to json str
    return json.dumps(input_dict)

def deserialize(input_string):
    # convert the given string into dictionary
    output_dict = json.loads(input_string)
    # convert the dictionary to class object
    return dictToObj(output_dict)
    
def main():
    node = Node(
        'root',
        Node('left',Node('left.left')),
        Node('right')
    )
    ip = serialize(node)
    print(ip,type(ip))
    op = deserialize(ip)
    print(op,type(op))
    print(deserialize(serialize(node)).left.left.val == 'left.left')
    assert deserialize(serialize(node)).left.left.val == 'left.left'

if __name__ == "__main__":
    main()
