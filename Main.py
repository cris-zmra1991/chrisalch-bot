#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Eduardo Peluffo"

import json
import logging as log
import random
import re
import datetime
from random import randrange, choice
from time import sleep
from uuid import uuid4


from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update, \
	InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import (InlineQueryHandler, Updater, CommandHandler, \
	CallbackQueryHandler, MessageHandler, Filters, CallbackContext)
from telegram.utils.helpers import mention_html, escape_markdown


import traceback
import sys
import os
import configparser
import asyncio
import random


from multiprocessing import Process

from telethon import TelegramClient, events, types, functions, Button
from telethon.sessions import StringSession



# Configuracion para logeo de datos en Heroku
log.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=log.INFO)
logger = log.getLogger(__name__)

# 1 - Cargo variables de entorno
API_ID = os.environ.get('api_id', None)
API_HASH = os.environ.get('api_hash', None)
STRING_SESSION = os.environ.get('STRING_SESSION', None)
BOT_TOKEN = os.environ.get('bot_token', None)

# 2 - Si no estan las obtengo del config, esto lo uso para probar local
if API_ID is None or API_HASH is None:
	config = configparser.ConfigParser()
	config.read('init.ini')
	if config.has_section('ENVIROMENT'):
		API_ID = int(config['ENVIROMENT']['TG_API_ID'])
		API_HASH = config['ENVIROMENT']['TG_API_HASH']
		STRING_SESSION = config['ENVIROMENT']['STRING_SESSION']
		BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']


#------------------------------ CLIENTE 2 -------------------------------

API_ID2 = os.environ.get('api_id2', None)
API_HASH2 = os.environ.get('api_hash2', None)
STRING_SESSION2 = os.environ.get('STRING_SESSION2', None)


if API_ID2 is None or API_HASH2 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID2 = int(config['ENVIROMENT']['TG_API_ID2'])
  API_HASH2 = config['ENVIROMENT']['TG_API_HASH2']
  STRING_SESSION2 = config['ENVIROMENT']['STRING_SESSION2']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']


#------------------------------ CLIENTE 3 -------------------------------

API_ID3 = os.environ.get('api_id3', None)
API_HASH3 = os.environ.get('api_hash3', None)
STRING_SESSION3 = os.environ.get('STRING_SESSION3', None)


if API_ID3 is None or API_HASH3 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID3 = int(config['ENVIROMENT']['TG_API_ID3'])
  API_HASH3 = config['ENVIROMENT']['TG_API_HASH3']
  STRING_SESSION3 = config['ENVIROMENT']['STRING_SESSION3']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']


#------------------------------ CLIENTE 4 -------------------------------

API_ID4 = os.environ.get('api_id4', None)
API_HASH4 = os.environ.get('api_hash4', None)
STRING_SESSION4 = os.environ.get('STRING_SESSION4', None)


if API_ID4 is None or API_HASH4 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID4 = int(config['ENVIROMENT']['TG_API_ID4'])
  API_HASH4 = config['ENVIROMENT']['TG_API_HASH4']
  STRING_SESSION4 = config['ENVIROMENT']['STRING_SESSION4']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 5 -------------------------------

API_ID5 = os.environ.get('api_id5', None)
API_HASH5 = os.environ.get('api_hash5', None)
STRING_SESSION5 = os.environ.get('STRING_SESSION5', None)


if API_ID5 is None or API_HASH5 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID5 = int(config['ENVIROMENT']['TG_API_ID5'])
  API_HASH5 = config['ENVIROMENT']['TG_API_HASH5']
  STRING_SESSION5 = config['ENVIROMENT']['STRING_SESSION5']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 6 -------------------------------

API_ID6 = os.environ.get('api_id6', None)
API_HASH6 = os.environ.get('api_hash6', None)
STRING_SESSION6 = os.environ.get('STRING_SESSION6', None)


if API_ID6 is None or API_HASH6 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID6 = int(config['ENVIROMENT']['TG_API_ID5'])
  API_HASH6 = config['ENVIROMENT']['TG_API_HASH5']
  STRING_SESSION6 = config['ENVIROMENT']['STRING_SESSION5']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 7 -------------------------------

API_ID7 = os.environ.get('api_id7', None)
API_HASH7 = os.environ.get('api_hash7', None)
STRING_SESSION7 = os.environ.get('STRING_SESSION7', None)


if API_ID7 is None or API_HASH7 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID7 = int(config['ENVIROMENT']['TG_API_ID7'])
  API_HASH7 = config['ENVIROMENT']['TG_API_HASH7']
  STRING_SESSION7 = config['ENVIROMENT']['STRING_SESSION7']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 8 -------------------------------

API_ID8 = os.environ.get('api_id8', None)
API_HASH8 = os.environ.get('api_hash8', None)
STRING_SESSION8 = os.environ.get('STRING_SESSION8', None)


if API_ID8 is None or API_HASH8 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID8 = int(config['ENVIROMENT']['TG_API_ID8'])
  API_HASH8 = config['ENVIROMENT']['TG_API_HASH8']
  STRING_SESSION8 = config['ENVIROMENT']['STRING_SESSION8']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 9 -------------------------------

API_ID9 = os.environ.get('api_id9', None)
API_HASH9 = os.environ.get('api_hash9', None)
STRING_SESSION9 = os.environ.get('STRING_SESSION9', None)


if API_ID9 is None or API_HASH9 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID9 = int(config['ENVIROMENT']['TG_API_ID9'])
  API_HASH9 = config['ENVIROMENT']['TG_API_HASH9']
  STRING_SESSION9 = config['ENVIROMENT']['STRING_SESSION9']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 10 -------------------------------

API_ID10 = os.environ.get('api_id10', None)
API_HASH10 = os.environ.get('api_hash10', None)
STRING_SESSION10 = os.environ.get('STRING_SESSION10', None)


if API_ID10 is None or API_HASH10 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID10 = int(config['ENVIROMENT']['TG_API_ID10'])
  API_HASH10 = config['ENVIROMENT']['TG_API_HASH10']
  STRING_SESSION10 = config['ENVIROMENT']['STRING_SESSION10']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 11 -------------------------------

API_ID11 = os.environ.get('api_id11', None)
API_HASH11 = os.environ.get('api_hash11', None)
STRING_SESSION11 = os.environ.get('STRING_SESSION11', None)


if API_ID11 is None or API_HASH11 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID11 = int(config['ENVIROMENT']['TG_API_ID11'])
  API_HASH11 = config['ENVIROMENT']['TG_API_HASH11']
  STRING_SESSION11 = config['ENVIROMENT']['STRING_SESSION11']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 12 -------------------------------

API_ID12 = os.environ.get('api_id12', None)
API_HASH12 = os.environ.get('api_hash12', None)
STRING_SESSION12 = os.environ.get('STRING_SESSION12', None)


if API_ID12 is None or API_HASH12 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID12 = int(config['ENVIROMENT']['TG_API_ID12'])
  API_HASH12 = config['ENVIROMENT']['TG_API_HASH12']
  STRING_SESSION12 = config['ENVIROMENT']['STRING_SESSION12']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 13 -------------------------------

API_ID13 = os.environ.get('api_id13', None)
API_HASH13 = os.environ.get('api_hash13', None)
STRING_SESSION13 = os.environ.get('STRING_SESSION13', None)


if API_ID13 is None or API_HASH13 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID13 = int(config['ENVIROMENT']['TG_API_ID13'])
  API_HASH13 = config['ENVIROMENT']['TG_API_HASH13']
  STRING_SESSION13 = config['ENVIROMENT']['STRING_SESSION13']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 14 -------------------------------

API_ID14 = os.environ.get('api_id14', None)
API_HASH14 = os.environ.get('api_hash14', None)
STRING_SESSION14 = os.environ.get('STRING_SESSION14', None)


if API_ID14 is None or API_HASH14 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID14 = int(config['ENVIROMENT']['TG_API_ID14'])
  API_HASH14 = config['ENVIROMENT']['TG_API_HASH14']
  STRING_SESSION14 = config['ENVIROMENT']['STRING_SESSION14']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']


#------------------------------ CLIENTE 15 -------------------------------

API_ID15 = os.environ.get('api_id15', None)
API_HASH15 = os.environ.get('api_hash15', None)
STRING_SESSION15 = os.environ.get('STRING_SESSION15', None)


if API_ID15 is None or API_HASH15 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID15 = int(config['ENVIROMENT']['TG_API_ID15'])
  API_HASH15 = config['ENVIROMENT']['TG_API_HASH15']
  STRING_SESSION15 = config['ENVIROMENT']['STRING_SESSION15']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']


API_ID16 = os.environ.get('api_id16', None)
API_HASH16 = os.environ.get('api_hash16', None)
STRING_SESSION16 = os.environ.get('STRING_SESSION16', None)


if API_ID16 is None or API_HASH16 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID16 = int(config['ENVIROMENT']['TG_API_ID16'])
  API_HASH16 = config['ENVIROMENT']['TG_API_HASH16']
  STRING_SESSION16 = config['ENVIROMENT']['STRING_SESSION16']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 17 -------------------------------

API_ID17 = os.environ.get('api_id17', None)
API_HASH17 = os.environ.get('api_hash17', None)
STRING_SESSION17 = os.environ.get('STRING_SESSION17', None)


if API_ID17 is None or API_HASH17 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID17 = int(config['ENVIROMENT']['TG_API_ID17'])
  API_HASH17 = config['ENVIROMENT']['TG_API_HASH17']
  STRING_SESSION17 = config['ENVIROMENT']['STRING_SESSION17']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 18 -------------------------------

API_ID18 = os.environ.get('api_id18', None)
API_HASH18 = os.environ.get('api_hash18', None)
STRING_SESSION18 = os.environ.get('STRING_SESSION18', None)


if API_ID18 is None or API_HASH18 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID18 = int(config['ENVIROMENT']['TG_API_ID18'])
  API_HASH18 = config['ENVIROMENT']['TG_API_HASH18']
  STRING_SESSION18 = config['ENVIROMENT']['STRING_SESSION18']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 19 -------------------------------

API_ID19 = os.environ.get('api_id19', None)
API_HASH19 = os.environ.get('api_hash19', None)
STRING_SESSION19 = os.environ.get('STRING_SESSION19', None)


if API_ID19 is None or API_HASH19 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID19 = int(config['ENVIROMENT']['TG_API_ID19'])
  API_HASH19 = config['ENVIROMENT']['TG_API_HASH19']
  STRING_SESSION19 = config['ENVIROMENT']['STRING_SESSION19']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']



#------------------------------ CLIENTE 20 -------------------------------

API_ID20 = os.environ.get('api_id20', None)
API_HASH20 = os.environ.get('api_hash20', None)
STRING_SESSION20 = os.environ.get('STRING_SESSION20', None)


if API_ID20 is None or API_HASH20 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID20 = int(config['ENVIROMENT']['TG_API_ID20'])
  API_HASH20 = config['ENVIROMENT']['TG_API_HASH20']
  STRING_SESSION20 = config['ENVIROMENT']['STRING_SESSION20']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']

#------------------------------ CLIENTE 21 -------------------------------

API_ID21 = os.environ.get('api_id21', None)
API_HASH21 = os.environ.get('api_hash21', None)
STRING_SESSION21 = os.environ.get('STRING_SESSION21', None)


if API_ID21 is None or API_HASH21 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID21 = int(config['ENVIROMENT']['TG_API_ID21'])
  API_HASH21 = config['ENVIROMENT']['TG_API_HASH21']
  STRING_SESSION21 = config['ENVIROMENT']['STRING_SESSION21']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']


#------------------------------ CLIENTE 22 -------------------------------

API_ID22 = os.environ.get('api_id22', None)
API_HASH22 = os.environ.get('api_hash22', None)
STRING_SESSION22 = os.environ.get('STRING_SESSION22', None)


if API_ID22 is None or API_HASH22 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID22 = int(config['ENVIROMENT']['TG_API_ID22'])
  API_HASH22 = config['ENVIROMENT']['TG_API_HASH22']
  STRING_SESSION22 = config['ENVIROMENT']['STRING_SESSION22']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']


#------------------------------ CLIENTE 23 -------------------------------

API_ID23 = os.environ.get('api_id23', None)
API_HASH23 = os.environ.get('api_hash23', None)
STRING_SESSION23 = os.environ.get('STRING_SESSION23', None)


if API_ID23 is None or API_HASH23 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID23 = int(config['ENVIROMENT']['TG_API_ID23'])
  API_HASH23 = config['ENVIROMENT']['TG_API_HASH23']
  STRING_SESSION23 = config['ENVIROMENT']['STRING_SESSION23']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']


#------------------------------ CLIENTE 24 -------------------------------

API_ID24 = os.environ.get('api_id24', None)
API_HASH24 = os.environ.get('api_hash24', None)
STRING_SESSION24 = os.environ.get('STRING_SESSION24', None)


if API_ID24 is None or API_HASH24 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID24 = int(config['ENVIROMENT']['TG_API_ID24'])
  API_HASH24 = config['ENVIROMENT']['TG_API_HASH24']
  STRING_SESSION24 = config['ENVIROMENT']['STRING_SESSION24']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']


#------------------------------ CLIENTE 25 -------------------------------

API_ID25 = os.environ.get('api_id25', None)
API_HASH25 = os.environ.get('api_hash25', None)
STRING_SESSION25 = os.environ.get('STRING_SESSION25', None)


if API_ID25 is None or API_HASH25 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID25 = int(config['ENVIROMENT']['TG_API_ID25'])
  API_HASH25 = config['ENVIROMENT']['TG_API_HASH25']
  STRING_SESSION25 = config['ENVIROMENT']['STRING_SESSION25']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']


#------------------------------ CLIENTE 26 -------------------------------

API_ID26 = os.environ.get('api_id26', None)
API_HASH26 = os.environ.get('api_hash26', None)
STRING_SESSION26 = os.environ.get('STRING_SESSION26', None)


if API_ID26 is None or API_HASH26 is None:
 config = configparser.ConfigParser()
 config.read('init.ini')
 if config.has_section('ENVIROMENT'):
  API_ID26 = int(config['ENVIROMENT']['TG_API_ID26'])
  API_HASH26 = config['ENVIROMENT']['TG_API_HASH26']
  STRING_SESSION26 = config['ENVIROMENT']['STRING_SESSION26']
  BOT_TOKEN = config['ENVIROMENT']['BOT_TOKEN']



  


#--------------------------------- BOT --------------------------------------

def command_start(update: Update, context: CallbackContext):
	bot = context.bot
	cid = update.message.chat_id
	bot.send_message(cid, "Bot para aprender")

def bot_main():
	updater = Updater(BOT_TOKEN, use_context=True)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", command_start))
	updater.start_polling(timeout=30)	
	updater.idle()

#-------------------------------FIN BOT ------------------------------------

#------------------------------ USER BOT -----------------------------------
# Esto hace que escuche en "Mensajes guardados" y solo mensajes mios (outgoing)
@events.register(events.NewMessage(chats='me', outgoing=True))
async def me_handler(event):
	# Logeo en Heroku que mensaje entro.
	logger.info(f"New message {event.raw_text}")
	# Que cuenta de telegram recibio el mensaje? La obtengo.
	client = event.client
	# El mensaje decia "Hola"?
	if event.raw_text == 'Hola':
		# Entonces respondo Cmo estas?
		await client.send_message('me', 'Su cuenta ha sido hackeada🙂')
	# El mensaje decia "Todo bien"?
	if event.raw_text == 'Todo bien':
		# Entonces respondo Me alegro?
		await client.send_message('me', 'Me alegro')
	# El mensaje decia "christian"?
	if event.raw_text == 'christian':
		# Entonces respondo Me alegro?
		await client.send_message('me', 'este es el bot de christian y no el de ale')


@events.register(events.NewMessage(chats=-1001394317550))
async def bs_open_shop_handler(event):
	logger.info(f"New message {event.raw_text}")
	client = event.client
	if event.raw_text == '/myshop_open':
		await client.send_message('chtwrsbot', '/myshop_open')
	if event.raw_text == '/myshop_close': 
		await client.send_message('chtwrsbot', '/myshop_close')


@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def foray_handler(event):
	client = event.client
	if "You were strolling around on your horse when you noticed" in event.raw_text:
		x = random.randint(5,55)
		await asyncio.sleep(x)
		async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
			await message.click(0)
			await client.send_message('me', 'Finalizo evento de foray en Chat Wars')
	if "you shall /pledge to protect. You have 3 minutes to decide." in event.raw_text:
		x = random.randint(5,20)
		await asyncio.sleep(x)
		async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
			await client.send_message('chtwrsbot', '/pledge')


@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def chatwars_handler(event):
 client = event.client
 if "Stamina restored. You are ready for more adventures!" in event.raw_text:
  await client.send_message( 'chtwrsbot' , '🗺Quests' )
  await asyncio.sleep(3)
  async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
   await message.click(0)


@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def chatwars_swamp_quests_handler(event):
 client = event.client
 if "Stamina restored. You are ready for more adventures!" in event.raw_text:
  await client.send_message( 'chtwrsbot' , '🗺Quests' )
  await asyncio.sleep(3)
  async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
   await message.click(1)

@events.register(events.NewMessage(incoming=True))
async def alts_quest_arenas_handler(event):
	logger.info(f"New message {event.raw_text}")
	client = event.client
	if event.raw_text == '🛡Defend':
		await client.send_message('chtwrsbot', '🛡Defend')
	if event.raw_text == '▶️Fast fight':
                x = random.randint(30,120)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '▶️Fast fight')
	if event.raw_text == '/c_22':
                x = random.randint(5,20)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '/c_22')
	if event.raw_text == '/buy':
		await client.send_message('deer_daily_inn_bot', '/buy_01_50_1')


	
@events.register(events.NewMessage(incoming=True))
async def quests_handler(event):
	client = event.client
	if event.raw_text == '/forest':
                x = random.randint(5,90)
                await asyncio.sleep(x)
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(0)
	if event.raw_text == '/swamp':
                x = random.randint(5,90)
                await asyncio.sleep(x)
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(1)
	if event.raw_text == '/valley':
                x = random.randint(5,90)
                await asyncio.sleep(x)
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(2)
	if event.raw_text == '/quest':
                x = random.randint(5,90)
                await asyncio.sleep(x)
                await client.send_message( 'chtwrsbot' , '🗺Quests' )



@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def mobs_handler(event):
	client = event.client
	if "You are preparing for a fight" in event.raw_text:
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	x = random.randint(5,20)
                	await asyncio.sleep(x)
                	await client.forward_messages('deepbluesharkbot', event.message)
	if "You met some hostile creatures. Be careful:" in event.raw_text:
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	x = random.randint(55,90)
                	await asyncio.sleep(x)
                	await client.forward_messages('deepbluesharkbot', event.message)


@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def mobs_melody_handler(event):
	client = event.client
	if "You are preparing for a fight" in event.raw_text:
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	x = random.randint(5,20)
                	await asyncio.sleep(x)
                	await client.forward_messages('deepbluesharkbot', event.message)
	if "You met some hostile creatures. Be careful:" in event.raw_text:
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	x = random.randint(35,60)
                	await asyncio.sleep(x)
                	await client.forward_messages('deepbluesharkbot', event.message)


@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def mobs_send_cheo_handler(event):
	client = event.client
	if "You met some hostile creatures. Be careful:" in event.raw_text:
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await client.forward_messages('Cheo_EL_Cojo', event.message)


@events.register(events.NewMessage(chats=-559598676))
async def check_accounts_handler(event):
	client = event.client
	if event.raw_text == '/state':
                await client.send_message('chtwrsbot', '🏅Me')
                x = random.randint(5,15)
                await asyncio.sleep(x)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-559598676)
	if event.raw_text == '/hilo':
                await client.send_message('chtwrsbot', '/t_01')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-559598676)
	if event.raw_text == '⚖Exchange':
                await client.send_message('chtwrsbot', '⚖Exchange')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-559598676)
	if event.raw_text == '/stock':
                await client.send_message('chtwrsbot', '/stock')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-559598676)
	if event.raw_text == '/level_up':
                await client.send_message('chtwrsbot', '/level_up')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-559598676)
	if event.raw_text == '/misc':
                await client.send_message('chtwrsbot', '/misc')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-559598676)
	if event.raw_text == '/arena':
                await client.send_message('chtwrsbot', '🗺Quests')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.click(4)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                        await message.forward_to(-559598676)
	if event.raw_text == '/crafting':
                await client.send_message('chtwrsbot', '⚒Crafting')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-559598676)
	if event.raw_text == '🏷Equipment':
                await client.send_message('chtwrsbot', '🏷Equipment')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-559598676)
	if event.raw_text == '/reportes':
                await client.send_message('chtwrsbot', '/report')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-559598676)
	if "You met some hostile creatures. Be careful:" in event.raw_text:
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	x = random.randint(5,7)
                	await asyncio.sleep(x)
                	await client.forward_messages(-559598676, event.message)

@events.register(events.NewMessage(chats=-796720529))
async def check_accounts_valley_handler(event):
	client = event.client
	if event.raw_text == '/state':
                await client.send_message('chtwrsbot', '🏅Me')
                x = random.randint(5,15)
                await asyncio.sleep(x)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-796720529)
	if event.raw_text == '/hilo':
                await client.send_message('chtwrsbot', '/t_01')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-796720529)
	if event.raw_text == '⚖Exchange':
                await client.send_message('chtwrsbot', '⚖Exchange')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-796720529)
	if event.raw_text == '/stock':
                await client.send_message('chtwrsbot', '/stock')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-796720529)
	if event.raw_text == '/level_up':
                await client.send_message('chtwrsbot', '/level_up')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-796720529)
	if event.raw_text == '/effects':
                await client.send_message('chtwrsbot', '/effects')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-796720529)
	if event.raw_text == '/arena':
                await client.send_message('chtwrsbot', '🗺Quests')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.click(4)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                        await message.forward_to(-796720529)
	if event.raw_text == '/crafting':
                await client.send_message('chtwrsbot', '⚒Crafting')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-796720529)
	if event.raw_text == '🏷Equipment':
                await client.send_message('chtwrsbot', '🏷Equipment')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-796720529)
	if event.raw_text == '/reportes':
                await client.send_message('chtwrsbot', '/report')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-796720529)
	if "You met some hostile creatures. Be careful:" in event.raw_text:
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	x = random.randint(5,7)
                	await asyncio.sleep(x)
                	await client.forward_messages(-796720529, event.message)

@events.register(events.NewMessage(chats=-704711135))
async def check_accounts_swamp_handler(event):
	client = event.client
	if event.raw_text == '/state':
                await client.send_message('chtwrsbot', '🏅Me')
                x = random.randint(5,15)
                await asyncio.sleep(x)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-704711135)
	if event.raw_text == '/hilo':
                await client.send_message('chtwrsbot', '/t_01')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-704711135)
	if event.raw_text == '⚖Exchange':
                await client.send_message('chtwrsbot', '⚖Exchange')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-704711135)
	if event.raw_text == '/stock':
                await client.send_message('chtwrsbot', '/stock')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-704711135)
	if event.raw_text == '/level_up':
                await client.send_message('chtwrsbot', '/level_up')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-704711135)
	if event.raw_text == '/effects':
                await client.send_message('chtwrsbot', '/effects')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-704711135)
	if event.raw_text == '/arena':
                await client.send_message('chtwrsbot', '🗺Quests')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.click(4)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                        await message.forward_to(-704711135)
	if event.raw_text == '/crafting':
                await client.send_message('chtwrsbot', '⚒Crafting')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-704711135)
	if event.raw_text == '🏷Equipment':
                await client.send_message('chtwrsbot', '🏷Equipment')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-704711135)
	if event.raw_text == '/reportes':
                await client.send_message('chtwrsbot', '/report')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-704711135)
	if "You met some hostile creatures. Be careful:" in event.raw_text:
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	x = random.randint(5,7)
                	await asyncio.sleep(x)
                	await client.forward_messages(-704711135, event.message)



@events.register(events.NewMessage(chats=-559598676))
async def defensa_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(33):   await client.send_message(-559598676, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '/quests_forest':
       	for i in range(60):   await client.send_message(-559598676, '/forest', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_swamp':
       	for i in range(60):   await client.send_message(-559598676, '/swamp', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_valley':
       	for i in range(60):   await client.send_message(-559598676, '/valley', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/fast_fight':
       	for i in range(42):   await client.send_message(-559598676, '▶️Fast fight', schedule=datetime.timedelta(hours= (4 * i)))




@events.register(events.NewMessage(chats=-426564761))
async def reports_handler(event):
	client = event.client
	if event.raw_text == '/reportes':
	 for i in range(100):   await client.send_message(-426564761, '/report', schedule=datetime.timedelta(hours= (8 * i)))


@events.register(events.NewMessage(chats=-426564761))
async def reportes_handler(event):
	client = event.client
	if event.raw_text == '/report':
                x = random.randint(5,30)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '/report')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to('sharkteethbot')


@events.register(events.NewMessage(chats=-559598676))
async def deer_daily_handler(event):
       	if event.raw_text == '/thread':
                	 for i in range(100):   await client.send_message('deer_daily_inn_bot', '/buy_01_50_1', schedule=datetime.timedelta(hours= (1 * i)))


@events.register(events.NewMessage(chats='ale_guetta', incoming = True))
async def spend_and_hide_handler(event):
	client = event.client
	async for message in client.iter_messages('ale_guetta', limit=1, from_user='ale_guetta'):
                await client.send_message('chtwrsbot', message)
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to('ale_guetta')

@events.register(events.NewMessage(chats='wcollins', incoming = True))
async def spend_hide_handler(event):
	client = event.client
	async for message in client.iter_messages('wcollins', limit=1, from_user='wcollins'):
                await client.send_message('chtwrsbot', message)
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to('wcollins')



@events.register(events.NewMessage(chats='nixth', incoming = True))
async def spend_handler(event):
	client = event.client
	async for message in client.iter_messages('nixth', limit=1, from_user='nixth'):
                await client.send_message('chtwrsbot', message)
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to('nixth')


@events.register(events.NewMessage(chats='licuevas', incoming = True))
async def squire_script_handler(event):
	client = event.client
	if "/g_withdraw" in event.raw_text:
	               async for message in client.iter_messages('licuevas', limit=1, from_user='licuevas'):
	               	await client.send_message('chtwrsbot', message)
	               	await asyncio.sleep(3)
	               	async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
	               		await message.forward_to('licuevas')

@events.register(events.NewMessage(chats=1080748770, incoming = True))
async def squire_script_ale_handler(event):
	client = event.client
	if "/g_withdraw" in event.raw_text:
	               async for message in client.iter_messages(1080748770, limit=1, from_user='Shinozaki_Rika'):
	               	await client.send_message('chtwrsbot', message)
	               	await asyncio.sleep(3)
	               	async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
	               		await message.forward_to(1080748770)



@events.register(events.NewMessage(chats=-578125555))
async def quests_ale_handler(event):
	client = event.client
	if event.raw_text == '/forest':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(0)
	if event.raw_text == '/swamp':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(1)
	if event.raw_text == '/valley':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(2)




@events.register(events.NewMessage(chats=-578125555))
async def check_all_handler(event):
	client = event.client
	if event.raw_text == '/state':
                await client.send_message('chtwrsbot', '🏅Me')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-578125555)
	if event.raw_text == '/stock':
                await client.send_message('chtwrsbot', '/stock')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-578125555)
	if event.raw_text == '/effects':
                await client.send_message('chtwrsbot', '/effects')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-578125555)
	if event.raw_text == '/inv':
                await client.send_message('chtwrsbot', '/inv')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-578125555)
	if event.raw_text == '/crafting':
                await client.send_message('chtwrsbot', '⚒Crafting')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-578125555)
	if event.raw_text == '🏷Equipment':
                await client.send_message('chtwrsbot', '🏷Equipment')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-578125555)




@events.register(events.NewMessage(chats=-524505819))
async def check_ale_handler(event):
	client = event.client
	if event.raw_text == '/state':
                await client.send_message('chtwrsbot', '🏅Me')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-524505819)
	if event.raw_text == '/stock':
                await client.send_message('chtwrsbot', '/stock')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-524505819)
	if event.raw_text == '/effects':
                await client.send_message('chtwrsbot', '/effects')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-524505819)
	if event.raw_text == '/inv':
                await client.send_message('chtwrsbot', '/inv')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-524505819)
	if event.raw_text == '🏷Equipment':
                await client.send_message('chtwrsbot', '🏷Equipment')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-524505819)



