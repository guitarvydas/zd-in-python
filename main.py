import reader
import writer
import queue
import message
import container

top = container.Container ()
# initialization
top.reader ().input.put (message.Message (port="initialize", payload="test.txt"))
top.dispatcher ()

# run system
top.writer ().input.put (message.Message (port="go", payload=True))
top.dispatcher ()

