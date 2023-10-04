from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configurar o driver do Selenium (você precisa baixar o driver adequado para o seu navegador)
driver = webdriver.Chrome(executable_path='/caminho/para/o/chromedriver')  # Substitua pelo caminho correto do chromedriver

# URL do site do supermercado
url = "https://amantino.marketmine.com.br/principal"

# Iniciar o navegador e abrir a página
driver.get(url)

# Encontrar o campo de pesquisa e inserir "pizza"
search_box = driver.find_element_by_name("q")
search_box.send_keys("pizza")
search_box.send_keys(Keys.RETURN)

# Aguardar um momento para que a página carregue os resultados
time.sleep(5)

# Encontrar e extrair informações sobre os produtos
product_elements = driver.find_elements_by_class_name("product")

for product in product_elements:
    product_name = product.find_element_by_class_name("product-name").text
    product_price = product.find_element_by_class_name("product-price").text
    print(f"Produto: {product_name}")
    print(f"Preço: {product_price}")

# Fechar o navegador
driver.quit()
