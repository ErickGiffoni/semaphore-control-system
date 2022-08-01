from utils.Comms import Comms
from utils.Config import Config


class Central:
    def __init__(self) -> None:
        self.config = Config()
        self.comms = Comms(True, 0, self.config)
        self.comms.listenToDistributedServers()
        self.comms.closeMySocket()


centralServer = Central()
