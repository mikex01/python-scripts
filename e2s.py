#!/usr/bin/python3
# @mikex01 20211228
# event -> syslog
# ./e2s.py 192.168.1.2 514  'datetime -- mesage syslog'

import socket
import sys

def event2syslog(event="test", host="127.0.0.1", port=514):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    s.sendto(event.encode("utf-8"), (host, port))
    s.close()

if __name__ == "__main__":
    host=str(sys.argv[1])
    port=int(sys.argv[2])
    event=str("".join(sys.argv[3:]))
    event2syslog(event, host, port)
    print("Event sent to udp://{}:{}".format(host, port))