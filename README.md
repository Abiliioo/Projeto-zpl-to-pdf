# ZPL to PDF Converter

Este projeto é um conversor de arquivos ZPL (Zebra Programming Language) para PDF. Ele utiliza a API Labelary para converter arquivos ZPL em PDFs e combina múltiplos arquivos PDF em um único arquivo PDF.

## Funcionalidades

- **Conversão de ZPL para PDF**: Converte arquivos ZPL em PDFs utilizando a API Labelary.
- **Combinação de PDFs**: Junta múltiplos arquivos PDF em um único arquivo PDF.
- **Interface Gráfica**: Permite selecionar arquivos ZPL através de uma caixa de diálogo.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `requests`
  - `PyPDF2`
  - `tkinter` (geralmente incluído com Python)

- Você pode instalar as bibliotecas necessárias usando `pip`:

  ```bash
  pip install requests PyPDF2
  ```
## Uso

Execute o script Python. Uma caixa de diálogo será exibida para selecionar arquivos ZPL.
O script converterá cada arquivo ZPL selecionado em um arquivo PDF.
Após a conversão, todos os PDFs gerados serão combinados em um único arquivo PDF chamado labels.pdf no mesmo diretório onde o primeiro PDF foi salvo.
Os arquivos PDF individuais serão removidos após a combinação (opcional).

## Exemplo de Execução

  ```bash
  python zpl_to_pdf_converter.py
```
## Contato

Se você tiver alguma dúvida, entre em contato com seu-emai joseiltonjass@hotmail.com
