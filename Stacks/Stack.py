class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    #use top instead of head
    def __init__(self,capacity):
        self.capacity = capacity
        self.head = None
        self.length = 0

    def push(self,value):
        if self.length==0:
            self.head = Node(value)
            self.length=1
            return
        else:
            if self.length<self.capacity:
                new_node = Node(value,self.head)
                self.head = new_node
                self.length +=1
                return 
            else:
                print("stack is full! can not push anymore")
                return

    def pop(self):
        if self.head == None:
            print("empty stack can not pop anything!!")
            return
        else:
            ptr = self.head
            self.head = self.head.next
            ptr.next = None
            self.length -=1
            return ptr.value
        
    def peek(self):
        if self.length==0:
            return "empty stack! peek is not possible"
        else:
            return self.head.value
        
    def printStack(self):
        ptr = self.head
        print('-'*20)
        while ptr!=None:
            print(ptr.value)
            ptr = ptr.next
        print('-'*20)
    
    def get_capacity(self):
        return self.capacity
    
    def get_length(self):
        return self.length