import sys
import queue
import message

class Writer:
    def __init__ (self):
        self.input = queue.Queue ()

    def handler (self, msg, outq):
        if msg.port == "go":
            outq.put (message.Message (port="request", payload=True))
        elif msg.port == "":
            c = msg.payload
            print (c, end='')
            outq.put (message.Message (port="request", payload=True))
        elif msg.port == "eof":
            sys.exit (0)