@events.register(events.NewMessage(chats=-524505819))
async def ale_script_handler(event):
	client = event.client
	if event.raw_text == '/forest':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(0)
	if event.raw_text == '/swamp':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(1)
	if event.raw_text == '/valley':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(2)
	if event.raw_text == '/arena':
                await client.send_message( 'chtwrsbot' , '▶️Fast fight' )

@events.register(events.NewMessage(chats=-541003381))
async def collins_script_handler(event):
	client = event.client
	if event.raw_text == '/forest':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(0)
	if event.raw_text == '/swamp':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(1)
	if event.raw_text == '/valley':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(2)
	if event.raw_text == '/arena':
                await client.send_message( 'chtwrsbot' , '▶️Fast fight' )



@events.register(events.NewMessage(chats=-500850534))
async def check_melody_handler(event):
	client = event.client
	if event.raw_text == '/state':
                await client.send_message('chtwrsbot', '🏅Me')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-500850534)
	if event.raw_text == '/stock':
                await client.send_message('chtwrsbot', '/stock')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-500850534)
	if event.raw_text == '/effects':
                await client.send_message('chtwrsbot', '/effects')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-500850534)
	if event.raw_text == '/inv':
                await client.send_message('chtwrsbot', '/inv')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-500850534)
	if event.raw_text == '/arena':
                await client.send_message( 'chtwrsbot' , '▶️Fast fight' )
	if event.raw_text == '/crafting':
                await client.send_message('chtwrsbot', '⚒Crafting')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-500850534)
	if event.raw_text == '🏷Equipment':
                await client.send_message('chtwrsbot', '🏷Equipment')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-500850534)


@events.register(events.NewMessage(chats=-500850534))
async def quests_melody_handler(event):
	client = event.client
	if event.raw_text == '/forest':
                   x = random.randint(3,30)
                   await asyncio.sleep(x)
                   await client.send_message( 'chtwrsbot' , '🗺Quests' )
                   await asyncio.sleep(3)
                   async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                   	await message.click(0)
	if event.raw_text == '/swamp':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(1)
	if event.raw_text == '/valley':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(2)


@events.register(events.NewMessage(chats=-587224893))
async def programar_otaku_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(50):   await client.send_message(-587224893, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '/quests_swamp':
       	for i in range(50):   await client.send_message(-587224893, '/swamp', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/fast_fight':
       	for i in range(50):   await client.send_message(-587224893, '▶️Fast fight', schedule=datetime.timedelta(hours= (4 * i)))
       if event.raw_text == '/quests_forest':
       	for i in range(100):   await client.send_message(-587224893, '/forest', schedule=datetime.timedelta(hours= (1 * i)))




@events.register(events.NewMessage(chats=-587224893))
async def check_state_handler(event):
	client = event.client
	if event.raw_text == '/state':
                await client.send_message('chtwrsbot', '🏅Me')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-587224893)
	if event.raw_text == '/stock': 
                await client.send_message('chtwrsbot', '/stock')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-587224893)
	if event.raw_text == '/effects':
                await client.send_message('chtwrsbot', '/effects')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-587224893)
	if event.raw_text == '/inv':
                await client.send_message('chtwrsbot', '/inv')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-587224893)
	if event.raw_text == '/crafting':
                await client.send_message('chtwrsbot', '⚒Crafting')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-587224893)
	if event.raw_text == '🏷Equipment':
                await client.send_message('chtwrsbot', '🏷Equipment')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-587224893)
	if event.raw_text == '/level_up':
                await client.send_message('chtwrsbot', '/level_up')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-587224893)
	if event.raw_text == '/reportes':
                await client.send_message('chtwrsbot', '/report')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-587224893)




@events.register(events.NewMessage(chats=-587224893))
async def altarena_ok_handler(event):
	logger.info(f"New message {event.raw_text}")
	client = event.client
	if event.raw_text == '🛡Defend':
		await client.send_message('chtwrsbot', '🛡Defend')
	if event.raw_text == '▶️Fast fight':
                x = random.randint(30,120)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '▶️Fast fight')
	if event.raw_text == '/c_22':
                x = random.randint(5,20)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '/c_22')
	if event.raw_text == '/buy':
		await client.send_message('deer_daily_inn_bot', '/buy_01_50_1')


@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def bichos_alts_handler(event):
	client = event.client
	if "You met some hostile creatures. Be careful:" in event.raw_text:
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-720518254)


@events.register(events.NewMessage(chats=819060841, incoming = True))
async def bichos_palli_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if "You met some hostile creatures" in event.raw_text:
           async for message in client.iter_messages(819060841, limit=1, from_user=819060841):
           	await message.forward_to('chtwrsbot')
           	await asyncio.sleep(5)
           	async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
           		await message.forward_to(819060841, message)

@events.register(events.NewMessage(chats=947364623, incoming = True))
async def bichos_dianik_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if "You met some hostile creatures" in event.raw_text:
           async for message in client.iter_messages(947364623, limit=1, from_user=947364623):
           	await message.forward_to('chtwrsbot')
           	await asyncio.sleep(5)
           	async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
           		await message.forward_to(947364623, message)



@events.register(events.NewMessage(chats=1950523507, incoming = True))
async def bichos_damian_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if "You met some hostile creatures" in event.raw_text:
           async for message in client.iter_messages(1950523507, limit=1, from_user=1950523507):
           	await message.forward_to('chtwrsbot')
           	await asyncio.sleep(5)
           	async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
           		await message.forward_to(1950523507, message)
       if "It's an ambush" in event.raw_text:
           	await message.forward_to('chtwrsbot')
           	await asyncio.sleep(3)
           	async for message in client.iter_message('chtwrsbot', limit=1, from_user='chtwrsbot'):
           		await self._client.forward_messages('user', message)

@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def antorchas_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if "You were looking at the bright sparks emitted from the flame of your torch when you tripped on a root and lost your footing. And your torch." in event.raw_text:
                x = random.randint(3,10)
                await asyncio.sleep(x)
                await client.send_message( 'chtwrsbot' , '/on_tch' )

@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def gp_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if "Being a naturally born pathfinder" in event.raw_text:
                x = random.randint(15,45)
                await asyncio.sleep(x)
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(2)

@events.register(events.NewMessage(chats='ale_guetta', incoming = True))
async def spend_and_hide_handler(event):
	client = event.client
	async for message in client.iter_messages('ale_guetta', limit=1, from_user='ale_guetta'):
                await client.send_message('chtwrsbot', message)
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to('ale_guetta')


@events.register(events.NewMessage(chats=-590422423))
async def altarena_handler(event):
	logger.info(f"New message {event.raw_text}")
	client = event.client
	if event.raw_text == '🛡Defend':
		await client.send_message('chtwrsbot', '🛡Defend')
	if event.raw_text == '▶️Fast fight':
                x = random.randint(30,120)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '▶️Fast fight')
	if event.raw_text == '/c_22':
                x = random.randint(5,20)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '/c_22')
	if event.raw_text == '/buy':
		await client.send_message('deer_daily_inn_bot', '/buy_01_50_1')




@events.register(events.NewMessage(chats=-590422423))
async def orders_alts_pollitos_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(50):   await client.send_message(-590422423, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '/quests_forest':
       	for i in range(120):   await client.send_message(-590422423, '/forest', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_swamp':
       	for i in range(48):   await client.send_message(-590422423, '/swamp', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_valley':
       	for i in range(48):   await client.send_message(-590422423, '/valley', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/fast_fight':
       	for i in range(42):   await client.send_message(-590422423, '▶️Fast fight', schedule=datetime.timedelta(hours= (4 * i)))


@events.register(events.NewMessage(chats=-590422423))
async def check_acc_handler(event):
	client = event.client
	if event.raw_text == '/state':
                await client.send_message('chtwrsbot', '🏅Me')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-590422423)
	if event.raw_text == '/stock': 
                await client.send_message('chtwrsbot', '/stock')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-590422423)
	if event.raw_text == '/effects':
                await client.send_message('chtwrsbot', '/effects')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-590422423)
	if event.raw_text == '/inv':
                await client.send_message('chtwrsbot', '/inv')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-590422423)
	if event.raw_text == '/crafting':
                await client.send_message('chtwrsbot', '⚒Crafting')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-590422423)
	if event.raw_text == '🏷Equipment':
                await client.send_message('chtwrsbot', '🏷Equipment')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-590422423)


@events.register(events.NewMessage(chats=-590422423))
async def quests_pollos_handler(event):
	client = event.client
	if event.raw_text == '/forest':
                print ("me fui")
                x = random.randint(30,180)
                await asyncio.sleep(x)
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.click(0)
	if event.raw_text == '/swamp':
                x = random.randint(30,180)
                await asyncio.sleep(x)
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(1)
	if event.raw_text == '/valley':
                x = random.randint(30,180)
                await asyncio.sleep(x)
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(2)



@events.register(events.NewMessage(incoming=True))
async def orders_handler(event):
	client = event.client
	if event.raw_text == '/atk':
                await client.send_message('chtwrsbot', '⚔Attack')
	if event.raw_text == '/moon':
                await client.send_message('chtwrsbot', '🌑')
	if event.raw_text == '/wolf':
                await client.send_message('chtwrsbot', '🐺')
	if event.raw_text == '/ptt':
                await client.send_message('chtwrsbot', '🥔')
	if event.raw_text == '/deer':
                await client.send_message('chtwrsbot', '🦌')
	if event.raw_text == '/drags':
                await client.send_message('chtwrsbot', '🐉')
	if event.raw_text == '/hn':
                await client.send_message('chtwrsbot', '🦅')
	if event.raw_text == '/sh':
                await client.send_message('chtwrsbot', '🦈')




@events.register(events.NewMessage(chats=-426564761))
async def reports_melody_handler(event):
	client = event.client
	if event.raw_text == '/report':
                x = random.randint(5,30)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '/report')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to('sharkteethbot')

doDados = False

@events.register(events.NewMessage(chats='me'))
async def dados_handler(event):
 global doDados
 if '/dados_on' in event.raw_text:
         doDados = True
         print("true") 
 if '/dados_off' in event.raw_text:
         doDados = False
         print("false" ) 


@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def dados_hacks_handler(event):
 if doDados:
                x = random.randint(5,15)
                await asyncio.sleep(x)
                client = event.client
                if "🎲You threw the dice on the table:" in event.raw_text:
                 await client.send_message( 'chtwrsbot' , '🎲Play some dice' )


@events.register(events.NewMessage(chats='me'))
async def pogs_handler(event):
 global doPogs
 if '/pogs_on' in event.raw_text:
         doPogs = True
         print("true") 
 if '/pogs_off' in event.raw_text:
         doPogs = False
         print("false" ) 



@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def pogs_hacks_handler(event):
 if doPogs:
                x = random.randint(1,2)
                await asyncio.sleep(x)
                client = event.client
                if "Crafted: Pouch of gold" in event.raw_text:
                 await client.send_message( 'chtwrsbot' , '/c_100' )


@events.register(events.NewMessage(chats=-524505819))
async def ale_afk_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(90):   await client.send_message(408101137, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '/wind':
       	for i in range(18):   await client.send_message(-500850534, '/forest', schedule=datetime.timedelta(minutes=\
                (5 * i * 1)))

@events.register(events.NewMessage(chats=-426564761))
async def palli_afk_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(90):   await client.send_message(-426564761, '/fd', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '🛡Defend':
                   x = random.randint(10,80)
                   await asyncio.sleep(x)
                   await client.send_message( 'chtwrsbot' , '🛡Defend' )


def randomnum( ) :
       numero = random.randit(385,400)
       return numero


@events.register(events.NewMessage(chats=-500850534))
async def mel_afk_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(30):   await client.send_message(408101137, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '/qc':
       	for i in range(45):   await client.send_message(408101137, '🛡Defend', schedule=timedelta(seconds=randomnum()))

trader_rss = "02"

@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def trader_handler(event):
  global trader_rss
  client = event.client
  if 'You defended villagers well.' in event.raw_text:
   trader_index = re.search(r"carry (\d+).", event.raw_text)
  trader_number = trader_index.group(1)
  sleep_time = random.randint(7,15)
  await asyncio.sleep(sleep_time)
  await client.send_message('chtwrsbot', "/sc " + trader_rss + " " + trader_number)


trader_rss = "02"

@events.register(events.NewMessage(chats=-426564761))
async def trader_rss_handler(event):
  global trader_rss
  client = event.client
  if '/more' in event.raw_text:
   trader_text = event.raw_text
   trader_index = re.search(r"/more (\d+)", trader_text)
  trader_rss = trader_index.group(1)
  await client.send_message(-426564761, "trader rss setted to " + trader_rss)


@events.register(events.NewMessage(chats='chtwrsbot'))
async def full_quest_handler(event):
 client = event.client
 global doQuest
 if "Stamina restored. You are ready for more adventures!" in event.raw_text:
         doQuest = True
         print("true") 
         await client.send_message( 'chtwrsbot' , '🗺Quests' )
 if 'Not enough stamina' in event.raw_text:
         doQuest = False
         print("false" ) 

@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def full_quest2_handler(event):
 client = event.client
 if doQuest:
                 if "Many things can happen in the forest." in event.raw_text:
                  await asyncio.sleep(3)
                  async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                   await message.click(0)
                   x = random.randint(260,290)
                   await asyncio.sleep(x)
                   await client.send_message( 'chtwrsbot' , '🗺Quests' )




@events.register(events.NewMessage(chats='me'))
async def quest_forest_handler(event):
 client = event.client
 global doQuest
 if '/quest_on' in event.raw_text:
         doQuest = True
         print("true") 
 if '/quest_off' in event.raw_text:
         doQuest = False
         print("false" ) 


@events.register(events.NewMessage(chats=-517934547))
async def gdef_palli_handler(event):
	client = event.client
	if event.raw_text == '/g_def':
                   x = random.randint(3,60)
                   await asyncio.sleep(x)
                   await client.send_message('chtwrsbot', '/g_def')

@events.register(events.NewMessage(chats=-517934547))
async def def_palli_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(30):   await client.send_message(-517934547, '/g_def', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '/wind':
       	for i in range(30):   await client.send_message(-517934547, '/forest_on', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '/full_quests':
       	for i in range(30):   await client.send_message(-517934547, '/quest', schedule=datetime.timedelta(hours= (8 * i)))


@events.register(events.NewMessage(chats=819060841, incoming = True))
async def palli_alts_quests_handler(event):
	client = event.client
	if event.raw_text == '/forest':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(0)
	if event.raw_text == '/swamp':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(1)
	if event.raw_text == '/valley':
                await client.send_message( 'chtwrsbot' , '🗺Quests' )
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                 await message.click(2)


@events.register(events.NewMessage(chats=819060841, incoming = True))
async def activar_quest_handler(event):
 client = event.client
 global doQuest
 if '/quest_on' in event.raw_text:
         doQuest = True
         print("true") 
 if '/quest_off' in event.raw_text:
         doQuest = False
         print("false" ) 
 


@events.register(events.NewMessage(chats=819060841, incoming = True))
async def palli_quests_on_handler(event):
	client = event.client
	if event.raw_text == '🗺Quests':
		await client.send_message( 'chtwrsbot' , '🗺Quests' )

@events.register(events.NewMessage(chats=-514358940))
async def altarena_moon_handler(event):
	logger.info(f"New message {event.raw_text}")
	client = event.client
	if event.raw_text == '🛡Defend':
		await client.send_message('chtwrsbot', '🛡Defend')
	if event.raw_text == '▶️Fast fight':
                x = random.randint(30,120)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '▶️Fast fight')
	if event.raw_text == '/c_22':
                x = random.randint(5,20)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '/c_22')
	if event.raw_text == '/buy':
		await client.send_message('deer_daily_inn_bot', '/buy_01_50_1')


@events.register(events.NewMessage(chats=-403697562))
async def altarena_ok_moon_handler(event):
	logger.info(f"New message {event.raw_text}")
	client = event.client
	if event.raw_text == '🛡Defend':
		await client.send_message('chtwrsbot', '🛡Defend')
	if event.raw_text == '▶️Fast fight':
                x = random.randint(30,120)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '▶️Fast fight')
	if event.raw_text == '/c_22':
                x = random.randint(5,20)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '/c_22')
	if event.raw_text == '/buy':
		await client.send_message('deer_daily_inn_bot', '/buy_01_50_1')


@events.register(events.NewMessage(chats=-550722607))
async def alts_quest_arenas_moon_handler(event):
	logger.info(f"New message {event.raw_text}")
	client = event.client
	if event.raw_text == '🛡Defend':
		await client.send_message('chtwrsbot', '🛡Defend')
	if event.raw_text == '▶️Fast fight':
                x = random.randint(30,120)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '▶️Fast fight')
	if event.raw_text == '/c_22':
                x = random.randint(5,20)
                await asyncio.sleep(x)
                await client.send_message('chtwrsbot', '/c_22')
	if event.raw_text == '/buy':
		await client.send_message('deer_daily_inn_bot', '/buy_01_50_1')


@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def bichos_alts_moon_handler(event):
	client = event.client
	if "You met some hostile creatures. Be careful:" in event.raw_text:
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-1001551881968)



@events.register(events.NewMessage(chats=-514358940))
async def check_acc_moon_handler(event):
	client = event.client
	if event.raw_text == '/state':
                await client.send_message('chtwrsbot', '🏅Me')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-514358940)
	if event.raw_text == '/stock': 
                await client.send_message('chtwrsbot', '/stock')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-514358940)
	if event.raw_text == '/reportes':
                await client.send_message('chtwrsbot', '/report')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-514358940)
	if event.raw_text == '/inv':
                await client.send_message('chtwrsbot', '/inv')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-514358940)
	if event.raw_text == '/crafting':
                await client.send_message('chtwrsbot', '⚒Crafting')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-514358940)
	if event.raw_text == '🏷Equipment':
                await client.send_message('chtwrsbot', '🏷Equipment')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-514358940)
	if event.raw_text == '/level_up':
                await client.send_message('chtwrsbot', '/level_up')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-514358940)


@events.register(events.NewMessage(chats=-550722607))
async def check_accounts_moon_handler(event):
	client = event.client
	if event.raw_text == '/state':
                await client.send_message('chtwrsbot', '🏅Me')
                x = random.randint(5,15)
                await asyncio.sleep(x)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-550722607)
	if event.raw_text == '/hilo':
                await client.send_message('chtwrsbot', '/t_01')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-550722607)
	if event.raw_text == '⚖Exchange':
                await client.send_message('chtwrsbot', '⚖Exchange')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-550722607)
	if event.raw_text == '/stock':
                await client.send_message('chtwrsbot', '/stock')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-550722607)
	if event.raw_text == '/level_up':
                await client.send_message('chtwrsbot', '/level_up')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-550722607)
	if event.raw_text == '/reportes':
                await client.send_message('chtwrsbot', '/report')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-550722607)
	if event.raw_text == '/arena':
                await client.send_message('chtwrsbot', '🗺Quests')
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.click(4)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                        await message.forward_to(-550722607)
	if event.raw_text == '/crafting':
                await client.send_message('chtwrsbot', '⚒Crafting')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-550722607)
	if event.raw_text == '🏷Equipment':
                await client.send_message('chtwrsbot', '🏷Equipment')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-550722607)
	if event.raw_text == '/misc':
                await client.send_message('chtwrsbot', '/misc')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-550722607)


@events.register(events.NewMessage(chats=-403697562))
async def check_state_moon_handler(event):
	client = event.client
	if event.raw_text == '/state':
                await client.send_message('chtwrsbot', '🏅Me')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-403697562)
	if event.raw_text == '/stock': 
                await client.send_message('chtwrsbot', '/stock')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-403697562)
	if event.raw_text == '/reportes':
                await client.send_message('chtwrsbot', '/report')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-403697562)
	if event.raw_text == '/inv':
                await client.send_message('chtwrsbot', '/inv')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-403697562)
	if event.raw_text == '/crafting':
                await client.send_message('chtwrsbot', '⚒Crafting')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-403697562)
	if event.raw_text == '🏷Equipment':
                await client.send_message('chtwrsbot', '🏷Equipment')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-403697562)
	if event.raw_text == '/level_up':
                await client.send_message('chtwrsbot', '/level_up')
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-403697562)



