import nmap
from datetime import datetime

alvo = "192.168.56.101" # IP alvo
nm = nmap.PortScanner()

print(f"[*] varrendo {alvo}...")
nm.scan(alvo, '22,23,80,445,139', arguments='-sV -sC')

#criar HTML
html = f"""
<html><head><style>
body{{font-family:Arial;background-color:#f4f4f4;padding:20px;}}
.card{{background:#fff;padding:20px;border-radius:8px;max-width:800px;margin:auto}}
th{{background:#000;color:#fff;padding:8px}} td{{padding:8px;border-bottom:1px solid #ddd}}
</style></head><body><div class="card">
<h1>relatorio Nmap - {alvo}</h1><p>data: {datetime.now()}</p>
<table border=1 width=100%>
<tr><th>Portas</th><th>estado</th><th>serviço</th><th>versão</th></tr>
"""

if alvo not in nm.all_hosts() or 'tcp' not in nm[alvo]:
    print("[-] Nenhuma porta aberta ou host offline.")
    exit()

for porta in nm[alvo]['tcp']:
    estado = nm[alvo]['tcp'][porta]['state']
    servico = nm[alvo]['tcp'][porta]['name']
    versao = f"{nm[alvo]['tcp'][porta].get('product', 'N/A')} {nm[alvo]['tcp'][porta].get('version', 'N/A')}".strip()
    html += f"<tr><td>{porta}</td><td>{estado}</td><td>{servico}</td><td>{versao}</td></tr>"

html += "</table></body></html>"

with open("relatorio.html", "w", encoding="utf-8") as f:
    f.write(html)

print("[*] Relatório gerado com sucesso: relatorio.html")