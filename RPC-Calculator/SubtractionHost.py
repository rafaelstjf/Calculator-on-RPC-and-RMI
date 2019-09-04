from xmlrpc.server import SimpleXMLRPCServer
def calcSubtraction (n1, n2):
    return n1-n2
        

server = SimpleXMLRPCServer(("localhost", 1232))
print("Listening on port 1232...")
server.register_function(calcSubtraction, "calcSubtraction")
server.serve_forever()