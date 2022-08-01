from threading import Thread

from utils.Comms import Comms
from utils.Config import Config
from .junction.Junction import Junction


class Distributed(Thread):
    def __init__(self, distributedId: int) -> None:
        """
        distributedId is either 1 or 2
        """
        Thread.__init__(self)
        self.name = f"Distributed Server {distributedId}"
        self.config = Config()
        self.comms = Comms(False, distributedId, self.config)
        self.junction = Junction(
            distributedId,
            self.config.getJunction(distributedId, 1)
        )

    def run(self):
        print("Starting " + self.name)
        self.junction.start()

        print("Exiting " + self.name)
        self.junction.join()

        self.comms.closeMySocket()
        return


d = Distributed(1)
d2 = Distributed(2)

d.start()
d2.start()

d.join()
d2.join()
