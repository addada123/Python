#https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b/train/python

#(ax+b)^n

import re

def factorial(n):
	if(n == 0):
		return 1
	else:
		return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def symbol(symbol, n):
    if symbol == "-" and n % 2 != 0: return "-"
    return ""

def expand(expr):
    exponential = str(re.findall("[^\\^]*$", expr)[0])
    symbol_expr = expr[1]
    text = str(re.findall("[a-zA-Z]", expr)[0])
    if re.findall(".+[(\\^)]", expr)[0][2:-2][0] == text and symbol_expr == "-":
        symbol_numbr = 1
    elif symbol_expr == text:
        symbol_numbr = 1
    else:
        if symbol_expr == "-":
            symbol_numbr = re.findall("^\d+", (re.findall(".+[(\\^)]", expr)[0][2:-2]))[0]
        else:
            symbol_numbr = re.findall("^\d+", (re.findall(".+[(\\^)]", expr)[0][1:-2]))[0]
    last_number = int(re.findall("\W\d+(?=/?)$", (re.findall(".+[(\\^)]", expr)[0][1:-2]))[0])
    answer = ""
    
    if exponential == '0':
        return '1'
    
    elif last_number == 0:
        return symbol(symbol_expr, exponential) + text + "^" + exponential
    
    for i in range(0, int(exponential) + 1):
        binom = int(nCr(int(exponential), i))
        exp = int(exponential) - i
        second_number = last_number ** i
        
        if i == 0:
            number = binom * (symbol_numbr ** exp)
            if number == 1:
                if exp == 1:
                    answer += symbol(symbol_expr, exp) + text
                else:
                    answer += symbol(symbol_expr, exp) + text + "^" + str(exp)
            else:
                if exp == 1:
                    answer += symbol(symbol_expr, exp) + str(number) + text
                else:
                    answer += symbol(symbol_expr, exp) + str(number) + text + "^" + str(exp)
                
        elif exp > 0 and i > 0:
            number = binom * second_number * (symbol_numbr ** exp)
            symbol_eq = symbol(symbol_expr, exp)
            if symbol_eq == "-":
                number *= -1
            if number > 0:
                if exp == 1:
                    answer += "+" + str(number) + text
                else:
                    answer += "+" + str(number) + text + "^" + str(exp)
            else:
                if exp == 1:
                    answer += str(number) + text
                else:
                    answer += str(number) + text + "^" + str(exp)
                    
        elif i == int(exponential):
            number = binom * (last_number ** i)
            if number > 0:
                answer += "+" + str(number)
            else:
                answer += str(number)
                
    return answer
    
    
    
print(expand("(-x+4)^3"))
