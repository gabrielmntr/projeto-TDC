import re
import requests

link = input("Insira o link: ")

if re.match(r'[a-z:/]+.wikipedia.org\/wiki\/([\w%]+)', link):  #valida o link dando match com a RegEx
    html_page = requests.get(link) #html_page recebe um objeto do tipo 'requests'
    print("LINK VALIDO")

    print("a) Listar os topicos do indice do artigo")
    print("b) Listar todos os nomes de arquivos de imagens presentes no artigo")
    print("c) Listar todos os links para outros artigos da wikipedia que sao citados no conteudo do artigo\n")
    info = input("Qual informacao deseja-se extrair da pagina? ")

    if info == 'a':

        data = re.findall(r'<h[^>]+>(.*)</h[^>]+>', html_page.text)
        #data recebe uma lista com todos os matchs dessa RegEx
        #que no caso eh tudo entre as tags h1, h2, h3 e nao soh o nome do topico
        #uso outra regEx mais abaixo pra separar apenas o topico do id, class, etc

        aux = 0
        print('\n')
        for line in data:
            #os 3 primeiros topicos de todos os links que testei fogem do padrao da segunda regEx
            #por isso estou printando essas 3 primeiras com aux enquanto n criamos uma regEx melhor

            if aux == 0:
                print(line)
            elif aux == 1:
                print(line)
            elif aux == 2:
                print(line)
            else:
                #aqui armazeno na lista apenas o nome do topico e printo em seguida
                list_of_topics = re.findall(r'id="[^"]+">([^<]+)<', line)
                for topic in list_of_topics:
                    print(topic)

            aux += 1

    #elif: info == b:

    #elif: info == c:



else:
    print("ERROR: LINK INVALIDO")



