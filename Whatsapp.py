print('AUTOMAÇÃO DE MENSAGENS PELO WHATSAPP')
print('-'*50)

import pandas as pd
import time
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Carregando os contatos
contatos_df = pd.read_excel('Contatos.xlsx')
print(contatos_df)
print()

# Abrindo o navegador para leitura do QR Code do Whatsapp
navegador = webdriver.Chrome(ChromeDriverManager().install())
navegador.get('https://web.whatsapp.com')

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

print('\nWhatsapp Web logado\n')

# Enviando as mensagens    
for i, msg in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, 'Pessoa']
    num = contatos_df.loc[i, 'Número']
    texto = urllib.parse.quote(f'Olá {pessoa}! {msg}')
    link = f'https://web.whatsapp.com/send?phone={num}&text={texto}'
    navegador.get(link)
    
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
        
    print(f'\nEnviando a mensagem para {pessoa}\n')
    
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)

navegador.close()
print('\nFim do processo\n')
