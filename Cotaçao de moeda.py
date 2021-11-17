# #Programa de cotação de moeda
from tkinter import *
import requests

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    text_cotacao["text"] = texto


janela = Tk()
janela.title("Cotação atual das moedas")
janela.geometry("120x150")

text_titulo = Label(janela, text="Cotações atualizadas")
text_titulo.grid(column=0, row=0)

text_cotacao = Label(janela, text="")
text_cotacao.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text="Atualizar Cotação", command=pegar_cotacoes)
botao.grid(column=0, row=2)


janela.mainloop()