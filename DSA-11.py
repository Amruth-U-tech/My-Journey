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
sol = Solution()
print(sol.evalRPN(tokens))
