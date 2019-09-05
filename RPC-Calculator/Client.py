from ExpressionTree import *

expression = input("Enter an expression: ")
exp_solver = ExpressionTree(expression)
result = exp_solver.evaluate()
print("Result: {}".format(result))