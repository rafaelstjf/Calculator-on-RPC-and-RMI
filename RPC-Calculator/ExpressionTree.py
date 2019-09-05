import xmlrpc.client
import socket

addition = xmlrpc.client.ServerProxy("http://localhost:1231/")
subtraction = xmlrpc.client.ServerProxy("http://localhost:1232/")
multiplication = xmlrpc.client.ServerProxy("http://localhost:1233/")
division = xmlrpc.client.ServerProxy("http://localhost:1234/")

ops = {
  "+": (lambda a, b: addition.calcAddition(a,b)),
  "-": (lambda a, b: subtraction.calcSubtraction(a,b)),
  "*": (lambda a, b: multiplication.calcMultiplication(a,b)),
  "/": (lambda a, b: division.calcDivision(a,b))
}

class ExpressionTree:
    def __init__(self, expression):
        self.expression = expression
        self.outQueue = []
        self.opStack = []
        self.constructTree()

    def isOperator(self, c):
        if c == '+' or c == '-' or c == '/' or c == '*' or c == '(' or c == ')':
            return True
        return False

    def predecence(self, op1, op2):
        if op1 == '+' and op2 == '*':
            return -1
        if op1 == '*' and op2 == '+':
            return 1
        if op1 == '+' and op2 == '/':
            return -1
        if op1 == '/' and op2 == '+':
            return 1
        if op1 == '-' and op2 == '*':
            return -1
        if op1 == '*' and op2 == '-':
            return 1
        if op1 == '-' and op2 == '/':
            return -1
        if op1 == '/' and op2 == '-':
            return 1
        if op1 == '+' and op2 == '-' or op1 == '-' and op2 == '+':
            return 0
        if op1 == '*' and op2 == '/' or op1 == '/' and op2 == '*':
            return 0
            
    def constructTree(self):
        number = ''
        #tokenization of input
        for c in range(len(self.expression)):
            curr = self.expression[c]
            if self.isOperator(curr):
                # if length of number is > 1, reverse it and insert to output queue
                number = number[::-1]
                self.outQueue.insert(0, number)
                
                ''' while there is a function at the top of the operator stack)
                    or (there is an operator at the top of the operator stack with greater precedence)
                    or (the operator at the top of the operator stack has equal precedence and is left associative))
                    and (the operator at the top of the operator stack is not a left parenthesis)'''
                if self.opStack: 
                    top_op = self.opStack[-1]
                    predecence = self.predecence(curr, top_op)
                while self.opStack and top_op is not '(' and predecence == -1:  
                    top_op = self.opStack.pop()
                    self.outQueue.insert(0, top_op)
                #if the token is a operator, push to operator stack
                self.opStack.append(curr)
                number = ''
            else:
                number = curr + number
            if curr == '(':
                self.opStack.append(curr)
            if curr == ')':
                top_op = self.opStack[-1]
                while top_op != '(':
                    top_op = self.opStack.pop()
                    self.outQueue.insert(0, top_op)
                top_op = self.opStack[-1]
                if top_op == '(':
                    self.opStack.pop()
        if number != '' and not self.isOperator(number):
            number = number[::-1]
            self.outQueue.insert(0, number)
        
        
        # while operator stack is not empty, insert it's elements to output queue
        while self.opStack:
            self.outQueue.insert(0, self.opStack.pop())
    
    def evaluate(self):
        tokens = self.outQueue[::-1]
        stack = []

        for token in tokens:
            if token == '' or token == ')' or token == '(':
                continue
            
            if token in ops:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = ops[token](arg1, arg2)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()