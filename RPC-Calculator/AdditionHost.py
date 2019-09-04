from xmlrpc.server import SimpleXMLRPCServer
def calcAddition (n1, n2):
    return n1+n2
        

server = SimpleXMLRPCServer(("localhost", 1231))
print("Listening on port 1231...")
server.register_function(calcAddition, "calcAddition")
server.serve_forever()