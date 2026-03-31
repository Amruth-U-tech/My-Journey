class Solution(object):
    def removeKdigits(self, num, k):
        l = list(num)
        count = 0
        s = ""
        for i in range(len(num)-2):
            print(count)
            print(l)
            print(s)
            print("---------------")
            s = s+l[i:i+2]
            if count==k:
                return s+l[-1]
            if int(l[i])<int(l[i+1]):
                s += l[i]
                l.pop(i+1)
                count +=1
            #elif int(l[i])>int(l[i+1]):
                #continue
            else:
                s+=l[i+1]
                l.pop(i)
                count+=1
        return (s+l[-1])
sol = Solution()
print(sol.removeKdigits("10200",1))


#this code is good but this is a global optimal solution
class Solution(object):
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # if still k left → remove from end
        while k > 0:
            stack.pop()
            k -= 1

        # build result
        res = ''.join(stack).lstrip('0')