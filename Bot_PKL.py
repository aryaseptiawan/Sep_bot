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
         WebDriverWait(driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@id='pt1:MA:0:n1:2:pt1:pc21:_vw'])[1]"))).click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "pt1:MA:0:n1:2:pt1:pc21:_clmns"))).click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "pt1:MA:0:n1:2:pt1:pc21:_shwMr"))).click()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "pt1:MA:0:n1:2:pt1:pc21:_shwClmDS::removeall"))).click()
        await asyncio.sleep(1)
        driver.find_element_by_id("pt1:MA:0:n1:2:pt1:pc21:showColsDlg::ok").click()
        await asyncio.sleep(1)
        try:
            zte = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID, "pt1:MA:0:n1:2:pt1:pc21:physicalDeviceHierarchyTreeTable:0:cl22"))).text

            target_id = driver.find_element_by_id("pt1:MA:0:n1:2:pt1:pc21:physicalDeviceHierarchyTreeTable:0:cl22").text.split(" ")[6].split(" ")[0]
            expand = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.ID, "pt1:MA:0:n1:2:pt1:pc21:physicalDeviceHierarchyTreeTable:0::di"))))
            webdriver.ActionChains(driver).move_to_element(expand).click(expand).perform()
            await asyncio.sleep(1)
            expand1 = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "pt1:MA:0:n1:2:pt1:pc21:physicalDeviceHierarchyTreeTable:1::di")))
            webdriver.ActionChains(driver).move_to_element(expand1).click(expand1).perform()
            expand2 = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "pt1:MA:0:n1:2:pt1:pc21:physicalDeviceHierarchyTreeTable:2::di")))
            webdriver.ActionChains(driver).move_to_element(expand2).click(expand2).perform()
            if "1/1/" in hasil:
                try:
                    noport = event.raw_text.split("1/1/")[1].split("/")[0]
                    if " " in noport:
                        raise IndexError
                    lastport = event.raw_text.split('1/1/' + str(noport) + '/')[1].split(" ")[0]
                    if ':' in lastport:
                        lastport = lastport.split(":")[0]
                    if '\n' in lastport:
                        lastport = lastport.split('\n')[0]
                except IndexError:
                    noport = ('1')
                    lastport = event.raw_text.split('1/')[2].split(' ')[0]
                    if ':' in lastport:
                        lastport = lastport.split(":")[0]
                    if '\n' in lastport:
                        lastport = lastport.split('\n')[0]
            else:
                try:
                    noport = event.raw_text.split("1/")[1].split("/")[0]
                    lastport = event.raw_text.split('1/' + str(noport) + '/')[1].split(' ')[0]
                    if ':' in lastport:
                        lastport = lastport.split(":")[0]
                    if '\n' in lastport:
                        lastport = lastport.split('\n')[0]
                except IndexError:
                    try:
                        noport = hasil.split('1/')[1].split("/")[0]
                        if '1' in noport:
                            noport = '11'
                        lastport = event.raw_text.split('1/' + str(noport) + '/')[1].split(' ')[0]
                        if ':' in lastport:
                            lastport = lastport.split(":")[0]
                        if '\n' in lastport:
                            lastport = lastport.split('\n')[0]
                    except IndexError:
                        pass
            if "1-1-" in hasil:
                try:
                    noport = event.raw_text.split("1-1-")[1].split("-")[0]
                    if " " in noport:
                        raise IndexError
                    lastport = event.raw_text.split('1-1-' + str(noport) + '-')[1].split(" ")[0]

                    if ':' in lastport:
                        lastport = lastport.split(":")[0]
                    if '\n' in lastport:
                        lastport = lastport.split('\n')[0]
                except IndexError:
                    noport = ('1')
                    lastport = event.raw_text.split('1-')[2].split(' ')[0]
                    if ':' in lastport:
                        lastport = lastport.split(":")[0]
                    if '\n' in lastport:
                        lastport = lastport.split('\n')[0]
            else:
                try:

                    noport = event.raw_text.split("1-")[1].split("-")[0]
                    lastport = event.raw_text.split('1-' + str(noport) + '-')[1].split(' ')[0]
                    if ':' in lastport:
                        lastport = lastport.split(":")[0]
                    if '\n' in lastport:
                        lastport = lastport.split('\n')[0]
                except IndexError:
                    try:
                        noport = hasil.split('1-')[1].split("-")[0]
                        if '1' in noport:
                            noport = '11'
                        lastport = event.raw_text.split('1-' + str(noport) + '-')[1].split(' ')[0]
                        if ':' in lastport:
                            lastport = lastport.split(":")[0]
                        if '\n' in lastport:
                            lastport = lastport.split('\n')[0]
                    except IndexError:
                        pass
            if 'C300' in zte:
                realport = int(noport) + 3
            else:
                realport = int(noport) + 2
            await asyncio.sleep(2)

            expand3 = WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.ID, "pt1:MA:0:n1:2:pt1:pc21:physicalDeviceHierarchyTreeTable:"+str(realport)+"::di")))
            for list in expand3:
                driver.execute_script("arguments[0].scrollIntoView();", list)
            webdriver.ActionChains(driver).move_to_element(list).click(list).perform()
            await asyncio.sleep(1)
            portnya = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "(//span[contains(text(),'Port-"+str(lastport)+"')])[1]")))
            for list1 in portnya:
                driver.execute_script("arguments[0].scrollIntoView();", list1)
                txt = list1.text
                ok = txt.split('- ')[1]
        except (TimeoutException,UnboundLocalError):
            typing = await client(functions.messages.SetTypingRequest(
                peer=peername,
                action=types.SendMessageTypingAction()
            ))
            await event.reply(message='cek slot port', attributes=typing)
            driver.quit()
            return

        if "mobanmo" in hasil:
            if 'zteg' in hasil:
                sm = hasil.split('zteg')[1].split('\n')[0].strip()
                serialnum = ('zteg' + sm).upper()
                vndr = 'ZTE'
            if 'fhtt' in hasil:
                sm = hasil.split('fhtt')[1].split('\n')[0].strip()
                serialnum = ('fhtt' + sm).upper()
                vndr = 'ZTE'
            if 'hwtc' in hasil:
                sm = hasil.split('hwtc')[1].split('\n')[0].strip()
                serialnum = ('hwtc' + sm).upper()
                vndr = 'HUAWEI'
            if 'alcl' in hasil:
                sm = hasil.split('alcl')[1].split('\n')[0].strip()
                serialnum = ('alcl' + sm).upper()
                vndr = 'ALCATEL'
            try:
                onu = hasil.split(lastport + ':')[1].split(' ')[0]
                if not onu.isdigit():
                    onu = hasil.split(lastport + ':')[1].split('\n')[0]
            except IndexError:
                try:
                    onu = hasil.split(lastport + '/')[1].split(' ')[0]
                    if not onu.isdigit():
                        onu = hasil.split(lastport + '/')[1].split('\n')[0]
                except IndexError:
                    pass
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "pt1:pt_r1:0:d4:0:j_id36"))).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@id='pt1:MA:0:n1:1:pt1:pc1:cb1Create'])[1]"))).click()
            selectont = Select(WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                                           "/html[1]/body[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/select[1]"))))
            selectont.select_by_visible_text('Generic ONT')
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html[1]/body[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[8]/td[2]/input[1]"))).send_keys(onu)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html[1]/body[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[6]/td[2]/input[1]"))).send_keys(
                serialnum)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH,
                 "(//input[@type='text'])[4]"))).send_keys(vndr)
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "(//button[@accesskey='u'])[1]"))).click()
            cpe = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
                (By.XPATH, "(//td[@id='pt1:MA:0:n1:2:pt1:j_id__ctru17pc11::_afrTtxt'])[1]"))).text.split('-')[
                1].strip()
                
client.start()
client.run_until_disconnected()