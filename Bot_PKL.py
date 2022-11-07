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


client.start()
client.run_until_disconnected()