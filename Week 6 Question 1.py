'''
while the size of the variable Store is greater than 0 then it checks
to see if the current node is not empty.
While the theres a node on the left hand side then it will add that node to the
list stored in the variable called Store and make the current node that node.
If there is no node on the left hand side then it will check the Stack if its
not empty, if it isnt then it will print values in the stack and add the node
on the right hand side.
'''

import sys

class BinTreeNode(object):
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

        
def tree_insert(tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree


def postorder(tree):  
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
  

def in_order(tree):
    
    Store = [tree]
    currentNode = tree

    while len(Store) > 0:
        if currentNode != None:
            while currentNode.left != None:
                Store.append(currentNode.left)
                currentNode = currentNode.left

            Stack = Store.pop()
            if Stack != None:
                print(Stack.value)
                Store.append(Stack.right)


if __name__ == '__main__':
    
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)

sys.exit()
