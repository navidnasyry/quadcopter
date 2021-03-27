from pyp2p.net import *
import time


#setup first user
first = Net(Passive_bind="127.0.0.1", passive_port=1234, interface="eth0:2", node_type="passive", debug=1)
first.start()
first.bootstrap()
first.advertise()

#loop
while True:
    for con in first:
        for reply in con:
            print(reply)

    time.sleep(1)
