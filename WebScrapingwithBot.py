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
    
def telegram_bot_sendtext(bot_message):
    
    bot_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    #Telegram Search,  BotFather, /start, New_bot, Setup_bot, Token. (for security proposes I don't show my token.)
    bot_chatID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    #bot_chatID = 'Open a new tab with your browser, enter https://api.telegram.org/bot<yourtoken>/getUpdates , replace <yourtoken> with your API token, press enter and you should see something like this'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

if precioInicial < precioDeseado
    test = telegram_bot_sendtext(f"Oferta! {'$'(precioInicial")}\nEnlance: https://www.mercadolibre.com.ar/smart-tv-samsung-series-5-un43t5300agczb-led-full-hd-43-220v-240v/p/MLA17291290?pdp_filters=category:MLA1002#searchVariation=MLA17291290&position=6&search_layout=stack&type=product&tracking_id=629e21d7-5fd5-46e2-8505-ba979a0869a8") 
else:
    test = telegram_bot_sendtext("No hay oferta")
