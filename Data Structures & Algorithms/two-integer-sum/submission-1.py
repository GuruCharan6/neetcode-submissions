class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                      # value -> index
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need] , i]   # 1-based
            seen[x] = i
        return []


        