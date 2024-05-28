import queue
import message

class Reader:
    def __init__ (self):
        self.filename = ""
        self.fd = None
        self.input = queue.Queue ()
        
    def handler (self, msg, outq):
        if msg.port == "initialize":
            self.filename = msg.payload
            self.fd = open (self.filename, "r")
        elif msg.port == "request":
            c = self.fd.read (1)
            if len (c) == 1:
                outq.put (message.Message (port="", payload=c))
            else:
                outq.put (message.Message (port="eof", payload=""))
        else:
            raise Exception (f'unhandled message in Reader {msg}')
        
        
