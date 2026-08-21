# Node is defined as:
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
def solve(head):
    count=0
    #Return the number of critical points (integer)
    curr=head.next
    prev=head
    while curr.next:
        temp=curr.next
        if prev.val<curr.val>temp.val or prev.val>curr.val<temp.val:
            count+=1
        curr.next=prev
        prev=curr
        curr=temp
    return count
        