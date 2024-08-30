import requests
from io import BytesIO
from PyPDF2 import PdfMerger
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

def zpl_to_pdf(zpl_content, zpl_file_path):
    """
    Converte o conteúdo ZPL para um arquivo PDF usando a API Labelary.

    Args:
        zpl_content (str): O conteúdo ZPL a ser convertido.
        zpl_file_path (str): Caminho para o arquivo ZPL original (para nomear o PDF gerado).

    Returns:
        str: Caminho para o arquivo PDF gerado ou None em caso de erro.
    """
    url = 'http://api.labelary.com/v1/printers/8dpmm/labels/4x6/0/'
    headers = {'Accept': 'application/pdf'}
    
    # Enviar o conteúdo ZPL para a API e obter a resposta em PDF
    files = {'file': ('test.zpl', BytesIO(zpl_content.encode('utf-8')))}
    response = requests.post(url, headers=headers, files=files, stream=True)
    
    # Verificar o tipo de conteúdo da resposta
    content_type = response.headers.get('Content-Type', '')
    if 'application/pdf' not in content_type:
        print(f"Erro: Tipo de conteúdo inesperado: {content_type}")
        print(f"Conteúdo da resposta (primeiros 1000 bytes): {response.content[:1000]}")
        return None

    if response.status_code == 200:
        pdf_file_path = os.path.splitext(zpl_file_path)[0] + '.pdf'
        with open(pdf_file_path, 'wb') as f:
            f.write(response.content)
        print(f"{pdf_file_path} criado com sucesso.")
        return pdf_file_path
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return None

def combine_pdfs(pdf_files, output_file):
    """
    Combina múltiplos arquivos PDF em um único arquivo PDF.

    Args:
        pdf_files (list of str): Lista de caminhos para arquivos PDF a serem combinados.
        output_file (str): Caminho para o arquivo PDF combinado a ser criado.
    """
    merger = PdfMerger()
    for pdf in pdf_files:
        try:
            merger.append(pdf)
        except Exception as e:
            print(f"Erro ao combinar {pdf}: {e}")
            continue  # Pule para o próximo PDF em caso de erro
    if merger.pages:
        merger.write(output_file)
        print(f"Arquivo unificado {output_file} criado com sucesso.")
    else:
        print("Nenhum PDF válido para combinar.")
    merger.close()

def select_files():
    """
    Abre uma caixa de diálogo para selecionar arquivos ZPL.

    Returns:
        list of str: Lista de caminhos para os arquivos ZPL selecionados.
    """
    Tk().withdraw()  # Oculta a janela principal do Tkinter
    file_paths = askopenfilenames(filetypes=[("ZPL files", "*.zpl")])
    return file_paths

# Selecionar arquivos ZPL via caixa de diálogo
zpl_files = select_files()
pdf_files = []

for zpl_file in zpl_files:
    with open(zpl_file, 'r') as f:
        zpl_content = f.read()
    pdf_file = zpl_to_pdf(zpl_content, zpl_file)
    if pdf_file:
        pdf_files.append(pdf_file)

if pdf_files:
    # Definir o caminho do arquivo unificado no mesmo diretório onde o primeiro PDF foi salvo
    first_pdf_dir = os.path.dirname(pdf_files[0])
    combined_pdf_path = os.path.join(first_pdf_dir, 'unified_labels.pdf')
    combine_pdfs(pdf_files, combined_pdf_path)
    
    # Opcional: Remover os PDFs individuais após a união
    for pdf in pdf_files:
        os.remove(pdf)
    print("Arquivos individuais removidos.")
else:
    print("Nenhum PDF para combinar.")
