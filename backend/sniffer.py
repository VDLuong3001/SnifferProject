from scapy.all import sniff, IP
from database import packets_collection

def process_packet(packet):

    if packet.haslayer(IP):

        packet_data = {
            "src_ip": packet[IP].src,
            "dst_ip": packet[IP].dst,
            "protocol": packet[IP].proto
        }

        packets_collection.insert_one(packet_data)

        print("Inserted:", packet_data)

def start_sniffer():
    sniff(prn=process_packet, store=False)