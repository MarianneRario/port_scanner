"""
Simple implementation of port scanner like NMAP.
Port scanner code to know how the scanning of ports on the target machine works.
The output includes the open port and the port banner.
"""

import socket
import termcolor
import threading
import time

def scan(target, ports):
    target_list = target.split(",")

    start_time = time.time()
    
    for t in target_list:
        print(termcolor.colored("Port scanner report for " + t, 'green'))
        for port in range(1, ports+1):
            thread = threading.Thread(target=scan_port, args=(t.strip(" "), port))
            thread.start()

    end_time = time.time()
    print("To all scan all ports it took {} seconds".format(end_time-start_time))


def scan_port(target_ip, port):
    try:
        sock = socket.socket() # initialize socket object
        sock.connect((target_ip, port)) # connect to the target ip address and port: success/fail
        banner = sock.recv(1024).decode()

        print("port {} is open with banner {}".format(port, banner))
        sock.close()
    except:
        pass


targets_ip = input("[*] Enter targets ip to scan ( split the input by comma(,) ): ")
port = int(input("[*] Enter port ranges to scan: "))

print("[*] Scanning Target")
scan(targets_ip, port)

