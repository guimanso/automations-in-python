from PIL import Image
import os

# Caminho da pasta principal
pasta_principal = "D:/Documents/hidrometros_teste"

# Define a área de recorte
x = 50
y = 1200
largura = 2500
altura = 2800
box = (x, y, x + largura, y + altura)

# Lista das subpastas ordenadas
subpastas = sorted([
    p for p in os.listdir(pasta_principal)
    if os.path.isdir(os.path.join(pasta_principal, p)) and p.isdigit()
], key=lambda nome: int(nome))

# Extensões que vamos considerar
extensoes_validas = (".jpg", ".jpeg")

for pasta in subpastas:
    caminho_pasta = os.path.join(pasta_principal, pasta)

    arquivos = [f for f in os.listdir(caminho_pasta) if f.lower().endswith(extensoes_validas)]

    for nome_arquivo in arquivos:
        caminho_imagem = os.path.join(caminho_pasta, nome_arquivo)

        try:
            imagem = Image.open(caminho_imagem)

            imagem_cortada = imagem.crop(box)

            nome_base, extensao = os.path.splitext(nome_arquivo)
            novo_nome = f"{nome_base}_recortada{extensao}"
            caminho_novo = os.path.join(caminho_pasta, novo_nome)

            imagem_cortada.save(caminho_novo)
            print(f"{nome_arquivo} -> {novo_nome}")

        except Exception as e:
            print(f"Erro ao processar {nome_arquivo}: {e}")