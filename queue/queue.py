import os

class Node:
    next=None
    data=None
    def __init__(self, data, next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class LQueue:
    front=None
    rear = None
    def __init__(self, front=None, rear = None):
        self.front=front
        self.rear = rear
    def isEmpty(self):
        if((self.front==None) and (self.rear == None)):
            return True
        else:
            return False

    def print(self):
        if(self.front==None):
            print("Queue is empty")
            return
        current=self.front
        print("Queue = [", end="")
        while(current.next!=None):
            print("%s "%(current.data), end="")
            current=current.next
        print("%s]"%(current.data))

    def delete(self, node):
        if(self.front==None):
            print("List is empty")
            return

        current=self.front
        if(current.data==node.data):
            self.front = current.next
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
            self.front=None
            print("%s deleted"%(current.data))
            return

    def enqueueF(self, node):
        current=self.front
        if(current==None):
            self.front = node
            self.rear = node
            print("%s enequed(front)"%(node.data))
            return
        elif(current.next==None):
            node.prev = None
            node.next=current
            current.prev = node
            current.next=None
            self.front = node
            self.rear = current
            print("%s enqueued(front)"%(node.data))
            return
        else:
            node.next=current
            current.prev = node
            self.front = node
            print("%s enqueued(front)"%(node.data))
            return

    def enqueueR(self, node):
        current=self.front
        if(current==None):
            self.front = node
            self.rear = node
            print("%s enequed(rear)"%(node.data))
            return
        elif(current.next==None):
            node.next=None
            current.next=node
            node.prev = current
            self.rear = node
            print("%s enqueued(rear)"%(node.data))
            return
        else:
            while(1):
                if(current.next==None):
                    node.next=None
                    current.next=node
                    node.prev = current
                    self.rear = node
                    print("%s enqueued(rear)"%(node.data))
                    return
                current = current.next

    def dequeueF(self):
        current = self.front
        current.next.prev = None
        self.front = current.next
        current.next = None
        print("%s dequeued(front)"%(current.data))
        return current.data

    def dequeueR(self):
        current = self.rear
        self.rear = current.prev
        self.rear.next=None
        current.prev = None
        print("%s dequeued(rear)"%(current.data))
        return current.data

    def peek(self):
        print("%s peeked"%(self.front.data))
        return self.front.data

# inputStr = input("Enter the formula : ")

queue = LQueue()


# for i in range(len(inputStr)):
#     stackTop.enqueueF(Node(inputStr[i]))
#
# stackTop.print()

while(1):
    a = input("값을 입력하세요(enF, enR, deF, deR, p, q)")

    if(a=="enF"):
        b = input("값 입력")
        temp = Node(b)
        queue.enqueueF(temp)
    elif(a=="enR"):
        b = input("값 입력")
        temp = Node(b)
        queue.enqueueR(temp)
    elif(a=="deF"):
        queue.dequeueF()
    elif(a=="deR"):
        queue.dequeueR()
    elif(a=="p"):
        queue.print()
    elif(a=="q"):
        os._exit(1)