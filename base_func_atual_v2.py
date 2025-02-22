from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


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
    arguments = ['--lang=pt-BR',
                 '--window-size=500,500']  # Removido '--incognito'
    for argument in arguments:
        chrome_options.add_argument(argument)
    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'C:\\Users\\amaro\\OneDrive\\Documentos\\Teste selenium',
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
    return driver
    # Navegar até um site


driver = iniciar_driver()
driver.get('https://app.powerbi.com/groups/2ba90831-03a6-440d-94cc-f72b007458f7/reports/ef2b246c-eca5-4e4c-99b1-18ad38e2de8f/ReportSection15f4e4b1435078c8f7a8?experience=power-bi')
driver.maximize_window()
sleep(5)

campo_login = driver.find_element(By.ID, 'email')
campo_login.click()
campo_login.send_keys('leonardo.orizio@cassol.com.br')
sleep(10)

botao_enviar = driver.find_element(By.ID, 'submitBtn')
botao_enviar.click()
sleep(10)

campo_senha = driver.find_element(By.ID, 'i0118')
campo_senha.click()
#campo_senha.send_keys('#####') #senha
sleep(10)

botao_enviar_2 = driver.find_element(By.ID, 'idSIButton9')
botao_enviar_2.click()
sleep(5)

mensagem_continuar_conectado = driver.find_element(By.ID, 'idSIButton9')
mensagem_continuar_conectado.click()
sleep(10)

elemento_ativador = driver.find_element(By.XPATH, '//div[contains(@class, "scroll-bar-part-bar") and @style = "--bar-color: #605E5C; --bar-color-hover: #605E5C; border-radius: 5px; border: 1px solid white; box-sizing: border-box; width: 1111.64px; height: 9px; transform: translateX(0px);"]')
actions = ActionChains(driver)
actions.move_to_element(elemento_ativador).perform()

botao_expansao = driver.find_element(By.XPATH, '//button[@class="vcMenuBtn"]')
botao_expansao.click()
sleep(5)

botao_exportar = driver.find_element(By.XPATH, '//span[contains(text(), "Exportar dados")]')
botao_exportar.click()
sleep(2)

exportar = driver.find_element(By.XPATH, '//button[contains(text(),"Exportar")]')
exportar.click()
sleep(2)

print('Fim do processo')

input('')