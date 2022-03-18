#!/usr/bin/env python
# coding: utf-8

# In[48]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[49]:


website = "https://www.coingecko.com/en"


# In[50]:


response = requests.get(website)


# In[51]:


response.status_code


# In[52]:


soup = BeautifulSoup(response.content, 'html.parser')


# In[53]:


#soup


# In[54]:


results = soup.find('table', {'class':'table-scrollable'}).find('tbody').find_all('tr')


# In[55]:


len(results)


# In[56]:


results[0].find('a', {'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip()


# In[94]:


results[0].find('td',{'class':'td-price price text-right pl-0'}).get_text().strip()


# In[58]:


results[0].find('td',{'class':'td-change1h change1h stat-percent text-right col-market'}).get_text().strip()


# In[59]:


results[0].find('td',{'class':'td-change24h change24h stat-percent text-right col-market'}).get_text().strip()


# In[60]:


results[0].find('td',{'class':'td-change7d change7d stat-percent text-right col-market'}).get_text().strip()


# In[61]:


results[0].find('td',{'class':'td-liquidity_score lit text-right col-market'}).get_text().strip()


# In[62]:


results[0].find('td',{'class':'td-market_cap cap col-market cap-price text-right'}).get_text().strip()


# In[110]:


name = []
price = []
change_1h = []
change_24h = []
change_7d = []
volume_24h = []
market_cap = []

for result in results:
    
    try:
        name.append(result.find('a', {'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
    except:
        name.append('n/a')
    
    try:
        price.append(result.find('td', {'class':'td-price price text-right pl-0'}).get_text().strip())
    except:
        price.append('n/a')
    
    try:
        change_1h.append(result.find('td', {'class':'td-change1h change1h stat-percent text-right col-market'}).get_text().strip())
    except:
        change_1h.append('n/a')
    
    try:
        change_24h.append(result.find('td', {'class':'td-change24h change24h stat-percent text-right col-market'}).get_text().strip())
    except:
        change_24h.append('n/a')
    
    try:
        change_7d.append(result.find('td', {'class':'td-change7d change7d stat-percent text-right col-market'}).get_text().strip())
    except:
        change_7d.append('n/a')
        
    try:
        volume_24h.append(result.find('td', {'class':'td-liquidity_score lit text-right col-market'}).get_text().strip())
    except:
        volume_24h.append('n/a')
        
    try:
        market_cap.append(result.find('td', {'class':'td-market_cap cap col-market cap-price text-right'}).get_text().strip())
    except:
        market_cap.append('n/a')


# In[111]:


crypto_df = pd.DataFrame({'Coin':name, 'Price':price, 'Change_1h':change_1h, 'Change_24h':change_24h, 'Change_7d':change_7d, 'Volume_24':volume_24h, 'Market Cap':market_cap})


# In[112]:


crypto_df


# In[113]:


crypto_df.to_excel('single_page_crypto.xlsx', index=False)


# In[117]:


name = []
price = []
change_1h = []
change_24h = []
change_7d = []
volume_24h = []
market_cap = []

for i in range(1,11): 
    
    website_pagination = 'https://www.coingecko.com/?page=' + str(i)
    
    response = requests.get(website_pagination)
    
    soup = BeautifulSoup(response.content, 'html.parser') 
    
    results = soup.find('table', {'class':'table-scrollable'}).find('tbody').find_all('tr')
    
    for result in results:
    
        try:
            name.append(result.find('a', {'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
        except:
            name.append('n/a')

        try:
            price.append(result.find('td', {'class':'td-price price text-right pl-0'}).get_text().strip())
        except:
            price.append('n/a')

        try:
            change_1h.append(result.find('td', {'class':'td-change1h change1h stat-percent text-right col-market'}).get_text().strip())
        except:
            change_1h.append('n/a')

        try:
            change_24h.append(result.find('td', {'class':'td-change24h change24h stat-percent text-right col-market'}).get_text().strip())
        except:
            change_24h.append('n/a')

        try:
            change_7d.append(result.find('td', {'class':'td-change7d change7d stat-percent text-right col-market'}).get_text().strip())
        except:
            change_7d.append('n/a')

        try:
            volume_24h.append(result.find('td', {'class':'td-liquidity_score lit text-right col-market'}).get_text().strip())
        except:
            volume_24h.append('n/a')

        try:
            market_cap.append(result.find('td', {'class':'td-market_cap cap col-market cap-price text-right'}).get_text().strip())
        except:
            market_cap.append('n/a')

    


# In[121]:


crypto_df = pd.DataFrame({'Coin':name, 'Price':price, 'Change_1h':change_1h, 'Change_24h':change_24h, 'Change_7d':change_7d, 'Volume_24':volume_24h, 'Market Cap':market_cap})


# In[122]:


crypto_df


# In[123]:


crypto_df.to_excel('multiple_page_crypto.xlsx', index=False)


# In[ ]:




