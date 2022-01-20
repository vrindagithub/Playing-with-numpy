#!/usr/bin/env python
# coding: utf-8

# 
# # 2: Evaluate the Summer Olympics, London 2012 dataset
# 

# #### 1: View and add the dataset

# In[3]:


#Import the necessary library

import numpy as np


# In[4]:


#Manually add the Summer Olympics, London 2012 dataset as arrays

country = np.array(['Great Britain','China', 'Russia','United States','Korea','Japan','Germany'])
country_code = np.array(['GBR','CHN','RUS','US','KOR','JPN','GER'])
year = np.array([2012,2012,2012,2012,2012,2012,2012])
gold = np.array([29,38,24,46,13,7,11])
silver = np.array([17,28,25,28,8,14,11])
bronze = np.array([19,22,32,29,7,17,14])


# #### Find the country with maximum gold medals

# In[14]:


#Use the argmax() method to find the highest number of gold medals

highest_gold = gold.argmax()
highest_gold


# In[15]:


#Print the name of the country

country_with_highest_gold = country[highest_gold]
country_with_highest_gold


# #### Find the countries with more than 20 gold medals

# In[16]:


#Use Boolean indexing technique to find the required output

print(country[gold>20])


# #### Evaluate the dataset and print the name of each country with its gold medals and total number of medals

# In[8]:


#Use a for loop to create the required output

for i in range(len(country)):
    gold_medal = gold[i]
    countryy = country[i]
    total_medal = bronze[i] + silver[i] +gold[i]
    print('{} ,gold medals - {}, total medals - {}'.format(countryy , gold_medal, total_medal))


# In[ ]:




