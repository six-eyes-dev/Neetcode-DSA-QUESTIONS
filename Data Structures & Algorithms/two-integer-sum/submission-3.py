class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pass
        elements = {}
        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target in elements:
                return [elements[new_target], i]
            
            elements[nums[i]] = i