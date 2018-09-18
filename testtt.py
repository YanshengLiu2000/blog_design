class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums)==1:
            return
        temp=None
        for i in range(len(nums)-1,0,-1):
            if nums[i]<=nums[i-1]:
                continue
            else:
                temp=i-1
                break
        if temp!=None:
            for j in range(len(nums)-1,temp,-1):
                if nums[j]>nums[temp]:
                    nums[temp],nums[j] = nums[j], nums[temp]
                    break
            for i in range(temp+1,len(nums)-1):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1], nums[i]
        else:
            nums.sort()
        return nums

print(Solution().nextPermutation([5,4,7,5,3,2]))