import asyncio

import selenium.common.exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from telethon import TelegramClient, events, utils
from selenium import webdriver
# from selenium.webdriver.chrome import webdriver
from telethon.events import StopPropagation
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
import time
import csv
from telethon import functions, types

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
# created by ARYASEPTIAWAN

api_id = 11036912
api_hash = '5499501717:AAGHvy9kFlvTjn_BY1wHfssQBfqhk0_12ok'
# bott = '5268523279:AAG_ALOUSp5SgQKYEbw_RHbYEhj0ZDNf_Rk'
client = TelegramClient('Arya', api_id, api_hash)
phone_number = '+6281231392790'

# @client.on(events.NewMessage(incoming=True, chats=522050610))
@client.on(events.NewMessage( chats=522050610))
async def ipnya(event):
    Username = "29071996"
    Password = "Audi7199"
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_argument('--disable-gpu')
    PATH = Service("C:\Intel\chromedriver.exe")
    driver = webdriver.Chrome(service=PATH, options=chrome_options)
    hasil = event.raw_text.lower()
    name = event.chat_id
    real_id, peer_type = utils.resolve_id(name)
    peername = peer_type(real_id)
    if 'moban' in hasil:
        typing = await client(functions.messages.SetTypingRequest(
            peer=peername,
            action=types.SendMessageTypingAction()
        ))
        try:
            if "172." in hasil:
                await event.reply(message='wait ya', attributes=typing)
                kentang = event.raw_text.split('172.')[1].split("\n")[0]
                if ')' in kentang:
                    kentang = kentang.split(')')[0]
                kentang = ('172.'+kentang)
            kentang = kentang.strip()
        except (IndexError, UnboundLocalError):
            await event.reply(message='IP kosong nih', attributes=typing)
            return
        try:
            if '_internet' in hasil:
                try:
                    inet = hasil.split('_internet')[0].split('\n')[2]
                    noinet = (inet + '_INTERNET')
                except IndexError:
                    try:
                        inet = hasil.split('_internet')[0].split('\n')[1]
                        noinet = (inet + '_INTERNET')
                    except IndexError:
                        try:
                            inet = hasil.split('_internet')[0]
                            noinet = (inet + '_INTERNET')
                        except IndexError:
                            pass
            if '_voice' in hasil:
                try:
                    voice = hasil.split('_voice')[0].split('\n')[2]
                    novoice = (voice + '_VOICE')

                except IndexError:
                    try:
                        voice = hasil.split('_voice')[0].split('\n')[1]
                        novoice = (voice + '_VOICE')

                    except IndexError:
                        try:
                            voice = hasil.split('_voice')[0]
                            novoice = (voice + '_VOICE')
                        except IndexError:
                            pass
            if '_iptv' in hasil:
                try:
                    iptv = hasil.split('_iptv')[0].split('\n')[3]
                    noiptv = (iptv + '_IPTV')
                except IndexError:
                    try:
                        iptv = hasil.split('_iptv')[0].split('\n')[2]
                        noiptv = (iptv + '_IPTV')

                    except IndexError:
                        try:
                            iptv = hasil.split('_iptv')[0].split('\n')[1]
                            noiptv = (iptv + '_IPTV')

                        except IndexError:
                            try:
                                iptv = hasil.split('_iptv')[0]
                                noiptv = (iptv + '_IPTV')

                            except IndexError:
                                pass
                            
client.start()
client.run_until_disconnected()