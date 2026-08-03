# TWO - PASS

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}
        for i in range(len(nums)):
            elements[nums[i]] = i
        
        for i in range(len(nums)):
            new_target = target - nums[i]

            if new_target in elements and elements[new_target] != i:
                return [i, elements[new_target]]

 
