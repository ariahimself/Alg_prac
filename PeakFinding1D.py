class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        L = 0
        R = len(nums) - 1
        
        while (R >= L):
            M = (L+R) //2

            if M==0:
                M_L = -2**32
            if M!= 0:
                M_L = nums[M-1]
            if M == len(nums) -1:
                M_H = -2**32
            if M != len(nums) -1:
                M_H = nums[M+1]
            if nums[M] > M_L and nums[M] > M_H:
                return M
            if nums[M] < M_L:
                R = M-1
            if nums[M] > M_L and nums[M]< M_H :
                L = M+1
        


