#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np


# In[4]:


df = pd.read_csv('C:\\Users\\VIKAS SINGH\\Downloads\\BigMartSales.csv')


# In[6]:


df.head()


# In[7]:


df.shape


# In[8]:


df.columns


# In[10]:


type(df.columns)


# In[11]:


df['Item_Identifier']


# In[18]:


df[['Item_Identifier','Item_Outlet_Sales']]


# In[19]:


df[['Item_Identifier','Item_Fat_Content','Item_MRP']]


# In[20]:


df.iloc[:5]


# In[21]:


df.iloc[10:20]


# In[22]:


df.iloc[100:110,:5]


# In[23]:


df.iloc[100:110,5:]


# In[24]:


df.columns


# In[27]:


df['Outlet_Establishment_Year'] == 2002


# In[28]:


df[ df['Outlet_Establishment_Year'] == 2002 ]


# In[29]:


#First 2 columns of last 10 rows.

df.iloc[-10:,:2]


# In[31]:


df.tail(10).iloc[:,:2]


# In[40]:


df.sort_values(by='Outlet_Establishment_Year')


# In[41]:


new_df = df.sort_values(by='Outlet_Establishment_Year')

new_df is df


# In[42]:


df.sort_values(by='Outlet_Establishment_Year',ascending=False)


# In[43]:


min(df['Outlet_Establishment_Year'])


# In[44]:


max(df['Outlet_Establishment_Year'])


# In[47]:


df.sort_values(by='Outlet_Establishment_Year',inplace=True)


# In[48]:


df    #Inplace sorting has changed the original dataframe. Important thing is original indexes are preserved.


# In[49]:


#Since original indexes are preserved, hence we can get the original dataframe.

df.sort_index()


# In[50]:


df.sort_values(by=['Outlet_Establishment_Year','Outlet_Size'])


# In[51]:


all(df['Outlet_Size'] == 'Medium')


# In[52]:


df.dropna(how='any')


# In[5]:


df2 = pd.read_csv('C:\\Users\\VIKAS SINGH\\Downloads\\BigMartSales_Test.csv')


# In[54]:


df2.head()


# In[55]:


df2.dropna(how='any')


# In[57]:


result = pd.concat([df,df2])


# In[59]:


result.shape


# In[60]:


result = pd.concat([df,df2],keys=['X','Y'])


# In[61]:


result.shape


# In[62]:


result.loc


# In[63]:


result.loc['X']


# In[64]:


result.loc['Y']


# In[65]:


result


# In[69]:


df.sort_index(inplace=True)


# In[70]:


result = pd.concat([df,df2],keys=['X','Y'])


# In[71]:


result


# In[72]:


result = pd.concat([df,df2])


# In[73]:


result


# In[74]:


result.sort_index()


# In[75]:


result.iloc[:2]


# In[76]:


result.sort_index(inplace=True)


# In[77]:


result.iloc[:2]


# In[79]:


result = pd.concat([df,df2],keys=['X','Y'])


# In[80]:


result.sort_index(inplace=True)


# In[81]:


result.loc['X']


# In[82]:


#Outer Join - Default one. Union of all dataframes

result = pd.concat([df,df2], axis=1, sort=False)


# In[83]:


result.head()


# In[84]:


result.shape


# In[85]:


result.columns


# In[86]:


#default value of axis argument is 0. It means concatenation happens index wise - One below the other. Argument 1 specifies
#the concatenation happens along the columns - Side by Side.


# In[87]:


result = pd.concat([df,df2], axis=1, join='inner')


# In[88]:


result.shape


# In[89]:


result.head()


# In[94]:


result.iloc[0,]


# In[95]:


df.iloc[0,]


# In[131]:


result = pd.concat([df,df2], axis=1)


# In[132]:


result