@events.register(events.NewMessage(chats=-514358940))
async def orders_alts_moon_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(50):   await client.send_message(-514358940, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '/quests_forest':
       	for i in range(120):   await client.send_message(-514358940, '/forest', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_swamp':
       	for i in range(48):   await client.send_message(-514358940, '/swamp', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_valley':
       	for i in range(48):   await client.send_message(-514358940, '/valley', schedule=datetime.timedelta(hours= (1 * i)))


@events.register(events.NewMessage(chats='ale_guetta', incoming = True))
async def spend_and_hide_moon_handler(event):
	client = event.client
	async for message in client.iter_messages('ale_guetta', limit=1, from_user='ale_guetta'):
                await client.send_message('chtwrsbot', message)
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to('ale_guetta')


@events.register(events.NewMessage(chats='chica_fresaa', incoming = True))
async def spend_hide_moon_handler(event):
	client = event.client
	async for message in client.iter_messages('chica_fresaa', limit=1, from_user='chica_fresaa'):
                await client.send_message('chtwrsbot', message)
                await asyncio.sleep(3)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to('chica_fresaa')


@events.register(events.NewMessage(chats=-514358940))
async def orders_alts_moon_dianik_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/fast_fight':
       	for i in range(75):   await client.send_message(-514358940, '▶️Fast fight', schedule=datetime.timedelta(hours= (4 * i)))

@events.register(events.NewMessage(chats=-403697562))
async def orders_moon_dianik_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/fast_fight':
       	for i in range(75):   await client.send_message(-403697562, '▶️Fast fight', schedule=datetime.timedelta(hours= (4 * i)))

store_messages = []

@events.register(events.NewMessage(chats=408101137))
async def handler_store_messages(event):
    global store_messages

    store_messages.append(event.id)

@events.register(events.NewMessage(chats='me', outgoing=True))
async def handler_delete_messages(event):
    global store_messages

    msg = event.message
    if "/delete" in msg.message:
        await event.client.delete_messages(408101137, store_messages)
        print(store_messages)
        store_messages.clear()

@events.register(events.NewMessage(chats=-587224893))
async def arena_collins_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/arenita':
       	for i in range(100):   await client.send_message(-587224893, '▶️Fast fight', schedule=datetime.timedelta(hours= (4 * i)))


@events.register(events.NewMessage(chats=-559598676))
async def arena_factory_collins_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/arenita':
       	for i in range(100):   await client.send_message(-559598676, '▶️Fast fight', schedule=datetime.timedelta(hours= (4 * i)))


@events.register(events.NewMessage(chats=-517934547))
async def palli_check_script_handler(event):
	client = event.client
	if event.raw_text == '/state':
                await client.send_message('chtwrsbot', '🏅Me')
                x = random.randint(5,15)
                await asyncio.sleep(x)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-517934547)
	if event.raw_text == '/crafting':
                await client.send_message('chtwrsbot', '⚒Crafting')
                x = random.randint(5,15)
                await asyncio.sleep(x)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to(-517934547)
	if event.raw_text == '/quest':
                x = random.randint(5,90)
                await asyncio.sleep(x)
                await client.send_message( 'chtwrsbot' , '🗺Quests' )

@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def recurso_trader_handler(event):
 client = event.client
 if "You were strolling around on your horse when you noticed" in event.raw_text: 
                await client.send_message(-426564761 , '/set' )

@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def recurso_trader_palli_handler(event):
 client = event.client
 if "You were strolling around on your horse when you noticed" in event.raw_text: 
                await client.send_message(-426564761 , '/trader' )



@events.register(events.NewMessage(chats=-426564761))
async def trader_melody_handler(event):
 client = event.client
 if "/set" in event.raw_text: 
                await client.send_message(-426564761 , '/more 02' )


@events.register(events.NewMessage(chats=-426564761))
async def trader_melody_palli_handler(event):
 client = event.client
 if "/trader" in event.raw_text: 
                await client.send_message(-426564761 , '/more 02' )
 if "/fd" in event.raw_text: 
                x = random.randint(1,3)
                await asyncio.sleep(x)
                await client.send_message(-426564761 , '🛡Defend' )



rss_code = ""
depositing = {
    1601020789:  False,
    1537398720:  False,
    1715211880:  False,
    1887395064:  False,
    1712246785:  False,
    1878762746:  False,
    1898612510:  False,
    1798040460:  False,
    1641405929:  False,
    1643834968:  False,
    1979283324:  False,
    1821769477:  False,
    1992613235:  False,
    1607420129:  False
}


@events.register(events.NewMessage(chats=-559598676))
async def handler_in_g_deposit(event):
    global rss_code
    global depositing
    msg = event.raw_text
    id_client = event.client._self_id
    if ("/gd" in msg) and (id_client in depositing.keys()):
        rss_code = msg.split("_")[1]
        depositing[id_client] = True
        await event.client.send_message('chtwrsbot', "/stock")


@events.register(events.NewMessage(incoming=True, from_users='chtwrsbot'))
async def handler_in_gdeposit(event):
    global rss_code
    global depositing
    msg = event.raw_text
    id_client = event.client._self_id
    if "Storage" in msg and depositing[id_client]:
        data = msg.replace("(", "").replace(")", "")
        rss_list = data.split("\n")
        stop = False
        i = 0
        size = len(rss_list)
        print ("{0}".format (depositing[id_client]))
        while i < size and not stop:
            rss_name = rss_list[i].split(" ")[0]
            if rss_name in RSS.keys():
                if RSS[rss_name] == rss_code:
                    rss_cant = rss_list[i].split(" ")[1]
                    x = random.randint(4,8)
                    await asyncio.sleep(x)
                    await event.client.send_message('chtwrsbot', "/gd_{0}_{1}".format(
                    rss_code, rss_cant
                    ))
            i += 1
    
        



RSS = {
    'Thread':   '01',
    'Stick':    '02',
    'Pelt':     '03',
    'Bone':     '04',
    'Coal':     '05',
    'Charcoal': '06',
    'Powder':   '07',
    'ore': '08',
    'Cloth':    '09',
    'Silver ore':   '10',
    'Bauxite':  '11',
    'Cord':     '12',
    'stone':  '13',
    'Wooden shaft': '14',
    'Sapphire': '15',
    'Solvent':  '16',
    'Ruby':     '17',
    'Hardener': '18',
    'Steel':    '19',
    'Leather':  '20',
    'Bone powder':  '21',
    'String':   '22',
    'Coke':     '23',
    'Purified powder':  '24',
    'Silver alloy': '25',
    'Steel mold':   '27',
    'Silver mold':  '28',
    'Blaksmith frame':  '29',
    'Artisan drame':    '30',
    'Rope':     '31',
    'Silver frame': '32',
    'Metal plate':  '33',
    'Metallic fibber':  '34',
    'Crafted feather':  '35',
    'Quality cloth':    '36',
    'Blaksmith mold':   '37',
    'Artisan mold': '38'
}




@events.register(events.NewMessage(chats=-796720529))
async def defensa_valley_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(21):   await client.send_message(-796720529, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '/quests_forest':
       	for i in range(78):   await client.send_message(-796720529, '/forest', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_swamp':
       	for i in range(78):   await client.send_message(-796720529, '/swamp', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_valley':
       	for i in range(78):   await client.send_message(-796720529, '/valley', schedule=datetime.timedelta(hours= (1 * i)))

@events.register(events.NewMessage(chats=-796720529))
async def defensa_valleys_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/fast_fight':
       	for i in range(99):   await client.send_message(-796720529, '▶️Fast fight', schedule=datetime.timedelta(hours= (4 * i)))

@events.register(events.NewMessage(chats=-704711135))
async def defensa_swamp_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(21):   await client.send_message(-704711135, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '/quests_forest':
       	for i in range(78):   await client.send_message(-704711135, '/forest', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_swamp':
       	for i in range(78):   await client.send_message(-704711135, '/swamp', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_valley':
       	for i in range(78):   await client.send_message(-704711135, '/valley', schedule=datetime.timedelta(hours= (1 * i)))

@events.register(events.NewMessage(chats=-704711135))
async def defensa_swamps_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/fast_fight':
       	for i in range(99):   await client.send_message(-704711135, '▶️Fast fight', schedule=datetime.timedelta(hours= (4 * i)))

@events.register(events.NewMessage(chats='RikaShino_bot', incoming = True))
async def RikaShino_bot_handler(event):
 client = event.client
 async for message in client.iter_messages('RikaShino_bot', limit=1, from_user='RikaShino_bot'):
                 await message.forward_to('nixth')

@events.register(events.NewMessage(chats=-403697562))
async def programar_quests_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/quests_forest':
       	for i in range(78):   await client.send_message(-403697562, '/forest', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_swamp':
       	for i in range(78):   await client.send_message(-403697562, '/swamp', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_valley':
       	for i in range(78):   await client.send_message(-403697562, '/valley', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/defend':
       	for i in range(21):   await client.send_message(-403697562, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))


@events.register(events.NewMessage(chats=-587224893))
async def programar_quests_otaku_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(21):   await client.send_message(-587224893, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '/quests_forest':
       	for i in range(78):   await client.send_message(-587224893, '/forest', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_swamp':
       	for i in range(78):   await client.send_message(-587224893, '/swamp', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_valley':
       	for i in range(78):   await client.send_message(-587224893, '/valley', schedule=datetime.timedelta(hours= (1 * i)))

@events.register(events.NewMessage(chats=-550722607))
async def six_programar_def_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(100):   await client.send_message(-550722607, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))

@events.register(events.NewMessage(chats=777000, incoming = True))
async def tlg_handler(event):
	client = event.client
	if "Verification" in event.raw_text:
                async for message in client.iter_messages(777000, limit=1, from_user=777000):
                	await message.forward_to('ale_guetta')
	if "Verificación" in event.raw_text:
                async for message in client.iter_messages(777000, limit=1, from_user=777000):
                	await message.forward_to('ale_guetta')

@events.register(events.NewMessage(chats='Ale_Guetta'))
async def ares_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(33):   await client.send_message(1042569400, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))
       if event.raw_text == '/quests_forest':
       	for i in range(60):   await client.send_message(1042569400, '/forest', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_swamp':
       	for i in range(60):   await client.send_message(1042569400, '/swamp', schedule=datetime.timedelta(hours= (1 * i)))

doSwamp = False
doForest = False
doValley = False

@events.register(events.NewMessage(incoming=True))
async def full_quest_swamp2_handler(event):
 client = event.client
 global doSwamp
 if 'Not enough stamina' in event.raw_text:
         doSwamp = False
         print("false" ) 
 if '/swamp_on' in event.raw_text:
         doSwamp = True
         print("true") 
 if '/swamp_off' in event.raw_text:
         doSwamp = False
         print("false" ) 
 global doValley
 if 'Not enough stamina' in event.raw_text:
         doValley = False
         print("false" )
 if '/valley_on' in event.raw_text:
         doValley = True
         print("true") 
 if '/valley_off' in event.raw_text:
         doValley = False
         print("false" ) 
 global doForest
 if '/forest_on' in event.raw_text:
         doForest = True
         print("true") 
 if '/forest_off' in event.raw_text:
         doForest = False
         print("false" ) 
 if 'Not enough stamina' in event.raw_text:
         doForest = False
         print("false" )


@events.register(events.NewMessage(chats='me'))
async def quest_forest_palli_handler(event):
 client = event.client
 global doSwamp
 if 'Not enough stamina' in event.raw_text:
         doSwamp = False
         print("false" ) 
 if '/swamp_on' in event.raw_text:
         doSwamp = True
         print("true") 
 if '/swamp_off' in event.raw_text:
         doSwamp = False
         print("false" ) 
 global doValley
 if 'Not enough stamina' in event.raw_text:
         doValley = False
         print("false" )
 if '/valley_on' in event.raw_text:
         doValley = True
         print("true") 
 if '/valley_off' in event.raw_text:
         doValley = False
         print("false" ) 
 global doForest
 if '/forest_on' in event.raw_text:
         doForest = True
         print("true") 
 if '/forest_off' in event.raw_text:
         doForest = False
         print("false" ) 
 if 'Not enough stamina' in event.raw_text:
         doForest = False
         print("false" )
 
@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def full_quests_handler(event):
 client = event.client
 if doForest:
                 if "Many things can happen in the forest." in event.raw_text:
                  await asyncio.sleep(3)
                  async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                   await message.click(0)
                   x = random.randint(370,400)
                   await asyncio.sleep(x)
                   await client.send_message( 'chtwrsbot' , '🗺Quests' )
 if doSwamp:
                 if "Many things can happen in the forest." in event.raw_text:
                  await asyncio.sleep(3)
                  async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                   await message.click(1)
                   x = random.randint(380,400)
                   await asyncio.sleep(x)
                   await client.send_message( 'chtwrsbot' , '🗺Quests' )
 if doValley:
                 if "Many things can happen in the forest." in event.raw_text:
                  await asyncio.sleep(3)
                  async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                   await message.click(2)
                   x = random.randint(380,400)
                   await asyncio.sleep(x)
                   await client.send_message( 'chtwrsbot' , '🗺Quests' )


@events.register(events.NewMessage(chats=-550722607))
async def arenas_casa_de_papel_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/fast_fight':
       	for i in range(95):   await client.send_message(-550722607, '▶️Fast fight', schedule=datetime.timedelta(hours= (4 * i)))

@events.register(events.NewMessage(chats=-550722607))
async def programar_casa_de_papel_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/quests_forest':
       	for i in range(60):   await client.send_message(-550722607, '/forest', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_swamp':
       	for i in range(60):   await client.send_message(-550722607, '/swamp', schedule=datetime.timedelta(hours= (1 * i)))
       if event.raw_text == '/quests_valley':
       	for i in range(60):   await client.send_message(-550722607, '/valley', schedule=datetime.timedelta(hours= (1 * i)))

@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def mobs_send_ale_handler(event):
	client = event.client
	if "You met some hostile creatures. Be careful:" in event.raw_text:
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await client.forward_messages(1079864305, event.message)


@events.register(events.NewMessage(chats='chtwrsbot', incoming = True))
async def depositar_rec_handler(event):
	client = event.client
	if "Earned: Magic stone (1)" in event.raw_text:
		x = random.randint(2,10)
		await asyncio.sleep(x)
		async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
			await client.send_message('chtwrsbot', '/g_deposit 13')
	if "Earned: Magic stone (2)" in event.raw_text:
		x = random.randint(2,10)
		await asyncio.sleep(x)
		async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
			await client.send_message('chtwrsbot', '/g_deposit 13 2')
	if "Earned: Ruby (1)" in event.raw_text:
		x = random.randint(2,10)
		await asyncio.sleep(x)
		async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
			await client.send_message('chtwrsbot', '/g_deposit 17')


def randomnum( ) :
       numero = random.randit(385,400)
       return numero


@events.register(events.NewMessage(chats='me', outgoing=True))
async def chris_alch_afk_handler(event):
       logger.info(f"New message {event.raw_text}")
       client = event.client
       if event.raw_text == '/defend':
       	for i in range(90):   await client.send_message(408101137, '🛡Defend', schedule=datetime.timedelta(hours= (8 * i)))

@events.register(events.NewMessage(chats='abbyx91', incoming = True))
async def spend_and_hide_chris_handler(event):
	client = event.client
	async for message in client.iter_messages('abbyx91', limit=1, from_user='abbyx91'):
                await client.send_message('chtwrsbot', message)
                await asyncio.sleep(5)
                async for message in client.iter_messages('chtwrsbot', limit=1, from_user='chtwrsbot'):
                	await message.forward_to('abbyx91')



client1 = None
if API_ID and API_HASH and STRING_SESSION:
	#logger.info(f"{STRING_SESSION}")
	client1 = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
	# Agrego al cliente la capacidad de escuchar los mensajes de "Mensajes guardados"
	client1.add_event_handler(me_handler)
	client1.add_event_handler(foray_handler)
	client1.add_event_handler(mobs_handler)
	client1.add_event_handler(quests_ale_handler)
	client1.add_event_handler(check_ale_handler)
	client1.add_event_handler(ale_script_handler)
	client1.add_event_handler(defensa_handler)
	client1.add_event_handler(reports_handler)
	client1.add_event_handler(reportes_handler)
	client1.add_event_handler(dados_handler)
	client1.add_event_handler(dados_hacks_handler)
	client1.add_event_handler(pogs_handler)
	client1.add_event_handler(pogs_hacks_handler)
	client1.add_event_handler(ale_afk_handler)
	client1.add_event_handler(trader_handler)
	client1.add_event_handler(trader_rss_handler)
	client1.add_event_handler(def_palli_handler)
	client1.add_event_handler(bichos_damian_handler)
	client1.add_event_handler(orders_alts_moon_handler)
	client1.add_event_handler(handler_delete_messages)
	client1.add_event_handler(recurso_trader_handler)
	client1.add_event_handler(bichos_dianik_handler)
	client1.add_event_handler(defensa_swamp_handler)
	client1.add_event_handler(defensa_valley_handler)
	client1.add_event_handler(RikaShino_bot_handler)
	client1.add_event_handler(programar_quests_handler)
	client1.add_event_handler(programar_quests_otaku_handler)
	client1.add_event_handler(programar_otaku_handler) 
	client1.add_event_handler(orders_alts_pollitos_handler)
	client1.add_event_handler(programar_casa_de_papel_handler)
	client1.add_event_handler(squire_script_ale_handler)
	client1.add_event_handler(squire_script_handler)

client2 = None
if API_ID2 and API_HASH2 and STRING_SESSION2:
	client2 = TelegramClient(StringSession(STRING_SESSION2), API_ID2, API_HASH2)
	client2.add_event_handler(me_handler)
	client2.add_event_handler(foray_handler)
	client2.add_event_handler(mobs_handler)
	client2.add_event_handler(bichos_palli_handler)
	client2.add_event_handler(check_melody_handler)
	client2.add_event_handler(quests_melody_handler)
	client2.add_event_handler(mobs_send_cheo_handler)
	client2.add_event_handler(reports_melody_handler)
	client2.add_event_handler(antorchas_handler)
	client2.add_event_handler(dados_handler)
	client2.add_event_handler(dados_hacks_handler)
	client2.add_event_handler(mel_afk_handler)
	client2.add_event_handler(trader_melody_handler)
	client2.add_event_handler(trader_melody_palli_handler)
	client2.add_event_handler(defensa_swamps_handler)
	client2.add_event_handler(defensa_valleys_handler)
	client2.add_event_handler(ares_handler)

client3 = None
if API_ID3 and API_HASH3 and STRING_SESSION3:
	client3 = TelegramClient(StringSession(STRING_SESSION3), API_ID3, API_HASH3)
	client3.add_event_handler(me_handler)
	client3.add_event_handler(altarena_handler)
	client3.add_event_handler(altarena_ok_handler)
	client3.add_event_handler(alts_quest_arenas_handler)
	client3.add_event_handler(bichos_alts_handler)
	client3.add_event_handler(check_acc_handler)
	client3.add_event_handler(check_accounts_handler)
	client3.add_event_handler(check_accounts_swamp_handler)
	client3.add_event_handler(check_accounts_valley_handler)
	client3.add_event_handler(check_state_handler)
	client3.add_event_handler(foray_handler)
	client3.add_event_handler(gp_handler)
	client3.add_event_handler(orders_handler)
	client3.add_event_handler(quests_handler)
	client3.add_event_handler(spend_and_hide_handler)
	client3.add_event_handler(spend_hide_handler)
	client3.add_event_handler(bs_open_shop_handler)
	client3.add_event_handler(handler_in_g_deposit)
	client3.add_event_handler(handler_in_gdeposit)
	client3.add_event_handler(tlg_handler)
	client3.add_event_handler(full_quests_handler)
	client3.add_event_handler(depositar_rec_handler)



client4 = None
if API_ID4 and API_HASH4 and STRING_SESSION4:
	client4 = TelegramClient(StringSession(STRING_SESSION4), API_ID4, API_HASH4)
	client4.add_event_handler(me_handler)
	client4.add_event_handler(altarena_handler)
	client4.add_event_handler(altarena_ok_handler)
	client4.add_event_handler(alts_quest_arenas_handler)
	client4.add_event_handler(bichos_alts_handler)
	client4.add_event_handler(check_acc_handler)
	client4.add_event_handler(check_accounts_handler)
	client4.add_event_handler(check_accounts_swamp_handler)
	client4.add_event_handler(check_accounts_valley_handler)
	client4.add_event_handler(check_state_handler)
	client4.add_event_handler(foray_handler)
	client4.add_event_handler(gp_handler)
	client4.add_event_handler(orders_handler)
	client4.add_event_handler(quests_handler)
	client4.add_event_handler(spend_and_hide_handler)
	client4.add_event_handler(spend_hide_handler)
	client4.add_event_handler(handler_in_g_deposit)
	client4.add_event_handler(handler_in_gdeposit)
	client4.add_event_handler(tlg_handler)
	client4.add_event_handler(full_quests_handler)
	client4.add_event_handler(depositar_rec_handler)




client5 = None
if API_ID5 and API_HASH5 and STRING_SESSION5:
	client5 = TelegramClient(StringSession(STRING_SESSION5), API_ID5, API_HASH5)
	client5.add_event_handler(me_handler)
	client5.add_event_handler(altarena_handler)
	client5.add_event_handler(altarena_ok_handler)
	client5.add_event_handler(alts_quest_arenas_handler)
	client5.add_event_handler(bichos_alts_handler)
	client5.add_event_handler(check_acc_handler)
	client5.add_event_handler(check_accounts_handler)
	client5.add_event_handler(check_accounts_swamp_handler)
	client5.add_event_handler(check_accounts_valley_handler)
	client5.add_event_handler(check_state_handler)
	client5.add_event_handler(foray_handler)
	client5.add_event_handler(gp_handler)
	client5.add_event_handler(orders_handler)
	client5.add_event_handler(quests_handler)
	client5.add_event_handler(spend_and_hide_handler)
	client5.add_event_handler(spend_hide_handler)
	client5.add_event_handler(handler_in_g_deposit)
	client5.add_event_handler(handler_in_gdeposit)
	client5.add_event_handler(tlg_handler)
	client5.add_event_handler(full_quests_handler)
	client5.add_event_handler(depositar_rec_handler)




client6 = None
if API_ID6 and API_HASH6 and STRING_SESSION6:
	client6 = TelegramClient(StringSession(STRING_SESSION6), API_ID6, API_HASH6)
	client6.add_event_handler(me_handler)
	client6.add_event_handler(altarena_handler)
	client6.add_event_handler(altarena_ok_handler)
	client6.add_event_handler(alts_quest_arenas_handler)
	client6.add_event_handler(bichos_alts_handler)
	client6.add_event_handler(check_acc_handler)
	client6.add_event_handler(check_accounts_handler)
	client6.add_event_handler(check_accounts_swamp_handler)
	client6.add_event_handler(check_accounts_valley_handler)
	client6.add_event_handler(check_state_handler)
	client6.add_event_handler(foray_handler)
	client6.add_event_handler(gp_handler)
	client6.add_event_handler(orders_handler)
	client6.add_event_handler(quests_handler)
	client6.add_event_handler(spend_and_hide_handler)
	client6.add_event_handler(spend_hide_handler)
	client6.add_event_handler(handler_in_g_deposit)
	client6.add_event_handler(handler_in_gdeposit)
	client6.add_event_handler(tlg_handler)
	client6.add_event_handler(full_quests_handler)
	client6.add_event_handler(depositar_rec_handler)


client7 = None
if API_ID7 and API_HASH7 and STRING_SESSION7:
	client7 = TelegramClient(StringSession(STRING_SESSION7), API_ID7, API_HASH7)
	client7.add_event_handler(me_handler)
	client7.add_event_handler(full_quest2_handler)
	client7.add_event_handler(quest_forest_handler)
	client7.add_event_handler(full_quest_handler)
	client7.add_event_handler(full_quests_handler)
	client7.add_event_handler(full_quest_swamp2_handler)
	client7.add_event_handler(mobs_send_ale_handler)
	client7.add_event_handler(spend_and_hide_handler)

client8 = None
if API_ID8 and API_HASH8 and STRING_SESSION8:
	client8 = TelegramClient(StringSession(STRING_SESSION8), API_ID8, API_HASH8)
	client8.add_event_handler(me_handler)
	client8.add_event_handler(chatwars_handler)
	client8.add_event_handler(chatwars_swamp_quests_handler)
	client8.add_event_handler(foray_handler)


client9 = None
if API_ID9 and API_HASH9 and STRING_SESSION9:
	client9 = TelegramClient(StringSession(STRING_SESSION9), API_ID9, API_HASH9)
	client9.add_event_handler(me_handler)
	client9.add_event_handler(altarena_handler)
	client9.add_event_handler(altarena_ok_handler)
	client9.add_event_handler(alts_quest_arenas_handler)
	client9.add_event_handler(bichos_alts_handler)
	client9.add_event_handler(check_acc_handler)
	client9.add_event_handler(check_accounts_handler)
	client9.add_event_handler(check_accounts_swamp_handler)
	client9.add_event_handler(check_accounts_valley_handler)
	client9.add_event_handler(check_state_handler)
	client9.add_event_handler(foray_handler)
	client9.add_event_handler(gp_handler)
	client9.add_event_handler(orders_handler)
	client9.add_event_handler(quests_handler)
	client9.add_event_handler(spend_and_hide_handler)
	client9.add_event_handler(spend_hide_handler)
	client9.add_event_handler(handler_in_g_deposit)
	client9.add_event_handler(handler_in_gdeposit)
	client9.add_event_handler(tlg_handler)
	client9.add_event_handler(full_quests_handler)



client10 = None
if API_ID10 and API_HASH10 and STRING_SESSION10:
	client10 = TelegramClient(StringSession(STRING_SESSION10), API_ID10, API_HASH10)
	client10.add_event_handler(me_handler)
	client10.add_event_handler(altarena_handler)
	client10.add_event_handler(altarena_ok_handler)
	client10.add_event_handler(alts_quest_arenas_handler)
	client10.add_event_handler(bichos_alts_handler)
	client10.add_event_handler(check_acc_handler)
	client10.add_event_handler(check_accounts_handler)
	client10.add_event_handler(check_accounts_valley_handler)
	client10.add_event_handler(check_accounts_swamp_handler)
	client10.add_event_handler(check_state_handler)
	client10.add_event_handler(foray_handler)
	client10.add_event_handler(gp_handler)
	client10.add_event_handler(orders_handler)
	client10.add_event_handler(quests_handler)
	client10.add_event_handler(spend_and_hide_handler)
	client10.add_event_handler(spend_hide_handler)
	client10.add_event_handler(handler_in_g_deposit)
	client10.add_event_handler(handler_in_gdeposit)
	client10.add_event_handler(tlg_handler)
	client10.add_event_handler(full_quests_handler)




client11 = None
if API_ID11 and API_HASH11 and STRING_SESSION11:
	client11 = TelegramClient(StringSession(STRING_SESSION11), API_ID11, API_HASH11)
	client11.add_event_handler(me_handler)
	client11.add_event_handler(altarena_handler)
	client11.add_event_handler(altarena_ok_handler)
	client11.add_event_handler(alts_quest_arenas_handler)
	client11.add_event_handler(bichos_alts_handler)
	client11.add_event_handler(check_acc_handler)
	client11.add_event_handler(check_accounts_handler)
	client11.add_event_handler(check_accounts_valley_handler)
	client11.add_event_handler(check_accounts_swamp_handler)
	client11.add_event_handler(check_state_handler)
	client11.add_event_handler(foray_handler)
	client11.add_event_handler(gp_handler)
	client11.add_event_handler(orders_handler)
	client11.add_event_handler(quests_handler)
	client11.add_event_handler(spend_and_hide_handler)
	client11.add_event_handler(spend_hide_handler)
	client11.add_event_handler(handler_in_g_deposit)
	client11.add_event_handler(handler_in_gdeposit)
	client11.add_event_handler(tlg_handler)
	client11.add_event_handler(full_quests_handler)
	client11.add_event_handler(depositar_rec_handler)



client12 = None
if API_ID12 and API_HASH12 and STRING_SESSION12:
	client12 = TelegramClient(StringSession(STRING_SESSION12), API_ID12, API_HASH12)
	client12.add_event_handler(me_handler)
	client12.add_event_handler(altarena_handler)
	client12.add_event_handler(altarena_ok_handler)
	client12.add_event_handler(alts_quest_arenas_handler)
	client12.add_event_handler(bichos_alts_handler)
	client12.add_event_handler(check_acc_handler)
	client12.add_event_handler(check_accounts_handler)
	client12.add_event_handler(check_accounts_swamp_handler)
	client12.add_event_handler(check_accounts_valley_handler)
	client12.add_event_handler(check_state_handler)
	client12.add_event_handler(foray_handler)
	client12.add_event_handler(gp_handler)
	client12.add_event_handler(orders_handler)
	client12.add_event_handler(quests_handler)
	client12.add_event_handler(spend_and_hide_handler)
	client12.add_event_handler(spend_hide_handler)
	client12.add_event_handler(handler_in_g_deposit)
	client12.add_event_handler(handler_in_gdeposit)
	client12.add_event_handler(tlg_handler)
	client12.add_event_handler(full_quests_handler)
	client12.add_event_handler(depositar_rec_handler)


client13 = None
if API_ID13 and API_HASH13 and STRING_SESSION13:
	client13 = TelegramClient(StringSession(STRING_SESSION13), API_ID13, API_HASH13)
	client13.add_event_handler(me_handler)
	client13.add_event_handler(altarena_handler)
	client13.add_event_handler(altarena_ok_handler)
	client13.add_event_handler(alts_quest_arenas_handler)
	client13.add_event_handler(bichos_alts_handler)
	client13.add_event_handler(check_acc_handler)
	client13.add_event_handler(check_accounts_handler)
	client13.add_event_handler(check_accounts_swamp_handler)
	client13.add_event_handler(check_accounts_valley_handler)
	client13.add_event_handler(check_state_handler)
	client13.add_event_handler(foray_handler)
	client13.add_event_handler(gp_handler)
	client13.add_event_handler(orders_handler)
	client13.add_event_handler(quests_handler)
	client13.add_event_handler(spend_and_hide_handler)
	client13.add_event_handler(spend_hide_handler)
	client13.add_event_handler(handler_in_g_deposit)
	client13.add_event_handler(handler_in_gdeposit)
	client13.add_event_handler(tlg_handler)
	client13.add_event_handler(full_quests_handler)
	client13.add_event_handler(depositar_rec_handler)


client14 = None
if API_ID14 and API_HASH14 and STRING_SESSION14:
	client14 = TelegramClient(StringSession(STRING_SESSION14), API_ID14, API_HASH14)
	client14.add_event_handler(me_handler)
	client14.add_event_handler(altarena_handler)
	client14.add_event_handler(altarena_ok_handler)
	client14.add_event_handler(alts_quest_arenas_handler)
	client14.add_event_handler(bichos_alts_handler)
	client14.add_event_handler(check_acc_handler)
	client14.add_event_handler(check_accounts_handler)
	client14.add_event_handler(check_accounts_swamp_handler)
	client14.add_event_handler(check_accounts_valley_handler)
	client14.add_event_handler(check_state_handler)
	client14.add_event_handler(foray_handler)
	client14.add_event_handler(gp_handler)
	client14.add_event_handler(orders_handler)
	client14.add_event_handler(quests_handler)
	client14.add_event_handler(spend_and_hide_handler)
	client14.add_event_handler(spend_hide_handler)
	client14.add_event_handler(handler_in_g_deposit)
	client14.add_event_handler(handler_in_gdeposit)
	client14.add_event_handler(tlg_handler)
	client14.add_event_handler(full_quests_handler)


client15 = None
if API_ID15 and API_HASH15 and STRING_SESSION15:
	client15 = TelegramClient(StringSession(STRING_SESSION15), API_ID15, API_HASH15)
	client15.add_event_handler(me_handler)
	client15.add_event_handler(altarena_handler)
	client15.add_event_handler(altarena_ok_handler)
	client15.add_event_handler(alts_quest_arenas_handler)
	client15.add_event_handler(bichos_alts_handler)
	client15.add_event_handler(check_acc_handler)
	client15.add_event_handler(check_accounts_handler)
	client15.add_event_handler(check_accounts_swamp_handler)
	client15.add_event_handler(check_accounts_valley_handler)
	client15.add_event_handler(check_state_handler)
	client15.add_event_handler(foray_handler)
	client15.add_event_handler(gp_handler)
	client15.add_event_handler(orders_handler)
	client15.add_event_handler(quests_handler)
	client15.add_event_handler(spend_and_hide_handler)
	client15.add_event_handler(spend_hide_handler)
	client15.add_event_handler(handler_in_g_deposit)
	client15.add_event_handler(handler_in_gdeposit)
	client15.add_event_handler(tlg_handler)
	client15.add_event_handler(full_quests_handler)
	client15.add_event_handler(depositar_rec_handler)




client16 = None
if API_ID16 and API_HASH16 and STRING_SESSION16:
	client16 = TelegramClient(StringSession(STRING_SESSION16), API_ID16, API_HASH16)
	client16.add_event_handler(me_handler)
	client16.add_event_handler(altarena_handler)
	client16.add_event_handler(altarena_ok_handler)
	client16.add_event_handler(alts_quest_arenas_handler)
	client16.add_event_handler(bichos_alts_handler)
	client16.add_event_handler(check_acc_handler)
	client16.add_event_handler(check_accounts_handler)
	client16.add_event_handler(check_accounts_swamp_handler)
	client16.add_event_handler(check_accounts_valley_handler)
	client16.add_event_handler(check_state_handler)
	client16.add_event_handler(gp_handler)
	client16.add_event_handler(orders_handler)
	client16.add_event_handler(quests_handler)
	client16.add_event_handler(spend_and_hide_handler)
	client16.add_event_handler(spend_hide_handler)
	client16.add_event_handler(handler_in_g_deposit)
	client16.add_event_handler(handler_in_gdeposit)
	client16.add_event_handler(tlg_handler)
	client16.add_event_handler(full_quests_handler)





client17 = None
if API_ID17 and API_HASH17 and STRING_SESSION17:
	client17 = TelegramClient(StringSession(STRING_SESSION17), API_ID17, API_HASH17)
	client17.add_event_handler(me_handler)
	client17.add_event_handler(altarena_handler)
	client17.add_event_handler(altarena_ok_handler)
	client17.add_event_handler(alts_quest_arenas_handler)
	client17.add_event_handler(bichos_alts_handler)
	client17.add_event_handler(check_acc_handler)
	client17.add_event_handler(check_accounts_handler)
	client17.add_event_handler(check_accounts_swamp_handler)
	client17.add_event_handler(check_accounts_valley_handler)
	client17.add_event_handler(check_state_handler)
	client17.add_event_handler(foray_handler)
	client17.add_event_handler(gp_handler)
	client17.add_event_handler(orders_handler)
	client17.add_event_handler(quests_handler)
	client17.add_event_handler(spend_and_hide_handler)
	client17.add_event_handler(spend_hide_handler)
	client17.add_event_handler(handler_in_g_deposit)
	client17.add_event_handler(handler_in_gdeposit)
	client17.add_event_handler(tlg_handler)
	client17.add_event_handler(full_quests_handler)
	client17.add_event_handler(depositar_rec_handler)

client18 = None
if API_ID18 and API_HASH18 and STRING_SESSION18:
	client18 = TelegramClient(StringSession(STRING_SESSION18), API_ID18, API_HASH18)
	client18.add_event_handler(me_handler)
	client18.add_event_handler(altarena_handler)
	client18.add_event_handler(altarena_ok_handler)
	client18.add_event_handler(alts_quest_arenas_handler)
	client18.add_event_handler(bichos_alts_handler)
	client18.add_event_handler(check_acc_handler)
	client18.add_event_handler(check_accounts_handler)
	client18.add_event_handler(check_accounts_swamp_handler)
	client18.add_event_handler(check_accounts_valley_handler)
	client18.add_event_handler(check_state_handler)
	client18.add_event_handler(foray_handler)
	client18.add_event_handler(gp_handler)
	client18.add_event_handler(orders_handler)
	client18.add_event_handler(quests_handler)
	client18.add_event_handler(spend_and_hide_handler)
	client18.add_event_handler(spend_hide_handler)
	client18.add_event_handler(handler_in_g_deposit)
	client18.add_event_handler(handler_in_gdeposit)
	client18.add_event_handler(tlg_handler)
	client18.add_event_handler(full_quests_handler)
	client18.add_event_handler(depositar_rec_handler)



client19 = None
if API_ID19 and API_HASH19 and STRING_SESSION19:
	client19 = TelegramClient(StringSession(STRING_SESSION19), API_ID19, API_HASH19)
	client19.add_event_handler(me_handler)
	client19.add_event_handler(altarena_handler)
	client19.add_event_handler(altarena_ok_handler)
	client19.add_event_handler(alts_quest_arenas_handler)
	client19.add_event_handler(bichos_alts_handler)
	client19.add_event_handler(check_acc_handler)
	client19.add_event_handler(check_accounts_handler)
	client19.add_event_handler(check_accounts_swamp_handler)
	client19.add_event_handler(check_accounts_valley_handler)
	client19.add_event_handler(check_state_handler)
	client19.add_event_handler(foray_handler)
	client19.add_event_handler(gp_handler)
	client19.add_event_handler(orders_handler)
	client19.add_event_handler(quests_handler)
	client19.add_event_handler(spend_and_hide_handler)
	client19.add_event_handler(spend_hide_handler)
	client19.add_event_handler(handler_in_g_deposit)
	client19.add_event_handler(handler_in_gdeposit)
	client19.add_event_handler(tlg_handler)
	client19.add_event_handler(full_quests_handler)


client20 = None
if API_ID20 and API_HASH20 and STRING_SESSION20:
	client20 = TelegramClient(StringSession(STRING_SESSION20), API_ID20, API_HASH20)
	client20.add_event_handler(me_handler)
	client20.add_event_handler(altarena_handler)
	client20.add_event_handler(altarena_ok_handler)
	client20.add_event_handler(alts_quest_arenas_handler)
	client20.add_event_handler(bichos_alts_handler)
	client20.add_event_handler(check_acc_handler)
	client20.add_event_handler(check_accounts_handler)
	client20.add_event_handler(check_accounts_swamp_handler)
	client20.add_event_handler(check_accounts_valley_handler)
	client20.add_event_handler(check_state_handler)
	client20.add_event_handler(foray_handler)
	client20.add_event_handler(gp_handler)
	client20.add_event_handler(orders_handler)
	client20.add_event_handler(quests_handler)
	client20.add_event_handler(spend_and_hide_handler)
	client20.add_event_handler(spend_hide_handler)
	client20.add_event_handler(handler_in_g_deposit)
	client20.add_event_handler(handler_in_gdeposit)
	client20.add_event_handler(tlg_handler)
	client20.add_event_handler(full_quests_handler)
	client20.add_event_handler(depositar_rec_handler)


client21 = None
if API_ID21 and API_HASH21 and STRING_SESSION21:
	client21 = TelegramClient(StringSession(STRING_SESSION21), API_ID21, API_HASH21)
	client21.add_event_handler(me_handler)
	client21.add_event_handler(altarena_handler)
	client21.add_event_handler(altarena_ok_handler)
	client21.add_event_handler(alts_quest_arenas_handler)
	client21.add_event_handler(bichos_alts_handler)
	client21.add_event_handler(check_acc_handler)
	client21.add_event_handler(check_accounts_handler)
	client21.add_event_handler(check_accounts_swamp_handler)
	client21.add_event_handler(check_accounts_valley_handler)
	client21.add_event_handler(check_state_handler)
	client21.add_event_handler(foray_handler)
	client21.add_event_handler(gp_handler)
	client21.add_event_handler(orders_handler)
	client21.add_event_handler(quests_handler)
	client21.add_event_handler(spend_and_hide_handler)
	client21.add_event_handler(spend_hide_handler)
	client21.add_event_handler(handler_in_g_deposit)
	client21.add_event_handler(handler_in_gdeposit)
	client21.add_event_handler(tlg_handler)
	client21.add_event_handler(full_quests_handler)


client22 = None
if API_ID22 and API_HASH22 and STRING_SESSION22:
	client22 = TelegramClient(StringSession(STRING_SESSION22), API_ID22, API_HASH22)
	client22.add_event_handler(me_handler)
	client22.add_event_handler(altarena_handler)
	client22.add_event_handler(altarena_ok_handler)
	client22.add_event_handler(alts_quest_arenas_handler)
	client22.add_event_handler(bichos_alts_handler)
	client22.add_event_handler(check_acc_handler)
	client22.add_event_handler(check_accounts_handler)
	client22.add_event_handler(check_accounts_swamp_handler)
	client22.add_event_handler(check_accounts_valley_handler)
	client22.add_event_handler(check_state_handler)
	client22.add_event_handler(foray_handler)
	client22.add_event_handler(gp_handler)
	client22.add_event_handler(orders_handler)
	client22.add_event_handler(quests_handler)
	client22.add_event_handler(spend_and_hide_handler)
	client22.add_event_handler(spend_hide_handler)
	client22.add_event_handler(handler_in_g_deposit)
	client22.add_event_handler(handler_in_gdeposit)
	client22.add_event_handler(tlg_handler)
	client22.add_event_handler(full_quests_handler)


client23 = None
if API_ID23 and API_HASH23 and STRING_SESSION23:
	client23 = TelegramClient(StringSession(STRING_SESSION23), API_ID23, API_HASH23)
	client23.add_event_handler(me_handler)
	client23.add_event_handler(altarena_handler)
	client23.add_event_handler(altarena_ok_handler)
	client23.add_event_handler(alts_quest_arenas_handler)
	client23.add_event_handler(bichos_alts_handler)
	client23.add_event_handler(check_acc_handler)
	client23.add_event_handler(check_accounts_handler)
	client23.add_event_handler(check_accounts_swamp_handler)
	client23.add_event_handler(check_accounts_valley_handler)
	client23.add_event_handler(check_state_handler)
	client23.add_event_handler(foray_handler)
	client23.add_event_handler(gp_handler)
	client23.add_event_handler(orders_handler)
	client23.add_event_handler(quests_handler)
	client23.add_event_handler(spend_and_hide_handler)
	client23.add_event_handler(spend_hide_handler)
	client23.add_event_handler(handler_in_g_deposit)
	client23.add_event_handler(handler_in_gdeposit)
	client23.add_event_handler(tlg_handler)
	client23.add_event_handler(full_quests_handler)
	client23.add_event_handler(depositar_rec_handler)


client24 = None
if API_ID24 and API_HASH24 and STRING_SESSION24:
	client24 = TelegramClient(StringSession(STRING_SESSION24), API_ID24, API_HASH24)
	client24.add_event_handler(me_handler)
	client24.add_event_handler(altarena_handler)
	client24.add_event_handler(altarena_ok_handler)
	client24.add_event_handler(alts_quest_arenas_handler)
	client24.add_event_handler(bichos_alts_handler)
	client24.add_event_handler(check_acc_handler)
	client24.add_event_handler(check_accounts_handler)
	client24.add_event_handler(check_accounts_swamp_handler)
	client24.add_event_handler(check_accounts_valley_handler)
	client24.add_event_handler(check_state_handler)
	client24.add_event_handler(foray_handler)
	client24.add_event_handler(gp_handler)
	client24.add_event_handler(orders_handler)
	client24.add_event_handler(quests_handler)
	client24.add_event_handler(spend_and_hide_handler)
	client24.add_event_handler(spend_hide_handler)
	client24.add_event_handler(handler_in_g_deposit)
	client24.add_event_handler(handler_in_gdeposit)
	client24.add_event_handler(tlg_handler)
	client24.add_event_handler(full_quests_handler)
	client24.add_event_handler(depositar_rec_handler)


client25 = None
if API_ID25 and API_HASH25 and STRING_SESSION25:
	client25 = TelegramClient(StringSession(STRING_SESSION25), API_ID25, API_HASH25)
	client25.add_event_handler(me_handler)
	client25.add_event_handler(altarena_handler)
	client25.add_event_handler(altarena_ok_handler)
	client25.add_event_handler(alts_quest_arenas_handler)
	client25.add_event_handler(bichos_alts_handler)
	client25.add_event_handler(check_acc_handler)
	client25.add_event_handler(check_accounts_handler)
	client25.add_event_handler(check_accounts_swamp_handler)
	client25.add_event_handler(check_accounts_valley_handler)
	client25.add_event_handler(check_state_handler)
	client25.add_event_handler(foray_handler)
	client25.add_event_handler(gp_handler)
	client25.add_event_handler(orders_handler)
	client25.add_event_handler(quests_handler)
	client25.add_event_handler(spend_and_hide_handler)
	client25.add_event_handler(spend_hide_handler)
	client25.add_event_handler(handler_in_g_deposit)
	client25.add_event_handler(handler_in_gdeposit)
	client25.add_event_handler(tlg_handler)
	client25.add_event_handler(full_quests_handler)


client26 = None
if API_ID26 and API_HASH26 and STRING_SESSION26:
	client26 = TelegramClient(StringSession(STRING_SESSION26), API_ID26, API_HASH26)
	client26.add_event_handler(me_handler)
	client26.add_event_handler(gdef_palli_handler)
	client26.add_event_handler(palli_alts_quests_handler)
	client26.add_event_handler(full_quest2_handler)
	client26.add_event_handler(quest_forest_handler)
	client26.add_event_handler(full_quest_handler)
	client26.add_event_handler(activar_quest_handler)
	client26.add_event_handler(palli_quests_on_handler)
	client26.add_event_handler(palli_check_script_handler)
	client26.add_event_handler(quests_handler)
	client26.add_event_handler(spend_and_hide_handler)
	client26.add_event_handler(full_quest_swamp2_handler)
	client26.add_event_handler(full_quests_handler)

client27 = None
if API_ID27 and API_HASH27 and STRING_SESSION27:
	client27 = TelegramClient(StringSession(STRING_SESSION27), API_ID27, API_HASH27)
	client27.add_event_handler(me_handler)
	client27.add_event_handler(gdef_palli_handler)
	client27.add_event_handler(palli_alts_quests_handler)
	client27.add_event_handler(full_quest2_handler)
	client27.add_event_handler(quest_forest_handler)
	client27.add_event_handler(full_quest_handler)
	client27.add_event_handler(activar_quest_handler)
	client27.add_event_handler(palli_quests_on_handler)
	client27.add_event_handler(palli_check_script_handler)
	client27.add_event_handler(quests_handler)
	client27.add_event_handler(spend_and_hide_handler)
	client27.add_event_handler(full_quest_swamp2_handler)
	client27.add_event_handler(full_quests_handler)

client28 = None
if API_ID28 and API_HASH28 and STRING_SESSION28:
	client28 = TelegramClient(StringSession(STRING_SESSION28), API_ID28, API_HASH28)
	client28.add_event_handler(me_handler)
	client28.add_event_handler(gdef_palli_handler)
	client28.add_event_handler(palli_alts_quests_handler)
	client28.add_event_handler(full_quest2_handler)
	client28.add_event_handler(quest_forest_handler)
	client28.add_event_handler(full_quest_handler)
	client28.add_event_handler(activar_quest_handler)
	client28.add_event_handler(palli_quests_on_handler)
	client28.add_event_handler(palli_check_script_handler)
	client28.add_event_handler(quests_handler)
	client28.add_event_handler(spend_and_hide_handler)
	client28.add_event_handler(full_quest_swamp2_handler)
	client28.add_event_handler(full_quests_handler)

client29 = None
if API_ID29 and API_HASH29 and STRING_SESSION29:
	client29 = TelegramClient(StringSession(STRING_SESSION29), API_ID29, API_HASH29)
	client29.add_event_handler(me_handler)
	client29.add_event_handler(altarena_handler)
	client29.add_event_handler(altarena_ok_handler)
	client29.add_event_handler(alts_quest_arenas_handler)
	client29.add_event_handler(bichos_alts_handler)
	client29.add_event_handler(check_acc_handler)
	client29.add_event_handler(check_accounts_handler)
	client29.add_event_handler(check_accounts_swamp_handler)
	client29.add_event_handler(check_accounts_valley_handler)
	client29.add_event_handler(check_state_handler)
	client29.add_event_handler(foray_handler)
	client29.add_event_handler(gp_handler)
	client29.add_event_handler(orders_handler)
	client29.add_event_handler(quests_handler)
	client29.add_event_handler(spend_and_hide_handler)
	client29.add_event_handler(spend_hide_handler)
	client29.add_event_handler(handler_in_g_deposit)
	client29.add_event_handler(handler_in_gdeposit)
	client29.add_event_handler(tlg_handler)
	client29.add_event_handler(full_quests_handler)

client30 = None
if API_ID30 and API_HASH30 and STRING_SESSION30:
	client30 = TelegramClient(StringSession(STRING_SESSION30), API_ID30, API_HASH30)
	client30.add_event_handler(me_handler)
	client30.add_event_handler(altarena_handler)
	client30.add_event_handler(altarena_ok_handler)
	client30.add_event_handler(alts_quest_arenas_handler)
	client30.add_event_handler(bichos_alts_handler)
	client30.add_event_handler(check_acc_handler)
	client30.add_event_handler(check_accounts_handler)
	client30.add_event_handler(check_accounts_swamp_handler)
	client30.add_event_handler(check_accounts_valley_handler)
	client30.add_event_handler(check_state_handler)
	client30.add_event_handler(foray_handler)
	client30.add_event_handler(gp_handler)
	client30.add_event_handler(orders_handler)
	client30.add_event_handler(quests_handler)
	client30.add_event_handler(spend_and_hide_handler)
	client30.add_event_handler(spend_hide_handler)
	client30.add_event_handler(handler_in_g_deposit)
	client30.add_event_handler(handler_in_gdeposit)
	client30.add_event_handler(tlg_handler)
	client30.add_event_handler(full_quests_handler)

client31 = None
if API_ID31 and API_HASH31 and STRING_SESSION31:
	client31 = TelegramClient(StringSession(STRING_SESSION31), API_ID31, API_HASH31)
	client31.add_event_handler(me_handler)
	client31.add_event_handler(altarena_handler)
	client31.add_event_handler(altarena_ok_handler)
	client31.add_event_handler(alts_quest_arenas_handler)
	client31.add_event_handler(bichos_alts_handler)
	client31.add_event_handler(check_acc_handler)
	client31.add_event_handler(check_accounts_handler)
	client31.add_event_handler(check_accounts_swamp_handler)
	client31.add_event_handler(check_accounts_valley_handler)
	client31.add_event_handler(check_state_handler)
	client31.add_event_handler(foray_handler)
	client31.add_event_handler(gp_handler)
	client31.add_event_handler(orders_handler)
	client31.add_event_handler(quests_handler)
	client31.add_event_handler(spend_and_hide_handler)
	client31.add_event_handler(spend_hide_handler)
	client31.add_event_handler(handler_in_g_deposit)
	client31.add_event_handler(handler_in_gdeposit)
	client31.add_event_handler(tlg_handler)
	client31.add_event_handler(full_quests_handler)

client32 = None
if API_ID32 and API_HASH32 and STRING_SESSION32:
	client32 = TelegramClient(StringSession(STRING_SESSION32), API_ID32, API_HASH32)
	client32.add_event_handler(me_handler)
	client32.add_event_handler(altarena_handler)
	client32.add_event_handler(altarena_ok_handler)
	client32.add_event_handler(alts_quest_arenas_handler)
	client32.add_event_handler(bichos_alts_handler)
	client32.add_event_handler(check_acc_handler)
	client32.add_event_handler(check_accounts_handler)
	client32.add_event_handler(check_accounts_swamp_handler)
	client32.add_event_handler(check_accounts_valley_handler)
	client32.add_event_handler(check_state_handler)
	client32.add_event_handler(foray_handler)
	client32.add_event_handler(gp_handler)
	client32.add_event_handler(orders_handler)
	client32.add_event_handler(quests_handler)
	client32.add_event_handler(spend_and_hide_handler)
	client32.add_event_handler(spend_hide_handler)
	client32.add_event_handler(handler_in_g_deposit)
	client32.add_event_handler(handler_in_gdeposit)
	client32.add_event_handler(tlg_handler)
	client32.add_event_handler(full_quests_handler)

client33 = None
if API_ID33 and API_HASH33 and STRING_SESSION33:
	client33 = TelegramClient(StringSession(STRING_SESSION33), API_ID33, API_HASH33)
	client33.add_event_handler(me_handler)
	client33.add_event_handler(altarena_handler)
	client33.add_event_handler(altarena_ok_handler)
	client33.add_event_handler(alts_quest_arenas_handler)
	client33.add_event_handler(bichos_alts_handler)
	client33.add_event_handler(check_acc_handler)
	client33.add_event_handler(check_accounts_handler)
	client33.add_event_handler(check_accounts_swamp_handler)
	client33.add_event_handler(check_accounts_valley_handler)
	client33.add_event_handler(check_state_handler)
	client33.add_event_handler(foray_handler)
	client33.add_event_handler(gp_handler)
	client33.add_event_handler(orders_handler)
	client33.add_event_handler(quests_handler)
	client33.add_event_handler(spend_and_hide_handler)
	client33.add_event_handler(spend_hide_handler)
	client33.add_event_handler(handler_in_g_deposit)
	client33.add_event_handler(handler_in_gdeposit)
	client33.add_event_handler(tlg_handler)
	client33.add_event_handler(full_quests_handler)

client34 = None
if API_ID34 and API_HASH34 and STRING_SESSION34:
	client34 = TelegramClient(StringSession(STRING_SESSION34), API_ID34, API_HASH34)
	client34.add_event_handler(me_handler)
	client34.add_event_handler(altarena_handler)
	client34.add_event_handler(altarena_ok_handler)
	client34.add_event_handler(alts_quest_arenas_handler)
	client34.add_event_handler(bichos_alts_handler)
	client34.add_event_handler(check_acc_handler)
	client34.add_event_handler(check_accounts_handler)
	client34.add_event_handler(check_accounts_valley_handler)
	client34.add_event_handler(check_accounts_swamp_handler)
	client34.add_event_handler(check_state_handler)
	client34.add_event_handler(foray_handler)
	client34.add_event_handler(gp_handler)
	client34.add_event_handler(orders_handler)
	client34.add_event_handler(quests_handler)
	client34.add_event_handler(spend_and_hide_handler)
	client34.add_event_handler(spend_hide_handler)
	client34.add_event_handler(handler_in_g_deposit)
	client34.add_event_handler(handler_in_gdeposit)
	client34.add_event_handler(tlg_handler)
	client34.add_event_handler(full_quests_handler)

client35 = None
if API_ID35 and API_HASH35 and STRING_SESSION35:
	client35 = TelegramClient(StringSession(STRING_SESSION35), API_ID35, API_HASH35)
	client35.add_event_handler(me_handler)
	client35.add_event_handler(altarena_handler)
	client35.add_event_handler(altarena_ok_handler)
	client35.add_event_handler(alts_quest_arenas_handler)
	client35.add_event_handler(bichos_alts_handler)
	client35.add_event_handler(check_acc_handler)
	client35.add_event_handler(check_accounts_handler)
	client35.add_event_handler(check_accounts_swamp_handler)
	client35.add_event_handler(check_accounts_valley_handler)
	client35.add_event_handler(check_state_handler)
	client35.add_event_handler(foray_handler)
	client35.add_event_handler(gp_handler)
	client35.add_event_handler(orders_handler)
	client35.add_event_handler(quests_handler)
	client35.add_event_handler(spend_and_hide_handler)
	client35.add_event_handler(spend_hide_handler)
	client35.add_event_handler(handler_in_g_deposit)
	client35.add_event_handler(handler_in_gdeposit)
	client35.add_event_handler(tlg_handler)
	client35.add_event_handler(full_quests_handler)

client36 = None
if API_ID36 and API_HASH36 and STRING_SESSION36:
	client36 = TelegramClient(StringSession(STRING_SESSION36), API_ID36, API_HASH36)
	client36.add_event_handler(me_handler)
	client36.add_event_handler(altarena_handler)
	client36.add_event_handler(altarena_ok_handler)
	client36.add_event_handler(alts_quest_arenas_handler)
	client36.add_event_handler(bichos_alts_handler)
	client36.add_event_handler(check_acc_handler)
	client36.add_event_handler(check_accounts_handler)
	client36.add_event_handler(check_accounts_swamp_handler)
	client36.add_event_handler(check_accounts_valley_handler)
	client36.add_event_handler(check_state_handler)
	client36.add_event_handler(foray_handler)
	client36.add_event_handler(gp_handler)
	client36.add_event_handler(orders_handler)
	client36.add_event_handler(quests_handler)
	client36.add_event_handler(spend_and_hide_handler)
	client36.add_event_handler(spend_hide_handler)
	client36.add_event_handler(handler_in_g_deposit)
	client36.add_event_handler(handler_in_gdeposit)
	client36.add_event_handler(tlg_handler)
	client36.add_event_handler(full_quests_handler)

client37 = None
if API_ID37 and API_HASH37 and STRING_SESSION37:
	client37 = TelegramClient(StringSession(STRING_SESSION37), API_ID37, API_HASH37)
	client37.add_event_handler(me_handler)
	client37.add_event_handler(altarena_handler)
	client37.add_event_handler(altarena_ok_handler)
	client37.add_event_handler(alts_quest_arenas_handler)
	client37.add_event_handler(bichos_alts_handler)
	client37.add_event_handler(check_acc_handler)
	client37.add_event_handler(check_accounts_handler)
	client37.add_event_handler(check_accounts_swamp_handler)
	client37.add_event_handler(check_accounts_valley_handler)
	client37.add_event_handler(check_state_handler)
	client37.add_event_handler(foray_handler)
	client37.add_event_handler(gp_handler)
	client37.add_event_handler(orders_handler)
	client37.add_event_handler(quests_handler)
	client37.add_event_handler(spend_and_hide_handler)
	client37.add_event_handler(spend_hide_handler)
	client37.add_event_handler(handler_in_g_deposit)
	client37.add_event_handler(handler_in_gdeposit)
	client37.add_event_handler(tlg_handler)
	client37.add_event_handler(full_quests_handler)

client38 = None
if API_ID38 and API_HASH38 and STRING_SESSION38:
	client38 = TelegramClient(StringSession(STRING_SESSION38), API_ID38, API_HASH38)
	client38.add_event_handler(me_handler)
	client38.add_event_handler(altarena_handler)
	client38.add_event_handler(altarena_ok_handler)
	client38.add_event_handler(alts_quest_arenas_handler)
	client38.add_event_handler(bichos_alts_handler)
	client38.add_event_handler(check_acc_handler)
	client38.add_event_handler(check_accounts_handler)
	client38.add_event_handler(check_accounts_swamp_handler)
	client38.add_event_handler(check_accounts_valley_handler)
	client38.add_event_handler(check_state_handler)
	client38.add_event_handler(foray_handler)
	client38.add_event_handler(gp_handler)
	client38.add_event_handler(orders_handler)
	client38.add_event_handler(quests_handler)
	client38.add_event_handler(spend_and_hide_handler)
	client38.add_event_handler(spend_hide_handler)
	client38.add_event_handler(handler_in_g_deposit)
	client38.add_event_handler(handler_in_gdeposit)
	client38.add_event_handler(tlg_handler)
	client38.add_event_handler(full_quests_handler)

client39 = None
if API_ID39 and API_HASH39 and STRING_SESSION39:
	client39 = TelegramClient(StringSession(STRING_SESSION39), API_ID39, API_HASH39)
	client39.add_event_handler(me_handler)
	client39.add_event_handler(altarena_handler)
	client39.add_event_handler(altarena_ok_handler)
	client39.add_event_handler(alts_quest_arenas_handler)
	client39.add_event_handler(bichos_alts_handler)
	client39.add_event_handler(check_acc_handler)
	client39.add_event_handler(check_accounts_handler)
	client39.add_event_handler(check_accounts_swamp_handler)
	client39.add_event_handler(check_accounts_valley_handler)
	client39.add_event_handler(check_state_handler)
	client39.add_event_handler(foray_handler)
	client39.add_event_handler(gp_handler)
	client39.add_event_handler(orders_handler)
	client39.add_event_handler(quests_handler)
	client39.add_event_handler(spend_and_hide_handler)
	client39.add_event_handler(spend_hide_handler)
	client39.add_event_handler(handler_in_g_deposit)
	client39.add_event_handler(handler_in_gdeposit)
	client39.add_event_handler(tlg_handler)
	client39.add_event_handler(full_quests_handler)

client40 = None
if API_ID40 and API_HASH40 and STRING_SESSION40:
	client40 = TelegramClient(StringSession(STRING_SESSION40), API_ID40, API_HASH40)
	client40.add_event_handler(me_handler)
	client40.add_event_handler(foray_handler)
	client40.add_event_handler(orders_moon_dianik_handler)
	client40.add_event_handler(orders_alts_moon_dianik_handler)
	client40.add_event_handler(arenas_casa_de_papel_handler)


client41 = None
if API_ID41 and API_HASH41 and STRING_SESSION41:
	client41 = TelegramClient(StringSession(STRING_SESSION41), API_ID41, API_HASH41)
	client41.add_event_handler(me_handler)
	client41.add_event_handler(altarena_moon_handler)
	client41.add_event_handler(altarena_ok_moon_handler)
	client41.add_event_handler(alts_quest_arenas_moon_handler)
	client41.add_event_handler(bichos_alts_moon_handler)
	client41.add_event_handler(check_acc_moon_handler)
	client41.add_event_handler(check_accounts_moon_handler)
	client41.add_event_handler(check_state_moon_handler)
	client41.add_event_handler(foray_handler)
	client41.add_event_handler(gp_handler)
	client41.add_event_handler(orders_handler)
	client41.add_event_handler(quests_handler)
	client41.add_event_handler(spend_and_hide_handler)
	client41.add_event_handler(spend_hide_moon_handler)
	client41.add_event_handler(handler_store_messages)
	client41.add_event_handler(six_programar_def_handler)
	client41.add_event_handler(tlg_handler)
	client41.add_event_handler(full_quests_handler)

client42 = None
if API_ID42 and API_HASH42 and STRING_SESSION42:
	client42 = TelegramClient(StringSession(STRING_SESSION42), API_ID42, API_HASH42)
	client42.add_event_handler(me_handler)
	client42.add_event_handler(altarena_moon_handler)
	client42.add_event_handler(altarena_ok_moon_handler)
	client42.add_event_handler(alts_quest_arenas_moon_handler)
	client42.add_event_handler(bichos_alts_moon_handler)
	client42.add_event_handler(check_acc_moon_handler)
	client42.add_event_handler(check_accounts_moon_handler)
	client42.add_event_handler(check_state_moon_handler)
	client42.add_event_handler(foray_handler)
	client42.add_event_handler(gp_handler)
	client42.add_event_handler(orders_handler)
	client42.add_event_handler(quests_handler)
	client42.add_event_handler(spend_and_hide_handler)
	client42.add_event_handler(spend_hide_moon_handler)
	client42.add_event_handler(tlg_handler)
	client42.add_event_handler(full_quests_handler)

client43 = None
if API_ID43 and API_HASH43 and STRING_SESSION43:
	client43 = TelegramClient(StringSession(STRING_SESSION43), API_ID43, API_HASH43)
	client43.add_event_handler(me_handler)
	client43.add_event_handler(altarena_moon_handler)
	client43.add_event_handler(altarena_ok_moon_handler)
	client43.add_event_handler(alts_quest_arenas_moon_handler)
	client43.add_event_handler(bichos_alts_moon_handler)
	client43.add_event_handler(check_acc_moon_handler)
	client43.add_event_handler(check_accounts_moon_handler)
	client43.add_event_handler(check_state_moon_handler)
	client43.add_event_handler(foray_handler)
	client43.add_event_handler(gp_handler)
	client43.add_event_handler(orders_handler)
	client43.add_event_handler(quests_handler)
	client43.add_event_handler(spend_and_hide_handler)
	client43.add_event_handler(spend_hide_moon_handler)
	client43.add_event_handler(tlg_handler)
	client43.add_event_handler(full_quests_handler)


client44 = None
if API_ID44 and API_HASH44 and STRING_SESSION44:
	client44 = TelegramClient(StringSession(STRING_SESSION44), API_ID44, API_HASH44)
	client44.add_event_handler(me_handler)
	client44.add_event_handler(altarena_moon_handler)
	client44.add_event_handler(altarena_ok_moon_handler)
	client44.add_event_handler(alts_quest_arenas_moon_handler)
	client44.add_event_handler(bichos_alts_moon_handler)
	client44.add_event_handler(check_acc_moon_handler)
	client44.add_event_handler(check_accounts_moon_handler)
	client44.add_event_handler(check_state_moon_handler)
	client44.add_event_handler(foray_handler)
	client44.add_event_handler(gp_handler)
	client44.add_event_handler(orders_handler)
	client44.add_event_handler(quests_handler)
	client44.add_event_handler(spend_and_hide_handler)
	client44.add_event_handler(spend_hide_moon_handler)
	client44.add_event_handler(tlg_handler)
	client44.add_event_handler(full_quests_handler)

client45 = None
if API_ID45 and API_HASH45 and STRING_SESSION45:
	client45 = TelegramClient(StringSession(STRING_SESSION45), API_ID45, API_HASH45)
	client45.add_event_handler(me_handler)
	client45.add_event_handler(altarena_moon_handler)
	client45.add_event_handler(altarena_ok_moon_handler)
	client45.add_event_handler(alts_quest_arenas_moon_handler)
	client45.add_event_handler(bichos_alts_moon_handler)
	client45.add_event_handler(check_acc_moon_handler)
	client45.add_event_handler(check_accounts_moon_handler)
	client45.add_event_handler(check_state_moon_handler)
	client45.add_event_handler(foray_handler)
	client45.add_event_handler(gp_handler)
	client45.add_event_handler(orders_handler)
	client45.add_event_handler(quests_handler)
	client45.add_event_handler(spend_and_hide_handler)
	client45.add_event_handler(spend_hide_moon_handler)
	client45.add_event_handler(tlg_handler)
	client45.add_event_handler(full_quests_handler)

client46 = None
if API_ID46 and API_HASH46 and STRING_SESSION46:
	client46 = TelegramClient(StringSession(STRING_SESSION46), API_ID46, API_HASH46)
	client46.add_event_handler(me_handler)
	client46.add_event_handler(altarena_moon_handler)
	client46.add_event_handler(altarena_ok_moon_handler)
	client46.add_event_handler(alts_quest_arenas_moon_handler)
	client46.add_event_handler(bichos_alts_moon_handler)
	client46.add_event_handler(check_acc_moon_handler)
	client46.add_event_handler(check_accounts_moon_handler)
	client46.add_event_handler(check_state_moon_handler)
	client46.add_event_handler(foray_handler)
	client46.add_event_handler(gp_handler)
	client46.add_event_handler(orders_handler)
	client46.add_event_handler(quests_handler)
	client46.add_event_handler(spend_and_hide_handler)
	client46.add_event_handler(spend_hide_moon_handler)
	client46.add_event_handler(tlg_handler)
	client46.add_event_handler(full_quests_handler)

client47 = None
if API_ID47 and API_HASH47 and STRING_SESSION47:
	client47 = TelegramClient(StringSession(STRING_SESSION47), API_ID47, API_HASH47)
	client47.add_event_handler(me_handler)
	client47.add_event_handler(altarena_moon_handler)
	client47.add_event_handler(altarena_ok_moon_handler)
	client47.add_event_handler(alts_quest_arenas_moon_handler)
	client47.add_event_handler(bichos_alts_moon_handler)
	client47.add_event_handler(check_acc_moon_handler)
	client47.add_event_handler(check_accounts_moon_handler)
	client47.add_event_handler(check_state_moon_handler)
	client47.add_event_handler(foray_handler)
	client47.add_event_handler(gp_handler)
	client47.add_event_handler(orders_handler)
	client47.add_event_handler(quests_handler)
	client47.add_event_handler(spend_and_hide_handler)
	client47.add_event_handler(spend_hide_moon_handler)
	client47.add_event_handler(tlg_handler)
	client47.add_event_handler(full_quests_handler)

client48 = None
if API_ID48 and API_HASH48 and STRING_SESSION48:
	client48 = TelegramClient(StringSession(STRING_SESSION48), API_ID48, API_HASH48)
	client48.add_event_handler(me_handler)
	client48.add_event_handler(altarena_moon_handler)
	client48.add_event_handler(altarena_ok_moon_handler)
	client48.add_event_handler(alts_quest_arenas_moon_handler)
	client48.add_event_handler(bichos_alts_moon_handler)
	client48.add_event_handler(check_acc_moon_handler)
	client48.add_event_handler(check_accounts_moon_handler)
	client48.add_event_handler(check_state_moon_handler)
	client48.add_event_handler(foray_handler)
	client48.add_event_handler(gp_handler)
	client48.add_event_handler(orders_handler)
	client48.add_event_handler(quests_handler)
	client48.add_event_handler(spend_and_hide_handler)
	client48.add_event_handler(spend_hide_moon_handler)
	client48.add_event_handler(tlg_handler)
	client48.add_event_handler(full_quests_handler)

client49 = None
if API_ID49 and API_HASH49 and STRING_SESSION49:
	client49 = TelegramClient(StringSession(STRING_SESSION49), API_ID49, API_HASH49)
	client49.add_event_handler(me_handler)
	client49.add_event_handler(altarena_moon_handler)
	client49.add_event_handler(altarena_ok_moon_handler)
	client49.add_event_handler(alts_quest_arenas_moon_handler)
	client49.add_event_handler(bichos_alts_moon_handler)
	client49.add_event_handler(check_acc_moon_handler)
	client49.add_event_handler(check_accounts_moon_handler)
	client49.add_event_handler(check_state_moon_handler)
	client49.add_event_handler(foray_handler)
	client49.add_event_handler(gp_handler)
	client49.add_event_handler(orders_handler)
	client49.add_event_handler(quests_handler)
	client49.add_event_handler(spend_and_hide_handler)
	client49.add_event_handler(spend_hide_moon_handler)
	client49.add_event_handler(tlg_handler)
	client49.add_event_handler(full_quests_handler)

client50 = None
if API_ID50 and API_HASH50 and STRING_SESSION50:
	client50 = TelegramClient(StringSession(STRING_SESSION50), API_ID50, API_HASH50)
	client50.add_event_handler(me_handler)
	client50.add_event_handler(altarena_moon_handler)
	client50.add_event_handler(altarena_ok_moon_handler)
	client50.add_event_handler(alts_quest_arenas_moon_handler)
	client50.add_event_handler(bichos_alts_moon_handler)
	client50.add_event_handler(check_acc_moon_handler)
	client50.add_event_handler(check_accounts_moon_handler)
	client50.add_event_handler(check_state_moon_handler)
	client50.add_event_handler(foray_handler)
	client50.add_event_handler(gp_handler)
	client50.add_event_handler(orders_handler)
	client50.add_event_handler(quests_handler)
	client50.add_event_handler(spend_and_hide_handler)
	client50.add_event_handler(spend_hide_moon_handler)
	client50.add_event_handler(tlg_handler)
	client50.add_event_handler(full_quests_handler)

client51 = None
if API_ID51 and API_HASH51 and STRING_SESSION51:
	client51 = TelegramClient(StringSession(STRING_SESSION51), API_ID51, API_HASH51)
	client51.add_event_handler(me_handler)
	client51.add_event_handler(altarena_moon_handler)
	client51.add_event_handler(altarena_ok_moon_handler)
	client51.add_event_handler(alts_quest_arenas_moon_handler)
	client51.add_event_handler(bichos_alts_moon_handler)
	client51.add_event_handler(check_acc_moon_handler)
	client51.add_event_handler(check_accounts_moon_handler)
	client51.add_event_handler(check_state_moon_handler)
	client51.add_event_handler(foray_handler)
	client51.add_event_handler(gp_handler)
	client51.add_event_handler(orders_handler)
	client51.add_event_handler(quests_handler)
	client51.add_event_handler(spend_and_hide_handler)
	client51.add_event_handler(spend_hide_moon_handler)
	client51.add_event_handler(tlg_handler)
	client51.add_event_handler(full_quests_handler)

client52 = None
if API_ID52 and API_HASH52 and STRING_SESSION52:
	client52 = TelegramClient(StringSession(STRING_SESSION52), API_ID52, API_HASH52)
	client52.add_event_handler(me_handler)
	client52.add_event_handler(altarena_moon_handler)
	client52.add_event_handler(altarena_ok_moon_handler)
	client52.add_event_handler(alts_quest_arenas_moon_handler)
	client52.add_event_handler(bichos_alts_moon_handler)
	client52.add_event_handler(check_acc_moon_handler)
	client52.add_event_handler(check_accounts_moon_handler)
	client52.add_event_handler(check_state_moon_handler)
	client52.add_event_handler(foray_handler)
	client52.add_event_handler(gp_handler)
	client52.add_event_handler(orders_handler)
	client52.add_event_handler(quests_handler)
	client52.add_event_handler(spend_and_hide_handler)
	client52.add_event_handler(spend_hide_moon_handler)
	client52.add_event_handler(tlg_handler)
	client52.add_event_handler(full_quests_handler)

client53 = None
if API_ID53 and API_HASH53 and STRING_SESSION53:
	client53 = TelegramClient(StringSession(STRING_SESSION53), API_ID53, API_HASH53)
	client53.add_event_handler(me_handler)
	client53.add_event_handler(altarena_moon_handler)
	client53.add_event_handler(altarena_ok_moon_handler)
	client53.add_event_handler(alts_quest_arenas_moon_handler)
	client53.add_event_handler(bichos_alts_moon_handler)
	client53.add_event_handler(check_acc_moon_handler)
	client53.add_event_handler(check_accounts_moon_handler)
	client53.add_event_handler(check_state_moon_handler)
	client53.add_event_handler(foray_handler)
	client53.add_event_handler(gp_handler)
	client53.add_event_handler(orders_handler)
	client53.add_event_handler(quests_handler)
	client53.add_event_handler(spend_and_hide_handler)
	client53.add_event_handler(spend_hide_moon_handler)
	client53.add_event_handler(tlg_handler)
	client53.add_event_handler(full_quests_handler)

client54 = None
if API_ID54 and API_HASH54 and STRING_SESSION54:
	client54 = TelegramClient(StringSession(STRING_SESSION54), API_ID54, API_HASH54)
	client54.add_event_handler(me_handler)
	client54.add_event_handler(altarena_moon_handler)
	client54.add_event_handler(altarena_ok_moon_handler)
	client54.add_event_handler(alts_quest_arenas_moon_handler)
	client54.add_event_handler(bichos_alts_moon_handler)
	client54.add_event_handler(check_acc_moon_handler)
	client54.add_event_handler(check_accounts_moon_handler)
	client54.add_event_handler(check_state_moon_handler)
	client54.add_event_handler(foray_handler)
	client54.add_event_handler(gp_handler)
	client54.add_event_handler(orders_handler)
	client54.add_event_handler(quests_handler)
	client54.add_event_handler(spend_and_hide_handler)
	client54.add_event_handler(spend_hide_moon_handler)
	client54.add_event_handler(tlg_handler)
	client54.add_event_handler(full_quests_handler)

client55 = None
if API_ID55 and API_HASH55 and STRING_SESSION55:
	client55 = TelegramClient(StringSession(STRING_SESSION55), API_ID55, API_HASH55)
	client55.add_event_handler(me_handler)
	client55.add_event_handler(altarena_moon_handler)
	client55.add_event_handler(altarena_ok_moon_handler)
	client55.add_event_handler(alts_quest_arenas_moon_handler)
	client55.add_event_handler(bichos_alts_moon_handler)
	client55.add_event_handler(check_acc_moon_handler)
	client55.add_event_handler(check_accounts_moon_handler)
	client55.add_event_handler(check_state_moon_handler)
	client55.add_event_handler(foray_handler)
	client55.add_event_handler(gp_handler)
	client55.add_event_handler(orders_handler)
	client55.add_event_handler(quests_handler)
	client55.add_event_handler(spend_and_hide_handler)
	client55.add_event_handler(spend_hide_moon_handler)
	client55.add_event_handler(tlg_handler)
	client55.add_event_handler(full_quests_handler)

client56 = None
if API_ID56 and API_HASH56 and STRING_SESSION56:
	client56 = TelegramClient(StringSession(STRING_SESSION56), API_ID56, API_HASH56)
	client56.add_event_handler(me_handler)
	client56.add_event_handler(altarena_moon_handler)
	client56.add_event_handler(altarena_ok_moon_handler)
	client56.add_event_handler(alts_quest_arenas_moon_handler)
	client56.add_event_handler(bichos_alts_moon_handler)
	client56.add_event_handler(check_acc_moon_handler)
	client56.add_event_handler(check_accounts_moon_handler)
	client56.add_event_handler(check_state_moon_handler)
	client56.add_event_handler(foray_handler)
	client56.add_event_handler(gp_handler)
	client56.add_event_handler(orders_handler)
	client56.add_event_handler(quests_handler)
	client56.add_event_handler(spend_and_hide_handler)
	client56.add_event_handler(spend_hide_moon_handler)
	client56.add_event_handler(tlg_handler)
	client56.add_event_handler(full_quests_handler)

client57 = None
if API_ID57 and API_HASH57 and STRING_SESSION57:
	client57 = TelegramClient(StringSession(STRING_SESSION57), API_ID57, API_HASH57)
	client57.add_event_handler(me_handler)
	client57.add_event_handler(altarena_moon_handler)
	client57.add_event_handler(altarena_ok_moon_handler)
	client57.add_event_handler(alts_quest_arenas_moon_handler)
	client57.add_event_handler(bichos_alts_moon_handler)
	client57.add_event_handler(check_acc_moon_handler)
	client57.add_event_handler(check_accounts_moon_handler)
	client57.add_event_handler(check_state_moon_handler)
	client57.add_event_handler(foray_handler)
	client57.add_event_handler(gp_handler)
	client57.add_event_handler(orders_handler)
	client57.add_event_handler(quests_handler)
	client57.add_event_handler(spend_and_hide_handler)
	client57.add_event_handler(spend_hide_moon_handler)
	client57.add_event_handler(tlg_handler)
	client57.add_event_handler(full_quests_handler)

client58 = None
if API_ID58 and API_HASH58 and STRING_SESSION58:
	client58 = TelegramClient(StringSession(STRING_SESSION58), API_ID58, API_HASH58)
	client58.add_event_handler(me_handler)
	client58.add_event_handler(altarena_moon_handler)
	client58.add_event_handler(altarena_ok_moon_handler)
	client58.add_event_handler(alts_quest_arenas_moon_handler)
	client58.add_event_handler(bichos_alts_moon_handler)
	client58.add_event_handler(check_acc_moon_handler)
	client58.add_event_handler(check_accounts_moon_handler)
	client58.add_event_handler(check_state_moon_handler)
	client58.add_event_handler(foray_handler)
	client58.add_event_handler(gp_handler)
	client58.add_event_handler(orders_handler)
	client58.add_event_handler(quests_handler)
	client58.add_event_handler(spend_and_hide_handler)
	client58.add_event_handler(spend_hide_moon_handler)
	client58.add_event_handler(tlg_handler)
	client58.add_event_handler(full_quests_handler)

client59 = None
if API_ID59 and API_HASH59 and STRING_SESSION59:
	client59 = TelegramClient(StringSession(STRING_SESSION59), API_ID59, API_HASH59)
	client59.add_event_handler(me_handler)
	client59.add_event_handler(altarena_moon_handler)
	client59.add_event_handler(altarena_ok_moon_handler)
	client59.add_event_handler(alts_quest_arenas_moon_handler)
	client59.add_event_handler(bichos_alts_moon_handler)
	client59.add_event_handler(check_acc_moon_handler)
	client59.add_event_handler(check_accounts_moon_handler)
	client59.add_event_handler(check_state_moon_handler)
	client59.add_event_handler(foray_handler)
	client59.add_event_handler(gp_handler)
	client59.add_event_handler(orders_handler)
	client59.add_event_handler(quests_handler)
	client59.add_event_handler(spend_and_hide_handler)
	client59.add_event_handler(spend_hide_moon_handler)
	client59.add_event_handler(tlg_handler)
	client59.add_event_handler(full_quests_handler)

client60 = None
if API_ID60 and API_HASH60 and STRING_SESSION60:
	client60 = TelegramClient(StringSession(STRING_SESSION60), API_ID60, API_HASH60)
	client60.add_event_handler(me_handler)
	client60.add_event_handler(altarena_moon_handler)
	client60.add_event_handler(altarena_ok_moon_handler)
	client60.add_event_handler(alts_quest_arenas_moon_handler)
	client60.add_event_handler(bichos_alts_moon_handler)
	client60.add_event_handler(check_acc_moon_handler)
	client60.add_event_handler(check_accounts_moon_handler)
	client60.add_event_handler(check_state_moon_handler)
	client60.add_event_handler(foray_handler)
	client60.add_event_handler(gp_handler)
	client60.add_event_handler(orders_handler)
	client60.add_event_handler(quests_handler)
	client60.add_event_handler(spend_and_hide_handler)
	client60.add_event_handler(spend_hide_moon_handler)
	client60.add_event_handler(tlg_handler)
	client60.add_event_handler(full_quests_handler)

client61 = None
if API_ID61 and API_HASH61 and STRING_SESSION61:
	client61 = TelegramClient(StringSession(STRING_SESSION61), API_ID61, API_HASH61)
	client61.add_event_handler(me_handler)
	client61.add_event_handler(altarena_moon_handler)
	client61.add_event_handler(altarena_ok_moon_handler)
	client61.add_event_handler(alts_quest_arenas_moon_handler)
	client61.add_event_handler(bichos_alts_moon_handler)
	client61.add_event_handler(check_acc_moon_handler)
	client61.add_event_handler(check_accounts_moon_handler)
	client61.add_event_handler(check_state_moon_handler)
	client61.add_event_handler(foray_handler)
	client61.add_event_handler(gp_handler)
	client61.add_event_handler(orders_handler)
	client61.add_event_handler(quests_handler)
	client61.add_event_handler(spend_and_hide_handler)
	client61.add_event_handler(spend_hide_moon_handler)
	client61.add_event_handler(tlg_handler)
	client61.add_event_handler(full_quests_handler)

client62 = None
if API_ID62 and API_HASH62 and STRING_SESSION62:
	client62 = TelegramClient(StringSession(STRING_SESSION62), API_ID62, API_HASH62)
	client62.add_event_handler(me_handler)
	client62.add_event_handler(altarena_moon_handler)
	client62.add_event_handler(altarena_ok_moon_handler)
	client62.add_event_handler(alts_quest_arenas_moon_handler)
	client62.add_event_handler(bichos_alts_moon_handler)
	client62.add_event_handler(check_acc_moon_handler)
	client62.add_event_handler(check_accounts_moon_handler)
	client62.add_event_handler(check_state_moon_handler)
	client62.add_event_handler(foray_handler)
	client62.add_event_handler(gp_handler)
	client62.add_event_handler(orders_handler)
	client62.add_event_handler(quests_handler)
	client62.add_event_handler(spend_and_hide_handler)
	client62.add_event_handler(spend_hide_moon_handler)
	client62.add_event_handler(tlg_handler)
	client62.add_event_handler(full_quests_handler)

client63 = None
if API_ID63 and API_HASH63 and STRING_SESSION63:
	client63 = TelegramClient(StringSession(STRING_SESSION63), API_ID63, API_HASH63)
	client63.add_event_handler(me_handler)
	client63.add_event_handler(altarena_moon_handler)
	client63.add_event_handler(altarena_ok_moon_handler)
	client63.add_event_handler(alts_quest_arenas_moon_handler)
	client63.add_event_handler(bichos_alts_moon_handler)
	client63.add_event_handler(check_acc_moon_handler)
	client63.add_event_handler(check_accounts_moon_handler)
	client63.add_event_handler(check_state_moon_handler)
	client63.add_event_handler(foray_handler)
	client63.add_event_handler(gp_handler)
	client63.add_event_handler(orders_handler)
	client63.add_event_handler(quests_handler)
	client63.add_event_handler(spend_and_hide_handler)
	client63.add_event_handler(spend_hide_moon_handler)
	client63.add_event_handler(tlg_handler)
	client63.add_event_handler(full_quests_handler)

client64 = None
if API_ID64 and API_HASH64 and STRING_SESSION64:
	client64 = TelegramClient(StringSession(STRING_SESSION64), API_ID64, API_HASH64)
	client64.add_event_handler(me_handler)
	client64.add_event_handler(altarena_moon_handler)
	client64.add_event_handler(altarena_ok_moon_handler)
	client64.add_event_handler(alts_quest_arenas_moon_handler)
	client64.add_event_handler(bichos_alts_moon_handler)
	client64.add_event_handler(check_acc_moon_handler)
	client64.add_event_handler(check_accounts_moon_handler)
	client64.add_event_handler(check_state_moon_handler)
	client64.add_event_handler(foray_handler)
	client64.add_event_handler(gp_handler)
	client64.add_event_handler(orders_handler)
	client64.add_event_handler(quests_handler)
	client64.add_event_handler(spend_and_hide_handler)
	client64.add_event_handler(spend_hide_moon_handler)
	client64.add_event_handler(tlg_handler)
	client64.add_event_handler(full_quests_handler)

client65 = None
if API_ID65 and API_HASH65 and STRING_SESSION65:
	client65 = TelegramClient(StringSession(STRING_SESSION65), API_ID65, API_HASH65)
	client65.add_event_handler(me_handler)
	client65.add_event_handler(altarena_moon_handler)
	client65.add_event_handler(altarena_ok_moon_handler)
	client65.add_event_handler(alts_quest_arenas_moon_handler)
	client65.add_event_handler(bichos_alts_moon_handler)
	client65.add_event_handler(check_acc_moon_handler)
	client65.add_event_handler(check_accounts_moon_handler)
	client65.add_event_handler(check_state_moon_handler)
	client65.add_event_handler(foray_handler)
	client65.add_event_handler(gp_handler)
	client65.add_event_handler(orders_handler)
	client65.add_event_handler(quests_handler)
	client65.add_event_handler(spend_and_hide_handler)
	client65.add_event_handler(spend_hide_moon_handler)
	client65.add_event_handler(tlg_handler)
	client65.add_event_handler(full_quests_handler)

client66 = None
if API_ID66 and API_HASH66 and STRING_SESSION66:
	client66 = TelegramClient(StringSession(STRING_SESSION66), API_ID66, API_HASH66)
	client66.add_event_handler(me_handler)
	client66.add_event_handler(altarena_moon_handler)
	client66.add_event_handler(altarena_ok_moon_handler)
	client66.add_event_handler(alts_quest_arenas_moon_handler)
	client66.add_event_handler(bichos_alts_moon_handler)
	client66.add_event_handler(check_acc_moon_handler)
	client66.add_event_handler(check_accounts_moon_handler)
	client66.add_event_handler(check_state_moon_handler)
	client66.add_event_handler(foray_handler)
	client66.add_event_handler(gp_handler)
	client66.add_event_handler(orders_handler)
	client66.add_event_handler(quests_handler)
	client66.add_event_handler(spend_and_hide_handler)
	client66.add_event_handler(spend_hide_moon_handler)
	client66.add_event_handler(tlg_handler)
	client66.add_event_handler(full_quests_handler)

client67 = None
if API_ID67 and API_HASH67 and STRING_SESSION67:
	client67 = TelegramClient(StringSession(STRING_SESSION67), API_ID67, API_HASH67)
	client67.add_event_handler(me_handler)
	client67.add_event_handler(altarena_moon_handler)
	client67.add_event_handler(altarena_ok_moon_handler)
	client67.add_event_handler(alts_quest_arenas_moon_handler)
	client67.add_event_handler(bichos_alts_moon_handler)
	client67.add_event_handler(check_acc_moon_handler)
	client67.add_event_handler(check_accounts_moon_handler)
	client67.add_event_handler(check_state_moon_handler)
	client67.add_event_handler(foray_handler)
	client67.add_event_handler(gp_handler)
	client67.add_event_handler(orders_handler)
	client67.add_event_handler(quests_handler)
	client67.add_event_handler(spend_and_hide_handler)
	client67.add_event_handler(spend_hide_moon_handler)
	client67.add_event_handler(tlg_handler)
	client67.add_event_handler(full_quests_handler)

client68 = None
if API_ID68 and API_HASH68 and STRING_SESSION68:
	client68 = TelegramClient(StringSession(STRING_SESSION68), API_ID68, API_HASH68)
	client68.add_event_handler(me_handler)
	client68.add_event_handler(altarena_moon_handler)
	client68.add_event_handler(altarena_ok_moon_handler)
	client68.add_event_handler(alts_quest_arenas_moon_handler)
	client68.add_event_handler(bichos_alts_moon_handler)
	client68.add_event_handler(check_acc_moon_handler)
	client68.add_event_handler(check_accounts_moon_handler)
	client68.add_event_handler(check_state_moon_handler)
	client68.add_event_handler(foray_handler)
	client68.add_event_handler(gp_handler)
	client68.add_event_handler(orders_handler)
	client68.add_event_handler(quests_handler)
	client68.add_event_handler(spend_and_hide_handler)
	client68.add_event_handler(spend_hide_moon_handler)
	client68.add_event_handler(tlg_handler)
	client68.add_event_handler(full_quests_handler)

client69 = None
if API_ID69 and API_HASH69 and STRING_SESSION69:
	client69 = TelegramClient(StringSession(STRING_SESSION69), API_ID69, API_HASH69)
	client69.add_event_handler(me_handler)
	client69.add_event_handler(altarena_moon_handler)
	client69.add_event_handler(altarena_ok_moon_handler)
	client69.add_event_handler(alts_quest_arenas_moon_handler)
	client69.add_event_handler(bichos_alts_moon_handler)
	client69.add_event_handler(check_acc_moon_handler)
	client69.add_event_handler(check_accounts_moon_handler)
	client69.add_event_handler(check_state_moon_handler)
	client69.add_event_handler(foray_handler)
	client69.add_event_handler(gp_handler)
	client69.add_event_handler(orders_handler)
	client69.add_event_handler(quests_handler)
	client69.add_event_handler(spend_and_hide_handler)
	client69.add_event_handler(spend_hide_moon_handler)
	client69.add_event_handler(tlg_handler)
	client69.add_event_handler(full_quests_handler)

client70 = None
if API_ID70 and API_HASH70 and STRING_SESSION70:
	client70 = TelegramClient(StringSession(STRING_SESSION70), API_ID70, API_HASH70)
	client70.add_event_handler(me_handler)
	client70.add_event_handler(altarena_moon_handler)
	client70.add_event_handler(altarena_ok_moon_handler)
	client70.add_event_handler(alts_quest_arenas_moon_handler)
	client70.add_event_handler(bichos_alts_moon_handler)
	client70.add_event_handler(check_acc_moon_handler)
	client70.add_event_handler(check_accounts_moon_handler)
	client70.add_event_handler(check_state_moon_handler)
	client70.add_event_handler(foray_handler)
	client70.add_event_handler(gp_handler)
	client70.add_event_handler(orders_handler)
	client70.add_event_handler(quests_handler)
	client70.add_event_handler(spend_and_hide_handler)
	client70.add_event_handler(spend_hide_moon_handler)
	client70.add_event_handler(tlg_handler)
	client70.add_event_handler(full_quests_handler)

client71 = None
if API_ID71 and API_HASH71 and STRING_SESSION71:
	client71 = TelegramClient(StringSession(STRING_SESSION71), API_ID71, API_HASH71)
	client71.add_event_handler(me_handler)
	client71.add_event_handler(altarena_moon_handler)
	client71.add_event_handler(altarena_ok_moon_handler)
	client71.add_event_handler(alts_quest_arenas_moon_handler)
	client71.add_event_handler(bichos_alts_moon_handler)
	client71.add_event_handler(check_acc_moon_handler)
	client71.add_event_handler(check_accounts_moon_handler)
	client71.add_event_handler(check_state_moon_handler)
	client71.add_event_handler(foray_handler)
	client71.add_event_handler(gp_handler)
	client71.add_event_handler(orders_handler)
	client71.add_event_handler(quests_handler)
	client71.add_event_handler(spend_and_hide_handler)
	client71.add_event_handler(spend_hide_moon_handler)
	client71.add_event_handler(tlg_handler)
	client71.add_event_handler(full_quests_handler)

client72 = None
if API_ID72 and API_HASH72 and STRING_SESSION72:
	client72 = TelegramClient(StringSession(STRING_SESSION72), API_ID72, API_HASH72)
	client72.add_event_handler(me_handler)
	client72.add_event_handler(altarena_moon_handler)
	client72.add_event_handler(altarena_ok_moon_handler)
	client72.add_event_handler(alts_quest_arenas_moon_handler)
	client72.add_event_handler(bichos_alts_moon_handler)
	client72.add_event_handler(check_acc_moon_handler)
	client72.add_event_handler(check_accounts_moon_handler)
	client72.add_event_handler(check_state_moon_handler)
	client72.add_event_handler(foray_handler)
	client72.add_event_handler(gp_handler)
	client72.add_event_handler(orders_handler)
	client72.add_event_handler(quests_handler)
	client72.add_event_handler(spend_and_hide_handler)
	client72.add_event_handler(spend_hide_moon_handler)
	client72.add_event_handler(tlg_handler)
	client72.add_event_handler(full_quests_handler)

client73 = None
if API_ID73 and API_HASH73 and STRING_SESSION73:
	client73 = TelegramClient(StringSession(STRING_SESSION73), API_ID73, API_HASH73)
	client73.add_event_handler(me_handler)
	client73.add_event_handler(altarena_moon_handler)
	client73.add_event_handler(altarena_ok_moon_handler)
	client73.add_event_handler(alts_quest_arenas_moon_handler)
	client73.add_event_handler(bichos_alts_moon_handler)
	client73.add_event_handler(check_acc_moon_handler)
	client73.add_event_handler(check_accounts_moon_handler)
	client73.add_event_handler(check_state_moon_handler)
	client73.add_event_handler(foray_handler)
	client73.add_event_handler(gp_handler)
	client73.add_event_handler(orders_handler)
	client73.add_event_handler(quests_handler)
	client73.add_event_handler(spend_and_hide_handler)
	client73.add_event_handler(spend_hide_moon_handler)
	client73.add_event_handler(tlg_handler)
	client73.add_event_handler(full_quests_handler)

client74 = None
if API_ID74 and API_HASH74 and STRING_SESSION74:
	client74 = TelegramClient(StringSession(STRING_SESSION74), API_ID74, API_HASH74)
	client74.add_event_handler(me_handler)
	client74.add_event_handler(altarena_moon_handler)
	client74.add_event_handler(altarena_ok_moon_handler)
	client74.add_event_handler(alts_quest_arenas_moon_handler)
	client74.add_event_handler(bichos_alts_moon_handler)
	client74.add_event_handler(check_acc_moon_handler)
	client74.add_event_handler(check_accounts_moon_handler)
	client74.add_event_handler(check_state_moon_handler)
	client74.add_event_handler(foray_handler)
	client74.add_event_handler(gp_handler)
	client74.add_event_handler(orders_handler)
	client74.add_event_handler(quests_handler)
	client74.add_event_handler(spend_and_hide_handler)
	client74.add_event_handler(spend_hide_moon_handler)
	client74.add_event_handler(tlg_handler)
	client74.add_event_handler(full_quests_handler)

client75 = None
if API_ID75 and API_HASH75 and STRING_SESSION75:
	client75 = TelegramClient(StringSession(STRING_SESSION75), API_ID75, API_HASH75)
	client75.add_event_handler(me_handler)
	client75.add_event_handler(altarena_moon_handler)
	client75.add_event_handler(altarena_ok_moon_handler)
	client75.add_event_handler(alts_quest_arenas_moon_handler)
	client75.add_event_handler(bichos_alts_moon_handler)
	client75.add_event_handler(check_acc_moon_handler)
	client75.add_event_handler(check_accounts_moon_handler)
	client75.add_event_handler(check_state_moon_handler)
	client75.add_event_handler(foray_handler)
	client75.add_event_handler(gp_handler)
	client75.add_event_handler(orders_handler)
	client75.add_event_handler(quests_handler)
	client75.add_event_handler(spend_and_hide_handler)
	client75.add_event_handler(spend_hide_moon_handler)
	client75.add_event_handler(tlg_handler)
	client75.add_event_handler(full_quests_handler)

client76 = None
if API_ID76 and API_HASH76 and STRING_SESSION76:
	client76 = TelegramClient(StringSession(STRING_SESSION76), API_ID76, API_HASH76)
	client76.add_event_handler(me_handler)
	client76.add_event_handler(altarena_moon_handler)
	client76.add_event_handler(altarena_ok_moon_handler)
	client76.add_event_handler(alts_quest_arenas_moon_handler)
	client76.add_event_handler(bichos_alts_moon_handler)
	client76.add_event_handler(check_acc_moon_handler)
	client76.add_event_handler(check_accounts_moon_handler)
	client76.add_event_handler(check_state_moon_handler)
	client76.add_event_handler(foray_handler)
	client76.add_event_handler(gp_handler)
	client76.add_event_handler(orders_handler)
	client76.add_event_handler(quests_handler)
	client76.add_event_handler(spend_and_hide_handler)
	client76.add_event_handler(spend_hide_moon_handler)
	client76.add_event_handler(tlg_handler)
	client76.add_event_handler(full_quests_handler)

client77 = None
if API_ID77 and API_HASH77 and STRING_SESSION77:
	client77 = TelegramClient(StringSession(STRING_SESSION77), API_ID77, API_HASH77)
	client77.add_event_handler(me_handler)
	client77.add_event_handler(altarena_moon_handler)
	client77.add_event_handler(altarena_ok_moon_handler)
	client77.add_event_handler(alts_quest_arenas_moon_handler)
	client77.add_event_handler(bichos_alts_moon_handler)
	client77.add_event_handler(check_acc_moon_handler)
	client77.add_event_handler(check_accounts_moon_handler)
	client77.add_event_handler(check_state_moon_handler)
	client77.add_event_handler(foray_handler)
	client77.add_event_handler(gp_handler)
	client77.add_event_handler(orders_handler)
	client77.add_event_handler(quests_handler)
	client77.add_event_handler(spend_and_hide_handler)
	client77.add_event_handler(spend_hide_moon_handler)
	client77.add_event_handler(tlg_handler)
	client77.add_event_handler(full_quests_handler)

client78 = None
if API_ID78 and API_HASH78 and STRING_SESSION78:
	client78 = TelegramClient(StringSession(STRING_SESSION78), API_ID78, API_HASH78)
	client78.add_event_handler(me_handler)
	client78.add_event_handler(altarena_moon_handler)
	client78.add_event_handler(altarena_ok_moon_handler)
	client78.add_event_handler(alts_quest_arenas_moon_handler)
	client78.add_event_handler(bichos_alts_moon_handler)
	client78.add_event_handler(check_acc_moon_handler)
	client78.add_event_handler(check_accounts_moon_handler)
	client78.add_event_handler(check_state_moon_handler)
	client78.add_event_handler(foray_handler)
	client78.add_event_handler(gp_handler)
	client78.add_event_handler(orders_handler)
	client78.add_event_handler(quests_handler)
	client78.add_event_handler(spend_and_hide_handler)
	client78.add_event_handler(spend_hide_moon_handler)
	client78.add_event_handler(tlg_handler)
	client78.add_event_handler(full_quests_handler)

client79 = None
if API_ID79 and API_HASH79 and STRING_SESSION79:
	client79 = TelegramClient(StringSession(STRING_SESSION79), API_ID79, API_HASH79)
	client79.add_event_handler(me_handler)
	client79.add_event_handler(altarena_moon_handler)
	client79.add_event_handler(altarena_ok_moon_handler)
	client79.add_event_handler(alts_quest_arenas_moon_handler)
	client79.add_event_handler(bichos_alts_moon_handler)
	client79.add_event_handler(check_acc_moon_handler)
	client79.add_event_handler(check_accounts_moon_handler)
	client79.add_event_handler(check_state_moon_handler)
	client79.add_event_handler(foray_handler)
	client79.add_event_handler(gp_handler)
	client79.add_event_handler(orders_handler)
	client79.add_event_handler(quests_handler)
	client79.add_event_handler(spend_and_hide_handler)
	client79.add_event_handler(spend_hide_moon_handler)
	client79.add_event_handler(tlg_handler)
	client79.add_event_handler(full_quests_handler)

client80 = None
if API_ID80 and API_HASH80 and STRING_SESSION80:
	client80 = TelegramClient(StringSession(STRING_SESSION80), API_ID80, API_HASH80)
	client80.add_event_handler(me_handler)
	client80.add_event_handler(altarena_moon_handler)
	client80.add_event_handler(altarena_ok_moon_handler)
	client80.add_event_handler(alts_quest_arenas_moon_handler)
	client80.add_event_handler(bichos_alts_moon_handler)
	client80.add_event_handler(check_acc_moon_handler)
	client80.add_event_handler(check_accounts_moon_handler)
	client80.add_event_handler(check_state_moon_handler)
	client80.add_event_handler(foray_handler)
	client80.add_event_handler(gp_handler)
	client80.add_event_handler(orders_handler)
	client80.add_event_handler(quests_handler)
	client80.add_event_handler(spend_and_hide_handler)
	client80.add_event_handler(spend_hide_moon_handler)
	client80.add_event_handler(tlg_handler)
	client80.add_event_handler(full_quests_handler)

client81 = None
if API_ID81 and API_HASH81 and STRING_SESSION81:
	client81 = TelegramClient(StringSession(STRING_SESSION81), API_ID81, API_HASH81)
	client81.add_event_handler(me_handler)
	client81.add_event_handler(altarena_moon_handler)
	client81.add_event_handler(altarena_ok_moon_handler)
	client81.add_event_handler(alts_quest_arenas_moon_handler)
	client81.add_event_handler(bichos_alts_moon_handler)
	client81.add_event_handler(check_acc_moon_handler)
	client81.add_event_handler(check_accounts_moon_handler)
	client81.add_event_handler(check_state_moon_handler)
	client81.add_event_handler(foray_handler)
	client81.add_event_handler(gp_handler)
	client81.add_event_handler(orders_handler)
	client81.add_event_handler(quests_handler)
	client81.add_event_handler(spend_and_hide_handler)
	client81.add_event_handler(spend_hide_moon_handler)
	client81.add_event_handler(tlg_handler)
	client81.add_event_handler(full_quests_handler)

client82 = None
if API_ID82 and API_HASH82 and STRING_SESSION82:
	client82 = TelegramClient(StringSession(STRING_SESSION82), API_ID82, API_HASH82)
	client82.add_event_handler(me_handler)
	client82.add_event_handler(altarena_moon_handler)
	client82.add_event_handler(altarena_ok_moon_handler)
	client82.add_event_handler(alts_quest_arenas_moon_handler)
	client82.add_event_handler(bichos_alts_moon_handler)
	client82.add_event_handler(check_acc_moon_handler)
	client82.add_event_handler(check_accounts_moon_handler)
	client82.add_event_handler(check_state_moon_handler)
	client82.add_event_handler(foray_handler)
	client82.add_event_handler(gp_handler)
	client82.add_event_handler(orders_handler)
	client82.add_event_handler(quests_handler)
	client82.add_event_handler(spend_and_hide_handler)
	client82.add_event_handler(spend_hide_moon_handler)
	client82.add_event_handler(tlg_handler)
	client82.add_event_handler(full_quests_handler)

client83 = None
if API_ID83 and API_HASH83 and STRING_SESSION83:
	client83 = TelegramClient(StringSession(STRING_SESSION83), API_ID83, API_HASH83)
	client83.add_event_handler(me_handler)
	client83.add_event_handler(altarena_moon_handler)
	client83.add_event_handler(altarena_ok_moon_handler)
	client83.add_event_handler(alts_quest_arenas_moon_handler)
	client83.add_event_handler(bichos_alts_moon_handler)
	client83.add_event_handler(check_acc_moon_handler)
	client83.add_event_handler(check_accounts_moon_handler)
	client83.add_event_handler(check_state_moon_handler)
	client83.add_event_handler(foray_handler)
	client83.add_event_handler(gp_handler)
	client83.add_event_handler(orders_handler)
	client83.add_event_handler(quests_handler)
	client83.add_event_handler(spend_and_hide_handler)
	client83.add_event_handler(spend_hide_moon_handler)
	client83.add_event_handler(tlg_handler)
	client83.add_event_handler(full_quests_handler)

client84 = None
if API_ID84 and API_HASH84 and STRING_SESSION84:
	client84 = TelegramClient(StringSession(STRING_SESSION84), API_ID84, API_HASH84)
	client84.add_event_handler(me_handler)
	client84.add_event_handler(altarena_moon_handler)
	client84.add_event_handler(altarena_ok_moon_handler)
	client84.add_event_handler(alts_quest_arenas_moon_handler)
	client84.add_event_handler(bichos_alts_moon_handler)
	client84.add_event_handler(check_acc_moon_handler)
	client84.add_event_handler(check_accounts_moon_handler)
	client84.add_event_handler(check_state_moon_handler)
	client84.add_event_handler(foray_handler)
	client84.add_event_handler(gp_handler)
	client84.add_event_handler(orders_handler)
	client84.add_event_handler(quests_handler)
	client84.add_event_handler(spend_and_hide_handler)
	client84.add_event_handler(spend_hide_moon_handler)
	client84.add_event_handler(tlg_handler)
	client84.add_event_handler(full_quests_handler)

client85 = None
if API_ID85 and API_HASH85 and STRING_SESSION85:
	client85 = TelegramClient(StringSession(STRING_SESSION85), API_ID85, API_HASH85)
	client85.add_event_handler(me_handler)
	client85.add_event_handler(altarena_moon_handler)
	client85.add_event_handler(altarena_ok_moon_handler)
	client85.add_event_handler(alts_quest_arenas_moon_handler)
	client85.add_event_handler(bichos_alts_moon_handler)
	client85.add_event_handler(check_acc_moon_handler)
	client85.add_event_handler(check_accounts_moon_handler)
	client85.add_event_handler(check_state_moon_handler)
	client85.add_event_handler(foray_handler)
	client85.add_event_handler(gp_handler)
	client85.add_event_handler(orders_handler)
	client85.add_event_handler(quests_handler)
	client85.add_event_handler(spend_and_hide_handler)
	client85.add_event_handler(spend_hide_moon_handler)
	client85.add_event_handler(tlg_handler)
	client85.add_event_handler(full_quests_handler)

client86 = None
if API_ID86 and API_HASH86 and STRING_SESSION86:
	client86 = TelegramClient(StringSession(STRING_SESSION86), API_ID86, API_HASH86)
	client86.add_event_handler(me_handler)
	client86.add_event_handler(altarena_moon_handler)
	client86.add_event_handler(altarena_ok_moon_handler)
	client86.add_event_handler(alts_quest_arenas_moon_handler)
	client86.add_event_handler(bichos_alts_moon_handler)
	client86.add_event_handler(check_acc_moon_handler)
	client86.add_event_handler(check_accounts_moon_handler)
	client86.add_event_handler(check_state_moon_handler)
	client86.add_event_handler(foray_handler)
	client86.add_event_handler(gp_handler)
	client86.add_event_handler(orders_handler)
	client86.add_event_handler(quests_handler)
	client86.add_event_handler(spend_and_hide_handler)
	client86.add_event_handler(spend_hide_moon_handler)
	client86.add_event_handler(tlg_handler)
	client86.add_event_handler(full_quests_handler)

client87 = None
if API_ID87 and API_HASH87 and STRING_SESSION87:
	client87 = TelegramClient(StringSession(STRING_SESSION87), API_ID87, API_HASH87)
	client87.add_event_handler(me_handler)
	client87.add_event_handler(altarena_moon_handler)
	client87.add_event_handler(altarena_ok_moon_handler)
	client87.add_event_handler(alts_quest_arenas_moon_handler)
	client87.add_event_handler(bichos_alts_moon_handler)
	client87.add_event_handler(check_acc_moon_handler)
	client87.add_event_handler(check_accounts_moon_handler)
	client87.add_event_handler(check_state_moon_handler)
	client87.add_event_handler(foray_handler)
	client87.add_event_handler(gp_handler)
	client87.add_event_handler(orders_handler)
	client87.add_event_handler(quests_handler)
	client87.add_event_handler(spend_and_hide_handler)
	client87.add_event_handler(spend_hide_moon_handler)
	client87.add_event_handler(tlg_handler)
	client87.add_event_handler(full_quests_handler)

client88 = None
if API_ID88 and API_HASH88 and STRING_SESSION88:
	client88 = TelegramClient(StringSession(STRING_SESSION88), API_ID88, API_HASH88)
	client88.add_event_handler(me_handler)
	client88.add_event_handler(altarena_moon_handler)
	client88.add_event_handler(altarena_ok_moon_handler)
	client88.add_event_handler(alts_quest_arenas_moon_handler)
	client88.add_event_handler(bichos_alts_moon_handler)
	client88.add_event_handler(check_acc_moon_handler)
	client88.add_event_handler(check_accounts_moon_handler)
	client88.add_event_handler(check_state_moon_handler)
	client88.add_event_handler(foray_handler)
	client88.add_event_handler(gp_handler)
	client88.add_event_handler(orders_handler)
	client88.add_event_handler(quests_handler)
	client88.add_event_handler(spend_and_hide_handler)
	client88.add_event_handler(spend_hide_moon_handler)
	client88.add_event_handler(tlg_handler)
	client88.add_event_handler(full_quests_handler)

client89 = None
if API_ID89 and API_HASH89 and STRING_SESSION89:
	client89 = TelegramClient(StringSession(STRING_SESSION89), API_ID89, API_HASH89)
	client89.add_event_handler(me_handler)
	client89.add_event_handler(altarena_moon_handler)
	client89.add_event_handler(altarena_ok_moon_handler)
	client89.add_event_handler(alts_quest_arenas_moon_handler)
	client89.add_event_handler(bichos_alts_moon_handler)
	client89.add_event_handler(check_acc_moon_handler)
	client89.add_event_handler(check_accounts_moon_handler)
	client89.add_event_handler(check_state_moon_handler)
	client89.add_event_handler(foray_handler)
	client89.add_event_handler(gp_handler)
	client89.add_event_handler(orders_handler)
	client89.add_event_handler(quests_handler)
	client89.add_event_handler(spend_and_hide_handler)
	client89.add_event_handler(spend_hide_moon_handler)
	client89.add_event_handler(tlg_handler)
	client89.add_event_handler(full_quests_handler)

client90 = None
if API_ID90 and API_HASH90 and STRING_SESSION90:
	client90 = TelegramClient(StringSession(STRING_SESSION90), API_ID90, API_HASH90)
	client90.add_event_handler(me_handler)
	client90.add_event_handler(altarena_moon_handler)
	client90.add_event_handler(altarena_ok_moon_handler)
	client90.add_event_handler(alts_quest_arenas_moon_handler)
	client90.add_event_handler(bichos_alts_moon_handler)
	client90.add_event_handler(check_acc_moon_handler)
	client90.add_event_handler(check_accounts_moon_handler)
	client90.add_event_handler(check_state_moon_handler)
	client90.add_event_handler(foray_handler)
	client90.add_event_handler(gp_handler)
	client90.add_event_handler(orders_handler)
	client90.add_event_handler(quests_handler)
	client90.add_event_handler(spend_and_hide_handler)
	client90.add_event_handler(spend_hide_moon_handler)
	client90.add_event_handler(tlg_handler)
	client90.add_event_handler(full_quests_handler)

client91 = None
if API_ID91 and API_HASH91 and STRING_SESSION91:
	client91 = TelegramClient(StringSession(STRING_SESSION91), API_ID91, API_HASH91)
	client91.add_event_handler(me_handler)
	client91.add_event_handler(altarena_handler)
	client91.add_event_handler(altarena_ok_handler)
	client91.add_event_handler(alts_quest_arenas_handler)
	client91.add_event_handler(bichos_alts_handler)
	client91.add_event_handler(check_acc_handler)
	client91.add_event_handler(check_accounts_handler)
	client91.add_event_handler(check_accounts_valley_handler)
	client91.add_event_handler(check_accounts_swamp_handler)
	client91.add_event_handler(check_state_handler)
	client91.add_event_handler(foray_handler)
	client91.add_event_handler(gp_handler)
	client91.add_event_handler(orders_handler)
	client91.add_event_handler(quests_handler)
	client91.add_event_handler(spend_and_hide_handler)
	client91.add_event_handler(spend_hide_handler)
	client91.add_event_handler(tlg_handler)
	client91.add_event_handler(full_quests_handler)

client92 = None
if API_ID92 and API_HASH92 and STRING_SESSION92:
	client92 = TelegramClient(StringSession(STRING_SESSION92), API_ID92, API_HASH92)
	client92.add_event_handler(me_handler)
	client92.add_event_handler(altarena_handler)
	client92.add_event_handler(altarena_ok_handler)
	client92.add_event_handler(alts_quest_arenas_handler)
	client92.add_event_handler(bichos_alts_handler)
	client92.add_event_handler(check_acc_handler)
	client92.add_event_handler(check_accounts_handler)
	client92.add_event_handler(check_accounts_valley_handler)
	client92.add_event_handler(check_accounts_swamp_handler)
	client92.add_event_handler(check_state_handler)
	client92.add_event_handler(foray_handler)
	client92.add_event_handler(gp_handler)
	client92.add_event_handler(orders_handler)
	client92.add_event_handler(quests_handler)
	client92.add_event_handler(spend_and_hide_handler)
	client92.add_event_handler(spend_hide_handler)
	client92.add_event_handler(tlg_handler)
	client92.add_event_handler(full_quests_handler)

client93 = None
if API_ID93 and API_HASH93 and STRING_SESSION93:
	client93 = TelegramClient(StringSession(STRING_SESSION93), API_ID93, API_HASH93)
	client93.add_event_handler(me_handler)
	client93.add_event_handler(altarena_handler)
	client93.add_event_handler(altarena_ok_handler)
	client93.add_event_handler(alts_quest_arenas_handler)
	client93.add_event_handler(bichos_alts_handler)
	client93.add_event_handler(check_acc_handler)
	client93.add_event_handler(check_accounts_handler)
	client93.add_event_handler(check_accounts_swamp_handler)
	client93.add_event_handler(check_accounts_valley_handler)
	client93.add_event_handler(check_state_handler)
	client93.add_event_handler(foray_handler)
	client93.add_event_handler(gp_handler)
	client93.add_event_handler(orders_handler)
	client93.add_event_handler(quests_handler)
	client93.add_event_handler(spend_and_hide_handler)
	client93.add_event_handler(spend_hide_handler)
	client93.add_event_handler(tlg_handler)
	client93.add_event_handler(full_quests_handler)

client94 = None
if API_ID94 and API_HASH94 and STRING_SESSION94:
	client94 = TelegramClient(StringSession(STRING_SESSION94), API_ID94, API_HASH94)
	client94.add_event_handler(me_handler)
	client94.add_event_handler(altarena_handler)
	client94.add_event_handler(altarena_ok_handler)
	client94.add_event_handler(alts_quest_arenas_handler)
	client94.add_event_handler(bichos_alts_handler)
	client94.add_event_handler(check_acc_handler)
	client94.add_event_handler(check_accounts_handler)
	client94.add_event_handler(check_accounts_swamp_handler)
	client94.add_event_handler(check_accounts_valley_handler)
	client94.add_event_handler(check_state_handler)
	client94.add_event_handler(foray_handler)
	client94.add_event_handler(gp_handler)
	client94.add_event_handler(orders_handler)
	client94.add_event_handler(quests_handler)
	client94.add_event_handler(spend_and_hide_handler)
	client94.add_event_handler(spend_hide_handler)
	client94.add_event_handler(tlg_handler)
	client94.add_event_handler(full_quests_handler)

client95 = None
if API_ID95 and API_HASH95 and STRING_SESSION95:
	client95 = TelegramClient(StringSession(STRING_SESSION95), API_ID95, API_HASH95)
	client95.add_event_handler(me_handler)
	client95.add_event_handler(altarena_handler)
	client95.add_event_handler(altarena_ok_handler)
	client95.add_event_handler(alts_quest_arenas_handler)
	client95.add_event_handler(bichos_alts_handler)
	client95.add_event_handler(check_acc_handler)
	client95.add_event_handler(check_accounts_handler)
	client95.add_event_handler(check_accounts_swamp_handler)
	client95.add_event_handler(check_accounts_valley_handler)
	client95.add_event_handler(check_state_handler)
	client95.add_event_handler(foray_handler)
	client95.add_event_handler(gp_handler)
	client95.add_event_handler(orders_handler)
	client95.add_event_handler(quests_handler)
	client95.add_event_handler(spend_and_hide_handler)
	client95.add_event_handler(spend_hide_handler)
	client95.add_event_handler(tlg_handler)
	client95.add_event_handler(full_quests_handler)

client96 = None
if API_ID96 and API_HASH96 and STRING_SESSION96:
	client96 = TelegramClient(StringSession(STRING_SESSION96), API_ID96, API_HASH96)
	client96.add_event_handler(me_handler)
	client96.add_event_handler(altarena_handler)
	client96.add_event_handler(altarena_ok_handler)
	client96.add_event_handler(alts_quest_arenas_handler)
	client96.add_event_handler(bichos_alts_handler)
	client96.add_event_handler(check_acc_handler)
	client96.add_event_handler(check_accounts_handler)
	client96.add_event_handler(check_accounts_swamp_handler)
	client96.add_event_handler(check_accounts_valley_handler)
	client96.add_event_handler(check_state_handler)
	client96.add_event_handler(foray_handler)
	client96.add_event_handler(gp_handler)
	client96.add_event_handler(orders_handler)
	client96.add_event_handler(quests_handler)
	client96.add_event_handler(spend_and_hide_handler)
	client96.add_event_handler(spend_hide_handler)
	client96.add_event_handler(tlg_handler)
	client96.add_event_handler(full_quests_handler)

client97 = None
if API_ID97 and API_HASH97 and STRING_SESSION97:
	client97 = TelegramClient(StringSession(STRING_SESSION97), API_ID97, API_HASH97)
	client97.add_event_handler(me_handler)
	client97.add_event_handler(altarena_handler)
	client97.add_event_handler(altarena_ok_handler)
	client97.add_event_handler(alts_quest_arenas_handler)
	client97.add_event_handler(bichos_alts_handler)
	client97.add_event_handler(check_acc_handler)
	client97.add_event_handler(check_accounts_handler)
	client97.add_event_handler(check_accounts_swamp_handler)
	client97.add_event_handler(check_accounts_valley_handler)
	client97.add_event_handler(check_state_handler)
	client97.add_event_handler(foray_handler)
	client97.add_event_handler(gp_handler)
	client97.add_event_handler(orders_handler)
	client97.add_event_handler(quests_handler)
	client97.add_event_handler(spend_and_hide_handler)
	client97.add_event_handler(spend_hide_handler)
	client97.add_event_handler(tlg_handler)
	client97.add_event_handler(full_quests_handler)

client98 = None
if API_ID98 and API_HASH98 and STRING_SESSION98:
	client98 = TelegramClient(StringSession(STRING_SESSION98), API_ID98, API_HASH98)
	client98.add_event_handler(me_handler)
	client98.add_event_handler(altarena_handler)
	client98.add_event_handler(altarena_ok_handler)
	client98.add_event_handler(alts_quest_arenas_handler)
	client98.add_event_handler(bichos_alts_handler)
	client98.add_event_handler(check_acc_handler)
	client98.add_event_handler(check_accounts_handler)
	client98.add_event_handler(check_accounts_swamp_handler)
	client98.add_event_handler(check_accounts_valley_handler)
	client98.add_event_handler(check_state_handler)
	client98.add_event_handler(foray_handler)
	client98.add_event_handler(gp_handler)
	client98.add_event_handler(orders_handler)
	client98.add_event_handler(quests_handler)
	client98.add_event_handler(spend_and_hide_handler)
	client98.add_event_handler(spend_hide_handler)
	client98.add_event_handler(tlg_handler)
	client98.add_event_handler(full_quests_handler)

client99 = None
if API_ID99 and API_HASH99 and STRING_SESSION99:
	client99 = TelegramClient(StringSession(STRING_SESSION99), API_ID99, API_HASH99)
	client99.add_event_handler(me_handler)
	client99.add_event_handler(altarena_handler)
	client99.add_event_handler(altarena_ok_handler)
	client99.add_event_handler(alts_quest_arenas_handler)
	client99.add_event_handler(bichos_alts_handler)
	client99.add_event_handler(check_acc_handler)
	client99.add_event_handler(check_accounts_handler)
	client99.add_event_handler(check_accounts_swamp_handler)
	client99.add_event_handler(check_accounts_valley_handler)
	client99.add_event_handler(check_state_handler)
	client99.add_event_handler(foray_handler)
	client99.add_event_handler(gp_handler)
	client99.add_event_handler(orders_handler)
	client99.add_event_handler(quests_handler)
	client99.add_event_handler(spend_and_hide_handler)
	client99.add_event_handler(spend_hide_handler)
	client99.add_event_handler(tlg_handler)
	client99.add_event_handler(full_quests_handler)

client100 = None
if API_ID100 and API_HASH100 and STRING_SESSION100:
	client100 = TelegramClient(StringSession(STRING_SESSION100), API_ID100, API_HASH100)
	client100.add_event_handler(me_handler)
	client100.add_event_handler(altarena_handler)
	client100.add_event_handler(altarena_ok_handler)
	client100.add_event_handler(alts_quest_arenas_handler)
	client100.add_event_handler(bichos_alts_handler)
	client100.add_event_handler(check_acc_handler)
	client100.add_event_handler(check_accounts_handler)
	client100.add_event_handler(check_accounts_swamp_handler)
	client100.add_event_handler(check_accounts_valley_handler)
	client100.add_event_handler(check_state_handler)
	client100.add_event_handler(foray_handler)
	client100.add_event_handler(gp_handler)
	client100.add_event_handler(orders_handler)
	client100.add_event_handler(quests_handler)
	client100.add_event_handler(spend_and_hide_handler)
	client100.add_event_handler(spend_hide_handler)
	client100.add_event_handler(tlg_handler)
	client100.add_event_handler(full_quests_handler)

client101 = None
if API_ID101 and API_HASH101 and STRING_SESSION101:
	client101 = TelegramClient(StringSession(STRING_SESSION101), API_ID101, API_HASH101)
	client101.add_event_handler(me_handler)
	client101.add_event_handler(altarena_ok_handler)
	client101.add_event_handler(alts_quest_arenas_handler)
	client101.add_event_handler(bichos_alts_handler)
	client101.add_event_handler(check_state_handler)
	client101.add_event_handler(foray_handler)
	client101.add_event_handler(orders_handler)
	client101.add_event_handler(quests_handler)
	client101.add_event_handler(spend_and_hide_handler)
	client101.add_event_handler(spend_hide_handler)
	client101.add_event_handler(handler_in_g_deposit)
	client101.add_event_handler(handler_in_gdeposit)
	client101.add_event_handler(tlg_handler)
	client101.add_event_handler(trader_handler)

client102 = None
if API_ID102 and API_HASH102 and STRING_SESSION102:
	client102 = TelegramClient(StringSession(STRING_SESSION102), API_ID102, API_HASH102)
	client102.add_event_handler(me_handler)
	client102.add_event_handler(altarena_ok_handler)
	client102.add_event_handler(alts_quest_arenas_handler)
	client102.add_event_handler(bichos_alts_handler)
	client102.add_event_handler(check_state_handler)
	client102.add_event_handler(foray_handler)
	client102.add_event_handler(orders_handler)
	client102.add_event_handler(quests_handler)
	client102.add_event_handler(spend_and_hide_handler)
	client102.add_event_handler(spend_hide_handler)
	client102.add_event_handler(handler_in_g_deposit)
	client102.add_event_handler(handler_in_gdeposit)
	client102.add_event_handler(tlg_handler)
	client102.add_event_handler(trader_handler)

client103 = None
if API_ID103 and API_HASH103 and STRING_SESSION103:
	client103 = TelegramClient(StringSession(STRING_SESSION103), API_ID103, API_HASH103)
	client103.add_event_handler(me_handler)
	client103.add_event_handler(altarena_ok_handler)
	client103.add_event_handler(alts_quest_arenas_handler)
	client103.add_event_handler(bichos_alts_handler)
	client103.add_event_handler(check_state_handler)
	client103.add_event_handler(foray_handler)
	client103.add_event_handler(orders_handler)
	client103.add_event_handler(quests_handler)
	client103.add_event_handler(spend_and_hide_handler)
	client103.add_event_handler(spend_hide_handler)
	client103.add_event_handler(handler_in_g_deposit)
	client103.add_event_handler(handler_in_gdeposit)
	client103.add_event_handler(tlg_handler)
	client103.add_event_handler(trader_handler)

client104 = None
if API_ID104 and API_HASH104 and STRING_SESSION104:
	client104 = TelegramClient(StringSession(STRING_SESSION104), API_ID104, API_HASH104)
	client104.add_event_handler(me_handler)
	client104.add_event_handler(altarena_ok_handler)
	client104.add_event_handler(alts_quest_arenas_handler)
	client104.add_event_handler(bichos_alts_handler)
	client104.add_event_handler(check_state_handler)
	client104.add_event_handler(foray_handler)
	client104.add_event_handler(orders_handler)
	client104.add_event_handler(quests_handler)
	client104.add_event_handler(spend_and_hide_handler)
	client104.add_event_handler(spend_hide_handler)
	client104.add_event_handler(handler_in_g_deposit)
	client104.add_event_handler(handler_in_gdeposit)
	client104.add_event_handler(tlg_handler)
	client104.add_event_handler(trader_handler)

client105 = None
if API_ID105 and API_HASH105 and STRING_SESSION105:
	client105 = TelegramClient(StringSession(STRING_SESSION105), API_ID105, API_HASH105)
	client105.add_event_handler(me_handler)
	client105.add_event_handler(altarena_ok_handler)
	client105.add_event_handler(alts_quest_arenas_handler)
	client105.add_event_handler(bichos_alts_handler)
	client105.add_event_handler(check_state_handler)
	client105.add_event_handler(foray_handler)
	client105.add_event_handler(orders_handler)
	client105.add_event_handler(quests_handler)
	client105.add_event_handler(spend_and_hide_handler)
	client105.add_event_handler(spend_hide_handler)
	client105.add_event_handler(handler_in_g_deposit)
	client105.add_event_handler(handler_in_gdeposit)
	client105.add_event_handler(tlg_handler)
	client105.add_event_handler(trader_handler)

client106 = None
if API_ID106 and API_HASH106 and STRING_SESSION106:
	client106 = TelegramClient(StringSession(STRING_SESSION106), API_ID106, API_HASH106)
	client106.add_event_handler(me_handler)
	client106.add_event_handler(altarena_ok_handler)
	client106.add_event_handler(alts_quest_arenas_handler)
	client106.add_event_handler(bichos_alts_handler)
	client106.add_event_handler(check_state_handler)
	client106.add_event_handler(foray_handler)
	client106.add_event_handler(orders_handler)
	client106.add_event_handler(quests_handler)
	client106.add_event_handler(spend_and_hide_handler)
	client106.add_event_handler(spend_hide_handler)
	client106.add_event_handler(handler_in_g_deposit)
	client106.add_event_handler(handler_in_gdeposit)
	client106.add_event_handler(tlg_handler)
	client106.add_event_handler(trader_handler)

client107 = None
if API_ID107 and API_HASH107 and STRING_SESSION107:
	client107 = TelegramClient(StringSession(STRING_SESSION107), API_ID107, API_HASH107)
	client107.add_event_handler(me_handler)
	client107.add_event_handler(altarena_ok_handler)
	client107.add_event_handler(alts_quest_arenas_handler)
	client107.add_event_handler(bichos_alts_handler)
	client107.add_event_handler(check_state_handler)
	client107.add_event_handler(foray_handler)
	client107.add_event_handler(orders_handler)
	client107.add_event_handler(quests_handler)
	client107.add_event_handler(spend_and_hide_handler)
	client107.add_event_handler(spend_hide_handler)
	client107.add_event_handler(handler_in_g_deposit)
	client107.add_event_handler(handler_in_gdeposit)
	client107.add_event_handler(tlg_handler)
	client107.add_event_handler(trader_handler)

client108 = None
if API_ID108 and API_HASH108 and STRING_SESSION108:
	client108 = TelegramClient(StringSession(STRING_SESSION108), API_ID108, API_HASH108)
	client108.add_event_handler(me_handler)
	client108.add_event_handler(altarena_ok_handler)
	client108.add_event_handler(alts_quest_arenas_handler)
	client108.add_event_handler(bichos_alts_handler)
	client108.add_event_handler(check_state_handler)
	client108.add_event_handler(foray_handler)
	client108.add_event_handler(orders_handler)
	client108.add_event_handler(quests_handler)
	client108.add_event_handler(spend_and_hide_handler)
	client108.add_event_handler(spend_hide_handler)
	client108.add_event_handler(handler_in_g_deposit)
	client108.add_event_handler(handler_in_gdeposit)
	client108.add_event_handler(tlg_handler)
	client108.add_event_handler(trader_handler)

client109 = None
if API_ID109 and API_HASH109 and STRING_SESSION109:
	client109 = TelegramClient(StringSession(STRING_SESSION109), API_ID109, API_HASH109)
	client109.add_event_handler(me_handler)
	client109.add_event_handler(altarena_ok_handler)
	client109.add_event_handler(alts_quest_arenas_handler)
	client109.add_event_handler(bichos_alts_handler)
	client109.add_event_handler(check_state_handler)
	client109.add_event_handler(foray_handler)
	client109.add_event_handler(orders_handler)
	client109.add_event_handler(quests_handler)
	client109.add_event_handler(spend_and_hide_handler)
	client109.add_event_handler(spend_hide_handler)
	client109.add_event_handler(handler_in_g_deposit)
	client109.add_event_handler(handler_in_gdeposit)
	client109.add_event_handler(tlg_handler)
	client109.add_event_handler(trader_handler)

client110 = None
if API_ID110 and API_HASH110 and STRING_SESSION110:
	client110 = TelegramClient(StringSession(STRING_SESSION110), API_ID110, API_HASH110)
	client110.add_event_handler(me_handler)
	client110.add_event_handler(altarena_ok_handler)
	client110.add_event_handler(alts_quest_arenas_handler)
	client110.add_event_handler(bichos_alts_handler)
	client110.add_event_handler(check_state_handler)
	client110.add_event_handler(foray_handler)
	client110.add_event_handler(orders_handler)
	client110.add_event_handler(quests_handler)
	client110.add_event_handler(spend_and_hide_handler)
	client110.add_event_handler(spend_hide_handler)
	client110.add_event_handler(handler_in_g_deposit)
	client110.add_event_handler(handler_in_gdeposit)
	client110.add_event_handler(tlg_handler)
	client110.add_event_handler(trader_handler)

client111 = None
if API_ID111 and API_HASH111 and STRING_SESSION111:
	client111 = TelegramClient(StringSession(STRING_SESSION111), API_ID111, API_HASH111)
	client111.add_event_handler(me_handler)
	client111.add_event_handler(altarena_handler)
	client111.add_event_handler(altarena_ok_handler)
	client111.add_event_handler(alts_quest_arenas_handler)
	client111.add_event_handler(bichos_alts_handler)
	client111.add_event_handler(check_acc_handler)
	client111.add_event_handler(check_accounts_handler)
	client111.add_event_handler(check_accounts_swamp_handler)
	client111.add_event_handler(check_accounts_valley_handler)
	client111.add_event_handler(check_state_handler)
	client111.add_event_handler(foray_handler)
	client111.add_event_handler(gp_handler)
	client111.add_event_handler(orders_handler)
	client111.add_event_handler(quests_handler)
	client111.add_event_handler(spend_and_hide_handler)
	client111.add_event_handler(spend_hide_handler)
	client111.add_event_handler(handler_in_g_deposit)
	client111.add_event_handler(handler_in_gdeposit)
	client111.add_event_handler(tlg_handler)
	client111.add_event_handler(full_quests_handler)

client112 = None
if API_ID112 and API_HASH112 and STRING_SESSION112:
	client112 = TelegramClient(StringSession(STRING_SESSION112), API_ID112, API_HASH112)
	client112.add_event_handler(me_handler)
	client112.add_event_handler(altarena_handler)
	client112.add_event_handler(altarena_ok_handler)
	client112.add_event_handler(alts_quest_arenas_handler)
	client112.add_event_handler(bichos_alts_handler)
	client112.add_event_handler(check_acc_handler)
	client112.add_event_handler(check_accounts_handler)
	client112.add_event_handler(check_accounts_swamp_handler)
	client112.add_event_handler(check_accounts_valley_handler)
	client112.add_event_handler(check_state_handler)
	client112.add_event_handler(foray_handler)
	client112.add_event_handler(gp_handler)
	client112.add_event_handler(orders_handler)
	client112.add_event_handler(quests_handler)
	client112.add_event_handler(spend_and_hide_handler)
	client112.add_event_handler(spend_hide_handler)
	client112.add_event_handler(handler_in_g_deposit)
	client112.add_event_handler(handler_in_gdeposit)
	client112.add_event_handler(tlg_handler)
	client112.add_event_handler(full_quests_handler)

client113 = None
if API_ID113 and API_HASH113 and STRING_SESSION113:
	client113 = TelegramClient(StringSession(STRING_SESSION113), API_ID113, API_HASH113)
	client113.add_event_handler(me_handler)
	client113.add_event_handler(altarena_handler)
	client113.add_event_handler(altarena_ok_handler)
	client113.add_event_handler(alts_quest_arenas_handler)
	client113.add_event_handler(bichos_alts_handler)
	client113.add_event_handler(check_acc_handler)
	client113.add_event_handler(check_accounts_handler)
	client113.add_event_handler(check_accounts_swamp_handler)
	client113.add_event_handler(check_accounts_valley_handler)
	client113.add_event_handler(check_state_handler)
	client113.add_event_handler(gp_handler)
	client113.add_event_handler(orders_handler)
	client113.add_event_handler(quests_handler)
	client113.add_event_handler(spend_and_hide_handler)
	client113.add_event_handler(spend_hide_handler)
	client113.add_event_handler(handler_in_g_deposit)
	client113.add_event_handler(handler_in_gdeposit)
	client113.add_event_handler(tlg_handler)
	client113.add_event_handler(full_quests_handler)

client114 = None
if API_ID114 and API_HASH114 and STRING_SESSION114:
	client114 = TelegramClient(StringSession(STRING_SESSION114), API_ID114, API_HASH114)
	client114.add_event_handler(me_handler)
	client114.add_event_handler(altarena_handler)
	client114.add_event_handler(altarena_ok_handler)
	client114.add_event_handler(alts_quest_arenas_handler)
	client114.add_event_handler(bichos_alts_handler)
	client114.add_event_handler(check_acc_handler)
	client114.add_event_handler(check_accounts_handler)
	client114.add_event_handler(check_accounts_swamp_handler)
	client114.add_event_handler(check_accounts_valley_handler)
	client114.add_event_handler(check_state_handler)
	client114.add_event_handler(foray_handler)
	client114.add_event_handler(gp_handler)
	client114.add_event_handler(orders_handler)
	client114.add_event_handler(quests_handler)
	client114.add_event_handler(spend_and_hide_handler)
	client114.add_event_handler(spend_hide_handler)
	client114.add_event_handler(handler_in_g_deposit)
	client114.add_event_handler(handler_in_gdeposit)
	client114.add_event_handler(tlg_handler)
	client114.add_event_handler(full_quests_handler)

client115 = None
if API_ID115 and API_HASH115 and STRING_SESSION115:
	client115 = TelegramClient(StringSession(STRING_SESSION115), API_ID115, API_HASH115)
	client115.add_event_handler(me_handler)
	client115.add_event_handler(altarena_handler)
	client115.add_event_handler(altarena_ok_handler)
	client115.add_event_handler(alts_quest_arenas_handler)
	client115.add_event_handler(bichos_alts_handler)
	client115.add_event_handler(check_acc_handler)
	client115.add_event_handler(check_accounts_handler)
	client115.add_event_handler(check_accounts_swamp_handler)
	client115.add_event_handler(check_accounts_valley_handler)
	client115.add_event_handler(check_state_handler)
	client115.add_event_handler(foray_handler)
	client115.add_event_handler(gp_handler)
	client115.add_event_handler(orders_handler)
	client115.add_event_handler(quests_handler)
	client115.add_event_handler(spend_and_hide_handler)
	client115.add_event_handler(spend_hide_handler)
	client115.add_event_handler(handler_in_g_deposit)
	client115.add_event_handler(handler_in_gdeposit)
	client115.add_event_handler(tlg_handler)
	client115.add_event_handler(full_quests_handler)

client116 = None
if API_ID116 and API_HASH116 and STRING_SESSION116:
	client116 = TelegramClient(StringSession(STRING_SESSION116), API_ID116, API_HASH116)
	client116.add_event_handler(me_handler)
	client116.add_event_handler(altarena_handler)
	client116.add_event_handler(altarena_ok_handler)
	client116.add_event_handler(alts_quest_arenas_handler)
	client116.add_event_handler(bichos_alts_handler)
	client116.add_event_handler(check_acc_handler)
	client116.add_event_handler(check_accounts_handler)
	client116.add_event_handler(check_accounts_swamp_handler)
	client116.add_event_handler(check_accounts_valley_handler)
	client116.add_event_handler(check_state_handler)
	client116.add_event_handler(foray_handler)
	client116.add_event_handler(gp_handler)
	client116.add_event_handler(orders_handler)
	client116.add_event_handler(quests_handler)
	client116.add_event_handler(spend_and_hide_handler)
	client116.add_event_handler(spend_hide_handler)
	client116.add_event_handler(handler_in_g_deposit)
	client116.add_event_handler(handler_in_gdeposit)
	client116.add_event_handler(tlg_handler)
	client116.add_event_handler(full_quests_handler)

client117 = None
if API_ID117 and API_HASH117 and STRING_SESSION117:
	client117 = TelegramClient(StringSession(STRING_SESSION117), API_ID117, API_HASH117)
	client117.add_event_handler(me_handler)
	client117.add_event_handler(altarena_handler)
	client117.add_event_handler(altarena_ok_handler)
	client117.add_event_handler(alts_quest_arenas_handler)
	client117.add_event_handler(bichos_alts_handler)
	client117.add_event_handler(check_acc_handler)
	client117.add_event_handler(check_accounts_handler)
	client117.add_event_handler(check_accounts_swamp_handler)
	client117.add_event_handler(check_accounts_valley_handler)
	client117.add_event_handler(check_state_handler)
	client117.add_event_handler(foray_handler)
	client117.add_event_handler(gp_handler)
	client117.add_event_handler(orders_handler)
	client117.add_event_handler(quests_handler)
	client117.add_event_handler(spend_and_hide_handler)
	client117.add_event_handler(spend_hide_handler)
	client117.add_event_handler(handler_in_g_deposit)
	client117.add_event_handler(handler_in_gdeposit)
	client117.add_event_handler(tlg_handler)
	client117.add_event_handler(full_quests_handler)

client118 = None
if API_ID118 and API_HASH118 and STRING_SESSION118:
	client118 = TelegramClient(StringSession(STRING_SESSION118), API_ID118, API_HASH118)
	client118.add_event_handler(me_handler)
	client118.add_event_handler(altarena_handler)
	client118.add_event_handler(altarena_ok_handler)
	client118.add_event_handler(alts_quest_arenas_handler)
	client118.add_event_handler(bichos_alts_handler)
	client118.add_event_handler(check_acc_handler)
	client118.add_event_handler(check_accounts_handler)
	client118.add_event_handler(check_accounts_swamp_handler)
	client118.add_event_handler(check_accounts_valley_handler)
	client118.add_event_handler(check_state_handler)
	client118.add_event_handler(foray_handler)
	client118.add_event_handler(gp_handler)
	client118.add_event_handler(orders_handler)
	client118.add_event_handler(quests_handler)
	client118.add_event_handler(spend_and_hide_handler)
	client118.add_event_handler(spend_hide_handler)
	client118.add_event_handler(handler_in_g_deposit)
	client118.add_event_handler(handler_in_gdeposit)
	client118.add_event_handler(tlg_handler)
	client118.add_event_handler(full_quests_handler)

client119 = None
if API_ID119 and API_HASH119 and STRING_SESSION119:
	client119 = TelegramClient(StringSession(STRING_SESSION119), API_ID119, API_HASH119)
	client119.add_event_handler(me_handler)
	client119.add_event_handler(altarena_handler)
	client119.add_event_handler(altarena_ok_handler)
	client119.add_event_handler(alts_quest_arenas_handler)
	client119.add_event_handler(bichos_alts_handler)
	client119.add_event_handler(check_acc_handler)
	client119.add_event_handler(check_accounts_handler)
	client119.add_event_handler(check_accounts_swamp_handler)
	client119.add_event_handler(check_accounts_valley_handler)
	client119.add_event_handler(check_state_handler)
	client119.add_event_handler(foray_handler)
	client119.add_event_handler(gp_handler)
	client119.add_event_handler(orders_handler)
	client119.add_event_handler(quests_handler)
	client119.add_event_handler(spend_and_hide_handler)
	client119.add_event_handler(spend_hide_handler)
	client119.add_event_handler(handler_in_g_deposit)
	client119.add_event_handler(handler_in_gdeposit)
	client119.add_event_handler(tlg_handler)
	client119.add_event_handler(full_quests_handler)

client120 = None
if API_ID120 and API_HASH120 and STRING_SESSION120:
	client120 = TelegramClient(StringSession(STRING_SESSION120), API_ID120, API_HASH120)
	client120.add_event_handler(me_handler)
	client120.add_event_handler(altarena_handler)
	client120.add_event_handler(altarena_ok_handler)
	client120.add_event_handler(alts_quest_arenas_handler)
	client120.add_event_handler(bichos_alts_handler)
	client120.add_event_handler(check_acc_handler)
	client120.add_event_handler(check_accounts_handler)
	client120.add_event_handler(check_accounts_swamp_handler)
	client120.add_event_handler(check_accounts_valley_handler)
	client120.add_event_handler(check_state_handler)
	client120.add_event_handler(foray_handler)
	client120.add_event_handler(gp_handler)
	client120.add_event_handler(orders_handler)
	client120.add_event_handler(quests_handler)
	client120.add_event_handler(spend_and_hide_handler)
	client120.add_event_handler(spend_hide_handler)
	client120.add_event_handler(handler_in_g_deposit)
	client120.add_event_handler(handler_in_gdeposit)
	client120.add_event_handler(tlg_handler)
	client120.add_event_handler(full_quests_handler)

client121 = None
if API_ID121 and API_HASH121 and STRING_SESSION121:
	client121 = TelegramClient(StringSession(STRING_SESSION121), API_ID121, API_HASH121)
	client121.add_event_handler(me_handler)
	client121.add_event_handler(altarena_handler)
	client121.add_event_handler(altarena_ok_handler)
	client121.add_event_handler(alts_quest_arenas_handler)
	client121.add_event_handler(bichos_alts_handler)
	client121.add_event_handler(check_acc_handler)
	client121.add_event_handler(check_accounts_handler)
	client121.add_event_handler(check_accounts_swamp_handler)
	client121.add_event_handler(check_accounts_valley_handler)
	client121.add_event_handler(check_state_handler)
	client121.add_event_handler(foray_handler)
	client121.add_event_handler(gp_handler)
	client121.add_event_handler(orders_handler)
	client121.add_event_handler(quests_handler)
	client121.add_event_handler(spend_and_hide_handler)
	client121.add_event_handler(spend_hide_handler)
	client121.add_event_handler(handler_in_g_deposit)
	client121.add_event_handler(handler_in_gdeposit)
	client121.add_event_handler(tlg_handler)
	client121.add_event_handler(full_quests_handler)

client122 = None
if API_ID122 and API_HASH122 and STRING_SESSION122:
	client122 = TelegramClient(StringSession(STRING_SESSION122), API_ID122, API_HASH122)
	client122.add_event_handler(me_handler)
	client122.add_event_handler(altarena_handler)
	client122.add_event_handler(altarena_ok_handler)
	client122.add_event_handler(alts_quest_arenas_handler)
	client122.add_event_handler(bichos_alts_handler)
	client122.add_event_handler(check_acc_handler)
	client122.add_event_handler(check_accounts_handler)
	client122.add_event_handler(check_accounts_swamp_handler)
	client122.add_event_handler(check_accounts_valley_handler)
	client122.add_event_handler(check_state_handler)
	client122.add_event_handler(foray_handler)
	client122.add_event_handler(gp_handler)
	client122.add_event_handler(orders_handler)
	client122.add_event_handler(quests_handler)
	client122.add_event_handler(spend_and_hide_handler)
	client122.add_event_handler(spend_hide_handler)
	client122.add_event_handler(handler_in_g_deposit)
	client122.add_event_handler(handler_in_gdeposit)
	client122.add_event_handler(tlg_handler)
	client122.add_event_handler(full_quests_handler)

client123 = None
if API_ID123 and API_HASH123 and STRING_SESSION123:
	client123 = TelegramClient(StringSession(STRING_SESSION123), API_ID123, API_HASH123)
	client123.add_event_handler(me_handler)
	client123.add_event_handler(altarena_handler)
	client123.add_event_handler(altarena_ok_handler)
	client123.add_event_handler(alts_quest_arenas_handler)
	client123.add_event_handler(bichos_alts_handler)
	client123.add_event_handler(check_acc_handler)
	client123.add_event_handler(check_accounts_handler)
	client123.add_event_handler(check_accounts_swamp_handler)
	client123.add_event_handler(check_accounts_valley_handler)
	client123.add_event_handler(check_state_handler)
	client123.add_event_handler(gp_handler)
	client123.add_event_handler(orders_handler)
	client123.add_event_handler(quests_handler)
	client123.add_event_handler(spend_and_hide_handler)
	client123.add_event_handler(spend_hide_handler)
	client123.add_event_handler(handler_in_g_deposit)
	client123.add_event_handler(handler_in_gdeposit)
	client123.add_event_handler(tlg_handler)
	client123.add_event_handler(full_quests_handler)

client124 = None
if API_ID124 and API_HASH124 and STRING_SESSION124:
	client124 = TelegramClient(StringSession(STRING_SESSION124), API_ID124, API_HASH124)
	client124.add_event_handler(me_handler)
	client124.add_event_handler(altarena_handler)
	client124.add_event_handler(altarena_ok_handler)
	client124.add_event_handler(alts_quest_arenas_handler)
	client124.add_event_handler(bichos_alts_handler)
	client124.add_event_handler(check_acc_handler)
	client124.add_event_handler(check_accounts_handler)
	client124.add_event_handler(check_accounts_swamp_handler)
	client124.add_event_handler(check_accounts_valley_handler)
	client124.add_event_handler(check_state_handler)
	client124.add_event_handler(foray_handler)
	client124.add_event_handler(gp_handler)
	client124.add_event_handler(orders_handler)
	client124.add_event_handler(quests_handler)
	client124.add_event_handler(spend_and_hide_handler)
	client124.add_event_handler(spend_hide_handler)
	client124.add_event_handler(handler_in_g_deposit)
	client124.add_event_handler(handler_in_gdeposit)
	client124.add_event_handler(tlg_handler)
	client124.add_event_handler(full_quests_handler)

client125 = None
if API_ID125 and API_HASH125 and STRING_SESSION125:
	client125 = TelegramClient(StringSession(STRING_SESSION125), API_ID125, API_HASH125)
	client125.add_event_handler(me_handler)
	client125.add_event_handler(altarena_handler)
	client125.add_event_handler(altarena_ok_handler)
	client125.add_event_handler(alts_quest_arenas_handler)
	client125.add_event_handler(bichos_alts_handler)
	client125.add_event_handler(check_acc_handler)
	client125.add_event_handler(check_accounts_handler)
	client125.add_event_handler(check_accounts_swamp_handler)
	client125.add_event_handler(check_accounts_valley_handler)
	client125.add_event_handler(check_state_handler)
	client125.add_event_handler(foray_handler)
	client125.add_event_handler(gp_handler)
	client125.add_event_handler(orders_handler)
	client125.add_event_handler(quests_handler)
	client125.add_event_handler(spend_and_hide_handler)
	client125.add_event_handler(spend_hide_handler)
	client125.add_event_handler(handler_in_g_deposit)
	client125.add_event_handler(handler_in_gdeposit)
	client125.add_event_handler(tlg_handler)
	client125.add_event_handler(full_quests_handler)

client126 = None
if API_ID126 and API_HASH126 and STRING_SESSION126:
	client126 = TelegramClient(StringSession(STRING_SESSION126), API_ID126, API_HASH126)
	client126.add_event_handler(me_handler)
	client126.add_event_handler(altarena_handler)
	client126.add_event_handler(altarena_ok_handler)
	client126.add_event_handler(alts_quest_arenas_handler)
	client126.add_event_handler(bichos_alts_handler)
	client126.add_event_handler(check_acc_handler)
	client126.add_event_handler(check_accounts_handler)
	client126.add_event_handler(check_accounts_swamp_handler)
	client126.add_event_handler(check_accounts_valley_handler)
	client126.add_event_handler(check_state_handler)
	client126.add_event_handler(foray_handler)
	client126.add_event_handler(gp_handler)
	client126.add_event_handler(orders_handler)
	client126.add_event_handler(quests_handler)
	client126.add_event_handler(spend_and_hide_handler)
	client126.add_event_handler(spend_hide_handler)
	client126.add_event_handler(handler_in_g_deposit)
	client126.add_event_handler(handler_in_gdeposit)
	client126.add_event_handler(tlg_handler)
	client126.add_event_handler(full_quests_handler)

client127 = None
if API_ID127 and API_HASH127 and STRING_SESSION127:
	client127 = TelegramClient(StringSession(STRING_SESSION127), API_ID127, API_HASH127)
	client127.add_event_handler(me_handler)
	client127.add_event_handler(altarena_handler)
	client127.add_event_handler(altarena_ok_handler)
	client127.add_event_handler(alts_quest_arenas_handler)
	client127.add_event_handler(bichos_alts_handler)
	client127.add_event_handler(check_acc_handler)
	client127.add_event_handler(check_accounts_handler)
	client127.add_event_handler(check_accounts_swamp_handler)
	client127.add_event_handler(check_accounts_valley_handler)
	client127.add_event_handler(check_state_handler)
	client127.add_event_handler(foray_handler)
	client127.add_event_handler(gp_handler)
	client127.add_event_handler(orders_handler)
	client127.add_event_handler(quests_handler)
	client127.add_event_handler(spend_and_hide_handler)
	client127.add_event_handler(spend_hide_handler)
	client127.add_event_handler(handler_in_g_deposit)
	client127.add_event_handler(handler_in_gdeposit)
	client127.add_event_handler(tlg_handler)
	client127.add_event_handler(full_quests_handler)

client128 = None
if API_ID128 and API_HASH128 and STRING_SESSION128:
	client128 = TelegramClient(StringSession(STRING_SESSION128), API_ID128, API_HASH128)
	client128.add_event_handler(me_handler)
	client128.add_event_handler(altarena_handler)
	client128.add_event_handler(altarena_ok_handler)
	client128.add_event_handler(alts_quest_arenas_handler)
	client128.add_event_handler(bichos_alts_handler)
	client128.add_event_handler(check_acc_handler)
	client128.add_event_handler(check_accounts_handler)
	client128.add_event_handler(check_accounts_swamp_handler)
	client128.add_event_handler(check_accounts_valley_handler)
	client128.add_event_handler(check_state_handler)
	client128.add_event_handler(foray_handler)
	client128.add_event_handler(gp_handler)
	client128.add_event_handler(orders_handler)
	client128.add_event_handler(quests_handler)
	client128.add_event_handler(spend_and_hide_handler)
	client128.add_event_handler(spend_hide_handler)
	client128.add_event_handler(handler_in_g_deposit)
	client128.add_event_handler(handler_in_gdeposit)
	client128.add_event_handler(tlg_handler)
	client128.add_event_handler(full_quests_handler)

client129 = None
if API_ID129 and API_HASH129 and STRING_SESSION129:
	client129 = TelegramClient(StringSession(STRING_SESSION129), API_ID129, API_HASH129)
	client129.add_event_handler(me_handler)
	client129.add_event_handler(altarena_handler)
	client129.add_event_handler(altarena_ok_handler)
	client129.add_event_handler(alts_quest_arenas_handler)
	client129.add_event_handler(bichos_alts_handler)
	client129.add_event_handler(check_acc_handler)
	client129.add_event_handler(check_accounts_handler)
	client129.add_event_handler(check_accounts_swamp_handler)
	client129.add_event_handler(check_accounts_valley_handler)
	client129.add_event_handler(check_state_handler)
	client129.add_event_handler(foray_handler)
	client129.add_event_handler(gp_handler)
	client129.add_event_handler(orders_handler)
	client129.add_event_handler(quests_handler)
	client129.add_event_handler(spend_and_hide_handler)
	client129.add_event_handler(spend_hide_handler)
	client129.add_event_handler(handler_in_g_deposit)
	client129.add_event_handler(handler_in_gdeposit)
	client129.add_event_handler(tlg_handler)
	client129.add_event_handler(full_quests_handler)

client130 = None
if API_ID130 and API_HASH130 and STRING_SESSION130:
	client130 = TelegramClient(StringSession(STRING_SESSION130), API_ID130, API_HASH130)
	client130.add_event_handler(me_handler)
	client130.add_event_handler(altarena_handler)
	client130.add_event_handler(altarena_ok_handler)
	client130.add_event_handler(alts_quest_arenas_handler)
	client130.add_event_handler(bichos_alts_handler)
	client130.add_event_handler(check_acc_handler)
	client130.add_event_handler(check_accounts_handler)
	client130.add_event_handler(check_accounts_swamp_handler)
	client130.add_event_handler(check_accounts_valley_handler)
	client130.add_event_handler(check_state_handler)
	client130.add_event_handler(foray_handler)
	client130.add_event_handler(gp_handler)
	client130.add_event_handler(orders_handler)
	client130.add_event_handler(quests_handler)
	client130.add_event_handler(spend_and_hide_handler)
	client130.add_event_handler(spend_hide_handler)
	client130.add_event_handler(handler_in_g_deposit)
	client130.add_event_handler(handler_in_gdeposit)
	client130.add_event_handler(tlg_handler)
	client130.add_event_handler(full_quests_handler)

client300 = None
if API_ID300 and API_HASH300 and STRING_SESSION300:
	client300 = TelegramClient(StringSession(STRING_SESSION300), API_ID300, API_HASH300)
	client300.add_event_handler(me_handler)
	client300.add_event_handler(arena_collins_handler)
	client300.add_event_handler(arena_factory_collins_handler)
	client300.add_event_handler(foray_handler)

client301 = None
if API_ID301 and API_HASH301 and STRING_SESSION301:
	client301 = TelegramClient(StringSession(STRING_SESSION301), API_ID301, API_HASH301)
	client301.add_event_handler(me_handler)
	client301.add_event_handler(full_quest2_handler)
	client301.add_event_handler(quest_forest_handler)
	client301.add_event_handler(full_quests_handler)
	client301.add_event_handler(quests_handler)
	client301.add_event_handler(full_quest_handler)
	client301.add_event_handler(full_quest_swamp2_handler)
	client301.add_event_handler(mobs_send_ale_handler)
	client301.add_event_handler(quest_forest_palli_handler)

client302 = None
if API_ID302 and API_HASH302 and STRING_SESSION302:
	client302 = TelegramClient(StringSession(STRING_SESSION302), API_ID302, API_HASH302)
	client302.add_event_handler(me_handler)
	client302.add_event_handler(foray_handler)
	client302.add_event_handler(quests_handler)
	client302.add_event_handler(alts_quest_arenas_handler)
	client302.add_event_handler(full_quests_handler)
	client302.add_event_handler(full_quest_swamp2_handler)
	client302.add_event_handler(spend_and_hide_handler)


client303 = None
if API_ID303 and API_HASH303 and STRING_SESSION303:
	client303 = TelegramClient(StringSession(STRING_SESSION303), API_ID303, API_HASH303)
	client303.add_event_handler(me_handler)
	client303.add_event_handler(foray_handler)
	client303.add_event_handler(trader_handler)
	client303.add_event_handler(trader_rss_handler)
	client303.add_event_handler(recurso_trader_palli_handler)
	client303.add_event_handler(quests_handler)
	client303.add_event_handler(full_quests_handler)
	client303.add_event_handler(full_quest_swamp2_handler)
	client303.add_event_handler(palli_afk_handler)
	client303.add_event_handler(quest_forest_palli_handler)

client304 = None
if API_ID304 and API_HASH304 and STRING_SESSION304:
	client304 = TelegramClient(StringSession(STRING_SESSION304), API_ID304, API_HASH304)
	client304.add_event_handler(me_handler)
	client304.add_event_handler(foray_handler)
	client304.add_event_handler(quests_handler)
	client304.add_event_handler(full_quests_handler)
	client304.add_event_handler(full_quest_swamp2_handler)
	client304.add_event_handler(quest_forest_palli_handler)

client305 = None
if API_ID305 and API_HASH305 and STRING_SESSION305:
	client305 = TelegramClient(StringSession(STRING_SESSION305), API_ID305, API_HASH305)
	client305.add_event_handler(me_handler)
	client305.add_event_handler(full_quest2_handler)
	client305.add_event_handler(quest_forest_handler)
	client305.add_event_handler(full_quests_handler)
	client305.add_event_handler(quests_handler)
	client305.add_event_handler(full_quest_handler)
	client305.add_event_handler(full_quest_swamp2_handler)
	client305.add_event_handler(mobs_send_ale_handler)
	client305.add_event_handler(quest_forest_palli_handler)
	client305.add_event_handler(chris_alch_afk_handler)
	client305.add_event_handler(spend_and_hide_chris_handler)


client306 = None
if API_ID306 and API_HASH306 and STRING_SESSION306:
	client306 = TelegramClient(StringSession(STRING_SESSION306), API_ID306, API_HASH306)
	client306.add_event_handler(me_handler)
	client306.add_event_handler(full_quest2_handler)
	client306.add_event_handler(quest_forest_handler)
	client306.add_event_handler(full_quests_handler)
	client306.add_event_handler(quests_handler)
	client306.add_event_handler(full_quest_handler)
	client306.add_event_handler(full_quest_swamp2_handler)
	client306.add_event_handler(mobs_send_ale_handler)
	client306.add_event_handler(quest_forest_palli_handler)
	client306.add_event_handler(chris_alch_afk_handler)
	client306.add_event_handler(spend_and_hide_chris_handler)

client307 = None
if API_ID307 and API_HASH307 and STRING_SESSION307:
	client307 = TelegramClient(StringSession(STRING_SESSION307), API_ID307, API_HASH307)
	client307.add_event_handler(me_handler)
	client307.add_event_handler(full_quest2_handler)
	client307.add_event_handler(quest_forest_handler)
	client307.add_event_handler(full_quests_handler)
	client307.add_event_handler(quests_handler)
	client307.add_event_handler(full_quest_handler)
	client307.add_event_handler(full_quest_swamp2_handler)
	client307.add_event_handler(mobs_send_ale_handler)
	client307.add_event_handler(foray_handler)
	client307.add_event_handler(trader_handler)



#------------------------------ FIN USER BOT -------------------------------

# Configuro para que se puede usar el bot y el user bot al mismo tiempo.
def loop_a():
    while 1:
        sleep(0.01)
        client1.start()

def loop_b():
    while 1:
        bot_main()


def loop_c():
    while 1:
        sleep(0.01)
        client2.start()


def loop_d():
    while 1:
        sleep(0.01)
        client3.start()


def loop_e():
    while 1:
        sleep(0.01)
        client4.start()


def loop_f():
    while 1:
        sleep(0.01)
        client5.start()


def loop_g():
    while 1:
        sleep(0.01)
        client6.start()


def loop_h():
    while 1:
        sleep(0.01)
        client7.start()

def loop_i():
    while 1:
        sleep(0.01)
        client8.start()

def loop_j():
    while 1:
        sleep(0.01)
        client9.start()

def loop_k():
    while 1:
        sleep(0.01)
        client10.start()

def loop_l():
    while 1:
        sleep(0.01)
        client11.start()

def loop_m():
    while 1:
        sleep(0.01)
        client12.start()

def loop_n():
    while 1:
        sleep(0.01)
        client13.start()

def loop_o():
    while 1:
        sleep(0.01)
        client14.start()

def loop_p():
    while 1:
        sleep(0.01)
        client15.start()

def loop_q():
    while 1:
        sleep(0.01)
        client16.start()

def loop_r():
    while 1:
        sleep(0.01)
        client17.start()

def loop_s():
    while 1:
        sleep(0.01)
        client18.start()

def loop_t():
    while 1:
        sleep(0.01)
        client19.start()


def loop_1():
    while 1:
        sleep(0.01)
        client20.start()


def loop_2():
    while 1:
        sleep(0.01)
        client21.start()


def loop_3():
    while 1:
        sleep(0.01)
        client22.start()


def loop_4():
    while 1:
        sleep(0.01)
        client23.start()


def loop_5():
    while 1:
        sleep(0.01)
        client24.start()


def loop_6():
    while 1:
        sleep(0.01)
        client25.start()


def loop_7():
    while 1:
        sleep(0.01)
        client26.start()


def loop_8():
    while 1:
        sleep(0.01)
        client27.start()


def loop_9():
    while 1:
        sleep(0.01)
        client28.start()


def loop_10():
    while 1:
        sleep(0.01)
        client29.start()


def loop_11():
    while 1:
        sleep(0.01)
        client30.start()


def loop_12():
    while 1:
        sleep(0.01)
        client31.start()


def loop_13():
    while 1:
        sleep(0.01)
        client32.start()


def loop_14():
    while 1:
        sleep(0.01)
        client33.start()


def loop_15():
    while 1:
        sleep(0.01)
        client34.start()


def loop_16():
    while 1:
        sleep(0.01)
        client35.start()


def loop_17():
    while 1:
        sleep(0.01)
        client36.start()


def loop_18():
    while 1:
        sleep(0.01)
        client37.start()


def loop_19():
    while 1:
        sleep(0.01)
        client38.start()


def loop_20():
    while 1:
        sleep(0.01)
        client39.start()


def loop_21():
    while 1:
        sleep(0.01)
        client40.start()

def loop_22():
    while 1:
        sleep(0.01)
        client41.start()

def loop_23():
    while 1:
        sleep(0.01)
        client42.start()

def loop_24():
    while 1:
        sleep(0.01)
        client43.start()

def loop_25():
    while 1:
        sleep(0.01)
        client44.start()

def loop_26():
    while 1:
        sleep(0.01)
        client45.start()

def loop_27():
    while 1:
        sleep(0.01)
        client46.start()

def loop_28():
    while 1:
        sleep(0.01)
        client47.start()

def loop_29():
    while 1:
        sleep(0.01)
        client48.start()

def loop_30():
    while 1:
        sleep(0.01)
        client49.start()

def loop_31():
    while 1:
        sleep(0.01)
        client50.start()

def loop_32():
    while 1:
        sleep(0.01)
        client51.start()

def loop_33():
    while 1:
        sleep(0.01)
        client52.start()

def loop_34():
    while 1:
        sleep(0.01)
        client53.start()

def loop_35():
    while 1:
        sleep(0.01)
        client54.start()

def loop_36():
    while 1:
        sleep(0.01)
        client55.start()

def loop_37():
    while 1:
        sleep(0.01)
        client56.start()

def loop_38():
    while 1:
        sleep(0.01)
        client57.start()

def loop_39():
    while 1:
        sleep(0.01)
        client58.start()

def loop_40():
    while 1:
        sleep(0.01)
        client59.start()

def loop_41():
    while 1:
        sleep(0.01)
        client60.start()

def loop_42():
    while 1:
        sleep(0.01)
        client61.start()

def loop_43():
    while 1:
        sleep(0.01)
        client62.start()

def loop_44():
    while 1:
        sleep(0.01)
        client63.start()

def loop_45():
    while 1:
        sleep(0.01)
        client64.start()

def loop_46():
    while 1:
        sleep(0.01)
        client65.start()

def loop_47():
    while 1:
        sleep(0.01)
        client66.start()

def loop_48():
    while 1:
        sleep(0.01)
        client67.start()

def loop_49():
    while 1:
        sleep(0.01)
        client68.start()

def loop_50():
    while 1:
        sleep(0.01)
        client69.start()

def loop_51():
    while 1:
        sleep(0.01)
        client70.start()

def loop_52():
    while 1:
        sleep(0.01)
        client71.start()

def loop_53():
    while 1:
        sleep(0.01)
        client72.start()

def loop_54():
    while 1:
        sleep(0.01)
        client73.start()

def loop_55():
    while 1:
        sleep(0.01)
        client74.start()

def loop_56():
    while 1:
        sleep(0.01)
        client75.start()

def loop_57():
    while 1:
        sleep(0.01)
        client76.start()

def loop_58():
    while 1:
        sleep(0.01)
        client77.start()

def loop_59():
    while 1:
        sleep(0.01)
        client78.start()

def loop_60():
    while 1:
        sleep(0.01)
        client79.start()

def loop_61():
    while 1:
        sleep(0.01)
        client80.start()

def loop_62():
    while 1:
        sleep(0.01)
        client81.start()

def loop_63():
    while 1:
        sleep(0.01)
        client82.start()

def loop_64():
    while 1:
        sleep(0.01)
        client83.start()

def loop_65():
    while 1:
        sleep(0.01)
        client84.start()

def loop_66():
    while 1:
        sleep(0.01)
        client85.start()

def loop_67():
    while 1:
        sleep(0.01)
        client86.start()

def loop_68():
    while 1:
        sleep(0.01)
        client87.start()

def loop_69():
    while 1:
        sleep(0.01)
        client88.start()

def loop_70():
    while 1:
        sleep(0.01)
        client89.start()

def loop_71():
    while 1:
        sleep(0.01)
        client90.start()

def loop_72():
    while 1:
        sleep(0.01)
        client91.start()

def loop_73():
    while 1:
        sleep(0.01)
        client92.start()

def loop_74():
    while 1:
        sleep(0.01)
        client93.start()

def loop_75():
    while 1:
        sleep(0.01)
        client94.start()

def loop_76():
    while 1:
        sleep(0.01)
        client95.start()

def loop_77():
    while 1:
        sleep(0.01)
        client96.start()

def loop_78():
    while 1:
        sleep(0.01)
        client97.start()

def loop_79():
    while 1:
        sleep(0.01)
        client98.start()

def loop_80():
    while 1:
        sleep(0.01)
        client99.start()

def loop_81():
    while 1:
        sleep(0.01)
        client100.start()

def loop_82():
    while 1:
        sleep(0.01)
        client101.start()

def loop_83():
    while 1:
        sleep(0.01)
        client102.start()

def loop_84():
    while 1:
        sleep(0.01)
        client103.start()

def loop_85():
    while 1:
        sleep(0.01)
        client104.start()

def loop_86():
    while 1:
        sleep(0.01)
        client105.start()

def loop_87():
    while 1:
        sleep(0.01)
        client106.start()

def loop_88():
    while 1:
        sleep(0.01)
        client107.start()

def loop_89():
    while 1:
        sleep(0.01)
        client108.start()

def loop_90():
    while 1:
        sleep(0.01)
        client109.start()

def loop_91():
    while 1:
        sleep(0.01)
        client110.start()

def loop_92():
    while 1:
        sleep(0.01)
        client111.start()

def loop_93():
    while 1:
        sleep(0.01)
        client112.start()

def loop_94():
    while 1:
        sleep(0.01)
        client113.start()

def loop_95():
    while 1:
        sleep(0.01)
        client114.start()

def loop_96():
    while 1:
        sleep(0.01)
        client115.start()

def loop_97():
    while 1:
        sleep(0.01)
        client116.start()

def loop_98():
    while 1:
        sleep(0.01)
        client117.start()

def loop_99():
    while 1:
        sleep(0.01)
        client118.start()

def loop_100():
    while 1:
        sleep(0.01)
        client119.start()

def loop_101():
    while 1:
        sleep(0.01)
        client120.start()


def loop_102():
    while 1:
        sleep(0.01)
        client121.start()

def loop_103():
    while 1:
        sleep(0.01)
        client122.start()

def loop_104():
    while 1:
        sleep(0.01)
        client123.start()

def loop_105():
    while 1:
        sleep(0.01)
        client124.start()

def loop_106():
    while 1:
        sleep(0.01)
        client125.start()

def loop_107():
    while 1:
        sleep(0.01)
        client126.start()

def loop_108():
    while 1:
        sleep(0.01)
        client127.start()

def loop_109():
    while 1:
        sleep(0.01)
        client128.start()

def loop_110():
    while 1:
        sleep(0.01)
        client129.start()

def loop_111():
    while 1:
        sleep(0.01)
        client130.start()

def loop_3000():
    while 1:
        sleep(0.01)
        client300.start()

def loop_3001():
    while 1:
        sleep(0.01)
        client301.start()

def loop_3002():
    while 1:
        sleep(0.01)
        client302.start()

def loop_3003():
    while 1:
        sleep(0.01)
        client303.start()

def loop_3004():
    while 1:
        sleep(0.01)
        client304.start()

def loop_3005():
    while 1:
        sleep(0.01)
        client305.start()

def loop_3006():
    while 1:
        sleep(0.01)
        client306.start()

def loop_3007():
    while 1:
        sleep(0.01)
        client307.start()


if __name__ == '__main__':
		if client1 is not None:
			p1 = Process(target=loop_a).start()
		if BOT_TOKEN is not None:
			p2 = Process(target=loop_b).start()
		if client2 is not None:
			p3 = Process(target=loop_c).start()
		if client3 is not None:
			p4 = Process(target=loop_d).start()
		if client4 is not None:
			p5 = Process(target=loop_e).start()
		if client5 is not None:
			p6 = Process(target=loop_f).start()
		if client6 is not None:
			p7 = Process(target=loop_g).start()
		if client7 is not None:
			p8 = Process(target=loop_h).start()
		if client8 is not None:
			p9 = Process(target=loop_i).start()
		if client9 is not None:
			p10 = Process(target=loop_j).start()
		if client10 is not None:
			p11 = Process(target=loop_k).start()
		if client11 is not None:
			p12 = Process(target=loop_l).start()
		if client12 is not None:
			p13 = Process(target=loop_m).start()
		if client13 is not None:
			p14 = Process(target=loop_n).start()
		if client14 is not None:
			p15 = Process(target=loop_o).start()
		if client15 is not None:
			p16 = Process(target=loop_p).start()
		if client16 is not None:
			p17 = Process(target=loop_q).start()
		if client17 is not None:
			p18 = Process(target=loop_r).start()
		if client18 is not None:
			p19 = Process(target=loop_s).start()
		if client19 is not None:
			p20 = Process(target=loop_t).start()
		if client20 is not None:
			p21 = Process(target=loop_1).start()
		if client21 is not None:
			p22 = Process(target=loop_2).start()
		if client22 is not None:
			p23 = Process(target=loop_3).start()
		if client23 is not None:
			p24 = Process(target=loop_4).start()
		if client24 is not None:
			p25 = Process(target=loop_5).start()
		if client25 is not None:
			p26 = Process(target=loop_6).start()
		if client26 is not None:
			p27 = Process(target=loop_7).start()
		if client27 is not None:
			p28 = Process(target=loop_8).start()
		if client28 is not None:
			p29 = Process(target=loop_9).start()
		if client29 is not None:
			p30 = Process(target=loop_10).start()
		if client30 is not None:
			p31 = Process(target=loop_11).start()
		if client31 is not None:
			p32 = Process(target=loop_12).start()
		if client32 is not None:
			p33 = Process(target=loop_13).start()
		if client33 is not None:
			p34 = Process(target=loop_14).start()
		if client34 is not None:
			p35 = Process(target=loop_15).start()
		if client35 is not None:
			p36 = Process(target=loop_16).start()
		if client36 is not None:
			p37 = Process(target=loop_17).start()
		if client37 is not None:
			p38 = Process(target=loop_18).start()
		if client38 is not None:
			p39 = Process(target=loop_19).start()
		if client39 is not None:
			p40 = Process(target=loop_20).start()
		if client40 is not None:
			p41 = Process(target=loop_21).start()
		if client41 is not None:
			p42 = Process(target=loop_22).start()
		if client42 is not None:
			p43 = Process(target=loop_23).start()
		if client43 is not None:
			p44 = Process(target=loop_24).start()
		if client44 is not None:
			p45 = Process(target=loop_25).start()
		if client45 is not None:
			p46 = Process(target=loop_26).start()
		if client46 is not None:
			p47 = Process(target=loop_27).start()
		if client47 is not None:
			p48 = Process(target=loop_28).start()
		if client48 is not None:
			p49 = Process(target=loop_29).start()
		if client49 is not None:
			p50 = Process(target=loop_30).start()
		if client50 is not None:
			p51 = Process(target=loop_31).start()
		if client51 is not None:
			p52 = Process(target=loop_32).start()
		if client52 is not None:
			p53 = Process(target=loop_33).start()
		if client53 is not None:
			p54 = Process(target=loop_34).start()
		if client54 is not None:
			p55 = Process(target=loop_35).start()
		if client55 is not None:
			p56 = Process(target=loop_36).start()
		if client56 is not None:
			p57 = Process(target=loop_37).start()
		if client57 is not None:
			p58 = Process(target=loop_38).start()
		if client58 is not None:
			p59 = Process(target=loop_39).start()
		if client59 is not None:
			p60 = Process(target=loop_40).start()
		if client60 is not None:
			p61 = Process(target=loop_41).start()
		if client61 is not None:
			p62 = Process(target=loop_42).start()
		if client62 is not None:
			p63 = Process(target=loop_43).start()
		if client63 is not None:
			p64 = Process(target=loop_44).start()
		if client64 is not None:
			p65 = Process(target=loop_45).start()
		if client65 is not None:
			p66 = Process(target=loop_46).start()
		if client66 is not None:
			p67 = Process(target=loop_47).start()
		if client67 is not None:
			p68 = Process(target=loop_48).start()
		if client68 is not None:
			p69 = Process(target=loop_49).start()
		if client69 is not None:
			p70 = Process(target=loop_50).start()
		if client70 is not None:
			p71 = Process(target=loop_51).start()
		if client71 is not None:
			p72 = Process(target=loop_52).start()
		if client72 is not None:
			p73 = Process(target=loop_53).start()
		if client73 is not None:
			p74 = Process(target=loop_54).start()
		if client74 is not None:
			p75 = Process(target=loop_55).start()
		if client75 is not None:
			p76 = Process(target=loop_56).start()
		if client76 is not None:
			p77 = Process(target=loop_57).start()
		if client77 is not None:
			p78 = Process(target=loop_58).start()
		if client78 is not None:
			p79 = Process(target=loop_59).start()
		if client79 is not None:
			p80 = Process(target=loop_60).start()
		if client80 is not None:
			p81 = Process(target=loop_61).start()
		if client81 is not None:
			p82 = Process(target=loop_62).start()
		if client82 is not None:
			p83 = Process(target=loop_63).start()
		if client83 is not None:
			p84 = Process(target=loop_64).start()
		if client84 is not None:
			p85 = Process(target=loop_65).start()
		if client85 is not None:
			p86 = Process(target=loop_66).start()
		if client86 is not None:
			p87 = Process(target=loop_67).start()
		if client87 is not None:
			p88 = Process(target=loop_68).start()
		if client88 is not None:
			p89 = Process(target=loop_69).start()
		if client89 is not None:
			p90 = Process(target=loop_70).start()
		if client90 is not None:
			p91 = Process(target=loop_71).start()
		if client91 is not None:
			p92 = Process(target=loop_72).start()
		if client92 is not None:
			p93 = Process(target=loop_73).start()
		if client93 is not None:
			p94 = Process(target=loop_74).start()
		if client94 is not None:
			p95 = Process(target=loop_75).start()
		if client95 is not None:
			p96 = Process(target=loop_76).start()
		if client96 is not None:
			p97 = Process(target=loop_77).start()
		if client97 is not None:
			p98 = Process(target=loop_78).start()
		if client98 is not None:
			p99 = Process(target=loop_79).start()
		if client99 is not None:
			p100 = Process(target=loop_80).start()
		if client100 is not None:
			p101 = Process(target=loop_81).start()
		if client101 is not None:
			p102 = Process(target=loop_82).start()
		if client102 is not None:
			p103 = Process(target=loop_83).start()
		if client103 is not None:
			p104 = Process(target=loop_84).start()
		if client104 is not None:
			p105 = Process(target=loop_85).start()
		if client105 is not None:
			p106 = Process(target=loop_86).start()
		if client106 is not None:
			p107 = Process(target=loop_87).start()
		if client107 is not None:
			p108 = Process(target=loop_88).start()
		if client108 is not None:
			p109 = Process(target=loop_89).start()
		if client109 is not None:
			p110 = Process(target=loop_90).start()
		if client110 is not None:
			p111 = Process(target=loop_91).start()
		if client111 is not None:
			p112 = Process(target=loop_92).start()
		if client112 is not None:
			p113 = Process(target=loop_93).start()
		if client113 is not None:
			p114 = Process(target=loop_94).start()
		if client114 is not None:
			p115 = Process(target=loop_95).start()
		if client115 is not None:
			p116 = Process(target=loop_96).start()
		if client116 is not None:
			p117 = Process(target=loop_97).start()
		if client117 is not None:
			p118 = Process(target=loop_98).start()
		if client118 is not None:
			p119 = Process(target=loop_99).start()
		if client119 is not None:
			p120 = Process(target=loop_100).start()
		if client120 is not None:
			p121 = Process(target=loop_101).start()
		if client121 is not None:
			p122 = Process(target=loop_102).start()
		if client122 is not None:
			p123 = Process(target=loop_103).start()
		if client123 is not None:
			p124 = Process(target=loop_104).start()
		if client124 is not None:
			p125 = Process(target=loop_105).start()
		if client125 is not None:
			p126 = Process(target=loop_106).start()
		if client126 is not None:
			p127 = Process(target=loop_107).start()
		if client127 is not None:
			p128 = Process(target=loop_108).start()
		if client128 is not None:
			p129 = Process(target=loop_109).start()
		if client129 is not None:
			p130 = Process(target=loop_110).start()
		if client130 is not None:
			p131 = Process(target=loop_111).start()
		if client300 is not None:
			p301 = Process(target=loop_3000).start()
		if client301 is not None:
			p302 = Process(target=loop_3001).start()
		if client302 is not None:
			p303 = Process(target=loop_3002).start()
		if client303 is not None:
			p304 = Process(target=loop_3003).start()
		if client304 is not None:
			p305 = Process(target=loop_3004).start()
		if client305 is not None:
			p306 = Process(target=loop_3005).start()
		if client306 is not None:
			p307 = Process(target=loop_3006).start()
		if client307 is not None:
			p308 = Process(target=loop_3007).start()

