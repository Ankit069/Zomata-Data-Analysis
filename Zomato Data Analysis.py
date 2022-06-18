#!/usr/bin/env python
# coding: utf-8

# # Import Basic Libraries

# In[41]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[42]:


#Load the dataset
df=pd.read_csv("zomato.csv",encoding='latin-1')


# In[43]:


df.head()


# # Exploratery Data Analysis

# In[44]:


#Data Cleaning
df.isnull().sum()


# In[45]:


df.columns


# In[46]:


df.info()


# In[47]:


df.describe().T


# In[48]:


df.isnull().sum()


# In[49]:


#Drop the null values
df.dropna(subset=['Cuisines'],inplace=True)


# In[50]:


#Load another Dataset
df_country=pd.read_csv("Country-Code.csv")


# In[51]:


df_country.head()


# In[52]:


#Rename the CountryCode to Country Code ,Tomerge both the dataset
df.rename(columns={"CountryCode":"Country Code"},inplace=True)


# In[53]:


#Merging datasets
final_df=pd.merge(df,df_country,on="Country Code",how='left')


# In[54]:


final_df.head()


# In[55]:


final_df.columns


# # Which are the Top 3 coutries using Zomato

# In[56]:


country_name=final_df.Country.value_counts().index


# In[57]:


country_name


# In[58]:


country_val=final_df.Country.value_counts().values


# In[59]:


country_val


# In[60]:


#top 3 countries uses zomato
plt.figure(figsize=(8,8))
sns.set(font_scale=2)
plt.pie(country_val[:3],labels=country_name[:3],autopct="%1.2f%%")
plt.show()


# **zomato maximum records or transaction are from india**

# # How the Aggregate rating is associated with Rating Color and Rating text

# In[61]:


final_df.groupby(["Aggregate rating","Rating color","Rating text"]).size()


# In[62]:


final_df.groupby(["Aggregate rating","Rating color","Rating text"]).size().reset_index()


# In[63]:


ratings=final_df.groupby(["Aggregate rating","Rating color","Rating text"]).size().reset_index().rename(columns={0:"Rating count"})


# In[64]:


plt.figure(figsize=(16,8))
sns.set_style('dark')
sns.set(font_scale=1.3)
sns.barplot(x="Aggregate rating",y="Rating count",hue="Rating color",palette=["white","red","orange","yellow","green","green"],data=ratings)
plt.show()


# **Most of the people did not rated**

# # Which rating color is mostly used in this dataset

# In[65]:


plt.figure(figsize=(8,8))
sns.countplot(x="Rating color",data=ratings,palette=["white","red","orange","yellow","green","green"])


# **Orange colour is mostly used in Rating color**
# 
# **Most of the people rated 'Average' or between 2.9 to 3.4**

# # Which Country gave maximum 0 ratings

# In[66]:


final_df[final_df["Rating color"]=="White"].groupby("Country").size().reset_index()


# **maximun no. of 0 rating is from india**

# In[67]:


final_df.head(2)


# In[68]:


final_df.columns


# # Show the Currencies owned by each Countrty

# In[69]:


final_df.groupby(["Country",'Currency']).size().reset_index()


# # Which country has online delivery 

# In[70]:


final_df[final_df['Has Online delivery']=="Yes"].Country.value_counts()


# # Which City has maximum restaurants in India

# In[71]:


final_df.City.value_counts().index


# In[72]:


city_values=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index


# In[73]:


plt.figure(figsize=(10,10))
plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')
plt.show()


# **New Delhi has maximum Restaurants**

# In[74]:


df.corr()


# In[75]:


final_df['Locality'].unique()


# # Which country has cheapest price of foods

# In[76]:


plt.figure(figsize=(15,15))
sns.set(font_scale=1.5)
sns.barplot(x='Country',y='Price range',data=final_df,ci=None)
plt.xticks(rotation=90)
plt.show()


# **India has cheapest price of food**

# In[77]:


#which locality has highest price range


# # From which Locality in Delhi maximum hotels are listed in Zomato

# In[78]:


Delhi=final_df[final_df["City"]=="New Delhi"]


# In[79]:


plt.figure(figsize=(8,8))
sns.barplot(x=Delhi.Locality.value_counts().head(20), y=Delhi.Locality.value_counts().head(20).index)
plt.title('Resturants Listing on Zomato')
plt.show()


# **Connaught Place has maximum no. of Restaurants in Delhi**

# # Which Kind of cuisiens are famous in Connaught Place

# In[80]:


## Fetching the resturants having 'Excellent' rating
ConnaughtPlace = Delhi[(Delhi.Locality.isin(['Connaught Place'])) & (Delhi['Rating text'].isin(['Excellent']))]
ConnaughtPlace = ConnaughtPlace.Cuisines.value_counts().reset_index()

## Extracing all the cuisens in a single list
cuisien = []
for x in ConnaughtPlace['index']: 
  cuisien.append(x)
cuisien


# # Result

# **Advice to other restaurants**
# 
# **Include 'Continental, Italian, Asian, Indian', 'North Indian', 'Ice Cream' In the Cuisines to increase their Sale**

# # Thank You
