from PIL import Image
import os

# Caminho relativo da pasta principal
pasta_principal = "D:/Documents/hidrometros_teste"

# Lista das subpastas do diretório
subpastas = [ p for p in os.listdir(pasta_principal) if os.path.isdir(os.path.join(pasta_principal, p))]

# Mostra as subpastas listadas
# for diretorios in subpastas: print(diretorios)

tipos_vistas = ["vista_dinamica", "vista_frente", "vista_cima", "vista_relojoaria"]

for diretorios in subpastas:
    caminho_pastas = os.path.join(pasta_principal, diretorios)

    imagens = [f for f in os.listdir(caminho_pastas) if f.lower().endswith((".jpeg",".jpg"))]

    imagens_ordenadas = sorted(imagens, key=lambda f: os.path.getmtime(os.path.join(caminho_pastas, f)))

    print(f"\nPasta {diretorios}: ({len(imagens_ordenadas)} imagens)")
    # for img in imagens_ordenadas:
    #     print(f"- {img}")

    for i, imagem in enumerate(imagens_ordenadas):
        if i >= len(tipos_vistas):
            print(f"Mais de 4 imagens, ignorando extra: {imagem}")
            continue

        # Formata o número da pasta com 3 dígitos
        numero_pasta = diretorios.zfill(3)

        # Pega extensão original do arquivo (.jpg ou .jpeg)
        extensao = os.path.splitext(imagem)[1].lower()

        novo_nome = f"hidrometro_{numero_pasta}_{tipos_vistas[i]}{extensao}"

        caminho_antigo = os.path.join(caminho_pastas, imagem)
        caminho_novo = os.path.join(caminho_pastas, novo_nome)

        os.rename(caminho_antigo, caminho_novo)
        print(f" {imagem} -> {novo_nome}")

    # teste
    # os.rename(caminho_antigo, caminho_novo)
    # print(f"- {imagem} → {novo_nome}")