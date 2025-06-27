import os
import re

# Caminho onde estão as músicas (raiz do pendrive)
CAMINHO = r"D:\SeuPendrive"  # <-- troque para a letra do seu pendrive

# Pega todos os arquivos .mp3, ordenados por nome
arquivos = sorted([
    f for f in os.listdir(CAMINHO)
    if f.lower().endswith(".mp3") and os.path.isfile(os.path.join(CAMINHO, f))
])

for i, nome_antigo in enumerate(arquivos, start=1):
    caminho_antigo = os.path.join(CAMINHO, nome_antigo)

    # Remove numeração antiga do início (ex: 01 -, 01., etc.)
    nome_limpo = re.sub(r"^\d{1,3}\s*[-.\s]+", "", nome_antigo).strip()

    # Gera nova numeração com 3 dígitos
    nova_num = f"{i:03}"
    novo_nome = f"{nova_num} - {nome_limpo}"

    caminho_novo = os.path.join(CAMINHO, novo_nome)

    os.rename(caminho_antigo, caminho_novo)
    print(f"Renomeado: {nome_antigo} → {novo_nome}")
