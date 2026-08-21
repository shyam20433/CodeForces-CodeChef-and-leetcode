'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.next = None
'''

class Solution:
    def removeDuplicates(self, head):
        # code here
        curr=head
        while curr and curr.next:
            if curr.data==curr.next.data:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head