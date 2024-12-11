import speedtest
import time
import requests
import psutil
from scapy.all import ARP, Ether, srp
import datetime

# Função para obter a velocidade contratada da internet


def get_contracted_speed():
    """Simula a obtenção da velocidade contratada pela internet. Você pode personalizar esse valor."""
    # Exemplo de velocidade contratada (em Mbps)
    return 100  # Substitua pelo valor real da sua velocidade contratada

# Função para detectar traffic shaping


def detect_traffic_shaping(measured_speed, contracted_speed, tolerance=0.8):
    """Detecta se há *traffic shaping* comparando a velocidade medida com a contratada."""
    if measured_speed < contracted_speed * tolerance:
        return f"**Traffic Shaping Detectado: A velocidade medida ({measured_speed:.2f} Mbps) está abaixo da contratada ({contracted_speed} Mbps)**"
    else:
        return "Nenhum *Traffic Shaping* Detectado"


def test_speed(iterations=3):
    """Realiza testes de velocidade usando o Speedtest e calcula a média."""
    print("Realizando testes de velocidade...")
    download_speeds = []
    upload_speeds = []

    for i in range(iterations):
        print(f"Teste {i + 1}/{iterations}...")
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            # Convertendo para Mbps
            download_speeds.append(st.download() / 1_000_000)
            upload_speeds.append(st.upload() / 1_000_000)
        except speedtest.ConfigRetrievalError as e:
            print(f"Erro ao obter configuração do Speedtest: {e}")
            download_speeds.append(0)
            upload_speeds.append(0)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            download_speeds.append(0)
            upload_speeds.append(0)

    avg_download_speed = sum(download_speeds) / len(download_speeds)
    avg_upload_speed = sum(upload_speeds) / len(upload_speeds)

    print(f"\nMédia de Velocidade de Download: {avg_download_speed:.2f} Mbps")
    print(f"Média de Velocidade de Upload: {avg_upload_speed:.2f} Mbps")

    return avg_download_speed, avg_upload_speed


def get_network_devices():
    """Obtém dispositivos conectados à rede local."""
    print("\nObtendo dispositivos conectados à rede...")
    devices = []
    try:
        ip_range = "192.168.0.1/24"  # Ajuste conforme necessário
        arp = ARP(pdst=ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp
        result = srp(packet, timeout=3, verbose=0)[0]

        for sent, received in result:
            devices.append({
                "ip": received.psrc,
                "mac": received.hwsrc
            })

        print("Dispositivos encontrados:")
        for device in devices:
            print(f"IP: {device['ip']}, MAC: {device['mac']}")
    except Exception as e:
        print(f"Erro ao obter dispositivos da rede: {e}")

    return devices


def save_results_to_file(filename, download, upload, devices, traffic_shaping_result):
    """Salva os resultados dos testes em um arquivo de texto."""
    try:
        with open(filename, 'w') as file:
            # Salvar velocidades de download e upload
            file.write("Resultados do Teste de Velocidade\n")
            file.write(f"Média de Velocidade de Download: {
                       download:.2f} Mbps\n")
            file.write(f"Média de Velocidade de Upload: {upload:.2f} Mbps\n\n")

            # Salvar traffic shaping
            file.write(f"{traffic_shaping_result}\n\n")

            # Salvar dispositivos conectados
            file.write("Dispositivos Conectados à Rede\n")
            for device in devices:
                file.write(f"IP: {device['ip']}, MAC: {device['mac']}\n")

        print(f"Resultados salvos em {filename}")
    except Exception as e:
        print(f"Erro ao salvar os resultados: {e}")


if __name__ == "__main__":
    print("Iniciando testes...")

    # Obter a velocidade contratada
    contracted_speed = get_contracted_speed()

    # Realiza os testes de velocidade
    download, upload = test_speed(iterations=5)

    # Verifica se há traffic shaping
    traffic_shaping_result = detect_traffic_shaping(download, contracted_speed)

    # Obtém dispositivos conectados à rede
    devices = get_network_devices()

    # Nome do arquivo com a data e hora atuais
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"C:/Users/fabia/Documents/Projeto rede via Python/Registros/{
        now}_resultados_teste.txt"

    # Salva os resultados em um arquivo de texto
    save_results_to_file(filename, download, upload,
                         devices, traffic_shaping_result)

    print("\nTestes finalizados.")
