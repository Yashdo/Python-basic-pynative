head = [1,2,3,4,5]
list1=[]

class ListNode:
    def __init__(self, val=0, next=None,k=2):
        self.val = val
        self.next = next
        
        while k > val:
            val = next(k)
            print(val)
            k+=1


