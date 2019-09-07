import Pyro.naming
import Pyro.core
from Pyro.errors import PyroError,NamingError

import calculator

###### testclass Pyro object

class multCalc(Pyro.core.ObjBase, calculator.multCalc):
        pass

###### main server program

def main():
        Pyro.core.initServer()
        daemon = Pyro.core.Daemon()
        # locate the NS
        locator = Pyro.naming.NameServerLocator()
        print('searching for Name Server...')
        ns = locator.getNS()
        daemon.useNameServer(ns)

        # connect a new object implementation (first unregister previous one)
        try:
                # 'test' is the name by which our object will be known to the outside world
                ns.unregister('mult')
        except NamingError:
                pass

        # connect new object implementation
        daemon.connect(multCalc(),'mult')

        # enter the server loop.
        print('Server object "mult" ready.')
        daemon.requestLoop()

if __name__=="__main__":
        main()