# 📁 Renomeador de Músicas para Pendrive

Este script automatiza a organização de arquivos `.mp3` em um pendrive, renomeando todas as músicas com numeração sequencial no formato `001 - Nome da Música.mp3`, `002 - Outra Música.mp3`, etc.

---

## 🛠️ Funcionalidades

- Remove numeração antiga dos nomes dos arquivos (ex: `01 - Música.mp3`, `01.Música.mp3`).
- Renomeia os arquivos com uma nova numeração sequencial de 3 dígitos.
- Mantém a ordem alfabética das músicas.
- Organiza de forma padronizada para facilitar a navegação em dispositivos de som, carros, etc.

---

## 📌 Pré-requisitos

- Python 3 instalado.
- Músicas no formato `.mp3` salvas na raiz do pendrive.
- Biblioteca padrão do Python (não é necessário instalar pacotes externos).

---

## 🚀 Como usar

1. **Copie o script** para seu computador.
2. **Edite o caminho da variável `CAMINHO`** no script:

   ```python
   CAMINHO = r"D:\SeuPendrive"  # <-- Altere para a letra do seu pendrive
   ```

   > Exemplo: se seu pendrive está em `E:\`, use `r"E:\\"`.

3. **Execute o script** com Python:

   ```bash
   python renomeador_musicas.py
   ```

4. O script irá renomear os arquivos e exibir no terminal algo como:

   ```
   Renomeado: música antiga.mp3 → 001 - música antiga.mp3
   ```

---

## 📂 Exemplo de antes e depois

**Antes:**
```
01 - Louvor.mp3
02. Forró.mp3
03 samba.mp3
```

**Depois:**
```
001 - Louvor.mp3
002 - Forró.mp3
003 - samba.mp3
```

---

## ⚠️ Atenção

- O script modifica permanentemente os nomes dos arquivos. Faça um backup se necessário.
- Certifique-se de que todos os arquivos estão na raiz do pendrive (não funciona em subpastas).
- Arquivos com nomes repetidos após remoção da numeração podem causar erros.

---

## 📄 Licença

Este projeto é livre para uso pessoal ou profissional. Sem garantia. Use por sua conta e risco.
