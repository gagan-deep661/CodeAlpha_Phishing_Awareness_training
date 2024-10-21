from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

# Function to handle packets
def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        print(f"[+] Packet: {ip_src} -> {ip_dst} (Protocol: {proto})")
        
        if TCP in packet:
            print(f"[*] TCP Packet: Source Port: {packet[TCP].sport}, Destination Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"[*] UDP Packet: Source Port: {packet[UDP].sport}, Destination Port: {packet[UDP].dport}")

# Start sniffing
def start_sniffing():
    print("Starting network sniffer...")
    sniff(prn=packet_callback, store=False)

# Run the sniffer
if __name__ == "__main__":
    start_sniffing()
