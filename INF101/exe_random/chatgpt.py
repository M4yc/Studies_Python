from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Iniciar o navegador Opera GX
driver = webdriver.Opera(executable_path=r'C:\caminho\para\operadriver_win64.exe')  # Substitua pelo caminho correto do operadriver

# URL do site do supermercado
url = "https://amantino.marketmine.com.br/principal"

# Abrir a página
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
