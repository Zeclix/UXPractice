class Node:
    next=None
    data=None
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

class LList:
    head=None
    def __init__(self, head):
        self.head=head
    def print(self):
        if(self.head==None):
            print("List is empty")
            return
        current=self.head
        while(current.next!=None):
            print("%d"%(current.data))
            current=current.next
        print("%d"%(current.data))

    def delete(self, node):
        if(self.head==None):
            print("List is empty")
            return

        current=self.head
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

    def insert(self, node):
        current=self.head
        if(current==None):
            self.head = node
            print("%s inserted"%(node.data))
            return
        while(1):
            if(current.next==None):
                node.next=None
                current.next=node
                print("%s inserted"%(node.data))
                return
            if(current.data==node.data):
                node.next = current.next
                current.next = node
                print("%s inserted"%(node.data))
                return
            elif(current.data<node.data):
                if(current.next.data>node.data):
                    node.next=current.next
                    current.next=node
                    print("%s inserted"%(node.data))
                    return
            current = current.next



n1 = Node(100)
n2 = Node(200)
n3 = Node(300)
n4 = Node(400)
n5 = Node(500)
'''
n1.next=n2
n2.next=n4
n4.next=n5

listHead=LList(n1)
listHead.print()
listHead.delete(n4)
listHead.insert(n3)
listHead.print()
listHead.delete(n5)
listHead.print()
listHead.insert(n5)
listHead.print()
'''
listHead = LList(n1)
listHead.print()
listHead.delete(n1)
listHead.print()
listHead.insert(n1)
listHead.print()