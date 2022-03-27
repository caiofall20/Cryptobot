# chat_id = 760369667
import telebot
from datetime import datetime
from classes import CoinGeckoAPI, TelegramBot
from time import sleep
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
import requests
import telegram

# mostra informações sobre o bot
# print(bot.get_me())

# atualizacoes = bot.get_updates()

# bot.send_message(text='Olá, aqui é o crypitinho!', chat_id=760369667)


api = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')
bot = TelegramBot(token='5158865778:AAFd2ddYXrxCyEMyNOC1oZYJgcQ2G3_MlIw', chat_id=760369667)




while True:

    if api.ping():
        preco, atualizado_em = api.consulta_preco(id_moeda='ethereum')
        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        mensagem = None

        if preco < 15000:
            mensagem = f'*Cotação do Ethereum*: \n\t*Preço*: R$ {preco}' \
                       f'\n\t*Horário*: {data_hora}\n\t*Motivo*: Valor menor que o mínimo'
        elif preco > 15000:
            mensagem = f'*Cotação do Ethereum*: \n\t*Preço*: R$ {preco}' \
                       f'\n\t*Horário*: {data_hora}\n\t*Motivo*: Valor maior que o máximo'

        if mensagem:
            bot.envia_mensagem(texto_markdown=mensagem)

    else:
        bot.send_message(text=f'API Offline, tente novamente mais tarde!', chat_id=760369667)

    sleep(30)
