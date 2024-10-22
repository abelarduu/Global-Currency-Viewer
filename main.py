import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def get_currency_values() -> dict:
    """Obtém as cotações atuais de USD, EUR, GBP e JPY em relação ao BRL do Google."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
    
    urls = {
        "Dollar": "https://www.google.com/search?q=cotacao+dolar",
        "Euro": "https://www.google.com/search?q=cotacao+euro",
        "Libra": "https://www.google.com/search?q=cotacao+libra",
        "Iene": "https://www.google.com/search?q=cotacao+iene"
    }
    
    values = {
        "Real": 1.00,
        "Dollar": None,
        "Euro": None,
        "Libra": None,
        "Iene": None
    }
  
    for currency, url in urls.items():
        response = requests.get(url, headers=headers)
        site = BeautifulSoup(response.text, "html.parser")
        value_tag = site.find("span", class_="DFlfde SwHCTb")
        # Convertendo o valor capturado de string em float
        values[currency] = float(value_tag.text.replace(',', '.'))

    pd.DataFrame()
    return values


def plot_currency_data(currency):
    """Plota os dados das cotações em um gráfico de barras, linha, e exibe o valor do USD."""
    # Definindo valores
    currency_names = list(currency.keys())
    currency_values = list(currency.values())
    
    # Definindo espaços para os gráficos
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Global-Currency-Visualizer')

    # Padronizando o grid em todos os subplots
    for ax in axs.flat:
        ax.grid(axis='y')
    axs[0, 0].axis('off')
    
    # Adicionando gráficos em cada posição específica dos subplots
    axs[0, 0].text(0.5, 0.5, f"Valor:\n{currency['Libra']} R$", ha='center', va='center', size=20)
    axs[0, 1].pie(currency_values, labels=currency_names, autopct='%1.1f%%', startangle=140)
    axs[1, 0].plot(currency_names, currency_values, marker='o', color= 'orange')
    axs[1, 1].bar(currency_names, currency_values)
    
    # Ajustando layout para evitar sobreposições 
    # Mostra os gráficos na tela
    plt.tight_layout()
    plt.show()

# Pegando os valores das moedas e plotando os gráficos
currency = get_currency_values()
plot_currency_data(currency)
