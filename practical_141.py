# Linked list

class Linkedlist:
    head = [3,2,0,-4]
    pos = 1
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

a=Linkedlist(5)
head=a.head
pos=a.pos
    

slowPointer = fastPointer = head
        
while slowPointer and fastPointer:
    fastPointer = fastPointer.next
    if fastPointer == slowPointer:
        print("True")
    elif not fastPointer:
         print("False")
    slowPointer = slowPointer.next
    fastPointer = fastPointer.next
else:
     print("False")

# n1=Linkedlist(3)
# n2=Linkedlist(2)
# n3=Linkedlist(0)
# n4=Linkedlist(-4)

# n1.next=n2
# n2.next=n3
# n3.next=n4
# n4.next=n2

# pos=2

# list1=[]
# list1.append(n1.data)
# list1.append(n2.data)
# list1.append(n3.data)
# list1.append(n4.data)
# print(list1)

# while list1:
#     list1.append()


# if pos==n2 :
#     print("True")
# else:
#     print("False")
