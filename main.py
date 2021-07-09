import re
import requests

link = input("Insira o link: ")

if re.match(r'[a-z:/]+.wikipedia.org\/wiki\/([\w%]+)', link):
    html_page = requests.get(link)
    print("LINK VALIDO")

    print("a) Listar os topicos do indice do artigo")
    print("b) Listar todos os nomes de arquivos de imagens presentes no artigo")
    print("c) Listar todos os links para outros artigos da wikipedia que sao citados no conteudo do artigo\n")
    info = input("Qual informacao deseja-se extrair da pagina? ")

    if info == 'a':
        firstHeading = re.findall(r'class="firstHeading" >([^<]+)</', html_page.text)
        indice = re.findall(r'id="mw-toc-heading">([^<]+)</', html_page.text)
        menu = re.findall(r'id="mw-navigation">\n\s+<h2>([^<]+)</', html_page.text)
        data = re.findall(r'class="mw-headline"[^>]+>([^<]+)</', html_page.text)

        print(firstHeading[0])
        print(indice[0])
        print(menu[0])
        for line in data:
            print(line)


    #elif: info == b:

    #elif: info == c:



else:
    print("ERROR: LINK INVALIDO")