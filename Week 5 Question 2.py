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
    l.display()
    
