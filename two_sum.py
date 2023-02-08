class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pervMap = {} # val : index

        for i,n in enumerate(nums):
            diff = target - n
            if diff in pervMap:
                return [pervMap[diff], i]
            pervMap[n] = i
        return

sol = Solution()

print(sol.twoSum([2,7,11,15], 9))