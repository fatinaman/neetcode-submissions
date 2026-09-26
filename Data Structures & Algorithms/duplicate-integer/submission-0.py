class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for v in nums:
            if v in duplicate:
                return True
            else:
                duplicate.add(v)
        return False