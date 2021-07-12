import re
import requests

def modA(request):
    data = re.findall(r'"toctext">(.*?)<', request.text)
    n = 0
    for topic in data:
        print(topic)
        n = n + 1
    print(n, " tópicos encontrados neste artigo.")

def modB(request):
    data = re.findall(r'Ficheiro:(.*?)" class="image">', request.text)
    n = 0
    for image in data:
            print(image)
            n = n + 1
    print(n, " imagens encontrados neste artigo.")

def modC(request):
    texto = re.findall(r'<p>(.*)(\n)</p>', request.text)

    for p in texto:
        data = re.findall(r'/wiki/([^"]+)"', str(p))
        for link in data:
            print("https://pt.wikipedia.org/wiki/"+link)

link = input("Insira o link: ")

if re.match(r'[a-z:/]+.wikipedia.org\/wiki\/([\w%]+)', link):
    print("LINK VALIDO")

    print("a) Listar os topicos do indice do artigo")
    print("b) Listar todos os nomes de arquivos de imagens presentes no artigo")
    print("c) Listar todos os links para outros artigos da wikipedia que sao citados no conteudo do artigo\n")
    ch = input("Qual informacao deseja-se extrair da pagina? ")

    if ch == 'a':
        modA(requests.get(link))
    elif ch == 'b':
        modB(requests.get(link))
    elif ch == 'c':
        modC(requests.get(link))


else:
    print("ERROR: LINK INVALIDO")