# df.shape - 8523 X 12
# df2.shape - 5681 X 11
# 
# axis{0/’index’, 1/’columns’}, default 0
# The axis to concatenate along.
# 
# join{‘inner’, ‘outer’}, default ‘outer’
# How to handle indexes on other axis (or axes) - Union or Intersection
# 
# Axis    Join    Dimension    Result
# ----    ----    ---------    ------
#  0      Outer   14204 X 12   One below other and all columns taken (union). Union will be same as df. Last column of df2 - NaN
#  0      Inner   14204 X 11   One below other and intersection of columns. Intersection will be same as df2.
#  1      Outer   8523 X 23    Side by side and all rows taken (union). For extra rows of df2, NaN will be added.
#  1      Inner   5681 X 23    Side by side and intersection of rows taken.

# In[149]:


df_a = pd.DataFrame({'subject_id': [1,2,3,4,5],
                     'first_name': ['Alex','Amy','Allen','Alice','Ayoung'],
                     'last_name': ['Anderson','Ackerman','Ali','Aoni','Atiches']})
df_a


# In[150]:


df_b = pd.DataFrame({'subject_id': [4,5,6,7,8],
                     'first_name': ['Billy','Brian','Bran','Bryce','Betty'],
                     'last_name': ['Bonder','Black','Balwner','Brice','Btisan']})
df_b


# In[151]:


df_c = pd.DataFrame({'subject_id': [1,2,3,4,5,7,8,9,10,11],
                    'test_id': [51,15,15,61,16,14,15,60,65,16]})
df_c


# In[143]:


pd.merge(df_a,df_c,on='subject_id')      #Similar to SQL join


# In[147]:


pd.merge(df_a,df_b,on='subject_id')    #See column names have been modified.


# how{‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘inner’
# Type of merge to be performed.
# 
# left: use only keys from left frame, similar to a SQL left outer join; preserve key order.
# 
# right: use only keys from right frame, similar to a SQL right outer join; preserve key order.
# 
# outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.
# 
# inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys.

# In[148]:


pd.merge(df_a,df_b,on='subject_id',how='outer')


# In[152]:


pd.merge(df_a,df_b,on='subject_id',how='left')


# In[153]:


pd.merge(df_a,df_b,on='subject_id',how='right')


# In[156]:


df.apply(lambda x : x)     #x refers to each row


# In[157]:


df.apply(lambda x : x[0])


# In[159]:


df.apply(lambda x : x , axis=1)           


# axis=0 in apply refers to evaluating row by row.
# axis=1 in apply refers to evaluating column by column.

# In[161]:


df.apply(lambda x : x['Outlet_Establishment_Year'], axis=1)


# In[178]:


def check_price(price):
    if price > 1000:
        return True
    else:
        return False
    
df['Item_Outlet_Sales'].apply(lambda x : check_price(x))


# In[179]:


#Surprisingly even this works

df['Item_Outlet_Sales'].apply(check_price)


# In[180]:


df


# In[185]:


df.groupby('Item_Type').first()


# In[187]:


df.groupby('Item_Type').Item_MRP.mean()


# In[7]:


df.groupby(['Item_Type','Item_Fat_Content']).first()


# In[8]:


df.groupby(['Item_Type','Item_Fat_Content']).Item_MRP.mean()


# In[9]:


pd.crosstab(df['Outlet_Size'],df['Outlet_Location_Type'],margins=True)


# In[13]:


pd.pivot_table(df,index=['Outlet_Establishment_Year'])     #Default operation is mean


# In[12]:


pd.pivot_table(df,index=['Outlet_Establishment_Year'],values='Item_Outlet_Sales')     #Default operation is mean


# In[15]:


pd.pivot_table(df,index=['Outlet_Establishment_Year','Outlet_Location_Type','Outlet_Size'])     #Default operation is mean


# In[17]:


pd.pivot_table(df,index=['Outlet_Establishment_Year','Outlet_Location_Type','Outlet_Size'],values=['Item_Outlet_Sales'],
              aggfunc=[np.mean,np.median,np.min,np.max,np.std])     #Default operation is mean


# In[ ]:




