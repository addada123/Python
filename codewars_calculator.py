import re
class Calculator(object):
    def evaluate(self, string):
        total = 0
        string = re.sub("[\s]" , "", string)
        def math_op(total, a, b):
            if a == "/":
                total /= b
            elif a == "*":
                total *= b
            elif a == "+":
                total += b
            elif a == "-":
                total -= b
            return total
        def parentheses(string):
            pt = re.findall('\(.*?\)', string)
            return parentheses(pt)
        return parentheses(string)
