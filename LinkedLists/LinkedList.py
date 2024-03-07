class node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
        self.Length = 0
    
    def print(self):
        ptr = self.head
        while ptr!=None:
            print(ptr.value,"-->",end="")
            ptr = ptr.next
        print("\n")

    def insert_at_begining(self,value):
        new_node = node(value,self.head)
        self.head = new_node
        self.Length +=1
    
    def insert_at_end(self,value):
        new_node = node(value,None)
        if self.head!=None:
            ptr = self.head
            while ptr.next !=None:
                ptr = ptr.next
            ptr.next = new_node
            self.Length +=1
        else:
            self.insert_at_begining(value)
    
    def remove_at_begining(self):
        if self.Length==0:
            print("List is empty")
        else:
            ptr = self.head
            self.head = self.head.next
            ptr.next = None
            self.Length -=1


    def remove_at_end(self):
        if self.Length>1:
            ptr = self.head
            while ptr.next.next!=None:
                ptr = ptr.next
            ptr.next = None
            self.Length -=1
        elif self.Length==1:
            self.head = None
            self.Length = 0
        else:
            print("The Linked List is empty!")
            

    def remove_at_index(self,index):
        if index<0 or index>=self.Length:
            print("Invalid index")
        elif index==0:
            self.remove_at_begining()
        else:
            ptr = self.head
            count =index-1
            while ptr!=None:
                if count==0:
                    temp = ptr.next
                    ptr.next = ptr.next.next
                    temp.next = None
                    self.Length -=1
                    break
                ptr = ptr.next
                count -=1

    def insert_at_index(self,index,value):
        if index<0 or index>=self.Length:
            print("Invalid Index")
        elif index==0:
            self.insert_at_begining(value)
        elif index==self.Length-1:
            self.insert_at_end(value)
        else:
            ptr = self.head
            count = index
            while ptr!=None:
                if count-1==0:
                    new_node = node(value,ptr.next)
                    ptr.next = new_node
                    self.Length +=1
                count -=1
                ptr =ptr.next
            
    
    def remove_by_value(self,value):
        ptr = self.head
        if self.Length==0:
            print("List is empty")
            return
        
        temp = self.head
        while ptr!=None:
            if ptr.value ==value:
                if ptr == self.head:
                    self.remove_at_begining()
                    break
                temp.next = ptr.next
                ptr.next = None
                self.Length -=1
                break
            temp = ptr
            ptr = ptr.next
        
    def extend(self,List2):
        ptr = self.head
        if self.head==None:
            self.head = List2.head
            self.Length = List2.Length
            return
        
        while ptr.next!=None:
            ptr = ptr.next
        ptr.next = List2.head
        self.Length +=List2.Length

    def revese(self):
        prev = None
        current = self.head
        next = None
        while current!=None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev



    def middle(self):
        pass

