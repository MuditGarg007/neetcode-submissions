class Solution:

    def util(self, nums, target, arr, i, currSum):
        if currSum > target:
            return
        if currSum == target:
            self.res.append(arr.copy())
            return

        if i==len(nums):
            return

        #exclude
        self.util(nums, target, arr, i+1, currSum)

        #include
        arr.append(nums[i])
        self.util(nums, target, arr, i, currSum + nums[i])
        arr.pop()

        
        

        
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.util(nums, target, [], 0, 0)

        return self.res