import re
import os
import requests

#-------------------------------------------------------------------------
def modA(request): #Modulo de listar tópicos
    data = re.findall(r'"toctext">(.*?)<', request.text)
    n = 0
    for topic in data:
        print(topic)
        n = n + 1
    print(n, " tópicos encontrados neste artigo.")

def modB(request): #Módulo para listar imagens
    data = re.findall(r'Ficheiro:(.*)" class="image"', request.text)
    n = 0
    for image in data:
            print(image)
            n = n + 1
    print(n, " imagens encontrados neste artigo.")

def modC(request): #Módulo para listar links
    texto = re.findall(r'<p>(.*)(\n)</p>', request.text)
    n = 0
    for p in texto:
        data = re.findall(r'/wiki/([^"]+)"', str(p))
        for link in data:
            print("https://pt.wikipedia.org/wiki/"+link)
            n = n + 1
    print(n, " links encontrados neste artigo.")

def menu():
    print("********** Web Scrapper **********\n")
    print("Você pode obter as seguintes informações a partir de qualquer artigo da Wikipédia em português:\n")
    print("A - Listar os topicos do indice do artigo")
    print("B - Listar todos os nomes de arquivos de imagens presentes no artigo")
    print("C - Listar todos os links para outros artigos da wikipedia que sao citados no conteudo do artigo")
    print("X - Sair do programa.\n")

#-------------------------------------------------------------------------
os.system("cls")
menu()
link = input("Insira o link de algum artigo para começar: ")

while(link != 'X' and link != 'x'):
    if re.match(r'https:\/\/pt.wikipedia.org\/wiki\/([\w%]+)', link):
        os.system("cls")
        print("O link é válido!")
        menu()
        ch = input("Qual tipo de informacao deseja listar? ")

        if ch == 'a':
            os.system("cls")
            print("Listando tópicos: \n")
            modA(requests.get(link))
            os.system("pause")
        elif ch == 'b':
            os.system("cls")
            print("Listando imagens: \n")
            modB(requests.get(link))
            os.system("pause")
        elif ch == 'c':
            os.system("cls")
            print("Listando links: \n")
            modC(requests.get(link))
            os.system("pause")
        elif ch == 'x' or ch == 'X':
            link = ch
        else:
            print("Opção inválida, tente novamente. ")
            os.system("pause")
    else:
        link = input("Link inválido, tenthe novamente: ")
    
print("Saindo...")
