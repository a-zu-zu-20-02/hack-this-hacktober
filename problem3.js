/*
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
*/
// * a class for node of tree is created
class Node {
    constructor(val, left = '', right = '') {
        this.val = val;
        this.left = left;
        this.right = right; 
    }
}
// * serialize will take root node of the tree as input and then converts it to a json string
const serialize = (root) => {
    return JSON.stringify(root);
};
// * deserialize takes the json string as object and then once again converts it back to an object
const deserialize = (str) => {
    return JSON.parse(str);
};

let node = new Node('root', new Node('left', new Node('left.left')), new Node('right'));
console.log(node);

console.log(deserialize(serialize(node)).left.left.val === 'left.left');
