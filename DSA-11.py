tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

# stack = []

# for token in tokens:
#     if token in {"+", "-", "*", "/"}:
#         b = stack.pop()
#         a = stack.pop()

#         if token == "+":
#             stack.append(a + b)
#         elif token == "-":
#             stack.append(a - b)
#         elif token == "*":
#             stack.append(a * b)
#         elif token == "/":
#             stack.append(int(a / b))

#     else:
#         stack.append(int(token))

# print(stack)

class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:

            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))  # important

            else:
                stack.append(int(token))

        return stack[0]

    def buildArray(self, target, n):
        index1 = 0
        l = []
        for i in range(1,n+1):

            if i==target[index1]:
                l.append("Push")
                if index1==len(target)-1:
                    return l
                index1+=1
                continue
            l.append("Push")
            l.append("Pop")
            

        return l
