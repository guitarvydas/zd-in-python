class Connection:
    def __init__ (self, from_who, from_port, to_who, to_port):
        self.sender = from_who
        self.send_port = from_port
        self.receiver = to_who
        self.receive_port = to_port
        
