from scapy.all import IP, ICMP, sr1


def ping_device(ip):
    """Envia um ping para um dispositivo específico."""
    packet = IP(dst=ip) / ICMP()
    response = sr1(packet, timeout=2, verbose=0)
    if response:
        print(f"{ip} está ativo.")
    else:
        print(f"{ip} não respondeu.")


ping_device("192.168.0.9")
