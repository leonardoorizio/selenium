from selenium import webdriver
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
    return driver
    # Navegar até um site


driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/desafios')
driver.maximize_window()
sleep(2)

janela_inicial = driver.current_window_handle

driver.execute_script('window.scrollTo(0, 2500);')
sleep(2)

botao_abrir = driver.find_element(By.XPATH, '//button[text()="Abrir nova janela"]')
sleep(2)
# caso essa opção de click não funcione, tente com o método driver.execute_script('arguments[0].click();', botao_abrir)
#botao_abrir.click()
driver.execute_script('arguments[0].click();', botao_abrir)

janelas = driver.window_handles

for janela in janelas:
    print(janela)
    if janela not in janela_inicial:
        driver.switch_to.window(janela)
        sleep(2)
        driver.maximize_window()
        sleep(2)
        opniao_sobre_curso = driver.find_element(By.ID, 'opiniao_sobre_curso')
        sleep(2)
        opniao_sobre_curso.send_keys('Ótimo curso!')
        sleep(2)
        botao_pesquisar = driver.find_element(By.ID, 'fazer_pesquisa')
        sleep(2)
        botao_pesquisar.click()
        driver.close()

driver.switch_to.window(janela_inicial)

ultima_opniao = driver.find_element(By.ID, 'campo_desafio7')
ultima_opniao.send_keys('Curso muito bom!')

print('Deu tudo certo!')    

input('')
driver.close()  # Fechar a aba
