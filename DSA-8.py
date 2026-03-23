class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        hashing = {0:1}

        for i in nums:
            prefix_sum+=i

            if prefix_sum-k in hashing:
                count+=hashing[prefix_sum-k]
            hashing[prefix_sum]=hashing.get(prefix_sum,0)+1
        return count
    def findMaxLength(self, nums):
        prefix_sum = 0
        hashmap = {0: -1}
        max_len = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in hashmap:
                length = i - hashmap[prefix_sum]
                max_len = max(max_len, length)
            else:
                hashmap[prefix_sum] = i

        return max_len
        