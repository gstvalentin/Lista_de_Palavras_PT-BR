from unidecode import unidecode

dicionario = open('br-utf8.txt', 'r', encoding='utf-8').readlines()[0:10] #!! BASTANTE CUIDADO AO IMPORTAR TODAS AS PALAVRAS
#! SÃO MAIS DE 250K DE ITENS QUE VOCÊ IRÁ COLOCAR EM SUA LISTA
#! PARA IMPORTAR TODAS, APAGUE A SEGUINTE PARTE DO CÓDIGO "[0:10]"
lista_palavras = []
for d in dicionario:
    words = unidecode(d.replace('\n', '')) #? Sem acentos e ç
    #words = d.replace('\n', '')  #? Com acentos e ç
    lista_palavras.append(words)

"""
? Palavras importadas da lista da USP Brasil em 12/04/2022 no site "https://www.ime.usp.br/~pf/dicios/index.html"
? Para atualiza-la, importe um novo arquivo "br-utf8.txt" e substitua o existente nesse diretorio.
"""