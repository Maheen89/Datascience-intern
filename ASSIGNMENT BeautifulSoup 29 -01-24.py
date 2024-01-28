#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# ##  Question number 01

# In[4]:


from bs4 import BeautifulSoup
import requests


# In[11]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')

page


# In[19]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[10]:


page = requests.get('https://en.wikipedia.org/wiki/Main_page')

page


# In[13]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')

page


# In[15]:


soup = BeautifulSoup(page.content)

soup


# In[16]:


header_tags = soup.find_all(["h1","h2","h3","h4","h5","h6"])

header_tags


# In[17]:


header_text = [tag.get_text()for tag in header_tags]

header_text


# In[27]:


df= pd.DataFrame(header_text,columns=["Header"])
print(df)


# ## question number 02

# In[1]:


from bs4 import BeautifulSoup
import pandas as pd
import requests


# In[2]:


page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')

page


# In[3]:


soup = BeautifulSoup(page.content)

soup


# In[ ]:


can not scrap as response is greater than 200


# ## Question number 03

# In[ ]:


from bs4 import BeautifulSoup
import requests


# In[5]:


page = requests.get('https://icc-cricket.com')


# In[6]:


page


# In[7]:


soup = BeautifulSoup(page.content)
soup


# In[ ]:





# In[ ]:





# ## question number 04

# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


page = requests.get('https://icc-cricket.com')


# In[5]:


page


# In[6]:


soup = BeautifulSoup(page.content)
soup


# In[10]:


teams = soup.find('div',class_="si-table-row")


# In[11]:


teams


# In[12]:


team = []

for i in soup.find_all('div',class_="si-table-row"):
    team.append(i.text)
    
team


# In[ ]:





# ## Question number 05

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup

import requests


# In[3]:


page = requests.get('https://www.cnbc.com/word/?region=world')

page


# In[ ]:


can not scrap as response is greater than 200


# In[ ]:





# In[ ]:





# ## question number 06

# In[8]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[11]:


from bs4 import BeautifulSoup
import requests


# In[12]:


page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')

page


# In[13]:


soup = BeautifulSoup(page.content)
soup


# In[14]:


author = soup.find('span',class_="sc-1w3fpd7-0 dnCnAO")

author


# In[15]:


author.text


# In[16]:


paper_title = []
for i in soup.find_all(class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    paper_title.append(i.text)
    
paper_title


# In[19]:


published_date = soup.find('span',class_="sc-1thf9ly-2 dvggWt")

published_date


# In[20]:


published_date.text


# In[21]:


author = []
for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    author.append(i.text)
    
author


# In[22]:


published_date = []

for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    published_date.append(i.text)
    
published_date


# In[23]:


paper_url = []

for i in soup.find_all(class_="sc-1fdbg4d-0 GaNmj"):
    paper_url.append("sc-1fdbg4d-0 GaNmj")

paper_url


# In[24]:


import pandas as pd

df = pd.DataFrame({'published_date':published_date,'author':author})
df


# In[ ]:





# In[ ]:





# In[ ]:





# ## question number 07

# In[26]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[27]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[28]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[29]:


page


# In[30]:


soup = BeautifulSoup(page.content)
soup


# In[31]:


restaurant_name = soup.find('div',class_="restnt-info cursor")

restaurant_name


# In[32]:


restaurant_name.text


# In[33]:


loc = soup.find('div',class_="restnt-loc ellipsis")

loc


# In[34]:


loc.text


# In[35]:


ratings = soup.find('div',class_="restnt-rating rating-4")
ratings


# In[36]:


ratings.text


# In[37]:


cuisine = soup.find(href="/delhi-restaurants/north-indian-cuisine")
cuisine


# In[38]:


cuisine.text


# In[39]:


names = []

for i in soup.find_all('div',class_="restnt-info cursor"):
    names.append(i.text)
    
names    


# In[40]:


location = []

for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
    
location


# In[41]:


ratings = []

for i in soup.find_all('div',class_="restnt-rating rating-4"):
    ratings.append(i.text)
    
ratings


# In[42]:


images = []

for i in soup.find_all("img",class_="no-img"):
    images.append(i['data-src'])
images


# In[43]:


cuisine = []

for i in soup.find_all(href="/delhi-restaurants/north-indian-cuisine"):
    cuisine.append(i.text)
    
cuisine


# In[47]:


import pandas as pd

df = pd.DataFrame({'names':names,'Location':location,'Ratings':ratings,'Images_url':images})
df


# In[ ]:




