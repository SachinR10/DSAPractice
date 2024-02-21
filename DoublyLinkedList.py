class node:
    def __init__(self,value,prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.Length = 0
    
    def print(self):
        ptr = self.head
        while ptr:
            print(ptr.value, "-->",end="")
            ptr = ptr.next
        print()
    def insert_at_begining(self,value):
        if self.Length==0:
            self.head = node(value)
            self.Length +=1
            return
        else:
            new_node = node(value,prev=None,next=self.head)
            self.head = new_node
            self.Length +=1
            return
    
    def insert_at_end(self,value):
        if self.Length ==0:
            self.insert_at_begining(value)
            return
        else:
            ptr = self.head
            while ptr.next!=None:
                ptr = ptr.next
            new_node = node(value,prev=ptr,next=None)
            ptr.next = new_node
            self.Length +=1
            return

    def remove_at_begining(self):
        if self.Length==0:
            print("list is empty! can not remove anything!!")
            return
        elif self.Length==1:
            self.head=None
            self.Length = 0
        else:
            ptr = self.head
            self.head = self.head.next
            self.head.prev = None
            ptr.next = None
            self.Length -=1
            return

    def remove_at_end(self):
        if self.Length==0:
            print("list is already Empty!! Can not remove anything at end:(")
            return
        elif self.Length==1:
            self.head = None
            self.Length = 0
            return
        else:
            ptr = self.head
            while ptr.next!=None:
                ptr = ptr.next
            ptr.prev.next = None
            ptr.prev = None
            self.Length -=1
            return


    def insert_at(self,index,value):
        if index<0 or index>=self.Length:
            print("Invalid index!!")
            return
        if index==0:
            self.head = node(value,prev=None,next=self.head)
            self.Length +=1
            return
        else:
            count = index-1
            ptr = self.head
            while count!=0:
                ptr = ptr.next
                count -=1
            new_node = node(value,next=ptr.next,prev=ptr)
            ptr.next = new_node
            self.Length +=1
            return



    def remove_at(self,index):
        if index<0 or index>=self.Length:
            print("Invalid index")
            return
        if self.Length==1:
            self.head = None
            self.Length = 0
            return
        else:
            count = index-1
            ptr = self.head
            while count!=0:
                ptr = ptr.next
                count -=1
            temp = ptr.next
            ptr.next = ptr.next.next
            temp.next.prev = ptr
            temp.next = None
            temp.prev = None
            self.Length -=1
            return
        
        

    def extend(self,list2):
        pass