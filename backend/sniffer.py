from scapy.all import sniff, IP
from predictor import predict
from flow_detector import extract_features
from database import save_alert


def process_packet(packet):

    if IP in packet:

        src_ip = packet[IP].src

        features = extract_features(packet)

        attack, prob = predict(features, src_ip)

        print("Packet detected:", src_ip, attack)

        # IMPORTANT: Save every packet
        save_alert(src_ip, attack, prob)


def start_sniffer():

    print("Sniffer started...")

    sniff(
        prn=process_packet,
        store=False
    )


if __name__ == "__main__":
    start_sniffer()