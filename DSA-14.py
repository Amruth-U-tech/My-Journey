class Solution(object):
    def getConcatenation(self, nums):
        ans = nums+nums
        return ans
    def containsDuplicate(self, nums):
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
    def shuffle(self, nums, n):
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
        