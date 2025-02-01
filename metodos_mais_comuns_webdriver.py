from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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
driver.get('https://cursoautomacao.netlify.app/')  # Navegar até um site
driver.maximize_window()  # Maximizar a janela
driver.refresh()  # Atualizar a página
driver.get(driver.current_url)  # Atualizar a página
driver.back()  # Voltar para a página anterior
driver.forward()  # Avançar para a próxima página
print(driver.title)  # Imprimir o título da página
print(driver.current_url)  # Imprimir a url atual
print(driver.page_source)  # Imprimir o código fonte da página
driver.quit()  # Fechar o navegador
# obtem o texto dentro de um elemento
print(driver.find_element(By.XPATH, '//a[@class="navbar-brand"]').text)
print(driver.find_element(
    By.XPATH, '//a[@class="navbar-brand"]').get_attribute('href'))

driver.close()  # Fechar a aba
input('')
