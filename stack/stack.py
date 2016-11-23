class Node:
    next=None
    data=None
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

class LStack:
    head=None
    def __init__(self, head):
        self.head=head
    def isEmpty(self):
        if(self.head==None):
            return True
        else:
            return False

    def print(self):
        if(self.head==None):
            print("Stack is empty")
            return
        current=self.head
        print("Stack = [")
        while(current.next!=None):
            print("%s "%(current.data), end="")
            current=current.next
        print("%s]"%(current.data))

    def delete(self, node):
        if(self.head==None):
            print("List is empty")
            return

        current=self.head
        if(current.data==node.data):
            self.head = current.next
            current.next = None
            print("%s deleted"%(current.data))
            return
        while(current.next!=None):
            if(current.next.data==(node.data)):
                temp=current.next
                current.next = (current.next).next
                temp.next = None
                print("%s deleted"%(temp.data))
                return
            current = current.next
        if(current.next==None):
            self.head=None
            print("%s deleted"%(current.data))
            return

    def push(self, node):
        current=self.head
        if(current==None):
            self.head = node
            print("%s pushed"%(node.data))
            return
        elif(current.next==None):
            node.next=None
            current.next=node
            print("%s pushed"%(node.data))
            return
        else:
            node.next=current
            self.head = node
            print("%s pushed"%(node.data))
            return

    def pop(self):
        if(self.isEmpty()==True):
            print("stack is empty")
            return
        current = self.head
        current.next = self.head
        print("%s popped"%(current.data))
        return current.data

    def peek(self):
        print("%s peeked"%(self.head.data))
        return self.head.data



