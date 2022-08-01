import socket

from utils.Config import Config


class Comms:
    def __init__(self, isCentral: bool, whichDistributed: int, config: Config) -> None:
        self.isCentral = isCentral
        self.mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.message = ""
        self.config = config

        if isCentral:
            self.distributed1 = socket.socket
            self.distributed2 = socket.socket

            self.mySocket.bind((self.config.centralIP, self.config.centralPort))

        # It is a distributed server
        else:
            if 1 > whichDistributed or 2 < whichDistributed:
                raise Exception(
                    f"CommsException: whichDistributed out of range: {whichDistributed}"
                )

            dist1Info, dist2Info = self.config.distributed
            bindAddrs = (
                (dist1Info["ip"], dist1Info["port"])
                if whichDistributed == 1
                else (dist2Info["ip"], dist2Info["port"])
            )

            self.mySocket.bind(bindAddrs)
            self.mySocket.connect((self.config.centralIP, self.config.centralPort))
            print(self.mySocket.recv(1024).decode())

    def closeMySocket(self):
        self.mySocket.close()
        return

    def listenToDistributedServers(self):
        if self.isCentral:
            self.mySocket.listen(2)
            distributed1Connected = False
            distributed2Connected = False
            while True:
                print(
                    "[...] Central server waiting connections from distributed servers"
                )
                conn, addr = self.mySocket.accept()
                distributed = self.config.whichDistributedIsAddr(addr)

                if distributed == None:
                    conn.send("You are not allowed".encode())
                    conn.close()

                elif distributed == 1:
                    self.distributed1 = conn
                    print(f"[.] {addr} connected: 1")
                    self.distributed1.send("[.] CONNECTED: 1".encode())
                    distributed1Connected = True

                elif distributed == 2:
                    self.distributed2 = conn
                    print(f"[.] {addr} connected: 2")
                    self.distributed2.send("[.] CONNECTED: 2".encode())
                    distributed2Connected = True

                if distributed1Connected and distributed2Connected:
                    print("[.] Both distributed servers are connected")
                    break

        else:
            print(
                "Comms Alert: listenToDistributedServers - only the central server\n\
            can listen to connections"
            )

        return
