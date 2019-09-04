from xmlrpc.server import SimpleXMLRPCServer
def calcDivision (n1, n2):
    if(n2!=0):
        return n1/n2
    else:
        return 0 #divisao por zero
        

server = SimpleXMLRPCServer(("localhost", 1234))
print("Listening on port 1234...")
server.register_function(calcDivision, "calcDivision")
server.serve_forever()