'''
To remove the node, it checks for a previous node, if there is one then
it makes a link of the previous node as the next node else the start of the node
is the next node
then it checks if the next node is not empty which then it will make as its
previous node else the last node is made as the previous node

This essentially deletes the node as it has no connection in the tree to other
nodes making it not a part of the tree hence deleted.

Value of the nodes have been stored in individual variables, this is so that
when a node is deleted it wont remove the links to the rest of the tree
instead the value of the node will just be removed while maintaining the links
within the tree sort.

'''

import sys

class Node(object):
      
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None

class List(object):
      
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insert(self,n,x):
          
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x
            
    def display(self):
          
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print ("List: ",",".join(values))

        
    def ListRemove(self,n):
          
          if n.prev != None:
                n.prev.next = n.next
          else:
                self.head = n.next
          if n.next != None:
                n.next.prev = n.prev
          else:
                self.tail = n.prev
              
if __name__ == '__main__':
    l=List()
    Node1 = Node(4)
    Node2 = Node(6)
    Node3 = Node(8)
    l.insert(None,Node1)
    l.insert(l.head,Node2)
    l.insert(l.head,Node3)
    l.display()
    l.ListRemove(Node2)
    print("After Node Removed")
    l.display()
    
sys.exit()
