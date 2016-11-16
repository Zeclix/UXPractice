class Node:
    prev=None
    next=None
    data=None
    def __init__(self, data, next=None, prev=None):
        self.data=data
        self.prev=prev
        self.next=next

class LList:
    starting=None
    def __init__(self, starting):
        self.starting=starting
    def print(self):
        if(self.starting==None):
            print("List is empty")
            return
        current=self.starting
        while(current.next!=self.starting):
            print("%d"%(current.data))
            current=current.next
        print("%d"%(current.data))

    def delete(self, node):
        if(self.starting==None):
            print("List is empty")
            return

        current=self.starting
        while(current.next!=self.starting):
            if(current.data==node.data):
                temp=current
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                print("%s deleted"%(temp.data))
                current.next = None
                current.prev = None
                return
            current = current.next
        if(current.next==self.starting):
            self.starting=None
            print("%s deleted"%(current.data))
            return

    def insert(self, node):
        current=self.starting
        if(current==None):
            self.starting = node
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

n1.next = n2
n2.prev = n1
n2.next = n4
n4.prev = n2
n4.next = n5
n5.prev = n4
n5.next = n1
n1.prev = n5

liststarting=LList(n1)
liststarting.print()
liststarting.delete(n4)
#liststarting.insert(n3)
liststarting.print()
liststarting.delete(n5)
liststarting.print()
#liststarting.insert(n5)
#liststarting.print()

