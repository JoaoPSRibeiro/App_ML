"""
Criar interface gráfica
    criar label com nome dp campo
    criar input de pesquisa
    criar botão de enciar
    crião botão de limpar
    criar label explicando que o arquivo foi salvo na área de trabalho
"""
import customtkinter as ctk # Importando o gerador de interface gráfica, customtkinter

janela = ctk.CTk() #CTk, não esquecer deste detalhe. Aqui, estamos abrindo a juanela
# Configurando janela principal
janela.title("Pesquise no Mercado Livre")
janela.geometry("700x400")
janela.maxsize(width=900, height=550) #Configurando o tamanho mãximo da janela
janela.minsize(width=500, height=300)
janela.iconbitmap("logo.ico")

tabview = ctk.CTkTabview(janela, width=400, corner_radius=20, border_width=2, border_color="yellow")
tabview.pack()
tabview.add("Nomes")
tabview.add("Idades")
tabview.add("Genero")
tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(0, weight=1)
tabview.tab("Genero").grid_columnconfigure(0, weight=1)

# Adicionando elemento na Tab
textof1 = ctk.CTkLabel(tabview.tab("Nomes"), text="Faça a Sua Pesquisa: ").pack()


janela.mainloop() #Este método, mantém a janela aberta


"""
acessar mercado livre
preencher pesquisa com a info passada pelo usuário
realizar pesquisa com mais de uma página de resultados
salvar os resultados em csv e em excel

"""