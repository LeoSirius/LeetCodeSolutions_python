from utils_py.list import *

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB  # 注意这里是让p1走B，让p2走A
            p2 = p2.next if p2 else headA
        return p1


def test(test_name, headA: ListNode, headB: ListNode, expected: ListNode):
    res = Solution().getIntersectionNode(headA, headB)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    # 输入：intersectVal = 8,
    # listA = [4,1,8,4,5],
    # listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    # 输出：Reference of the node with value = 8
    headA1 = ListNode(4)
    headA1.next = ListNode(1)
    headA1.next.next = ListNode(8)
    headA1.next.next.next = ListNode(4)
    headA1.next.next.next.next = ListNode(5)
    headB1 = ListNode(5)
    headB1.next = ListNode(0)
    headB1.next.next = ListNode(1)
    headB1.next.next.next = headA1.next.next

    expected1 = ListNode(8)
    expected1.next = ListNode(4)
    expected1.next.next = ListNode(5)

    test('test1', headA1, headB1, expected1)






# 输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
# 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。


# 输入：intersectVal = 2, 
# listA = [0,9,1,2,4], 
# listB = [3,2,4], skipA = 3, skipB = 1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。

# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。





