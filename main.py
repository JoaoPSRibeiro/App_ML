"""
Criar interface gráfica
    criar label com nome do campo
    criar input de pesquisa
    criar botão de enviar
    crião botão de limpar
    criar label explicando que o arquivo foi salvo na área de trabalho
"""
import customtkinter as ctk # Importando o gerador de interface gráfica, customtkinter
import requests
from bs4 import BeautifulSoup
import pandas as pd

janela = ctk.CTk() #CTk, não esquecer deste detalhe. Aqui, estamos abrindo a juanela
# Configurando janela principal
janela.title("Pesquise no Mercado Livre")
janela.geometry("700x400")
janela.maxsize(width=900, height=550) #Configurando o tamanho mãximo da janela
janela.minsize(width=500, height=300)
janela.iconbitmap("logo.ico")

tabview = ctk.CTkTabview(janela, width=400, corner_radius=20, border_width=2, border_color="yellow")
tabview.pack()
tabview.add("Pesquisa")
# tabview.add("Idades")
# tabview.add("Genero")
tabview.tab("Pesquisa").grid_columnconfigure(0, weight=1)
# tabview.tab("Idades").grid_columnconfigure(0, weight=1)
# tabview.tab("Genero").grid_columnconfigure(0, weight=1)

# Adicionando elemento na Tab
textof1 = ctk.CTkLabel(tabview.tab("Pesquisa"), text="Faça a Sua Pesquisa: ").pack()
boxf1 = ctk.CTkTextbox(tabview.tab("Pesquisa"), width = 300, height=20 ).pack()
btn_clear = ctk.CTkButton(tabview.tab("Pesquisa"), width = 100, height = 30, text="Limpar").pack_configure(side='left')
btn_search = ctk.CTkButton(tabview.tab("Pesquisa"), width = 100, height= 30, text="Pesquisar", command="produto_nome").pack_configure(side="right")

info = ctk.CTkLabel(janela, text="O arquivo será salvo na Área de Trabalho.").pack()



lista_produtos = []
url_base = 'https://lista.mercadolivre.com.br/'
produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome) # concatenamos a url base com o input que o usuário quer pesquisar.

site = BeautifulSoup(response.text, 'html.parser')
produtos = site.findAll('div', attrs={'class':'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

for produto in produtos:
    print()
    titulo = produto.find('h2', attrs={'class':'ui-search-item__title'})
    #print(produto.prettify())
    print('Titulo do produto:  ', titulo.text)
    link_produto = produto.find('a', attrs={'class':'ui-search-link'})
    print('Link do Produto', link_produto['href'])
    
    preco_inteiro = produto.find('span', attrs={'class':'andes-money-amount__fraction'})
    preco_tipo_moeda = produto.find('span', attrs={'class' : 'andes-money-amount__currency-symbol'})
    preco_centavos = produto.find('span', attrs={'class':'andes-money-amount__cents'})
    if (preco_centavos):
        print('Preço do Produto: ', preco_tipo_moeda.text, preco_inteiro.text,',',  preco_centavos.text)
        lista_produtos.append([titulo.text, preco_tipo_moeda.text, preco_inteiro.text + ',' + preco_centavos.text])
    else:
        print('Preço do Produto: ', preco_tipo_moeda.text, preco_inteiro.text)
        lista_produtos.append([titulo.text, preco_tipo_moeda.text,preco_inteiro.text ])
        print('\n\n')

catalogo = pd.DataFrame(lista_produtos, columns=['Título Produto', 'Tipo Moeda', 'Valor Inteiro'])
catalogo.to_csv("C:/Users/User/Desktop/produtos.csv", index=False)
catalogo.to_excel('C:/Users/User/Desktop/produtos.xlsx', index=False)


janela.mainloop() #Este método, mantém a janela aberta


"""
acessar mercado livre
preencher pesquisa com a info passada pelo usuário
realizar pesquisa com mais de uma página de resultados
salvar os resultados em csv e em excel

"""