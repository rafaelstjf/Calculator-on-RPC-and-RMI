import xmlrpc.client
import socket
addition = xmlrpc.client.ServerProxy("http://localhost:1231/")
subtraction = xmlrpc.client.ServerProxy("http://localhost:1232/")
multiplication = xmlrpc.client.ServerProxy("http://localhost:1233/")
division = xmlrpc.client.ServerProxy("http://localhost:1234/")


print(multiplication.calcMultiplication(3,2))
print(division.calcDivision(3,2))
print(addition.calcAddition(3,2))
print(subtraction.calcSubtraction(3,2))
