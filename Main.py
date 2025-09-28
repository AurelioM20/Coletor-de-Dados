import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

def coletar_filmes_bilheteria():
    url = "https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria"
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/116.0.0.0 Safari/537.36")
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Lança erro se status != 200

    # Parse com BeautifulSoup para garantir captura da tabela
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontrar todas as tabelas na página
    tables = soup.find_all("table", {"class": "wikitable"})

    if not tables:
        print("Nenhuma tabela encontrada na página.")
        return

    # A primeira tabela wikitable é a principal com a lista de filmes
    table_html = str(tables[0])

    # Use pandas para extrair a tabela HTML
    df = pd.read_html(StringIO(table_html))[0]

    # Exporta para CSV com codificação utf-8-sig para compatibilidade
    df.to_csv("filmes_maior_bilheteria.csv", index=False, encoding="utf-8-sig")
    print("Arquivo filmes_maior_bilheteria.csv criado com sucesso.")

if __name__ == "__main__":
    coletar_filmes_bilheteria()
