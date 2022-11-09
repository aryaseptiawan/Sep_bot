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
            if 'ncli:' in hasil:
                try:

                    noncli = hasil.split('ncli: ')[1].split('\n')[0].strip()
                    inet = event.raw_text.split('1527')[1].split('\n')[0].strip()
                    noinet = str(noncli + '_1527' + inet + '_INTERNET')
                    voice = event.raw_text.split('0341')[1].split(' ')[0].strip()
                    novoice = str(noncli + '_0341' + voice + '_VOICE')
                    noiptv = str(noncli + '_1527' + inet + '_IPTV')
                except IndexError:
                    try:
                        noncli = hasil.split('ncli: ')[1].split('\n')[0].strip()
                        inet = event.raw_text.split('1527')[1].split(' ')[0].strip()
                        noinet = str(noncli + '_1527' + inet + '_INTERNET')
                        voice = event.raw_text.split('0341')[1].split('\n')[0].strip()
                        novoice = str(noncli + '_0341' + voice + '_VOICE')
                        noiptv = str(noncli + '_1527' + inet + '_IPTV')
                    except IndexError:
                        try:
                            noncli = hasil.split('ncli: ')[1].split('\n')[0].strip()
                            voice = event.raw_text.split('0341')[1].split('\n')[0].strip()
                            novoice = str(noncli + '_0341' + voice + '_VOICE')
                        except IndexError:
                            try:
                                noncli = hasil.split('ncli: ')[1].split('\n')[0].strip()
                                inet = event.raw_text.split('1527')[1].split('\n')[0].strip()
                                noinet = str(noncli + '_1527' + inet + '_INTERNET')
                                noiptv = str(noncli + '_1527' + inet + '_IPTV')
                            except IndexError:
                                pass
            else:
                try:
                    noncli = hasil.split('ncli\n: ')[1].split('\n')[0].strip()
                    inet = event.raw_text.split('1527')[1].split('/')[0].strip()
                    noinet = str(noncli + '_1527' + inet + '_INTERNET')
                    voice = event.raw_text.split('0341')[1].split('\n')[0].strip()
                    novoice = str(noncli + '_0341' + voice + '_VOICE')
                    noiptv = str(noncli + '_1527' + inet + '_IPTV')
                    if not inet.isdigit():
                        noncli = hasil.split('ncli\n: ')[1].split('\n')[0].strip()
                        inet = event.raw_text.split('1527')[1].split('\n')[0].strip()
                        noinet = str(noncli + '_1527' + inet + '_INTERNET')
                        voice = event.raw_text.split('0341')[1].split('/')[0].strip()
                        novoice = str(noncli + '_0341' + voice + '_VOICE')
                        noiptv = str(noncli + '_1527' + inet + '_IPTV')

                except IndexError:
                    try:
                        noncli = hasil.split('ncli : ')[1].split('\n')[0].strip()
                        inet = event.raw_text.split('1527')[1].split('/')[0].strip()
                        noinet = str(noncli + '_1527' + inet + '_INTERNET')
                        voice = event.raw_text.split('0341')[1].split('\n')[0].strip()
                        novoice = str(noncli + '_0341' + voice + '_VOICE')
                        noiptv = str(noncli + '_1527' + inet + '_IPTV')
                        if not inet.isdigit():
                            noncli = hasil.split('ncli : ')[1].split('\n')[0].strip()
                            inet = event.raw_text.split('1527')[1].split('\n')[0].strip()
                            noinet = str(noncli + '_1527' + inet + '_INTERNET')
                            voice = event.raw_text.split('0341')[1].split('/')[0].strip()
                            novoice = str(noncli + '_0341' + voice + '_VOICE')
                            noiptv = str(noncli + '_1527' + inet + '_IPTV')
                        if not voice.isdigit():
                            noncli = hasil.split('ncli : ')[1].split('\n')[0].strip()
                            inet = event.raw_text.split('1527')[1].split('\n')[0].strip()
                            noinet = str(noncli + '_1527' + inet + '_INTERNET')
                            voice = event.raw_text.split('0341')[1].split('\n')[0].strip()
                            novoice = str(noncli + '_0341' + voice + '_VOICE')
                            noiptv = str(noncli + '_1527' + inet + '_IPTV')
                    except IndexError:
                        try:
                            noncli = hasil.split('ncli\n: ')[1].split('\n')[0].strip()
                            voice = event.raw_text.split('0341')[1].split('\n')[0].strip()
                            novoice = str(noncli + '_0341' + voice + '_VOICE')
                        except IndexError:
                            try:
                                noncli = hasil.split('ncli : ')[1].split('\n')[0].strip()
                                voice = event.raw_text.split('0341')[1].split('\n')[0].strip()
                                novoice = str(noncli + '_0341' + voice + '_VOICE')
                            except IndexError:
                                try:
                                    noncli = hasil.split('ncli\n: ')[1].split('\n')[0].strip()
                                    inet = event.raw_text.split('1527')[1].split('\n')[0].strip()
                                    noinet = str(noncli + '_1527' + inet + '_INTERNET')
                                    noiptv = str(noncli + '_1527' + inet + '_IPTV')
                                except IndexError:
                                    try:
                                        noncli = hasil.split('ncli : ')[1].split('\n')[0].strip()
                                        inet = event.raw_text.split('1527')[1].split('\n')[0].strip()
                                        noinet = str(noncli + '_1527' + inet + '_INTERNET')
                                        noiptv = str(noncli + '_1527' + inet + '_IPTV')
                                    except IndexError:
                                        pass
        except IndexError:
            await event.reply(message='cek format', attributes=typing)
            return

        try:
            driver.get("https://nossf-uim.telkom.co.id/Inventory/")
        except WebDriverException:
            typing = await client(functions.messages.SetTypingRequest(
                peer=peername,
                action=types.SendMessageTypingAction()
            ))
            await event.reply(message='GP belum connect', attributes=typing)
            return
        try:
            WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "j_username"))).send_keys(Username)
            driver.find_element_by_name("j_password").send_keys(Password, Keys.ENTER)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "pt1:pt_r1:0:d4:0:j_id36"))).click()
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/form/div[1]/div[2]/div/div[5]/div/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div[3]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[5]/td[4]/table/tbody/tr/td[2]/input'))).send_keys(kentang)
            except UnboundLocalError:
                driver.quit()
                return
            driver.find_element_by_id("pt1:MA:0:n1:1:pt1:sv8:searchButton").click()
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pt1:MA:0:n1:1:pt1:pc1:rtId:0:cl1"]'))).click()
        except (TimeoutException, ConnectionResetError):
            typing = await client(functions.messages.SetTypingRequest(
                peer=peername,
                action=types.SendMessageTypingAction()
            ))
            await event.reply(message='uimnya lemot ni', attributes=typing)
            driver.quit()
            return
        
client.start()
client.run_until_disconnected()