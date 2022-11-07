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
    
client.start()
client.run_until_disconnected()