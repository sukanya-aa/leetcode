'''
445. Add Two Numbers II

Tag: Medium
https://leetcode.com/problems/add-two-numbers-ii/description/

You are given two non-empty linked lists representing two non-negative integers. The most 
significant digit comes first and each of their nodes contains a single digit. Add the two 
numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]

 
Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Using stacks to solve the problem. Technically, this is also a form of reversing the list.
Stacks have Last In First Out (LIFO)
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        #Append values of the input list to the stacks
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        c = 0    #Carry   
        t_head = None #Temporary head of resultant linked list
        while stack1 or stack2 or c:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + c
            c = total // 10        #Floor operator will give the quotient rounded to the nearest integer(7//10=0)
            new_n = ListNode(total % 10) #Modulo operator will return dividend if the divisor is greater than dividend(7 % 10 = 7) and the remainder, otherwise(13%10=3). This will be the value of this node(ex, 0 if total is 10)
            '''
            new_n.next = t_head: Link the new node to the temporary head.
            The next attribute of new_n is assigned the current value of t_head.
            This operation effectively links the new node to the current linked list under construction.
            t_head = new_n: Update the temporary head to the new node.
            t_head is updated to point to the newly created node new_n.
            Since this node is now at the beginning of the linked list, it becomes the new head, and the previously created nodes are linked after it.
            '''
            new_n.next = t_head
            t_head = new_n
        return t_head
