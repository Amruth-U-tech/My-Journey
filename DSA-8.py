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