cat > README.md << 'EOF'
# Projeto Análise de Vulnerabilidades

Projeto educacional de Segurança Ofensiva para varredura de portas e auditoria de serviços em ambiente controlado.

### 🎯 Objetivo
Simular uma auditoria de segurança em rede local, identificando portas abertas, serviços e versões na máquina alvo Metasploitable 2, gerando um relatório para análise posterior de vetores de ataque.

### 🛠️ Tecnologias
- Python 3
- Nmap + python-nmap
- Kali Linux
- VirtualBox (Rede Host-Only)
- Metasploitable 2
- Hydra (próxima etapa)

### ⚙️ Funcionalidades
- Varredura de 1000 portas TCP mais comuns
- Identificação de serviço e versão (banner grabbing)
- Geração automática de relatório em HTML
- Base para testes de brute-force em FTP/SSH/Telnet

### 🚀 Como Executar
```bash
# instalar dependencia
pip install python-nmap

# rodar o scan
python3 scanports.py

# abrir relatório
firefox relatorio.html
