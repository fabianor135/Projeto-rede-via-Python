
![image](https://github.com/user-attachments/assets/017b9994-aa60-407e-bbf3-d26be676cc3f)

# Teste de Internet e Monitoramento de Rede

Este projeto é um script Python que realiza testes abrangentes de desempenho de conexão com a Internet e monitoramento de rede local. Ele foi projetado para diagnosticar possíveis problemas, identificar dispositivos conectados e verificar indícios de práticas como **traffic shaping** por parte de provedores de Internet.

---

## ✨ Funcionalidades

- **Teste de Velocidade**: Mede a velocidade média de download e upload com base em múltiplas iterações.
- **Teste de Latência**: Calcula a latência média para diferentes servidores globais.
- **Comparação de Tráfego HTTP e HTTPS**: Identifica possíveis práticas de traffic shaping analisando as velocidades de tráfego entre HTTP e HTTPS.
- **Monitoramento de Banda Local**: Verifica o consumo total de dados enviados e recebidos pelo dispositivo durante um intervalo de tempo.
- **Detecção de Dispositivos na Rede**: Identifica dispositivos conectados na rede local, exibindo seus endereços IP e MAC.

---

## 🛠️ Tecnologias Utilizadas

Este script utiliza as seguintes bibliotecas Python:

- `speedtest-cli`: Para medir a velocidade de download e upload.
- `requests`: Para realizar testes de latência e tráfego HTTP/HTTPS.
- `psutil`: Para monitorar o uso de banda local.
- `scapy`: Para detectar dispositivos conectados à rede via ARP.

---

## 🚀 Como Executar

### Pré-requisitos
Certifique-se de ter instalado:
- **Python 3.8 ou superior**
- Pip (gerenciador de pacotes do Python)


📊 Saída Esperada
O script fornece uma saída detalhada com:

Velocidade média de download e upload (em Mbps).
Latência média para servidores pré-definidos.
Velocidades médias de tráfego HTTP e HTTPS.
Lista de dispositivos conectados à rede local (IP e MAC Address).
Dados enviados e recebidos no intervalo monitorado.

🛡️ Avisos
O script foi desenvolvido para uso educacional e diagnóstico de redes pessoais. Evite utilizar em redes corporativas sem autorização.
Para a função de detecção de dispositivos, pode ser necessário executar o script com permissões administrativas.
🧑‍💻 Contribuindo
Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

Faça um fork do repositório.
Crie uma branch para suas alterações:
bash
Copiar código
git checkout -b minha-feature
Commit suas alterações:
bash
Copiar código
git commit -m "Adicionei uma nova funcionalidade"
Faça um push para a branch:
bash
Copiar código
git push origin minha-feature
Abra um Pull Request no GitHub.
📞 Contato
Caso tenha dúvidas ou sugestões, entre em contato:

E-mail: fabianor135@gmail.com
LinkedIn: [Fabiano](https://www.linkedin.com/in/fabiano-rodrigues-leite-820855179/)
GitHub: fabianor135

📝 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.






