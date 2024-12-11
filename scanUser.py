import nmap  # Biblioteca para scanner de rede
from scapy.all import ARP, Ether, srp  # Funções da Scapy para análise de rede


def get_network_devices(ip_range="192.168.1.1/24"):
    """
    Obtém dispositivos conectados à rede local usando ARP e Nmap.
    :param ip_range: Intervalo de IPs a ser escaneado, como "192.168.1.1/24"
    :return: Lista de dispositivos encontrados com IP, MAC e função (sistema operacional).
    """
    devices = []

    try:
        # Passo 1: Usando ARP para identificar dispositivos na rede
        arp = ARP(pdst=ip_range)
        # Pacote Ethernet para broadcast
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp
        result = srp(packet, timeout=3, verbose=0)[
            0]  # Envia e recebe pacotes ARP

        # Adiciona dispositivos encontrados ao dicionário
        for sent, received in result:
            device = {
                "ip": received.psrc,  # IP do dispositivo
                "mac": received.hwsrc,  # MAC do dispositivo
                # Inicializa o campo de função (a ser descoberto pelo Nmap)
                "function": None
            }
            devices.append(device)

        # Passo 2: Usando Nmap para tentar identificar a função de cada dispositivo
        nm = nmap.PortScanner()

        for device in devices:
            try:
                # Faz um scan de portas no IP do dispositivo para identificar o sistema operacional
                # Pode-se modificar o intervalo de portas
                nm.scan(device["ip"], "22-443")
                # Tenta identificar o sistema operacional
                if 'osmatch' in nm[device["ip"]]:
                    device["function"] = nm[device["ip"]]["osmatch"][0]["name"]
                else:
                    device["function"] = "Desconhecido"
            except Exception as e:
                print(f"Erro ao tentar escanear o dispositivo {
                      device['ip']}: {e}")
                device["function"] = "Desconhecido"

        # Exibe os dispositivos encontrados com suas funções
        for device in devices:
            print(f"IP: {device['ip']}, MAC: {
                  device['mac']}, Função: {device['function']}")

    except Exception as e:
        print(f"Erro ao obter dispositivos da rede: {e}")

    return devices


if __name__ == "__main__":
    print("Iniciando o scan de dispositivos na rede...")
    # Substitua pelo seu intervalo de IPs
    devices = get_network_devices("192.168.0.1/24")
    print("\nScan de dispositivos finalizado.")
