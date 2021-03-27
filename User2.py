from pyp2p.net import *
import time

#setup second user
second = Net(passive_bind="127.0.0.1", passive_port="1212", interface="eth0:1", node_type="passive", debug=1)
second.start()
second.bootstrap()
second.advetise()

#loop
while True:
    for con in second:
        con.send_line('test')

    time.sleep(1)