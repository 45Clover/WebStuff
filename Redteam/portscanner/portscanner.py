import socket 
import threading
from queue import Queue



target = "target ip"
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
#if connectable
for port in range(1, 1024):
    result = portscan(port)
    if result:
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed!".format(port))

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)



#the actual port scan
def worker():
    while not queue.empty():

        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)

    


port_list = range(40, 80)
fill_queue(port_list)

thread_list = []

for t in range(10):
    thread = threading.Thread(target=worker)

    thread_list.append(thread)

for thread in thread_list:
    thread.start()



for thread in thread_list:
    thread.join()


print("Open ports are: ", open_ports)

