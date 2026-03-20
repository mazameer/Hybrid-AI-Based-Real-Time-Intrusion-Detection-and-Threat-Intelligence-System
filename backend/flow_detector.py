from scapy.all import IP, TCP, UDP

def extract_features(packet):

    packet_size = len(packet)

    protocol = 0

    if TCP in packet:
        protocol = 1

    elif UDP in packet:
        protocol = 2

    else:
        protocol = 0

    packet_rate = packet_size / 100

    return [packet_size, protocol, packet_rate]