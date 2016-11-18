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
        if(current.next==current):
            print("%d"%(current.data))
            return
        while(current.next!=self.starting):
            print("%d"%(current.data))
            current=current.next
        print("%d"%(current.data))

    def delete(self, node):
        if(self.starting==None):
            print("List is empty")
            return
        current=self.starting
        if(current.next==current):
            current.next=None
            current.prev=None
            self.starting=None
            print("%s deleted"%(current.data))
            return

        while(self.starting.next!=self.starting):
            if(current.data==node.data):
                if(current==self.starting):
                    temp=current
                    if(current.prev.data>current.next.data):
                        self.starting = current.next
                    else:
                        self.starting = current.prev
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    print("%s deleted"%(temp.data))
                    current.next = None
                    current.prev = None
                    return
                temp=current
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                print("%s deleted"%(temp.data))
                current.next = None
                current.prev = None
                return
            current = current.next


    def insert(self, node):
        current=self.starting
        if(self.starting==None):
            self.starting = node
            node.next = node
            node.prev = node
            print("%s inserted"%(node.data))
            return
        if(self.starting.next == self.starting):
            node.next = current
            node.prev = current
            current.next = node
            current.prev = node
            print("%s inserted"%(node.data))
            if(node.data<self.starting.data):
                self.starting=node
            return
        while(1):
            if(current.data==node.data):
                node.next = current.next
                node.prev = current
                current.next = node
                node.next.prev = node
                print("%s inserted"%(node.data))
                return
            elif(current.data<node.data):
                if((current.next.data>node.data)or(current.next==self.starting)):
                    node.next=current.next
                    node.prev=current
                    current.next=node
                    node.next.prev = node
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
liststarting.delete(n1)
liststarting.print()
liststarting.delete(n4)
#liststarting.insert(n3)
liststarting.print()
liststarting.delete(n5)
liststarting.print()
liststarting.delete(n2)
liststarting.print()
print("test1")
liststarting.delete(n2)
print("test2")
liststarting.print()


print('test')
liststarting.insert(n2)
print(liststarting.starting.next.data)
print(liststarting.starting.prev.data)
liststarting.print()
print("test2")
liststarting.insert(n1)
print("test3")
print(liststarting.starting.next.data)
print(liststarting.starting.prev.data)
print("test4")
liststarting.print()
print('test5')


liststarting.insert(n4)
liststarting.print()
liststarting.insert(n3)
liststarting.print()


#liststarting.insert(n5)
#liststarting.print()

