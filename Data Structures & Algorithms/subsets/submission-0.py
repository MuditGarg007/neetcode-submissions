class Solution:

    def util(self, nums, i, arr):
        if i==len(nums):
            self.res.append(arr.copy())
            return 

        self.util(nums, i+1, arr)
        arr.append(nums[i])
        self.util(nums, i+1, arr)
        arr.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.util(nums, 0, [])
        return self.res