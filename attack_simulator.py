from scapy.all import *
import random
import time

target = "127.0.0.1"


def normal_traffic():

    pkt = IP(dst=target)/TCP(dport=80)
    send(pkt, verbose=0)


def port_scan():

    port = random.randint(20,100)
    pkt = IP(dst=target)/TCP(dport=port,flags="S")
    send(pkt, verbose=0)


def suspicious_packet():

    pkt = IP(dst=target)/UDP(dport=9999)/Raw(load="A"*1500)
    send(pkt, verbose=0)


def dos_attack():

    pkt = IP(dst=target)/TCP(dport=80)

    for i in range(5):
        send(pkt, verbose=0)


print("Traffic generator started...")

while True:

    r=random.random()

    if r < 0.5:
        normal_traffic()

    elif r < 0.7:
        port_scan()

    elif r < 0.9:
        suspicious_packet()

    else:
        dos_attack()

    time.sleep(1)