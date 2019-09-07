from ExpressionTree import *

expression = str(raw_input("Enter an expression: "))
exp_solver = ExpressionTree(expression)
result = exp_solver.evaluate()
print("Result: {}".format(result))