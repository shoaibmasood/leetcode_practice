class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n_size =len(nums)
        for i in range(0,n_size):
           nums.append(nums[i])
        return nums
