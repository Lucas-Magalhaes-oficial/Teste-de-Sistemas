from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#configuração do webdriver (nesse exemplo, estamos usando o chrome)
driver = webdriver.Chrome()

#acessa a página de cadastro usando o caminho absoluto com o protocolo file://
#certifique-se de que o caminho está apontando para um arquivo HTML específico

driver.get("file:///C:/Users/lucas_sarmento/Documents/GitHub/Teste-de-Sistemas/produto.html")

#preenche o campo ID
nome_input = driver.find_element(By.ID, "ID_Produto")
nome_input.send_keys("01")
time.sleep(1)

#preenche o campo Descrição
cpf_input = driver.find_element(By.ID, "descricao")
cpf_input.send_keys("Esponja de Aço")
time.sleep(1)

#preenche o campo Marca
endereco_input = driver.find_element(By.ID, "marca")
endereco_input.send_keys("Bombril")
time.sleep(1)

#preenche o campo Quantidade
telefone_input = driver.find_element(By.ID, "qtd")
telefone_input.send_keys("47")
time.sleep(1)

#preenche o campo Preço
telefone_input = driver.find_element(By.ID, "preco")
telefone_input.send_keys("R$3,49")
time.sleep(1)

#clica no botão de Cadastrar
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()


#aguarda um momento para visualizar o resultado (em uma aplicação real, você verificaria a resposta)
time.sleep(8)

#fecha o navegador
#driver.quit