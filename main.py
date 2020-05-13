from selenium import webdriver
import time
import urllib.request
from PIL import Image, ImageDraw
import PIL.ImageOps 
import os
import pyautogui
from random import randrange
from textwrap import wrap

class face_bot:

    def __init__(self):
        self.imagem = None
        self.mensagem = None
        self.palavra = 'mulher'
        options = webdriver.FirefoxOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Firefox(executable_path=r'./geckodriver.exe')
        self.palavra_aleatoria()
        self.busca_imagem()
        self.palavra_aleatoria()
        self.get_frase()
        self.escreve()
        self.loga_face()
        self.cria_publicacao()

    def palavra_aleatoria(self):
        self.driver.get('https://www.palabrasaleatorias.com/palavras-aleatorias.php')
        time.sleep(2)
        palavra = self.driver.find_element_by_xpath("//div[@style = 'font-size:3em; color:#6200C5;']").text
        self.palavra = palavra

    def busca_imagem(self):
        self.driver.get('https://www.google.com.br/imghp?hl=pt-BR&tab=wi&authuser=0&ogbl')
        pesquisa = self.driver.find_element_by_xpath("//input[@aria-label='Pesquisar']")
        pesquisa.click()
        pesquisa.send_keys(self.palavra)
        time.sleep(2)
        botao = self.driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']")
        botao.click()
        time.sleep(2)
        img = self.driver.find_elements_by_tag_name('img')
        img_escolhida = randrange(0,len(img))
        url = img[img_escolhida].get_attribute('src')
        print(url)
        try:
            urllib.request.urlretrieve(url, "random.jpg")
        except:
            img_escolhida = randrange(0,len(img))
            url = img[img_escolhida].get_attribute('src')
            urllib.request.urlretrieve(url, "random.jpg")
        time.sleep(5)

    def get_frase(self):
        self.driver.get('https://www.pensador.com')
        busca = self.driver.find_element_by_xpath("//input[@name='q']")
        busca.click()
        busca.send_keys(self.palavra)
        botao = self.driver.find_element_by_xpath("//button[@type='submit']")
        botao.click()
        time.sleep(2)
        frases = self.driver.find_elements_by_xpath("//p[@class='frase fr']")
        quantidade_frases = len(frases)
        frase = randrange(0,int(quantidade_frases))
        valores = frases[frase].text
        valores.split()

        for line in wrap(valores, width = 30):
            print(line)
        
        print(valores)

        self.mensagem = frases[frase].text


    def escreve(self):
        img = Image.open('random.jpg')
        draw = ImageDraw.Draw(img)
        frase = self.mensagem
        draw.text((10,10), frase, fill=(0,0,0))
        img.save('C:/Users/Renna/OneDrive/Área de Trabalho/random.jpg')

    def loga_face(self):
        self.driver.get('https://www.facebook.com/')
        time.sleep(2)
        usuario = self.driver.find_element_by_id('email')
        usuario.click()
        usuario.send_keys('seuemail@hotmail.com')
        senha = self.driver.find_element_by_id('pass')
        senha.click()
        senha.send_keys('suasenha')
        botao = self.driver.find_element_by_xpath("//input[@value='Entrar']")
        botao.click()

    def cria_publicacao(self):
        self.driver.get('link da sua pagina ou perfil do facebook')
        time.sleep(5)
        span = self.driver.find_element_by_xpath("//span[contains(text(), 'Criar publicação')]")
        span.click()
        time.sleep(3)
        btn_img = self.driver.find_element_by_xpath("//img[@class ='hu5pjgll bixrwtb6']")
        btn_img.click()
        time.sleep(2)
        pyautogui.write('random.jpg') 
        pyautogui.press('enter')
        time.sleep(5)
        publicar = self.driver.find_element_by_xpath("//div[contains(text(), 'Publicar')]")
        publicar.click()


h = face_bot()
