class Solution(object):

    # def __init__(self,nums, target):
    #     self.nums = nums
    #     self.target = target


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = 0
        R = len(nums)-1
        
        while (R >=L):
            M = int((R+L)/2)
            if nums[M]==target:
                return M
            if nums[M] > target:
                R = M -1
            if nums[M] < target:
                L = M + 1
        return -1


    def test(self, nums, target):
        binary_search = Solution()
        Index = binary_search.search(nums, target)

        if target in nums:

            index = nums.index(target)
            print (index)
        else :
            index = -1



        return index == Index


nums = [-1,0,3,5,9,12]
target = 9

binary_search = Solution()

Index = binary_search.search(nums, target)

Output = binary_search.test(nums, target)

print (Output)

if Output == True:
    print('--------Approved--------')
else: 
    print('--------Rejected--------')