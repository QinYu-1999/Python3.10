class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index = 0  #nums1索引
        count = 0  #nums2索引
        while count<n:
            if nums1[index] >nums2[count]:
                nums1[index+1:m+count+1] = nums1[index:m+count]
                nums1[index] = nums2[count]
                print(f"1:{nums1}")
                count+=1
            if index > m+count-1:
                nums1[index] = nums2[count]
                print(f"2:{nums1}")
                count+=1
            index+=1
        return nums1

if __name__ == '__main__':
    nums1 =[1,2,3,0,0,0]
    nums2 = [2,5,6]
    ss = Solution().merge(nums1,3,nums2,3)
    print(ss)