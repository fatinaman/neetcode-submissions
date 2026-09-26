class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_hash = {} #save the index of complement in hashmap
        for i,v in enumerate(nums):
            complement = target - v
            if complement not in comp_hash:
                comp_hash[v] = i
            else:
                return [comp_hash[complement], i]