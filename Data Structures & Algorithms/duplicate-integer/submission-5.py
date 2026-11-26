class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dists = set()
        for num in nums:
            if num in dists:
                return True
            else:
                dists.add(num)
        return False