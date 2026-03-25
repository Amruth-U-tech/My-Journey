class Solution(object):
    def characterReplacement(self, s, k):
        count = [0] * 26
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            count[index] += 1

            max_freq = max(max_freq, count[index])

            # Shrink window if replacements exceed k
            while (right - left + 1) - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k still remains, remove from end
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else "0"