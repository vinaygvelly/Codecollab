class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_set = set()

        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False


sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))
