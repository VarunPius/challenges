'''
Question: Find if value exists in BST

Time complexity: O(log n) - depth of the node
'''

import sys
sys.path.append("./mylib")
import BST

#Create BST
root = BST.BSTNode(4)
input = [3,2,1,5,10,7,6,9,15]
for x in input:
    BST.insertNode(root, BST.BSTNode(x))



#Solution 1: Recursive
def BSTSearch(root,K):
    if(root is None):
        return False
    elif (root.data > K): 
        return(BSTSearch(root.left,K))
    elif (root.data < K):
        return(BSTSearch(root.right,K))
    else:
        return True
    
#Solution 2: Iterative
def  BSTSearch2(node,target):
    while node:
        if node.data == target:
            return True
        elif node.data > target:
            node = node.left
        else:
            node = node.right
    return False

input2 = [15,3,0]    
for K in input2:
    print("%d exist: %s" % (K,BSTSearch(root,K)))
