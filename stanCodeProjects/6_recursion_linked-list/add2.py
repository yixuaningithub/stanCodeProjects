"""
File: add2.py
Name: Yi-Syuan Chung
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    cur1 = l1                                                                   # l1 head to cur1
    cur2 = l2                                                                   # l2 head to cur2
    carry = 0                                                                   # carry in
    count = True                                                                # to check if it's the first calculation
    ans_head = cur = ListNode(0, None)              # ans_head to store ListNode of the ans, cur to avoid memory leak
    while cur1.next is not None or cur2.next is not None:
        if cur1.next is None:
            ans = ListNode((cur1.val + cur2.val + carry) % 10, None)
            carry = (cur1.val+cur2.val+carry) // 10                             # calculate the next carry
            cur1.next = ListNode(0, None)                                       # cur1.next.val to 0 for calculation
            cur1 = cur1.next
            cur2 = cur2.next
        elif cur2.next is None:
            ans = ListNode((cur1.val + cur2.val + carry) % 10, None)
            carry = (cur1.val+cur2.val+carry) // 10
            cur2.next = ListNode(0, None)
            cur2 = cur2.next
            cur1 = cur1.next
        else:
            ans = ListNode((cur1.val+cur2.val+carry) % 10, None)
            carry = (cur1.val+cur2.val+carry) // 10
            cur1 = cur1.next
            cur2 = cur2.next
        if count:                                                               # if it's the first calculation
            ans_head = ans                                                      # the ans of the head to ans_head
            cur = ans
        else:
            cur.next = ans
            cur = cur.next
        count = False
    ans = ListNode((cur1.val+cur2.val+carry) % 10, None)                        # if cur1.next and cur2.next is None
    if count:                                                                   # if didn't go to the while loop
        ans_head = ans
        cur = ans
    else:
        cur.next = ans
    if (cur1.val+cur2.val+carry) // 10 == 1:                                    # calculate the last carry
        cur.next.next = ListNode(1, None)
    return ans_head
####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
