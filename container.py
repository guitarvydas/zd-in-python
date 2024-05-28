# Container simplified for clarity of this example, e.g. children here are hard-coded (not necessary), connections need "direction" to allow recursive containers, etc.

import reader
import writer
import queue
import message
import connection

class Container:
    # see ![](container.png)
    def __init__ (self):
        reader_child = reader.Reader ()
        writer_child = writer.Writer ()
        self.children = [reader_child, writer_child]
        self.connections = [
            connection.Connection (reader_child, '', writer_child, ''),
            connection.Connection (writer_child, 'request', reader_child, 'request')
        ]

    def dispatcher (self):
        while self.any_child_ready ():
            self.dispatch_some_child ()

    def any_child_ready (self):
        for child in self.children:
            if not child.input.empty ():
                return True
        return False

    def dispatch_some_child (self):
        for child in self.children:
            if not child.input.empty ():
                in_msg = child.input.get ()
                outq = queue.Queue ()
                child.handler (in_msg, outq)
                self.route_outputs (child, outq)
                return

    def route_outputs (self, child, outq):
        while not outq.empty ():
            out_msg = outq.get ()
            for c in self.connections:
                if (child == c.sender) and (out_msg.port == c.send_port):
                    remapped_msg = self.make_msg_relative_to_receiver (out_msg, c.receiver, c.receive_port)
                    c.receiver.input.put (remapped_msg)

    def make_msg_relative_to_receiver (self, msg, receiver, port):
        return message.Message (port=port, payload=msg.payload)

    def reader (self):
        return self.children [0]

    def writer (self):
        return self.children [1]

