'''
import ast

x, k = map(int,input().split())

polynomial = input() # eg: x**3 + x**2 + x+ 1

result = ast.literal_eval(polynomial)#  ast.literal_eval this is one of trh key word for evaluvate this equation eg: x**3 + x**2 + x+ 1 

print(result == k)

'''