class Solution(object):
    def exclusiveTime(self, n, logs):
        stack = []
        timestamp = [0]*n

        for i in logs:
            print(stack)
            print(timestamp)
            if i[2]=="s":
                stack.append(i)
            else:
                j = stack.pop()
                if i[2]=="e":
                    index1 = int(j[0])
                    a = int(i[-1])
                    b = int(j[-1])
                    print(f"----a={a},b={b},at index={index1}")
                    timestamp[index1] += a-b
                    continue
                stack.append(j)
        return timestamp
    
sol = Solution()
print(sol.exclusiveTime(2,["0:start:0","1:start:2","1:end:5","0:end:6"]))

class Solution(object):
    def exclusiveTime(self, n, logs):
        stack = []
        res = [0] * n
        prev_time = 0

        for log in logs:
            fid, typ, time = log.split(":")
            fid = int(fid)
            time = int(time)

            if typ == "start":
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time

            else:  # "end"
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return res