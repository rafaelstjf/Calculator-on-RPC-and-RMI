from xmlrpc.server import SimpleXMLRPCServer

def calcMultiplication (n1, n2):
    return n1*n2

server = SimpleXMLRPCServer(("localhost", 1233))
print("Listening on port 1233...")
server.register_function(calcMultiplication, "calcMultiplication")
server.serve_forever()
