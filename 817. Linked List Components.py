# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        count = 0
        ele = 0
        flag = False
        Gset = set(G)
        while head is not None:
            if head.val in Gset and ele < len(Gset):
                flag = True
                ele += 1
            elif ele >= len(Gset):
                break
            else:
                if flag == True:
                    count+=1
                    flag = False
            head = head.next
        if flag == True:
            return count+1
        else:
            return count