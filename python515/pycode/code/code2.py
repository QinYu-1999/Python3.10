# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, nums):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        for i in range(1, len(nums)):
            print(f"1:{nums[i]}")
            print(f"2:{nums[i - 1] + nums[i]}")
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
            print(nums)
        return max(nums)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution().mergeTwoLists(nums)
    print(s)
