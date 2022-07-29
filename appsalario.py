from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

from pyparsing import col

# Cores
branco = "#fcfcfc"
branco_claro = "#f2f2f2"
preto = "#030303"
preto_cinza = "#1f1d1d"
azul = "#04007d"
amarelo = "#edfa00"
laranja = "#fa9200"
vermelho = "#8c0601"
verde = "#0f8c01"


janela = Tk()
janela.title("Calculadora de Salário")
janela.config(bg=preto)
janela.geometry("700x350")
janela.resizable(width=FALSE, height=FALSE)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Frames

frame_cima = Frame(janela, width=690, height=150, bg=preto_cinza)
frame_cima.grid(row=0, column=0, pady=5, padx=5)

frame_baixo = Frame(janela, width=690, height=185, bg=preto_cinza)
frame_baixo.grid(row=1, column=0, pady=1, padx=5)


def calcular():
    # Variáveis básicas
    nome = str(entry_nome.get())
    profissão = str(entry_prof.get())
    horas_dia = float(entry_horas.get())
    dias_mes = float(entry_dias.get())
    salario_base = float(entry_salario.get())

    # Horas no mes
    horas_mes = dias_mes*horas_dia

    # Valor da hora
    valor_hora = salario_base/horas_mes

    # Valor dia
    valor_dia = salario_base/dias_mes

    # Valor semana
    semana = dias_mes/4
    valor_sem = valor_dia*semana

    # Valor mes é o salário base

    # Valor anual
    valor_ano = salario_base*12

    # Valor da hora extra
    extra = 1.5
    valor_hora_extra = valor_hora*extra

    # Exibindo resultados
    mostrador_nome = Label(frame_baixo, text=f"Nome: {nome}",
                           font="Raleway 10 bold", bg=preto_cinza, fg=branco)
    mostrador_nome.place(x=30, y=60)

    mostrador_prof = Label(frame_baixo, text=f"Profissão: {profissão}",
                           font="Raleway 10 bold", bg=preto_cinza, fg=branco)
    mostrador_prof.place(x=30, y=80)

    mostrador_salariobase = Label(frame_baixo, text=f"Salário base: R${salario_base}",
                                  font="Raleway 10 bold", bg=preto_cinza, fg=branco)
    mostrador_salariobase.place(x=30, y=100)

    mostrador_semhora = Label(frame_baixo, text=f"Trabalhando {horas_dia} horas, {dias_mes} dias por mês",
                              font="Raleway 10 bold", bg=preto_cinza, fg=branco)
    mostrador_semhora.place(x=30, y=120)

    mostrador_salhora = Label(frame_baixo, text=f"Salário por hora: R${valor_hora}",
                              font="Raleway 10 bold", bg=preto_cinza, fg=branco)
    mostrador_salhora.place(x=380, y=40)

    mostrador_salhora = Label(frame_baixo, text=f"Valor da sua hora extra: R${valor_hora_extra}",
                              font="Raleway 10 bold", bg=preto_cinza, fg=branco)
    mostrador_salhora.place(x=380, y=60)

    mostrador_saldia = Label(frame_baixo, text=f"Salário por dia: R${valor_dia}",
                             font="Raleway 10 bold", bg=preto_cinza, fg=branco)
    mostrador_saldia.place(x=380, y=80)

    mostrador_salsem = Label(frame_baixo, text=f"Salário por semana: R${valor_sem}",
                             font="Raleway 10 bold", bg=preto_cinza, fg=branco)
    mostrador_salsem.place(x=380, y=100)

    mostrador_salmes = Label(frame_baixo, text=f"Salário por mês: R${salario_base}",
                             font="Raleway 10 bold", bg=preto_cinza, fg=branco)
    mostrador_salmes.place(x=380, y=120)

    mostrador_salano = Label(frame_baixo, text=f"Salário por ano: R${valor_ano}",
                             font="Raleway 10 bold", bg=preto_cinza, fg=branco)
    mostrador_salano.place(x=380, y=140)


# Entry
img = Image.open('icon.png')
img = img.resize((50, 50), Image.LANCZOS)
img = ImageTk.PhotoImage(img)

icon = Label(frame_cima, image=img, bg=preto_cinza)
icon.place(x=5, y=5)

label_title = Label(frame_cima, text="Calculadora de Salário",
                    font="Raleway 17 bold", bg=preto_cinza, fg=branco)
label_title.place(x=70, y=15)

# Nome
label_nome = Label(frame_cima, text="Nome:",
                   font="Raleway 10 bold", bg=preto_cinza, fg=branco)
label_nome.place(x=10, y=80)

entry_nome = Entry(frame_cima, width=22,
                   font="Raleway 10 ", bg=branco, fg=preto)
entry_nome.place(x=60, y=81)

# Profissão
label_prof = Label(frame_cima, text="Profissão:",
                   font="Raleway 10 bold", bg=preto_cinza, fg=branco)
label_prof.place(x=10, y=110)

entry_prof = Entry(frame_cima, width=20,
                   font="Raleway 10 ", bg=branco, fg=preto)
entry_prof.place(x=75, y=111)

# Horas diárias
label_horas = Label(frame_cima, text="Quantas horas por dia trabalha? ",
                    font="Raleway 10 bold", bg=preto_cinza, fg=branco)
label_horas.place(x=250, y=65)

entry_horas = Entry(frame_cima, width=5,
                    font="Raleway 10 ", bg=branco, fg=preto)
entry_horas.place(x=450, y=66)

# Dias por mês
label_dias = Label(frame_cima, text="Quantas dias por mes trabalha? ",
                   font="Raleway 10 bold", bg=preto_cinza, fg=branco)
label_dias.place(x=250, y=95)

entry_dias = Entry(frame_cima, width=5,
                   font="Raleway 10 ", bg=branco, fg=preto)
entry_dias.place(x=450, y=96)

# Salário mensal
label_dias = Label(frame_cima, text="Qual o seu salário mensal base? ",
                   font="Raleway 10 bold", bg=preto_cinza, fg=branco)
label_dias.place(x=250, y=125)

entry_salario = Entry(frame_cima, width=5,
                      font="Raleway 10 ", bg=branco, fg=preto)
entry_salario.place(x=450, y=126)

# Imagem lateral e botão
icon = Label(frame_cima, image=img, bg=preto_cinza)
icon.place(x=565, y=30)

botao = Button(frame_cima, command=calcular, text="Calcular", font="Raleway 12 bold", width=10,
               height=1, relief=FLAT, overrelief=RAISED, bg=laranja, fg=preto)
botao.place(x=540, y=100)

# Frame baixo

label_resultado = Label(frame_baixo, text="Resultados:",
                        font="Raleway 17 bold", bg=preto_cinza, fg=branco)
label_resultado.place(x=30, y=15)

janela.mainloop()
