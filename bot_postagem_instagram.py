from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def iniciar_driver():
    # Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e  https://peter.sh/experiments/chromium-command-line-switches/
    chrome_options = Options()
    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    arguments = ['--lang=pt-BR', '--window-size=500,500', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    # inicializando o webdriver
    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait (
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,]

    )

    return driver, wait  
    # Navegar até um site


driver, wait = iniciar_driver()
driver.get('https://www.instagram.com/#')
driver.maximize_window()
sleep(10)

email = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH, '//input[contains(@name, "username")]')))
#email.click()
email.send_keys('lgo.dev.floripa@gmail.com')
sleep(10)

senha = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH, '//input[contains(@name, "password")]')))
#senha.click()
senha.send_keys()
sleep(10)

botao_entrar = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH, '//button[contains(@class, " _acan _acap _acas _aj1- _ap30")]')))
botao_entrar.click()
sleep(10)

while True:
    driver.get('https://www.instagram.com/satoshinakamoto._/')
    sleep(5)
    postagens = wait.until(CondicaoExperada.visibility_of_all_elements_located((By.XPATH, '//div[contains(@class, "_aagu")]')))
    sleep(5)
    postagens[0].click()
    sleep(5)
    elementos_postagem = wait.until(CondicaoExperada.visibility_of_any_elements_located((By.XPATH, '//div[@class="x1lliihq x1n2onr6 xyb1xck"]')))
    sleep(5)
    if len(elementos_postagem) == 20:
        elementos_postagem[0].click()
        sleep(86400)
    else:
        print('postagem já foi curtida')
        sleep(86400)

input('')

# >> Terminar de revisar o código para ficar igual do vídeo