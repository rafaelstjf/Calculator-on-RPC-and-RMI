import Pyro.naming
import Pyro.core
from Pyro.errors import PyroError,NamingError

from calculator import divCalc

###### testclass Pyro object

class divclass(Pyro.core.ObjBase, divCalc):
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
                ns.unregister('div')
        except NamingError:
                pass

        # connect new object implementation
        daemon.connect(divclass(),'div')

        # enter the server loop.
        print('Server object "div" ready.')
        daemon.requestLoop()

if __name__=="__main__":
        main()