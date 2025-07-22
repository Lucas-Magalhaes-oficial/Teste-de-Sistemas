from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#configuração do webdriver (nesse exemplo, estamos usando o chrome)
driver = webdriver.Chrome()

#acessa a página de cadastro usando o caminho absoluto com o protocolo file://
#certifique-se de que o caminho está apontando para um arquivo HTML específico

driver.get("file:///C:/Users/lucas_sarmento/Documents/GitHub/Teste-de-Sistemas/index.html")

#preenche o campo Nome
nome_input = driver.find_element(By.ID, "name")
nome_input.send_keys("João da Silva")
time.sleep(1)

#preenche o campo CPF
cpf_input = driver.find_element(By.ID, "cpf")
cpf_input.send_keys("12345678901")
time.sleep(1)

#preenche o campo Endereço
endereco_input = driver.find_element(By.ID, "address")
endereco_input.send_keys("Rua das Flores, 123")
time.sleep(1)

#preenche o campo Telefone
telefone_input = driver.find_element(By.ID, "phone")
telefone_input.send_keys("11987654321")
time.sleep(1)

#clica no botão de Cadastrar
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()


#aguarda um momento para visualizar o resultado (em uma aplicação real, você verificaria a resposta)
time.sleep(8)

#fecha o navegador
#driver.quit