class Node:
    def __init__ (self,value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__  (self):
      self.head = None
      self.count=0

    def isempty(self):
      return self.head==None 
      
    
    
    def InsertatHead(self,value):
      newNode=Node(value)
      newNode.next=self.head
      self.head=newNode
      self.count=self.count + 1

    def traverse(self):
      curr=self.head
      while(curr!=None):
       print(curr.data)
       curr=curr.next

    def InsertatTail(self,value):
       newNode=Node(value)
       if self.isempty():
          self.InsertatHead(value)
       curr=self.head
       while curr.next!=None:
         curr=curr.next
         curr.next=newNode

    def display(self):
        curr=self.head
        while curr!=None:
            print(curr.data ,end="")
            curr=curr.next
        print()
    
    def InsertatGivenData(self,after,value):
      newNode=Node(value)
      curr = self.head

      while curr != None:
       if curr.data == after:
        break
      curr = curr.next

      if curr != None:
       new_node.next = curr.next
       curr.next = new_node
       self.n = self.n + 1
      else:
       return 'Item not found'
      
    def deleteHead(self):

      if self.isempty():
        return 'Empty LL'
      else:
        self.head=self.head.next
        curr = curr +1

    def deleteTail(self):
      if self.isempty():
        return 'Empty LL'
      curr=self.head
      if curr.next==None:
        return self.deleteHead()
      while curr.next.next!=None:
        curr=curr.next
      curr.next=None
    

    def remove(self,value):

      if self.head == None:
        return 'Empty LL'

      if self.head.data == value:
         return self.deleteHead()

      curr = self.head

      while curr.next != None:
       if curr.next.data == value:
        break
      curr = curr.next

      if curr.next == None:

        return 'Not Found'
      else:
       curr.next = curr.next.next
       self.count = self.count- 1

    def search(self,item):

       curr = self.head
       pos = 0

       while curr != None:
        if curr.data == item:
         return pos
       curr = curr.next
       pos = pos + 1

       return 'Not Found'

s=LinkedList()
linked_list = LinkedList()
linked_list.InsertatHead(10)
linked_list.InsertatTail(20)
linked_list.InsertatTail(30)

print("Traverse after Insertions:")
linked_list.traverse() 

linked_list.InsertatGivenData(20, 25)
print("Traverse after InsertatGivenData:")
linked_list.traverse()  

linked_list.deleteHead()
print("Traverse after deleteHead:")
linked_list.traverse()  

linked_list.deleteTail()
print("Traverse after deleteTail:")
linked_list.traverse() 

print("Search for 25:")
print(linked_list.search(25))  

print("Search for 100:")
print(linked_list.search(100))

linked_list.remove(25)
print("Traverse after removing 25:")
linked_list.traverse() 
        
   

  