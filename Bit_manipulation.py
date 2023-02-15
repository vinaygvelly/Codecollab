class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0 # as 0^n = n
        for i in nums:
            res = i ^ res
        return res
    def hammingWeight(self, n: int) -> int:
        count = 0
        n = str(bin(n))
        for i in n:
            if i == "1":
                count = count + 1
        return count

    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        for i in range(res):
            res += (i - nums[i])
        return res

    def countBits(self, n: int) -> list[int]:
        count_list = []
        for i in range(n+1):
            count_list.append(bin(i).count('1'))
        return count_list

    def reverseBits(self, nu: int) -> int:
        res = 0

        for i in range(32):
            bit = (nu >> i) & 1
            res = res | (bit << (31 - i))
        return res



sol = Solution()

single_nums = [2,2,1]
print(sol.singleNumber(single_nums))

# hamm_n = 00000000000000000000000000001011
# sol.hammingWeight(hamm_n)


count_n=5 #countBits
print(sol.countBits(count_n))

# nu = 00000010100101000001111010011100 #reversebit
# sol.reverseBits(nu)

nums = [3,0,1] #missing number
print(sol.missingNumber(nums))