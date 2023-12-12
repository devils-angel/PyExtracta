from bs4 import BeautifulSoup
import requests
import pandas as pd

for page in range(1, 51):
    url = "https://www.jumia.co.ke/all-products/" + "?page=" + str(page)+"#catalog-listing"
    url = requests.get(url)
    jsoup = BeautifulSoup(url.content, 'html.parser')
    products = jsoup.find_all('div', class_='info')

    for product in products:
        Name = product.find('h3', class_="name").text.replace('\n', '')
        Price = product.find('div', class_="prc").text.replace('\n', '')
        try:
            Rating = product.find('div', class_='stars _s').text.replace('\n', '')
        except:
            Rating = None
        info = [Name, Price, Rating]
        print(info)
        df = pd.DataFrame({'Product Name':Name,'Price':Price,'Rating':Rating},index=[0]) 

        df.to_csv('products.csv', index=False, encoding='utf-8',mode='a')