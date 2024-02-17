class Node:

    def __init__(self,value):
        self.value = value
        self.next = None


#append,Insert,Pop,delete,print,getIndex 
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.Length = 0

    def append(self,value):
        node = Node(value)
        if self.Length == 0:
            self.head = node
            self.tail = node
            self.Length +=1
        else:
            self.tail.next = node
            self.tail = node
            self.Length +=1
        return 1
    def printLL(self):
        if self.Length > 0:
            pointer = self.head
            while pointer.next != None:
                print(pointer.value)
                pointer = pointer.next
            print(pointer.value)
        else:
            print("Empty list")

    def GetLength(self):
        return self.Length
    
    def pop(self):
        if self.Length>1:
            pointer = self.head
            while pointer.next != self.tail:
                pointer = pointer.next
            self.tail = pointer
            pointer.next = None
            self.Length -=1
            return 1
        elif self.Length==1:
            self.head = None
            self.tail = None
            self.Length = 0
        else:
            print("List is empty can not pop")
        

    def insert(self,position,value):
        pass

    def delete(self,value):
        if self.Length>1:
            pointer = self.head
            while pointer.next.value != value:
                pointer = pointer.next
            temp = pointer.next
            pointer.next = pointer.next.next
            temp.next = None
            self.Length -=1            
        else:
            print("LL is empty")
    



    
