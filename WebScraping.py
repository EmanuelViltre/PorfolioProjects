from bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get('https://www.mercadolibre.com.ar/smart-tv-samsung-series-5-un43t5300agczb-led-full-hd-43-220v-240v/p/MLA17291290?pdp_filters=category:MLA1002#searchVariation=MLA17291290&position=6&search_layout=stack&type=product&tracking_id=629e21d7-5fd5-46e2-8505-ba979a0869a8')

soup = BeautifulSoup(url.content, "html.parser")
resultado = soup.find("span", {"class":"andes-money-amount__fraction"})
precioInicio_text = resultado.text
precioInicial = float(precioInicio_text)

precioDeseado = 60.000

if precioInicial < precioDeseado:
    print("Hay oferta")
else: 
    print("No hay oferta")