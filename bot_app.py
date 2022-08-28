from turtle import delay
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WhatsappBot:
    def __init__(self):
        self.mensagem = "Olá"
        self.pessoas = ["Mãe"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMsg(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)

        while True:
            for pessoa in self.pessoas:
                if (self.driver.find_element(By.XPATH, "//div[@data-testid='chat-list']")) and (self.driver.find_element(By.CLASS_NAME, "_1pJ9J")):
                    psa = self.driver.find_element(
                        By.XPATH, f"//span[@title='{pessoa}']")
                    time.sleep(1)
                    psa.click()
                    box_text = self.driver.find_element(By.CLASS_NAME, "p3_M1")
                    time.sleep(1)
                    box_text.click()
                    box_text.send_keys(Keys.CONTROL, 'a')
                    box_text.send_keys('Olá')
                    btn_enviar = self.driver.find_element(
                        By.XPATH, "//span[@data-icon='send']")
                    time.sleep(1)
                    btn_enviar.click()

    def LerMSg(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(20)

        for pessoa in self.pessoas:
            psa = self.driver.find_element(
                By.XPATH, f"//span[@title='{pessoa}']")
            time.sleep(1)
            psa.click()
            delay(2)
            self.txt = self.driver.find_element(By.CLASS_NAME, 'message-in')

            for self.aux in self.text:
                print(self.aux.find_element(By.TAG_NAME, 'span'))

            print(self.txt)
            if self.driver.find_element(By.CLASS_NAME, 'message-in'):
                self.text = self.driver.find_element(
                    By.CLASS_NAME, "_1Gy50").text
                print(self.text)


bot = WhatsappBot()

bot.LerMSg()
