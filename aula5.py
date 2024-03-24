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

frame1 = ctk.CTkFrame(janela, width=200, height=330, fg_color="teal", bg_color="transparent", border_width=2, corner_radius=30).place(x=30, y=30)
frame2 = ctk.CTkFrame(janela, width=200, height=330, fg_color="teal", bg_color="transparent", border_width=2, corner_radius=30).place(x=250, y=30)
frame3 = ctk.CTkFrame(janela, width=200, height=330, fg_color="teal", bg_color="transparent", border_width=2, corner_radius=30).place(x=470, y=30)




janela.mainloop() #Este método, mantém a janela aberta


"""
acessar mercado livre
preencher pesquisa com a info passada pelo usuário
realizar pesquisa com mais de uma página de resultados
salvar os resultados em csv e em excel

"""