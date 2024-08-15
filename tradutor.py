import customtkinter as ct
from deep_translator import GoogleTranslator #pip install deep_translator

#Funções---------------------

def traduzir():
    texto_para_traduzir= texto.get()
    idioma=lang_to_var.get()
    saida= GoogleTranslator(source='auto',target=idioma).translate(texto_para_traduzir)
    texto_traduzido.delete(0,'end')
    texto_traduzido.insert(0,saida)

#-----------------------------
ct.set_appearance_mode('dark')


janela = ct.CTk()
janela.geometry('600x500')
janela.title('Tradutor Universal V1.0') 

titulo = ct.CTkLabel(janela,text='Tradutor Universal V1.0', font = ('Arial',25,'bold'),text_color='#7a1879')
titulo.pack(padx=10,pady=10)

titulo2 = ct.CTkLabel(janela,text='Texto para traduzir ☻', font = ('Arial',18,'bold'))
titulo2.pack(padx=10,pady=10)


texto = ct.CTkEntry(janela,placeholder_text='Digite aqui', width=400, height=50)
texto.pack(padx=5,pady=5)

titulo3 = ct.CTkLabel(janela,text='Selecione a linguagem', font = ('Arial',15,'bold'))
titulo3.pack(padx=10,pady=10)

lang_to_var=ct.StringVar(value='english')
lang_list= GoogleTranslator().get_supported_languages()
lang_to = ct.CTkOptionMenu(janela, values=lang_list, variable=lang_to_var,fg_color='#7a1879')
lang_to.set('english')
lang_to.pack(padx=5,pady=5)

titulo4 = ct.CTkLabel(janela,text='Texto traduzido', font = ('Arial',18,'bold'))
titulo4.pack(padx=10,pady=10)

texto_traduzido = ct.CTkEntry(janela,placeholder_text='O texto traduzido aparecerá aqui', width=400, height=100)
texto_traduzido.pack(padx=5,pady=5)


botao1 = ct.CTkButton(janela,text='Traduzir',fg_color='#7a1879',text_color='white', hover_color='#9b3899',width=150,height=40,font = ('Arial',15,'bold'), command=traduzir)
botao1.pack(padx=10,pady=10)



janela.mainloop()