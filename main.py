import re
import requests

link = input("Insira o link: ")

if re.match(r'[a-z:/]+.wikipedia.org\/wiki\/([\w%]+)', link):
    html_page = requests.get(link)
    print("LINK VALIDO")

    print("a) Listar os topicos do indice do artigo")
    print("b) Listar todos os nomes de arquivos de imagens presentes no artigo")
    print("c) Listar todos os links para outros artigos da wikipedia que sao citados no conteudo do artigo\n")
    ch = input("Qual informacao deseja-se extrair da pagina? ")

    if ch == 'a':

        data = re.findall(r'"toctext">(.*?)<', html_page.text)
        
        for topic in data:
            print(topic)

    elif ch == 'b':

        data = re.findall(r'Ficheiro:(.*?)" class="image">', html_page.text)
        aux = 0
        for image in data:
            print(image)
            aux = aux + 1

        print(aux)

    elif ch == 'c':

        texto = re.findall(r'<p>(.*)(\n)</p>', html_page.text)

        for p in texto:
            data = re.findall(r'/wiki/([^"]+)"', str(p))

            for link in data:
                print(link)

    elif ch == 'd':

        texto = re.findall(r'<p>(.*)(\n)</p>', html_page.text)
        print(len(texto))
        print(type(texto[1]))


else:
    print("ERROR: LINK INVALIDO")