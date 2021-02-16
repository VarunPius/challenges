'''
Question: Find the max value of the binary tree

Algorithm:
1. Recursively traverse the tree
2. Recursive function take node and max value computed so far and returns new max value
'''

import sys
sys.path.append("./mylib")
import Tree


#Recursive traversal
def MaxValue(root,maxvalue):
	if (root.data >  maxvalue):
		maxvalue = root.data
	maxLeft = maxvalue
	maxRight = maxvalue	
	if (root.getLeft() is not None):
		maxLeft  = MaxValue(root.getLeft(),maxvalue)
	if (root.getRight() is not None):
		maxRight = MaxValue(root.getRight(),maxvalue)
	return max(maxLeft,maxRight)

#Find the node with max value
def MaxValue2(node,maxS):
	if (node is None):
		return maxS
	if (node.data > maxS):
		maxS = node.data
	maxl =  MaxValue(node.getLeft(),maxS)
	maxr = MaxValue(node.getRight(),maxS)
	return (max(maxS,maxl,maxr))	

#Initialize Binary Tree
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(40)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(70)

print("Maximum value =",MaxValue2(root,root.data))
